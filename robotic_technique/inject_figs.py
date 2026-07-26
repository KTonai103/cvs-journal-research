#!/usr/bin/env python3
"""Insert the extracted source figures into md/robotic_technique_review.md.

Convention follows the other reviews in this repo: raw <figure> blocks live in
the Markdown (pandoc passes them through), images are published under
output/figures/ with an `rt_` prefix so they cannot collide with the figure sets
of the other reviews.

All figures are ORIGINAL journal figures extracted from the source PDFs — no
authored diagrams, no video frame-grabs.  Idempotent: re-running replaces the
previously injected blocks.
"""
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
MD = os.path.join(HERE, "md", "robotic_technique_review.md")
SRC_DIR = os.path.join(HERE, "figures")
PUB_DIR = os.path.join(REPO, "output", "figures")
PREFIX = "rt_"

BEGIN = "<!-- FIG:{} -->"
END = "<!-- /FIG:{} -->"

# --- sources -----------------------------------------------------------------
# key -> (citation line, licence note)
S = {
    "hage": ("Hage A, Malas T, Gillinov M. <i>JTCVS Tech</i> 2025;29:9-11. "
             '<a href="https://doi.org/10.1016/j.xjtc.2024.10.001">doi:10.1016/j.xjtc.2024.10.001</a>',
             "CC BY-NC-ND 4.0（図は Cleveland Clinic © 2024）"),
    "czesla": ("Czesla M, et al. <i>Ann Cardiothorac Surg</i> 2013;2(6):849-852. "
               '<a href="https://doi.org/10.3978/j.issn.2225-319X.2013.07.26">doi:10.3978/j.issn.2225-319X.2013.07.26</a>',
               "Ann Cardiothorac Surg（AME）"),
    "wei_ravr": ("Wei LM, Badhwar V. <i>Ann Cardiothorac Surg</i> 2025;14(3):228-234. "
                 '<a href="https://doi.org/10.21037/acs-2025-ravr-12">doi:10.21037/acs-2025-ravr-12</a>',
                 "CC BY-NC-ND 4.0"),
    "wertan": ("Wertan MC, et al. <i>Ann Cardiothorac Surg</i> 2024;13(5):442-451. "
               '<a href="https://doi.org/10.21037/acs-2024-rcabg-0034">doi:10.21037/acs-2024-rcabg-0034</a>',
               "CC BY-NC-ND 4.0"),
    "algoet": ("Algoet M, et al. <i>Ann Cardiothorac Surg</i> 2024;13(5):397-408. "
               '<a href="https://doi.org/10.21037/acs-2023-rcabg-0210">doi:10.21037/acs-2023-rcabg-0210</a>',
               "CC BY-NC-ND 4.0"),
    "arai": ("Arai A, Kitahara H, Balkhy HH. <i>JTCVS Tech</i> 2026;35:102169. "
             '<a href="https://doi.org/10.1016/j.xjtc.2025.102169">doi:10.1016/j.xjtc.2025.102169</a>',
             "CC BY-NC-ND 4.0"),
    "goto": ("Goto Y, et al. <i>Cureus</i> 2025;17(6):e86081. "
             '<a href="https://doi.org/10.7759/cureus.86081">doi:10.7759/cureus.86081</a>',
             "CC BY 4.0"),
    "wei_ntuh": ("Wei LY, et al. <i>Ann Cardiothorac Surg</i> 2025;14(3):210-217. "
                 '<a href="https://doi.org/10.21037/acs-2024-ravr-0185">doi:10.21037/acs-2024-ravr-0185</a>',
                 "CC BY-NC-ND 4.0"),
    "kim": ("Kim K, et al. <i>JTCVS Tech</i> 2024;28:73-81. "
            '<a href="https://doi.org/10.1016/j.xjtc.2024.05.022">doi:10.1016/j.xjtc.2024.05.022</a>',
            "CC BY-NC-ND 4.0"),
    "myxoma": ("Nakamura Y, et al. <i>JTCVS Tech</i> 2025;29:100-102. "
               '<a href="https://doi.org/10.1016/j.xjtc.2024.10.005">doi:10.1016/j.xjtc.2024.10.005</a>',
               "CC BY-NC-ND 4.0"),
    "agnino": ("Agnino A, et al. <i>J Clin Med</i> 2024;13(6):1563. "
               '<a href="https://doi.org/10.3390/jcm13061563">doi:10.3390/jcm13061563</a>',
               "CC BY 4.0"),
    "laa": ("Nakamura Y, et al. <i>JTCVS Tech</i> 2026;36:102268. "
            '<a href="https://doi.org/10.1016/j.xjtc.2026.102268">doi:10.1016/j.xjtc.2026.102268</a>',
            "CC BY-NC-ND 4.0"),
    "bubble": ("Nakayama T, et al. <i>Interdiscip Cardiovasc Thorac Surg</i> 2025;40(10):ivaf172. "
               '<a href="https://doi.org/10.1093/icvts/ivaf172">doi:10.1093/icvts/ivaf172</a>',
               "CC BY-NC 4.0"),
}

