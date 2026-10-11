"""Sample questions with a fixed seed; save ids (committed) and full records (raw/, gitignored)."""
import argparse
from pathlib import Path

from ess import data

ap = argparse.ArgumentParser()
ap.add_argument("--hotpot", required=True, help="hotpot_dev_distractor_v1.json")
ap.add_argument("--musique", required=True, help="musique_ans_v1.0_dev.jsonl")
ap.add_argument("--n", type=int, default=500)
ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()

Path("raw").mkdir(exist_ok=True)
Path("data/ids").mkdir(parents=True, exist_ok=True)
for name, load, path in (("hotpotqa", data.load_hotpot, a.hotpot), ("musique", data.load_musique, a.musique)):
    qs = data.sample(load(path), a.n, a.seed)
    data.save_ids(qs, f"data/ids/{name}_n{a.n}_seed{a.seed}.json")
    data.save_questions(qs, f"raw/{name}_n{a.n}_seed{a.seed}.jsonl")
    print(name, len(qs), "questions,", len(data.build_corpus(qs)), "corpus paragraphs")
