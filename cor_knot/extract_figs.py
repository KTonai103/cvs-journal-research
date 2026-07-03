#!/usr/bin/env python3
import re, sys, urllib.request, json, os

ART = {
    "PMC10792379": ("BY-NC", "How It Happens/Prevent", "37927063"),
    "PMC11708687": ("BY", "Leaflet Perforation MIS AVR", "39790133"),
    "PMC8186203":  ("BY", "Incidence regurg/perforation", "34099017"),
    "PMC12291292": ("BY", "Aortic root injury", "40708028"),
    "PMC12529675": ("BY", "Valsalva sinus perforation", "41112446"),
    "PMC11211209": ("BY", "Preventive role SAVR", "38913864"),
}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")

out = {}
for pmc, (lic, name, pmid) in ART.items():
    try:
        html = get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
    except Exception as e:
        print(f"ERR {pmc}: {e}", file=sys.stderr); continue
    figs = []
    # find <figure ...> ... </figure> blocks
    for fm in re.finditer(r"<figure\b.*?</figure>", html, re.DOTALL):
        block = fm.group(0)
        # image src (prefer full-res bin jpg)
        imgs = re.findall(r'src="([^"]*?\.(?:jpg|jpeg|png|gif))"', block)
        # figure label
        lbl = re.search(r'<figcaption.*?>(.*?)</figcaption>', block, re.DOTALL)
        cap = re.sub(r"<[^>]+>", " ", lbl.group(1)).strip() if lbl else ""
        cap = re.sub(r"\s+", " ", cap)
        if imgs:
            figs.append({"img": imgs, "caption": cap[:400]})
    out[pmc] = {"license": lic, "name": name, "pmid": pmid, "figs": figs}
    print(f"== {pmc} ({name}) CC-{lic} : {len(figs)} figures", file=sys.stderr)
    for i, f in enumerate(figs):
        print(f"   [{i}] imgs={f['img']}", file=sys.stderr)
        print(f"       cap: {f['caption'][:160]}", file=sys.stderr)

json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus", "figs_index.json"), "w"), ensure_ascii=False, indent=2)
