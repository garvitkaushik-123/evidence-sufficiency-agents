# Evidence sufficiency in multi-step retrieval agents

When a retrieval agent says "I have enough evidence", how often is that true, does it predict a correct answer, and which stopping rule gives the best accuracy per retrieval step?

The agent always runs all 5 retrieval steps and logs a sufficiency verdict, a probability and its current answer at every step. Every stopping rule (fixed steps, self-judge, probability threshold, oracle) is then evaluated offline from those logs, so each question runs once per model.

"Sufficient" is defined objectively: all gold supporting paragraphs (from HotpotQA / MuSiQue annotations) are in the agent's context.

## Results (500 questions per dataset, two models)

Models: `gemini-3.5-flash-lite` (small) and `gemini-3.8-flash` (strong). All numbers are in `results/`; every comparison below has a paired bootstrap test in `results/paired_tests.md`.

- **Self-judging saves retrieval at about the same accuracy.** Stopping at the first SUFFICIENT verdict uses 1.6 to 1.8 of 5 steps on HotpotQA (65 to 67% fewer) and 2.9 to 3.3 on MuSiQue (34 to 41% fewer). Against always running 5 steps, answer F1 differs by -0.003 on MuSiQue (both models, not significant) and by -0.010 (not significant) to -0.025 (significant) on HotpotQA for the strong and small model.
- **The model matters far more than the stopping rule.** Strong minus small F1 is +0.07 to +0.26 for every rule on both datasets (all significant).
- **How often is "enough" true?** Against "all gold paragraphs retrieved" the verdict has precision 0.90 to 0.93 on HotpotQA and 0.65 to 0.78 on MuSiQue. Against "the gold answer text is in the retrieved evidence" (the ground-truth-in-context heuristic that Joren et al., ICLR 2025, found reasonable but imperfect against human labels) precision is 0.96 to 0.98 and 0.86 to 0.95. A manual read of 50 premature stops (`results/error_analysis/`) found about 7 in 10 already answerable from what was retrieved, so gold coverage understates the verdict's precision. The truth lies between the two labels.
- **Stated probabilities are close to binary**, so thresholds barely matter and calibration is poor (ECE 0.24 to 0.34). AUROC against answer exact match is 0.65 to 0.84 over all steps, but much of it is abstentions ("Not enough information" is wrong by construction and carries a low probability); on steps where the model commits to an answer it is 0.51 for the small model and 0.62 to 0.63 for the strong one. The small model says exactly 0 or 1 in 93 to 94% of judgements; the strong model in 61% (HotpotQA) and 25% (MuSiQue), but 91% and 75% of its probabilities lie within 0.1 of 0 or 1. Thresholds of 0.7 and 0.8 match self-judge to within 0.001 F1 in all four cases.
- **The pattern survives a dense retriever (small model only).** With `gemini-embedding-2` the gold paragraphs are in context at step 1 for 89% (HotpotQA) and 30% (MuSiQue) of questions, against 37% and 7% with BM25 (top-3, question as query). Accuracy rises (F1 at 5 steps 0.743 and 0.521 against 0.730 and 0.455) and self-judge saves more: 1.24 and 2.39 steps (75% and 52% fewer) at F1 0.768 and 0.522, which is not worse than 5 fixed steps (+0.025, significant, on HotpotQA; +0.000 on MuSiQue). The oracle still adds nothing, and on answered steps the stated probability is again no better than chance (AUROC 0.51). Details in `results/` (`results/retrieval_check.md` for retrieval alone).
- **More steps help on MuSiQue, not on HotpotQA.** 3 vs 5 fixed steps: no difference on HotpotQA, -0.04 F1 on MuSiQue. Even oracle stopping adds at most 0.02 F1 over self-judge.

Limits: two Gemini models (the dense retriever only with the small one), 500 questions per dataset, pooled corpus easier than open-domain search, the error analysis was tagged by an LLM and needs a human check. The logs in `runs/` are the full per-step records, so every number can be recomputed without an API key: `make setup data eval report` (the `data` step only downloads the public datasets; it is needed for the answer-in-context label).

## Reproduce

```
cp .env.example .env      # put your GEMINI_API_KEY in .env
make all                  # setup, download data, sample, run both datasets, evaluate
```

