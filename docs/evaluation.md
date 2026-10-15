[Leia em português](evaluation.pt-BR.md)

# Evaluation: how every article is judged

## In plain words

Every level gets the same request: 25 peer-reviewed empirical journal articles on a narrow topic, with 9 fields each.
We then check every article it delivers, in the same way for all four levels. Code checks everything that has a
right answer in a public registry (the DOI, the title, the author, the year, the journal, the period, the publication
type, the quote and the sample). A jury of three AIs from three different companies, who do not know which level
produced the article, reads the abstract and decides the rest: is it on topic, is it empirical, is the method the one
stated, does the abstract support the finding. An article counts as right only when every check passes. One wrong
field and the whole article counts as wrong.

The main metric is **precision**: of the articles delivered, how many are 100% correct. Next to it we report time,
AI calls, tokens, cost in reais, and how the 25 requested articles split into right, wrong and not delivered.

The metrics and the judging criteria were fixed before the runs.

## The task and the design

- **Task.** A literature review. Each run asks for 25 peer-reviewed empirical journal articles on a narrow topic,
  published 2018 to 2025, and for each one 9 fields: DOI, title, authors, year, journal, study type and method,
  sample size as it appears in the abstract, main finding in one sentence, and a literal quote from the abstract.
- **Design.** 4 levels x 6 topics x 2 repetitions = 48 runs, 12 runs per level. A run is one level on one topic,
  once. Each topic runs twice per level because the AI is probabilistic: the same input can give different outputs.
- **Executor.** Claude Sonnet 5.5, the same at every level, called through the Claude Agent SDK (Claude Code). The
  only thing that changes between levels is the architecture.
- **Five companies.** Claude (Anthropic) executes, GLM (Z.ai) checks inside Levels 2 and 3; DeepSeek, Qwen (Alibaba)
  and Gemini (Google) judge.

The six topics (ids as in `benchmark/topics.json`):

| Id | Topic |
| --- | --- |
| a04 | Games against misinformation, like Bad News (the example topic) |
| a01 | Continued influence of misinformation |
| a02 | Brazilian fact-checking agencies |
| a03 | Media literacy in school and university |
| a05 | Perception of images, videos and audio made by AI |
| a06 | Clickbait headlines |

## What counts as correct

An article is correct when all 9 fields are right and it meets the request. The rule is strict on purpose: in a
literature review, a reference with a wrong year, a quote that is not in the abstract or a finding the abstract does
not support is a reference the researcher cannot use as delivered. So one wrong field and the whole article counts as
wrong. This follows the item-by-item logic of FActScore (Min et al., 2023): break the output into units that can each
be checked, and measure the share that holds.

Each field has an owner:

| Field | Checked by | What is checked |
| --- | --- | --- |
| DOI | code | it exists in Crossref or OpenAlex |
| Title | code | it matches the registry title |
| Authors | code | the first author given matches one of the first authors in the registry |
| Year | code | it matches a year in the registry; it falls in the requested period |
| Journal | code | it matches the registry journal; the record is a journal article |
| Study type and method | jury | the study is empirical, and the type and method match the abstract |
| Sample size | code | as written, it is in the abstract (or the agent states it is not reported) |
| Main finding | jury | the abstract supports it |
| Literal quote | code | it is in the abstract |

On top of the fields, the jury decides whether the article is **on topic**: inside the requested scope (subject,
platform, country, audience).

### Why precision, and why outcomes are reported apart

Precision is measured over the articles **delivered**. An agent that delivers fewer articles is not punished in
precision for the ones it leaves out. This is deliberate: a metric that rewards filling the list pushes the agent to
guess, and guessing is exactly the behavior that produces invented references (Kalai et al., 2025). An agent that says
"I found 20 that hold" is more useful than one that pads the list to 25 with 5 wrong ones.

To keep the full picture visible, every run is also split into three shares of the **25 articles requested**, which
always add up to 100%:

- **Right:** delivered and 100% correct.
- **Wrong:** delivered with at least one failed check.
- **Not delivered:** requested but not in the delivery. A paused run (the verifier refused the fifth attempt of a
  step, so the run delivered no report) counts its 25 articles as not delivered.

## The code checks, in detail

