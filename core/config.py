"""Shared configuration for the research-agent benchmark."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cache"   # downloads, registry lookups and judgments, so a repeated run never pays twice

# Every AI call in the experiment uses the same model and effort, so the only
# independent variable is the architecture of the agent.
MODEL = "claude-sonnet-5-5"
EFFORT = "high"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/141.0 Safari/537.36 ufrj-research-agents/1.0"
)


def find_claude_exe() -> str:
    """Newest Claude Code binary shipped with the VS Code extension."""
    ext_root = Path.home() / ".vscode" / "extensions"
    best: tuple[tuple[int, ...], Path] | None = None
    for d in ext_root.glob("anthropic.claude-code-*-win32-x64"):
        m = re.search(r"claude-code-(\d+)\.(\d+)\.(\d+)", d.name)
        exe = d / "resources" / "native-binary" / "claude.exe"
        if m and exe.exists():
            version = tuple(int(x) for x in m.groups())
            if best is None or version > best[0]:
                best = (version, exe)
    if best is None:
        raise FileNotFoundError("claude.exe from the VS Code extension not found")
    return str(best[1])


def brave_api_key() -> str:
    """Brave Search key, read at runtime from the Claude Code MCP config. Never stored or logged."""
    env = os.environ.get("BRAVE_API_KEY")
    if env:
        return env
    cfg = json.loads((Path.home() / ".claude.json").read_text(encoding="utf-8"))
    return cfg["mcpServers"]["brave-search"]["env"]["BRAVE_API_KEY"]
