"""Level 1: one agent, the four layers described, no checking.

One agent receives instructions written in four layers (profile, memory, planning and action, prompts/level_1.md)
and the request, searches the web and reads pages guided by those layers, and nobody checks what it delivers.
"""
from __future__ import annotations

from pathlib import Path

from benchmark.common import read_prompt, run_single_agent
from core.events import EventLog

PROMPT = Path(__file__).resolve().parent / "prompts" / "level_1.md"


async def run(topic: dict, run_dir: Path, log: EventLog) -> None:
    await run_single_agent("n1", read_prompt(PROMPT), topic, run_dir, log)