# --- figures -----------------------------------------------------------------
# (file, source key, bold lead, body text)
FIGS = {
 "4.1": [
  ("mv_hage_f1_ports_standard.png", "hage", "図 4-1. 標準体格のポート配置（Fig 1）",
   "第4肋間の小開胸（前腋窩線 <b>AAL</b> の約1 cm 外側から内側へ 3–4 cm）を中心に、左アーム＝第2肋間、"
   "右アーム＝第6肋間、左房リトラクター＝第4肋間・鎖骨中線（<b>MCL</b>）上。"
   "本文の「標準の配置」表と対応する。"),
  ("mv_hage_f2_ports_thin.png", "hage", "図 4-2. きわめて痩せた小柄な患者での修正配置（Fig 2）",
   "全ポートを外側・下方へずらし、<b>右アームは第7肋間（皮膚穿刺は第8肋間）</b>、"
   "左アームは第2肋間だが<b>皮膚穿刺は第1肋間</b>で、いずれもきわめて浅い進入角にする。"
   "左房リトラクターは逆に<b>傍胸骨側</b>へ寄せる。これで triangle of attack が「ズームアウト」し、"
   "アーム同士の干渉が消える。"),
 ],
 "4.6": [
  ("mv_czesla_f4_cx_anatomy.png", "czesla", "図 4-3. 左回旋枝と僧帽弁輪の位置関係（Fig 4）",
   "解剖標本。1＝左心耳、2＝<b>左回旋枝</b>、3＝後尖、4＝前外側交連、5＝前尖、6＝前乳頭筋。"
   "Cx は左心耳基部と前交連の間を、弁尖–弁輪付着部から <b>3–4 mm</b> の距離で走る。"
   "本文の「7時方向から先が最も危険」「深い運針を避ける区間」がどこかを目で確認できる。"),
 ],
 "5.2": [
  ("ravr_f01_position.png", "wei_ravr", "図 5-1. 体位（Fig 1）",
   "仰臥位、右肩甲骨先端の下にロール、<b>右腕は上腕をできるだけ垂直にして後方へ</b>吊る。"
   "これで右腋窩が最大限に開く。"),
  ("ravr_f02_ports_docking.png", "wei_ravr", "図 5-2. ポート配置とドッキング（Fig 2）",
   "作業孔（第4肋間・前腋窩線、3 cm）を中心に、<b>Arm 1＝10時方向・第3肋間、"
   "Arm 3＝1時方向・第5肋間、Arm 4＝4時方向・第6肋間</b>、Arm 2（カメラ）は作業孔から。"
   "ロボットは<b>患者左側</b>からドッキングする（僧帽弁とは逆）。"),
 ],
 "5.3": [
  ("ravr_f03_aortotomy.png", "wei_ravr", "図 5-3. 大動脈切開（Fig 3）",
   "洞管接合部の約 <b>2 cm 遠位</b>から始め、内側・頭側へ、外側・尾側へ<b>非冠尖洞の中央まで</b>延長する"
   "modified “hockey stick”。"),
  ("ravr_f04_valvectomy.png", "wei_ravr", "図 5-4. ロボット弁切除（Fig 4）",
   "曲剪刀で<b>右–無交連から</b>開始し、術者の好みで右冠尖側または非冠尖側の弁輪に沿って延長する。"),
  ("ravr_f05_decalcification.png", "wei_ravr", "図 5-5. 弁輪の脱灰とデブライドメント（Fig 5）",
   "刃は<b>石灰を切るのではなく、石灰と弁輪の間の層を見つけて持ち上げる</b>のに使う。"
   "全例で <b>rongeur を要さず</b>弁輪まで完全に脱灰できたと報告されている。"
   "ベッドサイド術者の吸引と洗浄が必須。"),
  ("ravr_f06_implant.png", "wei_ravr", "図 5-6. 人工弁の植込みと結紮（Fig 6）",
   "<b>心室側から周方向に結節縫合</b>を左–無交連から時計回りに置き、体外で人工弁の縫合輪に通してから"
   "作業孔から搬入し、<b>long Cor-Knot</b> で固定する。"),
  ("ravr_f07a_aortotomy_closure.png", "wei_ravr", "図 5-7A. 大動脈切開の閉鎖（Fig 7A）",
   "<b>4-0 ポリプロピレンの2層</b>で閉鎖する。"),
  ("ravr_f07b_closure_test.png", "wei_ravr", "図 5-7B. 閉鎖の完成と順行性テスト（Fig 7B）",
   "<b>遮断解除の前に</b>順行性冷血/心筋保護液を流して縫合線の健全性を確認する。"),
 ],
 "5.4": [
  ("ravr_f08_are_extension.png", "wei_ravr", "図 5-8. 非冠尖弁輪に沿った大動脈切開の延長（Fig 8）",
   "人工弁のアップサイジングと基部拡大の準備。<b>modified Nicks</b> として非冠尖洞の中点から弁輪まで、"
   "必要なら弁輪の一部または全体に沿って延長する。"),
  ("ravr_f09_dacron_patch.png", "wei_ravr", "図 5-9. 合成ポリエステル（Dacron）パッチの裁断（Fig 9）",
   "パッチは体外で概形を作り、<b>作業孔から入れてから胸腔内でさらに微調整</b>する。"
   "大きな拡大では合成ポリエステル、小さければ自己/ウシ心膜を選ぶ。"),
  ("ravr_f10_are_anchor.png", "wei_ravr", "図 5-10. 基部拡大の起点（Fig 10）",
   "最初の1針は<b>非冠尖弁輪のレベルで、残存する大動脈組織の基部を outside-in</b> に通し、"
   "続いてパッチへ通す。"),
  ("ravr_f11_are_complete.png", "wei_ravr", "図 5-11. 基部拡大の完成（Fig 11）",
   "4-0 ポリプロピレンの各脚を右方向・左方向へ縫い進めて結紮し、"
   "しばしば<b>大動脈切開全体</b>をパッチで補強して最大の効果を得る。"
   "完成後は順行性冷血/心筋保護液で健全性を確認する。"),
 ],
 "6.2": [
  ("cabg_algoet_f3_incisions.png", "algoet", "図 6-1. RA-MIDCAB と TECAB の切開（Fig 3）",
   "左＝<b>RA-MIDCAB</b>（第2・4・6肋間のトロカール＋第4肋間の小開胸）、"
   "右＝<b>TECAB</b>（前腋窩線上の第2・4・6肋間＋標的により剣状突起外側または肋骨弓下、"
   "＋左第2肋間・傍胸骨の助手ポート）。同じ「ロボット冠動脈手術」でも創の数と位置が違う。"),
  ("cabg_algoet_f4_valve_incisions.png", "algoet", "図 6-2. 弁手術（僧帽弁・大動脈弁）の切開（Fig 4）",
   "右胸に 8 mm ポート4本＋<b>1.5–4.0 cm の助手切開</b>。"
   "大動脈弁では<b>人工弁を胸腔内に入れられる大きさ</b>が助手切開に必要という点だけが僧帽弁と異なる。"
   "“ports only” 化する場合は助手切開を 10–12 mm ポートに置き換える。"),
  ("cabg_wertan_f1_coordinates.png", "wertan", "図 6-3. “precision incision” の3座標（Fig 1）",
   "肋間や鎖骨中線ではなく、<b>胸骨正中線・LIMA の位置・横隔膜前縁</b>の3つを"
   "Ioban ドレープ上にマークして内視鏡ポート位置を決める。"
   "このポートがそのまま小開胸になるため、1点の精度が手術の難易度を決める。"),
  ("cabg_wertan_f2_coord1.png", "wertan", "図 6-4. 座標1 — 長軸上の位置決め（Fig 2）",
   "<b>胸骨上切痕と剣状突起の中点</b>にマークする。LIMA の近位・遠位に等しく届く高さになる。"),
  ("cabg_wertan_f3_coord3.png", "wertan", "図 6-5. 座標3 — 標的に応じた微調整（Fig 3）",
   "座標1・2 は<b>中〜遠位 LAD</b> に合わせてある。"
   "標的がより近位なら<b>1肋間上</b>、より遠位なら<b>1肋間下</b>。"
   "近位LADや第1対角枝／ramus ならより<b>内側</b>へ寄せる。"),
  ("cabg_wertan_f4_port_alignment.png", "wertan", "図 6-6. 3本のポートの縦一直線配置（Fig 4）",
   "内視鏡ポートの<b>上下 8〜10 cm（指4本分）</b>に、骨性胸郭が許す範囲で縦一直線に置く。"
   "<b>下方ポートは骨性胸郭を持ち上げて</b>心膜と前胸壁の間の空間を広げるのに使い、"
   "上方ポートは軽く “burp” する程度にとどめる（強く持ち上げると肋間筋が裂ける）。"),
 ],
 "6.4": [
  ("cabg_wertan_f5a_pericardium.png", "wertan", "図 6-7A. 後方（横隔神経後方）の心膜切開（Fig 5A）",
   "吻合中に貯まる血液を排出させるための切開。必須ではないが、胸壁・シャント周囲・"
   "スタビライザーによる心外膜静脈の軽微な損傷からの出血管理に効く。"),
  ("cabg_wertan_f5b_pericardium.png", "wertan", "図 6-7B. 前方心膜切開と LAD 標的の同定（Fig 5B）",
   "<b>心膜越しに肺動脈が見える部位のすぐ外側、左室の上</b>で開ける。"
   "損傷するなら<b>左室の方が右室や肺動脈より許容できる</b>。"
   "心膜尖部で外側に切開を入れると心臓が心膜の外へずれるので避ける。"),
  ("cabg_wertan_f6_lima_clip.png", "wertan", "図 6-8. LIMA 採取（分枝のクリップ）（Fig 6）",
   "分枝は<b>近位をクリップ、遠位を焼灼</b>。skeletonize は<b>遠位（分岐部）から近位へ</b>進める"
   "（近位→遠位の全周性剥離は静脈出血を増やした）。"
   "<b>前方の付着を一部残す</b>と LIMA が吊られてロボットアームの損傷から守られる。"),
  ("cabg_wertan_f7_incision_drain.png", "wertan", "図 6-9. precision incision と上方ドレーン（Fig 7）",
   "小開胸は <b>4〜12 cm</b>、術者が快適な大きさでよい。"
   "「患者にとっての主たる利益は<b>ロボットによる低侵襲な IMA 採取</b>であって、"
   "必ずしも切開の大きさではない」。19Fr Blake ドレーンを上方ポートから肺尖上に置く。"),
  ("cabg_wertan_f8a_stabilizer.png", "wertan", "図 6-10A. OCTOPUS NUVO スタビライザー（術野の2部品）（Fig 8A）",
   "スタビライザー本体とポールは<b>別々に術野に出し</b>、小開胸の内側で連結する。"),
  ("cabg_wertan_f8b_stabilizer.png", "wertan", "図 6-10B. 胸腔内での連結（Fig 8B）",
   "<b>先に指を小開胸から入れて</b>、下方ポートから入れる器械を視野に導く。"
   "ポール挿入時は指先で誘導して心臓を傷つけない — 心臓が胸壁のすぐ下にあるため、"
   "この注意はいくら強調してもし過ぎることはない、と原著は書いている。"),
  ("cabg_wertan_f9_saddleloop.png", "wertan", "図 6-11. SaddleLoop による近位 LAD のスネア（Fig 9）",
   "吸引式スタビライザーを心拍動下に当て、<b>鈍先の SaddleLoop 1541</b> を近位 LAD に回して"
   "余分なテープを切る。吻合は <b>7-0 Prolene</b>、踵側で3結び、内側の中点で終える。"),
 ],
 "7.1": [
  ("comb_wei_f1_setup.png", "wei_ntuh", "図 7-1. 複合弁手術のセットアップ（Fig 1）",
   "A＝ロボット（作業孔＝第4肋間・右前腋窩線 3 cm、左右アーム＝第3・第6肋間、"
   "心房リトラクター＝第4肋間、カメラは作業孔のすぐ上、ベント用 sub-working port はその下）。"
   "B＝内視鏡（同じ第4肋間の切開＋<b>第2または第3肋間</b>のカメラポート）。"),
  ("comb_wei_f2_traction.png", "wei_ntuh", "図 7-2. 3本の牽引糸による大動脈弁の展開（Fig 2）",
   "<b>上方牽引</b>＝左–右交連の糸を上方心膜へ、"
   "<b>右方牽引</b>＝右–無冠交連の糸を横隔膜方向へ、"
   "<b>下方牽引</b>＝左–無冠交連の糸を作業孔方向へ。"
   "台湾とオーストラリアの独立プログラムが WVU 法と収斂した際、"
   "共有していた唯一の戦略が「牽引糸で大動脈基部を回転させる」ことだった。"),
  ("comb_goto_f2_dualcamera.png", "goto", "図 7-3. dual-camera 戦略（Fig 2）",
   "A＝術前造影CTで<b>大動脈弁と僧帽弁の最適視軸が大きく異なる</b>ことを実測した図"
   "（矢印がそれぞれの正面視に必要なカメラポート進入角）。"
   "B＝実際のポート配置。4 cm の主作業切開に対し<b>カメラポートを2本</b>置いている。"),
  ("comb_goto_f3_views.png", "goto", "図 7-4. カメラポートによる大動脈弁の見え方の差（Fig 3）",
   "A＝<b>ポートA（僧帽弁用）</b>からは弁尖の一部しか見えない。"
   "B＝<b>ポートB（大動脈弁用）</b>に切り替えると弁全体が展開される。"
   "C・D は各ポートへの内視鏡挿入の術中写真。矢印は乳頭状線維弾性腫。"),
 ],
 "7.4": [
  ("comb_arai_f1_tecab_ports.png", "arai", "図 7-5. bilateral アプローチ①：左胸 TECAB のポート（Fig 1）",
   "<b>第4肋間に 12 mm カメラポート</b>、第2・第6肋間に 8 mm アームポート。"
   "スタビライザー用の 12 mm ポートは剣状突起の外側に置く。da Vinci <b>Si</b> を左胸にドッキング。"),
  ("comb_arai_f2_mv_ports.png", "arai", "図 7-6. bilateral アプローチ②：右胸 僧帽弁形成のポート（Fig 2）",
   "第4肋間の 8 mm カメラポートを起点に第5肋間へカメラを移し、"
   "最初のカメラポートを <b>Alexis XXS</b> に替えて 8 mm 作業孔とし、"
   "新しいカメラポートを同肋間のより内側に置く。da Vinci <b>Xi</b> を右胸にドッキング。"
   "先に off-pump TECAB を済ませることで CPB 時間を短縮できる。"),
 ],
 "8.1": [
  ("oth_kim_f1_atriotomy_shape.png", "kim", "図 8-1. 右房切開の向き（Fig 1）",
   "A＝従来の<b>斜切開</b>、B＝<b>心房間溝に平行な垂直右房切開（VRA）</b>。"
   "この違いだけで ASD の rim 全周の展開が変わり、"
   "IPTW 調整後で <b>CPB 143.1→92.8分、遮断 60.8→30.7分（いずれも P&lt;.001）</b>となった。"),
  ("oth_kim_f2_scope_angle.png", "kim", "図 8-2. 内視鏡の角度と視軸（Fig 2）",
   "A＝30°スコープ、B＝0°スコープ。右胸から見たときの視軸の違いを胸部横断面で示す。"),
  ("oth_kim_f3_exposure.png", "kim", "図 8-3. 実際の術野での rim の見え方（Fig 3）",
   "白丸＝ASD の rim、黄丸＝下方 rim。切開の向きにより下方 rim の見え方が変わる。"),
 ],
 "8.2": [
  ("oth_myxoma_f1_sonopet.png", "myxoma", "図 8-4. 超音波吸引器（Sonopet iQ）の適用（Fig 1）",
   "A＝205 mm 軟部組織チップ、B＝ベッドサイド術者が <b>3 cm の作業孔</b>から Sonopet を当てる術中写真。"
   "設定は<b>超音波出力 50%・吸引圧 70%・灌流 15 mL/分</b>。"),
  ("oth_myxoma_f2_before_after.png", "myxoma", "図 8-5. 吸引前後の粘液腫（Fig 2）",
   "A＝吸引前。<b>カメラは腫瘍の手前しか見えず付着部が隠れている</b>。"
   "B＝吸引後、<b>1 cm 程度の弾性硬な核だけ</b>が残り、左房心内膜の付着部が明瞭になる。"
   "この時点で心内膜を <b>5 mm のマージン</b>をつけて全層切除する。"),
 ],
 "8.3": [
  ("oth_agnino_f1_workingport.png", "agnino", "図 8-6. ロボット AF アブレーションの作業ポート評価（Fig 1）"
   , "左胸腔鏡単独。人工心肺なし・心拍動下で、肺静脈と左房後壁の隔離＋左心耳閉鎖＋Marshall靱帯の離断を行う。"),
  ("oth_agnino_f2_marshall.png", "agnino", "図 8-7. Marshall 靱帯の剥離（Fig 2）",
   "左心耳とともに、AF の不整脈基質として標的になる構造。"),
  ("oth_agnino_f7_laa_ablation.png", "agnino", "図 8-8. 左心耳基部の焼灼（Fig 7）",
   "a＝左心耳基部、b＝基部と尖部の間の焼灼。RF は <b>30 W × 90秒</b> の pre-set で、"
   "吸引で密着を確保し生理食塩水で持続冷却する。"),
  ("oth_agnino_f8_lesion_complete.png", "agnino", "図 8-9. 完成した lesion set（Fig 8）",
   "肺静脈隔離＋左房後壁隔離＋左心耳基部。"
   "3ヶ月後の電気生理学的検査で<b>ギャップを心内膜側から埋める</b>ハイブリッド戦略を前提としている。"),
  ("oth_laa_obliterative_steps.png", "laa", "図 8-10. 閉塞的左心耳閉鎖の手順（Fig 1）",
   "A→E：①左心耳の<b>遠位半分を反転</b>させ、②<b>櫛状筋に沿った斜めのライン上で 3-0 barbed 糸の"
   "巾着縫合で圧縮</b>し、③本来の向きに戻して、④ポリプロピレンの<b>2層の入口部閉鎖</b>を行う。"
   "上段が模式図、下段が対応する術中所見。"),
  ("oth_laa_obliterative_ct.png", "laa", "図 8-11. 術後 心電図同期CT による確認",
   "入口部だけを閉じる従来法では約 <b>24%</b> に造影剤の流入が残るのに対し、"
   "本法では 24例全例が <b>3〜6ヶ月のCTで完全閉鎖</b>（造影剤流入なし・残存腔なし・"
   "心嚢液貯留なし・心耳周囲血腫なし）だった。"),
  ("oth_speechbubble.png", "bubble", "図 8-12. “speech bubble” サイン",
   "心内膜側からの入口部縫合閉鎖後、心電図同期CTで左心耳内に造影剤がびまん性に充満する像。"
   "125例中CTを撮った100例で<b>完全閉鎖 76%・不完全閉鎖 24%</b>、"
   "不完全部位は<b>僧帽弁との接合部または縫合の開始点</b>に典型的だった。"),
 ],
}

