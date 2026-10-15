"""Deterministic retrieval for level 3: fixed connectors, fixed limits, fixed order. No AI here.

Every document keeps the exact URL it came from, the HTTP status, the retrieval time and a SHA-256 of the
text, so every citation in the final report can be traced back to bytes on disk.
"""
from __future__ import annotations

import asyncio
import hashlib
import io
import json
import re
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import httpx
import pymupdf
import trafilatura

from .config import USER_AGENT, brave_api_key

HEADERS = {"User-Agent": USER_AGENT, "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"}
# Wikimedia requires an identifiable User-Agent with contact information.
WIKI_HEADERS = {"User-Agent": "ufrj-research-agents/1.0 (https://abajur.ai; bruno@abajur.ai) httpx"}
WIKI_URL = re.compile(r"^https?://([a-z]{2,3})(?:\.m)?\.wikipedia\.org/wiki/([^?#]+)", re.I)
MAX_BYTES = 8 * 1024 * 1024
LIMITS = {"brave": 5, "openalex": 4, "wikipedia": 2, "archive": 2}

FACT_CHECK = ("lupa.uol.com.br", "aosfatos.org", "snopes.com", "politifact.com", "factcheck.org",
              "fullfact.org", "boatos.org", "e-farsas.com", "estadao.com.br/estadao-verifica", "g1.globo.com/fato-ou-fake",
              "afp.com", "checamos.afp.com", "projetocomprova.com.br", "apublica.org/checagem")
OFFICIAL = (".gov", ".gov.br", ".gov.uk", ".jus.br", ".leg.br", ".mp.br", "ico.org.uk", "europa.eu", ".mil")
ACADEMIC = ("doi.org", "jstor.org", "springer.com", "sciencedirect.com", "tandfonline.com", "wiley.com",
            "sagepub.com", "scielo", "academia.edu", "researchgate.net", "arxiv.org", "ssrn.com", ".edu",
            "periodicos", "revistas.", "ojs.", "oup.com", "cambridge.org", "muse.jhu.edu", "uchicago.edu")
ENCYCLOPEDIA = ("wikipedia.org", "britannica.com")


@dataclass
class Candidate:
    url: str
    title: str
    connector: str
    query: str
    snippet: str = ""
    meta: dict = field(default_factory=dict)


@dataclass
class Document:
    doc_id: str
    url: str
    final_url: str
    connector: str
    query: str
    title: str
    author: str
    date: str
    kind_hint: str
    status: int
    chars: int
    sha256: str
    retrieved_at: str


def normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query = "&".join(p for p in parts.query.split("&") if p and not p.lower().startswith(("utm_", "fbclid", "gclid")))
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def kind_hint(url: str, connector: str) -> str:
    u = url.lower()
    if connector == "openalex" or any(a in u for a in ACADEMIC):
        return "academic"
    if connector == "wikipedia" or any(e in u for e in ENCYCLOPEDIA):
        return "encyclopedia"
    if any(f in u for f in FACT_CHECK):
        return "fact_check"
    host = urlsplit(u).netloc
    if any(host.endswith(o) or o in host for o in OFFICIAL):
        return "official"
    return "press" if connector == "brave" else "other"


class Brave:
    _lock = asyncio.Lock()
    _last = 0.0

    def __init__(self) -> None:
        self.key = brave_api_key()

    async def search(self, client: httpx.AsyncClient, q: str, lang: str) -> list[Candidate]:
        async with Brave._lock:  # free plan: one request per second
            wait = 1.15 - (time.time() - Brave._last)
            if wait > 0:
                await asyncio.sleep(wait)
            r = await client.get("https://api.search.brave.com/res/v1/web/search",
                                 params={"q": q, "count": 10, "search_lang": "pt-br" if lang == "pt" else "en"},
                                 headers={"Accept": "application/json", "X-Subscription-Token": self.key}, timeout=30)
            Brave._last = time.time()
        if r.status_code != 200:
            return []
        out = []
        for item in (r.json().get("web", {}).get("results") or [])[: LIMITS["brave"]]:
            url = item.get("url", "")
            m = WIKI_URL.match(url)
            if m:
                title = unquote(m.group(2)).replace("_", " ")
                out.append(Candidate(url, title, "wikipedia", q, meta={"lang": m.group(1).lower(), "wiki_title": title}))
            else:
                out.append(Candidate(url, item.get("title", ""), "brave", q, item.get("description", "")))
        return out


