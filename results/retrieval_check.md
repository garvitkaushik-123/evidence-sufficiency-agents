# Retrieval check: BM25 vs dense

Dense = `gemini-embedding-2`, 768 dimensions, cosine. Query = the raw question, ranking over the pooled corpus of the 500 sampled questions.

| dataset | retriever | k | all gold in top-k | mean share of gold in top-k |
|---|---|---|---|---|
| hotpotqa | bm25 | 3 | 0.366 | 0.644 |
| hotpotqa | bm25 | 5 | 0.476 | 0.721 |
| hotpotqa | bm25 | 10 | 0.736 | 0.867 |
| hotpotqa | bm25 | 15 | 0.802 | 0.900 |
| hotpotqa | dense | 3 | 0.886 | 0.938 |
| hotpotqa | dense | 5 | 0.940 | 0.970 |
| hotpotqa | dense | 10 | 0.978 | 0.989 |
| hotpotqa | dense | 15 | 0.984 | 0.992 |
| musique | bm25 | 3 | 0.072 | 0.406 |
| musique | bm25 | 5 | 0.118 | 0.470 |
| musique | bm25 | 10 | 0.168 | 0.534 |
| musique | bm25 | 15 | 0.202 | 0.578 |
| musique | dense | 3 | 0.298 | 0.630 |
| musique | dense | 5 | 0.396 | 0.711 |
| musique | dense | 10 | 0.572 | 0.811 |
| musique | dense | 15 | 0.630 | 0.845 |
