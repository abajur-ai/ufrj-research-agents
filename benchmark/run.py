"""Run one level on one topic: python -m benchmark.run --level n3 --topic a04 --tag mytest --rep 1

Writes agents/level_N/runs/<run_id>/: events.jsonl (live, read by the viewer), final.json (status and report),
meta.json (time, calls and tokens per role and per provider) and calls/ (every prompt and every answer).
The final status is done, paused (the verifier refused the fifth attempt of a step), failed or error.
"""
from __future__ import annotations

import argparse
import asyncio
import importlib
import json
import time
from collections import defaultdict
from pathlib import Path

from core.events import EventLog

from . import paths

TOPICS = Path(__file__).resolve().parent / "topics.json"
TITLES = {"n0": "Nível 0, uma frase, e mais nada", "n1": "Nível 1, um agente, sem conferência",
          "n2": "Nível 2, multiagente, com conferência", "n3": "Nível 3, multiagente com conferência, mais código"}


def load_topic(topic_id: str) -> dict:
    topics = json.loads(TOPICS.read_text(encoding="utf-8"))
    return next(t for t in topics if t["id"] == topic_id)


def summarize(run_dir: Path) -> dict:
    calls, tokens = defaultdict(int), defaultdict(int)
    for line in (run_dir / "events.jsonl").read_text(encoding="utf-8").splitlines():
        ev = json.loads(line)
        if ev.get("kind") == "ai_call_end":
            who = f"{ev.get('role')}:{ev.get('provider', 'anthropic')}"
            calls[who] += 1
            for k in ("input_tokens", "output_tokens", "cache_read", "cache_write"):
                tokens[f"{ev.get('provider', 'anthropic')}:{k}"] += ev.get(k) or 0
    return {"calls": dict(calls), "tokens": dict(tokens), "calls_total": sum(calls.values())}


async def run_one(level: str, topic_id: str, tag: str = "mytest", rep: int = 1) -> str:
    topic = load_topic(topic_id)
    run_id = paths.make_run_id(tag, level, topic_id, rep)
    run_dir = paths.run_dir(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    log = EventLog(run_dir)
    log.emit("run_start", run_id=run_id, level=level, item=topic_id, title=TITLES[level], request=topic["request_pt"])
    started = time.time()
    status = "error"
    try:
        agent = importlib.import_module(f"agents.level_{level[1]}.agent")
        await agent.run(topic, run_dir, log)
        status = json.loads((run_dir / "final.json").read_text(encoding="utf-8")).get("status", "error")
    except Exception as exc:  # recorded and re-raised for the runner
        log.emit("run_error", message=f"{type(exc).__name__}: {str(exc)[:400]}")
        raise
    finally:
        wall = round(time.time() - started, 1)
        log.emit("run_end", status=status, wall_seconds=wall)
        meta = {"run_id": run_id, "level": level, "item": topic_id, "rep": rep, "status": status,
                "wall_seconds": wall, **summarize(run_dir)}
        (run_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return run_id


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", required=True, choices=list(TITLES))
    ap.add_argument("--topic", required=True, help="topic id from benchmark/topics.json, a01 to a06")
    ap.add_argument("--tag", default="mytest")
    ap.add_argument("--rep", type=int, default=1)
    a = ap.parse_args()
    print(asyncio.run(run_one(a.level, a.topic, a.tag, a.rep)))


if __name__ == "__main__":
    main()
