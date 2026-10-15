[Leia em português](results.pt-BR.md)

# Results

## In plain words

Level 3 (multi-agent with checking, plus code) is the best approach on every axis we measured: the highest
precision (97% by the jury), the fewest wrong articles (2% of the articles requested), the fastest (5 minutes per run)
and the cheapest (R$ 2.90 per run). Describing the agent well (Level 1) already lifts precision from 82% to 89%. Adding
an AI that checks the AI (Level 2) gives the same precision as a well-described agent, 90%, but takes longer and costs
more. Almost every agent gets the hard data right (DOI, author, year, journal); the errors are in what requires reading
the article.

All numbers come from 48 runs: 4 levels x 6 topics x 2 repetitions, 12 runs per level. How each article is judged is
in [evaluation.md](evaluation.md); how the levels are compared is in [statistics.md](statistics.md).

## Precision by level

Precision: of the articles delivered, the share that is 100% correct. Mean over the six topics, with the 95% interval
(Student t over the 6 topics). The jury and the single judge judged the same runs.

| Level | Jury (main) | 95% interval | Single judge | 95% interval |
| --- | --- | --- | --- | --- |
| 0 | 82% | 68 to 97% | 79% | 66 to 92% |
| 1 | 89% | 83 to 96% | 86% | 77 to 94% |
| 2 | 90% | 78 to 100% | 86% | 77 to 95% |
| 3 | 97% | 94 to 100% | 94% | 88 to 100% |

Jury: DeepSeek V4 Pro, Qwen3.7 Plus and Gemini 3.1 Flash-Lite, majority per criterion. Single judge: DeepSeek V4 Pro
alone, same criteria.

## Precision with code checks only

The same precision, counting only what code checks (registry, period, publication type, quote and sample in the
abstract), with no judge at all:

| Level | Code-only precision |
| --- | --- |
| 0 | 92% |
| 1 | 95% |
| 2 | 98% |
| 3 | 99% |

The gap between this table and the one above is what only reading can catch: scope, method and finding.

## Cost and outcome per run

Mean per run, 12 runs per level. Right, wrong and not delivered are shares of the 25 articles requested per run, by
the jury, and add up to 100%. Precision is the share of the articles delivered that are 100%
correct.

| Level | Time | AI calls | Tokens | Cost per run | Right | Wrong | Not delivered | Precision (of delivered) | Paused runs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 10.2 min | 1.0 | 2.2 M | R$ 7.11 | 80% | 17% | 3% | 82% | 0 of 12 |
| 1 | 17.0 min | 1.0 | 4.2 M | R$ 9.84 | 82% | 10% | 8% | 89% | 0 of 12 |
| 2 | 42.1 min | 9.9 | 5.9 M | R$ 16.33 | 59% | 8% | 33% | 90% | 3 of 12 |
| 3 | 5.1 min | 7.0 | 146 k | R$ 2.90 | 81% | 2% | 17% | 97% | 0 of 12 |

Cost per run: Claude Sonnet 5.5 at Anthropic's public API price (tokens and web searches) plus the verifier at the
cost OpenRouter charged, converted at the Banco Central PTAX selling rate of 14/10/2026, US$ 1 = R$ 5.0441. A paused
run is one where the verifier refused the fifth attempt of a step, so the run delivered no report; its 25 articles
count as not delivered.

What the whole test actually cost: a Claude Code subscription (already owned) plus about R$ 170 in OpenRouter tokens
(US$ 33.38, verifier and judges).

## What the test showed

**1. Level 3 is the best approach: code where it can, AI with checking where it must.** It makes the fewest errors:
2% of the articles requested are wrong, against 17%, 10% and 8% for Levels 0, 1 and 2. It is the fastest, 5 minutes
per run, and the cheapest, R$ 2.90 per run. Code does the search, the filtering and the references; the AI only reads
and judges, and is checked. Code is fast and cheap where the AI is slow and expensive, and it does not invent: when it
fails, it fails in plain sight.

**2. Describing the agent well already helps a lot.** Writing out the four layers (profile, memory, planning, action)
and what the agent does in each beats the one-sentence instruction: precision rises from 82% to 89%, and wrong
articles fall from 17% to 10% (Level 1 over Level 0). It costs only a better instruction.

**3. AI checking AI equals a well-described agent.** With today's models, precision is the same: 90% for Level 2
against 89% for Level 1. But Level 2 takes 42 minutes instead of 17 and costs R$ 16.33 instead of R$ 9.84, and 3 of
its 12 runs paused without a report, which accounts for most of the 33% of requested articles it did not deliver. A checker is
only as solid as what it checks against; an AI verifier is still an AI (Huang et al., 2024; Stechly, Valmeekam and
Kambhampati, 2025). The checks that move the needle are external and sound, such as code against an official registry
(Kambhampati et al., 2024), which is what Level 3 adds.

**4. Hard data, almost everyone gets right.** DOI, author, year and journal come out almost always right, which is
why code-only precision is high at every level. The error is in what requires reading the article:

- **Scope:** is it on the requested topic?
- **Method:** is it research with data, of the stated type?
- **Finding:** does the abstract confirm what the agent said?

### By statistical test

Level 3 beats Level 0 in precision with statistical confidence (Holm p 0.001). It also beats Levels 1 and 2, with a
weaker signal (Holm p about 0.06, just above the usual 5% cutoff). See [statistics.md](statistics.md).

## The two measures agree on the order

The jury and the single judge give the same ranking. Level 3 is first by both (97% and 94%), Level 0 is last by both
(82% and 79%), and Levels 1 and 2 sit close together in the middle by both (89% and 90% by the jury, 86% and 86% by
the single judge). Code-only precision rises in the same order, from 92% to 99%. The single judge is a little stricter
across the board, so its numbers are a few points lower, but no change of judge changes which architecture wins. The
order is a property of the architectures, not of the way of judging.

## Where the per-run files are

Each level keeps its runs and their evaluations in its own folder:

```
agents/level_N/
  runs/class-nN-<topic>-r<rep>/    events.jsonl, final.json, meta.json, calls/
  evaluations/judge-deepseek/      one file per run, single judge (DeepSeek V4 Pro) + code checks
  evaluations/judge-qwen/          same, Qwen3.7 Plus
  evaluations/judge-gemini/        same, Gemini 3.1 Flash-Lite
  evaluations/jury/                the jury: majority of the three, per criterion
  media/level-N.mp4                the video of the example topic
```

Run ids follow `class-<level>-<topic>-r<rep>`; for example, `class-n3-a04-r1` is Level 3 on the example topic (games
against misinformation), repetition 1. `final.json` holds the delivered list; `meta.json` holds time, calls and tokens;
`events.jsonl` is the event log of the run; `calls/` holds every AI call. Any run can be replayed in the viewer:

```
python -m http.server 8000
```

then open `http://127.0.0.1:8000/viewer/index.html?run=class-n3-a04-r1&replay=1`.

## How to regenerate

From the repository root:

```
python -m evaluation.report class
python -m evaluation.stats class
```

`python -m evaluation.report class` reproduces the class numbers from the shipped evaluations and writes
`evaluation/REPORT.md` (precision, intervals, cost, outcome). `python -m evaluation.stats class` writes
`evaluation/STATISTICS.md` (the per-article test with Holm correction). Neither command calls an AI: they read the runs
and the evaluation files already in `agents/level_N/`.

## References for this document

Huang et al. (2024); Kambhampati et al. (2024); Stechly, Valmeekam and Kambhampati (2025). Full entries in
[references.md](references.md).
