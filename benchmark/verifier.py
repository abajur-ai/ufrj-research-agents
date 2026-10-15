"""Independent verifier through OpenRouter: GLM-5.3 Flash (Zhipu), effort high, with two tools of ours.

A different vendor from the Claude executor (Anthropic) and from the judge (DeepSeek), as Panickssery, Bowman and
Feng (NeurIPS 2024) require. Tools: web_search (Brave Search API, the key read at run time) and open_page (our own
HTTP fetch and text extraction). The verifier calls them as it wants; then a last call forces the verdict into a
JSON schema. Every search, page, token and dollar is logged. The OpenRouter key is read at run time.
"""
from __future__ import annotations

import asyncio
import json
import time

import httpx

from core.events import EventLog, clip
from core.llm import AgentResult
from core.sources import HEADERS
from evaluation.verify import _fetch_once

from evaluation.judge_llm import _key

VERIFIER_MODEL = "z-ai/glm-5.3-flash"
VERIFIER_EFFORT = "high"
VERIFIER_LABEL = "GLM-5.3 Flash (Zhipu)"
MAX_ROUNDS = 10
PAGE_CHARS = 9000
_sem = asyncio.Semaphore(4)
_brave_lock = asyncio.Lock()
_brave_last = 0.0

TOOLS = [
    {"type": "function", "function": {"name": "web_search", "description": "Busca na web (Brave). Devolve título, endereço e trecho de até 8 resultados.",
                                      "parameters": {"type": "object", "properties": {"query": {"type": "string"}},
                                                     "required": ["query"]}}},
    {"type": "function", "function": {"name": "open_page", "description": "Abre um endereço e devolve o texto da página (até 9.000 caracteres).",
                                      "parameters": {"type": "object", "properties": {"url": {"type": "string"}},
                                                     "required": ["url"]}}},
]


FINAL_ASK = ("Agora entregue o parecer final no esquema pedido, com base no que você encontrou. Preencha TODOS os campos: "
             "em checked, cada coisa que você conferiu e o que viu (por exemplo: 'abri doi.org/10.x: o título é Y'); em "
             "issues, cada problema encontrado, numa frase que um estudante entenda (lista vazia só se aprovar); em "
             "feedback, o que o executor deve fazer. Se houver lista por item no esquema, preencha um elemento por item.")


def strict_schema(schema: dict) -> dict:
    """Structured output wants every object closed and every property required."""
    s = dict(schema)
    if s.get("type") == "object":
        props = {k: strict_schema(v) for k, v in s.get("properties", {}).items()}
        s.update(properties=props, required=list(props), additionalProperties=False)
    elif s.get("type") == "array" and isinstance(s.get("items"), dict):
        s["items"] = strict_schema(s["items"])
    return s


async def _web_search(client: httpx.AsyncClient, query: str) -> str:
    global _brave_last
    from core.config import brave_api_key
    for attempt in range(3):
        async with _brave_lock:   # free plan: about one request per second
            wait = 1.15 - (time.time() - _brave_last)
            if wait > 0:
                await asyncio.sleep(wait)
            try:
                r = await client.get("https://api.search.brave.com/res/v1/web/search", params={"q": query, "count": 8},
                                     headers={"Accept": "application/json", "X-Subscription-Token": brave_api_key()},
                                     timeout=30)
            except httpx.HTTPError:
                r = None
            _brave_last = time.time()
        if r is not None and r.status_code == 200:
            items = (r.json().get("web") or {}).get("results") or []
            return "\n".join(f"- {i.get('title', '')} | {i.get('url', '')} | {clip(i.get('description', ''), 300)}"
                             for i in items) or "(nenhum resultado)"
        await asyncio.sleep(2 * (attempt + 1))
    return "(a busca falhou; tente outra consulta)"


async def _open_page(client: httpx.AsyncClient, url: str) -> str:
    url = "".join(url.split())   # the model sometimes breaks a long URL across lines
    try:
        rec = await _fetch_once(client, url, timeout=40)
    except (httpx.InvalidURL, ValueError):
        return f"(endereço inválido: {url[:200]})"
    text = (rec.get("text") or rec.get("raw") or "").strip()
    if rec.get("status") != 200 or not text:
        return f"(a página não abriu: HTTP {rec.get('status')})"
    return clip(text, PAGE_CHARS)


async def _post(client: httpx.AsyncClient, body: dict, result: AgentResult, timeout_s: int) -> dict:
    for attempt in range(4):
        try:
            r = await client.post("https://openrouter.ai/api/v1/chat/completions", json=body, timeout=timeout_s,
                                  headers={"Authorization": f"Bearer {_key()}", "X-Title": "LabIA benchmark"})
        except httpx.HTTPError as exc:
            result.errors.append(type(exc).__name__)
            await asyncio.sleep(5 * (attempt + 1))
            continue
        if r.status_code == 200:
            return r.json()
        result.errors.append(f"HTTP {r.status_code}: {clip(r.text, 200)}")
        await asyncio.sleep(5 * (attempt + 1))
    return {}


