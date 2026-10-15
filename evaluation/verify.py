"""Deterministic checks of every source cited in a run. No AI here.

For each cited source: open the URL ourselves (cached), find the literal quote in the page text, compare the
claimed title, and, when the page is unavailable, look the title up in search engines to separate a broken link
from a reference that cannot be located anywhere.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import time
import unicodedata
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from rapidfuzz import fuzz

from core.config import CACHE_DIR
from core.sources import HEADERS, WIKI_HEADERS, WIKI_URL, Brave, _fetch_url, openalex

CACHE = CACHE_DIR / "pages"
BLOCKED = {401, 402, 403, 406, 429, 451}  # 406: sites such as time.com answer it to robots

QUOTE_CHARS = str.maketrans({"\u201c": '"', "\u201d": '"', "\u201e": '"', "\u2018": "'", "\u2019": "'",
                             "\u00ab": '"', "\u00bb": '"', "\u2013": "-", "\u2014": "-", "\u00ad": "",
                             "\u00a0": " "})


def norm(text: str) -> str:
    t = unicodedata.normalize("NFKC", text or "").translate(QUOTE_CHARS).casefold()
    t = re.sub(r"\[[0-9]+\]", "", t)          # wikipedia footnote markers
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def quote_segments(quote: str) -> list[str]:
    # non-contiguous passages: ellipses, or explicit separators " // " and " / " between literal passages
    parts = re.split(r"\.\.\.|…|\[\s*\.\.\.\s*\]|\(\s*\.\.\.\s*\)|\s//\s|\s/\s|[\r\n]+", quote)
    return [norm(p).strip(' "\'') for p in parts if len(norm(p).strip(' "\'')) >= 15]


def find_quote(quote: str, page: str) -> str:
    """'exact' when every segment is a substring, 'near' when every segment aligns at >= 90, else 'not_found'."""
    segs = quote_segments(quote)
    if not segs:
        return "too_short"
    p = norm(page)
    if all(s in p for s in segs):
        return "exact"
    ok = 0
    for s in segs:
        if s in p:
            ok += 1
            continue
        alignment = fuzz.partial_ratio_alignment(s, p, score_cutoff=90) if len(s) <= 2000 else None
        if alignment is not None:
            ok += 1
    return "near" if ok == len(segs) else "not_found"


def _key(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()


async def fetch_page(client: httpx.AsyncClient, url: str) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{_key(url)}.json"
    if f.exists():
        cached = json.loads(f.read_text(encoding="utf-8"))
        if cached.get("status") and cached["status"] < 500:
            return cached
    rec = await _fetch_once(client, url)
    if not rec.get("status") or rec["status"] >= 500:   # connection dropped or server error: one more try
        await asyncio.sleep(3)
        rec = await _fetch_once(client, url, timeout=60)
    f.write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")
    return rec


async def _fetch_once(client: httpx.AsyncClient, url: str, timeout: int = 30) -> dict:
    rec = {"url": url, "status": 0, "final_url": url, "title": "", "text": "", "raw": ""}
    try:
        m = WIKI_URL.match(url)
        if m:
            title = httpx.URL(url).path.split("/wiki/", 1)[1]
            from urllib.parse import unquote
            r = await client.get(f"https://{m.group(1).lower()}.wikipedia.org/w/api.php",
                                 params={"action": "query", "prop": "extracts", "explaintext": 1,
                                         "titles": unquote(title).replace("_", " "), "format": "json", "redirects": 1},
                                 headers=WIKI_HEADERS, timeout=40)
            pages = r.json().get("query", {}).get("pages", {}) if r.status_code == 200 else {}
            page = next(iter(pages.values()), {}) if pages else {}
            rec.update(status=404 if "missing" in page else r.status_code, title=page.get("title", ""),
                       text=page.get("extract", ""))
        else:
            async with client.stream("GET", url, headers=HEADERS, timeout=timeout, follow_redirects=True) as r:
                rec["status"], rec["final_url"] = r.status_code, str(r.url)
                body = b""
                async for chunk in r.aiter_bytes():
                    body += chunk
                    if len(body) > 8 * 1024 * 1024:
                        break
                ctype = r.headers.get("content-type", "").lower()
            if rec["status"] == 200 and body:
                if "pdf" in ctype or body[:5] == b"%PDF-":
                    import io
                    import pymupdf
                    with pymupdf.open(stream=io.BytesIO(body), filetype="pdf") as doc:
                        rec["text"] = "\n".join(pg.get_text() for pg in doc)
                else:
                    html = body.decode("utf-8", errors="replace")
                    import trafilatura
                    rec["text"] = trafilatura.extract(html, favor_recall=True) or ""
                    soup = BeautifulSoup(html, "lxml")
                    rec["title"] = (soup.title.get_text(" ", strip=True) if soup.title else "")[:300]
                    for tag in soup(["script", "style", "noscript"]):
                        tag.decompose()
                    rec["raw"] = soup.get_text(" ", strip=True)
    except (httpx.HTTPError, ValueError, RuntimeError) as exc:
        rec["error"] = type(exc).__name__
    return rec


async def _brave_titles(client: httpx.AsyncClient, brave: Brave, q: str) -> list[tuple[str, str]]:
    """Brave results as (title, url). Raises on any non-200, so a refused request never reads as 'no result'."""
    async with Brave._lock:  # free plan: one request per second
        wait = 1.15 - (time.time() - Brave._last)
        if wait > 0:
            await asyncio.sleep(wait)
        r = await client.get("https://api.search.brave.com/res/v1/web/search", params={"q": q, "count": 10},
                             headers={"Accept": "application/json", "X-Subscription-Token": brave.key}, timeout=30)
        Brave._last = time.time()
    r.raise_for_status()
    return [(i.get("title", ""), i.get("url", "")) for i in (r.json().get("web", {}).get("results") or [])]


async def locate_title(client: httpx.AsyncClient, brave: Brave, title: str, author: str) -> dict:
    """Look a reference up by title. Used only when its URL does not open. A failed lookup is retried, never cached."""
    f = CACHE / f"title-{_key(title + '|' + author)}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    best = {"found": False, "score": 0, "match": "", "where": ""}
    if not title or len(title) < 8:
        return best
    for attempt in range(3):
        try:
            hits = await _brave_titles(client, brave, f'"{title}"')
            if not any(fuzz.token_set_ratio(norm(title), norm(t)) >= 85 for t, _ in hits):
                hits += [(w.title, w.url) for w in await openalex(client, title)]
            for t, url in hits:
                s = fuzz.token_set_ratio(norm(title), norm(t))
                if s > best["score"]:
                    best = {"found": s >= 85, "score": s, "match": t, "where": url}
            f.write_text(json.dumps(best, ensure_ascii=False), encoding="utf-8")
            return best
        except (httpx.HTTPError, ValueError, KeyError) as exc:
            best["error"] = type(exc).__name__
            await asyncio.sleep(5 * (attempt + 1))
    return best


async def check_sources(report: dict) -> list[dict]:
    brave = Brave()
    out = []
    async with httpx.AsyncClient(headers=HEADERS) as client:
        sem = asyncio.Semaphore(6)

        async def one(src: dict) -> dict:
            async with sem:
                page = await fetch_page(client, src.get("url", ""))
            status = page.get("status", 0)
            text = (page.get("text", "") or "") + "\n" + (page.get("raw", "") or "")
            res = {"id": src.get("id"), "url": src.get("url"), "http": status, "kind": src.get("kind")}
            if status == 200 and text.strip():
                res["quote"] = find_quote(src.get("quote", ""), text)
                head = norm(page.get("title", "") + " " + text[:3000])
                res["title_score"] = fuzz.partial_ratio(norm(src.get("title", ""))[:200], head) if src.get("title") else 0
                res["class"] = "verified" if res["quote"] in ("exact", "near") else "page_ok_quote_missing"
            else:
                res["quote"] = "unverifiable"
                loc = await locate_title(client, brave, src.get("title", ""), src.get("author", ""))
                res["located"] = loc
                if "error" in loc and status not in BLOCKED:
                    res["class"] = "lookup_failed"   # search engines refused three times: counted as unknown, never as fabricated
                elif status in BLOCKED or loc["found"]:
                    res["class"] = "exists_unverifiable" if loc["found"] or status in BLOCKED else "not_located"
                else:
                    res["class"] = "not_located"
            return res

        out = await asyncio.gather(*(one(s) for s in report.get("sources", [])))
    return list(out)
