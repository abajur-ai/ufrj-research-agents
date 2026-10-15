[Leia em português](run-the-benchmark.pt-BR.md)

# Run the benchmark

In this guide you will run the research agents yourself. You start with the simplest way, which is asking Claude Code to do it for you with an instruction ready to paste. Then you see the manual commands, one section each: one run, a batch of runs, the evaluation by the three judges, the jury, the report and the statistics, reproducing the class numbers at no cost, watching a run in the viewer, and recording a replay video. The guide ends with where every output goes, how much each level costs and how long it takes, and what to do when something goes wrong. Before you start, finish [Getting started](getting-started.md).

## Contents

1. [The simplest way: ask Claude Code](#1-the-simplest-way-ask-claude-code)
2. [Names you will see](#2-names-you-will-see)
3. [One run](#3-one-run)
4. [A batch of runs](#4-a-batch-of-runs)
5. [Evaluation with the three judges](#5-evaluation-with-the-three-judges)
6. [The jury](#6-the-jury)
7. [Report and statistics](#7-report-and-statistics)
8. [Reproduce the class numbers](#8-reproduce-the-class-numbers)
9. [Watch a run in the viewer](#9-watch-a-run-in-the-viewer)
10. [Record a replay video](#10-record-a-replay-video)
11. [Where the outputs go](#11-where-the-outputs-go)
12. [Cost and time per level](#12-cost-and-time-per-level)
13. [Troubleshooting](#13-troubleshooting)

## 1. The simplest way: ask Claude Code

You do not need to type commands. Create an empty folder, open it in Visual Studio Code (**File > Open Folder**), open the Claude Code panel (or OpenCode, in setup (b) of [Getting started](getting-started.md#2-which-agentic-ai-to-use)), and paste one of the instructions below. The agentic AI clones the repository, reads this guide, installs what is missing, runs the commands and tells you the result. It asks for your permission before running each command, so you stay in control.

**Run Level 3 on the example topic** (a few minutes, a few cents of OpenRouter):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, read docs/run-the-benchmark.md and run Level 3 on topic a04. When it ends, tell me how many articles it delivered and open the run in the viewer.
```

**Reproduce the class report from the shipped evaluations** (no AI calls, no cost):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, read docs/run-the-benchmark.md and reproduce the class report from the shipped evaluations with python -m evaluation.report class. Do not run any agent or judge. Then show me the precision of each level by the jury, with the 95% intervals.
```

**Run the whole benchmark** (many hours, about US$ 33 of OpenRouter, plus the executor: your Claude plan, or OpenRouter tokens if Claude Code points to OpenRouter):

```text
Clone https://github.com/abajur-ai/ufrj-research-agents, read docs/run-the-benchmark.md and run the whole benchmark with the tag mytest: the four levels on the six topics, two repetitions each. Then evaluate every run with the three judges, run the jury, and generate the report and the statistics. Before you start, tell me the expected cost and time and wait for my confirmation.
```

## 2. Names you will see

| Name | Meaning |
| --- | --- |
| **Level 0** (`n0`) | one sentence, and nothing else |
| **Level 1** (`n1`) | one agent, the four layers described (profile, memory, planning, action), no checking |
| **Level 2** (`n2`) | multi-agent, with checking: a verifier checks every step |
| **Level 3** (`n3`) | multi-agent with checking, plus code: code where it can, AI with checking where it must |
| **run** | one level on one topic, once |
| **tag** | a name you choose for a group of runs, for example `mytest`; the class runs use `class` |
| **run id** | `<tag>-<level>-<topic>-r<rep>`, for example `class-n3-a04-r1` |

Every run asks for the same thing: 25 peer-reviewed empirical journal articles on a narrow topic, published 2018 to 2025, and for each one the DOI, title, authors, year, journal, study type and method, sample size as it appears in the abstract, main finding in one sentence, and a literal quote from the abstract.

The six topics, in `benchmark/topics.json`:

| Id | Topic |
| --- | --- |
| `a04` | games against misinformation, like Bad News (**the example topic**) |
| `a01` | continued influence of misinformation |
| `a02` | Brazilian fact-checking agencies |
| `a03` | media literacy at school and at university |
| `a05` | perception of images, videos and audio made by AI |
| `a06` | clickbait headlines |

All commands below run in PowerShell, from the repository root, with the environment active (`.venv\Scripts\activate`).

## 3. One run

```powershell
python -m benchmark.run --level n3 --topic a04 --tag mytest --rep 1
```

| Option | What it sets |
| --- | --- |
| `--level` | `n0`, `n1`, `n2` or `n3` |
| `--topic` | `a01` to `a06` |
| `--tag` | the name of your group of runs |
| `--rep` | the repetition number; use another number to run the same level on the same topic again without overwriting |

The command prints the run id when it ends, here `mytest-n3-a04-r1`, and the run is in `agents/level_3/runs/mytest-n3-a04-r1/`. While it runs, you can watch it live in the viewer (section 9).

### What a first run looks like

This is the path a newcomer follows, run end to end from a fresh clone of this repository on Windows 11 with Python 3.13:

| Step | Command | What you should see |
| --- | --- | --- |
| Install | `pip install -r requirements.txt` | a few minutes; no errors |
| Check the setup at no cost | `python -m evaluation.report class` | the class table: Level 3 at 97% by the jury |
| One run of Level 3 on the example topic | `python -m benchmark.run --level n3 --topic a04 --tag mytest --rep 1` | about 5 to 8 minutes; it prints `mytest-n3-a04-r1`; `final.json` has `"status": "done"` and around 20 articles |
| Evaluate it with the three judges | `python -m evaluation.evaluate --judge deepseek --prefix mytest` (then `qwen` and `gemini`; they can run at the same time in three terminals) | a few minutes each; one line per run with delivered and correct articles |
| Combine them | `python -m evaluation.jury mytest` | `jury: 1 runs, ... articles` |
| Read the result | `python -m evaluation.report mytest` | `evaluation/REPORT_mytest.md`, with precision, time, cost and right, wrong and not delivered |

In that end-to-end check, Level 3 on topic a04 delivered 20 articles in 7.1 minutes with 6 AI calls, every AI step approved on the first attempt; the jury judged 20 of 20 correct and the single judge 19 of 20; the verifier and the three judges cost US$ 0.67 on OpenRouter. With one level and one topic the report shows no interval and no comparison between levels: those need runs of at least two levels on at least two topics.

## 4. A batch of runs

```powershell
python -m benchmark.bench --topics a01,a02,a03,a04,a05,a06 --levels n0,n1,n2,n3 --reps 2 --tag mytest --workers 4
```

This is the whole benchmark: 4 levels x 6 topics x 2 repetitions = 48 runs.

- Each run goes in its own process, so one failure does not stop the others.
- `--workers 4` runs four at a time. The longest levels start first.
- A run that ends in `error` is tried once more. Runs that already ended as `done`, `paused` or `failed` are kept as they are.
- So you can stop the batch and start the same command again: it continues with what is missing.

Use fewer topics, levels or repetitions to try a smaller batch, for example `--topics a04 --levels n0,n3 --reps 1`.

## 5. Evaluation with the three judges

Each judge evaluates every run whose id starts with your tag:

```powershell
python -m evaluation.evaluate --judge deepseek --prefix mytest
python -m evaluation.evaluate --judge qwen --prefix mytest
python -m evaluation.evaluate --judge gemini --prefix mytest
```

For every article a run delivered, the evaluation does two kinds of checks.

**Checks by code (hard data).** The DOI exists; title, author, year and journal match the official registry; the article is in the requested period and is a journal article; the quote and the sample size are in the abstract. To find the abstract, the evaluator also consults sources Level 3 does not use (Semantic Scholar and the publisher page), so Level 3 is not checked only against its own sources.

**Checks by the judge (what requires reading).** The judge, blind to the level, reads the abstract and decides four criteria: the article is on the topic, it is empirical, the method is the one stated, and the abstract supports the stated finding.

An article counts as correct only when every check passes. One wrong field and the whole article counts as wrong.

The three judges are DeepSeek V4 Pro (`deepseek`), Qwen3.7 Plus (`qwen`) and Gemini 3.1 Flash-Lite (`gemini`), called through OpenRouter. Each writes one file per run in `agents/level_N/evaluations/judge-<name>/`. Judge answers are saved on disk, so evaluating the same run again does not pay again.

## 6. The jury

```powershell
python -m evaluation.jury mytest
```

The jury is the main measure. For each article, it takes the majority of the three judges on each criterion, separately. An article is correct when the code checks pass and the jury approves. The jury only covers runs that all three judges evaluated, and it writes one file per run in `agents/level_N/evaluations/jury/`.

Why three companies: a model tends to favor answers like its own. The executor (Claude) and the verifier (GLM) come from two companies, and the three judges from three others. **DeepSeek V4 Pro alone** is the single judge, kept for comparison: same criteria, same runs.

## 7. Report and statistics

```powershell
python -m evaluation.report mytest
python -m evaluation.stats mytest
```

**`report`** computes, per level:

- **precision**, the main metric: of the articles delivered, how many are 100% correct;
- the **95% interval** of each mean;
- **cost**: time, AI calls, tokens and cost per run;
- **outcome**: right, wrong and not delivered, out of the 25 articles requested.

**`stats`** runs the per-article test.

The statistical reasoning has three steps:

1. **Mean per topic.** Each topic is a unit: the two runs of a level on a topic become one mean.
2. **Likely range (95% interval).** Student t with 5 degrees of freedom (6 topics minus 1), the conservative choice for few groups (Cameron and Miller 2015, section VI).
3. **Per-article test.** A logistic regression of correctness on level and topic, with errors clustered by run (the articles of the same run form a group), t critical values, and the Holm correction for the multiple comparisons.

The class results, in `evaluation/REPORT.md` and `evaluation/STATISTICS.md`, were generated by these two commands with the tag `class`.

## 8. Reproduce the class numbers

```powershell
python -m evaluation.report class
```

The evaluations of the 48 class runs ship with the repository, so this command recomputes every number of the class from those files. It makes no AI call and costs nothing. You should see:

| Level | Precision, jury | 95% interval | Precision, single judge | 95% interval |
| --- | --- | --- | --- | --- |
| 0 | 82% | 68 to 97% | 79% | 66 to 92% |
| 1 | 89% | 83 to 96% | 86% | 77 to 94% |
| 2 | 90% | 78 to 100% | 86% | 77 to 95% |
| 3 | 97% | 94 to 100% | 94% | 88 to 100% |

Run `python -m evaluation.stats class` to reproduce the per-article test: Level 3 beats Level 0 with statistical confidence (Holm p 0.001), and it also beats Levels 1 and 2 with a weaker signal (Holm p about 0.06, just above the usual 5% cutoff).

## 9. Watch a run in the viewer

The viewer is a web page that draws a run step by step: each AI call, each search, each verifier verdict, and the delivery. Start a small local web server at the repository root:

```powershell
python -m http.server 8000
```

Leave that terminal open and, in Google Chrome, open one of these addresses.

**Replay of a finished run:**

```text
http://127.0.0.1:8000/viewer/index.html?run=class-n3-a04-r1&replay=1
```

The replay plays the real events of the run at a faster speed, and the clock shows the real time. Add `&speed=20` to the address to play it 20 times faster.

**Live:** start a run in another terminal and open the same address without `&replay=1`, with your run id:

```text
http://127.0.0.1:8000/viewer/index.html?run=mytest-n3-a04-r1
```

The page reads the run's log several times per second and draws each event as it happens.

To stop the server, go back to its terminal and press Ctrl+C.

## 10. Record a replay video

```powershell
python -m benchmark.record_replay class-n3-a04-r1 --speed 20 --cap 0.8 --hold 6
```

The command serves the project on a local port, opens the viewer in replay mode in Google Chrome without a window, at 1920 x 1080, records until the replay ends, and writes an `.mp4` video plus a `.jpg` poster (a frame near the end). It prints the path of the video when it finishes. It needs Google Chrome and ffmpeg.

| Option | What it sets |
| --- | --- |
| `--speed 20` | each event plays at its real time divided by 20 |
| `--cap 0.8` | a pause longer than 0.8 seconds on screen is shortened to 0.8 seconds |
| `--hold 6` | each verifier verdict stays 6 seconds on screen, so you can read it |

The videos of the class are in `agents/level_N/media/`, from `level-0.mp4` to `level-3.mp4`: real runs of the example topic (a04, repetition 1), recorded with these options, each ending with the delivery.

## 11. Where the outputs go

Each level lives in its own folder, `agents/level_N/`, with its code, its instructions, its runs and their evaluations. Level 0 is `agents/level_0/`, Level 3 is `agents/level_3/`.

**A run:** `agents/level_N/runs/<run_id>/`

| File | Content |
| --- | --- |
| `events.jsonl` | every event of the run, one per line, written as it happens (the viewer reads this file) |
| `final.json` | the delivered list of articles and the status of the run |
| `meta.json` | status, total time, AI calls and tokens, by role and by provider |
| `calls/` | every prompt sent to an AI and every answer it gave |

**An evaluation:** `agents/level_N/evaluations/<judge>/<run_id>.json`, where `<judge>` is `judge-deepseek`, `judge-qwen`, `judge-gemini` or `jury`.

**The status of a run:**

| Status | Meaning |
| --- | --- |
| `done` | the run delivered its list |
| `paused` | Levels 2 and 3: the verifier refused the fifth attempt of a step, so the run delivered no report |
| `failed` | the run ended without a list to deliver, for example when Level 3 finds too few candidates after the filters |
| `error` | the program stopped on an unexpected problem, such as the network or the usage limit of your Claude plan; a batch tries it once more |

A paused run is a real result, not a crash: it is the price of checking. In the class, 3 of the 12 runs of Level 2 paused, and no run of the other levels did.

## 12. Cost and time per level

Mean per run in the class (12 runs per level). Right, wrong and not delivered are out of the 25 articles requested, by the jury.

| Level | Time | AI calls | Tokens | Cost per run | Right | Wrong | Not delivered | Paused runs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10.2 min | 1.0 | 2.2 M | R$ 7.11 | 80% | 17% | 3% | 0 of 12 |
| 1 | 17.0 min | 1.0 | 4.2 M | R$ 9.84 | 82% | 10% | 8% | 0 of 12 |
| 2 | 42.1 min | 9.9 | 5.9 M | R$ 16.33 | 59% | 8% | 33% | 3 of 12 |
| 3 | 5.1 min | 7.0 | 146 k | R$ 2.90 | 81% | 2% | 17% | 0 of 12 |

How to read the cost column: it is Claude Sonnet 5.5 at Anthropic's public API price (tokens and web searches) plus the verifier at the cost OpenRouter charged, converted at the Banco Central PTAX selling rate of 14/10/2026, US$ 1 = R$ 5.0441. It shows what each architecture costs in a comparable way.

What you actually pay:

- **The executor** is Claude Code. Logged in to a Claude subscription, it uses your plan's usage, not money per token. Pointed to OpenRouter, it is paid per token from your OpenRouter credits, and the cost column above is the reference for that, at Anthropic's public API price.
- **OpenRouter** pays the verifier (Levels 2 and 3) and the three judges. A single run costs cents. The whole benchmark, with the evaluation, used about **US$ 33.38 (about R$ 170)**.

So the whole class test cost a Claude Code subscription plus about R$ 170 in OpenRouter tokens.

On time: Level 3 is the fastest, about 5 minutes per run, because code does the search, the filters and the references. Level 2 is the slowest, about 42 minutes, because every step can go back and forth with the verifier up to 5 times. The whole batch of 48 runs takes several hours, even with four workers.

## 13. Troubleshooting

**"Key not found", or an error mentioning `OPENROUTER_API_KEY`, `OPENALEX_API_KEY` or `BRAVE_API_KEY`.**
The terminal was open before you saved the key. Close every terminal and Visual Studio Code, open them again, and check with `if ($env:OPENROUTER_API_KEY) { 'ok' } else { 'missing' }` (same for the other two). If it prints `missing`, save the key again as shown in [Getting started](getting-started.md#4-openrouter-one-key-for-many-ai-companies). An HTTP 401 from OpenRouter means the key is wrong or was deleted; an HTTP 402 means your OpenRouter credits ran out.

**"claude.exe from the VS Code extension not found", or Claude Code is not logged in.**
The code uses the `claude.exe` that comes with the Claude Code extension for Visual Studio Code, in both recommended setups. Install the extension (see [Getting started](getting-started.md#3-install-claude-code-from-zero)), then either sign in with a paid Claude plan or point it to OpenRouter (in that case, `/status` must show the base URL `https://openrouter.ai/api`). Send a message to confirm that it answers. Then start the run again.

**The usage limit of your Claude plan is reached (Claude subscription only).**
The run stops with `error`. Wait until your plan's limit resets and start the same `benchmark.bench` command again: finished runs are kept and only the missing ones run. Fewer `--workers` spread the use over more time.

**OpenAlex rate limit (HTTP 429).**
OpenAlex limits how many requests a key can make per day. First confirm that `OPENALEX_API_KEY` is set: without it, the limit is much lower. If the daily budget is used up, waiting a few seconds does not help: wait for it to reset and run again. Answers from OpenAlex and Crossref are saved on disk, so a run that repeats a query does not spend the budget again.

**A run ended as `paused`.**
This is a normal outcome of Levels 2 and 3: the verifier refused the fifth attempt of a step. To see why, open the run in the viewer (the last verdict is on screen) or read the last events of `events.jsonl`. To try again, run the same level and topic with another `--rep` number.

**PowerShell says running scripts is disabled.**
Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and activate the environment again.

**`python` opens the Microsoft Store.**
Use `py -3.13` in place of `python`.

Still stuck? Paste the error message into Claude Code, in the repository folder, and ask it to read this guide and fix the problem. Or write to bruno@abajur.ai.
