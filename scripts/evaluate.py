"""Print RQ1/RQ2 numbers and the stopping-rule table for each run log: python scripts/evaluate.py runs/*.jsonl"""
import sys

from ess.evaluate import report

for p in sys.argv[1:]:
    report(p)
