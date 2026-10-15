[Leia em português](bibliography-check.pt-BR.md)

# Bibliography check

In this guide you will use the method of Level 3 to check a bibliography: for each claim in a text, does the cited source really say that? You will see how the check works (code finds each work in the official records and searches its text; a jury of three AI models from three companies reads what code found and decides by majority), how to run it, how to replace the example data with your own references and claims, how to read the outputs, and how much it costs. The example data is the class deck: every reference and every claim of the deck went through this check.

## Contents

1. [What it does](#1-what-it-does)
2. [How it works, step by step](#2-how-it-works-step-by-step)
3. [Why this design](#3-why-this-design)
4. [Run it](#4-run-it)
5. [Check your own bibliography](#5-check-your-own-bibliography)
6. [The outputs](#6-the-outputs)
7. [Cost and cache](#7-cost-and-cache)
8. [How to use the result](#8-how-to-use-the-result)

## 1. What it does

A text cites a source and says something about it: "55% of the references were fabricated", "the model tends to prefer its own answers", "the CNPq requires declaring the use of AI". Each of these sentences can go wrong in two ways. The reference itself can be wrong (the work does not exist, the author or the year is different). Or the reference is right, but the source does not say what the text claims, or says less, or says something else.

The bibliography check, in the `bibcheck/` folder, answers both questions for every reference and every claim:

- **Does the work exist, with this author, year and venue?** Answered by code, in the official records.
- **Does the source support the claim?** Answered by a jury of three models, reading only passages of the source that code found.

## 2. How it works, step by step

**1. Code finds each work in the official records.** Each reference has a kind, and each kind has its records:

| Kind | Where code looks |
| --- | --- |
| `paper` | OpenAlex, DBLP, arXiv and Crossref, searched in parallel by title |
| `book` | OpenLibrary, plus a web search for pages about the book |
| `web` | a web search; code opens the results and keeps the pages that carry the work's title |

Code then checks whether the work exists (a close title match in at least one record), whether the first author matches, whether the year matches, and whether the venue (journal, conference or publisher) matches.

**2. Code downloads the text of the source.** Whatever is open: the abstract (OpenAlex, Crossref, arXiv), the full text (the arXiv PDF, when there is one), the publisher page through the DOI, or the web page itself. Pages that refuse simple downloads are opened in a real browser.

**3. Code looks for the claim's numbers and literal phrases.** Each claim comes with a few *needles*: short strings that must appear in the source if the claim is right, such as `55%`, `636` or `never replace ultimate human responsibility`. Code searches every downloaded text for each needle and records where it found it, or that it did not.

**4. Code cuts the passages.** It builds a short reading file for the jury: the abstracts, plus the text around each needle it found. The jury reads these passages, not the whole internet.

**5. A jury of three models from three companies decides.** DeepSeek V4 Pro, Qwen3.7 Plus (Alibaba) and Gemini 3.1 Flash-Lite (Google), called through OpenRouter, each receive the work, the claim and the passages. Each one must copy the passage that decides, and return one of four verdicts:

- **supports**: the passages say this, including numbers and literal quotes (a faithful translation counts);
- **partly supports**: part of it is said, or the claim goes beyond, exaggerates or distorts the source;
- **does not support**: the passages say something else, or the opposite;
- **passages insufficient**: the passages do not deal with the point.

The judges may use only the passages, not their own knowledge of the work. The final verdict is the one at least two judges gave. When all three disagree, the claim is marked as **split**.

## 3. Why this design

It is the principle of Level 3: **code where it can, AI with checking where it must.**

- Finding a work, comparing a title, a year or an author, and searching a text for a number are tasks with one right answer. Code does them the same way every time, and when it fails, it fails in plain sight.
- Deciding whether a passage supports a sentence requires reading. That is the one step left to AI, and it is checked: three models from three different companies, each one blind to the others, decide by majority.
- The judges read only what code found, so a judge cannot invent a quote that is not in the source.

## 4. Run it

You need the setup from [Getting started](getting-started.md), with the three keys: `OPENROUTER_API_KEY` (the jury), `OPENALEX_API_KEY` (OpenAlex) and `BRAVE_API_KEY` (the web searches for books, web pages and primary sources). In PowerShell, at the repository root, with the environment active:

```powershell
python -m bibcheck.run
```

The command checks every reference and every claim in `bibcheck/data.py`, prints the start of the report, and writes the two output files (section 6).

You can also ask Claude Code, in the repository folder:

```text
Read docs/bibliography-check.md, run python -m bibcheck.run and show me every claim whose verdict is not "supports", with the judges' reasons.
```

## 5. Check your own bibliography

All the data is in one file, `bibcheck/data.py`, in two lists: `REFS` (the works) and `CLAIMS` (the sentences that cite them). Replace the example entries with yours and run the command again. Nothing in this file is trusted: identifiers, links and texts are always found by code.

### The works: `REFS`

```python
REFS = [
    {"id": "walters", "kind": "paper",
     "title": "Fabrication and errors in the bibliographic citations generated by ChatGPT",
     "authors": ["Walters", "Wilder"], "year": 2023, "venue": "Scientific Reports"},
    {"id": "unesco", "kind": "web",
     "title": "Recommendation on the Ethics of Artificial Intelligence",
     "authors": ["UNESCO"], "year": 2021, "venue": "UNESCO",
     "query": "UNESCO Recommendation on the Ethics of Artificial Intelligence \"never replace ultimate human responsibility\""},
]
```

| Field | Required | What to write |
| --- | --- | --- |
| `id` | yes | a short name you choose, used by the claims to point at this work |
| `kind` | yes | `paper` (article, conference paper, preprint), `book`, or `web` (report, blog post, law, page) |
| `title` | yes | the title as published, in its original language |
| `authors` | yes | a list of surnames; the first one is the one code checks |
| `year` | yes | the year of publication |
| `venue` | yes | journal, conference, publisher or site; write `arXiv` for a preprint, and code skips the venue check |
| `query` | for `book` and `web` | the web search that should find the work; quotes force an exact phrase |

### The claims: `CLAIMS`

```python
CLAIMS = [
    {"id": "c12", "page": 12, "refs": ["walters"],
     "claim": "55% of the references of ChatGPT-3.5 were fabricated; 18% in ChatGPT-4, in the same test; 636 references across the two models.",
     "needles": ["55%", "18%", "636"]},
    {"id": "n04", "page": 40, "refs": ["unesco"],
     "claim": "An AI system can never replace ultimate human responsibility and accountability.",
     "needles": ["never replace ultimate human responsibility"], "prefer": "unesco.org"},
]
```

| Field | Required | What to write |
| --- | --- | --- |
| `id` | yes | a short name for the claim |
| `page` | yes | where the claim is in your text (page, slide or section number), shown in the report |
| `refs` | yes | the `id` of the cited works; the first one is the work the jury is told about, and the texts of all of them are searched |
| `claim` | yes | the sentence exactly as it appears in your text, in any language |
| `needles` | yes | short literal strings or numbers that must appear in the source if the claim is right |
| `extra` | no | extra web searches aimed at the primary source, when the records are not enough |
| `prefer` | no | the domain of the primary source, such as `nature.com` or `in.gov.br`; its results are opened first |

Tips for good needles:

- Write them in the **language of the source**, not of your text. A claim in Portuguese about an English article needs English needles.
- Prefer **numbers and distinctive phrases** over common words. `636` says more than `references`.
- Write a number the way the source writes it. When in doubt, list both forms, such as `"11.9"` and `"11,9"`.
- The search ignores upper and lower case, so `hallucinat` finds both *hallucinate* and *hallucination*.
- A needle that is not found is a signal, not a verdict: the text may be behind a paywall. The jury still reads what code found.

## 6. The outputs

**`bibcheck/REPORT.md`** is the report to read. It has two parts:

- **Works**: one line per reference, saying whether the work exists, and whether author, year and venue match, plus what code was able to read (abstract, full text, publisher page, web page).
- **Claims**: one block per claim, with the final verdict, the claim itself, which needles code found, and the verdict and reason of each of the three judges.

**`bibcheck/result.json`** holds the same data in full, for programs and for auditing:

- `refs`: for each work, what each record returned, the four checks, and the list of texts code read;
- `claims`: for each claim, where each needle was found, the vote of each judge (the passage it copied, its verdict and its reason), the final verdict, and every source read.

## 7. Cost and cache

The only paid part is the jury: three calls on OpenRouter per claim, which cost **cents per claim**. The searches in OpenAlex, DBLP, arXiv, Crossref and OpenLibrary are free; the web searches use your Brave Search plan.

Records, downloaded texts and every judge answer are saved on disk. A judge answer is saved in `bibcheck/cache/`, tied to exactly what the judge read: when a new run gives the judge the same passages, the saved answer is reused and costs nothing. If you edit one claim, only that claim goes back to the jury.

## 8. How to use the result

The check points where to look; it does not sign for you. The agent speeds up, the researcher decides.

- **supports**: open the passage the judges copied and confirm it in the source before you cite it.
- **partly supports**: the most useful verdict. Read the judges' reasons: usually the text goes one step further than the source, and one word fixes it.
- **does not support**: read the source; either the claim or the reference is wrong.
- **passages insufficient** or **split**: code did not reach the right text, often because it is closed. Read the source yourself.
- A work that does not exist in any record, or with the wrong author or year, is the first thing to fix.

The researcher answers for the final text. The CNPq Portaria 2.664/2026 (art. 9, I) asks researchers to declare the use of generative AI, with the tool and the purpose, and states that the researcher answers for the final content, including errors that came from AI.
