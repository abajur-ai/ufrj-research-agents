"""Per-article test of the level comparison: python -m evaluation.stats class

Logistic regression, one row per delivered article: correct ~ level + topic (topic fixed effects pair the levels),
with standard errors clustered by run, since the articles of one run are not independent, and t critical values with
G - 1 degrees of freedom (Cameron and Miller 2015, section VI). For each comparison between levels: the odds ratio and
its two-sided p, and the p after Holm correction over the comparisons (Holm 1979). Run for the jury (the main
measure), for the single judge and for the code-only checks (no judge). Writes evaluation/STATISTICS.md and
evaluation/STATISTICS.pt-BR.md for the class runs, or STATISTICS_<tag>.md for any other tag.
"""
from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from benchmark import paths

from .jury import code_ok

HERE = Path(__file__).resolve().parent
PAIRS = (("n1", "n0"), ("n2", "n1"), ("n3", "n2"), ("n3", "n1"), ("n3", "n0"))


def items_frame(judge: str, tag: str, code_only: bool = False) -> pd.DataFrame:
    rows = []
    for f in paths.eval_files(judge, tag):
        r = json.loads(f.read_text(encoding="utf-8"))
        for it in r.get("items", []):
            ok = code_ok(it) if code_only else bool(it.get("correct"))
            rows.append({"run": r["run_id"], "level": r["level"], "topic": r["item"], "correct": int(ok)})
    return pd.DataFrame(rows)


def holm(ps: list[float]) -> list[float]:
    """Holm step-down adjustment: sort the p values, multiply each by the number of comparisons still open, keep the
    sequence non-decreasing and cap it at 1."""
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, run_max = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        run_max = max(run_max, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run_max
    return adj


def logit(df: pd.DataFrame):
    df = df.copy()
    df["level"] = pd.Categorical(df["level"], categories=sorted(df["level"].unique()))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return smf.logit("correct ~ C(level) + C(topic)", df).fit(
            disp=False, cov_type="cluster", cov_kwds={"groups": pd.factorize(df["run"])[0]}, use_t=True)


def contrast(fit, a: str, b: str) -> tuple[float, float]:
    """Odds ratio of level a over level b and its two-sided p (Wald, errors clustered by run)."""
    name = lambda lv: f"C(level)[T.{lv}]"
    vec = np.zeros(len(fit.params))
    for lv, sign in ((a, 1), (b, -1)):
        if name(lv) in fit.params.index:
            vec[list(fit.params.index).index(name(lv))] += sign
    t = fit.t_test(vec)
    return float(np.exp(t.effect[0])), float(t.pvalue)


def section(title: str, df: pd.DataFrame, pt_br: bool) -> list[str]:
    T = (lambda en, pt: pt) if pt_br else (lambda en, pt: en)
    lv_name = lambda lv: T(f"Level {lv[1]}", f"Nível {lv[1]}")
    prec = df.groupby(["topic", "run", "level"])["correct"].mean().groupby(["topic", "level"]).mean().groupby("level").mean()
    out = [f"## {title}", "",
           T(f"{len(df)} articles, {df['run'].nunique()} runs with a report, {df['topic'].nunique()} topics. "
             "Mean precision per level: ", f"{len(df)} artigos, {df['run'].nunique()} rodadas com relatório, "
             f"{df['topic'].nunique()} temas. Precisão média por nível: ")
           + ", ".join(f"{lv_name(lv)} {v * 100:.0f}%" for lv, v in prec.items()) + ".", "",
           T("| Comparison | Odds ratio | p | p Holm |", "| Comparação | Razão de chances | p | p Holm |"),
           "| --- | --- | --- | --- |"]
    present = set(df["level"]) if len(df) else set()
    pairs = [(a, b) for a, b in PAIRS if a in present and b in present]
    if not pairs or df["topic"].nunique() < 2 and len(present) < 2:
        # comparing levels needs runs of at least two levels
        return out[:3] + [T("Comparing levels needs runs of at least two levels.",
                            "Comparar níveis exige rodadas de pelo menos dois níveis."), ""]
    fit = logit(df)
    con = [contrast(fit, a, b) for a, b in pairs]
    adj = holm([p for _, p in con])
    for (a, b), (orr, p), ph in zip(pairs, con, adj):
        out.append(f"| {lv_name(a)} {T('vs', 'contra')} {lv_name(b)} | {orr:.2f} | {p:.4f} | {ph:.4f} |")
    return out + [""]


def stats_md(tag: str, pt_br: bool = False) -> str:
    T = (lambda en, pt: pt) if pt_br else (lambda en, pt: en)
    lines = [f"[{T('Leia em português', 'Read in English')}]({T('STATISTICS.pt-BR.md', 'STATISTICS.md')})", "",
             T(f"# Statistics of the `{tag}` runs", f"# Estatística das rodadas `{tag}`"), "",
             T("Logistic regression per article (correct ~ level + topic), standard errors clustered by run, t critical "
               "values with G - 1 degrees of freedom (Cameron and Miller 2015, section VI); Holm correction over the five "
               "comparisons of each block (Holm 1979). Generated by `python -m evaluation.stats`.",
               "Regressão logística por artigo (acerto ~ nível + tema), erro-padrão agrupado por rodada, valores críticos "
               "t com G - 1 graus de liberdade (Cameron e Miller 2015, seção VI); correção de Holm sobre as cinco "
               "comparações de cada bloco (Holm 1979). Gerado por `python -m evaluation.stats`."), ""]
    lines += section(T("Jury of three companies, majority per criterion (main measure)",
                       "Júri de três empresas, maioria por critério (medida principal)"), items_frame(paths.JURY, tag), pt_br)
    lines += section(T("Single judge (DeepSeek V4 Pro), for comparison", "Juiz único (DeepSeek V4 Pro), para comparar"),
                     items_frame(paths.JUDGES[0], tag), pt_br)
    lines += section(T("Code checks only (no judge)", "Só o que o código confere (sem juiz)"),
                     items_frame(paths.JUDGES[0], tag, code_only=True), pt_br)
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tag")
    a = ap.parse_args()
    # the class statistics are evaluation/STATISTICS.md; any other tag gets its own file
    stem = "STATISTICS" if a.tag == "class" else f"STATISTICS_{a.tag}"
    en = stats_md(a.tag).replace("(STATISTICS.pt-BR.md)", f"({stem}.pt-BR.md)")
    pt = stats_md(a.tag, pt_br=True).replace("(STATISTICS.md)", f"({stem}.md)")
    (HERE / f"{stem}.md").write_text(en, encoding="utf-8", newline="\n")
    (HERE / f"{stem}.pt-BR.md").write_text(pt, encoding="utf-8", newline="\n")
    print(stats_md(a.tag))


if __name__ == "__main__":
    main()
