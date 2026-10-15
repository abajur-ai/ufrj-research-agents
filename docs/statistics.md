[Leia em português](statistics.pt-BR.md)

# Statistics: how the levels are compared

## In plain words

Forty-eight runs is a small test, so the statistics are built to be careful, not to impress. They answer two
questions in three steps.

1. **Mean per topic.** Each topic is one unit. The two runs of a level on a topic become one number: their mean
   precision.
2. **Likely range.** For each level, the mean over the six topics comes with a 95% interval: where the true mean
   should be. With only six topics, the interval is made wider on purpose.
3. **Per-article test.** To ask whether one level really beats another, every delivered article counts. Articles of
   the same run are treated as a group, because they share the same search and the same decisions. A correction
   (Holm) accounts for making several comparisons at once.

The result, in precision, by the jury: **Level 3 beats Level 0 with statistical confidence (Holm p 0.001). It also
beats Levels 1 and 2, with a weaker signal (Holm p about 0.06, just above the usual 5% cutoff).**

The metrics and the judging criteria were fixed before the runs. The statistical analysis below is the method used to
compare the levels.

## Step 1: the mean per topic

The six topics are not equally hard. A topic with a narrow criterion and few studies can lower the precision of every
level, while a topic with a large literature can raise it. If we pooled all runs
and all articles together, a level would look better or worse depending on which topics happened to give it more
articles.

So the topic is the unit. For each level and each topic, the precision of the two runs is averaged into one number.
Each level ends up with six numbers, one per topic, and every level is measured on the same six topics. The level's
precision is the mean of those six numbers.

The two runs of a topic are not two independent units: they are the same question asked twice. Averaging them first
keeps the analysis honest about how many independent units there are (six), and it absorbs part of the run-to-run
variation of a probabilistic model.

## Step 2: the likely range (95% interval)

A mean from six topics is an estimate. Another six topics would give a somewhat different mean. The 95% interval says
how far the true mean could plausibly be: if the test were repeated many times, intervals built this way would contain
the true value about 95% of the time.

The interval is computed over the six topic means: the mean, plus or minus a critical value times the standard error
(the standard deviation of the six topic means divided by the square root of six). The critical value comes from the
**Student t distribution with 5 degrees of freedom**: G - 1, where G = 6 topics.

Why Student t, and why G - 1. With many groups, the critical value would be the familiar 1.96 of the normal curve.
With few groups, that value is too small and the interval comes out too narrow, which overstates confidence. Cameron
and Miller (2015, section VI) set out the problem of few groups (clusters) and recommend the T distribution with G - 1
degrees of freedom as the minimum correction. With 5 degrees of freedom the critical value is about 2.57 instead of
1.96, so the interval is about 30% wider. It is the conservative choice.

The interval is then clipped to the range precision can take, 0 to 100%. That is why some upper limits read exactly
100%.

### A worked reading

By the jury, Level 3 has mean precision 97% with interval 94 to 100%. Level 2 has 90% with interval 78 to 100%. The
two means are seven points apart, but the widths tell a second story: the six topic means of Level 3 were close to
each other, so its interval is narrow; Level 2 varied more from topic to topic, so its interval is wide. Overlapping intervals do
not by themselves prove that two levels are equal. To compare two levels directly, use step 3.

The intervals for every level, by the jury and by the single judge, are in [results.md](results.md).

## Step 3: the per-article test

Step 2 describes each level. Step 3 tests the differences between levels, using every article.

### The model

A **logistic regression** of correctness on level and topic, one row per delivered article:

```
correct ~ level + topic
```

- **The outcome is one article: right (1) or wrong (0).** Precision is a share of articles, and runs deliver
  different numbers of articles. A model at the article level weights each article once and uses all the information
  in the test. Logistic regression is the standard model for a yes or no outcome.
- **Topic as a fixed effect.** Each topic gets its own baseline. The level effect is then estimated *within* topics:
  Level 3 on the games topic is compared with Level 0 on the games topic, not with Level 0 on another, harder topic.
  This pairs the levels by topic, as in step 1.
