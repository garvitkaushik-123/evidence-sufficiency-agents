"""Paired bootstrap tests (95% CI on the F1 difference, same questions in both arms) -> results/paired_tests.md.
Usage: python scripts/compare.py   (reads runs/<dataset>_n500_seed0__<model>.jsonl for the models below)"""
from pathlib import Path

from ess.evaluate import RULES, load, paired_diff, per_question

MODELS = ["gemini-3.5-flash-lite", "gemini-3.8-flash"]
DATASETS = ["hotpotqa", "musique"]
RULE_PAIRS = [("self-judge", "fixed-5"), ("self-judge", "fixed-3"), ("oracle", "self-judge"), ("fixed-3", "fixed-5")]


def row(label, a, b):
    d, (lo, hi), ds = paired_diff(a, b)
    return f"| {label} | {d:+.3f} | [{lo:+.3f}, {hi:+.3f}] | {'yes' if lo > 0 or hi < 0 else 'no'} | {ds:+.2f} |"


head = "| comparison (A - B) | F1 diff | 95% CI | CI excludes 0 | steps diff |\n|---|---|---|---|---|"
out = ["# Paired bootstrap tests", "", "F1 difference A - B over the same 500 questions (2,000 resamples of questions). "
       "Compare rules within a model, then models within a rule.", ""]
runs = {(d, m): load(f"runs/{d}_n500_seed0__{m}.jsonl") for d in DATASETS for m in MODELS}
for d in DATASETS:
    for m in MODELS:
        out += [f"## {d}, {m}: rule vs rule", "", head]
        for ra, rb in RULE_PAIRS:
            out.append(row(f"{ra} - {rb}", per_question(runs[d, m], RULES[ra]), per_question(runs[d, m], RULES[rb])))
        out.append("")
    out += [f"## {d}: {MODELS[1]} - {MODELS[0]}, same rule", "", head]
    for rule in ("fixed-1", "fixed-3", "fixed-5", "self-judge", "oracle"):
        out.append(row(rule, per_question(runs[d, MODELS[1]], RULES[rule]), per_question(runs[d, MODELS[0]], RULES[rule])))
    out.append("")
Path("results").mkdir(exist_ok=True)
Path("results/paired_tests.md").write_text("\n".join(out))
print("\n".join(out))
