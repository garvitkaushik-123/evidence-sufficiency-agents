"""Small dependency-free BM25 (Okapi) over title + text."""
import math
import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9]+")
_STOP = frozenset("a an the of in on at to for and or is was are were by with as from that this it its be who what which when where how did does do".split())


def tokenize(s):
    return [t for t in _TOKEN.findall(s.lower()) if t not in _STOP]


class BM25:
    def __init__(self, paragraphs, k1=1.5, b=0.75):
        self.paras = paragraphs
        self.k1, self.b = k1, b
        self.tfs = [Counter(tokenize(p["title"] + " " + p["text"])) for p in paragraphs]
        self.lens = [sum(tf.values()) for tf in self.tfs]
        self.avg = sum(self.lens) / max(len(self.lens), 1)
        df = Counter(t for tf in self.tfs for t in tf)
        n = len(paragraphs)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def search(self, query, k=3, exclude=()):
        """Top-k paragraphs by score; `exclude` pids are skipped so each step yields new evidence."""
        q = tokenize(query)
        scored = []
        for i, tf in enumerate(self.tfs):
            if self.paras[i]["pid"] in exclude:
                continue
            s = 0.0
            for t in q:
                f = tf.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.lens[i] / self.avg))
            scored.append((s, i))
        scored.sort(key=lambda x: (-x[0], x[1]))
        return [self.paras[i] for s, i in scored[:k]]
