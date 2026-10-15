"""Check the deck's bibliography with the level 3 method: python -m bibcheck.run

Code finds every work in the official records (OpenAlex, DBLP, arXiv, Crossref, OpenLibrary, the web), downloads
abstract, full text or page, and looks for the claim's numbers and phrases; a jury of three models from three companies
reads the passages code found and decides, by majority, whether the source supports the claim.
Writes bibcheck/REPORT.md and bibcheck/result.json.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import fitz
import httpx
from rapidfuzz import fuzz

from core.sources import HEADERS
from evaluation.verify import fetch_page, norm
from evaluation.judge_llm import _key
from benchmark.scholar import _cached_get, _openalex_record
from benchmark.verifier import _web_search

from .data import CLAIMS, REFS

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
JURY = [("deepseek/deepseek-v4-pro", "DeepSeek V4 Pro"), ("qwen/qwen3.7-plus", "Qwen3.7 Plus"),
        ("google/gemini-3.1-flash-lite", "Gemini 3.1 Flash-Lite")]
VENUE_ALIASES = {"NeurIPS": ["neurips", "neural information processing"], "ICLR": ["iclr", "learning representations"],
                 "ICML": ["icml", "machine learning"], "EMNLP": ["emnlp", "empirical methods"],
                 "NAACL": ["naacl", "north american chapter"], "STOC": ["stoc", "theory of computing"]}
_sem = asyncio.Semaphore(6)
_arxiv_lock = asyncio.Lock()


def title_score(a: str, b: str) -> float:
    return fuzz.token_set_ratio(norm(a), norm(b))


async def openalex(client, title):
    d = await _cached_get(client, "https://api.openalex.org/works", {"search": title, "per-page": 5})
    return [_openalex_record(w) for w in (d or {}).get("results", [])]


async def crossref_any(client, title):
    d = await _cached_get(client, "https://api.crossref.org/works", {
        "query.bibliographic": title, "rows": 5, "select": "DOI,title,author,container-title,issued,abstract"})
    out = []
    for m in ((d or {}).get("message") or {}).get("items", []):
        parts = ((m.get("issued") or {}).get("date-parts") or [[0]])[0]
        out.append({"doi": (m.get("DOI") or "").lower(), "title": " ".join(m.get("title") or []), "year": parts[0] if parts else 0,
                    "venue": " ".join(m.get("container-title") or []), "abstract": re.sub(r"<[^>]+>", " ", m.get("abstract", "")),
                    "authors": [" ".join(x for x in (a.get("given"), a.get("family")) if x) for a in (m.get("author") or [])]})
    return out


_render_lock = asyncio.Lock()


async def render(url: str) -> str:
    """Open a page in a real headless browser, for sites that refuse plain HTTP clients."""
    from playwright.async_api import async_playwright
    async with _render_lock, async_playwright() as p:
        b = await p.chromium.launch()
        try:
            pg = await b.new_page()
            await pg.goto(url, wait_until="domcontentloaded", timeout=45000)
            await pg.wait_for_timeout(3000)
            return await pg.evaluate("() => document.body.innerText")
        except Exception:
            return ""
        finally:
            await b.close()


async def claim_pages(client, claim, ref) -> list[dict]:
    """Extra evidence for one claim: web searches aimed at the primary source; the preferred domain goes first."""
    prefer = claim.get("prefer")
    queries = list(claim.get("extra", [])) + ([ref.get("query") or ref["title"]] if prefer else [])
    pages, seen = [], set()
    for q in queries:
        urls = re.findall(r"\| (https?://\S+) \|", await _web_search(client, q))
        urls.sort(key=lambda u: 0 if prefer and prefer in u else 1)
        for url in urls[:5]:
            if url in seen:
                continue
            seen.add(url)
            rec = await fetch_page(client, url)
            text = (rec.get("text") or "") if rec.get("status") == 200 else ""
            if len(text) < 500 and prefer and prefer in url:
                text = await render(url)
            low = norm(text)
            if text and ((prefer and prefer in url) or any(norm(n) in low for n in claim["needles"])):
                pages.append({"src": f"web, busca dirigida: {url}", "text": text})
    return pages


async def dblp(client, title):
    d = await _cached_get(client, "https://dblp.org/search/publ/api", {"q": title, "format": "json", "h": 5})
    hits = (((d or {}).get("result") or {}).get("hits") or {}).get("hit") or []
    out = []
    for h in hits:
        i = h.get("info", {})
        au = i.get("authors", {}).get("author", [])
        au = [au] if isinstance(au, dict) else au
        out.append({"title": i.get("title", ""), "venue": i.get("venue", ""), "year": int(i.get("year", 0) or 0),
                    "authors": [a.get("text", "") for a in au], "url": i.get("ee", "")})
    return out


async def arxiv(client, title):
    f = CACHE / f"arxiv_{hashlib.sha1(title.encode()).hexdigest()}.xml"
    if f.exists():
        text = f.read_text(encoding="utf-8")
    else:
        q = re.sub(r"[^\w\s]", " ", title)
        async with _arxiv_lock:   # arXiv asks for one request every 3 seconds
            r = await client.get("http://export.arxiv.org/api/query", params={"search_query": f'ti:"{q}"', "max_results": 3},
                                 timeout=60)
            await asyncio.sleep(3)
        text = r.text if r.status_code == 200 else ""
        if text:
            f.write_text(text, encoding="utf-8")
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    try:
        for e in ET.fromstring(text).findall("a:entry", ns) if text else []:
            out.append({"title": " ".join(e.findtext("a:title", "", ns).split()), "abstract": " ".join(e.findtext("a:summary", "", ns).split()),
                        "id": e.findtext("a:id", "", ns).rsplit("/", 1)[-1], "year": int(e.findtext("a:published", "0", ns)[:4]),
                        "authors": [a.findtext("a:name", "", ns) for a in e.findall("a:author", ns)]})
    except ET.ParseError:
        pass
    return out


async def arxiv_fulltext(client, arxiv_id):
    f = CACHE / f"pdf_{arxiv_id.replace('/', '_')}.txt"
    if f.exists():
        return f.read_text(encoding="utf-8")
    async with _arxiv_lock:
        r = await client.get(f"https://arxiv.org/pdf/{arxiv_id}", timeout=120)
        await asyncio.sleep(3)
    if r.status_code != 200 or not r.content.startswith(b"%PDF"):
        return ""
    with fitz.open(stream=r.content, filetype="pdf") as doc:
        text = "\n".join(page.get_text() for page in doc)
    f.write_text(text, encoding="utf-8")
    return text


async def openlibrary(client, title, author):
    d = await _cached_get(client, "https://openlibrary.org/search.json", {"title": title, "author": author, "limit": 5})
    return [{"title": x.get("title", ""), "authors": x.get("author_name", []), "years": x.get("publish_year", []),
             "first_year": x.get("first_publish_year"), "publishers": x.get("publisher", [])[:30]} for x in (d or {}).get("docs", [])]


async def web_pages(client, query, title, k=4):
    """Search the web, open the top results, keep the pages that carry the work's title (or the quoted phrase)."""
    lines = await _web_search(client, query)
    urls = re.findall(r"\| (https?://\S+) \|", lines)
    pages = []
    for url in urls[:6]:
        rec = await fetch_page(client, url)
        text = (rec.get("text") or "") if rec.get("status") == 200 else ""
        if text and (fuzz.partial_ratio(norm(title), norm(text)) >= 85 or len(pages) < 1):
            pages.append({"url": url, "text": text, "has_title": fuzz.partial_ratio(norm(title), norm(text)) >= 85})
        if len(pages) >= k:
            break
    return pages, lines


