"""Agreement between the LLM tagger and the human annotator on the error-analysis sample.

Usage: python scripts/agreement.py
Reads results/error_analysis/llm_tags.csv (column `cause`, the LLM's second-pass tags)
and results/error_analysis/human_tags.csv, and prints raw agreement, Cohen's kappa and
the cases where the two differ.
"""
import csv
from collections import Counter
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "results" / "error_analysis"


def load(name):
    with open(DIR / name, newline="") as f:
        return {r["case"]: r["cause"] for r in csv.DictReader(f)}


def cohen_kappa(a, b):
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    expected = sum(ca[k] * cb[k] for k in set(a) | set(b)) / n ** 2
    return observed, expected, (observed - expected) / (1 - expected)


def main():
    llm, human = load("llm_tags.csv"), load("human_tags.csv")
    if set(llm) != set(human):
        raise SystemExit(f"case lists differ: {sorted(set(llm) ^ set(human))}")
    cases = sorted(llm)
    a = [llm[c] for c in cases]
    b = [human[c] for c in cases]
    observed, expected, kappa = cohen_kappa(a, b)
    agree = sum(x == y for x, y in zip(a, b))
    print(f"cases: {len(cases)}")
    print(f"agreement: {agree} of {len(cases)} ({observed:.0%})")
    print(f"chance agreement: {expected:.3f}")
    print(f"Cohen's kappa: {kappa:.3f}")
    for c, x, y in zip(cases, a, b):
        if x != y:
            print(f"  {c}: LLM {x}, human {y}")


if __name__ == "__main__":
    main()