def _abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    words: dict[int, str] = {}
    for w, positions in inv.items():
        for p in positions:
            words[p] = w
    return " ".join(words[i] for i in sorted(words))


async def openalex(client: httpx.AsyncClient, q: str) -> list[Candidate]:
    r = await client.get("https://api.openalex.org/works",
                         params={"search": q, "per-page": LIMITS["openalex"], "mailto": "bruno@abajur.ai"}, timeout=40)
    if r.status_code != 200:
        return []
    out = []
    for w in r.json().get("results", []):
        loc = (w.get("primary_location") or {})
        url = (w.get("doi") or loc.get("landing_page_url") or w.get("id") or "")
        authors = ", ".join(a["author"]["display_name"] for a in (w.get("authorships") or [])[:4] if a.get("author"))
        text = f"{w.get('display_name', '')}. {_abstract(w.get('abstract_inverted_index'))}".strip()
        out.append(Candidate(url, w.get("display_name", ""), "openalex", q, meta={
            "author": authors, "year": str(w.get("publication_year") or ""),
            "venue": ((loc.get("source") or {}) or {}).get("display_name", ""),
            "oa_url": ((w.get("open_access") or {}).get("oa_url") or ""), "text": text}))
    return out


async def wikipedia(client: httpx.AsyncClient, q: str, lang: str) -> list[Candidate]:
    base = f"https://{lang}.wikipedia.org/w/api.php"
    r = await client.get(base, params={"action": "query", "list": "search", "srsearch": q,
                                       "srlimit": LIMITS["wikipedia"], "format": "json"},
                         headers=WIKI_HEADERS, timeout=30)
    if r.status_code != 200:
        return []
    out = []
    for hit in r.json().get("query", {}).get("search", []):
        title = hit["title"]
        out.append(Candidate(f"https://{lang}.wikipedia.org/wiki/{quote(title.replace(' ', '_'))}", title,
                             "wikipedia", q, meta={"lang": lang, "wiki_title": title}))
    return out


async def internet_archive(client: httpx.AsyncClient, q: str) -> list[Candidate]:
    r = await client.get("https://archive.org/advancedsearch.php",
                         params={"q": f"({q}) AND mediatype:texts", "fl[]": ["identifier", "title", "date", "creator"],
                                 "rows": LIMITS["archive"], "output": "json"}, timeout=40)
    if r.status_code != 200:
        return []
    words = {w for w in re.findall(r"\w{4,}", q.casefold())}
    out = []
    for d in r.json().get("response", {}).get("docs", []):
        title_words = set(re.findall(r"\w{4,}", str(d.get("title", "")).casefold()))
        if len(words & title_words) < 2:
            continue
        ident = d["identifier"]
        creator = d.get("creator") or ""
        out.append(Candidate(f"https://archive.org/details/{ident}", str(d.get("title", ident)), "archive", q, meta={
            "identifier": ident, "author": ", ".join(creator) if isinstance(creator, list) else str(creator),
            "year": str(d.get("date", ""))[:4]}))
    return out


async def _fetch_text(client: httpx.AsyncClient, c: Candidate) -> tuple[int, str, str, dict]:
    """Return (status, final_url, text, metadata) for a candidate."""
    if c.connector == "wikipedia":
        lang = c.meta["lang"]
        r = await client.get(f"https://{lang}.wikipedia.org/w/api.php",
                             params={"action": "query", "prop": "extracts", "explaintext": 1, "titles": c.meta["wiki_title"],
                                     "format": "json", "redirects": 1}, headers=WIKI_HEADERS, timeout=40)
        pages = r.json().get("query", {}).get("pages", {}) if r.status_code == 200 else {}
        text = next(iter(pages.values()), {}).get("extract", "") if pages else ""
        return r.status_code, c.url, text, {"title": c.title, "author": "Wikipedia", "date": ""}
    if c.connector == "archive":
        ident = c.meta["identifier"]
        r = await client.get(f"https://archive.org/download/{ident}/{ident}_djvu.txt", timeout=60, follow_redirects=True)
        text = r.text[:MAX_BYTES] if r.status_code == 200 else ""
        return r.status_code, c.url, text, {"title": c.title, "author": c.meta.get("author", ""), "date": c.meta.get("year", "")}
    if c.connector == "openalex":
        text, status, final = c.meta.get("text", ""), 200, c.url
        oa = c.meta.get("oa_url")
        if oa:
            try:
                st, fin, full, _ = await _fetch_url(client, oa)
                if st == 200 and len(full) > len(text):
                    text = text + "\n\n" + full
            except (httpx.HTTPError, ValueError):
                pass
        return status, final, text, {"title": c.title, "author": c.meta.get("author", ""), "date": c.meta.get("year", "")}
    return await _fetch_url(client, c.url)


