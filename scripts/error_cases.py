"""Sample premature-stop cases for manual error analysis -> results/error_analysis/cases.md and tags.csv.
A premature stop = the self-judge rule's stop step (first SUFFICIENT verdict) where not all gold paragraphs are in context.
Usage: python scripts/error_cases.py [--model gemini-3.8-flash] [--per-dataset 25] [--seed 0]"""
import argparse
import csv
import json
import random
from pathlib import Path

from ess.evaluate import RULES, covered, load, score, stop_step

CAUSES = """- `answerable`: the evidence shown already supports the answer; the missing gold paragraph is a bridge or descriptor page that adds nothing (gold coverage is a conservative proxy)
- `parametric`: answer comes from the model's own memory, not from the evidence shown
- `bridge-missed`: the first-hop evidence is there but the second-hop (bridge) paragraph is missing and the model did not notice
- `distractor`: a retrieved non-gold paragraph was taken as the evidence
- `partial-answer`: part of the answer is supported, a required piece is not
- `ambiguous`: the question or gold answer is ambiguous or the gold label looks wrong
- `other`: write why in notes"""

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="gemini-3.8-flash")
ap.add_argument("--per-dataset", type=int, default=25)
ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()

out = ["# Premature-stop cases for manual tagging", "",
       f"Model `{a.model}`. Each case: the agent said SUFFICIENT while at least one gold paragraph was not yet retrieved. "
       "Read the evidence, decide why it stopped, and write one cause per case in `tags.csv`.", "", "Causes:", CAUSES, ""]
rows = []
for d in ("hotpotqa", "musique"):
    recs = load(f"runs/{d}_n500_seed0__{a.model}.jsonl")
    qs = {q["id"]: q for q in map(json.loads, open(f"raw/{d}_n500_seed0.jsonl"))}
    corpus = {p["pid"]: p for q in qs.values() for p in q["paragraphs"]}  # retrieval is over the pooled corpus
    pool = []
    for r in recs:
        t = stop_step(RULES["self-judge"], r)
        s = r["steps"][t - 1]
        if s["verdict"] == "SUFFICIENT" and not covered(r, s):
            pool.append((r, s))
    pool.sort(key=lambda x: x[0]["question_id"])
    pick = random.Random(a.seed).sample(pool, min(a.per_dataset, len(pool)))
    out += [f"## {d}: {len(pool)} premature stops of {len(recs)} questions, {len(pick)} sampled", ""]
    for n, (r, s) in enumerate(pick, 1):
        by_pid = corpus
        ctx = set(s["context_pids"])
        em, f = score(s["answer"], r)
        missing = [by_pid[p] for p in r["gold_pids"] if p not in ctx]
        case = f"{d}-{n:02d}"
        out += [f"### {case} `{r['question_id']}` (stopped at step {s['step']}, stated probability {s['probability']})", "",
                f"**Question:** {r['question']}", "",
                f"**Gold answer:** {r['gold_answer']}  |  **Model answer:** {s['answer']}  |  EM {em:.0f}, F1 {f:.2f}"
                f"{'  <- correct without all gold evidence' if em else ''}", "",
                f"**Gold paragraphs:** {len(r['gold_pids'])}, retrieved {len(r['gold_pids']) - len(missing)}", "", "**Evidence the agent had:**", ""]
        for i, pid in enumerate(s["context_pids"], 1):
            p = by_pid[pid]
            out.append(f"{i}. {'[GOLD] ' if pid in r['gold_pids'] else ''}**{p['title']}**: {p['text'][:350]}")
        out += ["", "**Gold paragraphs NOT retrieved:**", ""] + [f"- **{p['title']}**: {p['text'][:350]}" for p in missing] + [""]
        rows.append([case, d, r["question_id"], f"{em:.0f}", "", ""])
Path("results/error_analysis").mkdir(parents=True, exist_ok=True)
Path("results/error_analysis/cases.md").write_text("\n".join(out))
if not Path("results/error_analysis/tags.csv").exists():  # never overwrite finished tags
    with open("results/error_analysis/tags.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case", "dataset", "question_id", "answer_correct_em", "cause", "notes"])
        w.writerows(rows)
print(f"{len(rows)} cases -> results/error_analysis/cases.md, tags.csv")
