"""Three-company jury, majority per criterion: python -m evaluation.jury mytest

For every run of the tag judged by all three judges (DeepSeek V4 Pro, Qwen3.7 Plus and Gemini 3.1 Flash-Lite), each
delivered article gets the majority vote of the judges on every criterion (on topic, empirical, method as stated,
finding supported by the abstract); the article is correct when the code checks pass and the jury approves every
criterion (Verga et al., 2024). Writes agents/level_N/evaluations/jury/<run_id>.json in the evaluator's format, so
evaluation/report.py and evaluation/stats.py read it like any judge.
"""
from __future__ import annotations

import argparse
import json

from benchmark import paths

CODE_CHECKS = ("doi_exists", "title_ok", "year_ok", "author_ok", "venue_ok", "in_period", "journal_article", "quote_ok")


def code_ok(it: dict) -> bool:
    return all(it["checks"].get(k) for k in CODE_CHECKS) and it["checks"].get("sample_ok") is not False


def judge_ok(j: dict) -> bool:
    return bool(j.get("on_topic") and j.get("empirical") and j.get("method_ok") and j.get("finding") == "supported")


def majority(judgments: list[dict]) -> dict:
    vote = lambda f: sum(bool(f(j)) for j in judgments) >= 2
    return {"on_topic": vote(lambda j: j.get("on_topic")), "empirical": vote(lambda j: j.get("empirical")),
            "method_ok": vote(lambda j: j.get("method_ok")),
            "finding": "supported" if vote(lambda j: j.get("finding") == "supported") else "partial"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tag")
    a = ap.parse_args()
    n_runs = n_items = 0
    for f in paths.eval_files(paths.JUDGES[0], a.tag):
        files = [paths.eval_file(j, f.stem) for j in paths.JUDGES]
        if not all(x.exists() for x in files):
            continue
        recs = [json.loads(x.read_text(encoding="utf-8")) for x in files]
        by_doi = [{it["doi"]: it for it in r["items"]} for r in recs]
        items = []
        for it in recs[0]["items"]:
            js = [b.get(it["doi"], {}).get("judge") for b in by_doi]
            jury = majority([j for j in js if j]) if all(js) else None
            items.append({**it, "judge": jury, "correct": bool(jury) and code_ok(it) and judge_ok(jury)})
        rec = {**recs[0], "items": items, "correct": sum(i["correct"] for i in items),
               "judge": "júri: DeepSeek V4 Pro, Qwen3.7 Plus, Gemini 3.1 Flash-Lite (maioria)"}
        rec["precision"] = rec["correct"] / rec["delivered"] if rec["delivered"] else None
        rec["yield"] = rec["correct"] / rec["requested"]
        out = paths.eval_file(paths.JURY, f.stem)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
        n_runs += 1
        n_items += len(items)
    print(f"jury: {n_runs} runs, {n_items} articles")


if __name__ == "__main__":
    main()
