"""Level 0: one sentence, and nothing else.

One agent receives a one-sentence instruction (prompts/level_0.md) and the request, searches the web and reads pages
by itself, and nobody checks what it delivers.
"""
from __future__ import annotations

from pathlib import Path

from benchmark.common import read_prompt, run_single_agent
from core.events import EventLog

PROMPT = Path(__file__).resolve().parent / "prompts" / "level_0.md"


async def run(topic: dict, run_dir: Path, log: EventLog) -> None:
    await run_single_agent("n0", read_prompt(PROMPT), topic, run_dir, log)
