# Rule tables (data behind the figures)

## HotpotQA, gemini-3.5-flash-lite

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.336 | 0.440 | [0.402, 0.479] |
| fixed-3 | 3.00 | 0.584 | 0.736 | [0.702, 0.768] |
| fixed-5 | 5.00 | 0.564 | 0.730 | [0.697, 0.763] |
| self-judge | 1.63 | 0.544 | 0.705 | [0.671, 0.741] |
| tau-0.5 | 1.55 | 0.506 | 0.665 | [0.630, 0.702] |
| tau-0.7 | 1.63 | 0.544 | 0.704 | [0.669, 0.740] |
| tau-0.8 | 1.63 | 0.544 | 0.704 | [0.669, 0.740] |
| tau-0.9 | 1.63 | 0.544 | 0.705 | [0.671, 0.741] |
| tau-0.95 | 1.63 | 0.544 | 0.705 | [0.671, 0.741] |
| oracle | 1.93 | 0.566 | 0.725 | [0.690, 0.759] |

## HotpotQA, gemini-3.8-flash

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.502 | 0.643 | [0.607, 0.683] |
| fixed-3 | 3.00 | 0.638 | 0.800 | [0.772, 0.830] |
| fixed-5 | 5.00 | 0.632 | 0.803 | [0.774, 0.832] |
| self-judge | 1.77 | 0.616 | 0.793 | [0.766, 0.823] |
| tau-0.5 | 1.77 | 0.616 | 0.793 | [0.766, 0.823] |
| tau-0.7 | 1.77 | 0.616 | 0.793 | [0.766, 0.823] |
| tau-0.8 | 1.77 | 0.616 | 0.793 | [0.766, 0.823] |
| tau-0.9 | 1.80 | 0.622 | 0.799 | [0.771, 0.827] |
| tau-0.95 | 1.82 | 0.622 | 0.800 | [0.773, 0.828] |
| oracle | 1.91 | 0.632 | 0.805 | [0.776, 0.834] |

## HotpotQA, gemini-3.5-flash-lite__dense

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.568 | 0.717 | [0.684, 0.753] |
| fixed-3 | 3.00 | 0.590 | 0.757 | [0.725, 0.790] |
| fixed-5 | 5.00 | 0.580 | 0.743 | [0.712, 0.775] |
| self-judge | 1.24 | 0.608 | 0.768 | [0.739, 0.801] |
| tau-0.5 | 1.21 | 0.606 | 0.766 | [0.737, 0.798] |
| tau-0.7 | 1.24 | 0.606 | 0.767 | [0.737, 0.800] |
| tau-0.8 | 1.24 | 0.606 | 0.767 | [0.737, 0.800] |
| tau-0.9 | 1.24 | 0.608 | 0.768 | [0.739, 0.801] |
| tau-0.95 | 1.24 | 0.608 | 0.768 | [0.739, 0.801] |
| oracle | 1.18 | 0.590 | 0.748 | [0.716, 0.781] |

## MuSiQue, gemini-3.5-flash-lite

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.094 | 0.145 | [0.117, 0.172] |
| fixed-3 | 3.00 | 0.310 | 0.413 | [0.374, 0.450] |
| fixed-5 | 5.00 | 0.344 | 0.455 | [0.420, 0.493] |
| self-judge | 2.94 | 0.342 | 0.452 | [0.414, 0.491] |
| tau-0.5 | 2.93 | 0.340 | 0.451 | [0.413, 0.490] |
| tau-0.7 | 2.94 | 0.340 | 0.451 | [0.413, 0.490] |
| tau-0.8 | 2.94 | 0.340 | 0.451 | [0.413, 0.490] |
| tau-0.9 | 2.94 | 0.342 | 0.452 | [0.414, 0.491] |
| tau-0.95 | 2.94 | 0.342 | 0.452 | [0.414, 0.491] |
| oracle | 3.48 | 0.340 | 0.440 | [0.402, 0.478] |

## MuSiQue, gemini-3.8-flash

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.286 | 0.406 | [0.367, 0.445] |
| fixed-3 | 3.00 | 0.474 | 0.637 | [0.603, 0.669] |
| fixed-5 | 5.00 | 0.514 | 0.676 | [0.642, 0.709] |
| self-judge | 3.29 | 0.514 | 0.673 | [0.639, 0.706] |
| tau-0.5 | 3.29 | 0.514 | 0.673 | [0.639, 0.706] |
| tau-0.7 | 3.29 | 0.514 | 0.673 | [0.639, 0.706] |
| tau-0.8 | 3.29 | 0.514 | 0.673 | [0.639, 0.706] |
| tau-0.9 | 3.46 | 0.514 | 0.673 | [0.639, 0.705] |
| tau-0.95 | 3.48 | 0.514 | 0.673 | [0.638, 0.705] |
| oracle | 3.40 | 0.522 | 0.688 | [0.655, 0.720] |