def venue_ok(expected: str, found: list[str]) -> bool:
    keys = VENUE_ALIASES.get(expected, [norm(expected)])
    return any(any(k in norm(v) for k in keys) for v in found if v)


async def resolve(client, ref) -> dict:
    async with _sem:
        r = {"id": ref["id"], "kind": ref["kind"], "expected": {k: ref[k] for k in ("title", "authors", "year", "venue")},
             "texts": [], "found": {}}
        first = norm(ref["authors"][0])
        if ref["kind"] == "paper":
            oa, db, ax, cr = await asyncio.gather(openalex(client, ref["title"]), dblp(client, ref["title"]),
                                                  arxiv(client, ref["title"]), crossref_any(client, ref["title"]))
            best = lambda xs: max(xs, key=lambda x: title_score(x["title"], ref["title"]), default=None)
            b_oa, b_db, b_ax, b_cr = best(oa), best(db), best(ax), best(cr)
            hits = [x for x in (b_oa, b_db, b_ax, b_cr) if x and title_score(x["title"], ref["title"]) >= 90]
            r["found"] = {"openalex": b_oa and {k: b_oa[k] for k in ("title", "year", "venue", "doi")},
                          "dblp": b_db and {k: b_db[k] for k in ("title", "year", "venue")},
                          "arxiv": b_ax and {k: b_ax[k] for k in ("title", "year", "id")},
                          "crossref": b_cr and {k: b_cr[k] for k in ("title", "year", "venue", "doi")}}
            if b_cr and title_score(b_cr["title"], ref["title"]) >= 90 and b_cr.get("abstract", "").strip():
                r["texts"].append({"src": f"resumo (Crossref {b_cr['doi']})", "text": b_cr["abstract"]})
            if (not b_oa or title_score(b_oa["title"], ref["title"]) < 90) and b_cr and title_score(b_cr["title"], ref["title"]) >= 90:
                b_oa = {**b_cr, "abstract": ""}
            r["exists"] = bool(hits)
            r["author_ok"] = any(any(first in norm(a) for a in x.get("authors", [])) for x in hits)
            years = {x["year"] for x in hits if x.get("year")}
            r["year_ok"] = any(abs(y - ref["year"]) <= 1 for y in years)
            r["venue_ok"] = ref["venue"] == "arXiv" or venue_ok(ref["venue"], [x.get("venue", "") for x in hits])
            if b_oa and title_score(b_oa["title"], ref["title"]) >= 90 and b_oa.get("abstract"):
                r["texts"].append({"src": "resumo (OpenAlex)", "text": b_oa["abstract"]})
            if b_ax and title_score(b_ax["title"], ref["title"]) >= 90:
                r["texts"].append({"src": f"resumo (arXiv {b_ax['id']})", "text": b_ax["abstract"]})
                full = await arxiv_fulltext(client, b_ax["id"])
                if full:
                    r["texts"].append({"src": f"texto completo (arXiv {b_ax['id']})", "text": full})
            elif b_oa and b_oa.get("doi") and title_score(b_oa["title"], ref["title"]) >= 90:
                page = await fetch_page(client, f"https://doi.org/{b_oa['doi']}")
                if page.get("status") == 200 and page.get("text"):
                    r["texts"].append({"src": f"página da editora (doi {b_oa['doi']})", "text": page["text"]})
        elif ref["kind"] == "book":
            ol = await openlibrary(client, ref["title"].split(":")[0], ref["authors"][0])
            hits = [x for x in ol if title_score(x["title"], ref["title"].split(":")[0]) >= 90]
            r["found"] = {"openlibrary": hits[:2]}
            r["exists"] = bool(hits)
            r["author_ok"] = any(any(first in norm(a) for a in x["authors"]) for x in hits)
            r["year_ok"] = any(ref["year"] in (x["years"] or []) for x in hits)
            r["venue_ok"] = any(any(fuzz.partial_ratio(norm(ref["venue"]), norm(p)) >= 85 for p in x["publishers"]) for x in hits)
            pages, _ = await web_pages(client, ref["query"], ref["title"].split(":")[0])
            r["texts"] += [{"src": f"web: {p['url']}", "text": p["text"]} for p in pages]
        else:
            pages, lines = await web_pages(client, ref["query"], ref["title"])
            titled = [p for p in pages if p["has_title"]]
            r["found"] = {"web": [p["url"] for p in pages], "search": lines[:1500]}
            r["exists"] = bool(titled)
            joined = " ".join(norm(p["text"]) for p in titled)
            r["author_ok"] = any(norm(a) in joined for a in ref["authors"])
            r["year_ok"] = str(ref["year"]) in joined
            r["venue_ok"] = None
            r["texts"] += [{"src": f"web: {p['url']}", "text": p["text"]} for p in pages]
        return r


