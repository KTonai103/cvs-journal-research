#!/usr/bin/env python3
"""Harvest open-access figures for the Ross technique review.

Two sources per article:
  * Europe PMC `fullTextXML`  -> licence statement + every figure label/caption
    (reliable, no bot check; used to spot third-party "reproduced with permission"
    figures that the article's CC licence does NOT cover)
  * PMC article HTML          -> the cdn.ncbi.nlm.nih.gov/pmc/blobs/… image bytes
    (the only path that serves the image; /articles/PMCxxx/bin/… is a 404 page)

urllib gets served the "Checking your browser - reCAPTCHA" stub; curl with a
browser UA does not, so every fetch goes through curl.

Usage:
  python3 harvest_figs.py meta      # cache XML + HTML, write figure_index.json
  python3 harvest_figs.py get       # download the images listed in FIGS
"""
import json
import os
import re
import subprocess
import sys
import time

BASE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BASE, "corpus")
FIGDIR = os.path.join(BASE, "figures")
INDEX = os.path.join(BASE, "figure_index.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

ARTICLES = {
    # Ann Cardiothorac Surg 2021 Ross issue (AME, CC BY-NC-ND) — not in the PMC OA subset
    "PMC8339621":  "Mazine_ACS2021_NonRepairableAR",
    "PMC8339626":  "Williams_ACS2021_TotalRoot",
    "PMC8339631":  "Afifi_ACS2021_LooseJacket",
    "PMC8339632":  "Skillington_ACS2021_Inclusion",
    "PMC8339629":  "Jahanyar_ACS2021_InclusionDacron",
    "PMC8339634":  "Misfeld_ACS2021_Subcoronary",
    "PMC8339622":  "David_ACS2021_WhyHowLearn",
    "PMC8339614":  "Liebrich_ACS2021_ReinforcedFullRoot",
    "PMC8339625":  "Abeln_ACS2021_AfterFailedRepair",
    "PMC8339636":  "Said_ACS2021_RossKonno",
    "PMC8339633":  "Sievers_ACS2021_GermanRegistry",
    "PMC10405345": "Jahanyar_ACS2023_ValveSparing",
    "PMC10248915": "Marey_ACS2023_VSRR",
    # JTCVS Tech / Open / Struct-Endovasc, ATS Short Reports (Elsevier, CC BY or CC BY-NC-ND)
    "PMC12237868": "Dafflisio_JTCVSTech2025_RootPressurization",
    "PMC11184485": "Spindel_JTCVSTech2024_FloridaSleeve",
    "PMC11145418": "Redondo_JTCVSTech2024_PEARS",
    "PMC11145073": "Farhat_JTCVSTech2024_2F",
    "PMC12683052": "Cote_JTCVSTech2025_DoubleRing",
    "PMC13245295": "Kawamura_ATSShortRep2026_ReversedGraft",
    "PMC13069552": "Nam_JTCVSTech2026_FullRoot",
    "PMC8691921":  "Skillington_JTCVSTech2021_RightSided",
    "PMC12230465": "Rea_JTCVSOpen2025_RVOT",
    "PMC10431381": "Filippa_JTCVSTech2023_BicuspidPV",
    "PMC11632344": "Verdi_JTCVSTech2024_AnomalousCoronary",
    "PMC11519732": "Tsaroev_JTCVSTech2024_Ministernotomy",
    "PMC13244776": "Stephens_JTCVSSE2026_Reoperations",
    "PMC9938366":  "Zhu_JTCVSTech2023_BeatingHeart",
    "PMC11708156": "Shih_ATSShortRep2023_Mentoring",
    # other CC-licensed journals
    "PMC13085382": "Ramkaran_JCTS2026_Rupture",
    "PMC12011152": "Koliastasis_JACCCaseRep2025_CoronaryOcclusion",
    "PMC12028067": "Scorsese_JCDD2025_Anesthesia",
    "PMC10516720": "Chandra_CJCOpen2023_ExplantedHearts",
    "PMC12909017": "Bloom_JAHA2026_Renaissance",
    # NIH author manuscript (no CC licence — inventory only, not embedded)
    "PMC8924018":  "Zhu_JTCVS2023_ExVivoBiomechanics",
}

# slug, PMC, blob basename, licence — filled in after reading figure_index.json.
# Third-party figures inside an OA article are deliberately absent (see FIGURES.md).
FIGS = []
try:
    FIGS = json.load(open(os.path.join(BASE, "figs_selected.json")))
except OSError:
    pass


def curl(url, out=None, tries=4):
    for i in range(tries):
        cmd = ["curl", "-sSL", "-A", UA, "--compressed", url]
        if out:
            cmd = ["curl", "-sSL", "-A", UA, "--compressed", "-o", out, url]
        r = subprocess.run(cmd, capture_output=True)
        data = open(out, "rb").read() if out else r.stdout
        if out:
            if len(data) > 2000 and not data[:400].lstrip().startswith(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE html"):
                return data
        else:
            if b"Checking your browser" not in data[:4000] and len(data) > 2000:
                return data
        time.sleep(3 + 4 * i)
    return b""


def meta():
    os.makedirs(os.path.join(CACHE, "epmc_xml"), exist_ok=True)
    os.makedirs(os.path.join(CACHE, "pmc_html"), exist_ok=True)
    index = {}
    for pmc, tag in ARTICLES.items():
        rec = {"tag": tag, "license": "", "figs": [], "blobs": {}}

        xp = os.path.join(CACHE, "epmc_xml", pmc + ".xml")
        if not (os.path.exists(xp) and os.path.getsize(xp) > 5000):
            d = curl(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML")
            if d:
                open(xp, "wb").write(d)
            time.sleep(0.6)
        if os.path.exists(xp):
            x = open(xp, encoding="utf-8", errors="replace").read()
            lm = re.search(r"<license\b.*?</license>", x, re.DOTALL)
            if lm:
                rec["license"] = strip(lm.group(0))[:400]
            for fm in re.finditer(r"<fig\b.*?</fig>", x, re.DOTALL):
                blk = fm.group(0)
                lab = re.search(r"<label>(.*?)</label>", blk, re.DOTALL)
                cap = re.search(r"<caption>(.*?)</caption>", blk, re.DOTALL)
                g = re.search(r'xlink:href="([^"]+)"', blk)
                rec["figs"].append({
                    "label": strip(lab.group(1)) if lab else "",
                    "graphic": g.group(1) if g else "",
                    "caption": strip(cap.group(1))[:1400] if cap else "",
                })

        hp = os.path.join(CACHE, "pmc_html", pmc + ".html")
        if not (os.path.exists(hp) and os.path.getsize(hp) > 40000):
            d = curl(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
            if d:
                open(hp, "wb").write(d)
            time.sleep(1.2)
        if os.path.exists(hp) and os.path.getsize(hp) > 40000:
            h = open(hp, encoding="utf-8", errors="replace").read()
            for u in re.findall(r"https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/"
                                r"[^\"'\s)]+?\.(?:jpg|jpeg|png|gif)", h):
                rec["blobs"].setdefault(u.split("/")[-1], u)

        index[pmc] = rec
        print(f"{pmc} {tag:52s} figs={len(rec['figs']):2d} blobs={len(rec['blobs']):2d} "
              f"lic={'yes' if rec['license'] else 'NO'}")
    json.dump(index, open(INDEX, "w"), ensure_ascii=False, indent=1)
    print(f"\nwrote {INDEX}")


def strip(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def get():
    os.makedirs(FIGDIR, exist_ok=True)
    index = json.load(open(INDEX))
    ok = fail = 0
    for slug, pmc, bf, lic in FIGS:
        dst = os.path.join(FIGDIR, f"ross_{slug}.jpg")
        if os.path.exists(dst) and os.path.getsize(dst) > 5000:
            continue
        blobs = index.get(pmc, {}).get("blobs", {})
        u = blobs.get(bf)
        if not u:
            near = [b for b in blobs if bf.split(".")[0] in b]
            print(f"MISS {pmc} {bf}  (candidates: {near[:4]})", file=sys.stderr)
            fail += 1
            continue
        b = curl(u, out=dst)
        if not b or (b[:2] != b"\xff\xd8" and b[:4] != b"\x89PNG"):
            print(f"BAD  {slug}: not an image", file=sys.stderr)
            fail += 1
            continue
        print(f"OK   ross_{slug}.jpg  {len(b)//1024} KB  [{lic}]")
        ok += 1
        time.sleep(0.4)
    print(f"\ndownloaded {ok}, failed {fail}, listed {len(FIGS)}")


if __name__ == "__main__":
    {"meta": meta, "get": get}[sys.argv[1] if len(sys.argv) > 1 else "meta"]()