## MuSiQue, gemini-3.5-flash-lite__dense

| rule | avg steps | EM | F1 | F1 95% CI |
|---|---|---|---|---|
| fixed-1 | 1.00 | 0.246 | 0.331 | [0.294, 0.368] |
| fixed-3 | 3.00 | 0.376 | 0.496 | [0.457, 0.537] |
| fixed-5 | 5.00 | 0.402 | 0.521 | [0.486, 0.561] |
| self-judge | 2.39 | 0.408 | 0.522 | [0.483, 0.564] |
| tau-0.5 | 2.38 | 0.408 | 0.522 | [0.485, 0.565] |
| tau-0.7 | 2.39 | 0.406 | 0.522 | [0.484, 0.563] |
| tau-0.8 | 2.39 | 0.406 | 0.522 | [0.484, 0.563] |
| tau-0.9 | 2.39 | 0.406 | 0.522 | [0.484, 0.563] |
| tau-0.95 | 2.39 | 0.406 | 0.522 | [0.484, 0.563] |
| oracle | 2.74 | 0.404 | 0.514 | [0.474, 0.558] |

# RQ1 under two sufficiency labels

Verdict SUFFICIENT vs (a) all gold paragraphs in context, (b) gold answer text in context (yes/no questions skipped).

| dataset | model (or model__dense) | label | precision | recall | F1 | premature | over-retrieval | pairs |
|---|---|---|---|---|---|---|---|---|
| HotpotQA | gemini-3.5-flash-lite | gold coverage | 0.900 | 0.945 | 0.922 | 211 | 110 | 2500 |
| HotpotQA | gemini-3.5-flash-lite | answer in context | 0.958 | 0.912 | 0.934 | 83 | 183 | 2345 |
| HotpotQA | gemini-3.8-flash | gold coverage | 0.929 | 0.952 | 0.940 | 147 | 97 | 2500 |
| HotpotQA | gemini-3.8-flash | answer in context | 0.980 | 0.912 | 0.945 | 38 | 183 | 2345 |
| HotpotQA | gemini-3.5-flash-lite__dense | gold coverage | 0.975 | 0.936 | 0.955 | 58 | 153 | 2500 |
| HotpotQA | gemini-3.5-flash-lite__dense | answer in context | 0.987 | 0.931 | 0.958 | 28 | 158 | 2345 |
| MuSiQue | gemini-3.5-flash-lite | gold coverage | 0.646 | 0.771 | 0.703 | 452 | 245 | 2500 |
| MuSiQue | gemini-3.5-flash-lite | answer in context | 0.863 | 0.685 | 0.764 | 175 | 507 | 2500 |
| MuSiQue | gemini-3.8-flash | gold coverage | 0.783 | 0.790 | 0.787 | 245 | 236 | 2500 |
| MuSiQue | gemini-3.8-flash | answer in context | 0.946 | 0.650 | 0.770 | 61 | 577 | 2500 |
| MuSiQue | gemini-3.5-flash-lite__dense | gold coverage | 0.725 | 0.760 | 0.742 | 436 | 363 | 2500 |
| MuSiQue | gemini-3.5-flash-lite__dense | answer in context | 0.920 | 0.702 | 0.797 | 126 | 619 | 2500 |
# RQ2: stated probability vs answer correctness

AUROC of the stated probability for answer exact match, over all steps, and over steps where the answer is not an abstention (for example 'Not enough information', matched by a keyword list, so approximate). Abstentions are wrong by construction.

| dataset | model | AUROC all steps | AUROC answered steps | ECE | steps | abstention-like answers |
|---|---|---|---|---|---|---|
| HotpotQA | gemini-3.5-flash-lite | 0.654 | 0.513 | 0.340 | 2500 | 352 |
| HotpotQA | gemini-3.8-flash | 0.660 | 0.619 | 0.296 | 2500 | 113 |
| HotpotQA | gemini-3.5-flash-lite__dense | 0.586 | 0.514 | 0.349 | 2500 | 157 |
| MuSiQue | gemini-3.5-flash-lite | 0.835 | 0.511 | 0.243 | 2497 | 1210 |
| MuSiQue | gemini-3.8-flash | 0.717 | 0.632 | 0.253 | 2500 | 385 |
| MuSiQue | gemini-3.5-flash-lite__dense | 0.776 | 0.506 | 0.292 | 2500 | 894 |