# marker -> the exact heading line the block is inserted BEFORE
MARKERS = {
 "4.1": "### 4.2 展開 — 左房切開と retractor",
 "4.6": "---\n\n## 5. 大動脈弁（RAVR）",
 "5.2": "### 5.3 大動脈切開・弁の出し方・視野最適化",
 "5.3": "### 5.4 併施手技 — 根部拡大と心筋切除",
 "5.4": "### 5.5 プラットフォーム論 — 本章の核心",
 "6.2": "### 6.3 IMA 採取",
 "6.4": "### 6.5 吻合",
 "7.1": "### 7.2 AVR + 僧帽弁",
 "7.4": "### 7.5 弁 + 不整脈手術（Cox-Maze / 左心耳）",
 "8.1": "### 8.2 心臓腫瘍 — 「掴まない」ための工夫",
 "8.2": "### 8.3 不整脈・左心耳 — 「閉じたつもり」が閉じていない",
 "8.3": "### 8.4 中隔心筋切除 — 2つの到達路",
}


def block(sec):
    out = [BEGIN.format(sec)]
    for item in FIGS[sec]:
        fn, key, lead, body = item
        cite, lic = S[key]
        out.append('<figure style="margin:22px 0;">')
        out.append(
            f'<img src="figures/{PREFIX}{fn}" alt="{lead}" loading="lazy" '
            'style="width:100%;border-radius:8px;border:1px solid #e3e3e3;">')
        out.append(
            '<figcaption style="font-size:12px;color:#5b6673;margin:6px auto 0;'
            f'line-height:1.7;text-align:left;"><b>{lead}</b> — {body}'
            f'<br><i>出典: {cite}. {lic}（原図を改変せず掲載）。</i></figcaption>')
        out.append("</figure>")
    out.append(END.format(sec))
    return "\n".join(out) + "\n\n"


