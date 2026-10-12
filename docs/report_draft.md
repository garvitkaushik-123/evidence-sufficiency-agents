# When Is Enough Evidence Enough? Sufficiency Judgments and Stopping Rules in Multi-Step Retrieval Agents

*Technical report, first draft. Numbers come from `results/` and `runs/`; `[CHECK]` marks places the author must confirm or fill in. Not a publication.*

## Abstract

A retrieval agent that searches in several steps must decide when it has seen enough. We let two Gemini models retrieve for five steps over a BM25 index and, after every step, state whether the evidence suffices, how likely that is, and their current answer. Logging every step lets us replay any stopping rule offline from one run per model. On 500 HotpotQA and 500 MuSiQue questions we ask how often "enough" is true, whether the judgement predicts a correct answer, and which rule gives the best accuracy for the retrieval spent. Stopping at the first "sufficient" verdict uses 34 to 67% fewer steps than always taking five, at an answer-F1 cost that is not significant in three of four model and dataset pairs and about 0.025 in the fourth. Model choice moves F1 by 0.07 to 0.26, far more than any rule. Against "all gold paragraphs retrieved" the verdict is right 65 to 93% of the time, but a manual read of 50 apparent premature stops found about three in four already answerable from the retrieved text, so gold coverage understates it. Stated probabilities sit near 0 and 1 and are poorly calibrated.

## 1. Introduction

Agents that search before answering spend a cost with every retrieval step: time, tokens and money. Stopping too early risks a wrong answer; stopping too late wastes retrieval. The agent's own sense of "I have enough" is the obvious signal, but it is rarely tested against ground truth. We test it.

Three questions:
- **RQ1.** When the agent says the evidence suffices, how often is that true?
- **RQ2.** Does the judgement, or the stated probability, predict whether the final answer is correct, and is it calibrated?
- **RQ3.** Which stopping rule (fixed steps, first sufficient verdict, probability threshold, oracle) gives the best accuracy per retrieval step?

Multi-hop QA datasets mark which paragraphs are needed, so "sufficient" has an objective reading without human labelling: all gold supporting paragraphs are in the agent's context. We also use a second, looser label: the gold answer text appears in the retrieved evidence.

## 2. Related work

*(Use the paragraph in `docs/related_work.md`, section 3, and the table in section 2 if space allows. Cite `joren2025sufficient`, `trivedi2023ircot`, `jiang2023flare`, `asai2023selfrag`, `jeong2024adaptiverag`, `lu2025agentrewardbench`.)* [CHECK: re-read the paragraph against the papers once more.]

## 3. Setup

**Data.** HotpotQA distractor dev (Yang et al., 2018) and MuSiQue-Ans dev (Trivedi et al., 2022); 500 questions each, sampled with a fixed seed (IDs in `data/ids/`). HotpotQA was taken from the HuggingFace mirror and converted to the original format. Each dataset's corpus pools and deduplicates the paragraphs of its 500 sampled questions: 4,945 paragraphs for HotpotQA and 7,017 for MuSiQue.

**Agent loop.** Up to T = 5 steps. Step 1 searches with the question. Later steps search with a query the model writes from the question and the evidence so far. BM25 (Robertson and Zaragoza, 2009) returns k = 3 paragraphs per step, excluding paragraphs already retrieved, so the context grows to 15 distinct paragraphs. After every step the model, which sees only the question and the evidence, outputs a verdict (SUFFICIENT or INSUFFICIENT), a probability that the evidence suffices, and its current answer. The agent always runs all five steps and everything is logged.

**Models.** `gemini-3.5-flash-lite` (small) and `gemini-3.8-flash` (strong), run on 11 and 12 October 2026 with temperature 0. Both are thinking models, so reruns need not be bit-identical; the committed logs are the record. [CHECK: dates of the runs.]

**Stopping rules, computed offline from the logs.** Fixed-k (k = 1, 3, 5); self-judge (stop at the first SUFFICIENT verdict, else step 5); threshold (first step with probability at least tau, tau from 0.5 to 0.95); oracle (first step where all gold paragraphs are in context, else step 5).

