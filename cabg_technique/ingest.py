#!/usr/bin/env python3
"""Match manually downloaded PDFs in ~/Downloads to the 60-paper list and file them.

Matching is done on extracted text (DOI first, then a title-token score), never on the
filename - publisher filenames carry online-first years that disagree with the citation.
"""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDFDIR = os.path.join(HERE, "pdf")


def text_of(path, pages=3):
    return subprocess.run(["pdftotext", "-f", "1", "-l", str(pages), path, "-"],
                          capture_output=True, text=True).stdout


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(s, n=52):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")[:n].rstrip("-")


recs = json.load(open(os.path.join(HERE, "raw/selected_verified.json")))
status = {r["pmid"]: r for r in json.load(open(os.path.join(HERE, "raw/download_status.json")))}
order = {p: i for i, p in enumerate(open(os.path.join(HERE, "selected.txt")).read().split())}

files = sys.argv[1:]
report = []
for path in files:
    if not os.path.exists(path):
        report.append((path, None, 0, "file not found"))
        continue
    txt = text_of(path)
    ntxt = norm(txt)
    best, score = None, 0

    # 1) DOI match
    dois = {d.lower().rstrip(".,;)") for d in re.findall(r"10\.\d{4,9}/[^\s\"'<>]+", txt)}
    for r in recs:
        d = (r.get("doi") or "").lower()
        if d and any(x.startswith(d) or d.startswith(x) for x in dois):
            best, score = r, 999
            break

    # 2) title-token overlap on the first pages
    if not best:
        for r in recs:
            toks = [t for t in norm(r["title"]).split() if len(t) > 3]
            if not toks:
                continue
            hit = sum(1 for t in toks if t in ntxt) / len(toks)
            if hit > score:
                best, score = r, hit
        if score < 0.7:
            report.append((path, best, score, "LOW CONFIDENCE"))
            continue

    idx = order[best["pmid"]] + 1
    name = (f"{idx:02d}_{best['year']}_{slug(best['first_author'], 18)}_"
            f"{slug(best['journal'], 14)}_{slug(best['title'], 46)}_PMID{best['pmid']}.pdf")
    dest = os.path.join(PDFDIR, name)
    note = "already filed" if os.path.exists(dest) else "filed"
    if not os.path.exists(dest):
        shutil.copy2(path, dest)
        st = status.get(best["pmid"])
        if st:
            st.update(status="ok", source="manual_dl", file=name)
    report.append((path, best, score, note))

json.dump(list(status.values()),
          open(os.path.join(HERE, "raw/download_status.json"), "w"),
          ensure_ascii=False, indent=1)

for path, r, sc, note in report:
    tag = "DOI" if sc == 999 else (f"{sc:.0%}" if r else "  -")
    pm = r["pmid"] if r else "-"
    print(f"{note:<14} {tag:>4} {pm:<9} {os.path.basename(path)[:46]:<46} "
          f"{(r['title'][:52] if r else '')}")

ok = sum(1 for r in status.values() if r["status"] == "ok")
print(f"\n=== 取得済み {ok}/60 ===")