`make all` runs `gemini-3.8-flash` on 500 HotpotQA + 500 MuSiQue questions. Override with `make run eval MODEL=<exact-model-id>`.
Individual steps: `make setup`, `make data`, `make run`, `make eval`, `make dense` (dense-retriever robustness run, small model), `make report` (paired tests + figures into `results/`), `make test`. Runs are resumable: re-running skips questions already in the log.

**Cost and time (measured on `gemini-3.8-flash`, paid tier):** about 1,000 questions x 9 LLM calls, roughly $20 and 10+ hours sequentially. `gemini-3.5-flash-lite` costs a fraction of that. Thinking tokens are billed as output and dominate the bill. Do a pilot first: `python scripts/run_agent.py --questions raw/hotpotqa_n500_seed0.jsonl --model <id> --pilot 50` (also runs the exit check and prints token usage).

## Data

- HotpotQA distractor dev: HuggingFace `hotpotqa/hotpot_qa` parquet, converted to the original json format (7,405 questions, same as the official dev set; the official host was unreachable).
- MuSiQue-Ans dev: HuggingFace `dgslibisey/MuSiQue`.
- Sampled question IDs (seed 0, n=500 each) are committed in `data/ids/`. `make data` regenerates them and they match; full records go to `raw/` (gitignored).
- Each dataset's corpus is the pooled, deduplicated paragraphs of its 500 sampled questions (4,945 for HotpotQA, 7,017 for MuSiQue).

## Log format (`runs/*.jsonl`, one line per question)

Question-level: `run, model, retriever, question_id, dataset, question, gold_answer, aliases, gold_pids, T, k`.
Per step: `step, query, retrieved_pids, context_pids (cumulative), verdict, probability, answer, raw_judge, parse_ok`.
Gold coverage at step t = `gold_pids ⊆ context_pids`. The six full-run logs are committed (`runs/<dataset>_n500_seed0__<model>[__dense].jsonl`, about 8 MB); pilot logs and run stdout are not. They contain text from the public HotpotQA (CC BY-SA 4.0) and MuSiQue datasets; see their pages for licences.

## Evaluation (`scripts/evaluate.py`)

- RQ1: precision / recall / F1 of the SUFFICIENT verdict over all (question, step) pairs, against two labels: all gold paragraphs in context, and the gold answer text in context (yes/no questions skipped); premature stops (says sufficient, is not) and over-retrieval (says insufficient, already is).
- RQ2: AUROC and expected calibration error of the stated probability against answer exact-match.
- RQ3: average steps, EM and F1 (bootstrap 95% CI) for fixed-1/3/5, self-judge, thresholds 0.5 to 0.95, and oracle. Oracle runs to step 5 when gold is never covered.

`make report` writes `results/paired_tests.md` (paired bootstrap, 95% CI on F1 differences between rules and between models), `results/rule_tables.md` (the numbers behind the figures) and `results/figures/` (accuracy vs retrieval steps, reliability diagram).

## Design choices and limitations

- Each step excludes already-retrieved paragraphs, so every step adds new evidence (k=3 gives 15 distinct paragraphs by step 5). Gold is never fully covered within 5 steps for a sizeable share of MuSiQue questions (BM25 limit).
- Step 1 searches with the raw question; steps 2+ use an LLM-written query from the question plus the evidence so far. An empty query reply falls back to the question.
- The sufficiency judge sees only the question and the evidence. Prompts live in `src/ess/agent.py`.
- Decoding is temperature 0. Thinking models still think, so reruns are not guaranteed bit-identical; the logs are the source of truth.
- The pooled corpus is easier than open-domain retrieval, and gold-paragraph coverage is a proxy for sufficiency. HotpotQA gold is matched by title, so a distractor sharing a gold title would count as gold.
- Stated probabilities cluster at 0 and 1 (see Results), so threshold rules barely differ from self-judge.
- Token usage counts thinking tokens only from commit "Count thinking tokens in usage" onward; earlier `usage:` lines undercount output.
- Model IDs are pinned in the run file names. Preview and "latest" aliases were avoided where possible, and some older IDs (e.g. `gemini-2.5-*`) are closed to new API users.

The report: [docs/report.pdf](docs/report.pdf) (source `docs/report.md`, rebuild with `sh docs/build_report.sh`, needs pandoc and Chrome). Related work notes and comparison table: `docs/related_work.md`; references: `refs.bib`.

This is a technical report project, not a publication.
