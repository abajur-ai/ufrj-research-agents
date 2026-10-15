"""Level 2: multi-agent, with checking.

Three steps, each with its own agent and instructions: the search plan (prompts/planner.md), the search and screening
(prompts/searcher.md) and the data extraction (prompts/extractor.md). Every step goes through a deterministic gate in
code and then through the verifier (QA), a model from another company, with its own web search and page fetch. A
rejected step returns to the executor with the verifier's reasons, up to five attempts; on the fifth rejection the run
pauses and delivers no report. An article the verifier rejects leaves the list and the step goes on with the rest.
"""
from __future__ import annotations

from pathlib import Path

from benchmark.common import (FINAL_SCHEMA, FORMAT_PT, N_WANTED, PER_ITEM_VERDICT, WEB, doi_issues, drop_rejected,
                              dump, read_prompt, verifier_text, write_final)
from benchmark.qa import history_block, qa_step, verify_step
from benchmark.scholar import norm_doi
from core.events import EventLog
from core.llm import run_agent

PROMPTS = Path(__file__).resolve().parent / "prompts"

PLAN_SCHEMA = {"type": "object", "properties": {
    "criteria": {"type": "array", "items": {"type": "string"}},
    "queries": {"type": "array", "items": {"type": "object", "properties": {
        "query": {"type": "string"}, "language": {"type": "string"}, "database": {"type": "string"}},
        "required": ["query", "language", "database"]}},
    "how_to_check": {"type": "array", "items": {"type": "string"}}},
    "required": ["criteria", "queries", "how_to_check"]}
CAND = {"type": "object", "properties": {
    "doi": {"type": "string"}, "title": {"type": "string"}, "authors": {"type": "array", "items": {"type": "string"}},
    "year": {"type": "integer"}, "venue": {"type": "string"}, "checked_url": {"type": "string"},
    "criteria_met": {"type": "array", "items": {"type": "string"}}},
    "required": ["doi", "title", "authors", "year", "venue", "checked_url", "criteria_met"]}
CANDS_SCHEMA = {"type": "object", "properties": {"candidates": {"type": "array", "items": CAND},
                                                  "notes": {"type": "string"}}, "required": ["candidates", "notes"]}


