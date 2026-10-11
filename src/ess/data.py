"""Load HotpotQA (distractor dev) and MuSiQue-Ans (dev) into one schema, sample with a fixed seed.

Unified question record:
  {id, dataset, question, answer, aliases, paragraphs: [{pid, title, text}], gold_pids: [pid]}
A paragraph pid is a content hash, so identical paragraphs shared across questions pool into one corpus entry.
"""
import hashlib
import json
import random
from pathlib import Path


def make_pid(title: str, text: str) -> str:
    return hashlib.sha1(f"{title}\x00{text}".encode()).hexdigest()[:12]


def _para(title, text):
    return {"pid": make_pid(title, text), "title": title, "text": text}


def load_hotpot(path):
    """HotpotQA distractor dev json: list of {_id, question, answer, context, supporting_facts}."""
    out = []
    for ex in json.loads(Path(path).read_text()):
        paras = [_para(t, " ".join(s.strip() for s in sents)) for t, sents in ex["context"]]
        gold_titles = {t for t, _ in ex["supporting_facts"]}
        gold = [p["pid"] for p in paras if p["title"] in gold_titles]
        out.append({"id": ex["_id"], "dataset": "hotpotqa", "question": ex["question"],
                    "answer": ex["answer"], "aliases": [], "paragraphs": paras, "gold_pids": gold})
    return out


def load_musique(path):
    """MuSiQue-Ans dev jsonl: {id, question, answer, answer_aliases, answerable, paragraphs: [{title, paragraph_text, is_supporting}]}."""
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            ex = json.loads(line)
            if ex.get("answerable") is False:
                continue
            paras, gold = [], []
            for p in ex["paragraphs"]:
                para = _para(p["title"], p["paragraph_text"])
                paras.append(para)
                if p["is_supporting"]:
                    gold.append(para["pid"])
            out.append({"id": ex["id"], "dataset": "musique", "question": ex["question"],
                        "answer": ex["answer"], "aliases": ex.get("answer_aliases", []),
                        "paragraphs": paras, "gold_pids": gold})
    return out


def sample(questions, n, seed):
    """Deterministic sample: sort by id first so the result does not depend on file order."""
    qs = sorted(questions, key=lambda q: q["id"])
    return random.Random(seed).sample(qs, n)


def save_ids(questions, path):
    Path(path).write_text(json.dumps([q["id"] for q in questions], indent=0) + "\n")


def save_questions(questions, path):
    with open(path, "w") as f:
        for q in questions:
            f.write(json.dumps(q) + "\n")


def load_questions(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def build_corpus(questions):
    """Pool paragraphs of the sampled questions into one corpus, deduplicated by pid."""
    corpus = {}
    for q in questions:
        for p in q["paragraphs"]:
            corpus.setdefault(p["pid"], p)
    return list(corpus.values())
