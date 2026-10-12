"""Figures and the table view of their data -> results/figures/*.png, results/rule_tables.md.
Colors: categorical slots 1-2 of the reference palette (blue, orange), checked with the dataviz validate_palette script."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from ess.evaluate import RULES, answer_in_context, corpus_for, load, per_question, rq1, rq2, rule_table, score

MODELS = {"gemini-3.5-flash-lite": "#2a78d6", "gemini-3.8-flash": "#eb6834"}
DATASETS = {"hotpotqa": "HotpotQA", "musique": "MuSiQue"}
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
                     "text.color": INK, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.edgecolor": GRID, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
                     "font.size": 10})
runs = {(d, m): load(f"runs/{d}_n500_seed0__{m}.jsonl") for d in DATASETS for m in MODELS}


def accuracy_vs_steps():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=False)
    for ax, (d, dname) in zip(axes, DATASETS.items()):
        for m, col in MODELS.items():
            recs, tab = runs[d, m], rule_table(runs[d, m])
            ks = range(1, 6)
            f1s = [sum(f for _, f in per_question(recs, ("fixed", k)).values()) / len(recs) for k in ks]
            ax.plot(ks, f1s, color=col, lw=2, marker="o", ms=5, mec=SURFACE, mew=1.5, zorder=2)
            st, _, f, (lo, hi) = tab["self-judge"]
            ax.errorbar(st, f, yerr=[[f - lo], [hi - f]], fmt="o", color=col, ms=10, mec=SURFACE, mew=2,
                        elinewidth=1.5, capsize=3, zorder=3)
            st, _, f, _ = tab["oracle"]
            ax.plot(st, f, "D", ms=8, mfc=SURFACE, mec=col, mew=2, zorder=3)
            ax.annotate(m.replace("gemini-", ""), (5, f1s[-1]), xytext=(6, 0), textcoords="offset points", color=INK, va="center", fontsize=9)
        ax.set_title(dname, loc="left", color=INK, fontsize=11, fontweight="bold")
        ax.set_xlabel("average retrieval steps used"); ax.set_xticks(range(1, 6)); ax.set_xlim(0.8, 6.2)
        ax.set_ylabel("answer F1")
    handles = [Line2D([], [], color=c, lw=2, label=m) for m, c in MODELS.items()] + [
        Line2D([], [], color=INK2, lw=2, marker="o", ms=5, label="fixed-k (k = 1..5)"),
        Line2D([], [], color=INK2, lw=0, marker="o", ms=9, label="self-judge (stop at first SUFFICIENT)"),
        Line2D([], [], color=INK2, lw=0, marker="D", ms=7, mfc=SURFACE, mew=2, label="oracle (stop when gold is in context)")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=9)
    fig.suptitle("Accuracy against retrieval cost (self-judge error bars: bootstrap 95% CI)", x=0.01, ha="left", color=INK, fontsize=12)
    fig.tight_layout(rect=(0, 0.13, 1, 0.95))
    fig.savefig("results/figures/accuracy_vs_steps.png", dpi=200); plt.close(fig)


def reliability_pairs(recs, bins=10, min_n=10):
    pairs = [(s["probability"], score(s["answer"], r)[0]) for r in recs for s in r["steps"] if s["probability"] is not None]
    out = []
    for b in range(bins):
        sel = [(p, y) for p, y in pairs if min(int(p * bins), bins - 1) == b]
        if len(sel) >= min_n:  # tiny bins are noise
            out.append((sum(p for p, _ in sel) / len(sel), sum(y for _, y in sel) / len(sel), len(sel)))
    return out


def reliability():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4))
    for ax, (d, dname) in zip(axes, DATASETS.items()):
        ax.plot([0, 1], [0, 1], color=INK2, lw=1, ls="--", zorder=1)
        for m, col in MODELS.items():
            pts = reliability_pairs(runs[d, m])
            ax.plot([p for p, _, _ in pts], [a for _, a, _ in pts], color=col, lw=1.5, zorder=2)
            ax.scatter([p for p, _, _ in pts], [a for _, a, _ in pts], s=[max(n, 5) ** 0.5 * 9 for _, _, n in pts],
                       color=col, edgecolors=SURFACE, linewidths=2, zorder=3)
            r = rq2(runs[d, m])
            ax.text(0.03, 0.93 - 0.07 * list(MODELS).index(m), f"{m.replace('gemini-', '')}: ECE {r['ece']:.2f}, AUROC {r['auroc']:.2f}",
                    transform=ax.transAxes, color=INK, fontsize=9)
        ax.set_xlim(-0.04, 1.04); ax.set_ylim(-0.04, 1.04)
        ax.set_title(dname, loc="left", color=INK, fontsize=11, fontweight="bold")
        ax.set_xlabel("stated probability that the evidence is sufficient"); ax.set_ylabel("answer exact match")
    handles = [Line2D([], [], color=c, lw=2, marker="o", ms=7, label=m) for m, c in MODELS.items()] + [
        Line2D([], [], color=INK2, lw=1, ls="--", label="perfect calibration")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=9)
    fig.suptitle("Stated probability vs observed correctness (marker area ~ number of judgments; bins under 10 hidden)", x=0.01, ha="left", color=INK, fontsize=12)
    fig.tight_layout(rect=(0, 0.08, 1, 0.95))
    fig.savefig("results/figures/reliability.png", dpi=200); plt.close(fig)


def tables():
    out = ["# Rule tables (data behind the figures)", ""]
    for d, dname in DATASETS.items():
        for m in MODELS:
            out += [f"## {dname}, {m}", "", "| rule | avg steps | EM | F1 | F1 95% CI |", "|---|---|---|---|---|"]
            for name, (st, em, f, ci) in rule_table(runs[d, m]).items():
                out.append(f"| {name} | {st:.2f} | {em:.3f} | {f:.3f} | [{ci[0]:.3f}, {ci[1]:.3f}] |")
            out.append("")
    if corpus_for(runs["hotpotqa", next(iter(MODELS))]):
        out += ["# RQ1 under two sufficiency labels", "",
                "Verdict SUFFICIENT vs (a) all gold paragraphs in context, (b) gold answer text in context (yes/no questions skipped).",
                "", "| dataset | model | label | precision | recall | F1 | premature | over-retrieval | pairs |", "|---|---|---|---|---|---|---|---|---|"]
        for d, dname in DATASETS.items():
            for m in MODELS:
                corpus = corpus_for(runs[d, m])
                for name, label in (("gold coverage", None), ("answer in context", lambda r, s: answer_in_context(r, s, corpus))):
                    x = rq1(runs[d, m]) if label is None else rq1(runs[d, m], label)
                    out.append(f"| {dname} | {m} | {name} | {x['precision']:.3f} | {x['recall']:.3f} | {x['f1']:.3f} | {x['premature']} | {x['over_retrieval']} | {x['n']} |")
    out += ["# RQ2: stated probability vs answer correctness", "",
            "AUROC of the stated probability for answer exact match, over all steps, and over steps where the answer is not an abstention "
            "(for example 'Not enough information', matched by a keyword list, so approximate). Abstentions are wrong by construction.",
            "", "| dataset | model | AUROC all steps | AUROC answered steps | ECE | steps | abstention-like answers |", "|---|---|---|---|---|---|---|"]
    for d, dname in DATASETS.items():
        for m in MODELS:
            x = rq2(runs[d, m])
            out.append(f"| {dname} | {m} | {x['auroc']:.3f} | {x['auroc_answered']:.3f} | {x['ece']:.3f} | {x['n']} | {x['abstained']} |")
    out.append("")
    Path("results/rule_tables.md").write_text("\n".join(out))


Path("results/figures").mkdir(parents=True, exist_ok=True)
accuracy_vs_steps(); reliability(); tables()
print("wrote results/figures/accuracy_vs_steps.png, reliability.png, results/rule_tables.md")
