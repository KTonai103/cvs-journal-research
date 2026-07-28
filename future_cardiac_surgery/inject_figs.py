#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert the harvested OA figures into the integrated review .md (house style).

House style follows af_surgical_ablation/md/AF_surgical_ablation_review.md:
inline <figure>/<figcaption> HTML blocks in the Markdown, which convert_to_html.py
passes through verbatim. Captions state what the reader can VERIFY in the image.

Rights policy for this repository (established in the AF review):
  - Only CC BY / CC BY-NC / CC BY-NC-ND originals, unmodified.
  - Third-party figures reproduced inside an OA article are excluded.
  - JACC-family and BMJ-family figures are NOT used.  → the Ozaki原典 (JACC Adv 2025)
    and the TEHV calcification Central Illustration (JACC Basic Transl Sci) are absent
    for that reason, and the text says so.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(BASE, "md", "FutureOfValveSurgery_integrated_review.md")
FD = "figures"

IMGSTYLE = 'style="width:100%;border-radius:8px;border:1px solid #e3e3e3;"'
CAPSTYLE = ('style="font-size:12px;color:#5b6673;margin:6px auto 0;'
            'line-height:1.7;text-align:left;"')

SRC = {
 "govers":  ("Govers PJ, et al. <i>Eur J Cardiothorac Surg</i> 2026;68(6):ezag177.",
             "10.1093/ejcts/ezag177", "42178209", "CC BY 4.0"),
 "aviator": ("Arabkhani B, Klautz RJM, de Heer F, et al. <i>Eur J Cardiothorac Surg</i> 2023;63(2):ezac514.",
             "10.1093/ejcts/ezac514", "36308450", "CC BY-NC 4.0"),
 "avp":     ("Arabkhani B, Sandker SC, Braun J, et al. <i>Eur J Cardiothorac Surg</i> 2023;64(5):ezad291.",
             "10.1093/ejcts/ezad291", "37610333", "CC BY 4.0"),
 "sarnaik": ("Sarnaik KS, et al. <i>JTCVS Open</i> 2024;17:185-214.",
             "10.1016/j.xjon.2023.10.033", "38420529", "CC BY-NC-ND 4.0"),
 "dph20":   ("Sarikouch S, Boethig D, Avsar M, et al. <i>Eur J Cardiothorac Surg</i> 2026;68(2):ezag087.",
             "10.1093/ejcts/ezag087", "41652890", "CC BY-NC 4.0"),
 "arise":   ("Horke A, Tudorache I, Laufer G, et al. <i>Eur J Cardiothorac Surg</i> 2024;65(4):ezae121.",
             "10.1093/ejcts/ezae121", "38532304", "CC BY 4.0"),
 "decell10":("Sarikouch S, Horke A, Tudorache I, et al. <i>Eur J Cardiothorac Surg</i> 2016;50(2):281-290.",
             "10.1093/ejcts/ezw050", "27013071", "CC BY 4.0"),
 "xeltis":  ("Morales DL, Herrington C, Bacha EA, et al. <i>Front Cardiovasc Med</i> 2020;7:583360.",
             "10.3389/fcvm.2020.583360", "33748192", "CC BY 4.0"),
 "shf":     ("Kasahara S, Yoshimura Y, Ichikawa H, et al. <i>Ann Thorac Surg Short Rep</i> 2024;2(4):804-809.",
             "10.1016/j.atssr.2024.04.020", "39790580", "CC BY-NC-ND 4.0"),
 "avneo":   ("Prinzing A, Boehm J, Burri M, et al. <i>JTCVS Tech</i> 2024;25:35-42.",
             "10.1016/j.xjtc.2024.02.011", "38899113", "CC BY-NC-ND 4.0"),
 "jsmics":  ("Shimokawa T, Kumamaru H, Motomura N, et al. <i>Gen Thorac Cardiovasc Surg</i> 2026;74(5):510-517.",
             "10.1007/s11748-025-02225-z", "41417160", "CC BY 4.0"),
}