def find_needles(needles, texts):
    found = {}
    for n in needles:
        nn = norm(n)
        found[n] = next((t["src"] for t in texts if nn in norm(t["text"])), None)
    return found


def passages(needles, texts, cap=7000):
    out, used = [], 0
    for t in texts:
        if t["src"].startswith("resumo"):
            chunk = t["text"][:2500]
            out.append(f"[{t['src']}]\n{chunk}")
            used += len(chunk)
    for t in texts:
        low = t["text"].lower()
        for n in needles:
            for m in list(re.finditer(re.escape(n.lower()), low))[:2]:
                a, b = max(0, m.start() - 700), min(len(t["text"]), m.end() + 700)
                chunk = " ".join(t["text"][a:b].split())
                if used + len(chunk) > cap:
                    return "\n\n".join(out)
                out.append(f"[{t['src']}]\n...{chunk}...")
                used += len(chunk)
    if not out:
        for t in texts[:2]:
            chunk = " ".join(t["text"][:3000].split())
            out.append(f"[{t['src']}]\n{chunk}")
    return "\n\n".join(out)


JUDGE_SYSTEM = """# Conferente de citação

## Perfil
Você confere, para uma aula de pós-graduação, se uma fonte sustenta o que um slide afirma sobre ela. Seja estrito.

## Memória
Use só os trechos da fonte fornecidos (obtidos por código). Não use conhecimento próprio sobre a obra.

## Planejamento
1. Copie o trecho que decide.
2. Decida: "sustenta" (os trechos dizem isso, inclusive números e citações literais, admitida tradução fiel),
   "sustenta_em_parte" (parte é dita, ou o slide vai além, exagera ou distorce), "nao_sustenta" (os trechos dizem
   outra coisa ou o contrário), "trechos_insuficientes" (os trechos não tratam do ponto).
3. Se for citação traduzida, confira se a tradução é fiel.

## Ação
Sem ferramentas. Responda no esquema, em português."""
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["evidence", "verdict", "reason"],
          "properties": {"evidence": {"type": "string"},
                         "verdict": {"type": "string", "enum": ["sustenta", "sustenta_em_parte", "nao_sustenta", "trechos_insuficientes"]},
                         "reason": {"type": "string"}}}