Code checks what has a right answer outside the AI. It is deterministic: the same input always gives the same
verdict, and every verdict can be traced. It lives in `evaluation/evaluate.py`, with page fetch, text normalization
and quote matching in `evaluation/verify.py`, and the registry clients in `benchmark/scholar.py`.

1. **The DOI exists.** The evaluator looks the DOI up in Crossref and OpenAlex. When neither knows it, the evaluator
   searches the title in OpenAlex to tell two errors apart: a real article with a wrong DOI, or a reference that
   cannot be found anywhere. This is the split Walters and Wilder (2023) use between fabricated references and
   substantive errors in real ones.
2. **Title.** Compared with every title the registries and the publisher hold for that DOI (Crossref, OpenAlex,
   Semantic Scholar and the publisher page). The comparison tolerates a subtitle, punctuation and case, and also the
   article's own title in another language when the publisher declares it.
3. **Author.** The first author given must match one of the first authors in the registry. Any citation style is
   accepted: "Given Surname", "Surname, Given" or "Surname Initials".
4. **Year.** It must be one of the years the registry records for the article (print and online dates can differ).
5. **Journal.** It must match the journal in the registry.
6. **Period.** The registry year must fall inside the requested period, 2018 to 2025.
7. **Publication type.** The Crossref record must be a journal article. Conference papers, book chapters and preprints
   do not count.
8. **Quote.** The literal quote must be in the abstract. The evaluator gathers the abstract from OpenAlex, Crossref
   and Semantic Scholar, and also opens the publisher page through the DOI. Both sides are normalized first (Unicode
   form, typographic quotes and dashes, spacing and case), so formatting differences never count as errors. A quote
   with an ellipsis is split into its literal passages, and each passage must be found. A near-literal match with a
   very high similarity score is accepted, to absorb an encoding difference; a paraphrase is not.
9. **Sample.** The sample size must be in the abstract: either the literal phrase, or every number it gives. When the
   agent states that the abstract does not report the sample, nothing is checked against it.

The evaluator consults sources Level 3 does not use: Semantic Scholar and the publisher page. So Level 3 is never
checked only against the same databases it searched.

## The judging criteria

Some fields have no registry answer: they require reading. For these, a judge receives the researcher's request, the
article's registry metadata (title, year, journal), its abstract, and the data the agent extracted (study type, method,
sample, finding). Nothing else. Then it decides four criteria:

1. **On topic.** Does the article deal with the requested subject, inside the requested scope (platform, country,
   audience)?
2. **Empirical.** Does the study collect or analyze its own data of the kind the request demands (experiment, survey,
   interviews, focus groups, content or document analysis)? A theoretical essay or a review does not count.
3. **Method as stated.** Do the study type and the method the agent reported match the abstract?
4. **Finding supported.** Does the abstract support the finding the agent stated? The judge answers `supported`,
   `partial` (only part of it, or the finding goes further than the abstract) or `unsupported`. Only `supported` passes.

The judge must first copy the passage of the abstract (or the metadata) that decides each criterion, and only then
decide. Its labels must agree with the passages it copied. It answers in a strict JSON schema, at temperature 0, so
every verdict comes with its evidence and has the same shape. The judge call is shared by the three judges, in
`evaluation/judge_llm.py`. Responses are cached, so running the evaluation again never pays twice for the same
judgment.

### The abstract is the evidence

The judges read the abstract, and only the abstract. Three reasons. It is the one piece of text every database holds
for almost every article, so every level is judged on the same evidence. It is what the request itself points to: the
sample "as it appears in the abstract" and the quote "from the abstract". And it keeps the judgment checkable: anyone
can open the same abstract and repeat the decision. The publisher page is used by code only, to find the quote; it is
never shown to a judge. An article for which no source holds an abstract cannot be judged, so it does not count as
right.

This is also a limit, discussed in [limits-and-next-steps.md](limits-and-next-steps.md): an abstract can omit a method
detail that the full article states.

## The three-company jury (the main measure)