async def run(topic: dict, run_dir: Path, log: EventLog) -> None:
    req = topic["request_pt"]
    n_wanted = topic.get("n_wanted", N_WANTED)
    turns, secs = 80 + 5 * n_wanted, 2400 + 90 * n_wanted

    async def plan_exec(attempt, history):
        r = await run_agent(log=log, name="n2-planner", role="executor", system_prompt=read_prompt(PROMPTS / "planner.md"),
                            user_prompt=f"PEDIDO DO PESQUISADOR:\n{req}\n\n{history_block(history)}\n\nEntregue o plano.",
                            tools=[], schema=PLAN_SCHEMA, max_turns=6, timeout_s=600, extra={"step": "plan"})
        return r.structured if isinstance(r.structured, dict) else None

    async def plan_verify(plan):
        return await verify_step(log, "n2-plan-verifier", "plan", verifier_text("plan"),
                                 f"PEDIDO DO PESQUISADOR:\n{req}\n\nPLANO A VERIFICAR:\n{dump(plan)}", web=False)

    log.emit("step_start", step="plan", label="Plano da busca", mode="ai")
    plan = await qa_step(log, "plan", "Plano da busca", plan_exec, plan_verify,
                         checks_pt="se o plano cobre todos os critérios do pedido (tema, período, tipo, método, recorte)")
    if not plan.approved:
        return write_final(run_dir, None, "paused", paused_at="plan")

    approved: list = []
    last: dict = {}

    async def search_exec(attempt, history):
        prev = ""
        if last:
            prev = "LISTA DA TENTATIVA ANTERIOR E PARECER DO VERIFICADOR, ARTIGO POR ARTIGO:\n" + dump(last)
        r = await run_agent(log=log, name="n2-searcher", role="executor", system_prompt=read_prompt(PROMPTS / "searcher.md"),
                            user_prompt=(f"PEDIDO DO PESQUISADOR:\n{req}\n\nPLANO APROVADO:\n{dump(plan.output)}\n\n"
                                         f"{prev}\n\n{history_block(history)}\n\nEntregue os candidatos."),
                            tools=WEB, schema=CANDS_SCHEMA, max_turns=turns, timeout_s=secs, extra={"step": "search"})
        return r.structured if isinstance(r.structured, dict) else None

    def search_gate(out):
        c = out.get("candidates") or []
        issues = doi_issues(c)
        if not c:
            issues.append("nenhum candidato")
        return issues

    async def search_verify(out):
        v = await verify_step(log, "n2-search-verifier", "search", verifier_text("search"),
                              f"PEDIDO DO PESQUISADOR:\n{req}\n\nCANDIDATOS A VERIFICAR:\n{dump(out)}",
                              schema=PER_ITEM_VERDICT, web=True)
        if v:
            last.clear()
            last.update(candidates=list(out["candidates"]), verdict=v.get("per_item", []))
            # a candidate the verifier rejects leaves the list and the rest goes on;
            # a candidate the verifier does not mention is not a rejection
            v = drop_rejected(v, out["candidates"], lambda c: norm_doi(c.get("doi", "")))
            approved[:] = out["candidates"]
        return v

    log.emit("step_start", step="search", label="Busca e triagem", mode="ai")
    search = await qa_step(log, "search", "Busca e triagem", search_exec, search_verify, search_gate,
                           checks_pt="se cada DOI existe e corresponde a título, autores, ano e periódico, e se cada "
                                     "artigo atende a todos os critérios do pedido",
                           gate_pt="DOI bem formado, sem repetição, pelo menos um candidato")
    if not search.approved:
        return write_final(run_dir, None, "paused", paused_at="search")
    approved_dois = {norm_doi(c["doi"]) for c in approved}

    async def extract_exec(attempt, history):
        r = await run_agent(log=log, name="n2-extractor", role="executor", system_prompt=read_prompt(PROMPTS / "extractor.md"),
                            user_prompt=(f"PEDIDO DO PESQUISADOR:\n{req}\n\nCANDIDATOS APROVADOS:\n{dump(approved)}\n\n"
                                         f"{history_block(history)}\n\nEscolha {min(n_wanted, len(approved))} e extraia."
                                         f"{FORMAT_PT}"),
                            tools=WEB, schema=FINAL_SCHEMA, max_turns=turns, timeout_s=secs, extra={"step": "extract"})
        return r.structured if isinstance(r.structured, dict) else None

    def extract_gate(out):
        items = out.get("items") or []
        issues = doi_issues(items)
        want = min(n_wanted, len(approved))
        if len(items) != want:
            issues.append(f"{len(items)} artigos; deviam ser {want}")
        for it in items:
            if norm_doi(it.get("doi", "")) not in approved_dois:
                issues.append(f"{it.get('doi')}: fora da lista aprovada na triagem")
            if len(it.get("abstract_quote", "").strip()) < 40:
                issues.append(f"{it.get('doi')}: trecho do resumo ausente ou curto demais")
        return issues

    async def extract_verify(out):
        v = await verify_step(log, "n2-extract-verifier", "extract", verifier_text("extract"),
                              f"PEDIDO DO PESQUISADOR:\n{req}\n\nLISTA FINAL A VERIFICAR:\n{dump(out)}",
                              schema=PER_ITEM_VERDICT, web=True)
        return drop_rejected(v, out["items"], lambda it: norm_doi(it.get("doi", "")))

    log.emit("step_start", step="extract", label="Extração dos dados", mode="ai")
    ext = await qa_step(log, "extract", "Extração dos dados", extract_exec, extract_verify, extract_gate,
                        checks_pt="se a citação está no resumo letra por letra, se a amostra e o método estão certos "
                                  "e se o achado diz só o que o resumo diz",
                        gate_pt="a quantidade pedida, todos da lista aprovada, com trecho do resumo")
    if not ext.approved:
        return write_final(run_dir, None, "paused", paused_at="extract")
    write_final(run_dir, ext.output["items"], "done", notes=ext.output.get("search_notes", ""),
                attempts={"plan": plan.attempts, "search": search.attempts, "extract": ext.attempts})
