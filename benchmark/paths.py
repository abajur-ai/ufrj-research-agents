"""Where each run and each evaluation lives.

Every level is isolated in its own folder: agents/level_N/runs/<run_id>/ holds the run, and
agents/level_N/evaluations/<judge>/<run_id>.json holds its evaluation by each judge and by the jury.
A run id is <tag>-<level>-<topic>-r<rep>, for example class-n3-a04-r1.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("n0", "n1", "n2", "n3")
JUDGES = ("judge-deepseek", "judge-qwen", "judge-gemini")
JURY = "jury"
RUN_ID = re.compile(r"^(?P<tag>.+)-(?P<level>n[0-3])-(?P<topic>a\d\d)-r(?P<rep>\d+)$")


def make_run_id(tag: str, level: str, topic: str, rep: int) -> str:
    return f"{tag}-{level}-{topic}-r{rep}"


def parse(run_id: str) -> dict:
    m = RUN_ID.match(run_id)
    if not m:
        raise ValueError(f"not a run id: {run_id}")
    return m.groupdict()


def level_dir(level: str) -> Path:
    return ROOT / "agents" / f"level_{level[1]}"


def run_dir(run_id: str) -> Path:
    return level_dir(parse(run_id)["level"]) / "runs" / run_id


def eval_dir(judge: str, level: str) -> Path:
    return level_dir(level) / "evaluations" / judge


def eval_file(judge: str, run_id: str) -> Path:
    return eval_dir(judge, parse(run_id)["level"]) / f"{run_id}.json"


def runs(prefix: str = "") -> list[Path]:
    """Finished runs whose id starts with prefix, across the four levels."""
    return sorted(d for lv in LEVELS for d in (level_dir(lv) / "runs").glob(f"{prefix}*")
                  if d.is_dir() and (d / "meta.json").exists())


def eval_files(judge: str, tag: str) -> list[Path]:
    """Evaluations of one judge (or of the jury) for every run of a tag, across the four levels."""
    return sorted(f for lv in LEVELS for f in eval_dir(judge, lv).glob(f"{tag}-*.json")
                  if RUN_ID.match(f.stem) and parse(f.stem)["tag"] == tag)
