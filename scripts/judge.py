"""LLM-judge the agent's answer at every step of a BrowseComp-Plus run log.
Prompt: BrowseComp-Plus grader template (texttron/BrowseComp-Plus, MIT); judge model: Gemini instead of gpt-4.1.
Verdicts are cached by (judge, question, answer) in runs/browsecomp_judge_cache.json, so re-runs are free.
Writes runs/<log>.judged.json = {question_id: {step: true/false}}. Both files are gitignored (they hold decrypted text).
Usage: python scripts/judge.py runs/browsecomp_n100_seed0__<model>.jsonl [--judge gemini-3.8-flash] [--handcheck 20]"""
import argparse
import csv
import hashlib
import json
import random
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from ess.evaluate import load
from ess.llm import GeminiLLM

GRADER = """
Judge whether the following [response] to [question] is correct or not based on the precise and unambiguous [correct_answer] below.

[question]: {question}

[response]: {response}

[correct_answer]: {correct_answer}

Your judgement must be in the format and criteria specified below:

extracted_final_answer: The final exact answer extracted from the [response]. 

[correct_answer]: Repeat the [correct_answer] given above.

reasoning: Explain why the extracted_final_answer is correct or incorrect based on [correct_answer], in the context of this [question]. You should judge whether the extracted_final_answer is semantically equivalent to [correct_answer], allowing the extracted_final_answer to be string variations of [correct_answer]. You should also allow the extracted_final_answer to be more precise or verbose than [correct_answer], as long as its additional details are correct. Do not comment on any background to the problem, do not attempt to solve the problem, do not argue for any answer different than [correct_answer], focus only on whether the answers are semantically equivalent.

correct: Answer 'yes' if extracted_final_answer matches the [correct_answer] given above, or is within a small margin of error for numerical problems. Answer 'no' otherwise, i.e. if there if there is any inconsistency, ambiguity, non-equivalency, or if the extracted answer is incorrect.

confidence: The extracted confidence score between 0|\\%| and 100|\\%| from [response]. Put 100 if there is no confidence score available.
""".strip()

CACHE = Path("runs/browsecomp_judge_cache.json")
ap = argparse.ArgumentParser()
ap.add_argument("log")
ap.add_argument("--judge", default="gemini-3.8-flash")
ap.add_argument("--handcheck", type=int, default=0, help="write N random judgements to a csv for a human check")
a = ap.parse_args()

recs = load(a.log)
cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
key = lambda r, ans: hashlib.sha1(f"{a.judge}\x00{r['question_id']}\x00{ans}".encode()).hexdigest()
llm = GeminiLLM(a.judge)


def judge(job):
    r, ans = job
    out = llm.complete(GRADER.format(question=r["question"], response=ans, correct_answer=r["gold_answer"]))
    m = re.findall(r"correct:\s*\**\s*(yes|no)", out, flags=re.I)
    return key(r, ans), (m[-1].lower() == "yes") if m else None


jobs = {key(r, s["answer"]): (r, s["answer"]) for r in recs for s in r["steps"] if s["answer"] and key(r, s["answer"]) not in cache}
print(len(jobs), "answers to judge (rest cached)")
with ThreadPoolExecutor(8) as ex:
    for k, v in ex.map(judge, jobs.values()):
        cache[k] = v
CACHE.write_text(json.dumps(cache))

# an empty answer (e.g. a failed reply) is incorrect; None = judge output did not parse
judged = {r["question_id"]: {s["step"]: (cache[key(r, s["answer"])] if s["answer"] else False) for s in r["steps"]} for r in recs}
Path(a.log).with_suffix(".judged.json").write_text(json.dumps(judged))
vals = [v for d in judged.values() for v in d.values()]
print(f"{sum(v is True for v in vals)} correct, {sum(v is False for v in vals)} incorrect, {sum(v is None for v in vals)} unparsed, of {len(vals)} steps")
last = [d[max(d)] for d in judged.values()]
print(f"final-step accuracy: {sum(v is True for v in last)}/{len(last)}")

if a.handcheck:
    pairs = sorted({(r["question_id"], s["answer"]) for r in recs for s in r["steps"] if s["answer"]})
    pick = random.Random(0).sample(pairs, min(a.handcheck, len(pairs)))
    by = {r["question_id"]: r for r in recs}
    out = Path(a.log).with_suffix(".handcheck.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "question", "gold_answer", "agent_answer", "judge_correct", "human_correct"])
        for q, ans in pick:
            r = by[q]
            w.writerow([q, r["question"], r["gold_answer"], ans, cache[key(r, ans)], ""])
    print("hand-check sheet:", out)