INDEX_BEGIN = "<!-- FIGINDEX -->"
INDEX_END = "<!-- /FIGINDEX -->"
INDEX_MARKER = "## 引用文献"


def index_block():
    rows = ["| 図 | 掲載節 | 出典 |", "|:--|:--|:--|"]
    for sec in MARKERS:
        for fn, key, lead, _ in FIGS[sec]:
            title = re.sub(r"<[^>]+>", "", lead)
            cite = re.sub(r"<[^>]+>", "", S[key][0])
            rows.append(f"| {title} | {sec} | {cite} ／ {S[key][1]} |")
    n = sum(len(FIGS[s]) for s in MARKERS)
    return (
        f"{INDEX_BEGIN}\n"
        "## 付録C 図表一覧（原典出典）\n\n"
        f"本レビューに掲載した図は**{n}点**、すべて**原典論文の Figure をそのまま切り出した**ものである。\n"
        "自作の概念図・模式図は一切含まない。動画からのコマ取りも行っていない\n"
        "（Mick らの「steps to success」は誌面図版に見えるが実体は Video 1–11 の1コマ目であるため、\n"
        "本文には掲載せず[付録A](#付録a-動画一覧術式別)の動画リンクとして扱った）。\n\n"
        "画像ファイルは `output/figures/` に `rt_` 接頭辞で格納している。\n\n"
        + "\n".join(rows)
        + "\n\n> **著作権について**\n"
        "> 掲載した図はいずれも各出版社・著者が著作権を有する論文からの抜粋であり、\n"
        "> 原典の手技を本文の記述と照合するための**個人的な参照目的**で引用している。\n"
        "> ライセンスは各図の出典行に明記した。再配布・二次利用は行わないこと。\n"
        "> 臨床判断にあたっては必ず原典を参照すること。\n\n"
        "---\n\n"
        f"{INDEX_END}\n\n"
    )


