# Paired bootstrap tests

F1 difference A - B over the same 500 questions (2,000 resamples of questions). Compare rules within a model, then models within a rule.

## hotpotqa, gemini-3.5-flash-lite: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | -0.025 | [-0.049, -0.001] | yes | -3.37 |
| self-judge - fixed-3 | -0.030 | [-0.052, -0.007] | yes | -1.37 |
| oracle - self-judge | +0.019 | [+0.001, +0.037] | yes | +0.30 |
| fixed-3 - fixed-5 | +0.005 | [-0.017, +0.027] | no | -2.00 |

## hotpotqa, gemini-3.8-flash: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | -0.010 | [-0.023, +0.002] | no | -3.23 |
| self-judge - fixed-3 | -0.007 | [-0.019, +0.006] | no | -1.23 |
| oracle - self-judge | +0.011 | [+0.002, +0.020] | yes | +0.14 |
| fixed-3 - fixed-5 | -0.003 | [-0.015, +0.008] | no | -2.00 |

## hotpotqa, gemini-3.5-flash-lite__dense: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | +0.025 | [+0.006, +0.045] | yes | -3.76 |
| self-judge - fixed-3 | +0.011 | [-0.007, +0.031] | no | -1.76 |
| oracle - self-judge | -0.020 | [-0.036, -0.007] | yes | -0.06 |
| fixed-3 - fixed-5 | +0.014 | [-0.004, +0.031] | no | -2.00 |

## hotpotqa: dense - BM25 retriever (gemini-3.5-flash-lite), same rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| fixed-1 | +0.277 | [+0.237, +0.318] | yes | +0.00 |
| fixed-3 | +0.021 | [+0.000, +0.043] | yes | +0.00 |
| fixed-5 | +0.013 | [-0.010, +0.036] | no | +0.00 |
| self-judge | +0.063 | [+0.037, +0.089] | yes | -0.38 |
| oracle | +0.023 | [-0.002, +0.048] | no | -0.75 |

## hotpotqa: gemini-3.8-flash - gemini-3.5-flash-lite, same rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| fixed-1 | +0.203 | [+0.167, +0.238] | yes | +0.00 |
| fixed-3 | +0.065 | [+0.039, +0.092] | yes | +0.00 |
| fixed-5 | +0.073 | [+0.047, +0.099] | yes | +0.00 |
| self-judge | +0.088 | [+0.061, +0.116] | yes | +0.15 |
| oracle | +0.080 | [+0.054, +0.106] | yes | -0.02 |

## musique, gemini-3.5-flash-lite: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | -0.003 | [-0.028, +0.022] | no | -2.06 |
| self-judge - fixed-3 | +0.040 | [+0.013, +0.068] | yes | -0.06 |
| oracle - self-judge | -0.012 | [-0.038, +0.013] | no | +0.54 |
| fixed-3 - fixed-5 | -0.043 | [-0.069, -0.016] | yes | -2.00 |

## musique, gemini-3.8-flash: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | -0.003 | [-0.015, +0.008] | no | -1.71 |
| self-judge - fixed-3 | +0.035 | [+0.013, +0.059] | yes | +0.29 |
| oracle - self-judge | +0.016 | [+0.005, +0.027] | yes | +0.11 |
| fixed-3 - fixed-5 | -0.039 | [-0.061, -0.017] | yes | -2.00 |

## musique, gemini-3.5-flash-lite__dense: rule vs rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| self-judge - fixed-5 | +0.000 | [-0.028, +0.028] | no | -2.61 |
| self-judge - fixed-3 | +0.026 | [-0.001, +0.054] | no | -0.61 |
| oracle - self-judge | -0.008 | [-0.031, +0.017] | no | +0.36 |
| fixed-3 - fixed-5 | -0.026 | [-0.050, -0.001] | yes | -2.00 |

## musique: dense - BM25 retriever (gemini-3.5-flash-lite), same rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| fixed-1 | +0.186 | [+0.149, +0.222] | yes | +0.00 |
| fixed-3 | +0.083 | [+0.051, +0.116] | yes | +0.00 |
| fixed-5 | +0.066 | [+0.032, +0.101] | yes | +0.00 |
| self-judge | +0.069 | [+0.034, +0.104] | yes | -0.55 |
| oracle | +0.073 | [+0.042, +0.106] | yes | -0.74 |

## musique: gemini-3.8-flash - gemini-3.5-flash-lite, same rule

| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |
|---|---|---|---|---|
| fixed-1 | +0.261 | [+0.224, +0.297] | yes | +0.00 |
| fixed-3 | +0.224 | [+0.187, +0.265] | yes | +0.00 |
| fixed-5 | +0.220 | [+0.182, +0.261] | yes | +0.00 |
| self-judge | +0.220 | [+0.179, +0.260] | yes | +0.35 |
| oracle | +0.248 | [+0.208, +0.288] | yes | -0.08 |