- **Errors clustered by run.** The articles of one run are not independent of each other: they come from the same
  search, the same screening and the same model session. If the agent misreads the topic once, many of its articles
  are wrong together. Treating them as independent would make the test far too confident. Clustered standard errors
  treat the articles of a run as one group and let them be correlated inside it.
- **t critical values.** Following Cameron and Miller (2015, section VI), the tests use the T distribution with G - 1
  degrees of freedom, where G is the number of clusters (runs), instead of the normal curve.

The result of each comparison is an **odds ratio** (how many times higher the odds of an article being right are in
one level than in the other, at the same topic) and a two-sided **p value**.

### The comparisons

Five comparisons are tested: Level 1 against Level 0, Level 2 against Level 1, Level 3 against Level 2, Level 3
against Level 1, and Level 3 against Level 0.

### The Holm correction

Each test carries a small chance of a false alarm: finding a difference that is only noise. Run five tests and the
chance that at least one of them gives a false alarm grows. Holm (1979) controls this, with a simple procedure:

1. Sort the five p values from smallest to largest.
2. Multiply the smallest by 5, the next by 4, then 3, 2 and 1.
3. Walk up the list and never let an adjusted p fall below the one before it; cap every value at 1.

The adjusted values are the **Holm p values**. A Holm p below 0.05 means the difference holds even after accounting
for the fact that five comparisons were made. Holm protects against false alarms as well as the simpler Bonferroni
correction (which multiplies every p by 5), and it is never less able to detect a real difference.

## How to read p and the 5% cutoff

A **p value** answers one question: if the two levels were truly equal, how likely would it be to see a difference at
least this large just by chance? A small p says the observed difference would be rare under equality.

The usual cutoff is **5% (p below 0.05)**: below it, the difference is called statistically significant. The cutoff
is a convention, not a law of nature. A p of 0.04 and a p of 0.06 carry almost the same evidence; the line between them
is drawn for consistency, not because something changes at 0.05.

Three things a p value does not say: it is not the probability that the levels are equal; it is not the size of the
difference (that is the odds ratio and the precision itself); and a p above 0.05 does not show that there is no
difference, only that this test, with this sample, cannot separate it from chance with the usual confidence.

## The result

In precision, by the three-company jury:

| Comparison | Holm p | Reading |
| --- | --- | --- |
| Level 3 against Level 0 | 0.001 | Level 3 beats Level 0 with statistical confidence |
| Level 3 against Level 1 | about 0.06 | Level 3 is ahead; the signal is weaker, just above the usual 5% cutoff |
| Level 3 against Level 2 | about 0.06 | Level 3 is ahead; the signal is weaker, just above the usual 5% cutoff |

In words: even after accounting for five comparisons, the chance of seeing the gap between Level 3 and Level 0 if the
two were equal is about 1 in 1,000. Against Levels 1 and 2, Level 3 is ahead in precision (97% against 89% and 90%),
and the chance of a gap that size under equality is about 6%: a consistent signal, not a conclusive one at the usual
cutoff. A larger test, with more topics and more repetitions, is the way to settle it (see
[limits-and-next-steps.md](limits-and-next-steps.md)).

Every comparison, with its odds ratio, its p and its Holm p, is in `evaluation/STATISTICS.md`.

## Reproduce it

From the repository root, with the evaluations shipped in `agents/level_N/evaluations/`:

```
python -m evaluation.report class
python -m evaluation.stats class
```

`evaluation/report.py` computes the per-topic means and the Student t intervals and writes `evaluation/REPORT.md`.
`evaluation/stats.py` fits the per-article logistic regression with errors clustered by run and applies Holm; it
writes `evaluation/STATISTICS.md`.

For runs of your own, replace `class` with your tag (for example `mytest`), after evaluating them as described in
[evaluation.md](evaluation.md).

## References for this document

Cameron and Miller (2015); Holm (1979). Full entries in [references.md](references.md).
