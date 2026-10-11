"""Multi-step retrieval agent. Always runs all T steps and logs every step, so every
stopping rule can be evaluated offline from the same log (one run per question per model).

Log record per question (one JSON line):
  {run, model, retriever, question_id, dataset, question, gold_answer, aliases, gold_pids, T, k,
   steps: [{step, query, retrieved_pids, context_pids, verdict, probability, answer,
            raw_judge, parse_ok}]}
`context_pids` is cumulative, so gold coverage at step t is computed offline from the log alone.
"""
import json
import re

QUERY_PROMPT = """You are searching a document collection to answer a question.

Question: {question}

Evidence so far:
{evidence}

Write ONE short search query that would find the missing information needed to answer the question. Output only the query."""

JUDGE_PROMPT = """Question: {question}

Evidence retrieved so far:
{evidence}

Using ONLY the evidence above, answer these three items exactly in this format:
VERDICT: SUFFICIENT or INSUFFICIENT (is the evidence enough to answer the question with certainty?)
PROBABILITY: a number from 0 to 1 (probability that the evidence is sufficient)
ANSWER: your best current answer, as short as possible (a few words)"""


def fmt_evidence(paras):
    if not paras:
        return "(none yet)"
    return "\n".join(f"[{i + 1}] {p['title']}: {p['text']}" for i, p in enumerate(paras))


def parse_judge(text):
    """Return (verdict, probability, answer, ok). Tolerates markdown/bold; ok=False if any field is missing."""
    v = re.search(r"VERDICT\W*(INSUFFICIENT|SUFFICIENT)", text, re.I)
    p = re.search(r"PROBABILITY\W*?(\d*\.?\d+)", text, re.I)
    a = re.search(r"ANSWER\W*[:\-]\s*(.+)", text, re.I)
    verdict = v.group(1).upper() if v else None
    prob = None
    if p:
        prob = float(p.group(1))
        if prob > 1:  # tolerate "85" meaning 85%
            prob = prob / 100 if prob <= 100 else None
    answer = a.group(1).strip().strip("*").strip() if a else None
    return verdict, prob, answer, all(x is not None for x in (verdict, prob, answer))


def run_question(q, llm, retriever, T=5, k=3, run_id="", retriever_name="bm25"):
    context, steps = [], []
    seen = set()
    for t in range(1, T + 1):
        if t == 1:
            query = q["question"]
        else:
            query = llm.complete(QUERY_PROMPT.format(question=q["question"], evidence=fmt_evidence(context))).strip().splitlines()[0]
        hits = retriever.search(query, k=k, exclude=seen)
        for h in hits:
            seen.add(h["pid"])
        context.extend(hits)
        raw = llm.complete(JUDGE_PROMPT.format(question=q["question"], evidence=fmt_evidence(context)))
        verdict, prob, answer, ok = parse_judge(raw)
        steps.append({"step": t, "query": query, "retrieved_pids": [h["pid"] for h in hits],
                      "context_pids": [p["pid"] for p in context], "verdict": verdict,
                      "probability": prob, "answer": answer, "raw_judge": raw, "parse_ok": ok})
    return {"run": run_id, "model": llm.model_id, "retriever": retriever_name,
            "question_id": q["id"], "dataset": q["dataset"], "question": q["question"],
            "gold_answer": q["answer"], "aliases": q.get("aliases", []),
            "gold_pids": q["gold_pids"], "T": T, "k": k, "steps": steps}


def run_all(questions, llm, retriever, out_path, T=5, k=3, run_id="", retriever_name="bm25"):
    """Append one JSON line per question; resumable (skips ids already in out_path)."""
    done = set()
    try:
        with open(out_path) as f:
            done = {json.loads(l)["question_id"] for l in f if l.strip()}
    except FileNotFoundError:
        pass
    with open(out_path, "a") as f:
        for q in questions:
            if q["id"] in done:
                continue
            rec = run_question(q, llm, retriever, T, k, run_id, retriever_name)
            f.write(json.dumps(rec) + "\n")
            f.flush()
