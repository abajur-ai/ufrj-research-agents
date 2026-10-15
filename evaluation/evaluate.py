"""Evaluator, the same for every level: python -m evaluation.evaluate --judge deepseek --prefix mytest

Per delivered article, by code: the DOI exists (Crossref or OpenAlex); title, first author, year and journal match the
registry (separating fabricated references from errors in real ones, as Walters and Wilder 2023 do); the article is in
the requested period and is a journal article; the quote is in an abstract held by OpenAlex, Crossref, Semantic Scholar
or the publisher page (the last two are sources Level 3 never uses); every number given as sample size is in it.
Per article, by one judge, blind to the level, reading the abstract: on topic, empirical, method as stated, and whether
the abstract supports the stated finding. An article is correct only when every check and every criterion passes.

--judge picks the judge: deepseek (DeepSeek V4 Pro, the single judge), qwen (Qwen3.7 Plus, Alibaba) or gemini
(Gemini 3.1 Flash-Lite, Google). The three together form the jury (evaluation/jury.py). Each run's evaluation goes to
agents/level_N/evaluations/judge-<name>/<run_id>.json.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

import httpx
from rapidfuzz import fuzz

from evaluation.verify import fetch_page, find_quote, norm
from core.sources import HEADERS

from benchmark import paths
from benchmark.common import NOT_REPORTED, numbers_in
from benchmark.run import load_topic
from benchmark.scholar import (abstracts_for, crossref, norm_doi, openalex_by_doi, openalex_search, publisher_titles,
                               semantic_scholar)

from . import judge_llm
from .judge_llm import judge

JUDGES = {"deepseek": ("deepseek/deepseek-v4-pro", "DeepSeek V4 Pro (DeepSeek), esforço high"),
          "qwen": ("qwen/qwen3.7-plus", "Qwen3.7 Plus (Alibaba), esforço high"),
          "gemini": ("google/gemini-3.1-flash-lite", "Gemini 3.1 Flash-Lite (Google), esforço high")}
JUDGE = "deepseek"
JUDGE_SYSTEM = """# Juiz de revisão de literatura

## Perfil
Você avalia, para uma revisão de literatura acadêmica, se um artigo atende ao pedido do pesquisador e se os dados
extraídos dele estão certos. Você não sabe quem extraiu os dados. Seja estrito e consistente.

## Memória
Use só o pedido, os metadados e o resumo fornecidos. Não use conhecimento próprio sobre o artigo.

## Planejamento
Para cada critério, copie primeiro o trecho do resumo (ou o dado dos metadados) que decide, e só então decida.
1. on_topic: o artigo trata do tema do pedido, dentro do recorte pedido (plataforma, país, público)? Para o país,
   valem o resumo, o título e o periódico juntos; não exija que o resumo repita o nome do país.
2. empirical: o estudo coleta ou analisa dados próprios do tipo que o pedido exige (por exemplo: experimento,
   survey, entrevistas, grupos focais, análise de conteúdo ou de documentos)? Ensaio teórico e revisão não contam.
3. method_ok: o tipo de estudo e o método informados batem com o resumo?
4. finding: o achado informado é sustentado pelo resumo? supported (inteiro), partial (parte, ou vai além),
   unsupported (não sustenta ou contradiz).
Os rótulos precisam concordar com os trechos que você copiou.

