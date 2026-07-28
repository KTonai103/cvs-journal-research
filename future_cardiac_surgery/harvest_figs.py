#!/usr/bin/env python3
"""Harvest open-access figure images from PMC for the future-of-valve-surgery review.

Policy (RESEARCH_PLAN.md §図の方針):
  - Only figures from articles carrying a CC licence (CC BY / CC BY-NC / CC BY-NC-ND) go into
    the public HTML. Licence for every PMC ID below was read from the PMC OA service
    (utils/oa/oa.fcgi) and is recorded in the 4th field for tables/figure_credits.csv.
  - The seed Editorial (ezag185) is NOT open access → its 4 figures stay in figures_local/
    and never reach output/. Nothing from it is listed here.
  - Third-party material inside an OA article is NOT covered by that article's CC licence.
    Every caption below was read in the JATS XML for
    "Reproduced / adapted / permission / courtesy / ©" before being listed.

Excluded on purpose (third-party rights inside an OA article):
  PMC10264707 Figure 2 (von Kossa histology panels — caption says "Reprinted with ...")

Notes (same traps as the AF review's harvest_figs.py):
  - Image bytes live ONLY at https://cdn.ncbi.nlm.nih.gov/pmc/blobs/... ; the
    .../articles/PMCxxxx/bin/<file>.jpg path returns a 404 HTML page that will happily be
    written into a .jpg. We check JPEG/PNG magic bytes.
  - PMC throws reCAPTCHA on rapid access: article HTML is cached locally, 3-6 s between hits.

Usage: python3 harvest_figs.py        # downloads into figures/ (skips existing)
"""
import os, re, sys, time, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(BASE, "figures")
CACHE = os.path.join(BASE, "pdf_text", "pmc_html")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}

