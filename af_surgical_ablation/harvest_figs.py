#!/usr/bin/env python3
"""Harvest open-access figure images from PMC for the surgical-AF-ablation review.

Only figures that are (1) in an article carrying a CC license AND (2) NOT flagged as
third-party material inside that article are listed here. Articles are CC BY / CC BY-NC /
CC BY-NC-ND; every entry below was verified by reading the article's JATS XML caption for
"permission / Reproduced / adapted / courtesy / ©" and by viewing the image itself.

Excluded on purpose (third-party rights inside an OA article — the CC license does NOT cover them):
  PMC13339239 Fig1 (Cox-Maze cut-and-sew, (c) Circ Arrhythm Electrophysiol)
  PMC13339239 Fig3/4/5 (EpiSense / EnCompass / cryo probes, (c) AtriCure & Medtronic)
  PMC12214460 Fig2 (decision flowchart, reproduced from McCarthy & Cox)
  PMC11095052 Fig1/2 (adapted from Hahn et al.)
  PMC12719823 Fig2 (reproduced)

Notes that cost time the first round:
  - PMC ID conversion: use https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/
    (the old /pmc/utils/idconv/v1.0/ endpoint 301-redirects and breaks JSON parsing).
  - Image bytes live ONLY at https://cdn.ncbi.nlm.nih.gov/pmc/blobs/... — the
    .../articles/PMCxxxx/bin/<file>.jpg path returns a 404 HTML page that will happily be
    written to a .jpg file. We verify the JPEG/PNG magic bytes instead.
  - PMC throws reCAPTCHA on rapid access: article HTML is cached locally, 3-6 s between hits.

Usage: python3 harvest_figs.py            # downloads into figures/ (skips existing)
"""
import os, re, sys, time, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(BASE, "figures")
CACHE = os.path.join(BASE, "corpus", "pmc_html")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}

# slug, PMC, image basename in the article, license (for the credits table in the review)
FIGS = [
    ("afmr_progression",     "PMC8203518",  "11748_2021_1629_Fig2_HTML.jpg",  "CC BY 4.0"),
    ("afmr_gap",             "PMC8203518",  "11748_2021_1629_Fig4_HTML.jpg",  "CC BY 4.0"),
    ("afmr_patch",           "PMC8203518",  "11748_2021_1629_Fig5_HTML.jpg",  "CC BY 4.0"),
    ("asmr_vs_vsmr",         "PMC13027757", "medicina-62-00520-g002.jpg",     "CC BY 4.0"),
    ("asmr_annuloplasty",    "PMC13027757", "medicina-62-00520-g003.jpg",     "CC BY 4.0"),
    ("afmr_mechanism",       "PMC12719823", "EHF2-12-3788-g001.jpg",          "CC BY-NC 4.0"),
    ("astr_overview",        "PMC11095052", "ehae088_ga.jpg",                 "CC BY-NC 4.0"),
    ("astr_discriminate",    "PMC11095052", "ehae088f3.jpg",                  "CC BY-NC 4.0"),
    ("astr_algorithm",       "PMC11095052", "ehae088f5.jpg",                  "CC BY-NC 4.0"),
    ("cmiv_lesionset",       "PMC13339239", "2153-8174-27-6-51123-g2.jpg",    "CC BY 4.0"),
    ("clamp_lesion_histo",   "PMC13339239", "2153-8174-27-6-51123-g6.jpg",    "CC BY 4.0"),
    ("cmiv_lesions_detail",  "PMC12059748", "2153-8174-26-4-26841-g2.jpg",    "CC BY 4.0"),
    ("maze_evolution",       "PMC12214460", "ezaf187f3.jpg",                  "CC BY-NC 4.0"),
    ("guideline_summary",    "PMC12214460", "ezaf187f1.jpg",                  "CC BY-NC 4.0"),
    ("sr_factors",           "PMC12214460", "ezaf187f4.jpg",                  "CC BY-NC 4.0"),
    ("concomitant_survival", "PMC13244388", "nihms-2162312-f0003.jpg",        "CC BY-NC-ND 4.0"),
    ("biatrial_vs_la",       "PMC13244388", "nihms-2162312-f0007.jpg",        "CC BY-NC-ND 4.0"),
    ("csa_trend",            "PMC12342894", "ezaf244f3.jpg",                  "CC BY 4.0"),
    ("incomplete_lesions",   "PMC11883703", "gr1.jpg",                        "CC BY-NC-ND 4.0"),
    ("nonpv_foci",           "PMC11883703", "fx3.jpg",                        "CC BY-NC-ND 4.0"),
    ("cs_cryo",              "PMC11883703", "gr3.jpg",                        "CC BY-NC-ND 4.0"),
    ("marshallplan",         "PMC12094258", "hae-18-e013427-g001.jpg",        "CC BY-NC-ND 4.0"),
    ("pfa_tissue_zones",     "PMC13303300", "euag080f1.jpg",                  "CC BY 4.0"),
    ("pfa_complications",    "PMC13303300", "euag080f5.jpg",                  "CC BY 4.0"),
    ("laa_remnant_measure",  "PMC12399235", "gr1.jpg",                        "CC BY-NC-ND 4.0"),
    ("laa_suboptimal",       "PMC12399235", "gr2.jpg",                        "CC BY-NC-ND 4.0"),
    ("laao_success_time",    "PMC13178962", "ezag146f2.jpg",                  "CC BY-NC 4.0"),
    ("opinion_km",           "PMC13191831", "ehaf674f2.jpg",                  "CC BY 4.0"),
    ("ceaseaf_km",           "PMC12304665", "ezaf146f2.jpg",                  "CC BY 4.0"),
    ("ceaseaf_complications","PMC12304665", "ezaf146f3.jpg",                  "CC BY 4.0"),
    ("surhyb_km",            "PMC10872694", "euae040f2.jpg",                  "CC BY 4.0"),
    ("thora_vs_hybrid_km",   "PMC11448334", "euae232f3.jpg",                  "CC BY 4.0"),
    ("beatparox_km",         "PMC13043192", "ehaf1115f2.jpg",                 "CC BY-NC 4.0"),
    ("advent_lto_km",        "PMC13099369", "41591_2026_4246_Fig2_HTML.jpg",  "CC BY-NC-ND 4.0"),
    ("ppm_cuminc",           "PMC12005902", "ivaf085f2.jpg",                  "CC BY 4.0"),
]


