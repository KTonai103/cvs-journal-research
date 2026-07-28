#!/usr/bin/env python3
"""MMCTS tutorials have no PDF (they are video-based). Capture the full text + video
chapter list from the Inertia JSON payload, verifying the title against PubMed first.
"""
import html, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "md", "mmcts")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")

TARGETS = {  # PMID -> (DOI, expected PubMed title)
    "34705350": ("10.1510/mmcts.2021.065",
                 "Myocardial revascularization: Tips and tricks for performing a coronary anastomosis"),
    "34787965": ("10.1510/mmcts.2021.076",
                 "Step-by-step harvesting of various grafts for coronary artery bypass surgery"),
    "33155775": ("10.1510/mmcts.2020.049",
                 "The endoscopic no-touch saphenous vein harvesting technique"),
}

SECTIONS = [
    ("abstract", "Abstract"), ("introduction", "Introduction"),
    ("patient_presentation", "Patient presentation"),
    ("surgical_technique_prefix", "Surgical technique"),
    ("surgical_technique_suffix", "Surgical technique (cont.)"),
    ("outcome_and_discussion", "Outcome and discussion"),
    ("summary", "Summary"), ("references", "References"),
]


def detag(s):
    s = re.sub(r"<br\s*/?>", "\n", s or "")
    s = re.sub(r"</p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


os.makedirs(OUT, exist_ok=True)
for pmid, (doi, want) in TARGETS.items():
    page = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA,
                           f"https://doi.org/{doi}"], capture_output=True, text=True).stdout
    m = re.search(r'data-page="([^"]+)"', page)
    if not m:
        print(f"NG  {pmid}  payload not found")
        continue
    post = json.loads(html.unescape(m.group(1)))["props"]["post"]
    got = (post.get("title") or "").strip()
    if got.lower()[:40] != want.lower()[:40]:
        print(f"NG  {pmid}  TITLE MISMATCH -> {got[:70]}")
        continue

    lines = [f"# {got}", "",
             f"- PMID: {pmid} / DOI: {doi} / MMCTS tutorial {post.get('id')}",
             f"- Authors: {', '.join(a.get('name','') for a in post.get('authors', []))}",
             f"- Published: {(post.get('published_at') or '')[:10]}"
             f" / duration: {post.get('duration')} / level: {post.get('expertise_level')}", ""]
    vs = post.get("video_sections") or []
    if vs:
        lines += ["## Video chapters", ""]
        lines += [f"- {v.get('start_time','')} — {detag(v.get('title') or v.get('name') or '')}"
                  for v in vs] + [""]
    for key, label in SECTIONS:
        body = detag(post.get(key))
        if body:
            lines += [f"## {label}", "", body, ""]

    dest = os.path.join(OUT, f"MMCTS_{pmid}_{re.sub(r'[^A-Za-z0-9]+','-',got)[:50].strip('-')}.md")
    text = "\n".join(lines)
    open(dest, "w").write(text)
    print(f"OK  {pmid}  {len(text)//1000}k chars, {len(vs)} chapters -> "
          f"{os.path.relpath(dest, HERE)}")
