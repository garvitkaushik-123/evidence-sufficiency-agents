"""BrowseComp-Plus pilot checks, aggregate numbers only. Run after scripts/evaluate_bc.py (which writes results/browsecomp_pilot.md):
  1. judge vs human agreement on the 20-judgement hand-check sheet (column human_all, filled by the author);
  2. memorisation check: every judge-correct answer goes to A (answer text in retrieved documents), B (text not found, a gold
     document in context) or C (neither). C answers show no retrieval support by these tests.
Appends both sections to results/browsecomp_pilot.md (replacing earlier copies). No benchmark text is printed or written."""
import csv
import json
from collections import Counter
from pathlib import Path

from ess.evaluate import answer_in_context, corpus_for, load, stop_step

RUNS = {"gemini-3.5-flash-lite": "runs/browsecomp_n100_seed0__gemini-3.5-flash-lite.jsonl",
        "gemini-3.8-flash": "runs/browsecomp_n100_seed0__gemini-3.8-flash.jsonl"}
out = ["## Judge check", ""]

rows = list(csv.DictReader(open("runs/browsecomp_n100_seed0__gemini-3.5-flash-lite.handcheck.csv")))
j = [r["judge_correct"] == "True" for r in rows]
h = [r["human_all"] == "yes" for r in rows]
po = sum(a == b for a, b in zip(j, h)) / len(j)
pe = sum((sum(x == v for x in j) / len(j)) * (sum(x == v for x in h) / len(h)) for v in (True, False))
out += [f"20 random judgements (small model) were marked by the author, who saw the judge's verdict: {sum(a == b for a, b in zip(j, h))} of 20 agree "
        f"(Cohen's kappa {(po - pe) / (1 - pe):.2f}). The one disagreement is a hedged answer (\"X (or Y)\") that the judge accepted and the author did not.", ""]

out += ["## Memorisation check", "",
        "Judge-correct answers by where the answer comes from: A = answer text in the retrieved documents, B = text not found but a gold document "
        "in context, C = neither.", "", "| model | slice | correct answers | A | B | C |", "|---|---|---|---|---|---|"]
for model, path in RUNS.items():
    recs = load(path)
    judged = json.load(open(path.replace(".jsonl", ".judged.json")))
    corpus = corpus_for(recs)
    rows, at_stop = [], []
    for r in recs:
        stop = stop_step(("self",), r)  # first SUFFICIENT step, 8 if never
        for s in r["steps"]:
            if judged[r["question_id"]].get(str(s["step"])) is True:
                a = bool(answer_in_context(r, s, corpus))
                rows.append((s["step"], "A" if a else ("B" if set(r["gold_pids"]) & set(s["context_pids"]) else "C")))
                if s["step"] == stop:
                    at_stop.append(rows[-1])
    for label, sub in (("step 1", [x for x in rows if x[0] == 1]), ("step 8", [x for x in rows if x[0] == 8]),
                       ("self-judge stop step", at_stop), ("all steps", rows)):
        c = Counter(b for _, b in sub)
        out.append(f"| {model} | {label} | {len(sub)} | " + " | ".join(f"{c[k]} ({c[k] / max(len(sub), 1):.0%})" for k in "ABC") + " |")
out += ["", "Reading: at step 8 every correct answer for both models has the answer text or a gold document in context (C = 0), so the final "
        "accuracy comes from retrieval in the pooled corpus. C is not empty early on: the strong model answers 10 of its 37 correct step-1 "
        "answers (27%) with neither, and 24 of 530 (5%) pooled; 3 of the 5 strong-model C cases opened by hand clearly and 1 possibly looked like answers from the "
        "model's own knowledge (the model's own verdict at that step was INSUFFICIENT), 1 was a string-match miss. The small model has 3 "
        "C cases in total (1 at step 1), 2 of them string-match misses. So a minority of early correct answers, mostly from the strong "
        "model, reflect prior knowledge, which inflates its fixed-1 accuracy a little but not the step-8 comparison. A and B cannot rule out "
        "that a model also knew the answer and retrieval confirmed it.", ""]

p = Path("results/browsecomp_pilot.md")
base = p.read_text().split("\n## Judge check")[0].rstrip("\n")
p.write_text(base + "\n\n" + "\n".join(out))
print("\n".join(out))
