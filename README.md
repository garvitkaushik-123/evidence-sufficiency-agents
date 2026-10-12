# Evidence sufficiency in multi-step retrieval agents

When a retrieval agent says "I have enough evidence", how often is that true, does it predict a correct answer, and which stopping rule gives the best accuracy per retrieval step?

The agent always runs all 5 retrieval steps and logs a sufficiency verdict, a probability and its current answer at every step. Every stopping rule (fixed steps, self-judge, probability threshold, oracle) is then evaluated offline from those logs, so each question runs once per model.

"Sufficient" is defined objectively: all gold supporting paragraphs (from HotpotQA / MuSiQue annotations) are in the agent's context.

## Reproduce

```
cp .env.example .env      # put your GEMINI_API_KEY in .env
make all                  # setup, download data, sample, run both datasets, evaluate
```

`make all` runs `gemini-3.8-flash` on 500 HotpotQA + 500 MuSiQue questions. Override with `make run eval MODEL=<exact-model-id>`.
Individual steps: `make setup`, `make data`, `make run`, `make eval`, `make report` (paired tests + figures into `results/`), `make test`. Runs are resumable: re-running skips questions already in the log.

**Cost and time (measured on `gemini-3.8-flash`, paid tier):** about 1,000 questions x 9 LLM calls, roughly $20 and 10+ hours sequentially. `gemini-3.5-flash-lite` costs a fraction of that. Thinking tokens are billed as output and dominate the bill. Do a pilot first: `python scripts/run_agent.py --questions raw/hotpotqa_n500_seed0.jsonl --model <id> --pilot 50` (also runs the exit check and prints token usage).

## Data

- HotpotQA distractor dev: HuggingFace `hotpotqa/hotpot_qa` parquet, converted to the original json format (7,405 questions, same as the official dev set; the official host was unreachable).
- MuSiQue-Ans dev: HuggingFace `dgslibisey/MuSiQue`.
- Sampled question IDs (seed 0, n=500 each) are committed in `data/ids/`. `make data` regenerates them and they match; full records go to `raw/` (gitignored).
- Each dataset's corpus is the pooled, deduplicated paragraphs of its 500 sampled questions (4,945 for HotpotQA, 7,017 for MuSiQue).

## Log format (`runs/*.jsonl`, one line per question)

Question-level: `run, model, retriever, question_id, dataset, question, gold_answer, aliases, gold_pids, T, k`.
Per step: `step, query, retrieved_pids, context_pids (cumulative), verdict, probability, answer, raw_judge, parse_ok`.
Gold coverage at step t = `gold_pids ⊆ context_pids`.

## Evaluation (`scripts/evaluate.py`)

- RQ1: precision / recall / F1 of the SUFFICIENT verdict vs gold coverage over all (question, step) pairs; premature stops (says sufficient, is not) and over-retrieval (says insufficient, already is).
- RQ2: AUROC and expected calibration error of the stated probability against answer exact-match.
- RQ3: average steps, EM and F1 (bootstrap 95% CI) for fixed-1/3/5, self-judge, thresholds 0.5 to 0.95, and oracle. Oracle runs to step 5 when gold is never covered.

`make report` writes `results/paired_tests.md` (paired bootstrap, 95% CI on F1 differences between rules and between models), `results/rule_tables.md` (the numbers behind the figures) and `results/figures/` (accuracy vs retrieval steps, reliability diagram).

## Design choices and limitations

- Each step excludes already-retrieved paragraphs, so every step adds new evidence (k=3 gives 15 distinct paragraphs by step 5). Gold is never fully covered within 5 steps for a sizeable share of MuSiQue questions (BM25 limit).
- Step 1 searches with the raw question; steps 2+ use an LLM-written query from the question plus the evidence so far. An empty query reply falls back to the question.
- The sufficiency judge sees only the question and the evidence. Prompts live in `src/ess/agent.py`.
- Decoding is temperature 0. Thinking models still think, so reruns are not guaranteed bit-identical; the logs are the source of truth.
- The pooled corpus is easier than open-domain retrieval, and gold-paragraph coverage is a proxy for sufficiency. HotpotQA gold is matched by title, so a distractor sharing a gold title would count as gold.
- Stated probabilities are nearly always 0 or 1, so threshold rules coincide.
- Token usage counts thinking tokens only from commit "Count thinking tokens in usage" onward; earlier `usage:` lines undercount output.
- Model IDs are pinned in the run file names. Preview and "latest" aliases were avoided where possible, and some older IDs (e.g. `gemini-2.5-*`) are closed to new API users.

This is a technical report project, not a publication.
