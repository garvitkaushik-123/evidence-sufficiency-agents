# Error analysis: premature stops of the self-judge rule

Tags were read and checked by hand (single annotator). Review changed 3 of 50 tags (musique-08, musique-13, hotpotqa-06). One cause per case in `tags.csv`; `cases.md` has the evidence.

Sample: 50 of the 188 premature stops of `gemini-3.8-flash` (25 of 84 on HotpotQA, 25 of 104 on MuSiQue, seed 0). A premature stop is the self-judge stop step where the verdict is SUFFICIENT but not all gold paragraphs are in context.

## Causes

| cause | HotpotQA | MuSiQue | total |
|---|---|---|---|
| answerable (shown evidence already supports the answer) | 20 | 14 | 34 |
| parametric (answer rests on the model's own knowledge) | 2 | 5 | 7 |
| ambiguous (question or gold label underdetermined) | 0 | 4 | 4 |
| partial-answer (supported only in part) | 3 | 0 | 3 |
| distractor (a retrieved non-gold page taken as evidence) | 0 | 1 | 1 |
| bridge-missed (needed hop never retrieved) | 0 | 1 | 1 |

## What it says

- **Most "premature" stops are not premature in the sense the question cares about.** In 34 of 50 cases the answer is already supported by what the agent retrieved. The "missing" gold paragraph is usually a bridge or descriptor page (for example the page that says "Eagle Feather coached the Indians") that the question's wording repeats or that the answer does not need. Gold coverage is therefore a conservative proxy for sufficiency: the RQ1 precision figures are lower bounds.
- **Genuine failures are a minority: 9 of 50 (18%)** are distractor, bridge-missed, partial-answer or a wrong reading of an ambiguous question. Seven more are right for the wrong reason (parametric).
- **Many EM misses are formatting.** 'Poland' vs 'Polish state', 'June' vs 'mid-June', 'Season 3' vs 'season three'. F1 is the fairer metric here.
- **The clearest real failure patterns** are on MuSiQue: taking a career record for a single-season record (musique-16), and skipping the hop that says what Gates played up (musique-15).

## Check on the whole pool (automatic, not manual)

Share of all premature stops where the gold answer text already appears in the shown evidence (yes/no questions counted as answerable):

| model | HotpotQA | MuSiQue |
|---|---|---|
| gemini-3.8-flash | 64 of 84 (76%) | 79 of 104 (76%) |
| gemini-3.5-flash-lite | 84 of 139 (60%) | 94 of 187 (50%) |

For the strong model this is close to the manual 68% (34 of 50); the string match is more lenient. The small model makes genuinely more premature stops: a larger share of its stops lack the answer in the evidence.

## Caveats

- Single annotator, single model (`gemini-3.8-flash`), 50 of 188 cases, and the taxonomy was adapted after reading the cases (`answerable` was added because it dominated).
- "Answer in shown evidence" is a string match, so it undercounts paraphrases and counts coincidental mentions.

## Borderline calls

- hotpotqa-09 (parametric): the shown Costus osae paragraph calls Costus a family of its own, which arguably implies it is not in Apiaceae. Parametric is the safer tag.
- musique-09, musique-24 (parametric): the missing hop picks out which network is meant. In the descriptor cases (hotpotqa-10, 11, 12, 17, musique-02, 12) the entity is already fixed and the missing page only confirms a property, so they stay answerable.
- musique-17 (parametric): the shown text has two treaties ceding territory to the US (Paris 1783, Adams-Onis); only the unstated Minneapolis-Mississippi link picks Paris.
- hotpotqa-06 and hotpotqa-08 are both partial-answer: the evidence gives part of the location, not all of it.
- `cases.md` truncates each paragraph to about 350 characters. Seven tags depend on later text (hotpotqa-21, musique-09, 14, 19, 22, 24, 25); they were checked against the full paragraphs and held. The February 7, 2018 date for musique-09 and 24 is in the text; their parametric tag is the borderline part.
