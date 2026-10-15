[Leia em português](README.pt-BR.md)

# Level 1: one agent, no checking

**The four layers described.** One agent, with its profile, memory, planning and action written out in the
instruction. It searches and reads on its own, guided by the four layers. Nobody checks what it delivers.

This README has two parts. Part 1 is for researchers. Part 2, [For AI agents](#part-2-for-ai-agents), is for an AI
coding agent that will run, test, debug or change this level.

# Part 1: for researchers

## What this level is

Level 1 is the second of the four architectures compared in the class benchmark. It has the same single agent, the
same model and the same tools as Level 0. The only difference is the instruction: instead of one sentence, it
describes the four layers of an agent (Wang et al. 2024) and what the agent does in each one.

The instruction opens with a priority that Level 0 never states: "Prefira entregar menos itens certos do que itens
duvidosos" (prefer delivering fewer correct items over doubtful ones).

## How it works, step by step

1. The agent receives the four-layer instruction, the request and the standard answer format.
2. It turns the request into inclusion criteria: topic, period, publication type, method, geographic or platform
   scope.
3. It searches academic databases and the web, in English and in Portuguese: the OpenAlex API, Crossref, SciELO and web
   search.
4. For each candidate, it opens the official record (DOI page, journal or OpenAlex) and checks title, authors, year,
   journal and publication type.
5. It reads the abstract, checks each criterion and discards what does not meet all of them.
6. It copies from the abstract the literal quote that supports the main finding and the sample size as written.
7. It delivers the final list, only with checked items. Nobody checks the list.

All of this happens inside one AI call: the agent decides how many searches and pages it needs.

Who does each task (deck page 22, Level 1 column):

| Task | Level 1 |
| --- | --- |
| Decide what to search for | AI |
| Search the articles | AI |
| Check DOI, year and type | AI |
| See if the article meets the request | AI |
| Extract method, sample and finding | AI |
| Check the quote in the abstract | Nobody |
| Build the reference | AI |

## The four layers in this level

Deck page 19, as written in `prompts/level_1.md`:

| Layer | In Level 1 |
| --- | --- |
| Profile | Who the agent is and what it prioritizes. An assistant that supports a literature review. Prefers delivering less to delivering wrong. |
| Memory | What it notes while working. A record card for each article it finds: where it checked each datum and what it decided. |
| Planning | The steps, in order, until delivery. Turns the request into criteria and searches the academic databases. Reads each abstract and discards what does not qualify. At the end, consolidates and delivers the report, only with what it checked. |
| Action | What it can use and the rules of use. Searches the web and opens the article pages. What it cannot check stays out. |

## What it receives, how it searches and reads, who checks

- **Receives:** instructions for the four layers, and the request.
- **Searches and reads:** alone, guided by the four layers.
- **Who checks:** nobody checks what it delivers.

## Results

The class benchmark: 4 levels x 6 topics x 2 repetitions = 48 runs, 12 per level. Each run asks for 25 peer-reviewed
empirical journal articles published 2018 to 2025, with 9 fields each. The executor is the same at every level (Claude
Sonnet 5.5); only the architecture changes.

**Precision** is the main metric: of the articles delivered, how many are 100% correct. One wrong field and the whole
article counts as wrong. Mean over the 6 topics, with the 95% interval (Student t over the topics):

| Level | Jury (main) | 95% interval | Single judge | 95% interval | Code checks only |
| --- | --- | --- | --- | --- | --- |
| 0 | 82% | 68 to 97% | 79% | 66 to 92% | 92% |
| **1** | **89%** | **83 to 96%** | **86%** | **77 to 94%** | **95%** |
| 2 | 90% | 78 to 100% | 86% | 77 to 95% | 98% |
| 3 | 97% | 94 to 100% | 94% | 88 to 100% | 99% |

The jury is three AI judges from three companies (DeepSeek V4 Pro, Qwen3.7 Plus, Gemini 3.1 Flash-Lite), blind to the
level, deciding by majority per criterion. The single judge is DeepSeek V4 Pro alone, on the same runs.

**Cost and outcome**, mean per run. Right, wrong and not delivered are shares of the 25 articles requested, by the jury; precision is the share of the articles delivered that are 100% correct:

| Level | Time | AI calls | Tokens | Cost per run | Right | Wrong | Not delivered | Precision (of delivered) | Paused runs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10.2 min | 1.0 | 2.2 M | R$ 7.11 | 80% | 17% | 3% | 82% | 0 of 12 |
| **1** | **17.0 min** | **1.0** | **4.2 M** | **R$ 9.84** | **82%** | **10%** | **8%** | **89%** | **0 of 12** |
| 2 | 42.1 min | 9.9 | 5.9 M | R$ 16.33 | 59% | 8% | 33% | 90% | 3 of 12 |
| 3 | 5.1 min | 7.0 | 146 k | R$ 2.90 | 81% | 2% | 17% | 97% | 0 of 12 |

Cost per run: Claude Sonnet 5.5 at Anthropic's public API price (tokens and web searches), converted at the Banco
Central PTAX selling rate of 14/10/2026, US$ 1 = R$ 5.0441. Level 1 has no verifier.

**How it compares.** Describing the agent well already helps a lot: over Level 0, precision rises from 82% to 89% and
wrong articles fall from 17% to 10%. Level 1 reaches the same precision as Level 2 (89% against 90%) in 17 min instead
of 42, for R$ 9.84 instead of R$ 16.33; Level 3 is more precise (97%), faster and cheaper.

## Watch it run

A real run of the example topic (a04, games against misinformation, like Bad News), repetition 1, replayed at 20x and
ending with the delivery.

[![Level 1 run on the example topic](media/level-1.jpg)](media/level-1.mp4)

Music: "Deliberate Thought", Kevin MacLeod (incompetech.com), CC BY 4.0.

## When to use this level

Use Level 1 when all you have is a chat or an agent with web search, and no verifier or code: writing the four layers
is the cheapest improvement over a one-sentence instruction. It serves a first, exploratory pass. Nobody checks its
list, and 10% of the articles requested came back wrong.

Human in the loop still applies: the agent speeds up, the researcher decides. Check in the original source every
article you will cite.

## Run only this level

Setup (Python, Claude Code) is in the [repository README](../../README.md). Running Level 1 needs only Claude Code
logged in; evaluating it needs `OPENROUTER_API_KEY` and `OPENALEX_API_KEY`. From the repository root, in PowerShell:

```
python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1
```

The run lands in `agents/level_1/runs/mytest-n1-a04-r1/`. To watch it, run `python -m http.server 8000` and open
`http://127.0.0.1:8000/viewer/index.html?run=mytest-n1-a04-r1&replay=1`.

## What you can edit

`prompts/level_1.md`, in Portuguese, plain text, with one section per layer (Perfil, Memória, Planejamento, Ação).
Change a rule, add a database, tighten a criterion, and rerun.

# Part 2: for AI agents

## Files of this level

| Path | What it does |
| --- | --- |
| `agent.py` | The Level 1 agent. Entry point: `run(topic, run_dir, log)`, a coroutine awaited by `benchmark/run.py`. `topic` is one entry of `benchmark/topics.json`, `run_dir` the run folder, `log` the event log from `core/`. One executor call: system prompt `prompts/level_1.md`, user prompt the topic's request plus the shared output format block, tools `WebSearch` and `WebFetch`, structured output in the final schema. |
| `prompts/level_1.md` | The system prompt: the four layers. Portuguese. |
| `runs/class-n1-<topic>-r<rep>/` | The 12 class runs: `events.jsonl`, `final.json`, `meta.json`, `calls/`. |
| `evaluations/judge-deepseek/` | One file per run: code checks plus the DeepSeek V4 Pro verdicts. |
| `evaluations/judge-qwen/` | Same, Qwen3.7 Plus. |
| `evaluations/judge-gemini/` | Same, Gemini 3.1 Flash-Lite. |
| `evaluations/jury/` | Majority of the three judges per criterion; the main measure. |
| `media/level-1.mp4`, `media/level-1.jpg` | Video of `class-n1-a04-r1` replayed at 20x, and its poster. |

## Shared modules it depends on

| Module | Used for |
| --- | --- |
| `benchmark/common.py` | The final schema (the 9-field item plus `search_notes`), the output format block appended to the request, `final.json` writing. The same schema and format block serve Level 0, so the two levels differ only in the system prompt. |
| `core/` | Executor call through the Claude Agent SDK (Claude Sonnet 5.5, effort high, the `claude.exe` of the Claude Code VS Code extension), the event log, configuration. |

Level 1 does not use `benchmark/qa.py`, `benchmark/verifier.py` or `benchmark/scholar.py` while running. The evaluator
uses `benchmark/scholar.py` to check its references.

## Output schema

The executor answers `{"items": [...], "search_notes": "..."}`. `final.json` holds `status`, `report.items` (or
`null`), `notes` (the search notes) and `errors` (up to 3). Each item has the 9 fields of the request (study type and
method are two keys), all written by the agent:

| Key | Content |
| --- | --- |
| `doi` | DOI only, for example `10.1000/xyz123` |
| `title` | Title |
| `authors` | List of names |
| `year` | Integer |
| `venue` | Journal |
| `study_type` | Study type |
| `method` | Method |
| `sample_size` | Sample as it appears in the abstract, or `não informado no resumo` |
| `main_finding` | Main finding in one sentence |
| `abstract_quote` | Literal quote from the abstract |

## Tools

`WebSearch` and `WebFetch` (Claude Agent SDK). The agent may call any public API through `WebFetch`; the prompt points
to the OpenAlex and Crossref APIs, SciELO and web search.

## Limits and constants

- 25 articles requested per run.
- One AI call, at most 215 turns (90 + 5 x 25) and 4,950 s (2,700 + 90 x 25).
- No verifier, no code gate, no retries.

## Run statuses

| Status | Meaning |
| --- | --- |
| `done` | The agent returned a valid structured answer; `final.json` has the items. |
| `paused` | Not produced by this level (there is no verifier). |
| `failed` | No valid structured answer (turn limit, timeout or malformed output); `final.json` has `errors`. |
| `error` | An exception; `events.jsonl` ends with `run_error` and `meta.json` records `error`. |

## How to run

```
python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1
```

Topic ids: `a01` to `a06` (`a04` is the example topic). Run id: `<tag>-n1-<topic>-r<rep>`.

## How to evaluate only this level's runs

```
python -m evaluation.evaluate --judge deepseek --prefix mytest-n1
python -m evaluation.evaluate --judge qwen --prefix mytest-n1
python -m evaluation.evaluate --judge gemini --prefix mytest-n1
python -m evaluation.jury mytest
python -m evaluation.report mytest
```

The prefix selects the runs. `jury` and `report` take the tag and cover every run of that tag that has evaluations; if
you ran only Level 1, only Level 1 appears. `python -m evaluation.report class` reproduces the class numbers from the
shipped evaluations.

## How to debug

1. Open `runs/<run_id>/meta.json`: status, wall time, AI calls and tokens.
2. Read `runs/<run_id>/events.jsonl` in order: `run_start`, `step_start`, `ai_call_start`, `ai_tool` (each search and
   page the agent opened), `ai_call_end` (tokens, errors), `step_end` (number of items), `run_error`, `run_end`.
3. Open `runs/<run_id>/calls/`: `.system.md` (the prompt), `.user.md` (request plus format block) and `.result.json`
   (structured answer, usage, errors) of the single call.
4. Replay the run: `python -m http.server 8000`, then `http://127.0.0.1:8000/viewer/index.html?run=<run_id>&replay=1`.

## Checklist before changing a prompt

- [ ] Keep the output schema: the format block in `benchmark/common.py` asks for the 9-field item; do not contradict it
      in the prompt.
- [ ] Keep the four sections (Perfil, Memória, Planejamento, Ação), so the level stays what the class describes.
- [ ] Rerun on the example topic: `python -m benchmark.run --level n1 --topic a04 --tag mytest --rep 1` (and `--rep 2`).
- [ ] Evaluate with the three judges, then `jury` and `report`.
- [ ] Compare with the shipped class runs `class-n1-a04-r1` and `class-n1-a04-r2`: precision, right, wrong, not
      delivered, time and tokens.