# n, file, src key, alt, bold title, body html
FIGS = [
 (1, "fv_jp_mics_volume_dist_PMC13139202.jpg", "jsmics",
  "日本のMICS僧帽弁手術の年間症例数の施設分布ヒストグラム",
  "日本のMICS僧帽弁手術は「年5例未満の施設」が最も多い",
  "JCVSD に登録された <b>242施設</b>の年間MICS-MV症例数分布。<b>中央値5.5例/年</b>、"
  "下位四分位2例、上位四分位14例、95パーセンタイル38例。"
  "0–5例/年の階級だけで<b>111施設</b>を占める。"
  "第10章で論じる「日本で volume 閾値を適用すると何が起きるか」を、そのまま数えた図。"),
 (2, "fv_govers_vo_longterm_PMC13282078.jpg", "govers",
  "VSARRの年間症例数と長期AV再介入回避生存のハザード比を結ぶ制限付き三次スプライン",
  "年12例で折れる — 長期のAV再介入回避生存",
  "VSARR 2,668例/37施設。縦軸は AV 再介入回避生存の <b>ハザード比</b>、横軸は年間症例数。"
  "円の大きさが施設規模。曲線は<b>年11–12例付近で HR 1.0 に達して以降は平坦</b>になり、"
  "elbow 法で導かれた閾値<b>年12例（95%CI 10–12）</b>がこの折れ点に対応する（P=.0023）。"),
 (3, "fv_govers_vo_early_PMC13282078.jpg", "govers",
  "VSARRの年間症例数と早期複合エンドポイントの関係を示す平坦な回帰直線",
  "早期成績は症例数に鈍感（P=.8003）",
  "同じコホートの<b>早期複合エンドポイント</b>（30日死亡・血栓塞栓・再介入・術中conversion・AR≥2度）。"
  "直線はほぼ水平で信頼区間も広い。<b>イベント率が2–5%と低すぎて症例数の差を検出できない</b>という構造が見える。"
  "「早期成績が良いから集約は不要」という主張が成立しないのは、この図が示す通り"
  "<b>早期成績では差が測れない</b>からである。"),
 (4, "fv_aviator_survival_PMC9942544.jpg", "aviator",
  "AVIATORのVSRRとCVG-ARRの全生存Kaplan-Meier曲線とat risk例数表",
  "AVIATOR：生存差はつくが、at risk が急速に減る",
  "PSM 3:1 後の 654 vs 218例。5年生存 <b>95.4% vs 85.4%</b>。"
  "下の at risk 表を見ると <b>8年時点で VSRR 57例・CVG 21例</b>まで落ちており、"
  "曲線の後半は少数例に依存している。"
  "なお本論文は同じ比較の p 値を<b>抄録・本文で P=0.002、この Figure 2A で p=0.01</b> と"
  "表記しており（本文の5年生存も 85.4%/84.4% と2通り）、点推定の扱いには注意が必要である。"),
 (5, "fv_aviator_reint_PMC9942544.jpg", "aviator",
  "AVIATORの大動脈基部再介入回避のKaplan-Meier曲線、P=0.98",
  "AVIATOR：再介入回避には差がない（P=0.98）",
  "同じコホートの<b>基部再介入回避</b>。5年で <b>96.8% vs 95.4%、P=0.98</b>。"
  "生存に10ポイントの差がつくのに再介入が同等であるという組み合わせは、"
  "<b>生存差が弁関連機序では説明しづらい</b>ことを意味する。"
  "本文で残余交絡を疑うべきと述べた根拠がこの2枚の対比である。"),
 (6, "fv_avp_device_view_PMC10903180.jpg", "avp",
  "術中加圧可視化deviceで大動脈弁を内視鏡で直視しているモニタ画像と術野写真",
  "術中加圧可視化device の実像（n=24・単群）",
  "左：加圧下（60–80 mmHg）に内視鏡で見た大動脈弁の閉鎖。右：術野での device 装着。"
  "24例中22例で術後AI ≤grade 1、漏れ中央値 <b>90 mL/分</b>（IQR 60–120）、"
  "3例で追加調整・2例で弁置換（残存AI 330・260 mL/分）。"
  "<b>対照群がないため「安全そう」までしか言えない</b>段階の技術である"
  "（かつシードEditorialの責任著者自身の開発品）。"),
 (7, "fv_ross_vs_mavr_surv_PMC10897596.jpg", "sarnaik",
  "18歳患者を想定したRossと機械弁AVRのmicrosimulation生存曲線",
  "18歳モデルの60年：Ross と機械弁の生存曲線",
  "Markov 決定木＋20,000回 Monte Carlo。10,000人の仮想コホートで、"
  "60年後に生存しているのは Ross 約5,900人 vs 機械弁約4,600人。"
  "20年死亡は <b>16.3% vs 23.2%</b>、生涯 QALY <b>28.3 vs 23.5</b>、費用 <b>$54,233 vs $507,240</b>。"
  "<b>これはモデルであって観察データではない</b>——入力した遷移確率がそのまま結論を決める点に注意。"),
 (8, "fv_dph20_freedom_PMC13017825.jpg", "dph20",
  "脱細胞化肺homograft 310例の死亡・explant・心内膜炎・狭窄・逆流回避のKaplan-Meier曲線6枚",
  "脱細胞化肺homograft 20年：上段は良好、下段が落ちる",
  "310例。上段（死亡・explantation・心内膜炎）の回避は20年で<b>96.9% / 85.2% / 91.0%</b>と良好。"
  "しかし下段の<b>狭窄回避・逆流回避・その複合</b>は下がり続け、"
  "15年で狭窄回避 <b>68.3%</b>・≥中等度逆流回避 <b>65.1%</b>、そして<b>20年で 0</b> に達する。"
  "各パネル下の at risk（310→210→101→31→4）が示す通り、20年時点の症例は少数である。"),
 (9, "fv_dph20_function_PMC13017825.jpg", "dph20",
  "explant回避曲線に年次ごとのconduit機能状態を色分けした棒を重ねた図",
  "「壊れていないが機能していない弁」が20年で全部になる",
  "同じ310例。黒い曲線が explantation 回避（20年 85.2%）、"
  "棒は各年の<b>conduit の機能状態</b>——白=intact、緑=≥中等度逆流、黄=圧較差50 mmHg（狭窄）、"
  "赤=狭窄＋逆流、灰=intervention後。"
  "<b>16年以降で白（intact）が消え、18–20年は緑と赤だけになる</b>。"
  "「再手術率で耐久性を測ると壊れている弁が見えなくなる」（第9章）の実例がこの1枚である。"),
 (10, "fv_arise_explant_PMC11009017.jpg", "arise",
  "ARISE 144例と全DAH 358例のexplant回避曲線と弁機能状態",
  "ARISE：144例（上）と全DAH 358例（下）の explant 回避",
  "上＝前向き試験の144例（追跡は7年で尽きる）。下＝<b>登録全体の358例</b>で、"
  "曲線は<b>9–10年で約70%まで落ちる</b>（本文の 5年92.4%→10年<b>69.5%</b>）。"
  "at risk は 358→131（5年）→58（7年）→27（10年）→5（11年）。"
  "Squiers/Brinkman が「凍結保存homograftの過去成績ときわめて整合的」と評したのはこの下段の曲線である。"),
 (11, "fv_decell10_vs_ch_bjv_PMC4951634.jpg", "decell10",
  "脱細胞化肺homograft・凍結保存homograft・bovine jugular veinのexplant回避と機能状態の比較",
  "10年時点では脱細胞化が明確に勝っていた（2016年の比較）",
  "年齢・病型・手術歴でマッチした各93例。左列＝explantation 回避、右列＝explantation＋intervention 回避。"
  "10年で <b>DPH 100% / 凍結保存 84.2% / BJV 84.3%</b>（右列は 85.3% / 79.1% / 65.2%）。"
  "灰色の帯（dysfunctional）が DPH で小さいことも読み取れる。"
  "<b>この2016年の図と、20年後の図8–9を並べると、「10年では勝ち、20年では機能が尽きる」</b>"
  "という本章の結論がそのまま見える。"),
 (12, "fv_shf_structure_PMC11708634.jpg", "shf",
  "合成ハイブリッド生地の構造図と、イヌ大動脈における1・6・36か月の組織像",
  "シンフォリウム：構造と、36か月までの組織置換",
  "(A) 生分解性の<b>PLLA</b>糸と非分解性の<b>PET</b>糸の経編に<b>架橋ゼラチン</b>膜を一体化した構造。"
  "(B) イヌ大動脈での前臨床：1か月ではゼラチンとPLLA/PETが見え、6か月で bridging tissue、"
  "<b>36か月では内膜に内皮細胞層ができ、PET束の残存のみになる</b>。"
  "(C) 引張試験で patch 植込み部が native と同等域の伸展性を示す。"
  "in situ 組織再生を狙った心血管材料で<b>薬事承認まで到達した唯一に近い例</b>（2023-07承認/2024-06発売）。"),
 (13, "fv_shf_sites_PMC11708634.jpg", "shf",
  "34例41部位のシンフォリウム植込み部位の解剖図と術野写真",
  "34例41部位の内訳（弁ではなくパッチである）",
  "(A) 植込み部位：<b>主肺動脈14・分枝肺動脈4（＝肺動脈計18）・RVOT 12・心房中隔7・心室中隔4＝41部位</b>。"
  "(B) 実際の術野。年齢中央値1歳11か月、追跡中央値40か月で手術成功率100%・重篤有害事象なし。"
  "<b>この図が示す通り対象はパッチ適用部位であり、弁尖ではない</b>——"
  "本文で E2 に留めた理由がここにある。"),
 (14, "fv_xeltis_pi_histogram_PMC7969645.jpg", "xeltis",
  "Xeltis XPVの肺動脈弁逆流グレードの頻度分布（7日・6か月・12か月）",
  "Xeltis XPV：第1世代で重度PIが積み上がる",
  "group 1＝XPV-1（12例）、group 2＝設計変更後のXPV-2（6例）。"
  "7日目は両群とも None/Trace/Mild に収まるが、"
  "<b>12か月で group 1 は Moderate 6例・Severe 5例に移動し、group 2 は Moderate 1例のみ</b>。"
  "「弁尖 prolapse による逆流」が設計の問題であったことを、この3枚の推移が示している。"),
 (15, "fv_xeltis_explant_PMC7969645.jpg", "xeltis",
  "摘出されたXeltis XPV conduitの下流側・上流側の実物写真",
  "摘出された XPV conduit の実物",
  "左＝肺動脈側から、右＝右室側から見た摘出 conduit。"
  "弁尖は保たれているが commissure に軽度の変化がある。"
  "スケール（cm定規）が入っており、<b>「生分解して自己組織に置き換わる」という設計意図と、"
  "実際に取り出された物体を突き合わせられる</b>数少ない画像である。"),
 (16, "fv_avneo_gradients_PMC11184442.jpg", "avneo",
  "AVNeo 162例のピーク圧較差・平均圧較差・EOAの経時変化",
  "AVNeo の血行動態は5年まで安定している",
  "162例（平均52.6±16.6歳、二尖弁81.5%）。退院時 ピーク/平均 <b>15.6 / 8.4 mmHg</b>・EOA 2.4±0.8 cm²、"
  "5年でも <b>14.5 / 7.5 mmHg</b>・EOA 2.3±0.8 cm²。"
  "Ozaki 手術の最大の強みが<b>圧較差の低さとその安定性</b>であることは、この3枚で確認できる。"),
 (17, "fv_avneo_svd_cuminc_PMC11184442.jpg", "avneo",
  "AVNeo 162例の中等度SVD・重度SVD・心内膜炎・bioprosthetic valve failureの累積発生率",
  "AVNeo の5年：SVD と bioprosthetic valve failure",
  "競合リスクによる累積発生率。5年で <b>中等度SVD 9.82%±3.87・重度SVD 6.96%±3.71・"
  "bioprosthetic valve failure 12.1%±4.12</b>、心内膜炎も立ち上がる。"
  "各パネル下の at risk が <b>162→24（5年）→1（5.5年）</b>と落ちるため、"
  "5年時点の信頼区間（陰影）が急に広がっていることも読み取れる——"
  "<b>点推定ではなく区間を見るべき</b>典型例（第9章）。"),
]