The main measure is a jury of three models from three companies: **DeepSeek V4 Pro** (DeepSeek), **Qwen3.7 Plus**
(Alibaba) and **Gemini 3.1 Flash-Lite** (Google). Each judge decides the four criteria on its own. The jury takes the
**majority per criterion**: a criterion passes when at least two of the three judges pass it. An article is right when
the code checks pass and the jury passes all four criteria. An article needs all three verdicts to count as right. The
jury lives in `evaluation/jury.py`.

Why three companies, and why these:

- **A panel beats a single judge.** Verga et al. (2024) show that a panel of smaller models from different families
  agrees better with human judgment than one large judge, and reduces the bias of any single model family.
- **No one judges its own company.** Models tend to recognize and favor text written by themselves (Panickssery,
  Bowman and Feng, 2024). So no judge comes from Anthropic, whose model executes, nor from Z.ai, whose model is the
  verifier inside Levels 2 and 3. The executor, the verifier and the judges are five companies apart.
- **Known judge biases are designed out.** Zheng et al. (2023) document the biases of AI judges: position (favoring
  the first answer shown), verbosity (favoring longer answers) and self-enhancement (favoring their own family). Here
  each judge rates one article at a time against fixed criteria, not two answers against each other, so there is no
  position to favor; it must quote its evidence before deciding; and it is from a different company than the executor.
- **Blind to the level.** The judge does not know which level, or which architecture, produced the article. Its
  instructions say only that it does not know who extracted the data. So a judge cannot favor an architecture it
  expects to be better.

The three judges give the same verdict on 85% of the 980 articles they judged; most disagreement is on method.

## The single judge (the comparison measure)

For comparison, **DeepSeek V4 Pro alone** judges the same articles, in the same runs, with the same criteria and the
same code checks. Only the vote changes: one judge instead of a majority of three. If the order of the levels held
only under one way of judging, it would be a property of the judge, not of the architectures. Both measures give the
same order: see [results.md](results.md).

## How cost is computed

For each run, the evaluator reports wall-clock time, AI calls, tokens and cost in reais.

- **Executor.** Claude Sonnet 5.5 priced at [Anthropic's public API price](https://platform.claude.com/docs/en/about-claude/pricing):
  input, output, cache writes and cache reads, each at its own rate, read from the usage the API records for every
  call in `calls/`; plus the web searches the executor made, at the public price per search.
- **Verifier.** GLM-5.3 Flash at the cost OpenRouter charged for each call, as recorded in the run's event log.
- **Exchange rate.** The dollar total is converted at the Banco Central do Brasil PTAX selling rate of 14/10/2026,
  US$ 1 = R$ 5.0441.

The executor in this test ran under a Claude Code subscription. Pricing its tokens at the public API rate gives a
cost anyone can compare and reproduce. The judges are not part of the cost of a run: they belong to the evaluation,
not to the agent. What the whole test actually cost was the subscription (already owned) plus about R$ 170 in
OpenRouter tokens (US$ 33.38, verifier and judges).

## Where each evaluation file lives

Each level keeps its own evaluations next to its own runs, so one level can be read and debugged without touching the
others:

```
agents/level_N/
  runs/class-nN-<topic>-r<rep>/    the run: events.jsonl, final.json, meta.json, calls/
  evaluations/judge-deepseek/      one file per run: code checks + DeepSeek V4 Pro
  evaluations/judge-qwen/          same, Qwen3.7 Plus
  evaluations/judge-gemini/        same, Gemini 3.1 Flash-Lite
  evaluations/jury/                the jury: majority of the three, per criterion
```

Each evaluation file holds, for every article delivered in that run, the result of every code check, the judge's
verdict with its copied evidence, and whether the article counts as right; and, for the run, the number delivered, the
number right and the precision.

To evaluate runs of your own (tag `mytest`):

```
python -m evaluation.evaluate --judge deepseek --prefix mytest
python -m evaluation.evaluate --judge qwen --prefix mytest
python -m evaluation.evaluate --judge gemini --prefix mytest
python -m evaluation.jury mytest
python -m evaluation.report mytest
python -m evaluation.stats mytest
```

## References for this document

Kalai et al. (2025); Min et al. (2023); Panickssery, Bowman and Feng (2024); Verga et al. (2024); Walters and Wilder
(2023); Zheng et al. (2023); Anthropic, Pricing; Banco Central do Brasil, PTAX. Full entries in
[references.md](references.md).
