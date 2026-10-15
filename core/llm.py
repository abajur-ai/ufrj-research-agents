"""One isolated Claude agent call through the Agent SDK, streamed into the run's event log.

Isolation: setting_sources=[] keeps the machine's CLAUDE.md, MCP servers and hooks out of the
experiment; no-session-persistence keeps transcripts out of ~/.claude/projects.
"""
from __future__ import annotations

import asyncio
import base64
import json
import re
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from claude_agent_sdk import ClaudeAgentOptions, query
from claude_agent_sdk.types import (
    AssistantMessage,
    RateLimitEvent,
    ResultMessage,
    ServerToolResultBlock,
    ServerToolUseBlock,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

from .config import EFFORT, MODEL, find_claude_exe
from .events import EventLog, clip

CLAUDE_EXE = find_claude_exe()

# Latest quota reading seen on any call, shared with the runner so it can slow down.
QUOTA: dict[str, Any] = {"utilization": None, "status": None, "type": None, "resets_at": None}


class RateLimited(RuntimeError):
    pass


@dataclass
class AgentResult:
    name: str
    structured: Any = None
    text: str = ""
    is_error: bool = False
    errors: list = field(default_factory=list)
    usage: dict = field(default_factory=dict)
    model_usage: dict = field(default_factory=dict)
    num_turns: int = 0
    duration_s: float = 0.0
    tool_calls: list = field(default_factory=list)

    @property
    def searches(self) -> list[str]:
        return [c["input"].get("query", "") for c in self.tool_calls if c["name"] == "WebSearch"]

    @property
    def fetched_urls(self) -> list[str]:
        return [c["input"].get("url", "") for c in self.tool_calls if c["name"] == "WebFetch"]


def kill_for(marker: str) -> None:
    """Stop claude.exe processes whose command line contains the marker (SDK cancel leaves them alive)."""
    ps = (
        "Get-CimInstance Win32_Process -Filter \"Name='claude.exe'\" | "
        f"Where-Object {{ $_.CommandLine -like '*{marker}*' }} | "
        "ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
    )
    encoded = base64.b64encode(ps.encode("utf-16-le")).decode()
    subprocess.run(["powershell", "-NoProfile", "-EncodedCommand", encoded], capture_output=True, timeout=60)


def _extract_json(text: str) -> Any:
    fence = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.S)
    candidates = fence or re.findall(r"(\{.*\})", text, flags=re.S)
    for c in reversed(candidates):
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def _tool_input_summary(name: str, data: dict) -> dict:
    if name == "WebSearch":
        return {"query": data.get("query", "")}
    if name == "WebFetch":
        return {"url": data.get("url", ""), "prompt": clip(data.get("prompt", ""), 200)}
    return {k: clip(v, 200) for k, v in data.items()}


