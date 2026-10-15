"""Judge call shared by the three judges of the jury, through OpenRouter (the default model is the single judge,
DeepSeek V4 Pro; evaluation/evaluate.py sets the model with --judge).

The key is read at run time from the user environment (OPENROUTER_API_KEY) and never written to disk or logs.
Responses are cached by prompt hash, so re-running the evaluation never pays twice for the same judgment.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
from pathlib import Path

import httpx

from core.config import CACHE_DIR

JUDGE_MODEL = "deepseek/deepseek-v4-pro"
JUDGE_EFFORT = "high"
JUDGE_LABEL = "DeepSeek V4 Pro (DeepSeek), esforço high"
CACHE = CACHE_DIR / "judge"
_sem = asyncio.Semaphore(6)


def _key() -> str:
    k = os.environ.get("OPENROUTER_API_KEY")
    if not k and os.name == "nt":
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
            k = winreg.QueryValueEx(h, "OPENROUTER_API_KEY")[0]
    return k


async def judge(client: httpx.AsyncClient, system: str, user: str, schema: dict, name: str = "judgment") -> dict | None:
    body = {"model": JUDGE_MODEL, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "reasoning": {"effort": JUDGE_EFFORT}, "temperature": 0,
            "response_format": {"type": "json_schema", "json_schema": {"name": name, "strict": True, "schema": schema}}}
    h = hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    f = CACHE / f"{h}.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))["parsed"]
    async with _sem:
        for attempt in range(4):
            try:
                r = await client.post("https://openrouter.ai/api/v1/chat/completions", json=body, timeout=300,
                                      headers={"Authorization": f"Bearer {_key()}", "X-Title": "ufrj-research-agents"})
            except httpx.HTTPError:
                await asyncio.sleep(5 * (attempt + 1))
                continue
            if r.status_code != 200:
                await asyncio.sleep(5 * (attempt + 1))
                continue
            data = r.json()
            try:
                parsed = json.loads(data["choices"][0]["message"]["content"])
            except (KeyError, IndexError, TypeError, json.JSONDecodeError):
                await asyncio.sleep(2)
                continue
            CACHE.mkdir(exist_ok=True)
            f.write_text(json.dumps({"parsed": parsed, "usage": data.get("usage"), "model": data.get("model")},
                                    ensure_ascii=False), encoding="utf-8")
            return parsed
    return None


if __name__ == "__main__":   # live check: one cheap call
    async def _main():
        schema = {"type": "object", "additionalProperties": False, "required": ["label", "reason"],
                  "properties": {"label": {"type": "string", "enum": ["supported", "partial", "unsupported"]},
                                 "reason": {"type": "string"}}}
        async with httpx.AsyncClient() as c:
            out = await judge(c, "Você julga se o RESUMO sustenta o ACHADO. Use só o resumo.",
                              "RESUMO: We surveyed 1,200 adults; 42% shared at least one false headline.\n"
                              "ACHADO: 42% dos 1.200 adultos compartilharam ao menos uma manchete falsa.", schema, "probe")
        assert out and out["label"] == "supported", out
        print("ok", out)
    asyncio.run(_main())
