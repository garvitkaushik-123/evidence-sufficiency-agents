# Evidence sufficiency in multi-step retrieval agents

Week 1 pipeline: sample questions, pool a corpus, BM25 retrieval, 5-step agent loop with full per-step logging.
Every stopping rule is evaluated offline from the logs, so each question runs once per model.

## Run

```
pip install -e ".[gemini,dev]"
export GEMINI_API_KEY=...
# 1. data: hotpot_dev_distractor_v1.json (HotpotQA) and musique_ans_v1.0_dev.jsonl (MuSiQue-Ans)
python scripts/sample.py --hotpot <path> --musique <path> --n 500 --seed 0
# 2. pilot on 50 questions (also runs the exit check and prints token usage)
python scripts/run_agent.py --questions raw/hotpotqa_n500_seed0.jsonl --model <exact-model-id> --pilot 50
pytest
```

Sampled question IDs are committed in `data/ids/`; full records go to `raw/` (gitignored).

## Log format (`runs/*.jsonl`, one line per question)

Question-level: `run, model, retriever, question_id, dataset, question, gold_answer, aliases, gold_pids, T, k`.
Per step: `step, query, retrieved_pids, context_pids (cumulative), verdict, probability, answer, raw_judge, parse_ok`.
Gold coverage at step t = `gold_pids ⊆ context_pids`.

## Design choices to know about
- Each step excludes already-retrieved paragraphs, so every step adds new evidence (k=3 → 15 distinct paragraphs by step 5).
- The corpus is pooled from all 500 sampled questions even in `--pilot` mode, so pilot retrieval difficulty matches the full run.
- Step 1 searches with the raw question; steps 2+ use an LLM-written query from the question plus evidence so far.
- Decoding is temperature 0. Prompts live in `src/ess/agent.py`; the sufficiency judge sees only the question and the evidence.
