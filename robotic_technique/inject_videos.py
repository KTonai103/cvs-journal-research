#!/usr/bin/env python3
"""Insert operative-video links into md/robotic_technique_review.md.

Two shapes, following ross_technique/:

  figure.vfig   a clickable thumbnail with a ▶ badge.  Only used where the
                publisher distributes a video poster image under a CC licence
                (Ann Cardiothorac Surg "Masters of Cardiothoracic Surgery"
                posters, CC BY-NC-ND 4.0, harvested from the PMC OA package).
  div.videolist a plain link list, used for MMCTS and for the pre-2019 ACS
                articles, whose poster images carry no CC licence.

No frame is ever grabbed from a video: thumbnails are the publisher's own
poster images.  Idempotent — re-running replaces the previously injected
blocks.  Every MMCTS id below was verified against the site catalogue
(mmcts.org/search returns the Inertia payload with id/type/doi/duration),
because DOI redirection is not reliable — 10.1510/mmcts.2025.098 resolves to
tutorial/2069, which is a different article.
"""
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
MD = os.path.join(HERE, "md", "robotic_technique_review.md")
SRC_DIR = os.path.join(HERE, "figures", "video")
PUB_DIR = os.path.join(REPO, "output", "figures")
PREFIX = "rtv_"

BEGIN = "<!-- VID:{} -->"
END = "<!-- /VID:{} -->"

ACS_LIC = "CC BY-NC-ND 4.0"


def mm(kind, num):
    return f"https://mmcts.org/{kind}/{num}"


def dur(sec):
    return f"{sec // 60}分{sec % 60:02d}秒"


# --- items -------------------------------------------------------------------
# ("fig", thumbnail, w, h, title, body, url, cite)
# ("mm",  title, who, kind, num, seconds, body)
# ("web", title, who, url, label, body)