**Metrics.** Answer exact match and token F1 after lower-casing and removing punctuation and articles, taking the best match over aliases. RQ1: precision, recall and F1 of the verdict against each label, over all (question, step) pairs; a premature stop is SUFFICIENT with the label false, over-retrieval is INSUFFICIENT with the label true. RQ2: AUROC and expected calibration error (10 bins) of the stated probability against answer exact match. RQ3: mean steps and F1 with 95% bootstrap confidence intervals over questions (1,000 resamples), and paired bootstrap tests (2,000 resamples) for differences between rules and between models on the same questions.

## 4. Results

### 4.1 RQ3: stopping rules (Table 1, Figure 1)

| | HotpotQA small | HotpotQA strong | MuSiQue small | MuSiQue strong |
|---|---|---|---|---|
| fixed-1: F1 | 0.440 | 0.643 | 0.145 | 0.406 |
| fixed-3: F1 | 0.736 | 0.800 | 0.413 | 0.637 |
| fixed-5: F1 | 0.730 | 0.803 | 0.455 | 0.676 |
| self-judge: steps, F1 | 1.63, 0.705 | 1.77, 0.793 | 2.94, 0.452 | 3.29, 0.673 |
| oracle: steps, F1 | 1.93, 0.725 | 1.91, 0.805 | 3.48, 0.440 | 3.40, 0.688 |

*Table 1. Answer F1 by stopping rule, 500 questions per dataset. 95% intervals are in `results/rule_tables.md`. Figure 1: `results/figures/accuracy_vs_steps.png`.*

- **Self-judging saves most of the retrieval at little cost in accuracy.** It uses 1.6 to 1.8 of five steps on HotpotQA (65 to 67% fewer) and 2.9 to 3.3 on MuSiQue (34 to 41% fewer). Compared with always taking five steps, the F1 difference is -0.003 on MuSiQue for both models (intervals [-0.028, +0.022] and [-0.015, +0.008]) and -0.010 for the strong model on HotpotQA ([-0.023, +0.002]), none significant. For the small model on HotpotQA it is -0.025 ([-0.049, -0.001]), a small but significant loss.
- **On MuSiQue more steps matter.** Fixed-3 is worse than fixed-5 by about 0.04 F1 for both models (significant), whereas on HotpotQA 3 and 5 steps do not differ. At roughly the same number of steps (0.06 fewer for the small model, 0.29 more for the strong one), self-judge beats fixed-3 on MuSiQue by 0.035 to 0.040 F1 (significant): it spends steps where they are needed.
- **The oracle is only slightly better than self-judge.** The gain is at most 0.02 F1 (0.011 to 0.019 on HotpotQA and 0.016 for the strong model on MuSiQue, significant; -0.012 for the small model on MuSiQue, not significant). Knowing exactly when the gold evidence is complete is worth little here.
- **Thresholds add little.** For tau = 0.7 and 0.8 the result matches self-judge to within 0.001 F1 in all four cases. tau = 0.5 differs only for the small model on HotpotQA (F1 -0.04, 1.55 steps). tau = 0.9 and 0.95 let the strong model take up to 0.2 more steps for at most +0.007 F1 (see 4.3).
- **The model matters far more than the rule.** The strong model beats the small one by 0.07 to 0.26 F1 under every rule on both datasets, all significant.

### 4.2 RQ1: how often is "enough" true? (Table 2)

| | Label | precision | recall | premature stops | over-retrieval |
|---|---|---|---|---|---|
| HotpotQA small | gold coverage | 0.900 | 0.945 | 211 | 110 |
| | answer in context | 0.958 | 0.912 | 83 | 183 |
| HotpotQA strong | gold coverage | 0.929 | 0.952 | 147 | 97 |
| | answer in context | 0.980 | 0.912 | 38 | 183 |
| MuSiQue small | gold coverage | 0.646 | 0.771 | 452 | 245 |
| | answer in context | 0.863 | 0.685 | 175 | 507 |
| MuSiQue strong | gold coverage | 0.783 | 0.790 | 245 | 236 |
| | answer in context | 0.946 | 0.650 | 61 | 577 |

*Table 2. SUFFICIENT verdicts against two labels, over 2,500 (question, step) pairs per cell (fewer for the second label, which skips yes/no questions on HotpotQA).*