def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")


def article_html(pmc):
    """Fetch (and cache) the PMC article page; retries around reCAPTCHA."""
    path = os.path.join(CACHE, pmc + ".html")
    if os.path.exists(path) and os.path.getsize(path) > 50_000:
        return open(path, encoding="utf-8").read()
    for attempt in range(4):
        time.sleep(3 + attempt * 4)
        try:
            h = get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")
        except Exception as e:
            print(f"  fetch error {pmc}: {e}", file=sys.stderr)
            continue
        if "reCAPTCHA" in h[:5000]:
            print(f"  {pmc} blocked, retrying", file=sys.stderr)
            continue
        open(path, "w", encoding="utf-8").write(h)
        return h
    return ""


def main():
    os.makedirs(FIGDIR, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)
    by_pmc = {}
    for slug, pmc, bf, lic in FIGS:
        by_pmc.setdefault(pmc, []).append((slug, bf))
    ok = fail = 0
    for pmc, items in by_pmc.items():
        pending = [(s, b) for s, b in items
                   if not os.path.exists(os.path.join(FIGDIR, f"af_{s}_{pmc}.jpg"))]
        if not pending:
            continue
        h = article_html(pmc)
        if not h:
            print(f"FAIL article {pmc}", file=sys.stderr)
            fail += len(pending)
            continue
        urls = {u.split("/")[-1]: u for u in re.findall(
            r"https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^\"']+?\.(?:jpg|jpeg|png|gif)", h)}
        for slug, bf in pending:
            u = urls.get(bf)
            if not u:
                print(f"MISS {pmc} {bf}", file=sys.stderr)
                fail += 1
                continue
            b = get(u, binary=True)
            if b[:2] != b"\xff\xd8" and b[:4] != b"\x89PNG":
                print(f"BAD  {slug}: not an image ({len(b)} bytes)", file=sys.stderr)
                fail += 1
                continue
            dst = os.path.join(FIGDIR, f"af_{slug}_{pmc}.jpg")
            open(dst, "wb").write(b)
            print(f"OK   {os.path.basename(dst)}  {len(b)//1024} KB")
            ok += 1
            time.sleep(0.5)
    print(f"\ndownloaded {ok}, failed {fail}, total listed {len(FIGS)}")
    print("remember: copy into ../output/figures/ as well (the HTML resolves figures/ from output/)")


if __name__ == "__main__":
    main()
