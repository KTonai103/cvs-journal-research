#!/usr/bin/env python3
"""Per-chapter and per-journal ranked views over the triaged corpus, so the
final ~50 can be picked deliberately rather than by a single global score."""
import json
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "corpus")
recs = json.load(open(os.path.join(OUT, "triaged.json")))

# Journals that publish figure-rich, step-by-step operative material
TECHNIQUE_JOURNALS = re.compile(
    r"Ann Cardiothorac Surg|Multimed Man Cardiothorac Surg|Innovations|"
    r"JTCVS Tech|Oper Tech Thorac|J Vis Surg|Semin Thorac|"
    r"Interact Cardiovasc Thorac|Interdiscip Cardiovasc Thorac|"
    r"Ann Thorac Surg|J Thorac Cardiovasc Surg|Eur J Cardiothorac Surg|"
    r"J Card Surg|Gen Thorac Cardiovasc Surg|Ann Thorac Cardiovasc Surg|"
    r"J Robot Surg|Int J Med Robot|J Thorac Dis|Front Cardiovasc Med", re.I)


def line(k):
    return (f"[{k['score']:>3}] PMID {k['pmid']} ({k['year']}) "
            f"{'ROBO' if k['robotic'] else 'ENDO'} "
            f"{'PMC' if k['pmc'] else '---'} | {k['journal']}\n"
            f"      {k['title']}\n")


bych = defaultdict(list)
for k in recs:
    for c in k["chapters"]:
        bych[c].append(k)

with open(os.path.join(OUT, "by_chapter.txt"), "w") as f:
    for ch in ["mitral", "avr", "tecab", "asd_tumor", "arrhythmia",
               "tricuspid_redo", "port_setup", "training", "future", "general"]:
        items = sorted(bych[ch], key=lambda x: -x["score"])
        f.write(f"\n{'='*78}\n== {ch.upper()}  (n={len(items)})\n{'='*78}\n\n")
        for k in items[:70]:
            f.write(line(k))
            f.write("\n")

tech = [k for k in recs if TECHNIQUE_JOURNALS.search(k["journal"] or "")]
tech.sort(key=lambda x: -x["score"])
with open(os.path.join(OUT, "by_technique_journal.txt"), "w") as f:
    f.write(f"technique-journal candidates: {len(tech)}\n\n")
    for k in tech[:260]:
        f.write(line(k))
        f.write("\n")

print("chapters:", {c: len(v) for c, v in sorted(bych.items())})
print("technique-journal candidates:", len(tech))
print("journal counts (top 30):",
      Counter(k["journal"] for k in recs).most_common(30))
