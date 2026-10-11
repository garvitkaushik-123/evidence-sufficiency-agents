"""Download the two datasets into raw/dl/ (skips files that exist) and convert HotpotQA to the original json format.

MuSiQue-Ans dev: HuggingFace dgslibisey/MuSiQue (same jsonl as the official release).
HotpotQA distractor dev: HuggingFace hotpotqa/hotpot_qa parquet, converted to hotpot_dev_distractor_v1.json
(the official CMU host was unreachable); 7405 questions, same as the official dev set.
"""
import argparse
import json
import urllib.request
from pathlib import Path

HF = "https://huggingface.co/datasets"
MUSIQUE = f"{HF}/dgslibisey/MuSiQue/resolve/main/musique_ans_v1.0_dev.jsonl"
HOTPOT = f"{HF}/hotpotqa/hotpot_qa/resolve/main/distractor/validation-00000-of-00001.parquet"


def fetch(url, dest):
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("downloading", url)
        urllib.request.urlretrieve(url, dest)


def hotpot_parquet_to_json(src, dest):
    import pyarrow.parquet as pq  # pip install -e ".[data]"
    rows = pq.read_table(src).to_pylist()
    out = [{"_id": r["id"], "question": r["question"], "answer": r["answer"],
            "context": [[t, list(s)] for t, s in zip(r["context"]["title"], r["context"]["sentences"])],
            "supporting_facts": [[t, int(i)] for t, i in zip(r["supporting_facts"]["title"], r["supporting_facts"]["sent_id"])]}
           for r in rows]
    dest.write_text(json.dumps(out))
    print(dest, len(out), "questions")


ap = argparse.ArgumentParser()
ap.add_argument("--out", default="raw/dl")
a = ap.parse_args()
out = Path(a.out)
fetch(MUSIQUE, out / "musique/musique_ans_v1.0_dev.jsonl")
fetch(HOTPOT, out / "hotpot/validation.parquet")
if not (out / "hotpot/hotpot_dev_distractor_v1.json").exists():
    hotpot_parquet_to_json(out / "hotpot/validation.parquet", out / "hotpot/hotpot_dev_distractor_v1.json")