## Ação
Sem ferramentas. Responda no esquema, em português."""
JUDGE_SCHEMA = {"type": "object", "additionalProperties": False,
                "required": ["evidence_topic", "on_topic", "evidence_empirical", "empirical", "method_ok", "finding",
                             "reason"],
                "properties": {"evidence_topic": {"type": "string"}, "on_topic": {"type": "boolean"},
                               "evidence_empirical": {"type": "string"}, "empirical": {"type": "boolean"},
                               "method_ok": {"type": "boolean"},
                               "finding": {"type": "string", "enum": ["supported", "partial", "unsupported"]},
                               "reason": {"type": "string"}}}


def _surname(name: str) -> str:
    parts = re.sub(r"[.,]", " ", name or "").split()
    return norm(parts[-1]) if parts else ""


async def check_item(client: httpx.AsyncClient, it: dict, constraints: dict, request: str) -> dict:
    doi = norm_doi(it.get("doi", ""))
    res = {"doi": doi, "title": it.get("title", ""), "checks": {}}
    c = res["checks"]
    cr = await crossref(client, doi) if doi else None
    oa = await openalex_by_doi(client, doi) if doi else None
    c["doi_exists"] = bool(cr or oa)
    if not c["doi_exists"]:
        # wrong DOI for a real article, or a reference that cannot be found anywhere (Walters and Wilder)
        hits = await openalex_search(client, it.get("title", "")[:200], 1900, 2026, per_page=5) if it.get("title") else []
        best = max((fuzz.token_set_ratio(norm(it.get("title", "")), norm(h["title"])) for h in hits), default=0)
        res["error_class"] = "wrong_doi_real_article" if best >= 90 else "not_found"
        res["correct"] = False
        return res
    reg_title = (cr or {}).get("title") or (oa or {}).get("title", "")
    s2 = await semantic_scholar(client, doi)
    titles = [t for t in [reg_title, (oa or {}).get("title", ""), (s2 or {}).get("title", "")] if t]
    titles += await publisher_titles(doi)
    years = set((cr or {}).get("years", [])) | ({oa["year"]} if oa and oa.get("year") else set())
    reg_authors = (cr or {}).get("authors") or (oa or {}).get("authors", [])
    venue = (cr or {}).get("venue") or (oa or {}).get("venue", "")
    mine = norm(it.get("title", ""))
    # a title with its subtitle, or the article's own title in another language declared by the publisher, matches
    c["title_ok"] = any(fuzz.token_set_ratio(mine, norm(t)) >= 85 or
                        (len(norm(t)) >= 12 and fuzz.partial_ratio(norm(t), mine) >= 92) for t in titles)
    c["year_ok"] = it.get("year") in years
    first = norm((it.get("authors") or [""])[0])
    # any citation style: "Given Surname", "Surname, Given" or "Surname Initials" (Vancouver, "Köbis NC")
    words = {w for w in re.sub(r"[.,]", " ", first).split() if len(w) > 2}
    c["author_ok"] = bool(first) and any(fuzz.token_set_ratio(first, norm(a)) >= 85 or _surname(first) in norm(a).split()
                                         or _surname(a) in words for a in reg_authors[:3])
    c["venue_ok"] = bool(venue) and fuzz.token_set_ratio(norm(it.get("venue", "")), norm(venue)) >= 80
    c["in_period"] = any(constraints["year_from"] <= y <= constraints["year_to"] for y in years)
    c["journal_article"] = (cr or {}).get("type") == "journal-article"
    abstracts = await abstracts_for(client, doi)
    texts = list(abstracts)
    page = await fetch_page(client, f"https://doi.org/{doi}")
    if page.get("status") == 200:   # full page text: only for finding the quote, never shown to the judge
        texts.append((page.get("text") or "") + "\n" + (page.get("raw") or ""))
    res["abstract_sources"] = len(abstracts)
    quote = it.get("abstract_quote", "")
    c["quote_ok"] = any(find_quote(quote, t) in ("exact", "near") for t in texts) if texts else None
    sample = norm(it.get("sample_size", "")).strip(' "\'.')
    if sample.startswith(norm(NOT_REPORTED)):
        c["sample_ok"] = None
    elif not texts:
        c["sample_ok"] = None
    else:
        # literal phrase of the abstract (words or digits), or every number it gives is in the abstract
        nums = numbers_in(sample)
        c["sample_ok"] = any(sample in norm(t) or (nums and nums <= numbers_in(t)) or
                             fuzz.partial_ratio(sample, norm(t)) >= 92 for t in texts)
    abstract = max(abstracts, key=len) if abstracts else ""
    if abstract:
        j = await judge(client, JUDGE_SYSTEM, (
            f"PEDIDO DO PESQUISADOR:\n{request}\n\nARTIGO (metadados do registro): {reg_title} ({sorted(years)}), {venue}\n"
            f"RESUMO:\n{abstract[:4000]}\n\nDADOS EXTRAÍDOS A JULGAR:\n"
            + json.dumps({k: it.get(k) for k in ("study_type", "method", "sample_size", "main_finding")},
                         ensure_ascii=False)), JUDGE_SCHEMA, "lit_item")
        res["judge"] = j
    else:
        res["judge"] = None
    jd = res["judge"] or {}
    det = ["title_ok", "year_ok", "author_ok", "venue_ok", "in_period", "journal_article"]
    res["metadata_ok"] = all(c[k] for k in det[:4])
    res["correct"] = bool(all(c[k] for k in det) and c["quote_ok"] and c["sample_ok"] is not False
                          and jd.get("on_topic") and jd.get("empirical") and jd.get("method_ok")
                          and jd.get("finding") == "supported")
    if not res["metadata_ok"]:
        res["error_class"] = "metadata_error"
    elif not abstracts:
        res["error_class"] = "no_abstract"   # nobody can check it: reported apart, never as a wrong item
    return res


async def evaluate_run(client: httpx.AsyncClient, run_dir: Path) -> dict:
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    final = json.loads((run_dir / "final.json").read_text(encoding="utf-8"))
    topic = load_topic(meta["item"])
    constraints = topic["constraints"]
    items = ((final.get("report") or {}).get("items")) or []
    checked = await asyncio.gather(*(check_item(client, it, constraints, topic["request_pt"]) for it in items))
    n_correct = sum(1 for r in checked if r["correct"])
    requested = topic["n_wanted"]
    rec = {"run_id": meta["run_id"], "level": meta["level"], "item": meta["item"], "status": final.get("status"),
           "delivered": len(items), "correct": n_correct, "requested": requested, "yield": n_correct / requested,
           "precision": n_correct / len(items) if items else None,
           "not_found": sum(1 for r in checked if r.get("error_class") == "not_found"),
           "wrong_doi": sum(1 for r in checked if r.get("error_class") == "wrong_doi_real_article"),
           "metadata_errors": sum(1 for r in checked if r.get("error_class") == "metadata_error"),
           "quote_fail": sum(1 for r in checked if r["checks"].get("quote_ok") is False),
           "no_abstract": sum(1 for r in checked if r.get("error_class") == "no_abstract"),
           "wall_seconds": meta["wall_seconds"], "calls": meta.get("calls_total"), "items": checked,
           "judge": JUDGES[JUDGE][1]}
    out = paths.eval_file(f"judge-{JUDGE}", meta["run_id"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    return rec


async def main_async(prefix: str) -> None:
    runs = paths.runs(prefix)
    sem = asyncio.Semaphore(3)

    async def one(d):
        done = paths.eval_file(f"judge-{JUDGE}", d.name)
        if done.exists() and done.stat().st_mtime >= (d / "meta.json").stat().st_mtime:
            return json.loads(done.read_text(encoding="utf-8"))
        async with sem:
            return await evaluate_run(client, d)

    async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
        recs = await asyncio.gather(*(one(d) for d in runs))
    for r in recs:
        print(f"{r['run_id']}: status {r['status']}, entregues {r['delivered']}, corretos {r['correct']}, "
              f"não encontrados {r['not_found']}, DOI trocado {r['wrong_doi']}, erro de dado {r['metadata_errors']}, "
              f"citação fora do resumo {r['quote_fail']}, {r['wall_seconds']:.0f} s")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", required=True, choices=list(JUDGES))
    ap.add_argument("--prefix", required=True, help="evaluate the finished runs whose id starts with this")
    a = ap.parse_args()
    JUDGE = a.judge
    judge_llm.JUDGE_MODEL = JUDGES[JUDGE][0]
    _hook = sys.unraisablehook

    def _quiet(u):
        # on Windows the browser subprocess used for publisher pages can be collected after the event loop closes;
        # Python then prints "I/O operation on closed pipe", which is harmless, so it is not shown
        if not (isinstance(u.exc_value, ValueError) and "closed pipe" in str(u.exc_value)):
            _hook(u)

    sys.unraisablehook = _quiet
    asyncio.run(main_async(a.prefix))