V = {
 "1.1": [
  ("mm", "Closed-chest, robotically assisted CABG", "Falk V, Jacobs S, Mohr FW, MMCTS 2006",
   "tutorial", 621, 727,
   "現在の TECAB の原型。31ステップに刻まれており、LITA の筋膜切開・pedicle 作成から "
   "silastic tape による標的血管の一時遮断、安定化器の挿入、吻合と結紮までを通して見られる。"
   "2004年の映像で、器械も画質も現在とは違うが、<b>工程そのものは今と変わっていない</b>ことが確認できる。"),
 ],

 "2.3": [
  ("mm", "体位・マーキング・ポート配置（男性）", "Cullen P, Malas T, Gillinov M, MMCTS 2025",
   "tutorial", 2069, 605,
   "マーキングと体位 → 大腿露出 → working port → angiocath 留置と横隔膜牽引 → 完成したセットアップ、の5工程。"),
  ("mm", "体位・マーキング・ポート配置（女性）", "Cullen P, Malas T, Gillinov M, MMCTS 2025",
   "tutorial", 2068, 449,
   "乳房下縁の扱いが男性版と違う。同じ術者・同じ構成で撮られているので差分が分かりやすい。"),
  ("mm", "心膜切開と大動脈遮断鉗子の当て方", "Cullen P, Malas T, Gillinov M, MMCTS 2025",
   "tutorial", 2067, 244,
   "体位・ポートの次の工程。"),
 ],

 "2.4": [
  ("mm", "僧帽弁のポート配置", "Cullen P ら, MMCTS 2025", "tutorial", 2069, 605, ""),
  ("mm", "RAVR のポート配置", "Arai A, Kitahara H, Balkhy HH, MMCTS 2024",
   "case-report", 1915, 328,
   "「operation set-up and port placement」が第2章に立っている。"),
  ("mm", "TECAB のポート配置と EndoWrist stabilizer の入れ方",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2023", "case-report", 1834, 482,
   "第4章が stabilizer と working port の位置決めに充てられている。"),
  ("mm", "RA-MIDCAB のポート配置", "Catalano M, Kelly J ら, MMCTS 2025",
   "tutorial", 2030, 728, "第2章がポート配置。"),
 ],

 "2.5": [
  ("mm", "ロボット心臓手術における片側経皮送脱血と endoaortic balloon の管理",
   "Amabile A, Hameed I ら, MMCTS 2022", "tutorial", 1717, 554,
   "Perclose Proglide を動静脈それぞれに先行留置してから穿刺送脱血する手順と、"
   "バルーン閉塞・脱血の全工程。本レビューが扱わない CPB 側は "
   '<a href="robotic_cpb_pitfalls_review.html">ロボット支援下CPB Pitfallレビュー</a>を参照。'),
  ("mm", "低侵襲僧帽弁手術における endoaortic balloon occlusion",
   "Van Praet KM, Kempfert J ら, MMCTS 2022", "tutorial", 1724, 1038,
   "バルーン単体を17分かけて扱った長編。移動・破裂・解離という争点の背景が分かる。"),
  ("web", "Robotic posterior bar decalcification and mitral repair in mitral annular calcification",
   "Loulmet DF, Hage A ら", "https://doi.org/10.21037/acs-2025-mac-19",
   "Ann Cardiothorac Surg 2025;14(6) の動画",
   "上表「重症MACはロボットでやるか」の NYU 側の実演。"),
 ],

 "3.3": [
  ("mm", "内視鏡下僧帽弁形成のための suturing map", "Sardari Nia P, Olsthoorn J, MMCTS 2018",
   "tutorial", 1041, 214,
   "high-fidelity シミュレータ上で、<b>弁輪のどの位置に針をどの向きで入れるか</b>を "
   "map として示す。訓練の初期に見るべき1本。"),
  ("mm", "内視鏡下僧帽弁置換の suture map", "Hamid UI, Sardari Nia P, MMCTS 2022",
   "tutorial", 1742, 370,
   "弁輪サイジングから人工弁の運針まで9工程。"),
  ("mm", "内視鏡下三尖弁形成の suture map", "Hamid UI, Aksoy R, MMCTS 2022",
   "tutorial", 1741, 557, "右房切開から弁輪縫縮まで。"),
  ("mm", "低忠実度シミュレータの作り方", "Moscarelli M ら, MMCTS 2019", "tutorial", 1267, 350,
   "低侵襲僧帽弁手術用の簡易シミュレータを自作する手順。"
   "<a href=\"#33-phase-i--チーム作りとシミュレーション\">3.3節</a>の「安価な箱から始める」の実物。"),
 ],

 "4.1": [
  ("fig", "36237587_acs-11-05-548-vid.jpg", 569, 320,
   "経乳輪（periareolar）アプローチ",
   "Musumeci らの乳輪切開。ポート配置の項で扱った「創をどこに置くか」の"
   "美容面での解の一つ。",
   "https://doi.org/10.21037/acs-2022-rmvs-12",
   "Musumeci F, Ranocchi F, et al. <i>Ann Cardiothorac Surg</i> 2022;11(5):548-549"),
  ("mm", "ロボット経乳輪僧帽弁形成", "Musumeci F, Lio A, MMCTS 2021",
   "tutorial", 1644, 412,
   "皮膚マーキング → 切開 → トロッカー挿入 → ロボット接続まで10工程。上の ACS 動画の詳細版。"),
 ],

 "4.3": [
  ("fig", "36483616_acs-11-06-629-vid.jpg", 569, 320,
   "完全内視鏡下ロボット僧帽弁形成の全工程",
   "Thomas Jefferson の Yost / Guy による "
   "「How I perform totally endoscopic robotic mitral valve repair」。"
   "1本で一連の流れが通して見られる標準的な症例。",
   "https://doi.org/10.21037/acs-2022-rmvs-16",
   "Yost CC, Rosen JL, et al. <i>Ann Cardiothorac Surg</i> 2022;11(6):629-631"),
  ("fig", "36483614_acs-11-06-583-vid.jpg", 569, 320,
   "難易度が上がっても質を落とさない形成",
   "WVU の Darehzereshki / Mehaffey による "
   "「maintaining quality at all levels of complexity」。"
   "<a href=\"#43-弁形成手技--術式を変えないことが原則\">4.3節</a>の「術式を変えない」という原則の実演。",
   "https://doi.org/10.21037/acs-2022-rmvs-27",
   "Darehzereshki A, Mehaffey JH, et al. <i>Ann Cardiothorac Surg</i> 2022;11(6):583-588"),
  ("mm", "三角切除", "Cullen P, Malas T, Gillinov M, MMCTS 2025", "tutorial", 2070, 346,
   "TOE 所見 → 左房切開 → 弁の評価 → 三角切除と縫合 → 弁輪縫縮と saline test → 左房閉鎖 → 修復後TOE。"),
  ("mm", "folding plasty（折り込み形成）", "Cullen P ら, MMCTS 2025", "tutorial", 2112, 407,
   "三角切除に folding plasty を足す8工程。cleft 閉鎖と再テストまで含む。"),
  ("mm", "annular plication（弁輪縫縮を併せた後尖形成）", "Cullen P ら, MMCTS 2025",
   "tutorial", 2116, 357, "P2 三角切除 → 弁輪縫縮 → 弁尖閉鎖 → 弁輪形成と passive test。"),
  ("mm", "commissuroplasty（交連形成）", "Cullen P ら, MMCTS 2025", "tutorial", 2107, 200,
   "同シリーズで最も短い3工程。"),
  ("mm", "四角切除＋双方向 sliding valvuloplasty", "Cullen P ら, MMCTS 2025",
   "tutorial", 2109, 597, "同シリーズで最も大きな弁尖処理。"),
  ("mm", "sliding plasty＋人工腱索＋弁輪縫縮（複雑形成）",
   "Amabile A, LaLonde MR ら, MMCTS 2023", "case-report", 1787, 343,
   "Yale の症例。後尖切除→人工腱索→弁輪縫縮を1本で。"),
  ("mm", "anomalous mitral arcade に対する3D完全内視鏡下形成",
   "Kitamura H, Fukumoto Y, MMCTS 2025", "case-report", 1985, 328,
   "乳頭筋剥離 → 人工腱索長の決定 → loop 固定 → 交連形成まで10工程。稀な病態の形成戦略。"),
  ("mm", "sliding leaflet valvuloplasty と remodelling partial annuloplasty",
   "Murashita T, Raffa G, MMCTS 2016", "tutorial", 530, 313,
   "びまん性粘液腫様変性の2症例を対比。"),
  ("mm", "ロボット僧帽弁形成の手技・成績・展望", "Algarni KD, Suri RM, MMCTS 2014",
   "tutorial", 60, 606,
   "Mayo の Suri による9工程。後尖・交連・前尖（人工腱索）の順に扱う古典。"),
  ("web", "Optimizing outcomes of robotic mitral valve repair for all prolapse anatomy: the Suri-Burkhart technique",
   "Suri RM, Burkhart HM", "https://doi.org/10.3978/j.issn.2225-319X.2013.10.05",
   "Ann Cardiothorac Surg 2013;2(6):841-845 の動画", ""),
  ("web", "Robotic mitral valve repair: algorithmic approach in degenerative mitral valve disease",
   "Javadikasgari H, Suri RM", "https://doi.org/10.21037/acs.2016.11.07",
   "Ann Cardiothorac Surg 2016;5(6):586-588 の動画", ""),
  ("web", "Robotic mitral valve repair: standardized repair strategy ensures consistent results",
   "Ishii H, Ting M", "https://doi.org/10.21037/acs.2018.10.11",
   "Ann Cardiothorac Surg 2018;7(6):837-838 の動画", ""),
 ],

 "4.4": [
  ("mm", "semi-continuous 3本縫合による弁輪縫縮", "Cullen P, Malas T, Gillinov M, MMCTS 2025",
   "tutorial", 2077, 552,
   "<a href=\"#44-弁輪縫縮--robotic-特有の工夫が最も進んだ領域\">4.4節</a>で扱った手技の原典動画。"),
  ("mm", "人工弁の運針（内視鏡下MVR の suture map）", "Hamid UI, Sardari Nia P, MMCTS 2022",
   "tutorial", 1742, 370, "弁輪サイジングと運針順序。"),
  ("mm", "Cor-Knot による結紮を含むロボットMVR", "Senay S, Gullu AU, MMCTS 2014",
   "tutorial", 54, 332,
   "第6工程が Cor-Knot での締結。自動ファスナーの合併症は"
   '<a href="cor_knot_pitfalls_review.html">Cor-Knot Pitfallレビュー</a>を参照。'),
 ],

 "4.5": [
  ("fig", "41383200_acs-14-06-511-vid1.jpg", 569, 320,
   "MAC 症例のロボット僧帽弁形成",
   "石灰化弁輪でどこまで踏み込むかを示した2025年の動画。",
   "https://doi.org/10.21037/acs-2025-mac-0127",
   "Pickering T, Dorton CW, et al. <i>Ann Cardiothorac Surg</i> 2025;14(6):511-513"),
  ("fig", "41383187_acs-14-06-504-vid.jpg", 569, 320,
   "posterior bar の広範囲脱灰と calcific emulsification",
   "Western Ontario の Chu ら。<b>石灰を乳化させて除去する</b>新法で、"
   "内視鏡下でも posterior bar を処理できるとする。"
   "<a href=\"#25-意見が分かれる点\">2.5節</a>の「重症MACをロボットでやるか」の争点に直結する。",
   "https://doi.org/10.21037/acs-2025-mac-10",
   "Rheault-Henry M, Chu MWA, et al. <i>Ann Cardiothorac Surg</i> 2025;14(6):504-507"),
  ("fig", "36237590_acs-11-05-545-vid.jpg", 569, 320,
   "弁輪石灰化の完全切除を伴うロボット形成",
   "NYU の Naito / Grossi。石灰を残さず取り切る側の立場。",
   "https://doi.org/10.21037/acs-2022-rmvs-64",
   "Naito N, Grossi EA, et al. <i>Ann Cardiothorac Surg</i> 2022;11(5):545-547"),
  ("mm", "内視鏡下手術中の SAM への対処", "Buttiglione G, Gollmann-Tepeköylü C, MMCTS 2024",
   "tutorial", 1934, 332,
   "2症例を並べて、弁の所見 → 到達法 → SAM の処理、をそれぞれ示す。"),
  ("mm", "両側乳頭筋移動（double papillary muscle relocation）",
   "Amabile A, LaLonde MR ら, MMCTS 2022", "case-report", 1757, 418,
   "乳頭筋頭の再固定から移動、弁輪縫縮での位置決めまで7工程。"),
  ("mm", "前回の乳頭筋接合が破綻した症例の再手術",
   "Amabile A, Antonios J ら, MMCTS 2024", "case-report", 1943, 330,
   "完全内視鏡下での再手術。乳頭筋位置の再建 → 弁輪縫縮 → 交連縫縮。"),
  ("mm", "TEER クリップ抜去を伴うロボット僧帽弁再形成",
   "Kaneyuki D, Yost CC, MMCTS 2023", "case-report", 1837, 399,
   "endoballoon 遮断・PFO 閉鎖・左房 CryoMAZE・左心耳閉鎖まで併施した1本。"),
  ("mm", "部分型房室中隔欠損修復後の再手術（内視鏡下僧帽弁形成）",
   "Arimura S, Chu MWA, MMCTS 2025", "case-report", 2058, 386,
   "cleft を 4-0 Gore-Tex で閉じ直す工程が独立章になっている。"),
  ("mm", "再手術：癒着剥離（前回正中×2・前回ロボット×1）＋複雑再形成",
   "Amabile A, LaLonde MR ら, MMCTS 2022", "case-report", 1766, 574, ""),
 ],

 "4.6": [
  ("web", "Complications and their management in robotic mitral valve surgery from the surgical assistant's perspective",
   "Patel NC, Macoskey AR ら", "https://doi.org/10.21037/acs-2022-rmvs-15",
   "Ann Cardiothorac Surg 2022;11(5):510-524",
   "助手の視点から合併症とその対処を網羅した15ページの総説（動画なし・本文のみ）。"
   "本節の Pitfall と対応させて読むとよい。"),
 ],

 "5.2": [
  ("mm", "縫着型生体弁によるロボット完全内視鏡下AVR",
   "Arai A, Kitahara H, Balkhy HH, MMCTS 2024", "case-report", 1915, 328,
   "セットアップとポート配置 → 遮断・大動脈切開 → 弁切除 → 人工弁植込み → 終了まで6工程。"
   "<b>rapid deployment 弁ではなく通常の縫着弁</b>で行った版。"),
  ("mm", "rapid deployment 弁による完全内視鏡下AVR＋僧帽弁形成",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2025", "tutorial", 2059, 419, ""),
  ("mm", "機械弁によるロボットAVR", "Morales-Rey I, Sandoval E, MMCTS 2026",
   "tutorial", 2132, 778,
   "Barcelona。小切開＋トロッカー＋大腿送脱血、経胸壁遮断＋順行性晶質液心筋保護、"
   "大動脈切開の<b>2層閉鎖</b>まで8工程。"),
 ],

 "5.3": [
  ("mm", "弁の種類ごとの tips and tricks（完全内視鏡下AVR）",
   "Danesi TH, MMCTS 2023", "tutorial", 1800, 947,
   "内視鏡下AVRの難所を整理したうえで、<b>sutureless / rapid deployment / stented / 機械弁</b>の"
   "4通りを弁種別に扱う。遮断と大動脈切開の tips が独立章にある。"),
  ("mm", "完全内視鏡下 micro-invasive AVR", "Bakhtiary F, Salamate S, MMCTS 2024",
   "tutorial", 1876, 657,
   "右前小開胸と中腋窩到達の2通りを示し、<b>RAM デバイスを使う版と使わない版</b>を並べる11工程。"),
  ("mm", "SAVR 後さらに TAVR を受けた症例の完全内視鏡下AVR（TAVR explant）",
   "Van Genechten S, Hillen W, MMCTS 2025", "case-report", 2021, 612,
   "癒着剥離 → LITA の一時遮断 → 大動脈切開 → <b>TAVR 抜去 → 旧SAVR弁抜去 → 基部デブリードマン</b> → "
   "Perceval 植込み、の12工程。<a href=\"#58-まだ埋まっていない穴\">5.8節</a>で抄録のみ引用した領域の実映像。"),
 ],

 "5.4": [
  ("fig", "40547430_acs-14-03-238-vid1.jpg", 640, 360,
   "RAVR＋大動脈基部拡大（modified Nicks）",
   "WVU の Darehzereshki / Wei。至適な人工弁サイズを得るための基部拡大を"
   "ロボットで行った3症例。",
   "https://doi.org/10.21037/acs-2024-ravr-0183",
   "Darehzereshki A, Wei L, et al. <i>Ann Cardiothorac Surg</i> 2025;14(3):238-240"),
  ("fig", "40547425_acs-14-03-241-vid.jpg", 569, 320,
   "RAVR＋中隔心筋切除の同時手術",
   "大動脈弁側から心室中隔筋切除を併施する。"
   "<a href=\"#84-中隔心筋切除--2つの到達路\">8.4節</a>の経大動脈路の RAVR 版にあたる。",
   "https://doi.org/10.21037/acs-2024-ravr-0186",
   "Pickering T, Dorton C, et al. <i>Ann Cardiothorac Surg</i> 2025;14(3):241-243"),
 ],

 "6.2": [
  ("mm", "RA-MIDCAB — 準備・グラフト採取・吻合", "Catalano M, Kelly J ら, MMCTS 2025",
   "tutorial", 2030, 728,
   "体位とポート → <b>第3〜6肋間の cryoablation とリポソーム型局所麻酔薬</b> → 後方心膜切開 → "
   "LIMA 採取 → 小開胸 → LIMA-LAD 吻合、の9工程。鎮痛まで含めて工程化されている点が有用。"),
  ("mm", "小開胸によるロボット支援MIDCAB — step-by-step",
   "Aerden A, Marynissen M, MMCTS 2022", "case-report", 1762, 1249,
   "同シリーズで最も長い。<b>shunt を用いた off-pump LIMA-LAD 吻合</b>と、"
   "肺門越しにグラフトが緊張しないかの確認まで示す。"),
  ("mm", "1枝病変に対するRA-MIDCAB", "Boulemden A, Pettinari M, MMCTS 2019",
   "tutorial", 1230, 399, "体位 → ポートとロボットアーム → LIMA 採取 → off-pump MIDCAB の4工程。"),
  ("mm", "ロボット支援 低侵襲多枝バイパス", "Arslanhan G, Özcan ZS, MMCTS 2024",
   "tutorial", 1871, 655,
   "<b>術前CTによる計画</b>を第2章に置く。ドッキング → LIMA 採取 → "
   "送脱血・小開胸・グラフト採取 → 遮断 → 標的血管展開 → 中枢・末梢吻合 → 流量測定。"),
  ("web", "Different styles in trocar placement in robotic-assisted beating heart coronary artery bypass grafting",
   "Algoet M, Balkhy HH ら", "https://doi.org/10.21037/acs-2023-rcabg-0209",
   "Ann Cardiothorac Surg 2024;13(5):458-460",
   "<a href=\"#62-ポート配置--ra-midcab-と-tecab-の違い\">6.2節</a>の流派の対比の原典。"),
 ],

 "6.3": [
  ("fig", "39434976_acs-13-05-455-vid.jpg", 569, 320,
   "内胸動脈の採取",
   "「How to robotically take down a mammary artery」。"
   "採取のみを1本にした動画で、初期学習の中心になる工程。",
   "https://doi.org/10.21037/acs-2023-rcabg-0189",
   "Newman JS, Lambert D, et al. <i>Ann Cardiothorac Surg</i> 2024;13(5):455-457"),
  ("mm", "bipolar micro forceps による skeletonize・クリップレス採取",
   "Arslan T, Heuts S, MMCTS 2025", "tutorial", 2062, 520,
   "到達 → ドッキングとターゲティング → <b>吻合予定部（landing zone）の評価</b> → "
   "内胸筋膜の切開 → 内側の剥離 → 側枝の処理 → 切離、の7工程。"
   "クリップを使わない側枝処理が主題。"),
  ("mm", "in-situ 両側内胸動脈を用いた off-pump 完全内視鏡下 hand-sewn CABG",
   "Hashimoto M, Ota T, MMCTS 2020", "tutorial", 1393, 1661,
   "RIMA・LIMA の採取をそれぞれ独立章で示す。両側採取の順序が分かる。"),
  ("mm", "胸腔鏡（非ロボット）による両側内胸動脈採取", "Akca F, MMCTS 2023",
   "tutorial", 1849, 457, "ロボットを使わない場合の比較対象。"),
  ("web", "Robotic-assisted bilateral internal thoracic artery harvest",
   "Sutter FP, Wertan MC", "https://doi.org/10.21037/acs.2018.06.12",
   "Ann Cardiothorac Surg 2018;7(5):704-706 の動画",
   "Lankenau の両側採取。"),
 ],

 "6.4": [
  ("fig", "39434978_acs-13-05-452-vid.jpg", 569, 320,
   "Cx 領域の展開",
   "pledget 付き Gore-Tex で下側壁を吊り上げて回旋枝領域を出す手技。"
   "<a href=\"#64-標的血管の展開\">6.4節</a>で扱った、後壁側にどう到達するかの原典動画。",
   "https://doi.org/10.21037/acs-2023-rcabg-12",
   "Bonatti J, Ashraf SF, et al. <i>Ann Cardiothorac Surg</i> 2024;13(5):452-454"),
  ("fig", "39157179_acs-13-04-385-vid.jpg", 569, 320,
   "心拍動下での LAD myocardial bridge unroofing",
   "冠動脈そのものではなく<b>心筋架橋の解除</b>をロボットで行った動画。"
   "標的血管の展開と剥離の難易度が伝わる。",
   "https://doi.org/10.21037/acs-2023-rcabg-0193",
   "Nisivaco S, Kitahara H, et al. <i>Ann Cardiothorac Surg</i> 2024;13(4):385-387"),
  ("mm", "多枝完全内視鏡下バイパス（RITA-LAD／LITA-PDA／LITA-OM sequential）",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2023", "case-report", 1834, 482,
   "両側内胸動脈採取 → stabilizer と working port → <b>標的血管の展開</b> → "
   "3本の吻合、の9工程。後壁側の到達がまとめて見られる。"),
  ("mm", "前回CABG後の右冠動脈への redo TECAB",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2023", "case-report", 1803, 316,
   "癒着剥離と RITA 採取からの再手術。"),
 ],

 "6.5": [
  ("fig", "39157189_acs-13-04-382-vid.jpg", 569, 320,
   "ロボットによる末梢吻合",
   "「How to perform distal anastomosis using a robotic platform」。"
   "本レビューで扱った吻合の要点（針の持ち替え・運針方向・結紮）が実際の映像で確認できる。",
   "https://doi.org/10.21037/acs-2023-rcabg-0211",
   "Bonatti J, Ashraf SF, et al. <i>Ann Cardiothorac Surg</i> 2024;13(4):382-384"),
  ("mm", "心拍動下 完全内視鏡下CABG", "Jansens JL, MMCTS 2011", "tutorial", 740, 315,
   "silastic loop の掛け方 → 冠動脈切開 → <b>coronary shunt 挿入</b> → 吻合 → shunt 抜去、"
   "の順が明示された10工程。"),
  ("web", "Robotic beating-heart totally endoscopic coronary artery bypass",
   "Melly L, Douglas D ら", "https://doi.org/10.21037/acs.2018.06.13",
   "Ann Cardiothorac Surg 2018;7(5):707-709 の動画", ""),
  ("web", "Robotic TECAB of the LAD and RCA system using an arterial Y-graft technique",
   "Bonatti J, Göbölös L ら", "https://doi.org/10.21037/acs.2018.06.10",
   "Ann Cardiothorac Surg 2018;7(5):700-703 の動画",
   "Y グラフトで2系統を賄う構成。"),
 ],

 "6.7": [
  ("fig", "39434971_acs-13-05-461-vid.jpg", 569, 320,
   "EndoWrist stabilizer を使わない TECAB",
   "GelPOINT Mini・AirSeal・Octopus Nuvo を組み合わせて "
   "<b>da Vinci Xi で EndoWrist stabilizer なしに</b>完全内視鏡下バイパスを成立させる。"
   "本節で述べた「安定化器が手に入らない」という外的制約への実際の回答。",
   "https://doi.org/10.21037/acs-2024-rcabg-0112",
   "Torregrossa G, Yakobitis A, et al. <i>Ann Cardiothorac Surg</i> 2024;13(5):461-463"),
 ],

 "7.2": [
  ("fig", "36237589_acs-11-05-543-vid1.jpg", 569, 320,
   "ロボット支援 二弁手術",
   "WVU の Comas / Wei による double valve surgery。"
   "1つの胸腔から2つの弁に到達する順序が確認できる。",
   "https://doi.org/10.21037/acs-2022-rmvs-79",
   "Comas GM, Wei LM, et al. <i>Ann Cardiothorac Surg</i> 2022;11(5):543-544"),
  ("mm", "rapid deployment 弁による完全内視鏡下AVR＋僧帽弁形成",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2025", "tutorial", 2059, 419,
   "本節で扱った AVR＋MV の原典動画。"),
  ("mm", "RAM デバイスによる僧帽弁置換＋三尖弁形成（完全内視鏡）",
   "Baysal F, Poschner T, MMCTS 2025", "case-report", 2006, 594,
   "器材の紹介と手術戦略を先に置き、RAM/SEW-EASY による MVR → 三尖弁輪縫縮の順。"),
  ("mm", "経乳輪切開による3D完全内視鏡下 VSD 閉鎖＋AVR",
   "Watanabe S, Ito T, MMCTS 2025", "case-report", 1998, 419,
   "大動脈弁を外して VSD を同定し、<b>パッチの下縁を縫ってから人工弁を入れ、"
   "最後に上縁を縫う</b>という順序が要点。"),
 ],

 "7.3": [
  ("mm", "三尖弁形成＋両心房 CryoMAZE（完全内視鏡）",
   "Amabile A, LaLonde M ら, MMCTS 2024", "case-report", 1861, 434, ""),
  ("mm", "人工腱索を用いた完全内視鏡下三尖弁形成",
   "Amabile A, LaLonde MR ら, MMCTS 2022", "case-report", 1758, 402,
   "上下大静脈の遮断・右房切開・弁の観察から形成まで。"),
  ("mm", "内視鏡下三尖弁形成の suture map", "Hamid UI, Aksoy R, MMCTS 2022",
   "tutorial", 1741, 557, ""),
  ("mm", "心拍動下 re-redo 三尖弁形成（smartcanula 使用）",
   "Hecker F, Montagner M, MMCTS 2026", "tutorial", 2144, 510,
   "2回の開心術後という最も難しい条件での三尖弁再手術。"),
  ("mm", "成人 Ebstein 病に対する3D完全内視鏡下三尖弁形成",
   "Kitamura H, Tamaki M, MMCTS 2026", "case-report", 2209, 640,
   "<b>心房化右室の縫縮</b>を含む7工程。"),
 ],

 "7.5": [
  ("mm", "心室細動下でのロボット完全内視鏡下 Cryo-Maze",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2024", "tutorial", 1957, 324,
   "中等度低体温＋<b>心室細動下</b>（大動脈遮断なし）で左房・右房それぞれの Cryo-Maze を行う。"
   "本節の「不整脈手術をどう足すか」の一つの解。"),
  ("mm", "AtriClip Pro2 による心表面左心耳閉鎖", "Baudo M, Yakobitis A, MMCTS 2024",
   "tutorial", 1913, 488, ""),
  ("mm", "高齢・出血既往例に対するロボット左心耳結紮",
   "Poffo R, Toma HE, MMCTS 2026", "case-report", 2139, 297,
   "体位とマーキング → 左心耳の展開 → デバイス選択と展開。"),
 ],

 "8.1": [
  ("mm", "ロボット完全内視鏡下 心房中隔欠損閉鎖", "Amabile A, Degife E, MMCTS 2021",
   "case-report", 1698, 387,
   "右房切開 → 欠損の観察 → 閉鎖 → <b>右房切開の2度縫い（second run）</b>まで。"),
  ("mm", "ロボット心房中隔欠損閉鎖", "Senay S, Gullu AU, MMCTS 2014", "tutorial", 53, 580,
   "心膜支持糸と外固定・遮断・両大静脈の bulldog 遮断・パッチ閉鎖・脱気、の8工程。"),
  ("mm", "AVR に伴う心室中隔瘤のロボットパッチ閉鎖",
   "Parkash J, Ehtesham A, MMCTS 2025", "case-report", 2108, 459,
   "大動脈弁を外したうえで中隔欠損を確認し、心膜パッチを縫着してから人工弁を入れる。"),
 ],

 "8.2": [
  ("fig", "36483609_acs-11-06-634-vid.jpg", 569, 320,
   "心房粘液腫の切除（papillary subtype）",
   "脆い乳頭状粘液腫を<b>掴まずに</b>取り出す工程。本節の主題そのもの。",
   "https://doi.org/10.21037/acs-2022-rmvs-162",
   "Rizkalla AJ, Yan TD, et al. <i>Ann Cardiothorac Surg</i> 2022;11(6):634-636"),
  ("mm", "僧帽弁 乳頭状線維弾性腫の完全内視鏡下切除",
   "Amabile A, Morrison A, MMCTS 2021", "tutorial", 1668, 204,
   "腫瘍切除そのものは短いが、弁を傷つけずに切除する視野の作り方が見える。"),
  ("mm", "心室中隔に転移した神経内分泌腫瘍のロボット切除",
   "Henkens A, Navarra E, MMCTS 2020", "tutorial", 1497, 499,
   "左房を開けて中隔の転移巣を切除する8工程。"),
  ("mm", "port-access による左房粘液腫切除", "Olsthoorn J, Sardari Nia P ら, MMCTS 2019",
   "tutorial", 1194, 199, "本レビューが挙げた動画で最も短い。"),
  ("mm", "完全内視鏡下ロボット心膜嚢胞切除", "Poffo R, Toma HE, MMCTS 2022",
   "tutorial", 1740, 349, "心腔を開けない腫瘤性病変の例。"),
 ],

 "8.4": [
  ("fig", "36483619_acs-11-06-632-vid.jpg", 569, 320,
   "ロボット中隔心筋切除",
   "台大（NTUH）の Cheng / Chi による HOCM への心筋切除。"
   "本節の2つの到達路のうち、経僧帽弁路の実演。",
   "https://doi.org/10.21037/acs-2022-rmvs-24",
   "Cheng BC, Chi NH, et al. <i>Ann Cardiothorac Surg</i> 2022;11(6):632-633"),
  ("mm", "経僧帽弁中隔心筋切除＋僧帽弁形成（HOCM）",
   "AlJamal YN, Kitahara H, Balkhy HH, MMCTS 2023", "case-report", 1812, 437, ""),
  ("mm", "前尖の縦切開を用いた内視鏡下経僧帽弁心筋切除",
   "Ito T, Sawaki S, MMCTS 2024", "tutorial", 1916, 478,
   "<b>前尖を縦に切って中隔に到達し、切除後に前尖を再建して弁輪縫縮する</b>という手順。"
   "経僧帽弁路で視野が足りない場合の解。"),
  ("mm", "右小開胸・経僧帽弁到達による HOCM の内視鏡下治療",
   "Paivin A, Denisyuk D, MMCTS 2025", "tutorial", 2061, 327,
   "心筋切除に加えて<b>僧帽弁下組織の再建</b>を行う。"),
  ("web", "Robotic trans-atrial and trans-mitral ventricular septal resection",
   "Chitwood WR Jr", "https://doi.org/10.21037/acs.2017.01.06",
   "Ann Cardiothorac Surg 2017;6(1):54-59 の動画",
   "経心房・経僧帽弁路の原典にあたる2017年の動画。"),
 ],

 "8.5": [
  ("mm", "胸腔鏡下 心臓再同期療法（心表面リード留置）", "Droghetti A ら, MMCTS 2015", "tutorial", 72, 232,
   "経静脈リードが留置できない場合の心表面リード。ロボットではなく胸腔鏡。"),
  ("mm", "拡張型心筋症に対する経心尖アプローチでの左室再同期最適化",
   "Kassai I, Alfieri O ら, MMCTS 2017", "tutorial", 544, 249, "留置部位の最適化という論点の参照先。"),
 ],

 "8.6": [
  ("mm", "再手術：癒着剥離（前回正中×2・前回ロボット×1）＋複雑再形成",
   "Amabile A, LaLonde MR ら, MMCTS 2022", "case-report", 1766, 574,
   "再手術での癒着剥離を最も詳しく見せる1本。"),
  ("mm", "前回CABG後の右冠動脈への redo TECAB",
   "Kitahara H, Grady K, Balkhy HH, MMCTS 2023", "case-report", 1803, 316, ""),
  ("mm", "SAVR→TAVR 後の完全内視鏡下AVR（TAVR explant）",
   "Van Genechten S, Hillen W, MMCTS 2025", "case-report", 2021, 612, ""),
  ("mm", "心拍動下 re-redo 三尖弁形成", "Hecker F, Montagner M, MMCTS 2026",
   "tutorial", 2144, 510, ""),
  ("mm", "TEER クリップ抜去を伴う僧帽弁再形成", "Kaneyuki D, Yost CC, MMCTS 2023",
   "case-report", 1837, 399, ""),
 ],
}

# marker -> the exact line the block is inserted BEFORE
MARKERS = {
 "1.1": "### 1.2 エビデンスの成熟度は術式で全く違う",
 "2.3": "### 2.4 ポート配置は術式別 — 共通の図は作れない",
 "2.4": "### 2.5 意見が分かれる点",
 "2.5": "---\n\n## 3. 訓練とプログラム構築",
 "3.3": "### 3.4 Phase II — 他施設研修と proctoring、そして最初の10例",
 "4.1": "### 4.2 展開 — 左房切開と retractor",
 "4.3": "### 4.4 弁輪縫縮 — robotic 特有の工夫が最も進んだ領域",
 "4.4": "### 4.5 難症例",
 "4.5": "### 4.6 Pitfall — どこで壊れるか",
 "4.6": "---\n\n## 5. 大動脈弁（RAVR）",
 "5.2": "### 5.3 大動脈切開・弁の出し方・視野最適化",
 "5.3": "### 5.4 併施手技 — 根部拡大と心筋切除",
 "5.4": "### 5.5 プラットフォーム論 — 本章の核心",
 "6.2": "### 6.3 IMA 採取",
 "6.3": "### 6.4 標的血管の展開",
 "6.4": "### 6.5 吻合",
 "6.5": "### 6.6 成績 — TECAB は何を達成したか",
 "6.7": "### 6.8 Pitfall — 転換のリスク因子は",
 "7.2": "### 7.3 僧帽弁 + 三尖弁",
 "7.3": "### 7.4 弁 + 冠動脈",
 "7.5": "### 7.6 どこまで足せるか — 線引き",
 "8.1": "### 8.2 心臓腫瘍 — 「掴まない」ための工夫",
 "8.2": "### 8.3 不整脈・左心耳 — 「閉じたつもり」が閉じていない",
 "8.4": "### 8.5 心表面リード（CRT）",
 "8.5": "### 8.6 再手術・その他",
 "8.6": "---\n\n## 9. 展望",
}

CHAPTER_TITLES = {
 "1": "1. 総論", "2": "2. 共通の土台", "3": "3. 訓練とプログラム構築",
 "4": "4. 僧帽弁形成", "5": "5. 大動脈弁（RAVR）", "6": "6. 冠動脈（TECAB / MIDCAB）",
 "7": "7. 複合弁・同時手術", "8": "8. Others",
}


def numbering():
    """section -> [(video_id, item), ...] with per-chapter running numbers."""
    counters, out = {}, {}
    for sec in MARKERS:
        ch = sec.split(".")[0]
        rows = []
        for item in V[sec]:
            counters[ch] = counters.get(ch, 0) + 1
            rows.append((f"{ch}-{counters[ch]}", item))
        out[sec] = rows
    return out


NUM = numbering()


def render(vid, item):
    if item[0] == "fig":
        _, fn, w, h, lead, body, url, cite = item
        return (
            f'<figure class="vfig" id="v{vid}">\n'
            f'<a href="{url}" target="_blank" rel="noopener">'
            f'<img src="figures/{PREFIX}{fn}" alt="{lead}の手術動画" '
            f'loading="lazy" decoding="async" width="{w}" height="{h}">'
            f'<span class="play">▶</span></a>\n'
            f'<figcaption><b>動画{vid}　{lead}</b>　{body}'
            f'<a href="{url}" target="_blank" rel="noopener">▶ 原典で動画を見る</a>'
            f'<span class="src">サムネイル出典: {cite}（{ACS_LIC}）。'
            f'ライセンス表示のある出版社公式のポスター画像であり、動画のコマ取りではない。</span>'
            f'</figcaption>\n</figure>')
    if item[0] == "mm":
        _, title, who, kind, num, sec_len, body = item
        url = mm(kind, num)
        return (
            f'<p id="v{vid}"><b>動画{vid}　{title}</b>'
            f'（{who}、{dur(sec_len)}）'
            + (f'　{body}' if body else "")
            + f'　→ <a href="{url}" target="_blank" rel="noopener">'
              f'mmcts.org/{kind}/{num}</a>（購読制）</p>')
    _, title, who, url, label, body = item
    return (
        f'<p id="v{vid}"><b>動画{vid}　{title}</b>（{who}）'
        + (f'　{body}' if body else "")
        + f'　→ <a href="{url}" target="_blank" rel="noopener">{label}</a></p>')


def block(sec):
    figs = [(v, it) for v, it in NUM[sec] if it[0] == "fig"]
    links = [(v, it) for v, it in NUM[sec] if it[0] != "fig"]
    out = [BEGIN.format(sec)]
    for vid, item in figs:
        out.append(render(vid, item))
    if links:
        out.append('<div class="videolist">')
        out.append('<p class="vl-head">▶ 実際の手技を動画で見る</p>')
        for vid, item in links:
            out.append(render(vid, item))
        out.append("</div>")
    out.append(END.format(sec))
    return "\n".join(out) + "\n\n"


INDEX_BEGIN = "<!-- VIDINDEX -->"
INDEX_END = "<!-- /VIDINDEX -->"
INDEX_MARKER = "## 付録B 略語集"


def index_block():
    n_fig = sum(1 for sec in MARKERS for _, it in NUM[sec] if it[0] == "fig")
    n_all = sum(len(NUM[sec]) for sec in MARKERS)
    rows = [
        INDEX_BEGIN,
        "## 付録A 動画一覧（術式別）",
        "",
        f"本レビューが参照した手技動画は **{n_all}点**（うち{n_fig}点はサムネイル付きで本文に掲載）。",
        "動画番号をクリックすると本文の該当箇所へ移動する。",
        "",
        "- **MMCTS**（*Multimedia Manual of Cardiothoracic Surgery*, EACTS）は"
        "tutorial / case-report ページに動画が埋まっている。**購読制**。",
        "- **Ann Cardiothorac Surg**（AME, *Masters of Cardiothoracic Surgery* シリーズ）は"
        "論文ページに動画が埋まっており、2019年以降の号は CC BY-NC-ND 4.0。",
        "- その他（JTCVS Tech / JTCVS Open / Ann Thorac Surg / ICVTS / Cureus ほか）は"
        "論文ページ（DOI）に動画がある。",
        "",
        "これらは**本文の記述の典拠ではなく、記述した手技を映像で確認するための参照先**である"
        "（典拠は[引用文献](#引用文献)）。",
        "",
    ]
    for ch, ch_title in CHAPTER_TITLES.items():
        secs = [s for s in MARKERS if s.split(".")[0] == ch]
        if not secs:
            continue
        rows += [f"### {ch_title}", "", "| 動画 | 内容 | 出典 |", "|:--|:--|:--|"]
        for sec in secs:
            for vid, item in NUM[sec]:
                if item[0] == "fig":
                    lead, url = item[4], item[6]
                    src = re.sub(r"<[^>]+>", "", item[7])
                    rows.append(f"| [動画{vid}](#v{vid}) | {lead} | [{src}]({url}) |")
                elif item[0] == "mm":
                    _, title, who, kind, num, sec_len, _b = item
                    rows.append(
                        f"| [動画{vid}](#v{vid}) | {title} | "
                        f"[{who}／{dur(sec_len)}]({mm(kind, num)}) |")
                else:
                    _, title, who, url, label, _b = item
                    rows.append(f"| [動画{vid}](#v{vid}) | {title} | [{who}／{label}]({url}) |")
        rows.append("")
    rows += [
        "> **著作権について**",
        "> 掲載したサムネイルは、いずれも出版社が OA パッケージで配布している"
        "動画ポスター画像（CC BY-NC-ND 4.0）をそのまま用いたものであり、",
        "> **動画からのコマ取りは一切行っていない**。動画本体は各出版社のページで視聴すること"
        "（MMCTS は購読が必要）。",
        "",
        "---",
        "",
        INDEX_END,
        "",
    ]
    return "\n".join(rows) + "\n"


def main():
    os.makedirs(PUB_DIR, exist_ok=True)
    n_copied = 0
    for sec in MARKERS:
        for _, item in NUM[sec]:
            if item[0] != "fig":
                continue
            src = os.path.join(SRC_DIR, item[1])
            if not os.path.exists(src):
                raise SystemExit(f"missing thumbnail: {src}")
            shutil.copy2(src, os.path.join(PUB_DIR, PREFIX + item[1]))
            n_copied += 1

    text = open(MD, encoding="utf-8").read()
    text = re.sub(r"<!-- VID:[\d.]+ -->.*?<!-- /VID:[\d.]+ -->\n\n?", "",
                  text, flags=re.DOTALL)
    text = re.sub(re.escape(INDEX_BEGIN) + r".*?" + re.escape(INDEX_END) + r"\n\n?",
                  "", text, flags=re.DOTALL)

    if text.count(INDEX_MARKER) != 1:
        raise SystemExit(f"video-index marker occurs {text.count(INDEX_MARKER)}x")
    text = text.replace(INDEX_MARKER, index_block() + INDEX_MARKER)

    for sec, marker in MARKERS.items():
        if text.count(marker) != 1:
            raise SystemExit(f"marker for {sec} occurs {text.count(marker)}x: {marker!r}")
        text = text.replace(marker, block(sec) + marker)

    open(MD, "w", encoding="utf-8").write(text)
    n_all = sum(len(NUM[s]) for s in MARKERS)
    print(f"{n_copied} thumbnails -> {PUB_DIR}")
    print(f"{n_all} videos in {len(MARKERS)} blocks -> {os.path.relpath(MD, REPO)}")


if __name__ == "__main__":
    main()
