#!/usr/bin/env python3
"""Assemble the Ross technique review from md/parts/*.md and build the HTML.

Steps
  1. concatenate md/parts/*.md in filename order
  2. expand <!--FIGINDEX--> into the 図表一覧 table (scanned from the <figure> blocks)
  3. expand <!--REFLIST--> from md/paper_pick_list.md
  4. write md/Ross_Technique_Review.md
  5. copy figures/ into ../output/figures/ (the HTML lives in output/ and resolves figures/…)
  6. run build_html.py

Usage: python3 ross_technique/build.py
"""
import glob
import os
import re
import shutil
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
PARTS = os.path.join(BASE, "md", "parts")
OUT_MD = os.path.join(BASE, "md", "Ross_Technique_Review.md")
OUT_HTML = os.path.join(ROOT, "output", "ross_technique_review.html")


def figindex(text):
    """Build the 図表一覧 rows from every <figure id=…> block in document order."""
    rows = []
    for m in re.finditer(r'<figure class="([^"]*)" id="([^"]+)">(.*?)</figure>',
                         text, re.DOTALL):
        cls, fid, body = m.group(1), m.group(2), m.group(3)
        cap = re.search(r"<figcaption>(.*?)</figcaption>", body, re.DOTALL)
        cap = cap.group(1) if cap else ""
        title = re.search(r"<b>(.*?)</b>", cap)
        title = re.sub(r"<[^>]+>", "", title.group(1)) if title else fid
        src = re.search(r'<span class="src">(.*?)</span>', cap, re.DOTALL)
        src = re.sub(r"<[^>]+>", "", src.group(1)) if src else ""
        src = src.replace("出典: ", "").replace("サムネイル画像出典: ", "") \
                 .replace("サムネイル出典: ", "").strip()
        lic = ""
        lm = re.search(r"（(CC BY[^）]*)）", src)
        if lm:
            lic = lm.group(1)
            src = src.replace("（" + lic + "）", "").strip()
        kind = "動画" if "vfig" in cls else "図"
        rows.append(f"| [{title}](#{fid}) | {kind} | {src} | {lic} |")
    header = ("| 番号・内容 | 種別 | 出典 | ライセンス |\n|---|---|---|---|\n")
    return (f"全 {len(rows)} 点（うち動画リンク "
            f"{sum(1 for r in rows if '| 動画 |' in r)} 点）。番号をクリックすると"
            f"本文の該当箇所へ移動する。\n\n" + header + "\n".join(rows))


# DOIs whose publisher resolver returns 404 (checked 2026-07-27) — printed unlinked.
DEAD_DOI = {"10.52198/24.STI.44.CV1763"}


def reflist():
    """Format md/paper_pick_list.md into a linked reference list, grouped by section."""
    src = open(os.path.join(BASE, "md", "paper_pick_list.md"), encoding="utf-8").read()
    out, n = [], 0
    for line in src.split("\n"):
        if line.startswith("## ") and not line.startswith("## PMID"):
            out.append("\n**" + line[3:].strip() + "**\n")
            continue
        m = re.match(r"^\d+\.\s+([★☆])\s+\*\*PMID:\s*(\d+)\*\*\s*(?:\[PMC:(PMC\d+)\])?\s*(.*)$",
                     line.strip())
        if not m:
            continue
        star, pmid, pmc, rest = m.groups()
        rest = rest.replace("　", " ").strip()
        doi = ""
        dm = re.search(r"doi:(\S+)$", rest)
        if dm:
            doi = dm.group(1).rstrip(".")
            rest = rest[:dm.start()].strip()
        badges = [f"[PMID {pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)"]
        if pmc:
            badges.append(f"[PMC](https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/)")
        if doi in DEAD_DOI:
            badges.append(f"doi:{doi}（リンク切れ）")
        elif doi:
            badges.append(f"[doi](https://doi.org/{doi})")
        mark = "★" if star == "★" else ""
        n += 1
        out.append(f"{n}. {mark} {rest} — " + " · ".join(badges))
    return "\n".join(out)


def main():
    parts = sorted(glob.glob(os.path.join(PARTS, "*.md")))
    if not parts:
        sys.exit("no parts found")
    text = "\n".join(open(p, encoding="utf-8").read().rstrip() + "\n" for p in parts)

    n_fig = len(re.findall(r'<figure class="', text))
    n_vid = len(re.findall(r'<figure class="[^"]*vfig', text))
    text = text.replace('<span id="figcount">—</span>', str(n_fig - n_vid))
    text = text.replace('<span id="vidcount">—</span>', str(n_vid))
    text = text.replace("<!--FIGINDEX-->", figindex(text))
    text = text.replace("<!--REFLIST-->", reflist())

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  MD:  {OUT_MD} ({os.path.getsize(OUT_MD)/1024:.1f} KB, "
          f"{len(text)} chars, {n_fig} figures)")

    dst = os.path.join(ROOT, "output", "figures")
    os.makedirs(dst, exist_ok=True)
    copied = 0
    for f in glob.glob(os.path.join(BASE, "figures", "*.jpg")):
        t = os.path.join(dst, os.path.basename(f))
        if not os.path.exists(t) or os.path.getmtime(f) > os.path.getmtime(t):
            shutil.copy2(f, t)
            copied += 1
    print(f"  figures copied to output/figures/: {copied}")

    subprocess.run([sys.executable, os.path.join(BASE, "build_html.py"),
                    OUT_MD, OUT_HTML], check=True)

    # every referenced image must exist next to the HTML
    missing = [s for s in re.findall(r'src="(figures/[^"]+)"', text)
               if not os.path.exists(os.path.join(ROOT, "output", s))]
    print("  missing images: " + (", ".join(missing) if missing else "none"))


if __name__ == "__main__":
    main()
