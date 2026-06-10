---
title: ロボット支援下心臓手術における人工心肺(CPB)管理の注意点・Pitfall — 心臓血管外科医／臨床工学技士／麻酔科医の3視点統合レビュー
---

# ロボット支援下心臓手術における人工心肺(CPB)管理の注意点・Pitfall

**心臓血管外科医 / 臨床工学技士（灌流） / 麻酔科医 — 3つの視点からの統合レビュー**

ロボット支援下・完全内視鏡下心臓手術（主に僧帽弁・三尖弁手術、ロボットTECAB）では、人工心肺（CPB）の運用そのものが胸骨正中切開とは構造的に異なる。**閉胸・末梢送脱血・大動脈内バルーン遮断・真空補助脱血（VAVD; vacuum-assisted venous drainage）・分離換気＋CO₂送気**という5つの特徴が、通常CPBには無い固有のPitfallを生む。本稿は心臓外科系主要誌（JTCVS/JTCVS Tech、EJCTS/ICVTS、Ann Thorac Surg、Innovations）と臨床工学・灌流系誌（J Extra Corpor Technol、Perfusion、体外循環技術）＋公式ガイドライン／コンセンサス計**31本**の精読から、注意点を3職種＋チーム横断の視点で整理したものである。各記述には出典（PubMed/DOI）をハイパーリンクしており、クリックして一次資料に当たれる。

