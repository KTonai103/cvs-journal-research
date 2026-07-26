#!/usr/bin/env python3
"""Fill in figure captions/licence from cached PMC HTML for articles Europe PMC
has no fullTextXML for (Ann Cardiothorac Surg, NIH author manuscripts), then
print the whole inventory for hand-picking.

Usage: python3 index_html_figs.py [--dump]
"""
import html as _html
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, "figure_index.json")
HTML = os.path.join(BASE, "corpus", "pmc_html")


def txt(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", _html.unescape(s)).strip()


def main():
    idx = json.load(open(INDEX))
    for pmc, rec in idx.items():
        p = os.path.join(HTML, pmc + ".html")
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8", errors="replace").read()
        if not rec.get("license"):
            m = re.search(r"(Creative Commons[^<]{0,240})", h)
            if m:
                rec["license"] = txt(m.group(1))[:240]
        if not rec.get("figs"):
            figs = []
            for fm in re.finditer(r'<figure class="fig[^"]*"[^>]*>(.*?)</figure>', h, re.DOTALL):
                blk = fm.group(1)
                lab = re.search(r'<h4 class="obj_head">(.*?)</h4>', blk, re.DOTALL)
                cap = re.search(r"<figcaption>(.*?)</figcaption>", blk, re.DOTALL)
                img = re.search(r'src="(https://cdn[^"]+?\.(?:jpg|jpeg|png|gif))"', blk)
                figs.append({
                    "label": txt(lab.group(1)) if lab else "",
                    "graphic": img.group(1).split("/")[-1] if img else "",
                    "caption": txt(cap.group(1))[:1400] if cap else "",
                })
            rec["figs"] = figs
    json.dump(idx, open(INDEX, "w"), ensure_ascii=False, indent=1)

    if "--dump" in sys.argv:
        for pmc, rec in idx.items():
            print(f"\n{'='*100}\n{pmc}  {rec['tag']}\n  LICENSE: {rec['license'][:150]}")
            for f in rec["figs"]:
                g = f["graphic"] or "?"
                flag = ""
                low = f["caption"].lower()
                for w in ("reproduced", "with permission", "adapted from", "courtesy",
                          "©", "copyright", "reprinted"):
                    if w in low:
                        flag = "  <<< THIRD-PARTY?"
                print(f"  [{f['label'] or '-':<14}] {g:<40} {f['caption'][:220]}{flag}")
            if not rec["figs"]:
                print(f"  (no captions parsed) blobs: {list(rec['blobs'])[:16]}")
    else:
        n = sum(len(v["figs"]) for v in idx.values())
        print(f"updated {INDEX}: {n} figures across {len(idx)} articles")


if __name__ == "__main__":
    main()
