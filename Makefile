MODEL ?= gemini-3.8-flash
N ?= 500
PY = .venv/bin/python
-include .env
export

DENSE_MODEL ?= gemini-3.5-flash-lite

.PHONY: all setup data run dense eval report test

all: setup data run eval

setup:
	python3 -m venv .venv
	.venv/bin/pip install -q -e ".[gemini,data,plots,dense,dev]"

data:
	$(PY) scripts/download.py
	$(PY) scripts/sample.py --hotpot raw/dl/hotpot/hotpot_dev_distractor_v1.json --musique raw/dl/musique/musique_ans_v1.0_dev.jsonl --n $(N) --seed 0

run:
	for d in hotpotqa musique; do $(PY) scripts/run_agent.py --questions raw/$${d}_n$(N)_seed0.jsonl --model $(MODEL) || exit 1; done

dense:  # robustness check: same loop with a dense retriever (gemini-embedding-2), small model
	for d in hotpotqa musique; do $(PY) scripts/run_agent.py --questions raw/$${d}_n500_seed0.jsonl --model $(DENSE_MODEL) --retriever dense || exit 1; done

eval:
	$(PY) scripts/evaluate.py $(filter-out %pilot.jsonl,$(wildcard runs/*_n$(N)_seed0__*.jsonl))  # every full-run log

report:
	$(PY) scripts/compare.py > /dev/null
	$(PY) scripts/plots.py

test:
	.venv/bin/pytest -q
