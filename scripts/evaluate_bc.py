"""BrowseComp-Plus pilot evaluation (T=8) from run logs plus judged verdicts (scripts/judge.py).
Same rules and metric names as the report; correctness is the LLM-judged verdict, exact match shown for continuity.
Prints markdown; writes aggregate numbers only (no benchmark text) to results/browsecomp_pilot.md.
Usage: python scripts/evaluate_bc.py runs/browsecomp_n100_seed0__<model>.jsonl ..."""
import json
import random
import re
import sys
from pathlib import Path

from ess.evaluate import (answer_in_context, auroc, corpus_for, covered, covered_strict, ece, is_abstention, load,
                          rq1, score, stop_step)

RULES = {"fixed-1": ("fixed", 1), "fixed-4": ("fixed", 4), "fixed-8": ("fixed", 8), "self-judge": ("self",),
         "tau-0.8": ("tau", 0.8), "oracle (gold covered)": ("oracle",)}
HEDGE = re.compile(r"\bor\b|\bperhaps\b|\bpossibly\b|\bprobably\b|\blikely\b|\bmight\b|\bwait\b", re.I)  # ponytail: crude hedge detector


def boot_ci(xs, n_boot=2000, seed=0):
    rng = random.Random(seed)
    b = sorted(sum(xs[rng.randrange(len(xs))] for _ in xs) / len(xs) for _ in range(n_boot))
    return b[int(.025 * n_boot)], b[int(.975 * n_boot)]


def fmt(v):
    return f"{v:.3f}" if isinstance(v, float) else str(v)


def evaluate(path):
    recs = load(path)
    judged = json.loads(Path(path).with_suffix(".judged.json").read_text())
    corr = lambda r, t: bool(judged[r["question_id"]][str(t)])  # None (unparsed) counts as incorrect
    model = recs[0]["model"]
    out = [f"### {model} ({len(recs)} questions, T={recs[0]['T']}, k={recs[0]['k']}, {recs[0]['retriever']})", ""]

    per = {}
    for name, rule in RULES.items():
        per[name] = [(stop_step(rule, r), corr(r, stop_step(rule, r)), score(r["steps"][stop_step(rule, r) - 1]["answer"], r)[0])
                     for r in recs]
    out += ["| rule | avg steps | judged accuracy (95% CI) | exact match | vs fixed-8 (accuracy, 95% CI; steps) |", "|---|---|---|---|---|"]
    base = per["fixed-8"]
    for name, rows in per.items():
        acc = [float(x[1]) for x in rows]
        lo, hi = boot_ci(acc)
        d = [float(a[1]) - float(b[1]) for a, b in zip(rows, base)]
        dlo, dhi = boot_ci(d)
        vs = "baseline" if name == "fixed-8" else f"{sum(d)/len(d):+.3f} [{dlo:+.3f}, {dhi:+.3f}]; {sum(a[0]-b[0] for a, b in zip(rows, base))/len(rows):+.2f} steps"
        out.append(f"| {name} | {sum(x[0] for x in rows)/len(rows):.2f} | {sum(acc)/len(acc):.3f} [{lo:.3f}, {hi:.3f}] | "
                   f"{sum(x[2] for x in rows)/len(rows):.3f} | {vs} |")

    out += ["", "RQ1: verdict SUFFICIENT against each sufficiency label, over all (question, step) pairs", "",
            "| label | precision | recall | premature stops | over-retrieval | n |", "|---|---|---|---|---|---|"]
    labels = {"gold coverage": covered, "strict (all evidence)": covered_strict}
    corpus = corpus_for(recs)
    if corpus:
        labels["answer in context"] = lambda r, s: answer_in_context(r, s, corpus)
    for name, lab in labels.items():
        m = rq1(recs, lab)
        out.append(f"| {name} | {m['precision']:.3f} | {m['recall']:.3f} | {m['premature']} | {m['over_retrieval']} | {m['n']} |")

    rows = [(s["probability"], float(corr(r, s["step"])), is_abstention(s["answer"]))
            for r in recs for s in r["steps"] if s["probability"] is not None]
    kept = [(p, y) for p, y, ab in rows if not ab]
    out += ["", f"RQ2 (stated probability vs judged correctness): AUROC {fmt(auroc([p for p,_,_ in rows],[y for _,y,_ in rows]))}, "
            f"AUROC on answered steps {fmt(auroc([p for p,_ in kept],[y for _,y in kept]))}, "
            f"ECE {fmt(ece([p for p,_,_ in rows],[y for _,y,_ in rows]))}, n={len(rows)} ({len(rows)-len(kept)} abstention-like answers)."]

    first = [next((s["step"] for s in r["steps"] if s["verdict"] == "SUFFICIENT"), None) for r in recs]
    never = sum(f is None for f in first)
    out += [f"Self-judge: SUFFICIENT at step 1 for {sum(f == 1 for f in first)} questions, never SUFFICIENT for {never}; "
            f"verdict SUFFICIENT in {sum(s['verdict'] == 'SUFFICIENT' for r in recs for s in r['steps'])} of {sum(len(r['steps']) for r in recs)} steps."]

    hedged = [r for r in recs if corr(r, 8) and HEDGE.search(r["steps"][7]["answer"])]
    out += [f"Hedged answers: {len(hedged)} of the {sum(corr(r, 8) for r in recs)} judged-correct fixed-8 answers contain a hedge word; "
            f"accuracy without them {(sum(corr(r, 8) for r in recs) - len(hedged))/len(recs):.3f}.", ""]
    return "\n".join(out)


text = "# BrowseComp-Plus pilot (100 questions, pooled corpus, T=8, k=3)\n\nLLM-judged accuracy (BrowseComp-Plus grader prompt, judge gemini-3.8-flash). Aggregates only.\n\n" + \
       "\n".join(evaluate(p) for p in sys.argv[1:])
print(text)
Path("results/browsecomp_pilot.md").write_text(text + "\n")
