"""What the four agents share: the output schema, the answer format, the verifier's instructions and helpers.

Every level answers the same request with the same 9 fields per article, so the evaluation is the same for all.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from core.events import EventLog
from core.llm import run_agent

from .scholar import norm_doi

N_WANTED = 25   # articles requested per run
WEB = ["WebSearch", "WebFetch"]
VERIFIER_PROMPT = Path(__file__).resolve().parent / "prompts" / "verifier.md"

ITEM = {
    "type": "object",
    "properties": {
        "doi": {"type": "string"}, "title": {"type": "string"},
        "authors": {"type": "array", "items": {"type": "string"}}, "year": {"type": "integer"},
        "venue": {"type": "string"}, "study_type": {"type": "string"}, "method": {"type": "string"},
        "sample_size": {"type": "string"}, "main_finding": {"type": "string"}, "abstract_quote": {"type": "string"},
    },
    "required": ["doi", "title", "authors", "year", "venue", "study_type", "method", "sample_size",
                 "main_finding", "abstract_quote"],
}
FINAL_SCHEMA = {"type": "object", "properties": {"items": {"type": "array", "items": ITEM},
                                                  "search_notes": {"type": "string"}},
                "required": ["items", "search_notes"]}
FORMAT_PT = (
    "\n\nFORMATO DA RESPOSTA (igual para todos): no esquema pedido, um item por artigo, com doi (só o identificador, "
    "por exemplo 10.1000/xyz123), title, authors (lista de nomes), year (número), venue (periódico), study_type, "
    "method, sample_size (como aparece no resumo, ou \"não informado no resumo\"), main_finding e abstract_quote "
    "(trecho literal do resumo, sem aspas externas); e search_notes, com o que você fez e o que ficou de fora.")
PER_ITEM_VERDICT = {"type": "object", "properties": {
    "approved": {"type": "boolean"}, "checked": {"type": "array", "items": {"type": "string"}},
    "per_item": {"type": "array", "items": {"type": "object", "properties": {
        "doi": {"type": "string"}, "ok": {"type": "boolean"}, "problem": {"type": "string"}}}},
    "issues": {"type": "array", "items": {"type": "string"}}, "feedback": {"type": "string"}}}
NOT_REPORTED = "não informado no resumo"


def read_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def verifier_text(key: str) -> str:
    """The verifier's instructions for one step, from benchmark/prompts/verifier.md (one ## section per step)."""
    blocks = re.split(r"^## (\w+)\s*$", read_prompt(VERIFIER_PROMPT), flags=re.M)
    return dict(zip(blocks[1::2], (b.strip() for b in blocks[2::2])))[key]


def dump(x) -> str:
    return json.dumps(x, ensure_ascii=False, indent=1)


def write_final(run_dir: Path, items: list | None, status: str, **extra) -> None:
    (run_dir / "final.json").write_text(dump({"status": status, "report": {"items": items} if items is not None
                                              else None, **extra}), encoding="utf-8")


def numbers_in(text: str) -> set:
    return {n.replace(".", "").replace(",", "") for n in re.findall(r"\d[\d.,]*\d|\d", text or "")}


def drop_rejected(v: dict | None, items: list, key_of) -> dict | None:
    """Articles the verifier rejects leave the list and the step goes on with the rest, as a careful researcher
    drops a doubtful article. The step is rejected only for a problem that is not about one article, or if nothing
    is left."""
    if not v:
        return v
    bad_items = [p for p in v.get("per_item") or [] if not p.get("ok")]
    bad = {str(p.get("doi") or p.get("id") or "").lower() for p in bad_items}
    if bad:
        items[:] = [it for it in items if str(key_of(it)).lower() not in bad]
        v["per_item"] = [p for p in v.get("per_item") or [] if p.get("ok")]
        v["checked"] = (v.get("checked") or []) + [f"retirado da lista: {p.get('doi') or p.get('id')}: "
                                                   f"{p.get('problem', '')}" for p in bad_items]
        item_words = [str(p.get("doi") or p.get("id") or "") for p in bad_items]
        v["issues"] = [i for i in v.get("issues") or [] if not any(w and w in i for w in item_words)]
        v["approved"] = bool(items) and not v["issues"]
    return v


def doi_issues(items: list, field: str = "doi") -> list:
    issues, seen = [], set()
    for it in items:
        d = norm_doi(it.get(field, ""))
        if not d:
            issues.append(f"DOI ausente ou malformado: '{it.get(field, '')}' ({it.get('title', '')[:60]})")
        elif d in seen:
            issues.append(f"DOI repetido: {d}")
        seen.add(d)
    return issues


async def run_single_agent(level: str, system_prompt: str, topic: dict, run_dir: Path, log: EventLog) -> None:
    """Levels 0 and 1: one agent with web search and page fetch, and no one checking it."""
    n = topic.get("n_wanted", N_WANTED)
    log.emit("step_start", step="single", label="Agente único", mode="ai")
    r = await run_agent(log=log, name=f"{level}-agent", role="single", system_prompt=system_prompt,
                        user_prompt=topic["request_pt"] + FORMAT_PT, tools=WEB, schema=FINAL_SCHEMA,
                        max_turns=90 + 5 * n, timeout_s=2700 + 90 * n)
    out = r.structured if isinstance(r.structured, dict) else None
    log.emit("step_end", step="single", items=len((out or {}).get("items", [])))
    write_final(run_dir, (out or {}).get("items"), "done" if out else "failed",
                notes=(out or {}).get("search_notes", ""), errors=r.errors[:3])
