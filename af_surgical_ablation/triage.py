#!/usr/bin/env python3
"""Triage harvested PubMed records into a reviewable shortlist."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
recs = json.load(open(os.path.join(HERE, "corpus", "records.json")))

HIGH = {
    "n engl j med": 10, "lancet": 10, "jama": 9, "jama cardiol": 9,
    "circulation": 9, "eur heart j": 9, "j am coll cardiol": 9,
    "jacc clin electrophysiol": 8, "jacc cardiovasc imaging": 8,
    "jacc heart fail": 8, "jacc cardiovasc interv": 8,
    "j thorac cardiovasc surg": 8, "ann thorac surg": 8,
    "eur j cardiothorac surg": 8, "jtcvs open": 6, "jtcvs tech": 6,
    "ann thorac surg short rep": 5,
    "heart rhythm": 7, "europace": 7, "circ arrhythm electrophysiol": 8,
    "j cardiovasc electrophysiol": 6, "eur heart j cardiovasc imaging": 7,
    "interdiscip cardiovasc thorac surg": 6, "interact cardiovasc thorac surg": 6,
    "j heart lung transplant": 7, "circ cardiovasc interv": 7,
    "eur j heart fail": 7, "heart": 6, "am j cardiol": 5, "int j cardiol": 5,
    "j am heart assoc": 6, "circ j": 5, "gen thorac cardiovasc surg": 5,
    "ann cardiothorac surg": 5, "semin thorac cardiovasc surg": 6,
    "eur heart j suppl": 4, "j clin med": 3, "j thorac dis": 3,
    "innovations (phila)": 5, "multimed man cardiothorac surg": 4,
    "j cardiothorac surg": 3, "front cardiovasc med": 3,
}
PT_BONUS = {
    "Randomized Controlled Trial": 6, "Meta-Analysis": 5,
    "Practice Guideline": 8, "Guideline": 8, "Systematic Review": 4,
    "Multicenter Study": 2, "Review": 1, "Comparative Study": 1,
    "Consensus Development Conference": 6,
}
LANDMARK = re.compile(
    r"LAAOS|CONVERGE|EAST-AFNET|CASTLE|CABANA|ADVENT|CTSN|AVATAR|"
    r"guideline|consensus|expert|meta-analys|systematic review|randomi",
    re.I)


def score(r):
    s = HIGH.get(r["journal"].lower().rstrip("."), 0)
    for pt in r.get("pubtype", []):
        s += PT_BONUS.get(pt, 0)
    if LANDMARK.search(r["title"]):
        s += 3
    try:
        y = int(r["year"])
        s += max(0, (y - 2016)) * 0.5
    except Exception:
        pass
    return s


THEME_LABEL = {
    "01": "Cox-Maze IV 遠隔成績", "02": "同時手術アブレーション全般",
    "03": "ガイドライン/コンセンサス", "04": "Box lesion / 後壁隔離",
    "05": "PVI vs biatrial lesion set", "06": "Cryo vs RF",
    "07": "ハイブリッドアブレーション", "08": "Convergent / 心外膜",
    "09": "胸腔鏡下・低侵襲単独手術", "10": "外科 vs カテーテル比較",
    "11": "LAA閉鎖 (LAAOS III等)", "12": "AtriClip / クリップデバイス",
    "13": "AFMR 心房性機能性MR", "14": "AFTR 心房性機能性TR",
    "15": "AFMR/AFTR 外科治療", "16": "PFA 基礎/臨床",
    "17": "PFA 外科・心外膜応用", "18": "PFA 再発・ギャップ",
    "19": "左房サイズと成績", "20": "左房縮小術",
    "21": "僧帽弁手術+AF", "22": "CABG/AVR+AF",
    "23": "洞調律維持の予後インパクト", "24": "早期リズムコントロール",
    "25": "デバイス (AtriCure等)", "26": "その他エネルギー源",
    "27": "GP / Marshall靱帯", "28": "日本・アジア",
    "29": "合併症・ペースメーカ", "30": "アブレーション後の抗凝固",
}

by_theme = {}
for pid, r in recs.items():
    r["score"] = score(r)
    for q in r["queries"]:
        by_theme.setdefault(q, []).append(r)

topn = int(sys.argv[1]) if len(sys.argv) > 1 else 25
for key in sorted(by_theme):
    lst = sorted(by_theme[key], key=lambda x: -x["score"])[:topn]
    print(f"\n{'='*100}\n## {key}  {THEME_LABEL.get(key[:2],'')}\n{'='*100}")
    for r in lst:
        print(f"[{r['score']:5.1f}] PMID {r['pmid']} | {r['year']} | {r['journal']}")
        print(f"        {r['title']}")