async def judge(client, model, claim, ref, text):
    body = {"model": model, "temperature": 0, "reasoning": {"effort": "high"},
            "messages": [{"role": "system", "content": JUDGE_SYSTEM},
                         {"role": "user", "content": f"OBRA: {ref['expected']['title']} ({', '.join(ref['expected']['authors'])}, {ref['expected']['year']}, {ref['expected']['venue']})\n\nO SLIDE AFIRMA:\n{claim}\n\nTRECHOS DA FONTE:\n{text}"}],
            "response_format": {"type": "json_schema", "json_schema": {"name": "cite_check", "strict": True, "schema": SCHEMA}}}
    h = hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    f = CACHE / f"judge_{h}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    for attempt in range(4):
        try:
            r = await client.post("https://openrouter.ai/api/v1/chat/completions", json=body, timeout=300,
                                  headers={"Authorization": f"Bearer {_key()}", "X-Title": "LabIA bibcheck"})
            if r.status_code == 200:
                out = json.loads(r.json()["choices"][0]["message"]["content"])
                f.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
                return out
        except (httpx.HTTPError, KeyError, IndexError, TypeError, json.JSONDecodeError):
            pass
        await asyncio.sleep(5 * (attempt + 1))
    return {"evidence": "", "verdict": "erro", "reason": "o juiz não respondeu"}


async def main_async():
    CACHE.mkdir(parents=True, exist_ok=True)
    async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
        refs = {r["id"]: r for r in await asyncio.gather(*(resolve(client, ref) for ref in REFS))}
        results = []

        async def check(c):
            texts = [t for rid in c["refs"] for t in refs[rid]["texts"]]
            if c.get("extra") or c.get("prefer"):
                texts = await claim_pages(client, c, next(x for x in REFS if x["id"] == c["refs"][0])) + texts
            text = passages(c["needles"], texts)
            votes = await asyncio.gather(*(judge(client, m, c["claim"], refs[c["refs"][0]], text) for m, _ in JURY))
            labels = [v["verdict"] for v in votes]
            top = max(set(labels), key=labels.count)
            results.append({**c, "needles_found": find_needles(c["needles"], texts), "votes": [
                {"judge": name, **v} for (_, name), v in zip(JURY, votes)],
                "verdict": top if labels.count(top) >= 2 else "dividido", "sources_read": [t["src"] for t in texts]})

        await asyncio.gather(*(check(c) for c in CLAIMS))
    results.sort(key=lambda x: x["id"])
    for r in refs.values():
        r["texts"] = [t["src"] for t in r["texts"]]
    (HERE / "result.json").write_text(json.dumps({"refs": refs, "claims": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    yn = lambda v: "-" if v is None else ("sim" if v else "NÃO")
    out = ["# Conferência da bibliografia do deck (método do nível 3)", "",
           "Código procura cada obra (OpenAlex, DBLP, arXiv, OpenLibrary, web) e os números e frases no texto da fonte; "
           "um júri de três empresas (DeepSeek, Qwen, Google) lê os trechos achados e decide por maioria.", "",
           "## Obras", "", "| Obra | Existe | Autor | Ano | Veículo | Lido |", "| --- | --- | --- | --- | --- | --- |"]
    for r in refs.values():
        out.append(f"| {r['id']} | {yn(r['exists'])} | {yn(r['author_ok'])} | {yn(r['year_ok'])} | {yn(r['venue_ok'])} | "
                   f"{'; '.join(r['texts'])[:160] or 'NADA'} |")
    out += ["", "## Afirmações", ""]
    for c in results:
        nf = ", ".join(f"{k}: {'achado' if v else 'NÃO achado'}" for k, v in c["needles_found"].items())
        out += [f"### {c['id']} (p. {c['page']}): **{c['verdict']}**", "", f"> {c['claim']}", "", f"Código: {nf}", ""]
        out += [f"- {v['judge']}: {v['verdict']}. {v['reason'][:400]}" for v in c["votes"]] + [""]
    (HERE / "REPORT.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out[:60]))


if __name__ == "__main__":
    asyncio.run(main_async())