async def run_agent(
    *,
    log: EventLog,
    name: str,
    role: str,
    system_prompt: str,
    user_prompt: str,
    tools: list[str] | None = None,
    schema: dict | None = None,
    max_turns: int = 40,
    timeout_s: int = 1500,
    extra: dict | None = None,
) -> AgentResult:
    """Run one agent call. `role` labels it in the log: executor, verifier, judge, single."""
    tools = tools or []
    run_dir = log.run_dir
    calls_dir = run_dir / "calls"
    calls_dir.mkdir(parents=True, exist_ok=True)
    seq = len(list(calls_dir.glob("*.system.md"))) + 1
    call_id = f"{seq:03d}-{name}"
    system_file = calls_dir / f"{call_id}.system.md"
    system_file.write_text(system_prompt, encoding="utf-8")
    (calls_dir / f"{call_id}.user.md").write_text(user_prompt, encoding="utf-8")
    work = run_dir / "work"
    work.mkdir(parents=True, exist_ok=True)

    options = ClaudeAgentOptions(
        model=MODEL,
        effort=EFFORT,
        system_prompt={"type": "file", "path": str(system_file)},
        tools=tools,
        allowed_tools=tools,
        setting_sources=[],
        # Without these two, every MCP server and claude.ai connector of the account is loaded into the
        # context (about 330k tokens per call, measured 13/10/2026); with them the base context is ~600 tokens.
        strict_mcp_config=True,
        mcp_servers={},
        max_turns=max_turns,
        cli_path=CLAUDE_EXE,
        cwd=str(work),
        extra_args={"no-session-persistence": None},
        max_buffer_size=64 * 1024 * 1024,
        output_format={"type": "json_schema", "schema": schema} if schema else None,
    )
    result = AgentResult(name=name)
    started = time.time()
    log.emit("ai_call_start", call=call_id, name=name, role=role, tools=tools, **(extra or {}))

    async def consume() -> None:
        async for msg in query(prompt=user_prompt, options=options):
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock) and block.text.strip():
                        log.emit("ai_text", call=call_id, name=name, role=role, text=clip(block.text, 500))
                    elif isinstance(block, (ToolUseBlock, ServerToolUseBlock)):
                        inp = _tool_input_summary(block.name, block.input or {})
                        result.tool_calls.append({"name": block.name, "input": inp})
                        log.emit("ai_tool", call=call_id, name=name, role=role, tool=block.name, input=inp)
            elif isinstance(msg, UserMessage) and isinstance(msg.content, list):
                for block in msg.content:
                    if isinstance(block, (ToolResultBlock, ServerToolResultBlock)):
                        is_err = bool(getattr(block, "is_error", False))
                        log.emit("ai_tool_result", call=call_id, name=name, role=role,
                                 is_error=is_err, preview=clip(block.content, 240))
            elif isinstance(msg, RateLimitEvent):
                info = msg.rate_limit_info
                QUOTA.update(utilization=info.utilization, status=info.status,
                             type=info.rate_limit_type, resets_at=info.resets_at)
                log.emit("quota", status=info.status, utilization=info.utilization,
                         limit_type=info.rate_limit_type, resets_at=info.resets_at)
                if info.status == "rejected":
                    raise RateLimited(f"quota rejected ({info.rate_limit_type}), resets at {info.resets_at}")
            elif isinstance(msg, ResultMessage):
                result.is_error = bool(msg.is_error)
                result.errors = list(msg.errors or [])
                result.usage = dict(msg.usage or {})
                result.model_usage = dict(msg.model_usage or {})
                result.num_turns = msg.num_turns or 0
                result.text = msg.result or ""
                result.structured = msg.structured_output

    try:
        await asyncio.wait_for(consume(), timeout=timeout_s)
    except asyncio.TimeoutError:
        kill_for(call_id)
        result.is_error = True
        result.errors.append(f"timeout after {timeout_s}s")
    except RateLimited:
        kill_for(call_id)
        raise
    except Exception as exc:  # SDK gave up (e.g. invalid structured output after its own retries)
        kill_for(call_id)
        result.is_error = True
        result.errors.append(f"{type(exc).__name__}: {str(exc)[:300]}")
        result.structured = None
        log.emit("ai_call_error", call=call_id, name=name, role=role, message=str(exc)[:300])
    finally:
        result.duration_s = round(time.time() - started, 2)

    if result.structured is None and schema and result.text:
        result.structured = _extract_json(result.text)
    (calls_dir / f"{call_id}.result.json").write_text(
        json.dumps({"structured": result.structured, "text": result.text, "usage": result.usage,
                    "num_turns": result.num_turns, "duration_s": result.duration_s,
                    "is_error": result.is_error, "errors": result.errors,
                    "tool_calls": result.tool_calls}, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8")
    log.emit("ai_call_end", call=call_id, name=name, role=role, duration_s=result.duration_s,
             turns=result.num_turns, is_error=result.is_error, errors=result.errors[:3],
             input_tokens=result.usage.get("input_tokens"), output_tokens=result.usage.get("output_tokens"),
             cache_read=result.usage.get("cache_read_input_tokens"),
             cache_write=result.usage.get("cache_creation_input_tokens"))
    return result