async def _fetch_url(client: httpx.AsyncClient, url: str) -> tuple[int, str, str, dict]:
    async with client.stream("GET", url, headers=HEADERS, timeout=30, follow_redirects=True) as r:
        status = r.status_code
        final = str(r.url)
        ctype = r.headers.get("content-type", "").lower()
        chunks, size = [], 0
        async for chunk in r.aiter_bytes():
            size += len(chunk)
            if size > MAX_BYTES:
                break
            chunks.append(chunk)
        body = b"".join(chunks)
    if status != 200 or not body:
        return status, final, "", {}
    if "pdf" in ctype or body[:5] == b"%PDF-":
        with pymupdf.open(stream=io.BytesIO(body), filetype="pdf") as doc:
            text = "\n".join(page.get_text() for page in doc)
        return status, final, text, {"title": "", "author": "", "date": ""}
    html = body.decode(r.encoding or "utf-8", errors="replace")
    text = trafilatura.extract(html, include_comments=False, include_tables=False, favor_recall=True) or ""
    meta = trafilatura.extract_metadata(html)
    md = {"title": (meta.title if meta else "") or "", "author": (meta.author if meta else "") or "",
          "date": (meta.date if meta else "") or ""}
    return status, final, text, md


async def collect(plan: dict, corpus_dir: Path, emit) -> list[Document]:
    """Run every query on every connector in a fixed order, then download and extract each document."""
    corpus_dir.mkdir(parents=True, exist_ok=True)
    brave = Brave()
    candidates: list[Candidate] = []
    async with httpx.AsyncClient(headers=HEADERS, http2=False) as client:
        for lang, key in (("pt", "queries_pt"), ("en", "queries_en")):
            for q in plan.get(key, []):
                found = []
                for name, coro in (("brave", brave.search(client, q, lang)), ("openalex", openalex(client, q)),
                                   ("wikipedia", wikipedia(client, q, lang)),
                                   ("archive", internet_archive(client, q) if lang == "en" else None)):
                    if coro is None:
                        continue
                    try:
                        res = await coro
                    except (httpx.HTTPError, ValueError, KeyError):
                        res = []
                    found.extend(res)
                    emit("det_search", connector=name, query=q, results=len(res))
                candidates.extend(found)

        seen, unique = set(), []
        for c in candidates:
            if not c.url:
                continue
            key = normalize_url(c.url)
            if key not in seen:
                seen.add(key)
                unique.append(c)
        emit("det_dedupe", candidates=len(candidates), unique=len(unique))

        sem = asyncio.Semaphore(8)
        docs: list[Document | None] = [None] * len(unique)

        async def grab(i: int, c: Candidate) -> None:
            async with sem:
                try:
                    status, final, text, md = await _fetch_text(client, c)
                except (httpx.HTTPError, ValueError, RuntimeError) as exc:
                    emit("det_download", url=c.url, status=0, chars=0, error=type(exc).__name__)
                    return
                text = text or ""
                emit("det_download", url=c.url, status=status, chars=len(text))
                if status != 200 or len(text) < 400:
                    return
                doc_id = f"D{i + 1:03d}"
                (corpus_dir / f"{doc_id}.txt").write_text(text, encoding="utf-8")
                docs[i] = Document(
                    doc_id=doc_id, url=c.url, final_url=final, connector=c.connector, query=c.query,
                    title=(md.get("title") or c.title or "").strip()[:300],
                    author=(md.get("author") or c.meta.get("author", "") or "").strip()[:200],
                    date=str(md.get("date") or c.meta.get("year", "") or "")[:20],
                    kind_hint=kind_hint(final or c.url, c.connector), status=status, chars=len(text),
                    sha256=hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    retrieved_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"))

        await asyncio.gather(*(grab(i, c) for i, c in enumerate(unique)))

    kept = [d for d in docs if d]
    (corpus_dir / "index.json").write_text(json.dumps([asdict(d) for d in kept], ensure_ascii=False, indent=1),
                                           encoding="utf-8")
    emit("det_corpus", documents=len(kept), chars=sum(d.chars for d in kept))
    return kept