# figure number -> insert-before anchor (must occur exactly once)
ANCHORS = {
 1:  "## エビデンス格付け（第2章）",
 2:  "この論文の意義は、**2025 ESC/EACTS ガイドラインが意図的に数値を出さなかった空白を埋めている**点にある。",
 4:  "**Reimplantation vs remodelling。**",
 6:  "さらに De Paulis 総説からは、Editorial に書かれていない**2つの重要な実務情報**が得られた。",
 7:  "## 5.2 ガイドラインとの乖離を原文で確認する",
 8:  "## 6.2 大動脈位（ARISE、シードref[6]）と、その論評",
 10: "## 6.3 著者自身が書いた限界（これが最も重い）",
 12: "## 7.2 in situ 型の唯一の成功例は「弁ではなくパッチ」で、それは日本製である",  # placeholder, fixed below
 14: "## 7.3 ex vivo 型：石灰化という共通の壁",
 16: "## 8.4 Ozaki への最も鋭い反証は、De Paulis 総説の一文である",
}
ANCHORS[12] = "## 7.2 in situ 型の「弁」：Xeltis の10年"
PAIRS = {2: [2, 3], 4: [4, 5], 8: [8, 9], 10: [10, 11], 12: [12, 13], 14: [14, 15], 16: [16, 17]}


