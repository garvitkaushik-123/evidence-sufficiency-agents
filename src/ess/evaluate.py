"""Offline evaluation of stopping rules from run logs (one JSONL per model x dataset).

A rule maps a question's 5 logged steps to a stop step (1..T); its answer is the logged answer at that step.
Oracle = first step whose context covers all gold paragraphs, else T (never-covered questions run to the end).
"""
import json
import random
import re
import string
from collections import Counter


def norm(s):
    s = "".join(c for c in (s or "").lower() if c not in string.punctuation)
    return " ".join(re.sub(r"\b(a|an|the)\b", " ", s).split())


def f1(pred, gold):
    p, g = norm(pred).split(), norm(gold).split()
    common = sum((Counter(p) & Counter(g)).values())
    if not common:
        return 0.0
    pr, rc = common / len(p), common / len(g)
    return 2 * pr * rc / (pr + rc)


def score(pred, r):
    golds = [r["gold_answer"], *r["aliases"]]
    return (float(any(norm(pred) == norm(g) for g in golds)), max(f1(pred, g) for g in golds))


def load(path):
    return [json.loads(l) for l in open(path) if l.strip()]


def covered(r, s):
    return set(r["gold_pids"]) <= set(s["context_pids"])


def stop_step(rule, r):
    T = len(r["steps"])
    if rule[0] == "fixed":
        return min(rule[1], T)
    for s in r["steps"]:
        if (rule[0] == "self" and s["verdict"] == "SUFFICIENT") or \
           (rule[0] == "tau" and (s["probability"] or 0) >= rule[1]) or \
           (rule[0] == "oracle" and covered(r, s)):
            return s["step"]
    return T


RULES = {"fixed-1": ("fixed", 1), "fixed-3": ("fixed", 3), "fixed-5": ("fixed", 5), "self-judge": ("self",),
         **{f"tau-{t}": ("tau", t) for t in (0.5, 0.7, 0.8, 0.9, 0.95)}, "oracle": ("oracle",)}


def rule_table(recs, n_boot=1000, seed=0):
    """name -> (mean steps, mean EM, mean F1, F1 95% bootstrap CI)."""
    out = {}
    for name, rule in RULES.items():
        rows = []
        for r in recs:
            t = stop_step(rule, r)
            em, f = score(r["steps"][t - 1]["answer"], r)
            rows.append((t, em, f))
        rng = random.Random(seed)
        boots = sorted(sum(rows[rng.randrange(len(rows))][2] for _ in rows) / len(rows) for _ in range(n_boot))
        n = len(rows)
        out[name] = (sum(x[0] for x in rows) / n, sum(x[1] for x in rows) / n, sum(x[2] for x in rows) / n,
                     (boots[int(.025 * n_boot)], boots[int(.975 * n_boot)]))
    return out


def rq1(recs):
    """Verdict SUFFICIENT vs gold coverage over all (question, step) pairs."""
    tp = fp = fn = tn = 0
    for r in recs:
        for s in r["steps"]:
            say, gold = s["verdict"] == "SUFFICIENT", covered(r, s)
            tp += say and gold
            fp += say and not gold   # premature stop
            fn += (not say) and gold  # over-retrieval
            tn += (not say) and not gold
    p, rc = tp / max(tp + fp, 1), tp / max(tp + fn, 1)
    return {"precision": p, "recall": rc, "f1": 2 * p * rc / max(p + rc, 1e-9),
            "premature": fp, "over_retrieval": fn, "n": tp + fp + fn + tn}


def auroc(probs, labels):
    pos = [p for p, y in zip(probs, labels) if y]
    neg = [p for p, y in zip(probs, labels) if not y]
    if not pos or not neg:
        return None
    return sum((a > b) + .5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))


def ece(probs, labels, bins=10):
    tot = 0.0
    for b in range(bins):
        idx = [i for i, p in enumerate(probs) if min(int(p * bins), bins - 1) == b]
        if idx:
            tot += len(idx) * abs(sum(probs[i] for i in idx) / len(idx) - sum(labels[i] for i in idx) / len(idx))
    return tot / len(probs)


def rq2(recs):
    """Stated sufficiency probability vs answer exact-match, over all steps with a parsed probability."""
    pairs = [(s["probability"], score(s["answer"], r)[0]) for r in recs for s in r["steps"] if s["probability"] is not None]
    probs, labels = [p for p, _ in pairs], [y for _, y in pairs]
    return {"auroc": auroc(probs, labels), "ece": ece(probs, labels), "n": len(pairs)}


def report(path):
    recs = load(path)
    print(f"== {path} ({len(recs)} questions)")
    print("RQ1", {k: round(v, 3) if isinstance(v, float) else v for k, v in rq1(recs).items()})
    print("RQ2", {k: round(v, 3) if isinstance(v, float) else v for k, v in rq2(recs).items()})
    print(f"{'rule':<11}{'steps':>6}{'EM':>7}{'F1':>7}  F1 95% CI")
    for name, (st, em, f, ci) in rule_table(recs).items():
        print(f"{name:<11}{st:>6.2f}{em:>7.3f}{f:>7.3f}  [{ci[0]:.3f}, {ci[1]:.3f}]")