> [!tip] このドキュメントの使い方（HTML版）
> - 左サイドバーは「視点 → トピック」の目次。クリックで該当箇所へジャンプ、スクロールで現在地がハイライトされる。
> - 右上ではなく**サイドバー上部の検索窓**にキーワード（例: `VAVD`, `バルーン`, `Harlequin`, `DO2`）を入れると本文をハイライトし、`Enter`/`↑↓`で一致箇所を順に移動、件数も表示される。キーボードの `/` で検索窓にフォーカス。
> - 各引用（例: [Murzi 2013](https://pubmed.ncbi.nlm.nih.gov/23404687/)）はPubMed/DOIへのリンク。**追加学習**にはここから一次資料へ。
> - 末尾に[全文献リスト（DL状況付き）](#文献リスト全31本--dl状況付き)。

> [!warning] エビデンスの大前提
> ロボット/低侵襲CPBに関するリスク推定の多くは**観察研究（エビデンスレベルB）**で、施設の症例選択・ラーニングカーブによる交絡を含む。数値は「因果」ではなく「関連」として読み、自施設の経験・適応に当てはめて解釈すること（[Falk/ISMICS 2011](https://pubmed.ncbi.nlm.nih.gov/22437890/)、[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)、[Burns 2021](https://pubmed.ncbi.nlm.nih.gov/32519587/)）。

---

## 総論：ロボット支援下CPBがなぜ難しいのか（リスクの源泉）

通常CPBとの差分が、そのままPitfallの源になる。

1. **閉胸・術野が見えない** — 中枢（上行大動脈・右房直接）カニュレーションができず、外科医はカニューレ位置や心内空気を直接確認できない。→ 画像（TEE＝経食道心エコー ／ CT）依存。
2. **末梢送脱血（大腿/腋窩/内頸）** — 細く長いカニューレによる流量制限、**逆行性送血**による脳塞栓・大動脈解離・下肢虚血。
3. **大動脈内バルーン遮断（EndoClamp/IntraClude）** — 遊離型遮断ゆえの**移動・破裂**、無名動脈閉塞、心筋保護液送達の不安定さ。
4. **真空補助脱血(VAVD)** — 細径カニューレを成立させる代償として**ガス状微小塞栓（GME; gaseous microemboli）・溶血・リザーバ過陽圧**。
5. **分離換気（OLV; one-lung ventilation）＋CO₂気胸(capnothorax)** — 低酸素・高炭酸ガス血症、静脈還流低下、片肺虚血再灌流障害（片側肺水腫）。

これらは外科・灌流・麻酔のいずれか一職種では完結せず、**3者の協働**で初めて安全域に入る。以下、各視点で詳述する。

---

## I. 心臓血管外科医の視点

### I-1. 送脱血カニュレーション戦略と血管合併症

末梢（大腿）送血は閉胸手術の標準アクセスだが、**逆行性送血の塞栓・解離リスク**と**鼠径・下肢の血管合併症**を伴う。

> [!danger] Pitfall — 逆行性大腿送血による脳卒中・大動脈解離
> 逆行性の大腿動脈送血は、下行大動脈の粥腫・壁在血栓を剥離して脳塞栓を起こしうる。NYUでは逆行性送血が神経学的合併症の独立予測因子（OR 3.8, P=0.01）、[Murzi 2013](https://pubmed.ncbi.nlm.nih.gov/23404687/) では逆行 vs 順行で脳卒中 4.8% vs 1.2%（補正後OR 4.24, P=0.002）・術後せん妄 14.4% vs 5.2%、医原性大動脈解離 1.2% vs 0%。[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/) は逆行性医原性解離を大腿0.47% vs 中枢0.06%と報告。

> [!tip] 対策
> - **全例術前CTA（CT血管造影; CT angiography）**（胸腹部・骨盤）で大動脈・腸骨/大腿の粥腫・石灰化・蛇行・瘤を評価し、適応を判断（[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/)、[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/) はCFA（総大腿動脈; common femoral artery）径 ≥7 mm・管腔内閉塞性病変なしを推奨）。
> - 粥腫負荷の高い患者は**順行（中枢/腋窩）送血**を選択。[Nakamura 2021](https://pubmed.ncbi.nlm.nih.gov/33448282/) はCT基準（血栓>3 mm厚、円周1/3超、全周性石灰化のいずれか）で腋窩送血へ振り分け（35%が腋窩）。
> - ガイドワイヤを**TEE（経食道心エコー; transesophageal echocardiography）で下行大動脈内に確認**してからカニューレ挿入（[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/)）。カニュレーション時は**収縮期血圧<100 mmHg**で解離リスク低減（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。

> [!warning] Pitfall — 鼠径・下肢の血管/創合併症（しばしば過小評価）
> 大規模実態（[Lamelas 2017](https://pubmed.ncbi.nlm.nih.gov/28017338/), 2645例）では末梢動脈合併症0.07%・**鼠径部漿液腫/表層感染6.58%（最多）**・下肢コンパートメント症候群で筋膜切開0.08%。深部鼠径感染は0。腋窩送血は内胸筋切開・瘢痕・手技時間延長という別の代償を伴う（[Nakamura 2021](https://pubmed.ncbi.nlm.nih.gov/33448282/)）。

> [!tip] 対策
> - リンパ管損傷を避ける愛護的展開、**経皮アクセス優先**（カットダウンより創/漿液腫/リンパ瘻が少ない；[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/) は "ProGlide-first"＝失敗時にMANTAでレスキュー可能を推奨）。ただし新規施設では視認性確保のため**1–2 cmカットダウン**から開始（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。
> - **下肢遠位灌流**（6Frカニューレ）または双方向Bi-Flowカニューレで肢虚血を予防（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。
> - 腋窩は近位鎖骨下/腕頭動脈狭窄があれば禁忌。脆弱なため**8 mm Dacron側枝**を介して送血（[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/)）。
> - IVCフィルター/閉塞がある患者は大腿静脈脱血が不可 → MICS（低侵襲心臓手術; minimally invasive cardiac surgery）適応外か中枢経由を検討（[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/)）。

### I-2. 大動脈遮断：エンドアオルティックバルーン vs 経胸壁クランプ

完全内視鏡では経胸壁クランプ（Chitwood/Cygnet）かエンドバルーン（IntraClude）かを選ぶ。両者は**安全性プロファイルが異なる**。

> [!danger] Pitfall — エンドバルーンの移動・破裂・解離
> バルーンは固定式クランプと違い、**大動脈基部圧・全身血圧・カテーテル張力**で位置が動く（[Kaneyuki 2023](https://pubmed.ncbi.nlm.nih.gov/36802961/)）。遠位移動 → 腕頭動脈閉塞（右脳/右上肢虚血）、近位移動 → 冠動脈口閉塞・心筋保護不良。メタ解析で**解離リスクがクランプより高い**（同一施設プールOR 3.88, P=0.04；[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)）、Kowalewski 2017では1.5% vs 0.4%（P=.004; [Ergi 2024](https://pubmed.ncbi.nlm.nih.gov/38657703/) 引用）。**胸骨切開への転換**もバルーンで高率（プールOR 3.07, P=0.009）で、多くが早期ラーニングカーブに集中。

> [!tip] 対策
> - 適応を厳格化：**上行大動脈>40 mm（device仕様20–38 mm）・有意なAR（大動脈弁逆流; aortic regurgitation）・著明な蛇行/粥腫・大腿石灰化は禁忌**（[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)、[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)、[Breves 2016](https://pubmed.ncbi.nlm.nih.gov/27607762/)）。径だけでなく**年齢・性・BSA（体表面積; body surface area）に対する期待径比**で判断（安全示唆は最大130%まで；[Breves 2016](https://pubmed.ncbi.nlm.nih.gov/27607762/)）。
> - 拡張大動脈では**固定容量でなくバルーンを生理的エンドポイント（大動脈基部圧が0になるまで）で滴定**して閉塞（[Breves 2016](https://pubmed.ncbi.nlm.nih.gov/27607762/)）。
> - 心筋保護液送達後は**カテーテルのslackを排除しロック**（近位移動防止；[Kaneyuki 2023](https://pubmed.ncbi.nlm.nih.gov/36802961/)）。
> - **バックアップ（クランプ／冷却細動下停止／胸骨切開）を必ずリハーサルし、術前同意**を取る（[Breves 2016](https://pubmed.ncbi.nlm.nih.gov/27607762/)）。
> - 経胸壁クランプはChitwood/Cygnetを第3–4肋間から。多くの施設が解離・移動を嫌いバルーンからクランプへ移行している（[Murzi 2013](https://pubmed.ncbi.nlm.nih.gov/23404687/)）。

> [!note] 時間の誤解に注意
> バルーンの利点は**遮断（虚血）時間短縮ではない**。[Ergi 2024](https://pubmed.ncbi.nlm.nih.gov/38657703/)（前向きMayo）では遮断時間64.0 vs 64.0分（差なし）・総手術時間も不変で、**CPB時間のみ約10分短縮**（84.0 vs 94.5分, P=.006、大動脈カテ抜去のための再送血を省けるため）。心筋保護計画はクランプと同一に立てる。

### I-3. 心筋保護（順行性／逆行性心筋保護）

> [!warning] Pitfall — 閉胸下での心筋保護不良
> 内視鏡下は遮断時間が延びやすく、AR合併時は順行性心筋保護液がLVへ逆流して保護不良＋LV過伸展を招く。逆行性単独はRV/中隔の保護が遅く不完全（順行30–60秒 vs 逆行2–4分；[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。RCA（右冠動脈; right coronary artery）起始が高位だとバルーンでRCA口を塞ぎRV保護不良（[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)）。

> [!tip] 対策
> - 遷延遮断・高度CAD・AR例は**順行＋逆行併用**。逆行性は冠静脈洞圧を低め（~50 mmHg）に、カテーテルを進め過ぎない（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。
> - 大動脈基部圧（バルーン中央腔）を**>30 mmHg・流量≥250 mL/min**で監視、TEEで左右冠動脈血流を確認（[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)）。
> - del Nido単回投与でも**予定遮断時間が1時間超なら40分で再投与**（実経過でなく予定で先回り；median遮断64分のため再投与はほぼ定型；[Ergi 2024](https://pubmed.ncbi.nlm.nih.gov/38657703/)）。

### I-4. 緊急時転換（コンバージョン）への備え

> [!danger] Pitfall — 閉胸ゆえの危機対応の遅れ
> 末梢CPBの閉胸構成では、出血・血行動態破綻時に**小開胸/胸骨切開への迅速転換**が要る。転換は出血が最多原因で、**出血による転換の死亡率は20–24%**（[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)、[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。肝損傷（右アーム/横隔膜縫合）など術野外の隠れ損傷もある（[Ergi 2024](https://pubmed.ncbi.nlm.nih.gov/38657703/)）。

> [!tip] 対策
> - **転換手順をフェーズI（シミュレーション）でリハーサル**、ロボット迅速アンドック、役割分担・チェックリスト・閉ループ通信を確立（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。常時、胸骨切開に備え消毒・ドレープ、カニュレーション部位を即アクセス可能に（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。
> - 大量輸血・体位変換の人員を確保（[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)）。転換率は経験で約14%→2.5%へ低下（[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)、[Falk/ISMICS 2011](https://pubmed.ncbi.nlm.nih.gov/22437890/) 平均3.4%）。

### I-5. 中枢カニュレーション・再手術の落とし穴

> [!warning] Pitfall — 中枢/末梢の二者択一は単純でない
> 中枢上行大動脈カニュレーションは逆行性リスクを排除し適応を広げる一方、技術的に難しく医原性解離は低頻度だが死亡率15–50%（[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/)、[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/) は解離0.01–0.09%）。再手術では末梢CPBが一律に安全とは限らず、独立した死亡予測因子になりうる（Brown: 18.7% vs 7.5%, HR 1.53；[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/)）。

> [!tip] 対策
> 解剖・リスクに基づく**個別化アルゴリズム**で選択。CPB開始後はTEEで解離を能動的に除外し、高ライン圧＋低全身圧は解離/カニューレ誤位置を疑う（[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/)、[Werner 2025](https://pubmed.ncbi.nlm.nih.gov/40261087/)）。触診でなく**epiaortic超音波**で軟性プラークを避けて遮断/送血部位を選ぶ（[Ramchandani 2016](https://pubmed.ncbi.nlm.nih.gov/27127556/)）。

---

## II. 臨床工学技士（灌流）の視点

### II-1. 静脈脱血と真空補助脱血(VAVD)

細く長い大腿静脈カニューレでは重力脱血が不足し、VAVD（真空補助脱血; vacuum-assisted venous drainage）が必須となる。その代償管理がCEの中心課題。

> [!danger] Pitfall — 過陰圧による溶血・GME・チャタリング
> 過剰な陰圧は溶血（遊離Hb上昇）とGME（ガス状微小塞栓; gaseous microemboli）増加を招き、**カニューレ先端で右房が虚脱（chattering）して逆に脱血が落ちる**。実際にカニューレが受ける陰圧は**リザーバ真空＋落差サイフォン圧の合計**で、レギュレータ設定値より強くなる点に注意（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。

> [!tip] 対策（陰圧の上限）
> - **必要最小限の真空**に留める。血液損傷は**−120 mmHg超で線形に悪化**するため、**正味陰圧（落差＋VAVD）を約−100 mmHgまで**に制限（[Gambino 2015](https://pubmed.ncbi.nlm.nih.gov/26543250/)）。−40 mmHgで小径カニューレでも虚脱なく脱血可（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。EACTSは**−60 mmHgまでは溶血なく安全、過陰圧は非推奨（Class III, Level B）・陰圧監視（Class I, Level C）**（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。臨床例では**最大−40 mmHg**運用（[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)）。
> - レギュレータは**0〜−100 mmHgに制限**し、開始プリセット−20 mmHg以下、定期校正（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。
> - 多孔/自己拡張型カニューレで低陰圧でも良好な脱血を確保。BSA（体表面積; body surface area）>2.0–2.1で**SVC補助カニューレ**追加（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。

> [!danger] Pitfall — リザーバ過陽圧 → 逆行性空気塞栓
> 真空系のキンクやPPRV（陽圧リリーフ弁; positive pressure relief valve）不良で**リザーバが陽圧化**すると、重力サイフォンを超えて**静脈ラインを逆行して空気が右房へ**送られ得る。約1/4のperfusionistが経験（26.2%）し、心内シャント例では系統的（奇異性）塞栓に至る（[Gambino 2015](https://pubmed.ncbi.nlm.nih.gov/26543250/)）。非閉塞性/遠心ポンプでは陰圧が人工肺に伝わりガス側から血液側へ空気を引き込む（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。

> [!tip] 対策（安全装備）
> **陰圧/陽圧の両方向リリーフ弁**＋一方向弁、**陽圧側でトリガする小さな閾値のアラーム**（負圧側だけでは不可）、リザーバ実圧のリアルタイム監視。PPRVは単独では不十分（+40 mmHg超を漏らす個体あり）で監視・サーボ制御を併用（[Gambino 2015](https://pubmed.ncbi.nlm.nih.gov/26543250/)、[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。AmSECT標準では**補助脱血時は静脈リザーバ圧監視（Standard 6.1）**を必須化（[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)）。

### II-2. ガス状微小塞栓(GME)と脱気・空気塞栓

> [!danger] Pitfall — VAVDがGME送達を約10倍に増幅
> 静脈側に空気が引き込まれると、VAVDは動脈ラインへのGME送達を**重力脱血比で約10倍**に増やす（不完全な閉鎖系＝縫合糸の小さな裂け目でも）。高真空・高流量・拍動流・温度勾配・冷却perfusateが各々GMEを増やす（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。GMEは目視不能（<200 µm）で神経認知障害の原因。

> [!tip] 対策
> - **真に閉鎖した系**を保ち、動脈ラインに気泡を見たら**直ちにVAVDを止めてリーク源を探す**（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。
> - **リアルタイムGMEモニタ**（EDAC等、動静脈ラインで同時検出）で発生源を特定（[Wang & Ündar 2008](https://pubmed.ncbi.nlm.nih.gov/19192754/)）。
> - **マクロ気泡検出器が動脈ポンプを制御**する構成、**動脈ラインフィルタ**と**ベント一方向弁**は必須（AmSECT Standard 6.2/6.5/6.6）。低レベルセンサが動脈ポンプをサーボ制御（6.3）（[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)）。
> - 閉胸ゆえ用手的脱気ができないため、**CO₂を術野へ充満**（カメラポートから）、TEE（経食道心エコー; transesophageal echocardiography）で心内空気消失を確認するまで大動脈基部ベントを留置（[Falk/ISMICS 2011](https://pubmed.ncbi.nlm.nih.gov/22437890/)、[Murzi 2013](https://pubmed.ncbi.nlm.nih.gov/23404687/)、[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。

### II-3. 遠心ポンプ・MiECC回路の落とし穴

> [!danger] Pitfall — VAVD＋遠心ポンプで「表示流量」が実送血量を覆い隠す
> 遠心ポンプは前負荷依存のため、VAVDの陰圧で**実際に患者へ送られる順行流量が低下**する（設定回転数は不変でも）。in vitroで−80 mmHg時、1500→590 mL/min（**60.4%減**）、2000→1220、2500→1830 mL/min。**低流量域ほど損失割合が大きい**（[Guimarães 2020](https://pubmed.ncbi.nlm.nih.gov/32369291/)）。動脈フィルタのパージライン等のシャントも真空で盗血が増える（−80 mmHgで全流量の最大80%）。

> [!tip] 対策
> - **動脈側に独立した流量プローブ**を設置し「実送血量」を直接監視（表示値を信用しない）。遠心ポンプ使用時は特に必須（[Guimarães 2020](https://pubmed.ncbi.nlm.nih.gov/32369291/)）。
> - 遠心ポンプは**逆流防止策**（一方向弁/ハードストップ/電動クランプ/低速アラームのいずれか）が必須（AmSECT Standard 6.7；[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)）。
> - **MiECC（低侵襲体外循環＝小型閉鎖回路; minimally invasive extracorporeal circulation）**は希釈・炎症・輸血・脳GMEを減らす一方、**静脈リザーバが無く空気/容量管理が脆弱**。静脈バブルトラップ/脱気装置を組み込み、**緊急時に開放系へ即転換できるハイブリッド（第4世代）**を用いる（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)、[Anastasiadis 2019](https://pubmed.ncbi.nlm.nih.gov/31293801/)）。

### II-4. 適正灌流量・酸素供給(DO₂/VO₂)と灌流モニタリング

> [!warning] Pitfall — MICS（低侵襲心臓手術; minimally invasive cardiac surgery）では「PI（灌流指数＝体表面積あたりの基準流量; perfusion index）」が達成できない
> 大腿カニューレ径に流量が制約され、成人標準PI 2.2–2.8 L/min/m²を出せない（ある研究では目標≥2.0に対し**実測中央値1.7**）。固定したPI/DO₂（DO₂＝酸素供給量 oxygen delivery、VO₂＝酸素消費量 oxygen consumption）目標を追うのは誤りで、希釈・低体温で代謝も変動する（[Hara 2024](https://doi.org/10.7130/jject.51.464)）。

> [!tip] 対策（GDP＝目標指向的灌流; goal-directed perfusion）
> - **絶対DO₂iでなく酸素需給比（VO₂i/DO₂i, 酸素摂取率）で管理**。VO₂i/DO₂i ≥0.245（=DO₂iが4×VO₂i未満）で高乳酸・AKI（急性腎障害; acute kidney injury）増（AKI 28% vs 9%, P=0.049）。**DO₂iをVO₂iの4倍以上・乳酸<2 mmol/Lに保つ**（[Hara 2024](https://doi.org/10.7130/jject.51.464)）。
> - EACTSは**最低DO₂ 280 mL/min/m²（Class I, Level A）**でAKI低減、昇圧でなくGDPを推奨。MAP（平均動脈圧; mean arterial pressure）<50・心係数<1.6が死亡予測（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。
> - **CO₂送気中はVCO₂由来指標が不正確**（術野CO₂がリザーバ静脈血に混入）。乳酸も低体温・アドレナリン・乳酸リンゲルで上昇するため単独では不可（重炭酸プライム推奨）。在線血ガス＋脳オキシメトリで多角的に（[Hara 2024](https://doi.org/10.7130/jject.51.464)、[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)）。
> - MICSは流量2.2–2.6 L/min/m²・最低体温32℃前後で**予備が乏しい**ため、複数経路（両大腿/大腿＋腋窩/中枢）のバックアップを準備（[Nakamura 2021](https://pubmed.ncbi.nlm.nih.gov/33448282/)）。

### II-5. 吸引回路と血液損傷

> [!warning] Pitfall — フレキシブルサッカーの過陰圧
> 視野確保で多用されるフレキシブルサッカー（細径・高抵抗）は、ローラーポンプ吸引で**理論1,000 mL/minで既に−100 mmHg超**、1,600 mL/minで**−199 mmHg**に達し許容陰圧を大きく超える。吸引嘴管は同条件で−71 mmHg（[Oshima/Tojo 2024](https://doi.org/10.7130/jject.51.138)）。

> [!tip] 対策
> - 可能なら**吸引嘴管を優先**。フレキシブルサッカー使用時は**800 mL/min程度（−100 mmHg以下）**に抑え、必要時は**複数系統で陰圧を分散**。表示（理論）流量は実吸引より最大13%低いため、**貯血量を見て実流量で管理**（[Oshima/Tojo 2024](https://doi.org/10.7130/jject.51.138)）。
> - 嘴管は先端の詰まり・先当たりで過陰圧＋空気混入の乱流→溶血。脱血圧基準−60〜−100 mmHg超過を避ける。cardiotomy suctionは血液損傷の主因なので短時間運用を（[Oshima/Tojo 2024](https://doi.org/10.7130/jject.51.138)）。

### II-6. 回路安全装備・チェックリスト・AmSECT標準

> [!danger] Pitfall — チェックリスト省略・単独施行で移行期のエラーが見逃される
> 重大エラーはセットアップ・開始・離脱・再CPBという**移行点に集中**する。VAVDのリーク（52.4%が経験）・レギュレータ不良（33.3%）・壁吸引不良（33.3%）はCPB開始時に脱血不能を起こす。VAVD圧の記録は28.4%、両方向アラームは51.6%にとどまる（[Gambino 2015](https://pubmed.ncbi.nlm.nih.gov/26543250/)）。

> [!tip] 対策（AmSECT標準）
> - **全例チェックリスト（2名read-verify、全フェーズ）**（Standard 4.1、Guideline 4.1–4.2）。
> - **患者個別の灌流計画を術前ブリーフで共有、閉ループ通信**（Standard 5.1、Guideline 5.2）。
> - 連続監視：動脈圧・ライン圧・流量・温度・血ガス・Hct（ヘマトクリット; hematocrit）・FiO₂/ガス流量・静脈飽和度（Standard 7.1–7.10）。**動脈出口温度アラーム**（過温防止, 6.4）。
> - 抗凝固は**ACT（活性化凝固時間; activated clotting time）アルゴリズム＋ヘパリン抵抗/HIT（ヘパリン起因性血小板減少症; heparin-induced thrombocytopenia）代替策**を事前規定（Standard 8.1）、長時間CPB(>2–3h)は高濃度ヘパリン維持（Class IIb）。
> - **予測希釈後Hctを算出しチームへ伝達**、回路容量最小化（Standard 9.1–9.3）。**ハンドクランク・予備ガス/電源・機器故障対応文書**を常備（Standard 6.9–6.11, 14.3–14.4）。勤務間休息（16時間あたり8時間）も標準（15.1）。すべて[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)。

---

## III. 麻酔科医の視点

### III-1. TEEガイド下カニュレーション（盲目的留置を避ける）

> [!danger] Pitfall — 盲目的末梢カニュレーションによる致命的血管/心損傷
> 閉胸で外科医は大血管を直視できず、ガイドワイヤ/カニューレが誤位置・穿孔しうる（肝静脈誤挿入、右房/右室/心房中隔穿孔；[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)）。透視ガイドは合併症7.14%・成功92.86%だったがTEE（経食道心エコー; transesophageal echocardiography）で穿孔0.78%に改善（[Wang 2012](https://pubmed.ncbi.nlm.nih.gov/22964315/)）。

> [!tip] 対策
> **TEEで全ステップを確認**：大腿静脈ワイヤ→右房→SVC（ME bicaval）、大腿動脈ワイヤを下行大動脈に確認（desc aortic SAX）、エンドバルーンワイヤを下行→上行へ。IVCカニューレ先端は心房-大静脈接合部直下、二段カニューレはSVCへ。解離・SVC損傷を早期除外（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)、[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)、[Wang 2012](https://pubmed.ncbi.nlm.nih.gov/22964315/)）。TEE不能は**MICS（低侵襲心臓手術; minimally invasive cardiac surgery）そのものの禁忌**に近い（RV/バルーン/AR（大動脈弁逆流; aortic regurgitation）評価ができない；[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)、[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。

### III-2. エンドバルーン位置・移動のモニタリング

> [!danger] Pitfall — 片側監視ではバルーン移動を見逃す
> バルーンが遠位移動して腕頭動脈を閉塞すると**右橈骨動脈圧・右脳NIRS（近赤外分光法＝脳局所酸素モニタ; near-infrared spectroscopy）のみ低下**する。片側（特に左のみ）監視では検出できない。左房開放後はTEEで気体介在によりバルーンが見えなくなる**監視の盲点**が生じる（[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)、[Falk/ISMICS 2011](https://pubmed.ncbi.nlm.nih.gov/22437890/)）。

> [!tip] 対策（多モーダル監視）
> - **両側橈骨（上肢）動脈圧＋両側脳NIRS＋大動脈基部圧＋TEE**を併用。バルーン移動の早期検出は**両側動脈圧（脳オキシメトリより速い）**（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)、[Kaneyuki 2023](https://pubmed.ncbi.nlm.nih.gov/36802961/)）。
> - 上行大動脈**<3.8 cm**をTEEで確認してからバルーン遮断、250–300 mmHgへ加圧はTEE確認後（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。両側脳オキシメトリ>20%低下（位置正常なら）→ 段階的に脳酸素供給を最適化（昇圧・FiO₂・Hct・麻酔深度/体温）（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。
> - 左房開放後は**TEEに頼らず**両側上肢圧・基部圧・脳NIRSで監視（[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)）。送血側と同側の動脈ラインは「ライン圧」を見ている点に注意（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。
> - 二腔チューブなら気管支カフを生食充填し**音響窓**を作ってバルーンを描出（左主気管支の空気で上行大動脈が隠れる対策；[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)）。

### III-3. 逆行性灌流の生理：Harlequin/differential hypoxemia と橈骨-大腿圧較差

> [!danger] Pitfall — Differential hypoxemia（Harlequin/north-south症候群）
> 大腿（逆行性）送血中、拍動する心臓が**低酸素の自己肺由来血を駆出**し、逆行する酸素化血との混合点（watershed）が弓部より遠位だと、**上半身・脳が低酸素血で灌流**される。非拍動流ではパルスオキシが無効になる点も（[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)、[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。

> [!tip] 対策
> **脳NIRSの急低下で即認識**。no-flow扱いの間も肺を換気し、心が駆出する血を酸素化する。右上肢パルスオキシを併用（[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)、[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。

> [!warning] Pitfall — 橈骨動脈圧が中枢圧を過小評価
> 逆行性灌流では**橈骨収縮期圧が大腿/中枢より有意に低く**読まれ、**離脱時に較差が最大（23±16 mmHg、54%で≥20 mmHg）**。perfusionist（大腿/回路側）と麻酔科（橈骨側）で「実圧」の認識がずれる（[Nakamura 2018](https://pubmed.ncbi.nlm.nih.gov/29998763/)）。

> [!tip] 対策
> 収縮期は信頼せず**平均血圧(MAP)で管理**（MAP較差≥20 mmHgは9%のみ）。離脱・遮断解除前後は特に較差が開くため、**橈骨単独で灌流圧を判断しない**。どの値を目標にするかをチームで明示（[Nakamura 2018](https://pubmed.ncbi.nlm.nih.gov/29998763/)）。逆行性は脳卒中だけでなく神経学的合併症全般の関連（[Burns 2021](https://pubmed.ncbi.nlm.nih.gov/32519587/)）— 死亡/腎は不変でも**神経学的監視を優先**。

### III-4. 分離換気(OLV)とCO₂気胸(capnothorax)

> [!danger] Pitfall — capnothorax過圧・OLV不耐
> 外科医が要求する10–15 mmHgの送気は**静脈還流低下・心係数/MAP/SvO₂低下・緊張性capnothorax**を起こしうる（最適は5–10 mmHg）。OLV（分離換気; one-lung ventilation）はPaO₂を最大51%低下、高炭酸ガスはヘパリン効果を下げ回路血栓・冠攣縮の一因（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)、[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。

> [!tip] 対策
> - 送気は**5–10 mmHg**、不安定なら**まず500 mL輸液→昇圧**、改善なければ左胸を脱気し昇圧後に再送気。胸腔内圧を18Gで測定・余剰CO₂を排出（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。前毛細血管性肺高血圧では相対禁忌（[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。
> - 安静時PaCO₂>50 mmHgやPaO₂<65 mmHgはOLV不耐＝内視鏡手術不適。FEV1<40%/DLCO<40%等を術前評価。非換気側CPAP＋換気側PEEP・高FiO₂、不耐なら**両肺換気へ転換**する計画を（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)、[White 2021](https://pubmed.ncbi.nlm.nih.gov/33841977/)）。
> - **CO₂気胸のタイミング**：bicaval脱血カニュレーション完了前にcapnothoraxを作ると右房虚脱でTEE bicaval像が得られない（[Singh 2026](https://pubmed.ncbi.nlm.nih.gov/41162279/) が問題提起）。

> [!warning] Pitfall — 片側肺水腫（CPB関連・高死亡）
> 手術側肺の虚血再灌流障害により**片側性肺水腫**が約1.4%、その死亡寄与は大きい（11例中5例；[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。対策はMurphyバンドル：CPB開始時に気管支カフ脱気・人工呼吸器離脱（room air）・能動冷却28–32℃・MAP 65・無加温CO₂・早期に肺血流再開・復温時抗炎症（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。

### III-5. 逆行性心筋保護のための冠静脈洞(CS)カテーテル

> [!danger] Pitfall — 経皮CSカテーテルの malposition・穿孔・無効保護
> 経皮CS（冠静脈洞; coronary sinus）カテーテル（内頸→9F）の盲目的進入は**右房/右室/CS穿孔・左房解離**を起こし、閉胸では胸骨切開を要しうる（CS損傷でsternotomy転換例；[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)、[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。**遺残左SVC・unroofed CS**があると逆行性保護が無効化。挿入操作でVT（心室頻拍 ventricular tachycardia; 要除細動）も。経皮CS留置は**約6%が留置失敗、成功例でも約10%は逆行単独で停止維持できず**（[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)）。

> [!tip] 対策
> - **TEEで先端を常時直視**し愛護的に操作。中食道変法bicaval/四腔/30–40°多平面で進める。2Dで困難なら**3D zoomのen face像**でCS口に同軸化（3D対応機・熟練が前提）（[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)）。
> - **バルーン閉塞は圧波形の"ventricularization"（静脈波→拍動波）で確認**してから注入。MCV（中心臓静脈; middle cardiac vein）等の分枝への迷入・過度のbowingをTEEで是正、深さは脱落と過挿入の間で全経路を描出（[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)）。波形がRA波なら先端は右房内（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。
> - **CS操作前に全身ヘパリン（5000単位、または100 U/kg）**、カテーテルは1000 U/100 mL生食でフラッシュ（血栓予防）。遺残左SVC（CS径>1 cmで疑う、左上肢からの撹拌生食で診断）・unroofed CSを術前に除外し、**代替（順行/併用）を準備**（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)、[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)）。
> - 静脈カニュレーション中に位置がずれるため**断続的に再確認**し、注入前にカテが正位・非クランプであることを閉ループ通信で確認（[Sun 2025](https://pubmed.ncbi.nlm.nih.gov/41139241/)）。

> [!note] その他の麻酔側デバイス
> 肺動脈ベント(EndoVent 8.3F)は非ヘパリンコートで拍動毎にPA（肺動脈; pulmonary artery）-RV間を移動し**OR外使用不可**。TEE下にバルーン生食充填で留置、搬送前に標準PAC（肺動脈カテーテル; pulmonary artery catheter）へ交換（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。PAベントは挿入時ヘパリン化、プロタミン後に抜去（[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。

### III-6. 抗凝固・出血・除細動の制約

> [!warning] Pitfall — 閉胸での除細動・出血が困難
> 内視鏡では**内部除細動が不可**、capnothoraxが通電を妨げ、ECGリードが背側/側方で虚血判読困難。外部パッドは**非手術側前方＋手術側後方**に貼り、通電前に**胸腔内器具を抜去し左肺を再膨張**（絶対）（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)、[Bernstein 2015](https://pubmed.ncbi.nlm.nih.gov/25566713/)）。VF（心室細動; ventricular fibrillation）時はアミオダロン/リドカイン投与・CO₂排出・両肺換気再開。術後出血は心嚢部分開放のため**右胸腔に潜在貯留**し検出が遅れる（[Heine 2026](https://pubmed.ncbi.nlm.nih.gov/41130847/)）。

> [!tip] 対策
> プロタミン投与・脱カニュレーション後は**MCS（機械的循環補助; mechanical circulatory support）の再確立が困難**になるため、TEEで修復・止血を確認するまでカニューレ温存・プロタミンを遅らせる。出血は「数値でなく出血そのもの」を治療、30分で累積>100 mLは再評価、フィブリノゲン製剤(RiaSTAP 25–75 mg/kg)を即時補正用に準備（[Fitzgerald 2020](https://pubmed.ncbi.nlm.nih.gov/30930139/)）。

---

## IV. チーム横断の注意点（外科・灌流・麻酔の協働）

### IV-1. 術前画像評価と患者選択

> [!tip] 全例で共有すべき選択基準
> - **術前CTA（CT血管造影; CT angiography。胸腹部・骨盤を3D再構成）**で大動脈・腸骨/大腿を評価：CFA（総大腿動脈; common femoral artery）径≥7 mm、管腔内閉塞性病変なし、上行大動脈の高度粥腫は**MICS（低侵襲心臓手術; minimally invasive cardiac surgery）自体の除外**（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)、[Nakamura 2021](https://pubmed.ncbi.nlm.nih.gov/33448282/)）。
> - **エンドバルーン**は上行>40 mm・有意AR（大動脈弁逆流; aortic regurgitation）・著明蛇行/粥腫・大腿石灰化で禁忌（[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)、[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)、[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。
> - 大動脈基部/上行の拡張・石灰化、中等度以上のARはロボット手術の**強い禁忌**（経胸壁遮断・順行心筋保護が不成立；[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。重度肺高血圧・高度肺気腫・右胸既往はOLV（分離換気; one-lung ventilation）/小開胸不耐で禁忌（[Murzi 2013](https://pubmed.ncbi.nlm.nih.gov/23404687/)）。

### IV-2. マルチモーダル・モニタリングの統合

> [!tip] 「単一モダリティに頼らない」が共通原則
> バルーン位置は動的で、**TEE（経食道心エコー; transesophageal echocardiography）・両側上肢動脈圧・大動脈基部圧・両側脳NIRS（近赤外分光法＝脳局所酸素モニタ; near-infrared spectroscopy）・ロボットカメラの蛍光直視**を同時に統合して判断（[Kaneyuki 2023](https://pubmed.ncbi.nlm.nih.gov/36802961/)、[Pisano 2021](https://pubmed.ncbi.nlm.nih.gov/33717574/)）。逆行性灌流では**頭部＋両下肢のrSO₂（局所脳酸素飽和度; regional cerebral O₂ saturation）**を測定（[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。TEEは必須だが食道穿孔等のリスク（罹病0.08%）もあり熟練者が施行（[Wahba/EACTS 2024](https://pubmed.ncbi.nlm.nih.gov/39949326/)）。

### IV-3. ラーニングカーブ・施設/チーム基準

> [!warning] Pitfall — 経験不足での高度手技の早期導入
> 脳卒中・転換・解離の多くが**早期症例に集中**（脳梗塞: 初期500例2% → 後期0.8%；[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。エンドバルーン/経皮カニュレーションは技術リスクが高く、新規施設の早期導入は危険（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。

> [!tip] 対策（施設・チーム基準）
> - **専任の体外循環認定士（≥1名）・年間CPB ≥100例（STS基準は≥250 adult/yr×3年）・TEE熟練麻酔科医・即時MCS（機械的循環補助; mechanical circulatory support）**を導入前に確保（[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)、[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。
> - 段階的導入：経皮カニュレーション/エンドバルーンはフェーズIV（既に内視鏡経験豊富なら≥50例/2年でII–III）。再手術はフェーズIV。VF（心室細動; ventricular fibrillation）停止は大動脈弁が健常な場合のみ（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。
> - **遮断・CPB時間を必須記録**し、最初の100例は25例ごとに成績レビュー（O/E≤1）、胸骨正中切開と同等に近づける（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)）。看護師・臨床工学技士・麻酔を含む**チーム訓練**（[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。

### IV-4. コミュニケーション・チェックリスト・緊急転換

> [!tip] 共通対策
> - **術前ブリーフで患者個別計画を共有、閉ループ通信、術後デブリーフ**（[Baker/AmSECT 2013](https://pubmed.ncbi.nlm.nih.gov/24303597/)）。送血方向・目標流量・遮断法・心筋保護法を「意図的な症例別決定」として明文化（[Burns 2021](https://pubmed.ncbi.nlm.nih.gov/32519587/)）。
> - **転換のリハーサル**、消毒・ドレープ・カニューレ温存で常時備える。機器故障時の対応を術前同意に明記（[Badhwar/STS 2026](https://pubmed.ncbi.nlm.nih.gov/41619927/)、[Shimokawa 2019](https://doi.org/10.11281/shinzo.51.18)）。

### IV-5. エビデンスの限界

> [!note]
> 本稿の数値の多くは観察研究（Level B）に基づき、症例選択・ラーニングカーブの交絡を含む。EABO vs EACも30研究中の直接比較は7研究のみで、1996–2016の時代変遷（EABO→EAC）と経験で結果が変わる（Port Accessレジストリで解離1.3%→0.2%）。**自施設の経験・適応で再解釈**し、同意・チーム計画でエビデンスの質の低さを共有すること（[Falk/ISMICS 2011](https://pubmed.ncbi.nlm.nih.gov/22437890/)、[Khan 2018](https://pubmed.ncbi.nlm.nih.gov/29506260/)、[Burns 2021](https://pubmed.ncbi.nlm.nih.gov/32519587/)）。

---

## 文献リスト（全31本）— DL状況付き

> [!info] 凡例
> ✅ = `robotic_cpb/pdf/` に全文取得済 ／ 🔒 = 要購読（本稿は要旨で反映）。リンクはPubMed/DOI（追加学習用）。

### ガイドライン・コンセンサス／ステートメント
1. ✅ Wahba A, et al. **2024 EACTS/EACTAIC/EBCP Guidelines on cardiopulmonary bypass in adult cardiac surgery.** Eur J Cardiothorac Surg 2025;67(2):ezae354. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39949326/) ・ [DOI](https://doi.org/10.1093/ejcts/ezae354)
2. ✅ Falk V, et al. **MICS vs open mitral valve surgery: ISMICS 2010 consensus statement.** Innovations 2011;6(2):66-76. [PubMed](https://pubmed.ncbi.nlm.nih.gov/22437890/)
3. ✅ Badhwar V, et al. **STS Expert Consensus Pathway for Robotic Cardiac Surgical Training.** Ann Thorac Surg 2026;121(5):1038-1048. [PubMed](https://pubmed.ncbi.nlm.nih.gov/41619927/)
4. ✅ Baker RA, et al. **AmSECT Standards and Guidelines for Perfusion Practice: 2013.** J Extra Corpor Technol 2013;45(3):156-166. [PubMed](https://pubmed.ncbi.nlm.nih.gov/24303597/)

### 送脱血カニュレーション・血管合併症
5. ✅ Werner P, et al. **Femoral versus central cannulation (State-of-the-art review).** Innovations 2025;20(2):148-157. [PubMed](https://pubmed.ncbi.nlm.nih.gov/40261087/)
6. ✅ Ramchandani M, et al. **Cannulation strategies and pitfalls in MICS.** Methodist DeBakey Cardiovasc J 2016;12(1):10-13. [PubMed](https://pubmed.ncbi.nlm.nih.gov/27127556/)
7. ✅ Nakamura Y, et al. **Axillary vs femoral cannulation, CT-based criteria (270例).** Eur J Cardiothorac Surg 2021;59(6):1200-1207. [PubMed](https://pubmed.ncbi.nlm.nih.gov/33448282/)
8. ✅ Lamelas J, et al. **Complications associated with femoral cannulation during MICS (2645例).** Ann Thorac Surg 2017;103(6):1927-1932. [PubMed](https://pubmed.ncbi.nlm.nih.gov/28017338/)

### 大動脈遮断（エンドバルーン vs クランプ）
9. ✅ Khan H, et al. **External aortic clamping vs endoaortic balloon occlusion: systematic review/meta-analysis.** Interact Cardiovasc Thorac Surg 2018;27(2):208-214. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29506260/)
10. ✅ Pisano C, et al. **Imaging and monitoring with an intra-aortic occlusion device.** J Thorac Dis 2021;13(2):1011-1019. [PubMed](https://pubmed.ncbi.nlm.nih.gov/33717574/)
11. ✅ Breves SL, et al. **Endoballoon occlusion feasible despite moderately enlarged aorta.** Innovations 2016;11(5):355-359. [PubMed](https://pubmed.ncbi.nlm.nih.gov/27607762/)
12. ✅ Ergi DG, et al. **Cross-clamp vs balloon occlusion in robotic mitral surgery (prospective).** Ann Thorac Surg 2024;118(2):412-419. [PubMed](https://pubmed.ncbi.nlm.nih.gov/38657703/)
13. 🔒 Kaneyuki D, et al. **Endoaortic balloon occlusion in totally endoscopic & percutaneous robotic cardiac surgery.** Innovations 2023;18(1):90-96. [PubMed](https://pubmed.ncbi.nlm.nih.gov/36802961/)

### 逆行性灌流・脳卒中
14. ✅ Murzi M, et al. **Antegrade vs retrograde perfusion in MICS mitral (1280例, propensity).** Eur J Cardiothorac Surg 2013;43(6):e167-72. [PubMed](https://pubmed.ncbi.nlm.nih.gov/23404687/)
15. 🔒 Burns DJP, et al. **Retrograde arterial perfusion in MICS mitral: systematic review.** Perfusion 2021;36(1):11-20. [PubMed](https://pubmed.ncbi.nlm.nih.gov/32519587/)
16. 🔒 Nakamura Y, et al. **Radial vs femoral pressure difference under retrograde perfusion.** Int J Artif Organs 2018;41(10):635-643. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29998763/)

### 静脈脱血(VAVD)・GME・吸引・回路
17. ✅ Wang S, Ündar A. **VAVD and gaseous microemboli in CPB (review).** J Extra Corpor Technol 2008;40(4):249-256. [PubMed](https://pubmed.ncbi.nlm.nih.gov/19192754/)
18. ✅ Gambino R, et al. **VAVD: a 2014 safety survey.** J Extra Corpor Technol 2015;47(3):160-166. [PubMed](https://pubmed.ncbi.nlm.nih.gov/26543250/)
19. ✅ Guimarães DP, et al. **Impact of VAVD on forward flow with a centrifugal pump.** Braz J Cardiovasc Surg 2020;35(2):134-140. [PubMed](https://pubmed.ncbi.nlm.nih.gov/32369291/)
20. ✅ 大島弘之・東條圭一ほか. **吸引カニューレの違いによる吸引回路の流量特性および圧変化に関する実験的検討.** 体外循環技術 2024;51(2):138-143. [DOI/J-STAGE](https://doi.org/10.7130/jject.51.138)
21. ✅ Anastasiadis K, et al. **MiECC: state-of-the-art in perfusion.** J Thorac Dis 2019;11(Suppl 10):S1507-S1514. [PubMed](https://pubmed.ncbi.nlm.nih.gov/31293801/)

### 灌流量・酸素需給（DO₂/VO₂）
22. ✅ 原怜史ほか. **MICSにおける酸素供給量と酸素消費量を用いた適正灌流量の検討.** 体外循環技術 2024;51(4):464-468. [DOI/J-STAGE](https://doi.org/10.7130/jject.51.464)

### モニタリング・TEE
23. ✅ Wang Y, et al. **TEE-guided cannulation for peripheral CPB in robotic cardiac surgery.** Chin Med J (Engl) 2012;125(18):3236-3239. [PubMed](https://pubmed.ncbi.nlm.nih.gov/22964315/)
24. ✅ Sun KW, et al. **Percutaneous coronary sinus catheter placement/management with TEE in robotic mitral surgery.** Echocardiography 2025. [PubMed](https://pubmed.ncbi.nlm.nih.gov/41139241/)
25. 🔒 Singh P, et al. **Capnothorax timing and echocardiographic challenges in robotic mitral valve surgery.** J Cardiothorac Vasc Anesth 2026;40(1):406-407. [PubMed](https://pubmed.ncbi.nlm.nih.gov/41162279/)

### 麻酔・灌流レビュー（ロボット/内視鏡）
26. ✅ Bernstein WK, Walker A. **Anesthetic issues for robotic cardiac surgery.** Ann Card Anaesth 2015;18(1):58-68. [PubMed](https://pubmed.ncbi.nlm.nih.gov/25566713/)
27. ✅ Fitzgerald MM, et al. **Robotic Cardiac Surgery Part I: anesthetic considerations (TERCS).** J Cardiothorac Vasc Anesth 2020;34(1):267-277. [PubMed](https://pubmed.ncbi.nlm.nih.gov/30930139/)
28. ✅ Heine M, et al. **Anesthetic management for endoscopic cardiac surgery.** J Cardiothorac Vasc Anesth 2026;40(2):710-723. [PubMed](https://pubmed.ncbi.nlm.nih.gov/41130847/)
29. ✅ White A, et al. **Anesthesia for minimally invasive cardiac surgery.** J Thorac Dis 2021;13(3):1886-1898. [PubMed](https://pubmed.ncbi.nlm.nih.gov/33841977/)

### 総説（本邦）
30. ✅ 下川智樹. **ロボット支援下心臓手術.** 心臓 2019;51(1):18-23. [DOI/J-STAGE](https://doi.org/10.11281/shinzo.51.18)

### 関連（要旨で補足、未取得）
31. 🔒 Condello I, et al. **The emerging role of MiECC in totally endoscopic and robotic-assisted cardiac surgery.** Perfusion 2025;40(5):1083-1087. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39244646/)

> [!note] さらなる追加学習の候補（本稿未収載・要検討）
> Colangelo 2006（VAVD in extrathoracic CPB, Perfusion; [PubMed](https://pubmed.ncbi.nlm.nih.gov/17312860/)）／Leonard 2019（術前CTで脳卒中低減のメタ解析, Int J Cardiol; [PubMed](https://pubmed.ncbi.nlm.nih.gov/30563771/)）／Anastasiadis 2022（MiECC systematic review, Perfusion; [PubMed](https://pubmed.ncbi.nlm.nih.gov/34137323/)）。
