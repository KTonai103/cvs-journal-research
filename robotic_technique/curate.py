#!/usr/bin/env python3
"""Hand-curated final download list, grouped by the review's chapters.

Selection criteria, in order:
  1. Figure-rich how-to content (step-by-step, "how I do it", trocar/port diagrams)
  2. Open access (PMC) — figures must be extractable for the HTML
  3. Unique contribution (no two entries covering the same ground)
  4. Named pitfall / complication content over pure outcome series
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "corpus")
meta = {r["pmid"]: r for r in json.load(open(os.path.join(OUT, "meta.json")))}

SELECTION = [
    ("A. 総論・エキスパートコンセンサス・プログラム構築", [
        ("41619927", "STS公式・ロボット心臓外科training pathwayの唯一の公式文書"),
        ("35748726", "ロボット僧帽弁の現状と推奨（欧州系の実質的コンセンサス）"),
        ("36237591", "ロボット僧帽弁プログラムの立ち上げ手順"),
        ("39209092", "習熟度到達の考え方（ATSレビュー）"),
    ]),
    ("B. ポート配置・体位・展開・術前CT計画", [
        ("40900082", "★MMCTS 男性のポート配置・体位（図の主軸）"),
        ("40900091", "★MMCTS 女性のポート配置・体位（乳房の扱い）"),
        ("39434974", "★TECABのトロカール配置「流派」比較＝配置図の比較検討"),
        ("41904670", "術前CTによる適応判定・アクセス計画のSR"),
        ("41669182", "ロボット僧帽弁の患者選択（Gillinov）"),
        ("39991302", "極端な低体重・薄い胸壁でのTips and tricks"),
        ("39991316", "第1肋骨胸骨結合の骨棘をLIMA採取のランドマークにする"),
    ]),
    ("C. 訓練・シミュレーション・ラーニングカーブ", [
        ("42188066", "ロボット/VATS心臓外科のシミュレーション訓練レビュー"),
        ("39786456", "wet labシミュレーションのラーニングカーブ実測"),
        ("37753828", "安価な自作TECABシミュレータの作り方"),
        ("39473044", "da Vinci Xi用・低コスト高忠実度IMA採取モデルの作製と検証"),
        ("30192451", "MMCTS 内視鏡下僧帽弁の「運針マップ」"),
        ("40886757", "MICSラーニングカーブのSR+メタ解析（症例数の定量）"),
    ]),
    ("D. 僧帽弁形成（MV repair）", [
        ("38152222", "★ロボット僧帽弁形成 成功のためのステップ"),
        ("38152209", "★ロボットMV形成を楽にするtricks and tips"),
        ("36237594", "★合併症とその対処＝助手（patient-side）視点"),
        ("24349995", "MICS僧帽弁のsafeguards and pitfalls（古典）"),
        ("41669170", "MAC（僧帽弁輪石灰化）など難症例をロボットで扱う"),
        ("38835581", "20年・ロボットMV形成で何を学んだか（Loulmet/NYU）"),
        ("41114561", "MMCTS 四角切除＋双方向スライディング"),
        ("40931770", "MMCTS 半連続3針＋flexible bandによる弁輪縫縮"),
        ("38152165", "弁下組織（腱・papillary）手技をロボットで行う"),
        ("37629762", "★Cx（左回旋枝）損傷という僧帽弁手術のpitfall"),
        ("40913323", "★ポートサイト出血をバルーンカテーテルでtamponadeする"),
    ]),
    ("E. 大動脈弁（AVR）", [
        ("40547427", "★側方アクセス完全ロボットAVR「RAVR」の確立"),
        ("40547428", "側方アプローチでの視野最適化"),
        ("40547426", "rapid deployment弁を使うロボット内視鏡AVR（Kitahara/千葉）"),
        ("40547430", "ロボットAVR＋大動脈弁輪拡大（小体格に直結）"),
        ("40547425", "ロボットAVR＋心室中隔心筋切除の同時手術"),
        ("40131409", "国際多施設RAVRの長期成績（エビデンスの位置づけ）"),
    ]),
    ("F. 冠動脈（TECAB / MIDCAB）", [
        ("39157189", "★ロボットでの末梢吻合の実際（Bonatti）"),
        ("39434978", "★Cx領域を出すための展開手技"),
        ("39434975", "MIDCABからTECABへ進むには（欧州 vs 米国）"),
        ("39157180", "ロボットCABGをどう「教える」か"),
        ("39434973", "ロボット支援MIDCABのstep-by-step"),
        ("39157183", "beating-heart TECABでのBITA・10年成績"),
        ("42232265", "多枝off-pump TECABの手術手技（Balkhy）"),
        ("23274864", "★ロボットCABGで胸骨正中切開に転換するリスク因子"),
    ]),
    ("G. Others（ASD・心房腫瘍／不整脈・LAA・リード／三尖弁・再手術）", [
        ("39669348", "ASD修復のpre-groove縦右房切開アプローチ"),
        ("39991301", "超音波アスピレータを用いたロボット心筋腫切除"),
        ("39196272", "MMCTS ロボット左心耳閉鎖の手順"),
        ("41134183", "★「speech bubble sign」＝左心耳閉鎖不完全のCT所見"),
        ("38541788", "ロボット心膜側ハイブリッドアブレーション＋LAA閉鎖"),
        ("38167378", "MMCTS 完全内視鏡ロボット三尖弁形成＋両心房CryoMAZE"),
        ("39267356", "再手術としてのロボット三尖弁手術の安全性"),
        ("36367136", "MMCTS 再手術僧帽弁：癒着剥離と複雑形成"),
        ("37314292", "MMCTS ロボット経僧帽弁的心筋切除（HOCM）"),
    ]),
    ("H. 展望（次世代機・遠隔・AR/AI）", [
        ("42027540", "単孔式ロボットによるCRT心外膜リード留置"),
        ("41622650", "hinotori（国産機）での両側IMA採取・初のヒト屍体例"),
        ("38845068", "単孔式システムはIMA採取に使えるか（Bonatti）"),
        ("41682905", "心臓外科におけるAR/MR（拡張現実）"),
    ]),
]


def fmt_cite(r):
    bits = [r["journal"]]
    if r["year"]:
        bits.append(r["year"])
    loc = ""
    if r["volume"]:
        loc = r["volume"]
        if r["issue"]:
            loc += f"({r['issue']})"
        if r["pages"]:
            loc += f":{r['pages']}"
    elif r["pages"]:
        loc = r["pages"]
    if loc:
        bits.append(loc)
    return "; ".join(bits[:2]) + (f"; {loc}" if loc else "")


rows = []
missing = []
n = 0
lines_md = ["# ロボット心臓外科 手技/Pitfall レビュー — DL対象論文リスト", "",
            f"総数 **{sum(len(v) for _, v in SELECTION)} 本**。",
            "`OA` = PubMed Central で全文・図が無料。★ = 図の主軸として特に重要。", ""]

for chapter, items in SELECTION:
    lines_md.append(f"\n## {chapter}\n")
    lines_md.append("| # | Title | PMID | Journal / Year | 全文 | 採用理由 |")
    lines_md.append("|---|---|---|---|---|---|")
    for pmid, why in items:
        r = meta.get(pmid)
        if r is None:
            missing.append(pmid)
            continue
        n += 1
        oa = f"OA (PMC{r['pmc'].replace('PMC','')})" if r["pmc"] else "要購読"
        title = r["title"].rstrip(".")
        lines_md.append(
            f"| {n} | {title} | {pmid} | {r['journal']} {r['year']} | {oa} | {why} |")
        rows.append({"n": n, "chapter": chapter, "pmid": pmid,
                     "title": title, "journal": r["journal"], "year": r["year"],
                     "doi": r["doi"], "pmc": r["pmc"],
                     "first_author": r["authors"][0] if r["authors"] else "",
                     "reason": why})

if missing:
    print("!! PMIDs absent from harvested metadata:", missing)

with open(os.path.join(HERE, "md", "download_list.md"), "w") as f:
    f.write("\n".join(lines_md) + "\n")
with open(os.path.join(OUT, "download_list.json"), "w") as f:
    json.dump(rows, f, indent=1, ensure_ascii=False)

oa = sum(1 for r in rows if r["pmc"])
print(f"selected {len(rows)} papers | open access {oa} | subscription {len(rows)-oa}")
print("wrote md/download_list.md and corpus/download_list.json")
