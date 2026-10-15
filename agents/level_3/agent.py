"""Level 3: multi-agent with checking, plus code. Code where it can, AI with checking where it must.

Six steps. AI only where judgment is needed, and each AI step goes through the verifier (QA):
1. AI + QA decides the search terms and the inclusion and exclusion criteria (prompts/terms.md);
2. code searches OpenAlex and Crossref and downloads the abstracts;
3. code filters by period and publication type in the official registry (Crossref);
4. AI + QA screens the downloaded abstracts (prompts/screener.md);
5. AI + QA extracts method, sample and finding (prompts/extractor.md), and code checks the quote and the sample
   against the abstract, letter by letter;
6. code builds each reference from the official registry: AI never types a DOI, a title or an author.
"""
from __future__ import annotations

from pathlib import Path

import httpx

from benchmark.common import N_WANTED, NOT_REPORTED, drop_rejected, dump, numbers_in, read_prompt, verifier_text, write_final
from benchmark.qa import history_block, qa_step, verify_step
from benchmark.scholar import crossref, crossref_search, openalex_search
from core.events import EventLog
from core.llm import run_agent
from evaluation.verify import norm

PROMPTS = Path(__file__).resolve().parent / "prompts"

TERMS_SCHEMA = {"type": "object", "properties": {
    "year_from": {"type": "integer"}, "year_to": {"type": "integer"},
    "queries_en": {"type": "array", "items": {"type": "string"}},
    "queries_pt": {"type": "array", "items": {"type": "string"}},
    "include": {"type": "array", "items": {"type": "string"}},
    "exclude": {"type": "array", "items": {"type": "string"}}},
    "required": ["year_from", "year_to", "queries_en", "queries_pt", "include", "exclude"]}
SCREEN_SCHEMA = {"type": "object", "properties": {
    "decisions": {"type": "array", "items": {"type": "object", "properties": {
        "id": {"type": "string"}, "include": {"type": "boolean"}, "reason": {"type": "string"}},
        "required": ["id", "include", "reason"]}},
    "selected": {"type": "array", "items": {"type": "string"}}},
    "required": ["decisions", "selected"]}
EXTRACT_SCHEMA = {"type": "object", "properties": {"items": {"type": "array", "items": {"type": "object", "properties": {
    "id": {"type": "string"}, "study_type": {"type": "string"}, "method": {"type": "string"},
    "sample_size": {"type": "string"}, "main_finding": {"type": "string"}, "abstract_quote": {"type": "string"}},
    "required": ["id", "study_type", "method", "sample_size", "main_finding", "abstract_quote"]}}},
    "required": ["items"]}
PER_ID_VERDICT = {"type": "object", "properties": {
    "approved": {"type": "boolean"}, "checked": {"type": "array", "items": {"type": "string"}},
    "per_item": {"type": "array", "items": {"type": "object", "properties": {
        "id": {"type": "string"}, "ok": {"type": "boolean"}, "problem": {"type": "string"}}}},
    "issues": {"type": "array", "items": {"type": "string"}}, "feedback": {"type": "string"}}}
MIN_CANDIDATES = 60          # candidates kept after the filters: at least this, or 5 per article requested
QUERIES_EN = (4, 10)         # how many search queries in English, min and max
QUERIES_PT = (2, 6)          # how many search queries in Portuguese, min and max


async def retrieve(terms: dict, log: EventLog, max_candidates: int) -> list[dict]:
    """Code searches OpenAlex and Crossref, keeps works with a DOI and an abstract, ranks them by how many searches
    found them, and keeps only journal articles in the period, confirmed in Crossref."""
    y1, y2 = terms["year_from"], terms["year_to"]
    hits: dict[str, dict] = {}
    async with httpx.AsyncClient() as client:
        for q in terms["queries_en"] + terms["queries_pt"]:
            for connector, search in (("openalex", openalex_search), ("crossref", crossref_search)):
                res = await search(client, q, y1, y2)
                log.emit("det_search", connector=connector, query=q, results=len(res))
                for w in res:
                    if w["doi"] and len(w["abstract"]) >= 200:
                        rec = hits.setdefault(w["doi"], dict(w, hits=0))
                        rec["hits"] += 1
                        if len(w["abstract"]) > len(rec["abstract"]):   # keep the fuller abstract of the two sources
                            rec["abstract"] = w["abstract"]
        ranked = sorted(hits.values(), key=lambda w: (-w["hits"], -(w["relevance"] or 0)))
        kept, dropped = [], {"not_journal": 0, "out_of_period": 0, "no_crossref": 0}
        for w in ranked:
            if len(kept) >= max_candidates:
                break
            cr = await crossref(client, w["doi"])
            if not cr:
                dropped["no_crossref"] += 1
            elif cr["type"] != "journal-article":
                dropped["not_journal"] += 1
            elif not any(y1 <= y <= y2 for y in cr["years"]):
                dropped["out_of_period"] += 1
            else:
                kept.append(dict(w, crossref=cr, id=f"C{len(kept) + 1:02d}"))
    log.emit("det_filter", unique=len(hits), kept=len(kept), dropped=dropped)
    return kept


