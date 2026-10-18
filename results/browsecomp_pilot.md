# BrowseComp-Plus pilot (100 questions, pooled corpus, T=8, k=3)

LLM-judged accuracy (BrowseComp-Plus grader prompt, judge gemini-3.8-flash). Aggregates only.

### gemini-3.5-flash-lite (100 questions, T=8, k=3, bm25)

| rule | avg steps | judged accuracy (95% CI) | exact match | vs fixed-8 (accuracy, 95% CI; steps) |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.200 [0.120, 0.280] | 0.160 | -0.390 [-0.490, -0.290]; -7.00 steps |
| fixed-4 | 4.00 | 0.550 [0.450, 0.650] | 0.470 | -0.040 [-0.120, +0.040]; -4.00 steps |
| fixed-8 | 8.00 | 0.590 [0.490, 0.690] | 0.500 | baseline |
| self-judge | 3.83 | 0.580 [0.480, 0.680] | 0.480 | -0.010 [-0.070, +0.050]; -4.17 steps |
| tau-0.8 | 3.78 | 0.580 [0.480, 0.680] | 0.480 | -0.010 [-0.070, +0.050]; -4.22 steps |
| oracle (gold covered) | 5.09 | 0.600 [0.500, 0.700] | 0.480 | +0.010 [-0.040, +0.060]; -2.91 steps |

RQ1: verdict SUFFICIENT against each sufficiency label, over all (question, step) pairs

| label | precision | recall | premature stops | over-retrieval | n |
|---|---|---|---|---|---|
| gold coverage | 0.652 | 0.794 | 152 | 74 | 800 |
| strict (all evidence) | 0.279 | 0.819 | 315 | 27 | 800 |
| answer in context | 0.760 | 0.822 | 105 | 72 | 800 |

RQ2 (stated probability vs judged correctness): AUROC 0.896, AUROC on answered steps 0.525, ECE 0.110, n=799 (341 abstention-like answers).
Self-judge: SUFFICIENT at step 1 for 17 questions, never SUFFICIENT for 18; verdict SUFFICIENT in 437 of 800 steps.
Hedged answers: 1 of the 59 judged-correct fixed-8 answers contain a hedge word; accuracy without them 0.580.

### gemini-3.8-flash (100 questions, T=8, k=3, bm25)

| rule | avg steps | judged accuracy (95% CI) | exact match | vs fixed-8 (accuracy, 95% CI; steps) |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.370 [0.270, 0.460] | 0.280 | -0.400 [-0.500, -0.310]; -7.00 steps |
| fixed-4 | 4.00 | 0.710 [0.620, 0.790] | 0.590 | -0.060 [-0.110, -0.020]; -4.00 steps |
| fixed-8 | 8.00 | 0.770 [0.690, 0.850] | 0.640 | baseline |
| self-judge | 4.18 | 0.780 [0.700, 0.860] | 0.660 | +0.010 [+0.000, +0.030]; -3.82 steps |
| tau-0.8 | 4.18 | 0.780 [0.700, 0.860] | 0.660 | +0.010 [+0.000, +0.030]; -3.82 steps |
| oracle (gold covered) | 4.82 | 0.770 [0.690, 0.850] | 0.660 | +0.000 [+0.000, +0.000]; -3.18 steps |

RQ1: verdict SUFFICIENT against each sufficiency label, over all (question, step) pairs

| label | precision | recall | premature stops | over-retrieval | n |
|---|---|---|---|---|---|
| gold coverage | 0.730 | 0.813 | 116 | 72 | 800 |
| strict (all evidence) | 0.323 | 0.908 | 291 | 14 | 800 |
| answer in context | 0.863 | 0.823 | 59 | 80 | 800 |

RQ2 (stated probability vs judged correctness): AUROC 0.959, AUROC on answered steps 0.876, ECE 0.090, n=800 (208 abstention-like answers).
Self-judge: SUFFICIENT at step 1 for 17 questions, never SUFFICIENT for 26; verdict SUFFICIENT in 430 of 800 steps.
Hedged answers: 0 of the 77 judged-correct fixed-8 answers contain a hedge word; accuracy without them 0.770.

