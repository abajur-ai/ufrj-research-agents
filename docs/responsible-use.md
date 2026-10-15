[Leia em português](responsible-use.pt-BR.md)

# Responsible use

## In plain words

The agent speeds up, the researcher decides. Even the best level in this test gets articles wrong, and it does not
say which ones. So the agent is a copilot: it searches, screens, extracts and checks the hard data in minutes, and the
researcher defines the question, checks in the original source what will be cited, judges method and finding, and
signs the text. The two traps to avoid are trusting the agent because it is usually right, and handing it the
understanding and the responsibility that belong to the person who signs. Brazil's CNPq already has rules for this.

## Human in the loop

Human in the loop means designing the system so that a person stays inside the process, with a defined role, instead
of receiving the machine's output at the end (Wu et al., 2022). In a literature review, the split is:

| The agent | The researcher |
| --- | --- |
| Searches the databases and reads the abstracts | Defines the question and the scope |
| Screens and extracts the data | Checks in the original source what will be cited |
| Checks the hard data by code | Judges the method and the finding |
| Delivers in minutes, at low cost | Signs and answers for the text |

The split follows the results. Code checks the hard data (DOI, author, year, journal) almost perfectly; the errors
that remain are of scope, method and finding, which require reading. That is where the researcher's attention pays
off most.

### Automation bias

With an automatic assistant as copilot, the tendency is to accept the answer and stop checking properly. This is
automation bias: people give the automated recommendation more weight than it deserves, and check less when the
system is usually right (Parasuraman and Manzey, 2010). It is not a beginner's mistake. It affects experts too, and it
grows with the reliability of the system: the better the agent, the easier it is to stop looking.

In practice: refine the agent for your topic, compare different approaches, and keep the checking. Decide in advance
what you will check for every article you cite, and check it even when the agent has been right many times in a row.

## Reliability: even the best level errs

Of every 100 articles requested from Level 3, by the three-company jury across the 48 runs of this test: **81 right,
2 wrong and 17 not delivered.** The agent does not say which are the 2. Finding the error is the researcher's job.

This is not a defect of one agent that a better prompt will remove. Kalai and Vempala (2024) show that a language
model that is well calibrated must still invent part of the rare facts: facts that appear rarely in its training data
cannot all be told apart from plausible fabrications. Error is part of the method. The architecture can lower it (from
17% wrong at Level 0 to 2% at Level 3, see [results.md](results.md)), not take it to zero.

Humans err too. In medical journals, 25% of quotations have an error, and 12% have a major one (Jergas and Baethge,
2015). The useful question is not whether the agent errs, but how its errors compare with a careful researcher's, and
how to catch them.

## Limits of AI use

Some things are not handed to a machine, however good it becomes.

**Understanding.** Messeri and Crockett (2024) warn that AI tools can create illusions of understanding: the feeling
of knowing more than one does, because the tool did the reading.

> "The proliferation of AI tools in science risks introducing a phase of scientific enquiry in which we produce more
> but understand less."
>
> Messeri and Crockett, *Artificial intelligence and illusions of understanding in scientific research*, Nature, 2024.

An agent that delivers 25 articles in five minutes has produced a list, not an understanding of the field. Reading
what will be cited is still the researcher's work.

**Responsibility.** The UNESCO Recommendation on the Ethics of Artificial Intelligence, paragraph 36:

> "an AI system can never replace ultimate human responsibility and accountability"
>
> UNESCO, *Recommendation on the Ethics of Artificial Intelligence*, 2021, paragraph 36.

**Authorship.** The Nature editorial that set its rules for AI tools:

> "any attribution of authorship carries with it accountability for the work, and AI tools cannot take such
> responsibility"
>
> Nature, editorial, v. 613, p. 612, 2023.

An agent can be a tool in the method section. It cannot be an author.

## The CNPq rules

CNPq Portaria nº 2.664/2026, the Policy for Integrity in Scientific Activity, article 9, item I (summarized; the
original is in Portuguese):

| Article | Rule |
| --- | --- |
| Art. 9, I, c | Declare the use of generative AI in any phase of the research, with the tool and the purpose. |
| Art. 9, I, d | It is forbidden to submit AI-generated content as if it were human authorship. |
| Art. 9, I, e | It is forbidden to put third-party projects into AI to write peer reviews. |
| Art. 9, I, f | The researcher answers for the final content, including plagiarism or inaccuracies of the AI. |

Applied to this repository: if you use an agent like Level 3 in a review, declare it, with the tool and what it did
(searching, screening, extraction); check what you cite; and treat its output as your responsibility.

## Questions to reflect on

The questions the class closes with:

1. Can you trust an AI agent to do a literature review? (A) No. (B) Yes, with it doing everything alone. (C) Yes, as
   my copilot.
2. What would you check in an agent that errs 2%?
3. How much of the time the agent saves should go into checking?
4. What error rate is acceptable in a literature review: zero, or that of an experienced researcher?
5. Where does the AI's role end and the human's begin?
6. In your dissertation, where and in how much detail would you declare the use of AI?

## References for this document

Brasil, CNPq, Portaria nº 2.664/2026; Jergas and Baethge (2015); Kalai and Vempala (2024); Messeri and Crockett
(2024); Nature (2023); Parasuraman and Manzey (2010); UNESCO (2021); Wu et al. (2022). Full entries in
[references.md](references.md).