async def run(topic: dict, run_dir: Path, log: EventLog) -> None:
    req = topic["request_pt"]
    n_wanted = topic.get("n_wanted", N_WANTED)
    q_en, q_pt = QUERIES_EN, QUERIES_PT

    async def terms_exec(attempt, history):
        r = await run_agent(log=log, name="n3-terms", role="executor", system_prompt=read_prompt(PROMPTS / "terms.md"),
                            user_prompt=(f"PEDIDO DO PESQUISADOR:\n{req}\n\n{history_block(history)}\n\nEntregue os "
                                         f"termos: de {q_en[0]} a {q_en[1]} consultas em inglês e de {q_pt[0]} a "
                                         f"{q_pt[1]} em português."),
                            tools=[], schema=TERMS_SCHEMA, max_turns=6, timeout_s=600, extra={"step": "terms"})
        return r.structured if isinstance(r.structured, dict) else None

    def terms_gate(t):
        issues = []
        if not (q_en[0] <= len(t["queries_en"]) <= q_en[1]):
            issues.append(f"{len(t['queries_en'])} consultas em inglês; o pedido é de {q_en[0]} a {q_en[1]}")
        if not (q_pt[0] <= len(t["queries_pt"]) <= q_pt[1]):
            issues.append(f"{len(t['queries_pt'])} consultas em português; o pedido é de {q_pt[0]} a {q_pt[1]}")
        for q in t["queries_en"] + t["queries_pt"]:
            if not (2 <= len(q.split()) <= 8):
                issues.append(f"consulta com tamanho fora de 2 a 8 palavras: '{q}'")
        if not (1990 <= t["year_from"] <= t["year_to"] <= 2026):
            issues.append(f"período inválido: {t['year_from']} a {t['year_to']}")
        return issues

    async def terms_verify(t):
        return await verify_step(log, "n3-terms-verifier", "terms", verifier_text("n3_terms"),
                                 f"PEDIDO DO PESQUISADOR:\n{req}\n\nTERMOS E CRITÉRIOS A VERIFICAR:\n{dump(t)}",
                                 web=False)

    log.emit("step_start", step="terms", label="IA decide os termos", mode="ai")
    terms = await qa_step(log, "terms", "IA decide os termos", terms_exec, terms_verify, terms_gate,
                          checks_pt="se as consultas e os critérios cobrem o pedido e se o período é o do pedido",
                          gate_pt=f"de {q_en[0]} a {q_en[1]} consultas em inglês e de {q_pt[0]} a {q_pt[1]} em "
                                  f"português, curtas, período válido")
    if not terms.approved:
        return write_final(run_dir, None, "paused", paused_at="terms")

    log.emit("step_start", step="retrieve", label="Código busca, filtra e confere no Crossref", mode="det")
    cands = await retrieve(terms.output, log, max(MIN_CANDIDATES, 5 * n_wanted))
    (run_dir / "candidates.json").write_text(dump(cands), encoding="utf-8")
    log.emit("step_end", step="retrieve", candidates=len(cands))
    if not cands:
        return write_final(run_dir, None, "failed", errors=["nenhum candidato depois dos filtros"])
    by_id = {c["id"]: c for c in cands}
    view = [{"id": c["id"], "title": c["title"], "year": c["year"], "venue": c["venue"], "abstract": c["abstract"][:1800]}
            for c in cands]
    criteria = {"include": terms.output["include"], "exclude": terms.output["exclude"]}

    async def screen_exec(attempt, history):
        r = await run_agent(log=log, name="n3-screener", role="executor", system_prompt=read_prompt(PROMPTS / "screener.md"),
                            user_prompt=(f"PEDIDO DO PESQUISADOR:\n{req}\n\nCRITÉRIOS APROVADOS:\n{dump(criteria)}\n\n"
                                         f"CANDIDATOS:\n{dump(view)}\n\n{history_block(history)}\n\n"
                                         f"Decida cada um e escolha até {n_wanted}."),
                            tools=[], schema=SCREEN_SCHEMA, max_turns=6, timeout_s=1200, extra={"step": "screen"})
        return r.structured if isinstance(r.structured, dict) else None

    def screen_gate(s):
        included = {d["id"] for d in s["decisions"] if d["include"]}
        issues = [f"{i}: id que não existe" for i in s["selected"] if i not in by_id]
        issues += [f"{i}: escolhido sem ter sido incluído na triagem" for i in s["selected"] if i not in included]
        want = min(n_wanted, len(included))
        if len(set(s["selected"])) != want:
            issues.append(f"{len(set(s['selected']))} escolhidos; deviam ser {want}")
        return issues

    async def screen_verify(s):
        chosen = [dict(by_id[i], reason=next((d["reason"] for d in s["decisions"] if d["id"] == i), ""))
                  for i in s["selected"] if i in by_id]
        material = (f"PEDIDO DO PESQUISADOR:\n{req}\n\nCRITÉRIOS:\n{dump(criteria)}\n\nARTIGOS INCLUÍDOS, COM O RESUMO "
                    f"BAIXADO POR CÓDIGO:\n" + dump([{k: c[k] for k in ("id", "title", "year", "venue", "abstract", "reason")}
                                                   for c in chosen]))
        v = await verify_step(log, "n3-screen-verifier", "screen", verifier_text("n3_screen"), material,
                              schema=PER_ID_VERDICT, web=False)
        return drop_rejected(v, s["selected"], lambda i: i)

    log.emit("step_start", step="screen", label="IA faz a triagem pelos resumos", mode="ai")
    screen = await qa_step(log, "screen", "IA faz a triagem pelos resumos", screen_exec, screen_verify, screen_gate,
                           checks_pt="se cada artigo escolhido atende a cada critério, lendo o resumo baixado",
                           gate_pt="ids existentes, escolhidos entre os incluídos, na quantidade pedida")
    if not screen.approved:
        return write_final(run_dir, None, "paused", paused_at="screen")
    selected = [by_id[i] for i in screen.output["selected"]]
    sel_view = [{"id": c["id"], "title": c["title"], "abstract": c["abstract"]} for c in selected]

    tries = {"n": 0}

    async def extract_exec(attempt, history):
        tries["n"] = attempt
        r = await run_agent(log=log, name="n3-extractor", role="executor", system_prompt=read_prompt(PROMPTS / "extractor.md"),
                            user_prompt=(f"PEDIDO DO PESQUISADOR:\n{req}\n\nARTIGOS:\n{dump(sel_view)}\n\n"
                                         f"{history_block(history)}\n\nExtraia os dados de cada um."),
                            tools=[], schema=EXTRACT_SCHEMA, max_turns=6, timeout_s=1200, extra={"step": "extract"})
        return r.structured if isinstance(r.structured, dict) else None

    def item_issues(it) -> list:
        c = by_id.get(it["id"])
        if not c:
            return [f"{it['id']}: id que não existe"]
        out = []
        q = norm(it["abstract_quote"]).strip(' "\'')
        if len(q) < 40 or q not in norm(c["abstract"]):
            out.append(f"{it['id']}: o trecho citado não está no resumo, letra por letra")
        s = norm(it["sample_size"]).strip(' "\'.')
        if s != norm(NOT_REPORTED):
            nums = numbers_in(it["sample_size"])
            if s not in norm(c["abstract"]) and (not nums or nums - numbers_in(c["abstract"])):
                out.append(f"{it['id']}: a amostra '{it['sample_size']}' não está no resumo; copie um trecho "
                           f"curto e literal, ou escreva '{NOT_REPORTED}'")
        return out

    def extract_gate(e):
        if tries["n"] >= 3:
            # from the third attempt on, code drops the articles whose quote or sample still fails
            dropped = [it["id"] for it in e["items"] if item_issues(it)]
            e["items"] = [it for it in e["items"] if not item_issues(it)]
            if dropped:
                log.emit("det_drop", step="extract", ids=dropped,
                         reason="citação ou amostra ainda fora do resumo na terceira tentativa")
            return [] if e["items"] else ["nenhum artigo com citação conferida"]
        ids = {it["id"] for it in e["items"]}
        issues = [f"{c['id']}: faltou extrair" for c in selected if c["id"] not in ids]
        for it in e["items"]:
            issues += item_issues(it)
        return issues

    async def extract_verify(e):
        material = (f"PEDIDO DO PESQUISADOR:\n{req}\n\nRESUMOS BAIXADOS POR CÓDIGO:\n{dump(sel_view)}\n\n"
                    f"DADOS EXTRAÍDOS A VERIFICAR:\n{dump(e)}")
        v = await verify_step(log, "n3-extract-verifier", "extract", verifier_text("n3_extract"), material,
                              schema=PER_ID_VERDICT, web=False)
        return drop_rejected(v, e["items"], lambda it: it["id"])

    log.emit("step_start", step="extract", label="IA extrai os dados dos resumos", mode="ai")
    ext = await qa_step(log, "extract", "IA extrai os dados dos resumos", extract_exec, extract_verify, extract_gate,
                        checks_pt="se método, amostra e achado dizem o que o resumo diz",
                        gate_pt="código confere a citação no resumo, letra por letra, e os números da amostra")
    if not ext.approved:
        return write_final(run_dir, None, "paused", paused_at="extract")

    log.emit("step_start", step="assemble", label="Código monta as referências", mode="det")
    items = []
    for it in ext.output["items"]:
        c, cr = by_id[it["id"]], by_id[it["id"]]["crossref"]
        items.append({"doi": c["doi"], "title": cr["title"] or c["title"], "authors": cr["authors"] or c["authors"],
                      "year": min(y for y in cr["years"] if terms.output["year_from"] <= y <= terms.output["year_to"]),
                      "venue": cr["venue"] or c["venue"], **{k: it[k] for k in ("study_type", "method", "sample_size",
                                                                                "main_finding", "abstract_quote")}})
    log.emit("det_validate", items=len(items), quotes_checked=len(items))
    write_final(run_dir, items, "done",
                attempts={"terms": terms.attempts, "screen": screen.attempts, "extract": ext.attempts})
