"""Append-only event log per run. The live viewer and the evaluator read it."""
from __future__ import annotations

import json
import threading
import time
from pathlib import Path
from typing import Any


class EventLog:
    def __init__(self, run_dir: Path):
        self.run_dir = Path(run_dir).resolve()
        self.path = self.run_dir / "events.jsonl"
        self.started = time.time()
        self._lock = threading.Lock()
        self.run_dir.mkdir(parents=True, exist_ok=True)

    def emit(self, kind: str, **payload: Any) -> dict:
        now = time.time()
        event = {"ts": round(now, 3), "t": round(now - self.started, 3), "kind": kind, **payload}
        line = json.dumps(event, ensure_ascii=False, default=str)
        with self._lock:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
        return event


def clip(text: Any, limit: int = 600) -> str:
    s = text if isinstance(text, str) else json.dumps(text, ensure_ascii=False, default=str)
    s = " ".join(s.split())
    return s if len(s) <= limit else s[: limit - 1] + "…"
