"""Week-1 exit check: every step of every question has verdict, probability, answer and retrieved ids."""
import json


def check_log(path, T=5):
    problems, n = [], 0
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            n += 1
            r = json.loads(line)
            qid = r["question_id"]
            if len(r["steps"]) != r["T"] or r["T"] != T:
                problems.append(f"{qid}: expected {T} steps, got {len(r['steps'])}")
            for s in r["steps"]:
                for key in ("verdict", "probability", "answer"):
                    if s.get(key) is None:
                        problems.append(f"{qid} step {s['step']}: missing {key}")
                if not s.get("retrieved_pids"):
                    problems.append(f"{qid} step {s['step']}: no retrieved ids")
    return n, problems
