"""Deterministic access to scholarly metadata: OpenAlex search, Crossref and Semantic Scholar by DOI. No AI here.

Used by level 3 to retrieve candidates and by the evaluator to check every reference of every level the same way.
Responses are cached on disk (.cache/scholar) so repeated checks of the same DOI give the same answer.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import time
from pathlib import Path

import httpx

from core.config import CACHE_DIR

CACHE = CACHE_DIR / "scholar"
MAILTO = "bruno@abajur.ai"
HEADERS = {"User-Agent": f"ufrj-research-agents/1.0 (mailto:{MAILTO})"}
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)
_s2_lock = asyncio.Lock()
_s2_last = 0.0


def norm_doi(doi: str) -> str:
    m = DOI_RE.search(doi or "")
    return m.group(0).rstrip(".,;)").lower() if m else ""


def abstract_from_index(inv: dict | None) -> str:
    if not inv:
        return ""
    words = {p: w for w, ps in inv.items() for p in ps}
    return " ".join(words[i] for i in sorted(words))


def _strip_tags(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


def openalex_key() -> str:
    """OpenAlex asks for a free API key since 2026; read at run time from the user environment, never stored."""
    import os
    k = os.environ.get("OPENALEX_API_KEY", "")
    if not k and os.name == "nt":
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
                k = winreg.QueryValueEx(h, "OPENALEX_API_KEY")[0]
        except OSError:
            k = ""
    return k


async def _cached_get(client: httpx.AsyncClient, url: str, params: dict | None = None, tries: int = 3) -> dict | None:
    key = hashlib.sha1((url + json.dumps(params or {}, sort_keys=True)).encode()).hexdigest()
    headers = dict(HEADERS)
    if "openalex.org" in url and openalex_key():   # the key travels in a header only, never in the URL or the cache
        headers["Authorization"] = f"Bearer {openalex_key()}"
    f = CACHE / f"{key}.json"
    if f.exists():
        rec = json.loads(f.read_text(encoding="utf-8"))
        return rec.get("data")
    for attempt in range(tries):
        try:
            r = await client.get(url, params=params, headers=headers, timeout=40)
        except httpx.HTTPError:
            await asyncio.sleep(2 * (attempt + 1))
            continue
        if r.status_code == 404:
            CACHE.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps({"status": 404, "data": None}), encoding="utf-8")
            return None
        if r.status_code == 200:
            data = r.json()
            CACHE.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps({"status": 200, "data": data}, ensure_ascii=False), encoding="utf-8")
            return data
        if r.status_code == 429 and "budget" in r.text.lower():
            break   # OpenAlex daily budget used up: waiting a few seconds will not help
        await asyncio.sleep(3 * (attempt + 1))   # 429 or 5xx: retried, never cached
    return None


def _openalex_record(w: dict) -> dict:
    loc = w.get("primary_location") or {}
    return {
        "doi": norm_doi(w.get("doi") or ""),
        "title": w.get("display_name") or "",
        "year": w.get("publication_year"),
        "venue": ((loc.get("source") or {}) or {}).get("display_name") or "",
        "authors": [a["author"]["display_name"] for a in (w.get("authorships") or []) if a.get("author")],
        "type": w.get("type"),
        "abstract": abstract_from_index(w.get("abstract_inverted_index")),
        "openalex_id": w.get("id"),
        "relevance": w.get("relevance_score"),
    }


async def openalex_search(client: httpx.AsyncClient, query: str, year_from: int, year_to: int,
                          per_page: int = 25) -> list[dict]:
    data = await _cached_get(client, "https://api.openalex.org/works", {
        "search": query, "per-page": per_page, "mailto": MAILTO,
        "filter": f"publication_year:{year_from}-{year_to},type:article,has_abstract:true,has_doi:true"})
    return [_openalex_record(w) for w in (data or {}).get("results", [])]


async def crossref_search(client: httpx.AsyncClient, query: str, year_from: int, year_to: int,
                          rows: int = 25) -> list[dict]:
    """Second deterministic source for level 3: Crossref search, journal articles with abstract in the period."""
    data = await _cached_get(client, "https://api.crossref.org/works", {
        "query.bibliographic": query, "rows": rows, "mailto": MAILTO,
        "filter": f"from-pub-date:{year_from}-01-01,until-pub-date:{year_to}-12-31,type:journal-article,has-abstract:true",
        "select": "DOI,title,author,container-title,issued,type,abstract,score"})
    out = []
    for m in ((data or {}).get("message") or {}).get("items", []):
        parts = ((m.get("issued") or {}).get("date-parts") or [[None]])[0]
        out.append({"doi": norm_doi(m.get("DOI", "")), "title": " ".join(m.get("title") or []),
                    "year": parts[0] if parts else None, "venue": " ".join(m.get("container-title") or []),
                    "authors": [" ".join(x for x in (a.get("given"), a.get("family")) if x) for a in (m.get("author") or [])],
                    "type": m.get("type"), "abstract": _strip_tags(m.get("abstract", "")), "openalex_id": None,
                    "relevance": m.get("score")})
    return out


async def openalex_by_doi(client: httpx.AsyncClient, doi: str) -> dict | None:
    data = await _cached_get(client, f"https://api.openalex.org/works/doi:{doi}", {"mailto": MAILTO})
    return _openalex_record(data) if data else None


async def crossref(client: httpx.AsyncClient, doi: str) -> dict | None:
    data = await _cached_get(client, f"https://api.crossref.org/works/{doi}", {"mailto": MAILTO})
    m = (data or {}).get("message")
    if not m:
        return None
    years = set()
    for k in ("published-print", "published-online", "issued", "published"):
        parts = ((m.get(k) or {}).get("date-parts") or [[None]])[0]
        if parts and parts[0]:
            years.add(int(parts[0]))
    return {
        "doi": norm_doi(m.get("DOI", "")),
        "title": " ".join(m.get("title") or []),
        "years": sorted(years),
        "venue": " ".join(m.get("container-title") or []),
        "authors": [" ".join(x for x in (a.get("given"), a.get("family")) if x) for a in (m.get("author") or [])],
        "families": [a.get("family", "") for a in (m.get("author") or [])],
        "type": m.get("type"),
        "abstract": _strip_tags(m.get("abstract", "")),
    }


async def semantic_scholar(client: httpx.AsyncClient, doi: str) -> dict | None:
    """Abstract fallback; the public API allows about one request per second without a key."""
    global _s2_last
    async with _s2_lock:
        wait = 1.1 - (time.time() - _s2_last)
        if wait > 0:
            await asyncio.sleep(wait)
        data = await _cached_get(client, f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                                 {"fields": "title,abstract,year,venue,authors"})
        _s2_last = time.time()
    return data


_browser = None
_browser_lock = asyncio.Lock()
_page_sem = asyncio.Semaphore(3)
META_RE = re.compile(r'<meta[^>]+(?:name|property)="(citation_abstract|dc\.description|og:description|description|'
                     r'twitter:description)"[^>]+content="([^"]{200,})"', re.I)


TITLE_RE = re.compile(r'<meta[^>]+(?:name|property)="(citation_title|dc\.title|dc\.title\.alternative|og:title)"[^>]+'
                      r'content="([^"]{8,})"', re.I)


async def publisher_titles(doi: str) -> list[str]:
    """Every title the publisher page declares (main and alternative languages); read from the same cached visit."""
    await publisher_abstract(doi)
    f = CACHE / f"pub-{hashlib.sha1(doi.encode()).hexdigest()}.json"
    return json.loads(f.read_text(encoding="utf-8")).get("titles", []) if f.exists() else []


async def publisher_abstract(doi: str) -> str:
    """Abstract from the publisher page, opened in headless Chrome (many publishers serve a script wall to plain
    HTTP clients). Longest abstract-like meta tag; cached per DOI, with the page titles."""
    global _browser
    f = CACHE / f"pub-{hashlib.sha1(doi.encode()).hexdigest()}.json"
    if f.exists():
        rec = json.loads(f.read_text(encoding="utf-8"))
        if "titles" in rec:
            return rec["abstract"]
    async with _browser_lock:
        if _browser is None:
            from playwright.async_api import async_playwright
            pw = await async_playwright().start()
            _browser = await pw.chromium.launch(channel="chrome", headless=True)
    text, titles, ok = "", [], False
    async with _page_sem:
        page = await _browser.new_page()
        try:
            await page.goto(f"https://doi.org/{doi}", wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(2500)
            html = await page.content()
            import html as htmllib
            metas = [htmllib.unescape(v) for _, v in META_RE.findall(html)]
            text = _strip_tags(max(metas, key=len)) if metas else ""
            titles = sorted({_strip_tags(htmllib.unescape(v)) for _, v in TITLE_RE.findall(html)})
            ok = True
        except Exception:  # timeouts and navigation errors: not cached, retried on the next evaluation
            pass
        finally:
            await page.close()
    if ok:
        CACHE.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps({"abstract": text, "titles": titles}, ensure_ascii=False), encoding="utf-8")
    return text


async def abstracts_for(client: httpx.AsyncClient, doi: str) -> list[str]:
    """Every abstract text the open scholarly APIs and the publisher page hold for a DOI."""
    out = []
    oa = await openalex_by_doi(client, doi)
    if oa and oa.get("abstract"):
        out.append(oa["abstract"])
    cr = await crossref(client, doi)
    if cr and cr.get("abstract"):
        out.append(cr["abstract"])
    s2 = await semantic_scholar(client, doi)
    if s2 and s2.get("abstract"):
        out.append(s2["abstract"])
    pub = await publisher_abstract(doi)
    if len(pub) >= 200:
        out.append(pub)
    return out
