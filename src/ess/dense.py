"""Dense retriever: Gemini embeddings and cosine similarity, with the same search() interface as BM25."""
import os
import time
from pathlib import Path

import numpy as np


class GeminiEmbedder:
    """embed(texts, task) -> L2-normalised float32 array. One Content per text, because gemini-embedding-2 merges a
    plain list of strings into a single embedding."""

    def __init__(self, model="gemini-embedding-2", dim=768, batch=50):
        from google import genai
        from google.genai import types
        self.types = types
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=120_000))
        self.model_id, self.dim, self.batch = model, dim, batch

    def __call__(self, texts, task):
        out = []
        for i in range(0, len(texts), self.batch):
            chunk = texts[i:i + self.batch]
            contents = [self.types.Content(parts=[self.types.Part(text=t)]) for t in chunk]
            for attempt in range(7):
                try:
                    r = self.client.models.embed_content(
                        model=self.model_id, contents=contents,
                        config=self.types.EmbedContentConfig(task_type=task, output_dimensionality=self.dim))
                    break
                except Exception:
                    if attempt == 6:
                        raise
                    time.sleep(min(60, 5 * 2 ** attempt))
            assert len(r.embeddings) == len(chunk)
            out.extend(e.values for e in r.embeddings)
        v = np.asarray(out, dtype=np.float32)
        return v / np.linalg.norm(v, axis=1, keepdims=True)


class DenseRetriever:
    def __init__(self, paragraphs, embed, cache=None):
        """`embed` is any callable (texts, task) -> normalised array. Document vectors are cached in `cache` (.npz)."""
        self.paras, self.embed = paragraphs, embed
        pids = [p["pid"] for p in paragraphs]
        if cache and Path(cache).exists() and list(np.load(cache)["pids"]) == pids:
            self.docs = np.load(cache)["vecs"]
        else:
            self.docs = embed([f"{p['title']}: {p['text']}" for p in paragraphs], "RETRIEVAL_DOCUMENT")
            if cache:
                Path(cache).parent.mkdir(parents=True, exist_ok=True)
                np.savez(cache, pids=np.array(pids), vecs=self.docs)
        self.index = {pid: i for i, pid in enumerate(pids)}

    def search(self, query, k=3, exclude=()):
        """Top-k paragraphs by cosine similarity; `exclude` pids are skipped so each step yields new evidence."""
        scores = self.docs @ self.embed([query], "RETRIEVAL_QUERY")[0]
        for pid in exclude:
            scores[self.index[pid]] = -np.inf
        top = sorted(range(len(scores)), key=lambda i: (-scores[i], i))[:k]
        return [self.paras[i] for i in top]