def figure_html(n, single):
    _, fn, key, alt, title, body = next(f for f in FIGS if f[0] == n)
    ref, doi, pmid, lic = SRC[key]
    width = 'style="margin:18px 0;max-width:680px;"' if single else 'style="margin:0;"'
    return (
        f'<figure {width}>\n'
        f'<img src="{FD}/{fn}" alt="{alt}" {IMGSTYLE}>\n'
        f'<figcaption {CAPSTYLE}><b>図 {n}. {title}</b> — {body}<br>'
        f'<i>出典: {ref} <a href="https://doi.org/{doi}">doi:{doi}</a> / '
        f'<a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/">PubMed</a>. {lic}（原図を改変せず掲載）。</i>'
        f'</figcaption>\n</figure>\n')


def block(nums):
    if len(nums) == 1:
        return figure_html(nums[0], True) + "\n"
    inner = "".join(figure_html(n, False) for n in nums)
    return ('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));'
            'gap:16px;margin:18px 0;">\n' + inner + '</div>\n\n')


def main():
    t = open(MD, encoding="utf-8").read()
    if "figures/fv_" in t:
        sys.exit("figures already injected — aborting")
    for first, anchor in sorted(ANCHORS.items()):
        nums = PAIRS.get(first, [first])
        if t.count(anchor) != 1:
            sys.exit(f"anchor not unique ({t.count(anchor)}): {anchor[:60]}")
        t = t.replace(anchor, block(nums) + anchor)
    open(MD, "w", encoding="utf-8").write(t)
    print(f"injected {len(FIGS)} figures at {len(ANCHORS)} anchors")


if __name__ == "__main__":
    main()
