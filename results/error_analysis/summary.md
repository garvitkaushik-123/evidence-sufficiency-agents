# Error analysis: premature stops of the self-judge rule

**Tagging was done by Claude (an LLM), not by a human annotator.** Treat the counts as a first pass: read `cases.md` and re-tag at least a dozen cases before quoting them as final. One cause per case in `tags.csv`.

Sample: 50 of the 188 premature stops of `gemini-3.8-flash` (25 of 84 on HotpotQA, 25 of 104 on MuSiQue, seed 0). A premature stop is the self-judge stop step where the verdict is SUFFICIENT but not all gold paragraphs are in context.

## Causes

| cause | HotpotQA | MuSiQue | total |
|---|---|---|---|
| answerable (shown evidence already supports the answer) | 20 | 17 | 37 |
| parametric (answer rests on the model's own knowledge) | 3 | 2 | 5 |
| ambiguous (question or gold label underdetermined) | 0 | 3 | 3 |
| partial-answer (supported only in part) | 2 | 0 | 2 |
| distractor (a retrieved non-gold page taken as evidence) | 0 | 2 | 2 |
| bridge-missed (needed hop never retrieved) | 0 | 1 | 1 |

## What it says

- **Most "premature" stops are not premature in the sense the question cares about.** In 37 of 50 cases the answer is already supported by what the agent retrieved. The "missing" gold paragraph is usually a bridge or descriptor page (for example the page that says "Eagle Feather coached the Indians") that the question's wording repeats or that the answer does not need. Gold coverage is therefore a conservative proxy for sufficiency: the RQ1 precision figures are lower bounds.
- **Genuine failures are a minority: 8 of 50 (16%)** are distractor, bridge-missed, partial-answer or a wrong reading of an ambiguous question. Five more are right-for-the-wrong-reason (parametric).
- **Many EM misses are formatting.** 'Poland' vs 'Polish state', 'June' vs 'mid-June', 'Season 3' vs 'season three'. F1 is the fairer metric here.
- **The clearest real failure patterns** are on MuSiQue: taking a career record for a single-season record (musique-16), taking the wrong Empress Wang (musique-13), and skipping the hop that says what Gates played up (musique-15).

## Check on the whole pool (automatic, not manual)

Share of all premature stops where the gold answer text already appears in the shown evidence (yes/no questions counted as answerable):

| model | HotpotQA | MuSiQue |
|---|---|---|
| gemini-3.8-flash | 64 of 84 (76%) | 79 of 104 (76%) |
| gemini-3.5-flash-lite | 84 of 139 (60%) | 94 of 187 (50%) |

For the strong model this matches the manual 74% (37 of 50). The small model makes genuinely more premature stops: a larger share of its stops lack the answer in the evidence.

## Second pass

Every case was re-checked mechanically (12 Oct 2026). All 37 `answerable` cases have the gold answer or the model's answer text in the retrieved evidence, or are yes/no questions. The other 13 were re-read; three borderline `parametric` tags (hotpotqa-14, hotpotqa-22, musique-17) were kept because the answer string is present but the link that justifies it is not. No tag changed. This is not a human check.

## Caveats

- Single tagger, single model (`gemini-3.8-flash`), 50 of 188 cases, and the taxonomy was adapted after reading the cases (`answerable` was added because it dominated).
- "Answer in shown evidence" is a string match, so it undercounts paraphrases and counts coincidental mentions.
