"""Retrieval-only comparison of BM25 and the dense retriever (no LLM): share of questions whose gold paragraphs are all in
the top-k when searching with the raw question, and mean share of gold paragraphs found. Builds the embedding cache.
Writes results/retrieval_check.md."""
import sys
from pathlib import Path

from ess import data
from ess.bm25 import BM25
from ess.dense import DenseRetriever, GeminiEmbedder

EMBED = sys.argv[1] if len(sys.argv) > 1 else "gemini-embedding-2"
KS = (3, 5, 10, 15)
out = ["# Retrieval check: BM25 vs dense", "", f"Dense = `{EMBED}`, 768 dimensions, cosine. Query = the raw question, ranking over the pooled corpus of the 500 sampled questions.",
       "", "| dataset | retriever | k | all gold in top-k | mean share of gold in top-k |", "|---|---|---|---|---|"]
embedder = GeminiEmbedder(EMBED)
for d in ("hotpotqa", "musique"):
    qs = data.load_questions(f"raw/{d}_n500_seed0.jsonl")
    corpus = data.build_corpus(qs)
    for name, ret in (("bm25", BM25(corpus)), ("dense", DenseRetriever(corpus, embedder, cache=f"raw/emb/{d}__{EMBED}.npz"))):
        hits = {k: [] for k in KS}
        for q in qs:
            top = [p["pid"] for p in ret.search(q["question"], k=max(KS))]
            for k in KS:
                found = set(q["gold_pids"]) & set(top[:k])
                hits[k].append((len(found) == len(q["gold_pids"]), len(found) / len(q["gold_pids"])))
        for k in KS:
            n = len(qs)
            out.append(f"| {d} | {name} | {k} | {sum(a for a, _ in hits[k]) / n:.3f} | {sum(b for _, b in hits[k]) / n:.3f} |")
        print(d, name, {k: round(sum(a for a, _ in hits[k]) / len(qs), 3) for k in KS}, flush=True)
Path("results/retrieval_check.md").write_text("\n".join(out) + "\n")