# slug, PMC, image basename in the article, licence, chapter, short purpose
FIGS = [
    # 第3章 VSARR / 集約化
    ("govers_vo_longterm",  "PMC13282078", "ezag177f1.jpg", "CC BY 4.0",        3,
     "年間症例数と長期AV再介入回避生存の非線形関係（P=.0023）と年12例の閾値"),
    ("govers_vo_early",     "PMC13282078", "ezag177f2.jpg", "CC BY 4.0",        3,
     "早期複合エンドポイントは症例数と関連しない（P=.8003）"),
    ("aviator_reint",       "PMC9942544",  "ezac514f3.jpg", "CC BY-NC 4.0",     3,
     "AVIATOR：基部再介入回避はVSRRとCVG-ARRで差がない（P=0.98）"),
    ("aviator_survival",    "PMC9942544",  "ezac514f2.jpg", "CC BY-NC 4.0",     3,
     "AVIATOR：全生存（5年 95.4% vs 85.4%, P=0.002）"),
    ("avp_device_view",     "PMC10903180", "ezad291f2.jpg", "CC BY 4.0",        3,
     "術中加圧可視化device による大動脈弁の直視像（n=24の単群）"),
    # 第5章 Ross
    ("ross_vs_mavr_surv",   "PMC10897596", "gr3.jpg",       "CC BY-NC-ND 4.0",  5,
     "Ross vs 機械弁AVR のmicrosimulation生存曲線（18歳モデル）"),
    # 第6章 脱細胞化homograft
    ("dph20_freedom",       "PMC13017825", "ezag087f2.jpg", "CC BY-NC 4.0",     6,
     "脱細胞化肺homograft 20年：死亡/心内膜炎/explant回避と、狭窄・逆流回避"),
    ("dph20_function",      "PMC13017825", "ezag087f3.jpg", "CC BY-NC 4.0",     6,
     "explant回避曲線に年次ごとの機能状態を重ねた図（20年で機能良好が消える）"),
    ("arise_explant",       "PMC11009017", "ezae121f2.jpg", "CC BY 4.0",        6,
     "ARISE 144例と全DAH 358例のexplant回避（5年92.4%→10年69.5%）"),
    ("decell10_vs_ch_bjv",  "PMC4951634",  "ezw05004.jpg",  "CC BY 4.0",        6,
     "脱細胞化(DPH) vs 凍結保存homograft(CH) vs bovine jugular vein(BJV) のexplant回避"),
    # 第7章 組織工学弁・ポリマー弁
    ("xeltis_pi_histogram", "PMC7969645",  "fcvm-07-583360-g0005.jpg", "CC BY 4.0", 7,
     "Xeltis XPV：肺動脈弁逆流(PI)の頻度分布。第1世代(group 1)で重度PIが集積"),
    ("xeltis_explant",      "PMC7969645",  "fcvm-07-583360-g0003.jpg", "CC BY 4.0", 7,
     "摘出されたXPV conduitの上流/下流像"),
    ("shf_structure",       "PMC11708634", "gr1.jpg",       "CC BY-NC-ND 4.0",  7,
     "シンフォリウム（合成ハイブリッド生地）の構造と前臨床の経時的組織像"),
    ("shf_sites",           "PMC11708634", "gr3.jpg",       "CC BY-NC-ND 4.0",  7,
     "34例41部位の植込み部位（PA 18/RVOT 12/心房中隔7/心室中隔4）"),
    # 第8章 Ozaki（原典はJACC Adv＝権利上使用不可。反証側のJTCVS Techを採用）
    ("avneo_svd_cuminc",    "PMC11184442", "gr4.jpg",       "CC BY-NC-ND 4.0",  8,
     "AVNeo 162例：中等度SVD・重度SVD・心内膜炎・bioprosthetic valve failureの累積発生率"),
    ("avneo_gradients",     "PMC11184442", "gr1.jpg",       "CC BY-NC-ND 4.0",  8,
     "AVNeo：ピーク/平均圧較差とEOAの経時変化（5年まで安定）"),
    # 第2章・第10章 日本のMICS集約化
    ("jp_mics_volume_dist", "PMC13139202", "11748_2025_2225_Fig1_HTML.jpg", "CC BY 4.0", 2,
     "日本のMICS僧帽弁症例数の施設分布（年10例未満の施設が多数）"),
]


def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")


def article_html(pmc):
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
    for slug, pmc, bf, lic, ch, why in FIGS:
        by_pmc.setdefault(pmc, []).append((slug, bf))
    ok = fail = 0
    for pmc, items in by_pmc.items():
        pending = [(s, b) for s, b in items
                   if not os.path.exists(os.path.join(FIGDIR, f"fv_{s}_{pmc}.jpg"))]
        if not pending:
            continue
        h = article_html(pmc)
        if not h:
            print(f"FAIL article {pmc}", file=sys.stderr); fail += len(pending); continue
        urls = {u.split("/")[-1]: u for u in re.findall(
            r"https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^\"']+?\.(?:jpg|jpeg|png|gif)", h)}
        for slug, bf in pending:
            u = urls.get(bf)
            if not u:
                print(f"MISS {pmc} {bf}  (available: {sorted(urls)[:8]})", file=sys.stderr)
                fail += 1; continue
            b = get(u, binary=True)
            if b[:2] != b"\xff\xd8" and b[:4] != b"\x89PNG":
                print(f"BAD  {slug}: not an image ({len(b)} bytes)", file=sys.stderr)
                fail += 1; continue
            dst = os.path.join(FIGDIR, f"fv_{slug}_{pmc}.jpg")
            open(dst, "wb").write(b)
            print(f"OK   {os.path.basename(dst)}  {len(b)//1024} KB")
            ok += 1
            time.sleep(0.5)
    print(f"\ndownloaded {ok}, failed {fail}, total listed {len(FIGS)}")
    print("next: copy figures/ into ../output/figures_future_valve/ (HTML resolves from output/)")


if __name__ == "__main__":
    main()