def main():
    os.makedirs(PUB_DIR, exist_ok=True)
    n_copied = 0
    for sec in FIGS:
        for fn, *_ in FIGS[sec]:
            src = os.path.join(SRC_DIR, fn)
            if not os.path.exists(src):
                raise SystemExit(f"missing figure: {src}")
            shutil.copy2(src, os.path.join(PUB_DIR, PREFIX + fn))
            n_copied += 1

    text = open(MD, encoding="utf-8").read()
    # drop previously injected blocks so the script is idempotent
    text = re.sub(r"<!-- FIG:[\d.]+ -->.*?<!-- /FIG:[\d.]+ -->\n\n?", "",
                  text, flags=re.DOTALL)
    text = re.sub(re.escape(INDEX_BEGIN) + r".*?" + re.escape(INDEX_END) + r"\n\n?",
                  "", text, flags=re.DOTALL)

    if text.count(INDEX_MARKER) != 1:
        raise SystemExit(f"figure-index marker occurs {text.count(INDEX_MARKER)}x")
    text = text.replace(INDEX_MARKER, index_block() + INDEX_MARKER)

    for sec, marker in MARKERS.items():
        if text.count(marker) != 1:
            raise SystemExit(f"marker for {sec} occurs {text.count(marker)}x: {marker!r}")
        text = text.replace(marker, block(sec) + marker)

    open(MD, "w", encoding="utf-8").write(text)
    print(f"{n_copied} figures -> {PUB_DIR}")
    print(f"{len(MARKERS)} blocks injected into {os.path.relpath(MD, REPO)}")


if __name__ == "__main__":
    main()
