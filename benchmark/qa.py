"""Quality-control loop of levels 2 and 3, with an independent verifier from another vendor.

execute (Claude Sonnet 5.5) -> deterministic gate -> verifier (GLM-5.3 Flash, Zhipu) -> approved? done : the
verifier's reasons go back to the executor. Up to MAX_ATTEMPTS attempts per step; after the last rejection the
verifier refuses for good and the pipeline pauses.

Every step announces who executes, who verifies (model and effort) and what the verifier checks there, and every
verdict carries what was checked and the reasons in plain language, so a viewer can follow why a step failed.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

from core.config import EFFORT
from core.events import EventLog, clip

from .verifier import VERIFIER_EFFORT, VERIFIER_LABEL, run_verifier

MAX_ATTEMPTS = 5
EXECUTOR_LABEL = f"Claude Sonnet 5.5 (Anthropic), esforço {EFFORT}"
VERIFIER_FULL_LABEL = f"{VERIFIER_LABEL}, esforço {VERIFIER_EFFORT}"

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "approved": {"type": "boolean"},
        "checked": {"type": "array", "items": {"type": "string"}},
        "issues": {"type": "array", "items": {"type": "string"}},
        "feedback": {"type": "string"},
    },
}

VERIFIER_RULES = (
    "\n\nCOMO RESPONDER\n"
    "- approved: false só por ERRO REAL que compromete o resultado (dado errado, critério do pedido violado ou\n"
    "  esquecido, fonte que não existe, citação que não está na fonte, afirmação que a fonte não sustenta).\n"
    "  Sugestão de melhoria, preferência de estilo ou cobertura que poderia ser maior não reprova: aprove e ponha a\n"
    "  sugestão em feedback.\n"
    "- checked: o que você conferiu, um item por linha, concreto (por exemplo: 'DOI 10.x abre e o título confere').\n"
    "- issues: cada problema numa frase curta que um estudante entenda: o que está errado ou faltou, e onde.\n"
    "- feedback: o que o executor precisa fazer na próxima tentativa.\n"
    "- Escreva em português do Brasil, sem travessão."
)


@dataclass
class StepOutcome:
    step: str
    approved: bool
    output: Any
    attempts: int
    history: list = field(default_factory=list)


Executor = Callable[[int, list], Awaitable[Any]]
Verifier = Callable[[Any], Awaitable[dict]]
Gate = Callable[[Any], list]


async def verify_step(log: EventLog, name: str, step: str, instructions: str, material: str,
                             schema: dict | None = None, web: bool = True) -> dict | None:
    r = await run_verifier(log=log, name=name, prompt=instructions + VERIFIER_RULES + "\n\n" + material,
                           schema=schema or VERDICT_SCHEMA, web=web, extra={"step": step})
    return r.structured if isinstance(r.structured, dict) else None


async def qa_step(log: EventLog, step: str, label_pt: str, execute: Executor, verify: Verifier | None,
                  gate: Gate | None = None, checks_pt: str = "", gate_pt: str = "") -> StepOutcome:
    log.emit("step_roles", step=step, label=label_pt, executor=EXECUTOR_LABEL,
             verifier=VERIFIER_FULL_LABEL if verify else None, checks=checks_pt, gate=gate_pt)
    history: list[dict] = []
    output: Any = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        log.emit("step_attempt", step=step, label=label_pt, attempt=attempt, max_attempts=MAX_ATTEMPTS)
        output = await execute(attempt, history)
        if output is None:
            verdict = {"approved": False, "checked": [], "issues": ["o executor não entregou uma resposta válida"],
                       "feedback": "Entregue a resposta completa no esquema pedido.", "by": "gate"}
        else:
            gate_issues = gate(output) if gate else []
            if gate_issues:
                verdict = {"approved": False, "checked": [gate_pt] if gate_pt else [], "issues": gate_issues,
                           "feedback": "Corrija os problemas apontados pela checagem automática: "
                                       + "; ".join(gate_issues[:12]), "by": "gate"}
            elif verify is not None:
                # a verifier that fails to answer (network, provider) gets one more call before it counts
                verdict = await verify(output) or await verify(output) or {
                    "approved": False, "checked": [], "issues": ["o verificador não respondeu"], "feedback": "Refaça."}
                verdict["by"] = "verifier"
                bad = [p for p in verdict.get("per_item") or [] if not p.get("ok")]
                if bad:
                    verdict["approved"] = False
                    if not verdict.get("issues"):
                        verdict["issues"] = [f"{p.get('doi') or p.get('id')}: {p.get('problem', '')}" for p in bad]
                elif not verdict.get("approved") and not verdict.get("issues"):
                    verdict["approved"] = True   # a rejection must state a reason; without one it does not count
            else:
                verdict = {"approved": True, "checked": [gate_pt] if gate_pt else [], "issues": [], "feedback": "",
                           "by": "gate"}
        log.emit("qa_verdict", step=step, label=label_pt, attempt=attempt, approved=bool(verdict.get("approved")),
                 by=verdict.get("by"), checked=[clip(c, 200) for c in (verdict.get("checked") or [])[:8]],
                 issues=[clip(i, 240) for i in (verdict.get("issues") or [])[:8]],
                 feedback=clip(verdict.get("feedback", ""), 400))
        if verdict.get("approved"):
            return StepOutcome(step, True, output, attempt, history)
        history.append({"attempt": attempt, "issues": verdict.get("issues", []),
                        "feedback": verdict.get("feedback", ""), "by": verdict.get("by")})
    log.emit("pause", step=step, label=label_pt, attempts=MAX_ATTEMPTS,
             reason="o verificador recusou a quinta tentativa; o fluxo foi pausado",
             last_issues=[clip(i, 240) for i in (history[-1]["issues"] if history else [])[:5]],
             last_feedback=clip(history[-1]["feedback"] if history else "", 400))
    return StepOutcome(step, False, output, MAX_ATTEMPTS, history)


def history_block(history: list) -> str:
    if not history:
        return ""
    lines = ["HISTÓRICO DE REPROVAÇÕES DESTE PASSO (corrija cada ponto; não repita o erro):"]
    for h in history:
        who = "checagem automática" if h.get("by") == "gate" else "verificador independente"
        lines.append(f"- Tentativa {h['attempt']} reprovada ({who}):")
        for issue in h.get("issues", [])[:12]:
            lines.append(f"  * {issue}")
        if h.get("feedback"):
            lines.append(f"  Retorno: {h['feedback']}")
    return "\n".join(lines)
