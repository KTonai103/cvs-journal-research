#!/usr/bin/env python3
"""Compress the reading corpus: drop references, affiliations and journal
boilerplate so the technique content fits one context."""
import glob, os, re

CUT_FROM = re.compile(r'^\s*(References|REFERENCES|Bibliography)\s*$', re.M)
DROP_LINE = re.compile(r"""
 ^\s*(Downloaded\ from|Correspondence\ to|Email:|E-mail:|ORCID|
 Conflicts?\ of\ Interest|Funding:|Open\ Access|This\ is\ an\ open\ access|
 Creative\ Commons|creativecommons\.org|©|ª|Copyright|
 doi:|DOI:|https?://|Submitted\ |Accepted\ for\ publication|Published\ online|
 Peer\ Review\ File|Reporting\ Checklist|reporting\ checklist|
 View\ this\ article\ at|Cite\ this\ article\ as|
 \d{1,4}\s*$|Page\ \d+\ of\ \d+\s*$)
""", re.X)

os.makedirs("reading", exist_ok=True)
tot_in = tot_out = 0
for f in sorted(glob.glob("pdf_text/*.txt")):
    s = open(f, errors="replace").read()
    tot_in += len(s)
    m = CUT_FROM.search(s)
    if m and m.start() > len(s) * 0.35:      # only cut a trailing reference list
        s = s[:m.start()]
    lines = [l for l in s.split("\n") if not DROP_LINE.match(l)]
    s = re.sub(r'\n{3,}', '\n\n', "\n".join(lines)).strip()
    out = "reading/" + os.path.basename(f)
    open(out, "w").write(s + "\n")
    tot_out += len(s)
print(f"{tot_in/1024:.0f} KB -> {tot_out/1024:.0f} KB  ({100*tot_out/tot_in:.0f}%)")