Precision depends strongly on the label. Against gold coverage the verdict is right 90 to 93% of the time on HotpotQA and 65 to 78% on MuSiQue; against answer-in-context it is right 96 to 98% and 86 to 95%. Premature stops are concentrated at step 1: of the questions where the small model said SUFFICIENT at step 1, 126 of 301 (HotpotQA) and 90 of 122 (MuSiQue) still lacked a gold paragraph; for the strong model, 72 of 246 and 33 of 64. The strong model makes fewer premature stops than the small one. Over-retrieval grows under the looser label, so the models are cautious as well as sometimes hasty. On MuSiQue the gold paragraphs are not all retrieved within five steps for 177 (strong) to 189 (small) of 500 questions, against 21 to 25 on HotpotQA, a BM25 limit that caps what any rule can reach.

### 4.3 RQ2: does the judgement predict correctness? (Figure 2)

The stated probability predicts answer exact match modestly: AUROC 0.65 and 0.66 on HotpotQA and 0.84 (small) and 0.72 (strong) on MuSiQue; expected calibration error is 0.24 to 0.34. The probabilities cluster at the ends: the small model says exactly 0 or 1 in 93 to 94% of judgements, the strong model in 61% (HotpotQA) and 25% (MuSiQue), with 91% and 75% within 0.1 of an extreme. The reliability diagram (`results/figures/reliability.png`) shows that stating 1 corresponds to answers that are right about 54 to 67% of the time. [CHECK: read exact values off the figure data before quoting.] The small model's higher AUROC on MuSiQue is not explained by this study; it may reflect its lower accuracy and more separable verdicts. [CHECK: either test this or drop the sentence.]

## 5. Error analysis

We sampled 50 of the 188 premature stops of the strong model (25 per dataset, fixed seed) and tagged why the agent stopped (`results/error_analysis/`). **The tagging was done by an LLM, not a human; re-tag before quoting.** [CHECK: a human re-tag of at least a dozen cases.]

| cause | HotpotQA | MuSiQue |
|---|---|---|
| answerable from the retrieved evidence | 20 | 17 |
| parametric (answer from the model's own knowledge) | 3 | 2 |
| ambiguous question or gold label | 0 | 3 |
| partial answer | 2 | 0 |
| distractor taken as evidence | 0 | 2 |
| needed hop never retrieved | 0 | 1 |

In 37 of 50 cases the answer was already supported by the retrieved text; the missing gold paragraph was a bridge or descriptor page. An automatic check on all premature stops agrees: the gold answer text is already in the evidence in 76% of the strong model's premature stops on both datasets and in 60% (HotpotQA) and 50% (MuSiQue) of the small model's. So gold coverage is a conservative proxy for sufficiency, and the small model stops genuinely too early more often. Real failures are few and instructive: taking a career scoring record for a single-season record, picking the wrong person of the same name, and skipping the hop that links an author to the statement being asked about. Several exact-match misses are formatting only (for example "Poland" against "Polish state"), so F1 is the fairer metric.

## 6. Limitations

- Two Gemini models from one family, 500 questions per dataset, one retriever (BM25); a dense retriever is untested.
- The pooled corpus is much smaller than open-domain search, so retrieval is easier than in practice.
- Gold coverage is a proxy for sufficiency, and the answer-in-context label is lenient (a string match can be coincidental). The truth lies between them.
- The verdict is the answering model's own, produced with a fixed prompt; other prompts could change it.
- The error analysis is a single LLM tagger on 50 of 188 cases.
- Thinking models are not bit-reproducible, and the HotpotQA data comes from a mirror of the official release.

## 7. Conclusion and next steps

Letting a model decide when to stop retrieving worked well here: a third to two thirds of the retrieval saved, at an accuracy cost that is mostly not distinguishable from zero, and a choice of model that matters far more than the choice of rule. Its judgement is better than gold coverage suggests but its stated probability is a coarse, poorly calibrated signal. A thesis could test a dense retriever and open-domain corpora, add a separate sufficiency judge as in Joren et al. (2025) to compare with self-judgement, train or calibrate the stopping signal, and run the same loop with open-weights models.

## References

See `refs.bib`.
