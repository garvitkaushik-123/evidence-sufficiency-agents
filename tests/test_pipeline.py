import json

from ess import data
from ess.agent import parse_judge, run_all
from ess.bm25 import BM25
from ess.check import check_log
from ess.llm import MockLLM


def hotpot_fixture(tmp_path, n=20):
    exs = []
    for i in range(n):
        ctx = [[f"Gold A{i}", [f"Alpha{i} was founded by Zed{i}."]],
               [f"Gold B{i}", [f"Zed{i} was born in Town{i}."]]]
        ctx += [[f"Distractor {i}-{j}", [f"Unrelated filler text number {j} about topic{j}."]] for j in range(8)]
        exs.append({"_id": f"h{i}", "question": f"Where was the founder of Alpha{i} born?", "answer": f"Town{i}",
                    "context": ctx, "supporting_facts": [[f"Gold A{i}", 0], [f"Gold B{i}", 0]]})
    p = tmp_path / "hotpot.json"
    p.write_text(json.dumps(exs))
    return p


def test_hotpot_gold_and_sampling_deterministic(tmp_path):
    qs = data.load_hotpot(hotpot_fixture(tmp_path))
    assert all(len(q["gold_pids"]) == 2 and len(q["paragraphs"]) == 10 for q in qs)
    a = [q["id"] for q in data.sample(qs, 5, seed=0)]
    b = [q["id"] for q in data.sample(list(reversed(qs)), 5, seed=0)]
    assert a == b and a != [q["id"] for q in data.sample(qs, 5, seed=1)]


def test_musique_loader_skips_unanswerable(tmp_path):
    rows = [{"id": "m1", "question": "q", "answer": "a", "answer_aliases": ["x"], "answerable": True,
             "paragraphs": [{"title": "T1", "paragraph_text": "p1", "is_supporting": True},
                            {"title": "T2", "paragraph_text": "p2", "is_supporting": False}]},
            {"id": "m2", "question": "q", "answer": "", "answerable": False, "paragraphs": []}]
    p = tmp_path / "m.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows))
    qs = data.load_musique(p)
    assert [q["id"] for q in qs] == ["m1"] and len(qs[0]["gold_pids"]) == 1


def test_corpus_dedupes_shared_paragraphs(tmp_path):
    qs = data.load_hotpot(hotpot_fixture(tmp_path, 3))
    assert len(data.build_corpus(qs)) == 30
    assert len(data.build_corpus(qs + qs)) == 30


def test_bm25_finds_gold_and_excludes_seen(tmp_path):
    qs = data.load_hotpot(hotpot_fixture(tmp_path))
    bm = BM25(data.build_corpus(qs))
    top = bm.search(qs[0]["question"], k=3)
    assert top[0]["pid"] in qs[0]["gold_pids"]
    again = bm.search(qs[0]["question"], k=3, exclude={p["pid"] for p in top})
    assert not ({p["pid"] for p in top} & {p["pid"] for p in again})


def test_parse_judge_variants():
    assert parse_judge("VERDICT: SUFFICIENT\nPROBABILITY: 0.9\nANSWER: Paris") == ("SUFFICIENT", 0.9, "Paris", True)
    v, p, a, ok = parse_judge("**VERDICT:** INSUFFICIENT\n**PROBABILITY:** 30%\n**ANSWER:** unknown")
    assert (v, p, a, ok) == ("INSUFFICIENT", 0.3, "unknown", True)
    assert parse_judge("VERDICT: SUFFICIENT")[3] is False


def test_end_to_end_log_has_all_fields(tmp_path):
    qs = data.load_hotpot(hotpot_fixture(tmp_path, 4))
    bm = BM25(data.build_corpus(qs))

    def script(prompt):
        if prompt.startswith("You are searching"):
            return "founder born town"
        return "VERDICT: INSUFFICIENT\nPROBABILITY: 0.4\nANSWER: guess"

    out = tmp_path / "log.jsonl"
    run_all(qs, MockLLM(script), bm, out)
    n, problems = check_log(out)
    assert n == 4 and problems == []
    rec = json.loads(out.read_text().splitlines()[0])
    assert len(rec["steps"]) == 5 and rec["model"] == "mock"
    ctx = rec["steps"][-1]["context_pids"]
    assert len(ctx) == len(set(ctx)) == 15  # 5 steps x k=3, no repeats
    # resumable: a second call adds nothing
    run_all(qs, MockLLM(script), bm, out)
    assert len(out.read_text().splitlines()) == 4


def test_evaluate_rules_and_metrics():
    from ess.evaluate import auroc, f1, norm, stop_step
    assert norm("The Eiffel Tower!") == "eiffel tower" and f1("Eiffel Tower", "the eiffel tower") == 1.0
    step = lambda t, v, p, cov: {"step": t, "verdict": v, "probability": p, "context_pids": ["g"] if cov else []}
    r = {"gold_pids": ["g"], "steps": [step(1, "SUFFICIENT", .6, False), step(2, "INSUFFICIENT", .9, True), step(3, "SUFFICIENT", .9, True)]}
    assert stop_step(("self",), r) == 1 and stop_step(("tau", .8), r) == 2
    assert stop_step(("oracle",), r) == 2 and stop_step(("fixed", 5), r) == 3
    assert auroc([.9, .1], [1, 0]) == 1.0


def test_paired_diff_keeps_sign_and_pairing():
    from ess.evaluate import paired_diff
    a = {i: (1, 0.9) for i in range(40)}
    b = {i: (3, 0.5) for i in range(40)}
    d, (lo, hi), ds = paired_diff(a, b, n_boot=200)
    assert abs(d - 0.4) < 1e-9 and lo > 0 and ds == -2
