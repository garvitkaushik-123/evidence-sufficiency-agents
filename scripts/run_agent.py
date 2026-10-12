"""Run the agent over a sampled question file. Use --pilot N for the first N questions."""
import argparse
import sys
from pathlib import Path

from ess import data
from ess.agent import run_all
from ess.bm25 import BM25
from ess.check import check_log
from ess.llm import GeminiLLM

ap = argparse.ArgumentParser()
ap.add_argument("--questions", required=True, help="raw/<dataset>_n500_seed0.jsonl")
ap.add_argument("--model", required=True, help="exact model version string, e.g. a Gemini model id")
ap.add_argument("--pilot", type=int, default=None)
ap.add_argument("--T", type=int, default=5)
ap.add_argument("--k", type=int, default=3)
ap.add_argument("--retriever", choices=["bm25", "dense"], default="bm25")
ap.add_argument("--embed-model", default="gemini-embedding-2")
ap.add_argument("--out", default=None)
a = ap.parse_args()

qs = data.load_questions(a.questions)
corpus = data.build_corpus(qs)  # corpus is pooled from ALL sampled questions, even in pilot mode
if a.pilot:
    qs = qs[:a.pilot]
llm = GeminiLLM(a.model)
dense = a.retriever == "dense"
out = a.out or f"runs/{Path(a.questions).stem}__{a.model}{'__dense' if dense else ''}{'__pilot' if a.pilot else ''}.jsonl"
if dense:
    from ess.dense import DenseRetriever, GeminiEmbedder
    retriever = DenseRetriever(corpus, GeminiEmbedder(a.embed_model), cache=f"raw/emb/{Path(a.questions).stem.split('_n')[0]}__{a.embed_model}.npz")
    retriever_name = f"dense-{a.embed_model}"
else:
    retriever, retriever_name = BM25(corpus), "bm25"
Path(out).parent.mkdir(exist_ok=True)
run_all(qs, llm, retriever, out, T=a.T, k=a.k, run_id=Path(out).stem, retriever_name=retriever_name)
print("usage:", llm.usage)
n, problems = check_log(out, a.T)
print(f"{n} questions logged, {len(problems)} problems")
for p in problems[:20]:
    print(" ", p)
sys.exit(1 if problems else 0)
