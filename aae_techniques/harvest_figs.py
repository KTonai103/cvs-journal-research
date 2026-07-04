#!/usr/bin/env python3
"""Harvest open-access figure images + captions from PMC for the AAE technique atlas.

Only OA-licensed articles are listed here (verified CC BY / CC BY-NC-ND).
Downloads full-resolution images into figures/ and writes corpus/figs_index.json.
"""
import re, sys, json, os, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(BASE, "figures")

# pmc: (license, short-name, pmid, doi)
ART = {
    "PMC12712157": ("CC BY 4.0", "Kitamura Y-and-I incision", "41425437", "10.1016/j.atssr.2025.04.013"),
    "PMC11148751": ("CC BY-NC-ND 4.0", "Yang rectangular-patch Y-incision", "38841092", "10.21037/acs-2023-aae-0151"),
    "PMC11148761": ("CC BY-NC-ND 4.0", "Makkinejad Y-incision vs traditional AAE", "38841083", "10.21037/acs-2023-aae-0102"),
    "PMC12237773": ("CC BY-NC-ND 4.0", "Wang new-roof Y-incision (Fuwai)", "40641760", "10.1016/j.xjtc.2025.02.013"),
    "PMC11148756": ("CC BY-NC-ND 4.0", "Truesdell aortic-root dimensions post Y-AAE", "38841089", "10.21037/acs-2024-aae-0042"),
}

def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")

out = {}
for pmc, (lic, name, pmid, doi) in ART.items():
    try:
        html = get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
    except Exception as e:
        print(f"ERR {pmc}: {e}", file=sys.stderr); continue
    figs = []
    for fm in re.finditer(r"<figure\b.*?</figure>", html, re.DOTALL):
        block = fm.group(0)
        imgs = re.findall(r'src="([^"]*?\.(?:jpg|jpeg|png|gif))"', block)
        lbl = re.search(r'<figcaption.*?>(.*?)</figcaption>', block, re.DOTALL)
        cap = re.sub(r"<[^>]+>", " ", lbl.group(1)).strip() if lbl else ""
        cap = re.sub(r"\s+", " ", cap)
        # figure number label e.g. "Figure 1" / "Fig 2"
        num = re.search(r'\b(Fig(?:ure)?\.?\s*\d+)', cap)
        if imgs:
            figs.append({"img": imgs, "caption": cap[:600], "num": num.group(1) if num else ""})
    out[pmc] = {"license": lic, "name": name, "pmid": pmid, "doi": doi, "figs": figs}
    print(f"== {pmc} ({name}) {lic} : {len(figs)} figures", file=sys.stderr)
    for i, f in enumerate(figs):
        print(f"   [{i}] {f['num']} imgs={f['img']}", file=sys.stderr)
        print(f"       cap: {f['caption'][:140]}", file=sys.stderr)

json.dump(out, open(os.path.join(BASE, "corpus", "figs_index.json"), "w"), ensure_ascii=False, indent=2)
print("\nwrote corpus/figs_index.json", file=sys.stderr)