async def run_verifier(*, log: EventLog, name: str, prompt: str, schema: dict, web: bool = True,
                       extra: dict | None = None, timeout_s: int = 300) -> AgentResult:
    calls_dir = log.run_dir / "calls"
    calls_dir.mkdir(parents=True, exist_ok=True)
    call_id = f"{len(list(calls_dir.glob('*.result.json'))) + 1:03d}-{name}"
    (calls_dir / f"{call_id}.prompt.md").write_text(prompt, encoding="utf-8")
    result = AgentResult(name=name)
    started = time.time()
    log.emit("ai_call_start", call=call_id, name=name, role="verifier", provider="zhipu", model=VERIFIER_MODEL,
             effort=VERIFIER_EFFORT, tools=["web_search", "open_page"] if web else [], **(extra or {}))
    messages = [{"role": "user", "content": prompt}]
    cost, tin, tout, searches, pages = 0.0, 0, 0, 0, 0
    async with _sem, httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
        if web:
            for _ in range(MAX_ROUNDS):
                data = await _post(client, {"model": VERIFIER_MODEL, "messages": messages, "tools": TOOLS,
                                            "reasoning": {"effort": VERIFIER_EFFORT}}, result, timeout_s)
                if not data:
                    break
                u = data.get("usage") or {}
                cost += u.get("cost") or 0
                tin += u.get("prompt_tokens") or 0
                tout += u.get("completion_tokens") or 0
                msg = (data.get("choices") or [{}])[0].get("message") or {}
                calls = msg.get("tool_calls") or []
                messages.append({k: v for k, v in msg.items() if k in ("role", "content", "tool_calls")})
                if not calls:
                    break
                for tc in calls:
                    fn = tc.get("function") or {}
                    try:
                        args = json.loads(fn.get("arguments") or "{}")
                    except json.JSONDecodeError:
                        args = {}
                    if fn.get("name") == "web_search":
                        searches += 1
                        q = str(args.get("query", ""))
                        log.emit("ai_tool", call=call_id, name=name, role="verifier", tool="WebSearch", input={"query": clip(q, 200)})
                        result.tool_calls.append({"name": "WebSearch", "input": {"query": q}})
                        out = await _web_search(client, q)
                    else:
                        pages += 1
                        url = str(args.get("url", ""))
                        log.emit("ai_tool", call=call_id, name=name, role="verifier", tool="WebFetch", input={"url": url})
                        result.tool_calls.append({"name": "WebFetch", "input": {"url": url}})
                        out = await _open_page(client, url)
                    messages.append({"role": "tool", "tool_call_id": tc.get("id"), "content": out})
            messages.append({"role": "user", "content": FINAL_ASK})
        data = await _post(client, {"model": VERIFIER_MODEL, "messages": messages, "reasoning": {"effort": VERIFIER_EFFORT},
                                    "response_format": {"type": "json_schema", "json_schema": {
                                        "name": "verdict", "strict": True, "schema": strict_schema(schema)}}},
                           result, timeout_s)
        u = (data or {}).get("usage") or {}
        cost += u.get("cost") or 0
        tin += u.get("prompt_tokens") or 0
        tout += u.get("completion_tokens") or 0
    msg = (((data or {}).get("choices") or [{}])[0].get("message") or {})
    result.text = msg.get("content") or ""
    try:
        result.structured = json.loads(result.text) if result.text else None
    except json.JSONDecodeError:
        result.structured = None
    result.is_error = result.structured is None
    result.usage = {"input_tokens": tin, "output_tokens": tout, "cost_usd": round(cost, 5)}
    result.duration_s = round(time.time() - started, 2)
    (calls_dir / f"{call_id}.result.json").write_text(json.dumps(
        {"structured": result.structured, "text": result.text, "usage": result.usage, "duration_s": result.duration_s,
         "errors": result.errors, "tool_calls": result.tool_calls, "model": VERIFIER_MODEL, "effort": VERIFIER_EFFORT},
        ensure_ascii=False, indent=2), encoding="utf-8")
    log.emit("ai_call_end", call=call_id, name=name, role="verifier", provider="zhipu", model=VERIFIER_MODEL,
             effort=VERIFIER_EFFORT, duration_s=result.duration_s, is_error=result.is_error, errors=result.errors[:3],
             input_tokens=tin, output_tokens=tout, web_searches=searches, pages=pages, cost_usd=round(cost, 5))
    return result


if __name__ == "__main__":   # live check: one call with the web, a few cents at most
    async def _main():
        import tempfile
        from pathlib import Path
        log = EventLog(Path(tempfile.mkdtemp(prefix="verifier-check-", dir=None)))
        schema = {"type": "object", "properties": {"approved": {"type": "boolean"},
                                                   "checked": {"type": "array", "items": {"type": "string"}},
                                                   "issues": {"type": "array", "items": {"type": "string"}},
                                                   "feedback": {"type": "string"}}}
        r = await run_verifier(log=log, name="probe", schema=schema, prompt=(
            "Você é um verificador. Use as ferramentas para conferir: o artigo 'Fact-checking misinformation on "
            "WhatsApp' tem o DOI 10.1037/xge0001234? Aprove só se o DOI existir e corresponder ao título. Português."))
        assert r.structured is not None, r.errors
        assert r.structured["approved"] is False, r.structured
        print("ok", r.duration_s, "s", r.usage, r.structured["issues"][:1])
    asyncio.run(_main())
