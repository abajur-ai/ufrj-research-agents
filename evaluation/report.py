"""Results report: python -m evaluation.report class

Reads the evaluations of every run of a tag, by the jury (the main measure) and by the single judge (the comparison),
and writes evaluation/REPORT.md (English) and evaluation/REPORT.pt-BR.md for the class runs, or REPORT_<tag>.md and
REPORT_<tag>.pt-BR.md for any other tag. With --deck PATH it also refreshes, in a
slide deck, the blocks /* BEGIN BENCH_<TAG> */ ... /* END BENCH_<TAG> */ (single judge) and BENCH_<TAG>_JURY (jury).

Analysis: per topic, the mean over the two repetitions; per level, the mean over topics with a 95% Student t interval
over topics (G - 1 degrees of freedom, the choice for few groups in Cameron and Miller 2015, section VI), clipped to
the range the metric can take. Cost of a run: the executor at Anthropic's public API price for Claude Sonnet 5.5
(tokens and web searches) plus the verifier at the cost OpenRouter charged, converted to BRL at the Banco Central PTAX
selling rate of 14/10/2026.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, stdev

from scipy.stats import t as t_dist

from benchmark import paths

HERE = Path(__file__).resolve().parent
LEVELS = paths.LEVELS
PAIRS = (("n1", "n0"), ("n2", "n1"), ("n3", "n2"), ("n3", "n0"), ("n3", "n1"))
PROPORTIONS = ("precision", "precisionCode", "yield")
REQUESTED = 25
# Claude Sonnet 5.5 public API price, USD per million tokens (platform.claude.com/docs/en/about-claude/pricing);
# web searches at USD 10 per 1,000; the verifier at the cost OpenRouter reports for each call.
SONNET_USD_PER_MTOK = {"input": 2.0, "write_5m": 2.5, "write_1h": 4.0, "cache_read": 0.10, "output": 10.0}
WEB_SEARCH_USD = 10.0 / 1000
USD_BRL, FX_DATE = 5.0441, "14/10/2026"
CODE_CHECKS = ("doi_exists", "title_ok", "year_ok", "author_ok", "venue_ok", "in_period", "journal_article", "quote_ok")
# why a delivered article is not 100% right; one article can fail several checks
FAILS = {
    "doi": (("DOI does not exist", "DOI inexistente"), lambda c, j: c.get("doi_exists") is False),
    "meta": (("Data error (title, year, author, journal)", "Erro de dado (título, ano, autor, revista)"),
             lambda c, j: any(c.get(k) is False for k in ("title_ok", "year_ok", "author_ok", "venue_ok"))),
    "scope": (("Out of scope (period, type, topic)", "Fora do recorte (período, tipo, tema)"),
              lambda c, j: c.get("in_period") is False or c.get("journal_article") is False or j.get("on_topic") is False),
    "empirical": (("Not empirical or wrong method", "Não empírico ou método errado"),
                  lambda c, j: j.get("empirical") is False or j.get("method_ok") is False),
    "quote": (("Quote or sample not in the abstract", "Citação ou amostra fora do resumo"),
              lambda c, j: c.get("quote_ok") is False or c.get("sample_ok") is False),
    "finding": (("Finding beyond the abstract", "Achado além do resumo"),
                lambda c, j: j.get("finding") in ("partial", "unsupported")),
}


def run_cost_usd(run_id: str) -> float:
    run = paths.run_dir(run_id)
    cost = 0.0
    for f in (run / "calls").glob("*.result.json"):
        if "verifier" in f.name:
            continue
        u = json.loads(f.read_text(encoding="utf-8")).get("usage") or {}
        cc = u.get("cache_creation") or {}
        w5, w1 = cc.get("ephemeral_5m_input_tokens") or 0, cc.get("ephemeral_1h_input_tokens") or 0
        if not cc:
            w5 = u.get("cache_creation_input_tokens") or 0
        p = SONNET_USD_PER_MTOK
        cost += ((u.get("input_tokens") or 0) * p["input"] + w5 * p["write_5m"] + w1 * p["write_1h"]
                 + (u.get("cache_read_input_tokens") or 0) * p["cache_read"] + (u.get("output_tokens") or 0) * p["output"]) / 1e6
    for line in (run / "events.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        if e.get("kind") == "ai_tool" and e.get("tool") == "WebSearch" and e.get("role") != "verifier":
            cost += WEB_SEARCH_USD
        elif e.get("kind") == "ai_call_end" and e.get("role") == "verifier":
            cost += e.get("cost_usd") or 0.0
    return cost


def precision_code(r: dict) -> float | None:
    """Precision with no judge at all: only what code checks (registry, period, type, quote and sample)."""
    if not r["delivered"]:
        return None
    ok = sum(all(it["checks"].get(k) for k in CODE_CHECKS) and it["checks"].get("sample_ok") is not False
             for it in r["items"])
    return ok / r["delivered"]


def tci(values: list[float], low: float | None = 0.0, high: float | None = None) -> dict:
    """Mean and 95% Student t interval over topics (n - 1 degrees of freedom), clipped to [low, high]."""
    if not values:
        return {"mean": None, "lo": None, "hi": None, "n": 0}
    m = mean(values)
    if len(values) < 2:
        return {"mean": m, "lo": None, "hi": None, "n": len(values)}
    h = t_dist.ppf(0.975, len(values) - 1) * stdev(values) / math.sqrt(len(values))
    lo, hi = m - h, m + h
    if low is not None:
        lo = max(lo, low)
    if high is not None:
        hi = min(hi, high)
    return {"mean": m, "lo": float(lo), "hi": float(hi), "n": len(values)}


def per_topic(recs: list[dict], key) -> dict[tuple[str, str], float]:
    by = defaultdict(list)
    for r in recs:
        v = key(r)
        if v is not None:
            by[(r["item"], r["level"])].append(v)
    return {k: mean(v) for k, v in by.items()}


def analyse(tag: str, judge: str) -> dict:
    recs = [json.loads(f.read_text(encoding="utf-8")) for f in paths.eval_files(judge, tag)]
    for r in recs:
        meta = json.loads((paths.run_dir(r["run_id"]) / "meta.json").read_text(encoding="utf-8"))
        r["tokens_k"] = sum(v for k, v in meta.get("tokens", {}).items()) / 1000
        r["calls_total"] = meta.get("calls_total", 0)
        r["cost_brl"] = run_cost_usd(r["run_id"]) * USD_BRL
    topics = sorted({r["item"] for r in recs})
    metrics = {"precision": lambda r: r["precision"], "precisionCode": precision_code, "yield": lambda r: r["yield"],
               "delivered": lambda r: r["delivered"], "correct": lambda r: r["correct"],
               "minutes": lambda r: r["wall_seconds"] / 60, "calls": lambda r: r["calls_total"],
               "tokensK": lambda r: r["tokens_k"], "costBRL": lambda r: r["cost_brl"]}
    pt = {m: per_topic(recs, f) for m, f in metrics.items()}
    levels = {}
    for lv in LEVELS:
        rs = [r for r in recs if r["level"] == lv]
        fails = Counter()
        for r in rs:
            for it in r.get("items", []):
                if not it.get("correct"):
                    for k, (_, test) in FAILS.items():
                        if test(it.get("checks", {}), it.get("judge") or {}):
                            fails[k] += 1
        levels[lv] = {m: tci([pt[m][(t, lv)] for t in topics if (t, lv) in pt[m]],
                             high=1.0 if m in PROPORTIONS else None) for m in metrics}
        levels[lv].update(runs=len(rs), noReport=sum(r["status"] != "done" for r in rs),
                          itemsDelivered=sum(r["delivered"] for r in rs), itemsCorrect=sum(r["correct"] for r in rs),
                          fails=dict(fails))
    paired = {}
    for m in PROPORTIONS:
        for a, b in PAIRS:
            d = [pt[m][(t, a)] - pt[m][(t, b)] for t in topics if (t, a) in pt[m] and (t, b) in pt[m]]
            paired[f"{m}:{a}-{b}"] = {k: (None if v is None else round(v * 100, 1)) if k != "n" else v
                                       for k, v in tci(d, low=-1.0, high=1.0).items()}
    by_topic = {t: {lv: pt["precision"].get((t, lv)) for lv in LEVELS} for t in topics}
    return {"tag": tag, "judge": judge, "runs": len(recs), "topics": topics, "levels": levels, "paired": paired,
            "byTopic": by_topic}


def split(x: dict) -> tuple[int, int, int]:
    """Of the 25 articles requested, in percent: right, wrong and not delivered, adding up to 100."""
    if x["correct"]["mean"] is None:   # every run of the level paused: nothing delivered
        return 0, 0, 100
    right = round(x["correct"]["mean"] / REQUESTED * 100)
    wrong = round((x["delivered"]["mean"] - x["correct"]["mean"]) / REQUESTED * 100)
    return right, wrong, 100 - right - wrong


def pct(v) -> str:
    return "-" if v is None else f"{v * 100:.0f}%"


def ci(m: dict, pt_br: bool) -> str:
    sep = "a" if pt_br else "to"
    if m["lo"] is None:   # one topic only: there is no interval over topics
        return pct(m["mean"])
    return f"{pct(m['mean'])} ({pct(m['lo'])} {sep} {pct(m['hi'])})"


def num(v: float, d: int, pt_br: bool) -> str:
    s = f"{v:.{d}f}"
    return s.replace(".", ",") if pt_br else s


def report_md(jury: dict, single: dict, pt_br: bool = False) -> str:
    T = (lambda en, pt: pt) if pt_br else (lambda en, pt: en)
    J, S = jury["levels"], single["levels"]
    lv_name = lambda lv: T(f"Level {lv[1]}", f"Nível {lv[1]}")
    levels = [lv for lv in LEVELS if J[lv]["runs"]]   # a tag may cover one level or all four
    out = [f"[{T('Leia em português', 'Read in English')}]({T('REPORT.pt-BR.md', 'REPORT.md')})", "",
           T(f"# Results of the `{jury['tag']}` runs", f"# Resultados das rodadas `{jury['tag']}`"), "",
           T(f"Runs: {jury['runs']}. Levels: {len(levels)}. Topics: {len(jury['topics'])}. 25 articles requested per run. "
             "Generated by `python -m evaluation.report`.",
             f"Rodadas: {jury['runs']}. Níveis: {len(levels)}. Temas: {len(jury['topics'])}. 25 artigos pedidos por rodada. "
             "Gerado por `python -m evaluation.report`."), "",
           T("## Precision: of the articles delivered, how many are 100% correct",
             "## Precisão: dos artigos entregues, quantos estão 100% certos"), "",
           T("Mean over topics, with the 95% interval (Student t over the topics).",
             "Média dos temas, com o intervalo de 95% (t de Student sobre os temas)."), "",
           T("| Level | Jury (main) | Single judge | Code only |", "| Nível | Júri (principal) | Juiz único | Só código |"),
           "| --- | --- | --- | --- |"]
    for lv in levels:
        out.append(f"| {lv_name(lv)} | {ci(J[lv]['precision'], pt_br)} | {ci(S[lv]['precision'], pt_br)} | "
                   f"{pct(J[lv]['precisionCode']['mean'])} |")
    out += ["", T("## Cost and outcome, mean per run", "## Custo e resultado, média por rodada"), "",
            T("Right, wrong and not delivered are 100% of the 25 articles requested, by the jury.",
              "Certos, errados e não entregues somam 100% dos 25 artigos pedidos, pelo júri."), "",
            T("| Level | Time | AI calls | Tokens | Cost | Right | Wrong | Not delivered | Paused runs |",
              "| Nível | Tempo | Chamadas de IA | Tokens | Custo | Certos | Errados | Não entregues | Rodadas pausadas |"),
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for lv in levels:
        x = J[lv]
        right, wrong, missing = split(x)
        tk = x["tokensK"]["mean"]
        tokens = (f"{num(tk / 1000, 1, pt_br)} {T('M', 'mi')}" if tk >= 1000 else f"{tk:.0f} {T('k', 'mil')}")
        out.append(f"| {lv_name(lv)} | {num(x['minutes']['mean'], 1, pt_br)} min | {num(x['calls']['mean'], 1, pt_br)} | "
                   f"{tokens} | R$ {num(x['costBRL']['mean'], 2, pt_br)} | {right}% | {wrong}% | {missing}% | "
                   f"{x['noReport']} {T('of', 'de')} {x['runs']} |")
    out += ["", T(f"Cost: Claude Sonnet 5.5 at Anthropic's public API price (tokens and web searches) plus the verifier at "
                  f"the cost OpenRouter charged; PTAX selling rate of {FX_DATE}, US$ 1 = R$ {USD_BRL}. A paused run is a "
                  "run whose verifier refused the fifth attempt of a step, so it delivered no report.",
                  f"Custo: Claude Sonnet 5.5 a preço público da API da Anthropic (tokens e buscas) mais o verificador pelo "
                  f"valor cobrado pela OpenRouter; PTAX de venda de {FX_DATE}, US$ 1 = R$ {num(USD_BRL, 4, True)}. Rodada "
                  "pausada: o verificador recusou a quinta tentativa de um passo, e a rodada não entregou relatório."), "",
            T("## Paired differences between levels, in points (jury)", "## Diferenças pareadas entre níveis, em pontos (júri)"),
            "", T("Per topic, then 95% Student t interval over the topics.", "Por tema, depois intervalo de 95% t de Student sobre os temas."), ""]
    if len(levels) < 2 or len(jury["topics"]) < 2:
        out.append(T("Needs runs of at least two levels on at least two topics.",
                     "Exige rodadas de pelo menos dois níveis em pelo menos dois temas."))
    for k, v in jury["paired"].items():
        if k.startswith("precision:") and v["mean"] is not None and v["lo"] is not None:
            a, b = k.split(":")[1].split("-")
            out.append(f"- {lv_name(a)} {T('over', 'sobre o')} {lv_name(b)}: {num(v['mean'], 1, pt_br)} "
                       f"({num(v['lo'], 1, pt_br)} {T('to', 'a')} {num(v['hi'], 1, pt_br)})")
    out += ["", T("## Precision per topic (jury)", "## Precisão por tema (júri)"), "",
            T("| Topic | ", "| Tema | ") + " | ".join(lv_name(lv) for lv in levels) + " |", "| --- |" + " --- |" * len(levels)]
    for t, row in jury["byTopic"].items():
        out.append(f"| {t} | " + " | ".join(pct(row[lv]) for lv in levels) + " |")
    out += ["", T("## Why a delivered article is not 100% right (jury; one article can fail several checks)",
                  "## Por que um artigo entregue não ficou 100% certo (júri; um artigo pode cair em mais de um)"), "",
            T("| Reason | ", "| Motivo | ") + " | ".join(lv_name(lv) for lv in levels) + " |", "| --- |" + " --- |" * len(levels)]
    for k, (names, _) in FAILS.items():
        out.append(f"| {names[1] if pt_br else names[0]} | " + " | ".join(str(J[lv]["fails"].get(k, 0)) for lv in levels) + " |")
    return "\n".join(out) + "\n"


def deck_block(res: dict, name: str) -> str:
    def m(x):
        f = lambda v: "null" if v is None else f"{v:.4f}"
        return f"{{ mean: {f(x['mean'])}, lo: {f(x['lo'])}, hi: {f(x['hi'])}, n: {x['n']} }}"
    lines = [f"/* BEGIN {name}: generated by evaluation/report.py; do not edit by hand. */",
             f"const {name} = {{", f"  runs: {res['runs']},", f"  topics: {len(res['topics'])},",
             f"  fx: {{ usdBrl: {USD_BRL}, date: '{FX_DATE}' }},", "  levels: {"]
    for lv, x in res["levels"].items():
        lines.append(f"    {lv}: {{ " + ", ".join(f"{k}: {m(x[k])}" for k in
                     ("precision", "precisionCode", "yield", "delivered", "correct", "minutes", "calls", "tokensK",
                      "costBRL"))
                     + f", runs: {x['runs']}, noReport: {x['noReport']}, itemsDelivered: {x['itemsDelivered']}, "
                     f"itemsCorrect: {x['itemsCorrect']}, fails: {json.dumps(x['fails'])} }},")
    lines.append("  },")
    lines.append("  paired: " + json.dumps({k: {"mean": v["mean"], "lo": v["lo"], "hi": v["hi"]}
                                            for k, v in res["paired"].items()}) + ",")
    lines.append("  byTopic: " + json.dumps({t: {lv: (None if v is None else round(v, 4)) for lv, v in row.items()}
                                             for t, row in res["byTopic"].items()}) + ",")
    lines += ["} as const;", f"/* END {name} */"]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tag")
    ap.add_argument("--deck", help="slide file whose BENCH_<TAG> blocks are refreshed with these numbers")
    a = ap.parse_args()
    jury, single = analyse(a.tag, paths.JURY), analyse(a.tag, paths.JUDGES[0])
    # the class report is evaluation/REPORT.md; any other tag gets its own file and never overwrites it
    stem = "REPORT" if a.tag == "class" else f"REPORT_{a.tag}"
    en = report_md(jury, single).replace("(REPORT.pt-BR.md)", f"({stem}.pt-BR.md)")
    pt = report_md(jury, single, pt_br=True).replace("(REPORT.md)", f"({stem}.md)")
    (HERE / f"{stem}.md").write_text(en, encoding="utf-8", newline="\n")
    (HERE / f"{stem}.pt-BR.md").write_text(pt, encoding="utf-8", newline="\n")
    if a.deck:
        path = Path(a.deck)
        src = path.read_text(encoding="utf-8")
        for res, name in ((single, f"BENCH_{a.tag.upper()}"), (jury, f"BENCH_{a.tag.upper()}_JURY")):
            block = deck_block(res, name)
            src, n = re.subn(rf"/\* BEGIN {name}\b.*?/\* END {name} \*/", lambda _: block, src, flags=re.S)
            assert n == 1, f"the deck has no block {name}"
        path.write_text(src, encoding="utf-8")
    print(report_md(jury, single))


if __name__ == "__main__":
    main()
