[Leia em português](limits-and-next-steps.pt-BR.md)

# Limits and next steps

## In plain words

This is a small test: six topics, one task, 48 runs. It is built so that its limits are visible and handled, not
hidden. Each limit below comes with how the test deals with it. The second half is practical: six ways a researcher
can take Level 3 further in their own field, with how to do each one in this repository.

## How to read these results

| The limit | How the test handles it |
| --- | --- |
| Small study: six topics, one task | Each topic runs twice per level; the mean is per topic, and the likely range of each mean is widened because there are only six topics. |
| One single executor model | It is the same at every level, so the difference measured comes from the architecture, not from the model. |
| The judges are AI and read only the abstract | A three-company jury, blind to the level, decides by majority; the hard data is checked by code. |
| The web, the databases and prices change | Metrics and criteria were fixed before the runs; cost is given with the exchange rate and its date. |

### Small study: six topics, one task

Six topics and one kind of task (a literature review of empirical journal articles) are enough to see the pattern,
not to close every question. The test handles it in three ways. Each topic runs twice per level, because the model is
probabilistic. The topic is the unit of analysis: the two runs become one mean, so the test never pretends to have
more independent units than it has. And the 95% interval uses Student t with G - 1 = 5 degrees of freedom, which
widens it on purpose for few groups (Cameron and Miller, 2015, section VI). This is also why Level 3 beats Levels 1
and 2 with a weaker signal (Holm p about 0.06): with six topics, a gap of seven or eight points is close to what the
test can resolve. See [statistics.md](statistics.md).

What the results do not cover: other tasks (a systematic review with a full protocol, data extraction from full text),
other fields with their own databases, or other languages of the literature.

### One single executor model

Every level runs on Claude Sonnet 5.5. A different model could do better or worse at every level. Keeping it the same
is the point: it is the control that makes the comparison fair, so the difference measured comes from the
architecture. Whether the same order holds with another executor is an open question.

### The judges are AI and read only the abstract

The judges can err, and an abstract can omit a method detail or soften a finding that the full article states. The
test handles it four ways. The jury has three models from three companies, none from the executor's or the verifier's
company (Panickssery, Bowman and Feng, 2024; Verga et al., 2024). The judges are blind to the level. The verdict is
the majority per criterion. And everything with a registry answer (DOI, title, author, year, journal, period, type,
quote, sample) is checked by code, not by a judge.

How much the judges agree: **the three judges give the same verdict on 85% of the 980 articles they judged; most
disagreement is on method**, the criterion that depends most on how an abstract describes a study. A single judge
(DeepSeek V4 Pro alone) gives the same order of the levels as the jury. See [evaluation.md](evaluation.md).

### The web, the databases and prices change

A run done tomorrow searches a slightly different web, OpenAlex and Crossref add records every day, and model prices
move. The test handles it by fixing the metrics and the judging criteria before the runs, by keeping every run on disk
(the delivered list, every AI call, the event log) so its evaluation can be repeated without running it again, and by
stating cost with the exchange rate and its date: PTAX selling rate of 14/10/2026, US$ 1 = R$ 5.0441.

## From Level 3 onward: how to refine the agent

Level 3 is a starting point, not a ceiling. These are the six steps that would make it better in a given field, in the
order a researcher would usually take them.

### 1. Build a bank of real cases

Reviews you already did and checked become the agent's answer key in your field. Run it after every change of model
or instruction.

How:

- Pick three to five reviews you trust, with their final lists of included articles.
- Turn each into a topic in `benchmark/topics.json`, with the same fields as the six topics already there: the request
  in your words, the period and the number of articles.
- Run Level 3 on them with a tag of your own, for example
  `python -m benchmark.bench --topics <your ids> --levels n3 --reps 2 --tag mybank --workers 4`.
- Evaluate (`python -m evaluation.evaluate --judge deepseek --prefix mybank`, and the other judges plus
  `python -m evaluation.jury mybank` for the full jury), then compare what the agent delivered with your list: what it
  found that you also included, what it found that you missed, and what you included that it did not find.
- Keep the bank fixed. Every time the model or a prompt changes, run the bank again and compare precision and
  wrong articles with the previous run. A change that lowers the bank's numbers does not ship.

### 2. Turn each error into a rule

Scope, method or finding: the error that repeats becomes a new rule or a new verifier in the agent. Then run the bank
again.

How:

- Open the evaluation files of your runs. For each wrong article, `agents/level_3/evaluations/jury/` shows which check
  failed, and the files of each judge (`judge-deepseek/`, `judge-qwen/`, `judge-gemini/`) hold the passage that judge
  copied as evidence.
- Group the failures by kind: off topic, not empirical or wrong method, finding beyond the abstract, quote or sample
  not in the abstract.
- When a kind repeats, decide where it belongs. A rule of judgment goes into the prompt of the step that makes that
  decision: `agents/level_3/prompts/screener.md` for scope and empirical design, `agents/level_3/prompts/extractor.md`
  for method, sample and finding. A rule with a right answer (a period, a publication type, a word that must appear)
  goes into code, which never forgets it.
- Run the bank again and check that the error dropped and nothing else rose.

### 3. Read the whole article

Level 3 decides from the abstract. With the full text, when it is open, method and finding are easier to confirm.

How:

- OpenAlex records, for many articles, whether an open-access version exists and where. The registry clients live in
  `benchmark/scholar.py`; that is the place to fetch the open full text when there is one.
- Give the extractor step the method and results sections in addition to the abstract, and keep the quote check
  against the text it came from.
- Keep the abstract-only path for closed articles, and record in each article which evidence was used, so the
  researcher knows what to check by hand.

### 4. Search the databases of your field

Level 3 searches two general databases, OpenAlex and Crossref. The databases, the vocabulary and the criteria of your
field specialize the agent.

How:

- Add your field's database as one more source in `benchmark/scholar.py`, next to OpenAlex and Crossref, so step 2 of
  Level 3 (code searches the academic databases) queries it too. Health, education, the social sciences and Latin
  American literature each have their own indexes.
- Put your field's vocabulary into the step that decides the search terms (`agents/level_3/prompts/terms.md`): the
  controlled terms, the synonyms and the terms to exclude.
- Write your field's inclusion criteria into the screener prompt: what counts as empirical, which designs are in,
  which publication types are out.

### 5. Put a specialist on the scale

A person from the field judges a sample, reading the whole article, and shows how often the AI judges are right.

How:

- Draw a random sample of delivered articles across levels, including some the jury passed and some it failed.
- Give the specialist the request, the article (full text) and the data the agent extracted, without the level and
  without the jury's verdict, and ask for the same four criteria: on topic, empirical, method as stated, finding
  supported.
- Compare the specialist's verdict with the jury's, criterion by criterion. Where they disagree, read why: it shows
  whether the jury is too lenient, too strict, or limited by reading only the abstract.

### 6. A bigger test, with a budget

More topics and more repetitions show clearly what each change improves.

How:

- Add topics to `benchmark/topics.json` and raise `--reps` in `python -m benchmark.bench`. More topics narrow the
  interval the most, because the topic is the unit of analysis; more repetitions steady each topic's mean.
- Budget: this test cost a Claude Code subscription and about R$ 170 in OpenRouter tokens (US$ 33.38) for the verifier
  and the judges, for 48 runs. Cost grows roughly in proportion to the number of runs and of articles judged.
- Fix the metrics and the criteria before running, as here, and write down the comparisons you will test, so the test
  answers the question you asked.

## References for this document

Cameron and Miller (2015); Panickssery, Bowman and Feng (2024); Verga et al. (2024). Full entries in
[references.md](references.md).
