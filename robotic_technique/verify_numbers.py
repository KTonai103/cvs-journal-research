#!/usr/bin/env python3
"""Two-stage numeric fact-check of the review against the reading corpus.

Stage 1 — every numeric token in the review body must appear somewhere in the
          corpus (reading/*.txt + md/*.md).  Catches transcription slips.
Stage 2 — co-occurrence: for each review line, the numbers on that line should
          all be findable within a single corpus line, which catches numbers
          that exist in the corpus but were re-combined wrongly.

Numbers that legitimately have no corpus source (dates, section numbers, the
review's own counts) are listed in ALLOW.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(HERE, "md", "robotic_technique_review.md")

NUM = re.compile(r"\d+(?:[.,]\d+)*")

ALLOW = {
    # review metadata / structure
    "2026", "2025", "2024", "2023", "2022", "07", "27", "75", "46", "59",
    # cross-reference to the sister review (robotic_cpb), not this corpus
    "283", "31",
    # section and figure numbering handled separately
}

SKIP_LINE = re.compile(
    r"^\s*(\|\s*\d+\s*\|)"            # numbered reference rows
    r"|doi\.org|pubmed\.ncbi|mmcts\.org|^\s*<img|^\s*<figcaption|^\s*<figure"
    r"|^#{1,4}\s|^\s*\|\s*図|^\s*<!--"
)


def corpus():
    """OUP/EJCTS print numbers as "13 731"; fold the space separator away."""
    text = []
    for pat in ("reading/*.txt", "md/*_ABSTRACT.md", "md/*MMCTS.md"):
        for f in glob.glob(os.path.join(HERE, pat)):
            text.append(open(f, errors="replace").read())
    joined = "\n".join(text)
    return re.sub(r"(?<=\d) (?=\d{3}\b)", "", joined)


def normalise(s):
    return s.replace(",", "").rstrip(".").rstrip("0").rstrip(".") if "." in s \
        else s.replace(",", "")


def main():
    body = open(REVIEW, encoding="utf-8").read()
    body = body.split("## 付録A")[0]          # body only, not the appendices
    corp = corpus()
    corp_nums = {normalise(n) for n in NUM.findall(corp)}
    corp_lines = corp.splitlines()

    unmatched, mixed = [], []
    in_video = False
    for i, line in enumerate(body.splitlines(), 1):
        # injected video blocks carry MMCTS metadata (durations, step counts),
        # not claims from the reading corpus — inject_videos.py checks those
        # against the site catalogue instead.
        if line.startswith("<!-- VID:"):
            in_video = True
        elif line.startswith("<!-- /VID:"):
            in_video = False
            continue
        if in_video or SKIP_LINE.search(line):
            continue
        nums = [n for n in NUM.findall(line)]
        keep = [n for n in nums if normalise(n) not in ALLOW and len(n) > 1]
        if not keep:
            continue
        for n in keep:
            if normalise(n) not in corp_nums:
                unmatched.append((i, n, line.strip()[:120]))
        # stage 2: all numbers on the line should co-occur in one corpus line
        if len(keep) >= 2:
            wanted = {normalise(n) for n in keep}
            ok = any(wanted <= {normalise(x) for x in NUM.findall(cl)}
                     for cl in corp_lines)
            if not ok:
                mixed.append((i, sorted(wanted), line.strip()[:120]))

    print(f"corpus numeric tokens: {len(corp_nums)}")
    print(f"\n== stage 1: numbers with no corpus source ({len(unmatched)}) ==")
    for i, n, l in unmatched:
        print(f"  L{i}  {n!r}  | {l}")
    print(f"\n== stage 2: multi-number lines not co-occurring ({len(mixed)}) ==")
    for i, ns, l in mixed[:80]:
        print(f"  L{i}  {ns}  | {l}")
    if len(mixed) > 80:
        print(f"  ... {len(mixed) - 80} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
