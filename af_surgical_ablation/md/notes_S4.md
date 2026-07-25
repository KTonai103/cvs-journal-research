# 精読ノート S4 — Lesion set：biatrial vs 左房 vs PVI／Box lesion

> セッションB / 対象 8編 / 作成 2026-07-23
> 本ノートは統合レビュー執筆（セッションF）で**これだけを読めば足りる**ことを目指す。

## このセクションの結論（3-5行）

1. **biatrial（BA）vs 左房限局（LA）は決着していない。** 韓国5施設1825例のIPTW研究（Pyo 2025）は全体でBA優位（5年AF再発 28.6% vs 34.2%、SHR 1.256, 95%CI 1.121-1.406, P<.0001）だが、**三尖弁手術を要さないサブグループ（LA 397例 vs BA 322例）では優劣が逆転**（SHR 0.76, 95%CI 0.62-0.93, P=.009）。19 RCT・2031例のBayesian NMA（Guo 2021）は random-effects で PVI/LAM/BAM の3者間に有意差なし。実務解は「右房病変（TR・右房拡大・typical flutter）があればBAを足す、なければLA lesion setで足りる」であり、これは両論文の著者の到達点でもある。
2. **右房lesionの代償はペースメーカである。** Pyo研究で早期PPMは BA 29/1296 (2.2%) vs LA 2/529 (0.4%)、IPTW調整OR 0.16 (95%CI 0.07-0.38, P<.001)。ただしこの差もTV手術非施行サブグループでは消失する（OR 0.38, 95%CI 0.12-1.18, P=.095）ため、「右房lesion＝PPM」ではなく「右房病変を持つ重症例＝既存の洞不全＋PPM」と読むのが正確。
3. **後壁隔離（box lesion）の"上乗せ効果"は、カテーテル領域の2つの大規模RCTでいずれも否定された**（CAPLA 3.6年 35.5% vs 42.1%, HR 1.15, 95%CI 0.88-1.51, P=.55／CORNERSTONE AF 18か月 80.9% vs 76.8%, HR 0.76, 95%CI 0.53-1.09, P=.110）。**しかし両試験とも再アブレーション時の後壁再伝導が 75%（39/52）・66.7% と高く、検証されたのは「耐久性のない後壁隔離」である。** 心外膜側からクランプで透壁lesionを作れる外科的box lesionを、これらの陰性RCTで否定してはならない。逆に、外科側も「transmuralityを担保できないbox」なら同じ運命であることを直視すべき。
4. **一方で「線状焼灼による心房コンパートメント化」＝Cox-Mazeの設計思想は、カテーテル領域でついに2つのRCTで陽性が出た**（PROMPT-AF: HR 0.73, 95%CI 0.54-0.99, P=.045／Marshall-Plan: 86.4% vs 66.1%, P=0.012）。両試験の共通項は「Marshall静脈・冠静脈洞という**心外膜構造を処理して**僧帽弁峡部ブロックを完成させたこと」であり、これは外科が術野から無償で行える処置である。
5. **Maze失敗の主因はlesion setの選択ではなく、個々のlesionの不完全性である。** Nitta 2025 は術後ATの67%（24/36）が不完全焼灼由来、そのうち67%（16/24）が冠静脈洞のギャップと同定。Goings 2025 は Maze後再発例86例のマッピングで PV再伝導 78.3%（65/83）、cut-and-sew 5% vs cryo 67% vs RF 56%（OR 0.07 / 0.11, いずれもP<.0001）。**「どのlesion setを置くか」より「置いたlesionが本当に通っていないかを術中に検証したか」の方が効果量が大きい**（Nitta: 術中PVペーシング実施が術後AF再発の独立予測因子 OR 0.32, 95%CI 0.13-0.71, P=.004。lesion set(box/U)は OR 0.50, 95%CI 0.21-1.15, P=.11 で非有意）。

---

## 論文別ノート

### [PMID 39481591] Pyo WK, Kim JB, et al. 2025 J Thorac Cardiovasc Surg 170(2):542-550 — 試験名なし（韓国5施設 IPTW観察研究、第104回AATS 2024 Toronto 演題）

- **デザイン**: 多施設後ろ向き観察コホート（Severance／Asan／Samsung／釜山大梁山／高麗大安岩）。2005年1月〜2017年12月（Figure 1は March 2006-December 2017 と表記され本文と不一致）。傾向スコアIPTW（LA群 1/PS、BA群 1/(1-PS)、SMD<10%を均衡基準）、死亡を競合リスクとしたFine-Gray（SHR）、robust SE。R 4.3.1 + SAS 6.4。RCTではない。
- **対象**: 術前AF＋MV手術 2680例 → 同時外科的アブレーション 1841例 → 右房のみ(n=3)・マイクロ波(n=13)除外 → **N=1825（LA 529 vs BA 1296）**。
  - AF病型: 発作性 LA 118/529 (22.3%) vs BA 102/1296 (7.8%), P<.001／持続性 257 (48.6%) vs 540 (41.7%), P=.007／長期持続性 154 (29.1%) vs 654 (50.5%), P<.001。全体で持続性＋長期持続性 1605/1825 (87.9%)。
  - AF罹病期間中央値 LA 2.0か月 (IQR 0.0-22.0) vs BA 12.0か月 (IQR 1.0-72.0), P<.001。
  - 年齢中央値 LA 57.5歳 (IQR 49.0-67.3) vs BA 59.3歳 (52.1-67.1), P=.016。LA径中央値 54.0mm (49.0-60.0) vs 58.0mm (52.0-64.0), P<.001。LVEF 両群59.0%。
  - **同時三尖弁手術 LA 132/529 (25.0%) vs BA 947/1296 (75.2%), P<.001（SMD 116.1%）** ← 本研究最大の交絡。
  - LAA処理 LA 139/529 (26.3%) vs BA 866/1296 (66.8%), P<.001。
  - MV病因のうち僧帽弁狭窄: LA 160 (30.2%) vs BA 501 (38.7%)（原文は "mitral stenosis" とのみ記載。リウマチ性か否かの内訳は記載なし）。東アジアコホート。
  - IPTW後 SMD<10%前後に均衡（ただし機械弁置換 SMD 13.7%、生体弁置換 14.4% と残存不均衡）。
- **追跡**: 本文中に2記載あり。Data Collection節「median 64.5か月（IQR 37.4-102.0）、10,492.7 patient-years、臨床追跡完遂率87.6%、2021年7月まで」／Abstract・Discussion「median 70.4か月（IQR 44.1-111.2）」。**使い分けの説明は記載なし**。
- **エンドポイント定義**:
  - blanking period = **3か月**。
  - 閾値 = **>30秒**（"atrial tachycardia lasting longer than 30 seconds after the 3-month blanking period"）。AF/AFL/AT の区別は明示されず一括表記。
  - **AADの扱い = 記載なし**（off-AAD要求の規定なし）。むしろ blanking 期間中は「β遮断薬またはアミオダロンで洞調律復帰を試みる」と記載され、AAD内服下の洞調律を成功に含めるか否かは不明。Limitationでも抗不整脈療法は未測定交絡として挙げられている。
  - 副次: 全死因死亡、PPM植込み、脳卒中（"sudden onset of neurologic deficits lasting >24 hours without apparent nonvascular causes"）。
- **リズム判定**: ★**12誘導ECGを主体とし、術後3・6・12・18・24か月、以後年1回**。加えて「フォローECGで洞調律と判定された患者のみ 24時間Holterで AF-free を追加確認」。**連続モニタリング（ILR／PPMインテロゲーション）・7日イベントレコーダは不使用。24時間Holterの実施率は記載なし。** なお著者が「リズムフォロープロトコルのばらつき」に言及しているのは**本研究とCTSN（DeRose 2019）とのPPM率の差を説明する文脈**であって「5施設間のばらつき」を認めた記載ではない（施設間の未測定交絡としてLimitationに挙げられているのは術式・術後内科戦略・術者熟練度）。いずれにせよ間欠的ECG主体であり無症候性再発は相当数見逃していると考えるべき（＝両群とも再発率は過小評価）。
- **主要結果**:
  - AF再発（IPTW調整、死亡を競合リスク）— **SHR 1.256 (95%CI 1.121-1.406), P<.0001**（LA群が高リスク）。**未調整では逆方向 SHR 0.76 (95%CI 0.62-0.92), P=.005**。
  - AF再発累積発生率（IPTW調整）— LA 5年 34.2%・10年 39.2% vs BA 5年 28.6%・10年 37.6%。**10年時点では差は約1.6ポイントに収束**。粗イベント数 LA 129例 (5.2/100PY) vs BA 419例 (6.7/100PY)、競合死亡131。
  - 早期PPM（入院中）— LA 2/529 (0.4%) vs BA 29/1296 (2.2%)、IPTW調整 **OR 0.16 (95%CI 0.07-0.38), P<.001**。コホート全体の早期PPM率 1.7%。
  - 晩期PPM — LA 19例 (0.6/100PY) vs BA 71例 (0.9/100PY)。未調整 0.70 (95%CI 0.42-1.15), P=.159 → **IPTW調整 SHR 1.630 (95%CI 1.268-2.097), P=.0001**（調整で反転）。
  - 晩期死亡 — LA 50例 (1.6/100PY) vs BA 143例 (1.7/100PY)、調整 HR 1.171 (95%CI 0.735-1.863), P=.5068。
  - 晩期脳卒中 — LA 23例 (0.8/100PY) vs BA 39例 (0.5/100PY)、調整 SHR 1.208 (95%CI 0.816-1.787), P=.3446。
  - 30日死亡 LA 7/529 (1.3%) vs BA 14/1296 (1.1%)、調整OR 0.74 (95%CI 0.39-1.42), P=.368。早期脳卒中 11 (2.1%) vs 42 (3.2%)、調整OR 1.49 (0.93-2.37), P=.096。出血再開胸 26 (4.9%) vs 64 (4.9%)、調整OR 1.04 (0.77-1.59), P=.594。
  - **★三尖弁手術なしサブグループ（LA 397 vs BA 322）**: AF再発 LA 77例 (3.8/100PY) vs BA 98例 (6.0/100PY)、調整 **SHR 0.76 (95%CI 0.62-0.93), P=.009 — 全体解析と方向が逆転しLA優位**。早期PPM 1/397 (0.3%) vs 4/322 (1.2%)、調整OR 0.38 (95%CI 0.12-1.18), P=.095（差消失）。晩期PPM 調整SHR 0.81 (95%CI 0.47-1.39), P=.449（差消失）。晩期脳卒中は逆に LA不利 **SHR 1.96 (95%CI 1.13-3.38), P=.017**（LA 18例 vs BA 12例、うち18例中13例 [72.2%] はAF-freeを維持していた）。晩期死亡 調整HR 0.74 (95%CI 0.38-1.44), P=.374。
  - lesion set・エネルギー: **クライオが LA 526/529 (99.4%)、BA 1285/1296 (99.2%)、全体 1811 (99.2%)**。バイポーラRFは 3 (0.6%) vs 11 (0.9%)（本文別所では n=14 [0.08%] と分母不整合）。LA lesion = 両側PVを囲むbox ＋ boxからLAAへの連結線 ＋ boxから後尖僧帽弁輪へのmitral isthmus線 ＋ 心外膜冠状静脈洞lesion。RA lesion = cavo-cavo線 ＋ RA自由壁-三尖弁輪線 ＋ CTI（modified Cox-maze III準拠）。
  - At-risk（IPTW重み付け後、0/3/6/9/12年）: BA 1795→1129→651→310→85、LA 1799→919→399→190→57。**12年時点では両群100例前後以下で10年推定の信頼性は限定的**。
- **限界**:
  - 【著者】後ろ向き交絡、5施設間の術後内科戦略・術者熟練度の未測定交絡、コホート構築時の選択バイアス、抗凝固情報および心房収縮回復のECGデータ欠如、LAA処置が過小施行（研究期間はLAAOS III以前）、脳卒中イベント数が少ない。
  - 【読み手】(a) **未調整とIPTW調整で結果の方向が完全に反転**（AF再発 0.76→1.26、晩期PPM 0.70→1.63）。TV手術のSMDが116.1%と極端で、IPTWの重みで無理に均衡させた推定の不安定性が疑われる。(b) それを裏づけるようにTV手術なしサブグループで結論が逆転。**「BAが優れる」という主論はTV手術を要する重症例に駆動されている可能性が高く、lesion setの効果と右房病態の効果を分離できていない**。(c) リズム判定が間欠的ECG中心・年1回で、24時間Holterは「洞調律だった患者のみ」に追加。実施率も不明。(d) 追跡期間中央値が本文64.5か月／Abstract 70.4か月で不一致。(e) Table 3のサブグループ人数（LA 397 + BA 322 = 719）がTable 1由来の計算（LA 529-132=397、BA 1296-947=349）と一致せずBA群で27例の差、説明なし。(f) LAA処置率が26.3% vs 66.8%と大きく異なり脳卒中比較は極めて交絡的。(g) AAD off/onの規定なし。(h) 追跡完遂率87.6%。(i) 99%がクライオで**クライオベースのCox-maze IIIとしてのデータ**（RFクランプ中心の欧米コホートへの直接外挿は要注意）。
- **推奨クラス**: 該当なし（本論文自身はClass/LOE表記を用いていない）。STS 2017（Badhwar）、2020 ESC/EACTS（Hindricks 2021）、2023 ACC/AHA/ACCP/HRS（Joglar 2024）はいずれも**二次引用**で、クラス表記の引用はない。
- **外科への含意**:
  - MV手術同時SAのlesion set選択に対する現時点で最大級の長期多施設データ。全体の読みは「BAが中期の洞調律維持で優位、ただし早期PPMは約5倍（2.2% vs 0.4%）」。
  - **しかし最も外科的に重要なのはサブグループ**。右房病変（TV手術を要する程度の）がなければ、右房lesionを足す利益は消え（むしろLA単独が優位）、PPMの不利益も消える。→ **TV手術を要する右房拡大・容量負荷・長期持続性AF例にはBA、右房病変のないMR単独例にはLA lesion set（box＋LAA連結線＋mitral isthmus＋冠状静脈洞）**という運用が妥当。
  - PPMの原因を著者は「右房lesionそのものではなく既存の洞不全（SND、AF患者の40-60%に併存）がSAで顕在化したもの」と論じている。術前長期持続性AF＋TV手術例ではPPMを織り込んだICと、術中一時ペーシングワイヤの確実な留置を。なお本コホートの早期PPM 1.7%はCTSN（DeRose 2019）の1年 16.1-20.5% より格段に低く、若年（中央値約58-59歳 vs 69.1歳）・AV手術除外・心不全少というコホート差による。
  - **「脳卒中18例中13例（72.2%）はAF-freeを維持していた」** — 洞調律回復＝脳卒中回避ではない。LAA処置と抗凝固継続判断は独立に重要。

---

### [PMID 34164872] Guo Q, Yan F, et al. 2021 J Cardiovasc Electrophysiol 32(8):2316-2328 — 試験名なし（RCTのみのBayesian network meta-analysis）

- **デザイン**: RCTのみを対象とした Bayesian NMA（観察研究は意図的に除外）。PRISMA-P準拠。PubMed/Embase/CENTRAL、最終検索 2021年1月17日、言語・年代制限なし。8061件→732件精査→**19 RCT**（4-arm 1、3-arm 4、2-arm 14）。RevMan 5.3でランダム効果ペアワイズ → MCMC（無情報事前分布）でBayesian NMA、収束はBrooks-Gelman-Rubin法。fixed/random 両モデル提示（主結論はrandom）。稀事象は NetMetaXL の adjusted continuity correction。順位付けはSUCRA、非一貫性はloop単位のIF、出版バイアスはcomparison-adjusted funnel plot、質はGRADE + Salanti法。NetMetaXL 1.6.1 / Stata MP 16.0 / R 4.0.3 / WinBUGS 1.4.3。
  - **介入の再定義（外科医が最も注意すべき点）**: (i) **PVI** = 左右PV個別circular 2本まで、**または box lesion**（エネルギー種・LAA処理の有無を問わない）、(ii) **LAM** = PVI＋「LAA-PVI連結線」または「PVI-僧帽弁輪線」の少なくとも一方、(iii) **BAM** = 右房自由壁の単純切開のみを除く右房lesionを1本以上追加、(iv) no ablation。
- **対象**: **N=2031（19 RCT）**。PVI 248例／LAM 599例／BAM 458例／no ablation 726例。AF病型: 発作性 203例 (10.0%)、持続性または長期持続性 1828例 (90.0%)。**プライマリ（AF freedom）のNMAには19試験・1823例が寄与**（2031との差208例の内訳は記載なし）。母集団は大半がリウマチ性または変性性弁膜症。単独CABGは Cherniavsky 2014・Pokushalov 2012 の2試験のみ。同時手術は MVR/MVP/OMV/AVR/AVP/TVP/TVR/ASD閉鎖/CABG の組合せ。
  - 個別試験N: Srivastava 160、Albrecht 60、Abreu Filho 70、Cherniavsky 95、Wang X 210、Gillinov 260、Khargi 30、Schuetz 43、Doukas 97、Blomström-Lundqvist (SWEDMAF) 65、von Oppell 49、Wang J 299、Jönsson (MAMA) 64、Bogachev-Prokophiev 52、Chevalier (SAFIR) 43、van Breugel 132、Knaut (EPIMIK) 45、Pokushalov 35、Budera (PRAGUE-12) 222。
  - **左房径（LA diameter）は online Table S1 のみで、本文中に実数値なし**。年齢・LA径・EFの具体値も本文に出てこない（「元試験で有意差なしと報告」との記述のみ）。
- **追跡**: 組入れ基準「平均追跡12か月未満は除外」、本文「Follow-up was performed at least 1 year after the procedure」。**統合された median (IQR) の記載なし**。試験別では12か月が大半、Cherniavsky 14か月、van Breugel 18か月、Bogachev-Prokophiev 18.6±2.1か月、Budera 28±5か月、Gillinov 44か月 → **範囲 12〜44か月**。
- **エンドポイント定義**:
  - 主要 = 「Freedom of AF over 12 months」。ただし**各試験の定義をそのまま採用しており統一されていない**。Table 1 の実際の記載: (a) 大多数が「NSR at follow-up」（時間閾値なし・単発ECG判定）、(b)「Freedom from AF/AFL/AT >30 s」2試験、(c)「Freedom from AF lasting >30 s」1試験、(d)「AF burden <0.5%」（Bogachev-Prokophiev、ILR）、(e)「99.5% of SR during overall follow-up」1試験、(f)「NSR and atrial pacing with atrial capture」（ペーシング下心房捕捉も洞調律扱い）1試験。
  - **blanking period = 本文・Tableのいずれにも記載なし**（この論文はblanking periodに一切言及していない）。
  - **AADの扱い = 記載なし**（AAD off/onは全く議論されていない）。
  - 副次 = early postoperative mortality（30日以内または初回入院中の死亡）、follow-up中のPPMI。
- **リズム判定**: ★試験ごとにバラバラ。総括は「12誘導ECG、24時間Holter、または植込み型モニタ」。Table 1の内訳: ECGのみ3か月毎／6か月毎／3・6・12か月／3・6・12か月＋以後年1回、ECG＋24時間Holter（3か月毎／12か月時／6・12か月／3・12か月）、3日Holterを6・12か月（1試験のみ）、**月1回ECG＋ILR（Cherniavsky・van Breugel）、ILR単独（Bogachev-Prokophiev、AF burden<0.5%を成功と定義）**。→ **連続モニタリング（ILR）は3試験のみ、残りは12誘導ECGまたは断片的24時間Holter。7日イベントレコーダの記載なし。** 著者自身が「The real AF recurrence may be underestimated by ECG and 24h-Holter monitoring as most included studies used」と明言。
- **主要結果**:
  - **AF freedom vs no ablation（NMA, random-effects）**: PVI **OR 5.02 (95% Cr.I 2.72-10.02)**、LAM **OR 7.97 (4.93-14.29)**、BAM **OR 8.29 (4.90-14.86)**、いずれもp<.05（19試験・1823例）。
  - **3術式間の比較（random-effects）: PVI・LAM・BAM の3者間で有意差なし**（本文で数値提示なし、Figure 2マトリクス参照）。すなわち BAM は LAM/PVI に優越しない。
  - **BAM vs PVI は fixed-effects でのみ有意 OR 1.79 (95% Cr.I 1.14-2.79)**（random では消失）＝感度解析扱い。
  - 粗のAF freedom率: PVI 67.25%、LAM 69.43%、BAM 75.12%、no ablation 28.08%（**群別分母の内訳は本文に記載なし**。組入れ全体の群別Nは PVI 248/LAM 599/BAM 458/no ablation 726）。
  - SUCRA（random）: BAM 88.97%、LAM 74.91%、PVI 36.12%、no ablation 0%（著者は「順位確率であり有意性を示すものではない」と明記）。
  - **早期死亡: BAM vs no ablation OR 4.08 (95% Cr.I 1.23-17.30), p<.05**（BAMで増加）。逆向き表記 no ablation vs BAM OR 0.24 (0.06-0.81)。fixed では LAM vs BAM OR 0.32 (0.10-0.91) も有意だったが random で消失。副次解析は17試験。
  - PPMI: random では全戦略間で有意差なし（fixedでは早期死亡と同パターン）。**ペアワイズでのみ BAM vs no ablation OR 3.14 (95%CI 1.51-6.52), p<.05**。
  - 粗の早期死亡率／PPMI率: PVI 1.72%／4.03%、LAM 3.48%／5.19%、BAM 2.81%／5.71%、no ablation 2.82%／5.68%（**群別分母の記載なし**）。BAMが両エンドポイントで最下位、no ablationが最良。
  - 従来型ペアワイズ（random）AF freedom vs no ablation: PVI OR 5.36 (95%CI 2.43-11.84)、LAM OR 5.32 (4.42-11.13)、BAM OR 7.38 (5.02-10.87)、いずれもp<.05（LAMの点推定とCIの整合性は原著記載のまま）。
  - ベネフィット・リスク2次元解析: 統計学的有意には至らないが、**LAMが両比較・両モデルで最良の位置**。著者は「LAMを標準術式と結論づけるのは時期尚早」と明記。
  - 異質性・非一貫性: 全closed loopのIFの95%CIがゼロでtruncate、有意な非一貫性なし。**I²の具体数値は本文に一切提示されず**定性的記述のみ。funnel plotに有意な非対称性なし。**GRADE: 全比較で indirectness による1段階ダウングレードを実施し、最終的な確信度は Low または Very low**。
- **限界**:
  - 【著者】全RCTだが小標本・非盲検（blinding of participants and personnel は一律 high risk）、乱数生成/割付隠蔽の記載不明瞭な試験が複数。Schuetz 2003 は no ablation群の早期生存18例中9例しか1年評価を完了せず incomplete outcome data で high risk。大半が事前サンプルサイズ計算なし。手技・AF病型・モニタ法・追跡期間が不均一 → GRADE Low/Very low。ECG＋24時間Holter依存のため真のAF再発は過小評価。メタ回帰・サブグループ解析は元データ不足で実施不能。**TR・右房拡大を有する「右房病変のある選択された患者」で右房アブレーションが有益かは、いずれの組入れ試験もそのデザインになっておらず判定不能**。3カテゴリ化してもなお lesion set はばらつき、**PVI群にbox isolation施行試験と後壁を含まない2本のcircular PVIのみの試験が混在**（後壁隔離の効果がPVIと他術式の差を縮小させた可能性）。右房lesion setはさらに不統一。早期死亡・PPMIは稀事象で検出力が低い。ゼロイベント補正自体が陰性所見の一因かもしれないと明記。
  - 【読み手】(a) **最大の弱点はリズム判定の質**。主要エンドポイントが「NSR at follow-up」（時間閾値なし・単発ECG）の試験が多数を占め、>30秒の現代標準を用いた試験は少数、ILRは3試験のみ。これを統合した「BAM は LAM/PVI に優越しない」は、**非差別的誤分類による null 方向へのバイアス**を受けている可能性が高い。(b) blanking period の記載が皆無。(c) AAD on/off の扱いに一切言及がなく「AADなしでの洞調律維持率」ではない。(d) I²の実数が本文にない。(e) 2031 → 1823 の208例の脱落内訳不明。(f) 「BAM は no ablation より早期死亡が多い OR 4.08 (1.23-17.30)」は Cr.I が極端に広く、RCT内でも術式割付が右房病変で層別化されていない交絡を排除できない。(g) 結論部（Conclusion）の「BAM may increase the risk of early mortality compared with no ablation, but adding right atrial ablation does not increase the risk of early mortality and PPMI」という並置は論理的に自己矛盾的（なお抄録は同じ趣旨を「no difference was found between bi-atrial and left atrial ablation」と表現）（検出力不足を「差がない」と読み替える危険）。(h) 90%が非発作性・大半がリウマチ性弁膜症（中国中心コホートを多く含む）。(i) **Gillinov 2015 (CTSN) は PVI 対 BAM で TTM を用いた高感度モニタで BAM 優位を示した唯一の大規模RCTだが、本NMAでは他の低感度試験に希釈されている**。
- **推奨クラス**: 該当なし（本論文自身のClass/LOE表記なし）。Introduction で STS 2017（Badhwar 2017, Ann Thorac Surg 103:329-341）を**二次引用**するのみ。結論部の "Ablation should be restricted to the left atrium for patients without right atrial pathology" は著者らの意見であり、クラス分類を伴う推奨ではない。
- **外科への含意**:
  - 「非選択の同時手術AF患者」全体では、右房lesionを追加するbiatrial Mazeは LAM/PVI に洞調律維持の有意な上乗せを示さない（random）。ただし fixed では BAM > PVI (OR 1.79, 1.14-2.79) となるため、「右房追加は無意味」ではなく**「不均一な集団と粗いモニタでは差が検出できない」**と読むのが妥当。
  - 著者の実践的結論「右房病変（TR・右房拡大）を持たない患者では左房限局で十分、右房病変を持つ患者での是非は本解析では答えられない」は、Pyo 2025 のサブグループ所見と方向が一致する。
  - 安全性: 粗の早期死亡 BAM 2.81% vs no ablation 2.82%、PPMI 5.71% vs 5.68% と絶対差は小さく、ペアワイズで有意だったPPMI増加（OR 3.14, 1.51-6.52）もNMA randomでは消失。BAMのPPMIは「洞結節近傍・分界稜・CTIのlesion設計と、既存の洞不全の術前評価」で管理すべき問題。
  - **自施設成績との比較の注意**: 本NMAの成功率（BAM 75.12%）は主として単発ECG／24時間Holterに基づく数値であり、Cox-Maze IV の連続モニタベースの成績（一般に低く出る）と直接比較してはならない。
  - **PVI群にbox lesion施行試験が混入していた**という著者の指摘は重要 — 「後壁隔離を含む左房lesion」は PVI と LAM の中間ではなく**実質的に LAM 相当**として扱うべき。

---

### [PMID 40061540] Nitta T, Iwasaki Y, et al. 2025 JTCVS Open 23:110-119 — 試験名なし（日本医科大学 単施設、Maze後AT機序のEPS解析）

- **デザイン**: 単施設後ろ向き観察コホート（1993-2017年、biatrial incision＋両側PVIを伴うmaze手術の全例）＋ 術後AT症例に対するEPS／電気解剖学的マッピングによる機序解析。単変量（ANOVA/χ²、Bonferroni補正: 3×2表 P<.0167、3×3表 P<.0056）＋ stepwise多変量ロジスティック回帰。JMP v12.1。IRB: Nippon Medical School B-2023-733、オプトアウト。
- **対象**: **N記載が本文内で不一致**（Abstract「453 patients」／Methods「451 patients」／Results「Of 441 patients who survived surgery」／Abstract結果部「Of 443 patients who survived surgery (98%)」）。PVI単独例・片房手術例は除外。
  - 背景（Table 1, n=451基準）: 男:女 = 270:181、年齢 65±11歳、NYHA 1=60 (13%)／2=324 (72%)／3=64 (14%)／4=3 (1%)、CTR 57±7%、**LAD 51±10 mm（LAD>60 mmはmaze適応外）**、LVEF 61±13%。
  - AF病型: 発作性 83 (18%)、持続性 11 (2%)、長期持続性 357 (79%)。**ただしTable E1では「Paroxysmal AF (n=349, 79%) vs long-standing persistent AF (n=81, 18%)」と逆転した記載があり原文が矛盾している**（読めた通りに記載）。
  - 基礎心疾患（重複含む）: 弁膜症 348 (77%)、冠動脈疾患 36 (8%)、成人先天性心疾患 26 (6%)、心臓腫瘍 7 (2%)、心筋症 6 (1%)、standalone AF 34 (8%)。
  - **Lesion set: box lesion 90例 (20%、中等度〜高度LA拡大＋長期持続性AF)、U lesion 361例 (80%、roof lineを作らず後壁LAを収縮部位として温存)**。全例 心停止・人工心肺下。
  - PVI手技: bipolar RFクランプ 347 (77%)、cryothermia 81 (18%)、cut-and-sew 13 (3%)、unipolar RF 9 (2%)、bipolar RF+cryo 1。
  - **CS／僧帽弁峡部**: 左房室間溝を剥離しCSを露出（original Cox-maze式）155例 (34%) → うち直接cryo 142 (92%)／クランプRF 10 (6%)／併用3 (2%)。剥離せず後下壁LAをCSごとbipolar RFクランプ 296例 (66%) → うち **264例 (89%) に追加心外膜CS焼灼**（pen型RF 223、cryo 43、併用2）。
- **追跡**: **全体の追跡期間中央値の明示的記載なし**。記載は (1) AF再発までの中央値26か月 (IQR 4-73)、(2) AT発症までの中央値28か月 (IQR 3-75)、(3) 遅発死亡17例 (3.8%) の追跡「1 to 180 months」。外来は6か月間隔。
- **エンドポイント定義**:
  - AF ＝「最終フォロー時の心電図でAFであること」（54例 12.2%）。内訳は術直後から持続 26例 (5.9%)、いったん洞調律後に再発 28例 (6.3%)。
  - AT ＝「12誘導ECGで洞調律と異なる心房波形の rapid and regular atrial activations」。EPS分類は Saoudi分類／Jais基準（macroreentry / focal AT / localized reentry＝直径3cm以内に頻拍周期の>85%）。
  - **blanking period = 記載なし**（術直後からAFだった26例をそのままAFに算入しており実質 blanking 0 と読める）。
  - **閾値（>30秒等）= なし**（Holter/イベントレコーダによる秒単位判定を行っていないため閾値自体が存在しない）。
  - **AADの扱い = 成功定義に明記なし**。記載されているのは「AFを生じた患者に経口アミオダロン3か月投与、洞調律に復さなければβ遮断薬＋抗凝固に切替」というプロトコルのみ。**＝AAD-freeを要求していない**。**STS/HRSの定義（3か月blanking＋30秒閾値＋AAD off）とは比較不能**。
- **リズム判定**: ★きわめて緩い。「Cardiac rhythm was examined by electrocardiogram at every clinic visit and by Holter recording for the patients with arrhythmic symptoms.」＝ **(1) 外来受診ごとの体表心電図（外来6か月間隔、紹介元循環器医/開業医でのフォローも併用）、(2) Holterは"不整脈症状のある患者のみ"（何時間Holterか・頻度の規定なし）**。**7日イベントレコーダ・ILR・ペースメーカ連続モニタは一切不使用。プロトコル化された定期Holterは存在しない。** ATを発症した全例は循環器医の診察を受け、AT 36例中33例 (92%) でEPS＋電気解剖学的マッピング施行（EP-WorkMate、フィルタ30-500 Hz、CARTOまたはEnSite NavX）。著者自身がLimitationで症候性バイアスによる過小評価を認めている。
- **主要結果**:
  - 手術死亡: 院内または30日以内 10例 (2.2%)。**maze手技またはablation deviceに関連した死亡・合併症は0例**。遅発死亡 17例 (3.8%)。**血栓塞栓性脳卒中 0例**。
  - **術後AF（最終フォロー時）54/441 = 12.2%**（術直後から持続 26例 5.9%＋洞調律後の再発 28例 6.3%、再発までの中央値26か月 IQR 4-73）。
  - **術後AT 36/441 = 8.2%**（Abstractは8.1%）、発症までの中央値28か月 (IQR 3-75)。**洞調律 351例 (79.6%)**。
  - **術中PVペーシング**: 施行211例中 **11例 (5.2%) でRF焼灼線を越える伝導ブロック不完全** → 追加RF焼灼でブロック確認（※Methodsでは「PV pacing was performed in 214 patients (62%)」と記載され、Results／Table E2 の211例と不一致）。bipolar RFでPVIを行った患者の術後AF発生率は **ペーシングテスト施行群 9% vs 非施行群 18%、P<.01**。
  - 術後AF再発の独立予測因子（多変量）: **LAD (per mm) OR 1.05 (95%CI 1.01-1.09, P=.009)**、**PV pacing施行 OR 0.32 (95%CI 0.13-0.71, P=.004)**。非有意: 男性 OR 2.05 (0.94-4.72, P=.07)、CTR OR 1.04 (0.98-1.11, P=.15)、AF病型 OR 2.70 (0.73-17.55, P=.15)、**lesion set (box/U) OR 0.50 (0.21-1.15, P=.11)**。
  - 術後AT発症の独立予測因子（多変量）: NYHA (1 vs 2) OR 4.08 (95%CI 1.72-9.48, P=.002)、NYHA (1 vs 3) OR 6.48 (95%CI 1.86-28.21, P=.003)、**追加心外膜CS焼灼 OR 0.21 (95%CI 0.06-0.82, P=.03)**。CS焼灼デバイス（bipolar RF/cryo）OR 1.12 (0.24-3.83, P=.87)。
  - 「不完全焼灼」自体の予測（サブ解析）: NYHA (1 vs 2) OR 17.67 (95%CI 2.95-142.56, P=.002)、追加心外膜CS焼灼 OR 0.02 (95%CI 0.00-0.25, P=.002)。**著者自身が95%CI上限142.56の不安定さを認めている**。
  - **★AT 36例のEPS機序内訳（33例=92%でEPS施行）**: **不完全焼灼に伴うマクロリエントリー 計24例 (67%)** ＝単独機序16例 (45%)＋非PV巣状機序との混合8例 (22%)。**非PV巣状機序 計16例 (44%)** ＝単独22%＋混合22%。Undetermined 3%、EPS未施行 8%。
  - **★不完全焼灼の部位（外科医が最も知るべき数値）**: **冠静脈洞(CS) 16例（24例中67%）＞ 僧帽弁峡部 5例 ＞ PVI 3例 ＞ 三尖弁峡部 2例**。CSとPVIの両方が不完全だった例が2例。
  - **追加心外膜CS焼灼のインパクト**（bipolar RFクランプでCS焼灼した301例中259例 [86%] に追加心外膜焼灼）: **術後AT発症 14% → 3%、P<.001**。エネルギー源による差なし（cryo 5% vs RF 3%, N.S.）。**ただしDiscussion本文は「from 14% to 5%」と記載しており、Results本文（14%→3%, P<.001）・Table E2（追加心外膜焼灼265例中AT 9例=3%）と食い違う**（原文の内部矛盾）。
  - PVIエネルギー源別（Table E2, 単変量）: **bipolar RF (n=341): SR 281 (82%)／AF 42 (12%)／AT 18 (5%)** vs **cryothermia (n=77): SR 51 (66%)／AF 10 (13%)／AT 16 (21%)**。bipolar RF vs cryo: SR vs AT P<.001、AF vs AT P=.006（SR vs AF P=.48）。cut-and-sew (n=13): SR 11 (85%)／AF 1／AT 1。unipolar RF (n=9): SR 7／AF 1／AT 1。**RF適用回数はブロック成否と相関せず**（右PV 2.6±1.1 / 2.3±1.3 / 2.2±1.3、左PV 3.2±0.6 / 3.4±0.5 / 3.1±0.6、SR/AF/AT別）。
  - 非PV巣状興奮の部位（Figure E1）: **1例あたり平均2.3±2.0箇所（範囲1-7）**。部位別患者数: LA中隔2、CS 2、IVC-三尖弁峡部2、洞結節近傍2、SVC 2、RA自由壁2、右心耳2、前方僧帽弁輪1、分界稜1 — **多くは右房側**。術前因子（性別・年齢・AF病型・弁膜症・LAD・EF・CTR）はいずれも非PV巣と相関せず。
  - **カテーテルアブレーションによる救済: 33例中30例 (91%) で conduction gap と非PV巣の双方を焼灼成功**。
  - **Box lesion vs U lesion**: 術後AF再発・AT発症とも有意差なし。Table E2 で U:Box = SR 280:71、AF 42:12、AT 32:4（SR vs AF P=.19、SR vs AT P=.74、AF vs AT P=.18）。多変量でも OR 0.50 (0.21-1.15, P=.11)。
- **限界**:
  - 【著者】(1) EPSは症候性AT例のみ → ATの実際の発生率は本研究より高い可能性（著者は「ATは症候性で長期は耐えられない」と反論するが弱い論拠）。(2) 洞調律でもATを発症せず隠れている不完全焼灼・非PV巣が存在 → 真の頻度はより高い。(3) 後ろ向きであり、PVペーシングと追加心外膜CS焼灼の有効性確定には前向きRCTが必要。(4) OR 17.67 の CI 上限 142.56 の広さを著者自身が「wide variation」と認め理由不明としている。
  - 【読み手】(a) リズム判定が「外来受診時の心電図＋症状のある人だけのHolter」で連続モニタは皆無。**AF 12.2%・AT 8.2%は明らかな過小評価**で、ILR/PPMベースやSTS定義準拠の他研究と並べてはならない。(b) blanking period規定なし・30秒閾値なし・AAD off要求なしで、術直後から持続するAF 26例を再発に含める一方AAD内服下の洞調律も成功扱い＝定義が混在。(c) **1993-2017年の24年コホートで、デバイス（非使い捨てCCS-200→cryoICE、bipolar RF世代）も術者経験も大きく変化しているが era effect の調整が皆無**。PVペーシング施行群・追加心外膜CS焼灼施行群が後年に偏っていれば、観察された効果は時代交絡そのものの可能性。多変量にも手術年が入っていない。(d) 「追加心外膜CS焼灼なし」の42例は心膜癒着等が理由＝再手術/複雑症例に偏る**適応交絡**があり、OR 0.21をそのまま因果として読めない。(e) 患者数が451/453/441/443と一致せず、AF病型内訳もTable 1とTable E1で逆転。(f) stepwise選択で、イベント数（AF 54、AT 36）に対し変数が多く不完全焼灼サブ解析は overfitting が濃厚。(g) 「NYHA class 1がATの予測因子」は機序が説明されておらず、軽症＝standalone AF＝若年（AT群 60.2±9.3歳 vs SR 64.9±10.8歳, P=.01）という交絡の反映と考えるのが自然。(h) 単施設・日本人・LAD>60mm除外の選択集団。(i) **Kaplan-Meierではなく「最終フォロー時点の断面」でAFを判定**しており、追跡期間の不揃い（1-180か月）が補正されていない。
- **推奨クラス**: 該当なし。本論文はClass/LOE表記を一切用いず、他ガイドラインのClass表記も引用していない。著者の規範的表現（"additional PVI is recommended until all the PVs are proved to be electrically isolated…"、"A touch-up catheter ablation for patients who develop AT postoperatively is strongly recommended"）は**著者自身の意見表明**であり一次資料としての推奨クラスではない。
- **外科への含意**:
  1. **CSが最大のアキレス腱**。CS筋層（myocardial sleeve）はCS入口部から3-5cmの深さまでRA心内膜筋が延び、RAと後壁LAをつなぐ伝導路になる。心内膜側からクランプRFやcryoprobeを当てても心外膜側のCS壁が残存し僧帽弁輪周囲リエントリーの回路になる。**対策 = 心内膜焼灼に加え pen型RF または cryo で心外膜側からCSを追加焼灼し "completely encircling necrosis" を作る**。冠動脈損傷回避のため直視下で。**エネルギー種は問わない（cryo 5% vs RF 3%, N.S.）— 重要なのは全周性であること**。
  2. **僧帽弁峡部ラインは「弁輪に到達させる」だけでは足りない**。不完全部位の第2位が僧帽弁峡部（5例）で、CSと合わせると左側房室弁輪領域が不完全焼灼の圧倒的多数。ここが外科maze最大の技術的難所であることが電気生理学的に裏づけられた。
  3. **術中PVペーシングは「やる価値がある」**。bipolar RFで2回以上・クランプ位置を変え・tissue conductance低下で透壁性を確認してもなお 5.2% で伝導残存。**RF適用回数はブロック成否と相関しなかった＝「回数を増やす」ではなく「クランプの掛け方（後壁antrumの咬み込み不足）」の問題**。多変量で OR 0.32 は lesion set (OR 0.50, P=.11) より強い効果。
  4. Cryoで両側PVIを行った群はATが21% (16/77) と高率（bipolar RF 5% [18/341] に対しP<.001）。cryoでantrumを均一に隔離する難しさを示唆（ただし後ろ向き・時代交絡あり、n=77と小さい）。
  5. **Box vs U lesionは再発率に差がない** → 後壁LAの収縮能を温存したいならU lesionを選んでよく、その判断は再発リスクを理由に否定されない（本研究の枠内では）。
  6. **MICS/胸腔鏡・ロボット手術への含意**: 限られたアクセスでは心外膜側CS焼灼が困難であり、これらのアプローチは構造的にAT発生リスクを抱える。**ハイブリッド戦略（術後の計画的カテーテルタッチアップ）を最初から治療計画に組み込むべき**という主張の根拠。心膜癒着で心外膜CS焼灼を諦めた症例は「ATハイリスク」としてEP医に申し送る。
  7. **非PV巣状興奮は外科的一律lesion setでは制圧できない**（AT症例の44%、平均2.3箇所、多くが右房側: 分界稜・SVC・洞結節近傍・右心耳）。外科手術単独の限界＝ハイブリッドの理論的根拠。
  8. **術後ATは諦めなくてよい: カテーテルアブレーションで 30/33 = 91% が成功**。ATを起こしたら早期にEP医へ紹介。無症候例への予防的EPSは著者も「controversial」。

---

### [PMID 41242589] Goings D, Haq IU（joint co-first）, ... Killu AM. 2025 Heart Rhythm（article in press）— 試験名なし（Mayo Clinic 単施設、Maze後再発例のカテーテルマッピング）

- **デザイン**: 後ろ向き単施設観察研究。2008-2023年に外科的Maze（Cox-Maze III/IV、両心房/左房のみ両方、および"Maze"と記載されたPVIのみ4例を含む）を受け、AF/AFl再発により2013-2024年に当院でカテーテルアブレーションを受けた患者。全例で高密度電気解剖学的マッピング（multipolar mapping catheter）。統計は**記述統計と単変量解析のみ**（"Given the high number of independent variables relative to cohort size, we were unable to perform multivariable modeling"）。χ²/Fisher、paired t/Wilcoxon、Student t/Mann-Whitney、Pearson。**多重比較補正はTable 4のlesion-level解析でのみHolm補正、それ以外は未補正**。Python 3.12.7 + R 4.3.2。Mayo IRB承認。※本文中に「ChatGPT-4oを文章推敲に使用」と明記。
- **対象**: **N=86**（同期間に施設で施行された**約3330例のMazeのうち、再発でカテーテルアブレーションに至った高度選択サブセット**）。除外: 臨床フォロー12か月未満。
  - 年齢（Maze時）62.3±11.9歳、男性 60/86 (70%)。
  - **AF病型（Maze施行時）: 発作性 59例 (69%)、持続性 26例 (30%)、長期持続性 1例 (1%)** ← 解釈上きわめて重要（実臨床のconcomitant Maze集団と乖離）。
  - 併存: 高脂血症 66 (77%)、高血圧 64 (74%)、2型DM 18 (21%)、Maze前のカテーテルアブレーション既往 4 (5%)。AF診断からMazeまで中央値 0.2年 (IQR 0.04-1.8)。
  - Maze術式（Table 1）: cut and sew 9 (10%)、cryoablation 42 (49%)、RF 22 (26%)、hybrid (cryo+RF) 13 (15%)。**本文記載とTable 1が不一致**（本文「All 85 patients… Cryothermal 37 [43.5%]、bipolar RF 30 [35.3%]、combination 18 [21.2%]、うち9例 [10.6%] がPVをcut-and-sewで primary isolation」）。分母も83/85/86が混在。
  - 同時手術: 僧帽弁手術 44 (51%)（repair 27／replacement 17）、CABG 16 (19%)、AVR 10 (12%)、三尖弁形成/修復 12 (14%)、PFO/ASD閉鎖 10 (12%)、**LAA結紮・切除 57 (66%)**（clip 11／suture ligation 18／complete excision 28）。
  - **LAA–僧帽弁輪ラインを持つ20例のうち14例 (70%) は annulus-to-LIPV ラインも併施、6例 (30%) は LAA-to-annulus のみ**（＝ライン連続性が断たれていた）。
  - カテーテルアブレーション前の心エコー: LVEF 59.0±9.9%、**LAVI 57.3±15.8 mL/m²（著明な左房拡大）**、RVSP 38.4±11.5 mmHg。**LA径（mm）の記載なし**。
  - **RA-only lesion setの患者はゼロ**。
- **追跡**: Mazeからカテーテルアブレーションまで 平均 20.0±26.7か月。**Mazeから不整脈再発まで中央値 7.3か月 (IQR 0.3-32.7)**。カテーテルアブレーション後は全例最低12か月（中央値/IQRの記載なし）。著者自身が「follow-up was limited to 12 months after catheter ablation」と明記。
- **エンドポイント定義**:
  - Maze後の再発（本研究の入口定義）＝「first documentation of AF/AFl recurrence on a 12-lead ECG, ambulatory cardiac monitor, or loop recorder after a **3-month postprocedure blanking period**」。
  - **持続時間の閾値（>30秒等）の記載は本文に一切なし**（"first documentation" のみ）。
  - **AADの扱い（off/on、成功例にAAD継続を含めるか）の記載も本文に一切なし**。AAD使用率・離脱率のデータも示されていない。
  - カテーテルアブレーションの手技エンドポイント = PVI（未達なら）＋ AFlの停止/非誘発性。線状lesionは differential pacing とマッピングで双方向ブロック確認。
  - カテーテルアブレーション後の主要アウトカム = 12か月時点の「freedom from any atrial arrhythmia（single procedure）」。**ここでも blanking の再設定・持続時間閾値・AADの扱いの記載なし**。
  - **【重要】本研究は「再発してアブレーションに至った患者だけ」の設計であり、Mazeの成功率を推定する研究ではない**。著者も "This should not be interpreted as the true Maze failure or recurrence rate" と明記。
- **リズム判定**: ★Maze後の再発検出は12誘導ECG、ambulatory cardiac monitor（装着期間の記載なし）、または loop recorder のいずれか。**定期的な監視スケジュール（何か月ごとに何時間のHolter等）は本文に記載なし**。症状ドリブンの臨床的検出に依存し、系統的な連続モニタリングプロトコルは存在しない。著者も "it is possible that some episodes of atypical AFl may not have been recognized before invasive EP testing" と認める。カテーテルアブレーション後の再発37例における検出手段の内訳のみ判明: **ECG 25例 (67.6%)、Holter 5例 (13.7%)、ペースメーカ/ICD interrogation 5例 (13.7%)、ILR 2例 (5.4%)**。Holterの記録時間・装着頻度・連続モニタ植込み率はいずれも記載なし。
  - → 本研究の「57.6% freedom at 12 months」は ILR等の連続モニタ試験と直接比較してはならない（過大評価方向）。**一方、Maze後のlesion完全性の評価は侵襲的マッピング（高密度電気解剖学的マッピング＋entrainment＋differential pacing）という最も厳格な手法で行われており、この点が本研究の最大の強み**。
- **主要結果**:
  - 臨床的再発パターン（3か月blanking後、n=86）: AF+AFl 両方 27例 (31.8%)、AFのみ 29例 (33.7%)、AFlのみ 29例 (33.7%)。**ただしマッピングでは 69例 (81.2%) にAFlが誘発可能**。
  - **PV再伝導（患者ベース）: PVIを受けた83例中 65例 (78.3%)**（Table 2では全86例中65例=75.6%と分母が異なる表記）。個別PV: RSPV 47/83 (56.6%)、RIPV 54/83 (65.1%)、**LSPV 57/83 (68.7%)、LIPV 56/83 (67.5%)** — 左側PVの再伝導率がやや高い。
  - **★エネルギー別 PV再伝導率（per-lesion、cryo 156 PV / RF 172 PV / cut-and-sew 40 PV）**: **cryo 67% vs RF 56%（RF vs cryo OR 0.63, P=.03）、cut-and-sew は 40 PV中 5% のみ（vs cryo OR 0.07, P<.0001／vs RF OR 0.11, P<.0001）**。**95%CIの記載は原文になし**。
  - **★線状lesionの再伝導率（施行数分母）**: LA roof line **3/48 (6.3%)**、posterior LA box **3/47 (6.4%)**、mitral isthmus **5/44 (11.4%)**、LAA–LSPV connecting line **1/31 (3.2%)**、LAA–mitral annulus line **2/21 (9.5%)**、intercaval line **3/15 (20%)**、**CTI line 8/28 (28.6%)** — **CTIとintercavalが最も破綻しやすい**。
  - EP検査での誘発性AFl（n=86）: 何らかのAFl/AT誘発 67例 (77.9%)、AFlなくAF再発のみ 19例 (22.1%)、典型的CTI依存性 33例 (38.4%)、非典型（非CTI依存）51例 (59.3%)、左房粗動 40例 (46.5%)、右房粗動 39例 (45.3%)、非CTI右房粗動 14例 (16.3%)、両心房性 7例 (8.1%)。
  - **★LAA–僧帽弁輪ライン（n=20-21）と粗動**: 全体粗動 **100% vs 71.2% (P=.005)**、左房粗動 **80% vs 36.4% (P=.001)**、非典型粗動 **90% vs 50% (P=.002)**。**このラインを置いた患者は全例が粗動を再発**。
  - LAA–LSPV connecting line: 左房粗動 63.3% vs 37.5% (P=.026)、両心房粗動 16.7% vs 3.6% (P=.047)。
  - **CTIラインを置いた症例で逆に非CTI右房粗動が増えた**: 29.6% vs 10.2% (P=.031)。
  - **同時僧帽弁形成術（replacementではなくrepair, n=27）と粗動**: 全体粗動 92.6% vs 71.2% (P=.028)、CTI依存性 55.6% vs 30.5% (P=.033)、非典型 81.5% vs 49.2% (P=.005)。**両群でLAサイズ・LVEDDに有意差なし** → 心房切開瘢痕が機序と著者は推定。
  - その他: PFO閉鎖 → 右房粗動 100% vs 41.3% (P=.007)。AVR → CTI依存性粗動 70% vs 34.2% (P=.040)。LAA切除のみのサブグループ (n=28) は有意な関連なし。
  - **カテーテルアブレーション後12か月の不整脈フリー（single procedure）: 49/86 = 57.6%**。
  - lesion-levelエネルギー種別（Table 4, Holm補正）: LA粗動に関与したラインの割合 **cryo 120/201 (59.7%) vs RF 31/73 (42.5%)**（Fisher 2-sided P=.013、Holm補正後 P=.040）、cut-and-sew 11/27 (40.7%)（cryo vs c&s P=.132、RF vs c&s P=1）。CTI粗動: cryo 10/21 (47.6%) vs RF 1/9 (11.1%), P=.10、c&sのRAラインは0本。両心房粗動: cryo 25/225 (11.1%)、RF 10/83 (12.0%)、c&s 5/27 (18.5%)（有意差なし）。**cut-and-sew は特定の粗動回路の増加とは関連しなかった**。
  - カテーテルアブレーション時の来院時調律 (n=85): 洞調律 30 (35.3%)、AF 16 (18.8%)、典型的AFl 17 (20.0%)、非典型AFl 4 (4.7%)、洞徐脈 8 (9.4%)、心房頻拍/接合部調律/心房ペーシング 各1 (1.2%)。**7例は洞調律かつ全PV isolated の状態でアブレーションに至った**。
- **限界**:
  - 【著者】後ろ向き単施設・約3330例中86例という高度選択集団で「真のMaze失敗率・再発率と解釈してはならない」。**再発しなかったMaze患者のコントロール群なし** → PV再伝導率・粗動率は真の頻度を過大評価している可能性。N=86で多変量解析不能・交絡調整なし。術式/lesion setが不均一（cryo vs RF、両心房 vs 左房のみ、mitral isthmus/RA isthmus省略例、PVIのみ4例を"Maze"に含む）。LAA–僧帽弁輪ラインの関連は「より難しい症例／特定の術者で使われた」ことの反映かもしれない。アブレーション後フォロー12か月のみ。多重比較補正はTable 4のみで exploratory/hypothesis-generating と解釈すべき。cryo凍結時間・RF通電回数が一貫して記録されておらず定量解析不能。心房切開部位の詳細データが全例では得られていない。ganglionated plexi ablationは1例のみ。
  - 【読み手】リズム判定が症状ドリブンの12誘導ECG中心で系統的連続モニタなし。**成功の持続時間閾値（>30秒等）およびAAD継続例の扱いが一切定義されておらず、他試験との数値比較は不可能**。本文とTable 1で術式内訳が食い違い分母も83/85/86が混在。Maze時のAF病型が発作性69%と実臨床のconcomitant Maze集団と乖離。cut-and-sewのPV数がわずか40本で5%のCIは広いはず（原文にCI記載なし）、かつcut-and-sew群はMaze IIIとして施行時期が古く術者・時代効果の交絡が避けられない。**「LAA–僧帽弁輪ライン＝100%粗動」はn=20の小群かつ選択バイアス集団での所見であり因果証明ではない。ライン自体の再伝導率はむしろ低い（2/21=9.5%）ため、「ラインが破綻したから粗動」というより「そのラインを置く症例背景」の可能性も残る**。
- **推奨クラス**: 該当なし（本論文自身はClass/LOE提示なし）。ただし Clinical implications に**二次引用**として "A standardized lesion set aligns with the Heart Rhythm Society guidelines recommending that if a line is created, bidirectional block across it should be demonstrated."（文献5 = Calkins H, et al. 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement, J Arrhythm 2017;33:369-409）。**原文の推奨クラスを本論文が明示していないため二次引用として扱う**。文献12（Robertson JO, et al. Ann Cardiothorac Surg 2014）も同様。
- **外科への含意**:
  1. **エネルギー源よりlesionの透壁性・完全性が本質だが、実装レベルではcut-and-sewが圧倒的にdurable**（PV再伝導 5% vs cryo 67% vs RF 56%）。著者も「最適な手技で行えばcryo/RFも同等になりうる」と留保しており、教訓は「エネルギー源の選択」ではなく**「組織接触・通電量・透壁性の担保を標準化・記録すること」**。
  2. **左側PVの再伝導が右側より多い（LSPV 68.7%／LIPV 67.5% vs RSPV 56.6%／RIPV 65.1%）**。著者の説明は「LAは interatrial groove から入るため右側PVの方が lesion 到達が良く、左側はアクセスが難しい／左房後壁が厚い」。左側PVへのclamp当て方・視野展開に特に注意。
  3. **LAA–僧帽弁輪ライン（lateral mitral isthmus 相当）は最も proarrhythmic**。20例中100%が粗動を再発し、かつ30%（6/20）は annulus-to-LIPV ラインを併施せずライン連続性が断たれていた。→ **「LAAに繋ぐラインは、置くなら完全透壁・解剖学的連続性・電気的アンカリングを必ず担保する。担保できないなら置かない方がよい」**。中途半端な線は macroreentry の走路（channel）を作る。
  4. **mitral isthmus line の物理は「アンカー」で決まる**。RAのCTIラインは三尖弁輪とIVCという2つの固定した非伝導構造に挟まれるが、LAのラインは自ら非伝導境界を作らねばならない。**PVIが不完全なら後方境界が伝導したままとなり、ライン自体が透壁でも mitral isthmus block は物理的に成立しない**（"Incomplete PVI creates a conducting posterior boundary, making durable mitral isthmus block physiologically impossible"）。→ mitral isthmus lesion を入れる前提としてPVIの確実性が不可欠。
  5. **CTIラインは最も破綻しやすい線状lesion（8/28 = 28.6%）、次いでintercaval line（3/15 = 20%）**。一方 roof 6.3%・posterior box 6.4%・mitral isthmus 11.4% と左房ラインは比較的durable。**右房lesionの手技的完成度に改善余地がある**。加えてCTIラインを置いた症例で逆に非CTI右房粗動が増えた（29.6% vs 10.2%, P=.031）ことは、右房への追加lesionも proarrhythmic になりうる警告。
  6. **同時僧帽弁形成術で粗動が増える（92.6% vs 71.2%）がLAサイズには差がない** → リモデリングではなく **Paterson's groove（後方心房間溝）・卵円窩近傍の中隔切開・Waterston's groove といった心房切開瘢痕そのもの** が incisional flutter 基質になっている可能性。**左房アプローチの切開線をMazeのlesion setと統合的に設計する（切開線をlesionでアンカーする）発想が必要**。
  7. **術中の伝導ブロック検証**: "Meticulous lesion formation and intraoperative verification may reduce recurrence"。手術室を出る前に pacing でラインを越える伝導を確認しギャップがあればその場で追加通電するプロトコル、あるいは **hybrid ablation（外科lesion＋EPによるギャップ埋めとブロック確認）** を将来方向として明示的に推奨。
  8. **Maze失敗例の再アブレーションは必ず高密度マッピング下で**。8%は両心房性回路で3Dマッピングなしには解明不能。「PVを経験的に再隔離するだけ、あるいは通常のCTIアブレーションだけでは大半の症例で不十分」。それでも single procedure の12か月不整脈フリーは57.6%にとどまる → **Maze失敗例は難治であり、最初の手術で完成させることが最大の治療戦略**。
  9. 両心房Mazeの標準化を推奨する一方、**両心房Mazeは洞結節機能不全とPPM植込みのリスクを増やす**ため個別判断が必要、とバランスをとった記載あり（Pyo 2025 と整合）。

---

### [PMID 39215996] William J, Chieng D, ... Kistler PM. 2025 Eur Heart J 46(2):132-143 — **CAPLA** 長期追跡（ACTRN12616001436460、原著12か月成績は JAMA 2023;329:127-35）

- **デザイン**: 多施設・国際（オーストラリア/英国/カナダ、11施設）investigator-initiated RCTの**3年以上の延長追跡を対象とした post hoc long-term follow-up 解析**。ITT。PVI+PWI vs PVI単独 1:1。**単盲検**（術者は非盲検、エンドポイント判定者は割付盲検）。Kaplan-Meier＋log-rank、HR/95%CIは単変量Cox。モニタリング法3群間の pairwise 比較のみBonferroni補正（調整α=.017）。SPSS v27。**本解析の検出力計算は独立には行われておらず、原CAPLAのpower calculationに依拠**。
- **対象**: 無作為化338例のうち長期追跡データが得られた **333例 (98.5%)**（PVI+PWI 169 vs PVI単独 164）。全例が症状のある持続性AF（7日以上3年未満の連続エピソードを1回以上）、1剤以上のAADに抵抗性、初回RFアブレーション。**除外: 発作性AF、very long-standing persistent AF（連続AF ≥3年）、HCM**。
  - long-standing persistent AF（本試験定義内）: 29例 (17.1%) vs 27例 (16.4%), P=.86。平均年齢 64.3±9.4歳、男性 77.2%（128 [75.7%] vs 129 [78.7%], P=.53）。
  - BMI 30.1 (5.3) vs 29.9 (5.3)、肥満(BMI>27) 65.7% vs 65.9%。CHA2DS2-VASc 中央値 2 (1-3) 両群。うっ血性心不全 41.7% vs 43.3%。
  - 心エコー: LVEF 52.6 (12.1)% vs 51.9 (12.1)%、**左房径 4.6 (0.6) vs 4.4 (0.6) cm (P=.16)、左房容積係数 49.5 (15.5) vs 45.4 (15.5) mL/m² (P=.05)**。
  - index前の最長AFエピソード期間 **中央値5か月 (IQR 2-8か月)**（Table 1では 6.6 (7.2) vs 7.1 (7.2) か月, P=.59 と表記が不一致）。**index時にAF/AT調律だったのは 63.7% vs 58.9%（＝約40%は洞調律下でのアブレーション）**。
  - **同時心臓手術は本試験の対象外**（カテーテル試験）。ただし追跡中、各群2例ずつ計4例が冠動脈疾患(1)/弁膜症(3)の心臓手術に伴い外科的（心外膜）アプローチでredo ablationを受けた。
- **追跡**: **index ablation 後 中央値 3.6年（IQR 3.2-4.3年）**（Abstract「median of 3.62 years」）。プロトコル上は最低3年の定期的臨床フォロー。3年前に死亡した患者は解析に含め最終臨床受診時点で打ち切り。晩期死亡6例（各群3例、平均1.5±1.1年後）。
- **エンドポイント定義**:
  - 主要（本長期解析）= 「freedom from documented atrial arrhythmia (AF, atrial tachycardia, or atrial flutter **exceeding 30 s**) **with or without the use of AAD therapy** at 3 years after **single** ablation procedure」。
  - **blanking period = index後 90日**。
  - **AADの扱い: on or off AAD（AAD継続例も成功に含める）**。プロトコルでは90日ブランキング終了までにAAD中止を指示したが、**3年時点で PVI+PWI 32.5%／PVI 27.4% がAADを継続しており、これらも成功に算入されうる**。
  - 副次: 3年時の%AF burden、redo ablationの必要性、最終臨床受診時の調律、AFEQT、医療資源利用、AAD使用、心血管死、全死亡。multi-procedure success = 1回または2回のアブレーション後の非再発（on or off AAD）。
- **リズム判定**: ★**3つのモダリティの混在（heterogeneous）**。(i) **Kardia mobile による1日2回＋症状時の経電話心電図（TTM, 単誘導ECG）**、(ii) **CIED（ILR/ペースメーカ/ICD）による連続モニタリング**、(iii) **3年時点の28日間連続携帯型ECGモニタリング**。
  - AF burden算出可能な十分なリズムデータがあったのは **274/333例 (82.3%)**。内訳は **TTM 61.3%（解析ECG総数 37,687枚、平均238.5枚/患者）、28日連続ECG 24.5%、CIED 13.9%**。
  - ベースラインでのモニタリング戦略の群間分布: TTM 89 (59.3%) vs 79 (63.7%), P=.67；**28日連続ECG 44 (29.3%) vs 24 (19.2%), P=.04（群間で有意に偏り）**；CIED 16 (10.7%) vs 22 (17.8%), P=.25。
  - **監視法によりAF burden中央値が有意に異なった（CIED 0.2% vs Kardia 0% vs 28日 0%, P=.008）** ← リズム判定手段が数値を規定する直接証拠。
  - **定期12誘導ECGのスケジュールは本文に明示的な記載なし**。著者自身が「the detection of recurrent arrhythmia and calculation of AF burden is ideally performed by implantable rhythm monitoring rather than the heterogeneous rhythm surveillance strategies used」と述べる。
- **主要結果**:
  - **主要: PVI+PWI 59/169 (35.5%) vs PVI単独 68/164 (42.1%)、HR 1.15 (95%CI 0.88-1.51), log-rank P=.55**（HR>1 は PVI+PWI で再発リスクがやや高い方向）。
  - 再発までの期間: 全体中央値 0.53年 (IQR 0.34-1.01)。群別 PVI+PWI 6.9か月 (IQR 4.3-12.3) vs PVI単独 5.9か月 (IQR 3.8-11.4), P=.29。
  - **3年時のAF burden 中央値は両群とも 0%**（IQR 0%-0.85% vs 0%-1.43%, P=.49）。再発が記録された206例（コホートの61.2%）に限っても中央値0%（IQR 0%-4.1% vs 0%-5.2%, P=.75）。
  - **最終臨床受診時の洞調律 144/169 (85.1%) vs 143/164 (87.1%), P=.60**。
  - redo: 全体104例 (30.9%)〔本文〕: 54 (32.0%) vs 49 (29.9%), P=.68, **HR 0.94 (95%CI 0.63-1.42)**。2回以上のredoは各群5例 (3.0%), P=.96。redoまで中央値1.4年 (IQR 0.8-2.8)。**本文「104」と群別合計103（54+49）およびAbstract「103」に不一致**。
  - **★RFによるPWIの耐久性: index で PVI+PWI を受け redo 心内膜アブレーションに至った患者のうち後壁再伝導 39/52 = 75.0%**。PV再伝導は全体で 54.5%、再伝導本数 平均 2.2±0.9本/例（2.3±0.8 vs 2.1±0.9, P=.60；PV再伝導率 29/52 [55.8%] vs 25/47 [53.2%], P=.80）。**PVI単独群で意図せず後壁が隔離されていた例は0**。
  - 急性期: PVIは両群全例で達成（169/169、164/164）。**PWIの急性期達成 146/169 (86.4%)**。線状焼灼のみでは隔離できず **box内追加焼灼を要したのは Table 2 で 89 (26.7%)、Discussion では「53% of patients randomized to PWI」（89/169 = 52.7%）と記載**（Tableの%は分母333と思われ内部不整合）。
  - **左房マクロリエントリー頻拍（LAMT）: redo時 PVI+PWI 11/52 (21.2%) vs PVI単独 6/47 (12.8%), P=.27**（有意差なしだが約2倍）。うち **peri-mitral flutter 9/52 (17.3%) vs 5/47 (10.6%), P=.34**。roof-dependent 1/52 (1.9%) vs 3/47 (6.4%), P=.26。anterior LA flutter 3/52 (5.8%) vs 0/47 (0%)。**CTI依存flutter 6/52 (11.5%) vs 5/47 (10.6%), P=.89**。
  - Multi-procedure success: **HR 1.04 (95%CI 0.76-1.42), P=.82**。redo時の戦略別の再発フリー生存も有意差なし (P=.15)。
  - 医療資源利用: healthcare utilization event 103 (60.9%) vs 93 (56.7%), P=.50。予定外入院 総イベント 115 vs 83、患者あたり 0.7±1.5 vs 0.5±1.5, P=.20。DCCV 0.6±1.3 vs 0.6±1.3, P=.97。入院理由の最多は症状のある心房性不整脈 64.6%、次いで心不全 15.2%。3年時AAD 55 (32.5%) vs 45 (27.4%), P=.31。抗凝固薬 103 (60.9%) vs 93 (56.7%), P=.43。
  - QOL: 3年時AFEQT 88.0±14.8 vs 88.9±14.8（Abstractは 88.9±15.4 で不一致）, P=.63。ΔAFEQT 35.6±21.1 vs 33.8±21.1, P=.85。
  - 手技: 総手技時間 147.4 (47.5) vs 124.7 (47.5) 分, P<.001；総RF時間 38.1 (16.2) vs 30.1 (16.2) 分, P<.001。合併症 5 (3.0%) vs 4 (2.4%), P=.96。**心房食道瘻/潰瘍 0例、手技死亡0、脳血管イベント0**。タンポナーデ 1 (0.5%) vs 0、横隔神経損傷 0 vs 1 (0.6%)、心不全 2 (1.2%) vs 2 (1.2%)。
- **限界**:
  - 【著者】(1) **RFアブレーションのみを使用しており、これがPWIの耐久性に影響し、他の技術（PFA等）で得られうる adjunctive PWI の潜在的利益を鈍化させた可能性**。(2) 再発検出とAF burden算出は本来は植込み型連続モニタリングで行うのが理想で、heterogeneous なリズム監視戦略はAF burdenを過小評価しうる。(3) 単盲検（エンドポイント判定者は盲検）。
  - 【読み手】(4) **事前規定ではなく post hoc extended follow-up で、長期エンドポイントに対する独立した検出力計算がない**。HR 1.15 の95%CI上限1.51は、PWIによる中等度の害を除外できていない。(5) リズム監視モダリティの群間分布が不均衡（28日連続ECG 29.3% vs 19.2%, P=.04）で、より高感度な監視を受けた群で再発が多く検出されるバイアスがありうる。(6) AF burden算出可能は 274/333 (82.3%) で17.7%欠測。(7) 3年時点で27-33%がAAD継続しており「on or off AAD」の成功定義は純粋なアブレーション効果を過大評価しうる。(8) **数値の内部不整合が複数**（redo総数 本文104 vs 群別合計103 vs Abstract 103、AF burden IQR上限 本文0.85% vs Graphical Abstract 0.87%、AFEQT SD 本文14.8 vs Abstract 15.4、box内焼灼 Table 26.7% vs Discussion 53%、PVI単独群redo時PV再隔離 本文29例 [55.8%] vs Table 25/47 [53.2%]）。(9) **後壁再伝導75%はredoに至った52例のみでの評価で、PVI+PWI群全体（169例）のPWI耐久性は不明**（著者も "the overall durability of PWI across the entire PVI + PWI cohort is unknown" と明記）。(10) 比較的「早期の」持続性AF集団（最長AF中央値5か月、40%は術時洞調律、LSPAF約17%、連続AF ≥3年は除外）で、**より進行した基質を持つ長期持続性AFへの外挿は不可**。(11) 定期12誘導ECGのスケジュールが本文に記載されていない。
- **推奨クラス**: 該当なし。本論文にClass/LOEの記載は一切なし。著者の結論は「Taken together, these results suggest against the empiric adoption of RF-based PWI at index CA for PsAF」という研究者の解釈にとどまる。
- **外科への含意**:
  1. **「box lesion（後壁隔離）を足せば持続性AFの成績が上がる」という前提は、少なくともRF心内膜アプローチでは3年でも成立しない**（HR 1.15, 95%CI 0.88-1.51, P=.55）。Cox-Maze IV の一部としてではなく「PVI＋後壁box」という限定的lesion setを単独で評価した話であることに注意。
  2. **ただし最大のメッセージは「PWIが無効」ではなく「RF心内膜PWIは持たない」可能性**。redo時の後壁再伝導 39/52 = 75.0% は decisive。著者は "the limited efficacy of RF-based PWI in this study may be related to its poor temporal durability" と述べ、機序として (a) roof line が septopulmonary bundle の心外膜層を貫通しきれない、(b) posterior LA の epi-endocardial connection が多数存在し box 内追加焼灼が53%で必要、(c) **食道加温により後壁での透壁病変形成が阻害される** を挙げる。**これらはいずれも「心外膜から、食道を避けて、透壁に焼く」外科アプローチが原理的に優位でありうる領域を名指ししている**（本文: "A surgical approach provides epicardial access to isolate the posterior wall."）。
  3. **しかしその期待は CASA-AF では実証されていない**。本論文が引用するCASA-AF（Haldar EHJ 2020／Boyalla Heart Rhythm 2024）は長期持続性AF 120例を thoracoscopic外科アブレーション vs 心内膜カテーテル に無作為化し、12か月・3年とも不整脈アウトカムに差がなかったと本文中で紹介（**二次引用**）。「外科なら透壁だから勝てる」は現時点で証明されていない。
  4. **催不整脈性の警告 — 外科的box後の peri-mitral flutter に備えよ**。redo時LAMTは 21.2% vs 12.8%（peri-mitral 17.3% vs 10.6%、いずれも有意差なしだが約2倍）。著者は Lim JACC Clin EP 2024（1100例）で有意差ありと引用。**外科でbox lesionを置く際は、mitral isthmus line（およびCTI line）を同時に完遂しない限り、後壁隔離が新たなmacro-reentrant substrateを作りうる**。実際 redo で enduring PVI+PWI だった8例中5例は mitral isthmus 線状焼灼を要した。
  5. **成功の物差しを binary recurrence から AF burden へ**。62%が「再発あり」と判定されながら3年時AF burden中央値は両群0%、AFEQTは88点前後で術前から+34〜36点改善。**最終受診時洞調律 85-87% と「>30秒の再発ゼロ」35-42% は全く別の指標**（外科文献で「洞調律率85%」と書かれている場合、CAPLAでいう洞調律85%に相当し、厳格な非再発率ではない可能性が高い）。
  6. 安全性の参照値: RF後壁焼灼で心房食道瘻/潰瘍 0/169。ただしPWI追加で手技時間+22.7分、RF時間+8.0分（いずれもP<.001）。**外科でも後壁lesionの追加コスト（体外循環/クロス時間）に見合う利益があるかを同じ枠組みで問うべき**。

---

### [PMID 42319794] Miyazaki S, Nitta J, ... Sasano T. 2026 Eur Heart J（Rapid Communications）— **CORNERSTONE AF trial**（UMIN000047638）

- **デザイン**: 研究者主導・多施設・前向き・無作為化・オープンラベル試験。**日本16施設**。1:1割付（PVI単独 vs PVI+左房後壁隔離 LAPWI）、施設・AF病型・アブレーションモダリティで層別化。full analysis set（ITT）。主要評価は層別log-rank検定（AF型・モダリティで層別）、Kaplan-Meier、Cox比例ハザードでHR/95%CI、両側P<.05。**必要サンプルサイズはシミュレーション研究により516例と算出**。※本稿は Rapid Communication（本文3ページ）で Table 類が本テキストに含まれず、**ベースライン数値表（LA径、CHA2DS2-VASc、AF罹患期間等）は本文に記載なし**。
- **対象**: **ランダム化 517例（LAPWI 258 / PVI単独 259）→ 解析 513例**（LAPWI群で2例同意撤回、2例が静脈奇形のため非施行）。組入れ: 20歳以上、**持続性AF（PsAF, <1年）または長期持続性AF（long-PsAF, 1-3年）**、初回アブレーション予定例。
  - AF病型: **513例中 long-PsAF 13.5%（＝PsAF 約86.5%）**。
  - エネルギー源: **クライオバルーン 25.1%（残り74.9%が高周波）**。PsAFにはRFまたはcryo（ランダム化前に決定）、long-PsAFにはRFのみ。
  - **男性が参加者の80%**。「Baseline characteristics were balanced」との記載のみ。
  - 同時手術は該当なし（カテーテル試験）。
- **追跡**: 計画追跡期間 **18か月**。18か月完遂率 LAPWI 90.2%／PVI単独 90.3%。**median (IQR/range) の記載なし**。受診は1・3・6・9・12・18か月。
- **エンドポイント定義**:
  - 主要 = 単回手技後、**90日のblanking period 以降のあらゆる心房性不整脈（>30秒）からの freedom**、**AAD使用の有無を問わない（with or without antiarrhythmic drugs）**。AADは可能な限り3か月以内に中止。
  - **副次解析としてAAD完全非使用下での不整脈非再発も評価（P=.223で有意差なし）**。
  - 安全性 = 手技関連重篤有害事象。副次 = サブグループ解析、再アブレーション、手技指標、LAPWI成功、追加隔離されたLAPW面積、lesion durability。
- **リズム判定**: ★受診時（1・3・6・9・12・18か月）の心電図に加え、**6・12・18か月に予定された7日間モニタリング（scheduled 7-day monitoring）**。判定は独立した医師が解析。臨床的に必要と判断された場合は追加のリズムモニタリング。**ILR等の連続モニタリングは不使用**で、著者自身が "Despite structured follow-up, asymptomatic arrhythmias may have been missed." と記載。**7日モニタリングの具体的機器（Holter／patch／event recorder）の記載は本文になし。12誘導か否かの明記もなし**。
- **主要結果**:
  - **主要: 18か月時点の心房性不整脈非再発率 LAPWI 80.9% vs PVI単独 76.8%、HR 0.76 (95%CI 0.53-1.09)、層別log-rank P=.110。絶対リスク差 4.1%、NNT 24**。
  - 再発の実患者数: PVI単独群 68例／LAPWI群 52例（分母 259 と 254＝513−259。除外4例はすべてLAPWI群）。
  - 非再発例のうちAAD服用中: **「6 and 13 patients on antiarrhythmic drugs, respectively」**。原文の並びは "76.8% vs 80.9%" すなわちPVI単独→LAPWIの順であり、字義通りには PVI単独 6例／LAPWI 13例。ただし原文表記上あいまいさが残る。
  - **AAD完全非使用下での不整脈非再発（副次）: 両群間に有意差なし、P=.223**（率の数値は本文に記載なし）。
  - **高周波(RF)サブグループ: 80.5% (LAPWI) vs 79.4% (PVI単独), P=.309**（差なし）。
  - **クライオバルーンサブグループ: 82.0% (LAPWI) vs 69.1% (PVI単独), P=.163**（数値上13ポイントLAPWI優位だが有意差なし、著者自身が検出力不足と明記。分母は 25.1%×513 ≒ 129例）。
  - 手技成功: PVIは全例で達成 (100%)、LAPWIはLAPWI群の98.4%で達成。
  - 手技時間: **155 (117-190) 分 vs 131 (95-170) 分、P<.0001**。透視時間は同等（数値の記載なし）。
  - **★lesion durability: 再手技70例中、PV再伝導 52.9%（群間・モダリティ間で有意差なし）、LAPW再伝導 66.7%**。
  - 手技関連有害事象: PVI単独 4.2% vs LAPWI 3.1%, P=.51。
  - **症候性胃不全麻痺（gastroparesis）: LAPWI群のみ3例 (1.2%)、術後2 (1-5) 日で発症、術後32 (4-60) 日で消失。PVI単独群では0例**。
  - 併施アブレーション（両群同等）: **CTIアブレーション 58.1%、SVC隔離 15.6%、非PVトリガーアブレーション 3.3%**。**PVI単独群のうち16例が追加LAPWIを受けた（クロスオーバー的要素）**。
- **限界**:
  - 【著者】構造化フォローにもかかわらず無症候性不整脈は見逃された可能性、アブレーション前のAF burdenが未評価、一部フォローアップ脱落（18か月完遂 約90%）、オープンラベルと追加アブレーション許容によるバイアス、サブグループ解析は検出力不足、2種類のエネルギー源が混在、QOL指標未評価、**参加者の80%が男性で一般化可能性に制限**。
  - 【読み手】(a) 主要評価のリズム判定が「受診時ECG＋6/12/18か月の7日モニタリング」で、**76.8%/80.9%という高い成功率はこの検出感度の低さに強く依存**。ILR判定の試験と直接比較してはならない。(b) 成功にAAD継続例を含む（off-AADでもP=.223で差なしと明記されているのは救い）。(c) **PVI単独群の16例が追加LAPWIを受け（ITT上はPVI単独群にカウント）群間差を希釈する方向に働く**。(d) **HR 0.76 (95%CI 0.53-1.09)・P=.110・NNT 24 は「差がない」ではなく「本サンプルサイズでは差を示せなかった」と読むのが正確**（CI上限1.09＝最大47%相対リスク低減の可能性を否定できない）。(e) クライオ群の13ポイント差は検出力不足。(f) **LAPW再伝導66.7%・PV再伝導52.9%と耐久性が乏しく、「LAPWIの真の効果」を検証できたか疑問**（著者も "Adjunctive ablation may not be beneficial if PVs are not durably isolated." と記載）。(g) Rapid Communication形式のためベースライン表・手技パラメータ（RF出力、CF、LA径、AF罹患期間）が本文に一切なく検証不能。(h) 資金源は "Nothing to declare" だが著者らはMedtronic/Boston Scientificの寄附講座所属・講演料受領。
- **推奨クラス**: 該当なし（本論文自身はClass/LOEを提示していない）。参考文献として 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement（Heart Rhythm 2017;14:e275-444）および 2024 EHRA/HRS/APHRS/LAHRS expert consensus statement（Europace 2024;26:euae043）を引用しているが**二次引用**で、本文中に Class I/IIa 等の表記は一切なし。
- **外科への含意**:
  1. **CAPLA に続く2つ目の大規模陰性RCT**として、「PVI＋後壁隔離＝標準」という前提を外科側も再考する材料になる。著者の機序的説明 "antral PVI already encompasses much of the LAPW, limiting the incremental benefit of additional lines" は、外科的には**「十分に広い antral/box的なPV隔離ができていれば、追加のroof/floor lineの増分は小さい」**と読める（Nitta 2025 の box vs U lesion で差がなかった所見と整合）。
  2. 一方で **LAPW再伝導66.7%・PV再伝導52.9%** は、カテーテルの点状焼灼による線状病変の透壁性・耐久性の限界を示す。**本試験は「後壁隔離が無効」ではなく「耐久性の低い後壁隔離は無効」と読むべき**で、外科的Maze/box lesionの正当性を直接否定するものではない。
  3. **安全性: 後壁焼灼による症候性胃不全麻痺が1.2%（3/254）とLAPWI群のみで発生**（発症中央値2日、消失32日）。**外科でも後壁・食道近傍のエネルギー印加時に迷走神経（胃前庭部枝）損傷リスクを意識すべき**というサポートデータ。
  4. クライオ群での数値上の優位（82.0% vs 69.1%）は、**「面としての広範な後壁焼灼（外科のクランプ/cryo lesionに近い）ならば効果が出うる」**という仮説を残す。
  5. **判定手段が7日モニタリング×3回** — 外科文献のILRベース成功率とは直接比較不能。

---

### [PMID 39556379] Sang C, Liu Q, Lai Y, et al. 2025 JAMA 333(5):381-389 — **PROMPT-AF**（NCT04497376）

- **デザイン**: 医師主導・多施設・オープンラベル・1:1 RCT。**中国12の三次医療施設**。登録 2021年8月27日〜2023年7月16日。中央コンピュータ割付、minimization法（80%の確率的要素、施設と性別で層別）。**modified ITT**（同意・無作為化されアブレーションを受けた全例）。初回アブレーションでのクロスオーバー不許可。中間解析なし。Kaplan-Meier＋log-rank、Cox、比例ハザード仮定は scaled Schoenfeld residuals で検証。感度解析として層別log-rank・層別因子調整Cox。SAS 9.4。サンプルサイズ: 再発率を介入群40%・PVI単独55%と想定、各群224例で両側α=.05・検出力90%、10%脱落を見込み各群249例。
  - **介入 = PVI ＋ EIVOM（Marshall静脈エタノール注入）＋ 3ラインの線状焼灼（僧帽弁輪峡部・左房ルーフ・CTI）**（"upgraded 2C3L"）。対照 = PVI単独（追加基質焼灼なし）。
- **対象**: 無作為化 498例、うち **495例 (99.4%) を主解析に組入れ（介入群 246 vs PVI単独 249）**。
  - **全例が持続性AF（3か月以上持続）。発作性AFは除外**。
  - **long-standing persistent AF（12か月超）: 介入群 113/246 (45.9%) vs PVI単独 89/249 (35.7%)** ← 介入群に不利な方向の不均衡。持続性AF診断からの期間 中央値 12か月 (IQR 5-24) vs 12か月 (IQR 4-24)。
  - 平均年齢 61.1歳 (SD 9.7)、男性 361/495 (72.9%)。高血圧 136 (55.3%) vs 130 (52.2%)、糖尿病 32 (13%) vs 27 (10.8%)、虚血性脳卒中/TIA 14 (5.7%) vs 17 (6.8%)、心不全 22 (8.9%) vs 31 (12.4%)。**CHA2DS2-VASc 中央値 1 (IQR 1-2) vs 1 (IQR 0-2)**。
  - **LA径 平均 42.8mm (SD 6.1) vs 42.8mm (SD 4.5)。>45mm: 84 (34.1%) vs 83 (33.3%)**。LVEF 61.3% (SD 7.6) vs 61.1% (SD 8)。
  - 除外: 発作性AF、**左房径>60mm**、LVEF<30%、余命<1年、禁忌。
  - 同時手術は該当なし（カテーテル試験）。
- **追跡**: index ablation後 **12か月に固定**（3か月ブランキング除外）。受診は1・3・6・12か月。**median (IQR) の記載なし**（全例12か月追跡設計）。介入群で術後2例が脱落、死亡は各群2例（計4例）。
- **エンドポイント定義**:
  - 主要 = index ablation後12か月間の、**>30秒**の documented atrial arrhythmia（AF・AT・AFL）からの freedom を、**AAD非使用下で（without antiarrhythmic drugs）**達成すること。
  - **blanking period = 3か月**。AADはブランキング期間終了後に中止。**3か月ブランキング後の class I または class III AAD の継続・再開は、電気的除細動やカテーテルアブレーションと同様に「treatment failure」として扱われる** ← 本セクション8編の中で**最も厳格なAAD定義**。
  - 副次 = AAD使用の有無を問わない①心房性不整脈からのfreedom、②AFからのfreedom、③複数回アブレーション後のfreedom、④AFL/ATからのfreedom、⑤AF burden、⑥QOL（AFEQT、EQ-5D-3L）。加えて急性期・亜急性期の手技合併症。
  - 手技的エンドポイント = 介入群では PVI成功 ＋ 全焼灼ラインの双方向ブロック（differential pacing と洞調律回復後の activation mapping で検証）。
- **リズム判定**: ★**ILRは不使用**（著者自身が第一のlimitationとして明記）。主体は **wearable single-lead ECG patch による continuous monitoring で、12か月の追跡期間全体を通じて「毎週少なくとも24時間」装着**することを要求。加えて Holter、他の認可済みウェアラブル、症状誘発時ECG。ウェアラブルで検出された心房性不整脈は**割付に盲検化された2名の独立医師が adjudicate**。受診は1・3・6・12か月。
  - **実際の遵守度: 12か月間の平均モニタリング時間 全体 13.0時間/週 (SD 8.0)**、介入群 12.7 (SD 8.7) vs PVI単独 13.4 (SD 8.4)、P=.39。
  - 著者は CIRCA-DOSE post hoc解析（Aguilar, Circulation 2022）を引用し「13時間/週の平均モニタリング時間はAF burden評価においてループレコーダとよく一致する」と主張しつつ、「ILRを用いていないため心房性不整脈再発を過小評価し、持続性AF集団としては比較的高い成功率を説明しうる」と限界を認めている。
  - **12誘導ECGの定期実施頻度についての明示的記載は本文中になし**。
- **主要結果**:
  - **主要: 介入群 174/246 (70.7%) vs PVI単独 153/249 (61.5%)。絶対差 9.2% (95%CI 1.0 to 17.6)、HR 0.73 (95%CI 0.54-0.99)、log-rank P=.045**。
  - 副次（AAD有無問わず）: 180/246 (73.2%) vs 161/249 (64.7%)、絶対差 8.5% (95%CI 0.4 to 16.6)、**HR 0.74 (95%CI 0.53-1.01), P=.06（非有意）**。
  - AFからのfreedom: 188/246 (76.4%) vs 174/249 (69.9%)、絶対差 6.5% (95%CI −1.2 to 14.3)、**HR 0.77 (95%CI 0.55-1.09), P=.14**。
  - 複数回アブレーション後: 191/246 (77.6%) vs 181/249 (72.7%)、絶対差 5.1% (95%CI −2.6 to 12.6)、**HR 0.81 (95%CI 0.57-1.16), P=.31**。再アブレーション 介入群11例 vs PVI単独20例。
  - **★AFL/ATからのfreedom（線状焼灼の催不整脈性の指標）: 212/246 (86.2%) vs 206/249 (82.7%)、絶対差 3.5% (95%CI −2.9 to 9.8)、HR 0.79 (95%CI 0.51-1.24), P=.25**。AFL/AT記録例は介入群 34 (13.8%) vs PVI単独 43 (17.3%)。**→ 線状焼灼を追加してもAT/AFLはむしろ増えなかった**。
  - AF burden: 中央値 0.0% (IQR 0.0%-0.0%) vs 0.0% (IQR 0.0%-0.1%), P=.67。
  - QOL: AFEQT 変化 中央値 −26 (IQR −46 to −10) vs −27 (−44 to −11), P=.94。EQ-5D-3L 10 (0 to 20) vs 10 (0 to 25), P=.08。**群間差なし**。
  - **EIVOM: 246例中 209例 (85%) で成功**。失敗理由: 静脈造影でVOMが描出されず 30例 (12.2%)、複雑な解剖でカニュレーション失敗 7例。
  - **★各線状焼灼ラインの完全ブロック達成率（外科lesion setに最も直結）**: **CTI 233/246 (94.3%)、左房ルーフライン 215/246 (87.4%)、僧帽弁輪峡部 215/246 (87.4%)**。**僧帽弁輪峡部ブロック達成のため冠静脈洞内からの追加焼灼が 154例 (62.6%) で必要**。※Discussionではrooflineブロック率を87.7%と記載しResultsの87.4%と不一致（原文の記載揺れ）。
  - 手技時間 平均 188.0分 (SD 54.1) vs 140.8分 (SD 39.7), P<.001。透視時間 15.9分 (SD 26.3) vs 5.1分 (SD 5.9), P<.001。両側PVIは2例（各群1例）を除く全例で達成。
  - 有害事象: 全体で有意差なし (P=.15)。**ただし心膜炎/ドレナージ不要の心嚢液貯留は介入群7件 vs PVI単独0件**。心タンポナーデ: 穿刺要 1 vs 1、外科手術要 1 vs 0。冠動脈イベント 1 vs 1。III度房室ブロック 0 vs 1。重篤有害事象全体でも群間差なし (P=.36)。
  - 死亡 計4例（各群2例）、全例ブランキング後、イベント委員会は全例を手技非関連と判定。
  - 事前規定サブグループ解析8項目（年齢≥65歳、性別、long-standing persistent AF ≥1年、左房径≥45mm、左房容積が50パーセンタイル超、心不全、LVEF<50%、左房low-voltage areaの有無）で**治療効果は一貫**（個別HR/CIは eFigure 7 のみで本文になし）。
- **限界**:
  - 【著者】(1) **ILR不使用** → 心房性不整脈再発を過小評価している可能性があり、持続性AF集団としては比較的高い成功率（70.7%/61.5%）が出た理由になりうる。(2) 3か月超の持続性AFのみで、より短い持続性AFへの一般化に限界。
  - 【読み手】(3) オープンラベルで、再アブレーションや電気的除細動（＝treatment failure としてカウントされる介入）の実施判断にバイアスが入りうる（ただしイベント判定は盲検化された独立医師2名）。(4) **P=.045、HR 95%CI上限 0.99 とギリギリの有意性。副次評価項目はすべて非有意（P=.06/.14/.31/.25）、AF burdenもQOLも差なし**。多重性調整に関する記載も本文に見当たらない。(5) **ベースラインで long-standing persistent AF が 45.9% vs 35.7% と介入群に不利な方向で偏っている**（無作為化はsiteと性別のみで層別）。主解析では未調整。(6) **「介入」は EIVOM＋3ラインのパッケージであり、どの要素が有効だったか分解できない**。EIVOM成功85%、僧帽弁輪峡部・ルーフのブロック率も87.4%と不完全。CTIラインは左房基質と無関係なのに全例に加えている。(7) 全12施設が中国のみ、CARTO＋SMARTTOUCH系＋ablation index という特定プラットフォーム依存で、PFA/クライオへの外挿は不可。(8) **追跡がわずか12か月**。線状焼灼の最大の懸念である「遅発性のギャップ由来マクロリエントリー性AT」は12か月では十分に出そろわない可能性が高い。(9) サブグループ解析の具体数値・手技詳細・感度解析・QOL詳細・重篤有害事象一覧は Supplement 2 にあり本PDFテキストで確認不能。(10) per-protocol解析の結果は本文に記載なし。
- **推奨クラス**: 該当なし（本論文自身はClass/LOEを提示していない）。**二次引用**として 2024 EHRA/HRS/APHRS/LAHRS expert consensus statement（Tzeis S, et al. Heart Rhythm 2024;21(9):e31-e149）に言及し、「最新のエキスパートコンセンサスは EIVOM が持続性AFアブレーションで reasonable かもしれないと示したが、依然として **area of uncertainty** に分類されている」「現行のエキスパートコンセンサスは僧帽弁輪峡部焼灼を支援するためのEIVOM使用を推奨している」と記述。**いずれも Class 表記・LOE の明示はなく二次引用**。
- **外科への含意**:
  1. **「線状焼灼（心房コンパートメント化）は持続性AFに有効」を初めてRCTで示した**。著者自身が "Linear ablation, derived from the Cox-Maze surgical technique" と述べ、"This approach has shown promising results in surgical ablation" として Khiabani らの Cox-Maze IV 長期成績（JTCVS 2022）を引用。**STAR-AF II で線状焼灼が否定された最大の理由は「lesionの非durability」であり、外科的Maze（cut-and-sew／両極性クランプ）が本質的に有する透壁性・恒久性こそが線状焼灼戦略を成立させる**、という読み方ができる。カテーテルはようやく ablation index ＋ contact force ＋ EIVOM でその水準に近づいた。
  2. **僧帽弁輪峡部ラインの難しさが数値で裏づけられた**。カテーテルではEIVOMを併用してなお完全ブロックは 215/246 (87.4%)、しかも **62.6% (154/246) で冠静脈洞内からの追加焼灼が必要**。「心内膜側だけでは不十分・心外膜側の伝導（Marshall靱帯、CS筋束）が残る」という機序は外科lesion setでも同じ。**外科は術野から心外膜側のMarshall靱帯を直視下に切離・焼灼でき、EIVOMに相当する処置を無償で実施できる強み**がある。Maze手術で僧帽弁輪ラインを完成させる際、**Marshall靱帯の処理を明示的に行う根拠**となる。
  3. **ルーフラインも 87.4% 止まり**。理由として septopulmonary bundle と septoatrial bundle の間の脂肪組織が透壁性lesion形成を阻むこと（Pambrun, Heart Rhythm 2021）が挙げられている。外科的box lesionでも左房ルーフの筋束走行と心外膜脂肪は同じ障壁であり、**両極性クランプや心外膜アプローチの優位性を裏づける**。
  4. **「線状焼灼を足すとATが増える」という長年の懸念は、本試験ではデータで否定された**（AFL/AT記録 13.8% vs 17.3%、HR 0.79, 95%CI 0.51-1.24）。**ブロックを完成させれば線状焼灼は催不整脈的にならない。外科でもlesionを incomplete に残すことこそが最大の催不整脈リスク**という Nitta/Goings の教訓と一致する。
  5. **CTIラインが全例に加えられている点も外科の実務に近い**（右房アプローチ時のCTI ablationは容易・低リスク）。CAPLA延長追跡で後壁隔離のみでは再アブレーション時に僧帽弁輪依存17.3%・CTI依存11.5%のflutterが見つかったことと合わせ、**「後壁boxだけでは足りない、anatomical integrated lesion set（＝Maze的思想）が要る」**というメッセージになる。
  6. **誇張して読んではいけない点**: 効果量は絶対差9.2%・P=.045とマージナルで副次は全て非有意、AF burdenもQOLも改善せず、追跡は12か月のみ。lesionを増やせば手技時間+47分・透視+11分、心膜炎/心嚢液貯留 7件 vs 0件。**外科同時Mazeでも「lesionを増やす分の追加時間・追加リスクに見合うか」は個別評価すべき**。またリズム判定が週24時間パッチであるため 70.7% を外科Mazeの成績と直接横並び比較してはならない。

---

### [PMID 40392905] Derval N, Tixier R, ... Pambrun T. 2025 Circ Arrhythm Electrophysiol 18(5):e013427 — **Marshall-Plan trial**（NCT04206982、Bordeaux単施設）

- **デザイン**: 前向き・無作為化・並行群間・**優越性検証RCT（単施設）**。1:1割付（施設統計家が事前に乱数表作成、Methodology and Data Management Centerで保管）。**modified ITT**（科学委員会の助言により2例除外: PVI群1例＝既往心臓手術による誤登録、MP群1例＝無作為化後の甲状腺機能亢進症で手技中止）。登録 2020年1月〜2022年11月。サンプルサイズ: PVI群1年再発50%、MP群25%を想定、α=5%、power 80% → 各群57例、脱落5%を見込み各群60例＝計120例。Kaplan-Meier＋log-rank、心エコー経時変化は random slope and intercept 線形混合モデル。**資金提供 Biosense Webster (IIS-546) および ANR**。CC BY-NC-ND OA。
  - **介入 = Marshall-Plan（VOMエタノール注入 ＋ PV隔離 ＋ 3ラインのブロック［僧帽弁峡部・dome（ルーフ、必要ならフロア追加）・CTI］）** vs **PVI単独**。
- **対象**: 計120例登録（MP 60／PVI 60）→ **解析118例（各群59）**。
  - 年齢 MP 66±8 vs PVI 65±8歳 (P=0.21)、女性 12 (20%) vs 9 (15%) (P=0.47)。**CHA2DS2-VASc 2±1 vs 2±1 (P=0.04)、高血圧 36 (60%) vs 25 (42%) (P=0.04)** ← MP群に不利な方向の残存不均衡。糖尿病 9 (15%) vs 3 (5%) (P=0.07)、脳卒中既往 5 (8.3%) vs 2 (3.3%) (P=0.44)、アミオダロン既往 54 (90%) vs 49 (82%) (P=0.19)、LVEF 51±12 vs 56±10% (P=0.12)、器質的心疾患 6 (10%) vs 6 (10%) (P=0.99)。
  - 全例 symptomatic persistent AF または long-standing persistent AF（発作性AFは対象外）。**long-standing persistent AF >1年 は 11 (18%) vs 11 (18%) (P=1.00)、全体22例 (18%)**。最長AF持続 10±18 vs 7±6か月 (P=0.86)。**本文では「41%が登録時6か月以上持続AF」**。登録時調律: AF 32 (53%) vs 39 (65%)、SR 28 (47%) vs 21 (35%) (P=0.19)。
  - **左房容積 187±53 vs 192±53 mL (P=0.31)（手技時 182±52 vs 192±53 mL, P=0.22）。LA径の記載なし**。
  - **除外: 肥大型心筋症、左房アブレーション既往、心房切開を伴う心臓手術既往** ← 外科症例は構造的に除外されている。
- **追跡**: **全例12か月**（受診3・6・9・12か月）。**median (IQR) の記載なし**（固定12か月デザイン）。**週次TTMのコンプライアンス 85.3%、Holterのコンプライアンス 86.9%**。追跡中1例死亡（重症laminopathy関連、MP群）。
- **エンドポイント定義**:
  - 主要 = 「1-year freedom from any arrhythmia (**AF/AT >30 seconds**) after a **single** ablation procedure after a **3-month blanking period** **with or without any antiarrhythmic medication**」。
  - **AADの扱い: 「with or without」（AAD継続例も成功に含める）**。ただしプロトコル上、ベースラインのAADは術後1か月間のみ継続しその後は全例で系統的に中止する方針。**AAD非使用下の副次エンドポイントも別途報告されている点が本試験の強み**。
  - **AFL（心房粗動）は独立カテゴリとして明記されずAF/ATに包含**。
  - 副次 = (1) AAD非使用下・単回手技後のfreedom、(2) 1回または2回の手技後のfreedom（AAD使用有無別）、(3) 手技時間、(4) 周術期重篤合併症、(5) 心房機能（A波速度）。
  - 不整脈burden = intermittent monitoring に基づき「利用可能なHolterデータ総時間に占めるAAの割合」と「TTM記録のあった週数のうちAAが記録された週の割合」のうち大きい方。<0.1%／0.1-9.9%／≥10% に層別。
- **リズム判定**: ★(1) 各受診時（3・6・9・12か月）の**12誘導心電図**、(2) **経電話モニター(TTM) KardiaMobile (AliveCor) による30秒心電図を12か月間 毎週 送信＋症状時随時**、(3) **Holter**（記録時間・実施タイミング・回数は本文に記載なし＝Supplemental Methods）、(4) 手技当日翌日・3か月・12か月の経胸壁心エコー。**全リズムストリップは Bordeaux大学病院の中央データベース（blinded core laboratory）へ送信され不整脈専門医がレビュー**。
  - **ILR等の植込み型連続モニタリングは不使用**（Limitationに "the follow-up period was limited to 12 months and conducted without implantable devices for surveillance" と明記）。
  - → 本試験の成功率は「週1回30秒TTM＋定期ECG＋間欠Holter」ベースであり連続モニタリング試験とは直接比較できない。**「>30秒」という閾値に対して週1回30秒スナップショットでは検出力が構造的に不足**しており、両群の成功率は過大評価の可能性。
- **主要結果**:
  - **主要（単回手技後・AAD有無問わず・12か月）: Marshall-Plan 51/59 (86.4%) vs PVI 39/59 (66.1%)、絶対差 +12例 (+20.3%)、P=0.012**。**ハザード比・95%CIの記載なし**（本試験はχ²/log-rankのP値のみで効果量の精度が不明）。
  - 副次（単回手技後・**AAD非使用下**）: **MP 50/59 (84.7%) vs PVI 39/59 (66.1%)、+11 (+18.6%)、P=0.022**。
  - 1〜2回手技後: AAD非使用 MP 51/59 (86.4%) vs PVI 39/59 (66.1%)、+12 (+20.3%)、P=0.011。AAD有無問わず MP 52/59 (88.1%) vs PVI 39/59 (66.1%)、+13 (+22.0%)、P=0.005。
  - **lesion set完遂率: 完全なMarshall-Plan lesion set達成 52/59 (88%) vs PVI群 59/59 (100%)、P=0.058**。
  - **VOMエタノール注入成功 57/59 (97%)**（失敗2例: VOM同定不能1、CS解離1）。エタノール量 10±2 mL、所要時間 22.5±15.4分、透視 6.3±6.8分。
  - **★僧帽弁峡部ライン: 試行 56/59 (95%)、ブロック成功 55例（試行あたり98%、全体93%）、RF時間 7.2±6.2分（うち系統的CS内焼灼 4±3分）。CS自由壁への追加通電が3例 (5%) で必要**。
  - **★ルーフライン単独でのブロックは 30例（試行あたり54%、全体51%、本文 4.5±1.4分／Table 2 は "RF roof line 6.3±4.4分" と不一致）のみ。心外膜側の残存ギャップのためフロアライン追加が 26例 (44%＝全体分母／Table 2 は試行分母で46%) で必要**（うちブロック成功24例＝試行あたり92%、全体43%、4.8±2.7分。2例で失敗）。**最終的なdome transection達成 54例（96%／92%、6.3±3.4分）**。
  - **CTIライン: 試行 56 (95%)、完全ブロック 55例（本文では93%）、RF時間 5.9±4.5分**（Table 2では「55 (93%; 98%)」と per attempt / total の表記順が僧帽弁ライン行と逆転しており原文に不整合）。
  - 手技コスト: 総手技時間 157±53 vs 125±31分、総RF時間 36.8±16.0 vs 29.6±8.1分、総透視時間 21±16 vs 11±6分（本文P<0.001、Table 2はP=0.001と表記）。**一方PVIのRF時間はMP群で有意に短い（23±8 vs 29±8分、P<0.01）、特に左PV隔離（9.5±4.3 vs 13.0±3.7分、P=0.001）** ← VOMエタノールが左側PV/リッジの基質を先に修飾したためと解釈できる。
  - 合併症: **重大合併症 MP 1例 (1.7%) vs PVI 1例 (1.7%)、P=1.0**。内訳: PVI群に**食道-心膜瘻＋縦隔炎1例**（早期外科修復・肋間筋弁充填で後遺症なし）、MP群に輸血・塞栓術を要した重症鼠径血腫1例。軽微合併症 12 vs 5例、P=0.11（心膜炎 6 vs 1、P=0.12）。**脳卒中/TIA/塞栓・横隔神経麻痺・タンポナーデはいずれも0例**。
  - **★再発様式（「ライン作成はAT再発を増やす」への反証）**: 主たる再発様式は両群とも持続性AF（MP 6例 vs PVI 14例、P=0.67）。臨床再発例の不整脈burden MP 35±29% vs PVI 29±27%、P=0.32。
  - **★再手技所見（ラインの耐久性 vs PV隔離の耐久性）**: 臨床再発29例中11例が12か月以内に2回目手技。**PVI群（7例）は全例lesion set完全＝4本のPVすべて隔離維持。MP群（4例）は全例PV隔離は維持されていたがラインにギャップ（僧帽弁ライン3例、ルーフライン2例、CTIライン3例）**。※考察本文では「all 8 patients from the PV isolation group」と記載され結果セクションの7例と不一致。
  - **★左房機能（A波速度）**: 両群ともSR例でA波速度が3か月までに有意に改善し12か月まで維持。**PVI群 49±17 → 67±16 cm/s（P<0.001）、MP群 47±21（3か月）→ 61±20 cm/s（P<0.001）、群間有意差なし**。改善は登録時AF例で顕著。
  - 急性期: 全例で全PVの隔離達成（両群59/59）。手技中のAF直接停止は MP 1例 vs PVI 3例, P=0.62。first-pass PVI率は PVI群83%、MP群80% (P=0.81)（原文の分子表記「10/59」「12/59」は%と整合せず原文の誤記と思われる）。
- **限界**:
  - 【著者】(1) **単施設（monocentric）**であり他施設・複数術者による検証が必要。(2) 追跡12か月かつ**植込み型モニタリング不使用**。著者らは24か月追跡・より大規模な多施設RCTを実施中。(3) COVID-19パンデミックにより登録期間が延長。
  - 【読み手】(4) 週1回30秒TTM＋定期12誘導ECG＋間欠Holterで、無症候性再発の検出感度が低く両群の成功率が過大評価されている可能性。**Holterの記録時間・回数が本文に記載されておらず他試験との比較が困難**。(5) 患者・術者の盲検化は不可能だが**リズム判定は盲検中央判定**であり、この点は担保。(6) ベースラインで高血圧（60% vs 42%, P=0.04）とCHA2DS2-VASc（P=0.04）がMP群で有意に高い（MP群に不利な方向）。(7) **各群59例と小さく、絶対差20.3%という大きな効果量を検出する設計。HR・95%CIが一切報告されておらず効果量の精度が不明**。(8) **PVI群の12か月成功率66.1%は既報の持続性AF PVI単独より高く**（著者も言及）、この高いcomparatorの下でも差が出た点は強みだが、同時に単施設high-volume centerの成績で一般化に注意。(9) 副次エンドポイントの多重性調整の記載なし。(10) **表と本文で数値の不一致が複数**（CTIラインの per attempt/total の順序、再手技症例数7例 vs 8例、first-pass PVIの分子、再発様式の76%表記、透視時間 21±6 vs 21±16）。(11) **資金提供元がBiosense Webster（使用機器メーカー）**。
- **推奨クラス**: 該当なし（本論文自身が推奨クラス/LOEを提示している箇所はない）。本文中のガイドライン/コンセンサス言及は**二次引用のみ**: (1) 冒頭「Patient selection and indications for catheter ablation are well defined in the latest guidelines」→ 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement、(2) 考察で食道温度プローブについて「no clear recommendations have emerged from the latest international expert consensus」→ 2024 EHRA/HRS/APHRS/LAHRS expert consensus statement。**いずれもClass/LOEの具体的表記は本文に記載なし**。
- **外科への含意**:
  1. **「PVIだけでは持続性AFに不十分」を高品質RCTで示した**。PVI単独でも66.1%と良好だったが、3つの解剖学的isthmus（僧帽弁峡部・dome/後壁・CTI）を閉じることで86.4%へ（絶対差 +20.3%, P=0.012）。**これはCox-Maze IIIの設計思想（マクロリエントリー回路の解剖学的遮断）をカテーテルで再現した結果**であり、著者ら自身が Cox JL 1991 (JTCVS) を引用して機序を説明している。外科的左房lesion set（PV隔離＋僧帽弁峡部＋box/roof＋CTI）を「PVIのみのconcomitant ablation」より優先すべき強い根拠。
  2. **心外膜構造こそがラインが通らない理由**。Marshall靭帯/VOMのエタノール焼灼と冠静脈洞筋層の系統的焼灼なしでは僧帽弁峡部ブロックは達成困難で、本試験ではVOMエタノール（97%成功）＋系統的CS内焼灼（4±3分）を前提に僧帽弁峡部ブロック93%を達成。**外科は心外膜側から直接Marshall靭帯を切離・焼灼でき、CS外側からもアプローチできるため理論上カテーテルより有利。逆に言えば、外科でMarshall靭帯を放置した僧帽弁峡部ラインは通っていない可能性が高い**（Nitta 2025 の「CSギャップがAT機序の67%」と完全に整合）。
  3. **ルーフライン単独では51%（30/59）しかブロックできなかった**（septopulmonary bundleの心外膜走行が原因）。44%（26/59）でフロアライン追加が必要となり最終的なdome transectionは92%。→ **外科的には roof line のみでなく box lesion（roof＋floor）を作るべき**という直接的示唆。
  4. **CTIラインは全体の93%でブロック達成**、かつ本lesion setの必須構成要素。外科では右房側のCTIを省略しがちだが、本試験のlesion setはこれを含む。**biatrial lesionの正当化材料の一つ**（ただし本試験はカテーテルで、外科のPPMリスクは伴わない）。
  5. **線状焼灼はAT再発を増やさない**。再発様式は両群とも持続性AFが主体（P=0.67）で、「ラインを引くと医原性ATが増える」という懸念は支持されなかった。**ただし条件は「ブロックを電気生理学的に確認できたライン」**。再手技所見でもMP群の再発は全例ラインのギャップ（僧帽3・ルーフ2・CTI3）が原因で、PVは全例隔離維持されていた＝**再発の原因はラインの非透壁性/耐久性**。
  6. **左房機能は悪化しない**。A波速度はMP群でも12か月時 61±20 cm/s へ改善（P<0.001）し群間差なし。**「広範なlesion setは心房収縮を失わせる」という懸念に対する反証**で、外科的Maze施行の説得材料になる。ただし線状lesionを生理的なwavefront collision部位（CTI septal側・dome下部・僧帽弁峡部）に置くという設計思想が前提。
  7. **代償は time**: 手技時間 +32分、透視 +10分。外科では体外循環時間・大動脈遮断時間の延長に相当する議論。
  8. **本試験は外科症例を除外している**（心房切開を伴う心臓手術既往は除外基準）。同時手術・外科的アブレーションへの外挿はあくまで機序・lesion setレベルの類推であり直接のエビデンスではない。使用エネルギーはRF点状焼灼で外科のクランプ型RF/クライオとは lesion 特性が異なる。

---

## 横断比較表

### 表1. lesion set 別の洞調律維持率と**リズム判定手段**（成功率の見かけ上の差の大半はここに由来する）

| 研究 | 領域 | 比較 lesion set | N（分母） | 追跡 | AF病型（非発作性割合） | エンドポイント定義（blanking／閾値／AAD） | **★リズム判定手段** | 成功率／効果量 |
|---|---|---|---|---|---|---|---|---|
| **Pyo 2025**（JTCVS） | 外科・MV同時 | **biatrial (BA) vs 左房のみ (LA)** | 1825（LA 529／BA 1296） | 中央値 64.5か月（本文）／70.4か月（Abstract） | 87.9%（1605/1825） | 3か月／>30秒／**AAD規定なし** | **12誘導ECG（3,6,12,18,24か月→年1回）＋ 洞調律例のみ24hHolter追加**。ILR等なし | AF再発 5年 LA 34.2% vs BA 28.6%、10年 39.2% vs 37.6%。**SHR 1.256 (95%CI 1.121-1.406), P<.0001**（未調整は逆 0.76 [0.62-0.92]） |
| Pyo 2025 サブ | 外科・**TV手術なし** | 同上 | 719（LA 397／BA 322） | 同上 | 同上 | 同上 | 同上 | **SHR 0.76 (95%CI 0.62-0.93), P=.009 — LA優位に逆転** |
| **Guo 2021**（JCE NMA） | 外科・同時手術 | **PVI vs LAM vs BAM vs no ablation** | 2031（PVI 248／LAM 599／BAM 458／none 726）、主解析1823 | 12〜44か月（統合中央値の記載なし） | 90.0%（1828/2031） | **blanking 記載なし／閾値は試験ごとに不統一（多くは「NSR at follow-up」）／AAD規定なし** | **試験ごとに不統一。ILRは3試験のみ、残りは12誘導ECGまたは断片的24hHolter** | vs no ablation: PVI **OR 5.02 (Cr.I 2.72-10.02)**、LAM **7.97 (4.93-14.29)**、BAM **8.29 (4.90-14.86)**。**3術式間は random で有意差なし**（fixed のみ BAM vs PVI **1.79 [1.14-2.79]**）。粗率 67.25%／69.43%／75.12%／28.08%。GRADE **Low〜Very low** |
| **Nitta 2025**（JTCVS Open） | 外科・maze全例 | **box lesion (n=90) vs U lesion (n=361)** | 441-453（表記不一致） | 中央値の記載なし（AF再発まで26か月、AT発症まで28か月） | 79%が長期持続性（Table E1と矛盾） | **blanking なし／閾値なし／AAD off 要求なし** | **外来受診時ECG（6か月間隔）＋ 症状のある患者のみHolter**。連続モニタ皆無 | 最終フォロー時 **洞調律 351/441 (79.6%)、AF 54 (12.2%)、AT 36 (8.2%)**。**box vs U に有意差なし（多変量 OR 0.50, 95%CI 0.21-1.15, P=.11）** |
| **Goings 2025**（Heart Rhythm） | 外科Maze後の**再発例のみ**をマッピング | lesion別の再伝導率 | 86（約3330例のMazeから抽出） | Maze→CA 平均20.0±26.7か月、CA後12か月 | **発作性69%**（30%持続性、1%長期持続性） | 3か月／**閾値記載なし**／**AAD記載なし** | **12誘導ECG中心の症状ドリブン**（定期スケジュール記載なし）。CA後再発37例の検出手段: ECG 25 (67.6%)/Holter 5/PPM-ICD 5/ILR 2 | **PV再伝導 65/83 (78.3%)**。エネルギー別: **cut-and-sew 5% (40 PV)／RF 56% (172 PV)／cryo 67% (156 PV)**（OR 0.07・0.11, P<.0001；RF vs cryo OR 0.63, P=.03）。CA後12か月 freedom **49/86 (57.6%)** |
| **CAPLA 長期**（EHJ 2025） | カテーテル | **PVI+PWI（後壁隔離）vs PVI単独** | 333（169／164） | **中央値 3.6年（IQR 3.2-4.3）** | 100%持続性（LSPAF 約17%） | 90日／**>30秒**／**on or off AAD**（3年時27-33%がAAD継続） | **混在: Kardia TTM 1日2回 61.3%／CIED 13.9%／3年時28日連続ECG 24.5%**。**監視法でAF burdenが有意に異なる（P=.008）** | **35.5% vs 42.1%、HR 1.15 (95%CI 0.88-1.51), P=.55**。最終受診時洞調律 85.1% vs 87.1%。**redo時の後壁再伝導 39/52 (75.0%)** |
| **CORNERSTONE AF**（EHJ 2026） | カテーテル | **PVI+LAPWI vs PVI単独** | 513（254／259） | 18か月（完遂 約90%） | 100%持続性（long-PsAF 13.5%） | 90日／**>30秒**／**with or without AAD**（off-AAD副次も P=.223） | **受診時ECG（1,3,6,9,12,18か月）＋ 6/12/18か月の7日間モニタリング**。ILRなし | **80.9% vs 76.8%、HR 0.76 (95%CI 0.53-1.09), P=.110**（ARD 4.1%、NNT 24）。**再手技70例で LAPW再伝導 66.7%、PV再伝導 52.9%** |
| **PROMPT-AF**（JAMA 2025） | カテーテル | **PVI+EIVOM+3線状（僧帽弁峡部・ルーフ・CTI）vs PVI単独** | 495（246／249） | 12か月 | 100%持続性（LSPAF 45.9% vs 35.7%） | 3か月／**>30秒**／**AAD off 必須（class I/III の継続・再開は failure）** | **単誘導ECGパッチを毎週24時間以上（実測平均 13.0時間/週, SD 8.0）＋ Holter＋症状時ECG**。盲検2名が adjudicate。ILRなし | **70.7% vs 61.5%、絶対差 9.2% (95%CI 1.0-17.6)、HR 0.73 (95%CI 0.54-0.99), P=.045**。**副次はすべて非有意** |
| **Marshall-Plan**（CircAE 2025） | カテーテル | **VOMエタノール+PVI+3ライン vs PVI単独** | 118（59／59） | 12か月 | 100%持続性（LSPAF 18%） | 3か月／**AF/AT >30秒**／**with or without AAD**（AAD非使用の副次も報告） | **週1回30秒 TTM（KardiaMobile）＋ 受診時12誘導ECG（3,6,9,12か月）＋ Holter（時間・回数の記載なし）**。盲検 core lab 判定。ILRなし | **86.4% (51/59) vs 66.1% (39/59)、絶対差 +20.3%、P=0.012**（**HR/95%CI の報告なし**）。AAD非使用下 84.7% vs 66.1%, P=0.022 |

### 表2. 各 lesion の「通っていない率」（再伝導／不完全ブロック）— 外科がどこで負けているか

| lesion | Goings 2025（外科Maze後の**再発例**のマッピング、施行数分母） | Nitta 2025（外科maze後のAT例のEPS、24例中の部位内訳） | カテーテルRCTでの急性期ブロック達成率 |
|---|---|---|---|
| **PVI（全体）** | **65/83 患者 (78.3%)** で再伝導。LSPV 57/83 (68.7%)／LIPV 56/83 (67.5%)／RIPV 54/83 (65.1%)／RSPV 47/83 (56.6%) | 3例（不完全部位の第3位）。**術中PVペーシングで 11/211 (5.2%) に伝導残存を検出** | PROMPT-AF: 両側PVI 493/495。Marshall-Plan: 118/118。CORNERSTONE: 100% |
| **冠静脈洞 (CS)** | （個別集計なし） | **16/24 (67%) — 最頻部位**。追加心外膜CS焼灼で **術後AT 14%→3%, P<.001**（多変量 OR 0.21, 95%CI 0.06-0.82, P=.03） | PROMPT-AF: 僧帽弁峡部ブロックのため **CS内焼灼が 154/246 (62.6%) で必要**。Marshall-Plan: **系統的CS内焼灼 4±3分が前提**、CS自由壁への追加通電 3例 (5%) |
| **僧帽弁峡部（mitral isthmus）** | **5/44 (11.4%)** 再伝導 | **5/24（第2位）** | PROMPT-AF **215/246 (87.4%)**／Marshall-Plan **55例（試行あたり98%、全体93%）** |
| **LA roof line** | **3/48 (6.3%)** | （box 90例 vs U 361例で再発差なし） | PROMPT-AF **215/246 (87.4%)**／Marshall-Plan: **ルーフ単独ブロックは 30例 (全体51%) のみ、フロア追加26例 (44%) で dome transection 54例 (92%)** |
| **posterior LA box（後壁隔離）** | **3/47 (6.4%)**（＝外科boxは durable） | — | **CAPLA: redo時の後壁再伝導 39/52 (75.0%)、急性期PWI達成 146/169 (86.4%)、box内追加焼灼 53%（89/169）／CORNERSTONE: LAPW再伝導 66.7%** |
| **LAA–LSPV connecting line** | **1/31 (3.2%)** | — | — |
| **LAA–mitral annulus line** | **2/21 (9.5%)**（ライン自体は durable だが **粗動100% vs 71.2%, P=.005**） | — | — |
| **intercaval line** | **3/15 (20%)** | — | — |
| **CTI line** | **8/28 (28.6%) — 最も破綻しやすい**。かつCTIラインを置くと非CTI右房粗動が増加（29.6% vs 10.2%, P=.031） | 2/24 | PROMPT-AF **233/246 (94.3%)**／Marshall-Plan **55例 (93%)** |

**この2表から読める最重要の非対称性**: 外科（Goings）では posterior box 6.4%・roof 6.3% と**左房後壁lesionは非常にdurable**なのに対し、カテーテル（CAPLA 75%／CORNERSTONE 66.7%）では後壁が最も破綻する。**つまりカテーテルの2つの陰性RCTが検証したのは「外科でいうbox lesion」とは別物であり、後壁隔離の価値をこの2試験で棄却してはならない。** 逆に外科が弱いのはCS・僧帽弁峡部（Nitta）とCTI・intercaval（Goings）である。

### 表3. lesion set を増やすことの代償（PPM・時間・特異的合併症）

| 研究 | 追加した lesion | 代償の指標 | 数値 |
|---|---|---|---|
| Pyo 2025 | 右房lesion（cavo-cavo＋RA自由壁-三尖弁輪＋CTI） | 早期PPM | BA 29/1296 (2.2%) vs LA 2/529 (0.4%)、**調整OR 0.16 (95%CI 0.07-0.38), P<.001**。**TV手術なしサブでは OR 0.38 (0.12-1.18), P=.095 と消失** |
| Pyo 2025 | 同上 | CPB／ACC時間 | CPB 中央値 152.0 vs 137.0分、ACC 110.0 vs 92.0分（ともにP<.001） |
| Guo 2021 | 右房lesion（BAM） | 早期死亡（NMA） | **BAM vs no ablation OR 4.08 (95% Cr.I 1.23-17.30), p<.05**。粗率 BAM 2.81% vs none 2.82%。**random では PPMI に有意差なし**（ペアワイズのみ OR 3.14 [1.51-6.52]） |
| CAPLA | 後壁隔離（RF） | 手技時間／RF時間 | +22.7分（147.4 vs 124.7, P<.001）／+8.0分（38.1 vs 30.1, P<.001）。**心房食道瘻/潰瘍 0/169、合併症 3.0% vs 2.4%, P=.96** |
| CORNERSTONE | 後壁隔離 | 手技時間／**胃不全麻痺** | 155 (117-190) vs 131 (95-170) 分, P<.0001／**症候性胃不全麻痺 3/254 (1.2%) が LAPWI群のみ**（発症2日、消失32日）。全体の有害事象 3.1% vs 4.2%, P=.51 |
| PROMPT-AF | EIVOM＋3ライン | 手技/透視時間・心膜炎 | +47.2分（188.0 vs 140.8, P<.001）／+10.8分（15.9 vs 5.1, P<.001）。**心膜炎/心嚢液貯留 7件 vs 0件**（全体の有害事象は P=.15） |
| Marshall-Plan | VOMエタノール＋3ライン | 手技/透視時間 | +32分（157±53 vs 125±31）／+10分（21 vs 11）、P<0.001。**重大合併症 1.7% vs 1.7%, P=1.0**。**左房A波速度は悪化せず（61±20 cm/s へ改善, P<0.001、群間差なし）** |

---

## 議論の対立点・未解決事項

1. **【biatrial vs 左房のみ】Pyo（韓国5施設 IPTW）vs Guo（19 RCTのNMA）— 表面上は対立、実質は「集団が違う」**
   - Pyo は全体で BA 優位（SHR 1.256, 95%CI 1.121-1.406）と主張。Guo は random-effects で3術式間に有意差なしと主張。
   - **説明**: ①AF病型 — Pyo は持続性＋長期持続性 87.9%、Guo も 90% と近いが、Guo の PVI群には box lesion 施行試験が混入し PVI と LAM の差を圧縮している（著者自身が指摘）。②リズム判定 — Guo の組入れ試験の多くは「NSR at follow-up」（時間閾値なし・単発ECG）で、非差別的誤分類が null 方向にバイアスをかける。③追跡 — Guo は12〜44か月、Pyo は中央値 64.5-70.4か月で、**Pyo自身のデータでも10年時点では 39.2% vs 37.6% と差が収束**する（BAの優位は主に5年前後の中期に現れる）。④**最大の違いは右房病変の分布** — Pyo の BA群は 75.2% が同時TV手術（SMD 116.1%）。
   - **未解決**: 「右房病変のない患者で右房lesionを足すべきか」に、両論文とも直接答えていない。Guo は「いずれの組入れ試験もそのデザインになっていない」と明記し、Pyo のサブグループ解析（TV手術なし）は事後解析かつ人数が Table 1 と27例合わない。**RCTが存在しない領域である。**
2. **【後壁隔離／box lesion】カテーテルの2大陰性RCT（CAPLA・CORNERSTONE AF）vs 外科的boxの durability データ（Goings）**
   - Kistler ら（CAPLA）は "these results suggest against the empiric adoption of RF-based PWI at index CA for PsAF" と結論。Miyazaki ら（CORNERSTONE）も「全例へのルーチンな後壁隔離追加は支持されない」。
   - **反論の材料**: 両試験とも後壁再伝導が 75.0%（39/52）・66.7% と極めて高い。Kistler ら自身が原因として (a) roof line が septopulmonary bundle の心外膜層を貫通しない、(b) epi-endocardial connection のため box 内追加焼灼が53%で必要、(c) **食道加温による透壁病変形成の阻害** を挙げ、"A surgical approach provides epicardial access to isolate the posterior wall." と書いている。一方 Goings のマッピングでは**外科の posterior LA box の再伝導は 3/47 (6.4%)**。
   - **しかし外科側にも反証がある**: CASA-AF（Haldar 2020／Boyalla 2024、CAPLA本文で二次引用）は thoracoscopic外科アブレーション vs 心内膜カテーテル で12か月・3年とも差なし。**「外科なら透壁だから勝てる」は未証明。**
   - また Nitta の box (n=90) vs U lesion (n=361) でも再発差なし（OR 0.50, 95%CI 0.21-1.15, P=.11）、CORNERSTONE の著者の "antral PVI already encompasses much of the LAPW" という説明とも整合する。**「後壁隔離の付加価値」は外科領域でも決着していない。**
3. **【線状焼灼は催不整脈的か】従来の懸念 vs PROMPT-AF／Marshall-Plan／Goings**
   - PROMPT-AF: AFL/AT からの freedom は 86.2% vs 82.7%、**HR 0.79 (95%CI 0.51-1.24), P=.25** — 線を足してもATは増えなかった。Marshall-Plan: 再発様式は両群とも持続性AF主体（P=0.67）。**両試験とも「ブロックを電気生理学的に確認したライン」という条件付き。**
   - 対して Goings: **LAA–僧帽弁輪ラインを置いた20例は100%が粗動を再発（vs 71.2%, P=.005）**、CTIラインを置くと非CTI右房粗動が増える（29.6% vs 10.2%, P=.031）。ただし Goings は再発例のみの選択集団で n=20、多変量なし、多重比較未補正。**そしてLAA–僧帽弁輪ライン自体の再伝導は 2/21 (9.5%) と低い** — 著者も「ラインが破綻したから粗動」ではなく「そのラインを置く症例背景」の可能性を残している。
   - **収束点**: 「不完全なライン＝催不整脈的、完全なライン＝催不整脈的でない」で概ね一致。**争点はむしろ「LAAに繋ぐラインは連続性（annulus-to-LIPV の併施）を担保できるか」という手技論に移っている。**
4. **【エネルギー源 vs 手技の丁寧さ】Goings（cut-and-sew 圧勝）vs 著者自身の留保**
   - Goings: PV再伝導 cut-and-sew 5%（40 PV）vs RF 56%（172 PV）vs cryo 67%（156 PV）、OR 0.07／0.11（P<.0001）。Nitta も cryo PVI群でAT 21%（16/77）vs bipolar RF 5%（18/341）、P<.001。
   - **反論**: Goings 自身が「最適な手技で行えば cryo/RF も同等になりうる」と留保。cut-and-sew 群は Maze III として施行時期が古く時代・術者効果の交絡が避けられない（Nitta のコホートも1993-2017年で era effect の調整が皆無）。Nitta の解析では**RF適用回数はブロック成否と相関しなかった**＝回数ではなくクランプの掛け方の問題。
   - **未解決**: この論点は S5（エネルギー源・透壁性）に持ち越す。S4 の枠内での結論は「lesion set の選択より lesion の完成度の方が効果量が大きい」（Nitta 多変量: PVペーシング OR 0.32 [0.13-0.71] > lesion set OR 0.50 [0.21-1.15, n.s.]）。
5. **【成功の定義そのもの】binary recurrence vs AF burden**
   - CAPLA では 62%（206/333）が「>30秒の再発あり」と判定されながら、3年時のAF burden中央値は両群とも 0%（再発例に限っても0%）、AFEQTは +34〜36点改善、最終受診時洞調律は 85.1%/87.1%。PROMPT-AF でも AF burden 中央値は両群 0.0%、QOLに差なし。
   - **外科文献で「洞調律率85%」と書かれている数値は、CAPLAでいう"最終受診時洞調律85%"に相当し、"（>30秒の）非再発率35-42%"とは全く別物である可能性が高い。** 統合レビューではこの2つを混同しないことが必須。
6. **【AAD の扱いの不統一】** 8編中、AAD off を成功の必須条件にしているのは **PROMPT-AF のみ**（class I/III の継続・再開を treatment failure と定義）。Marshall-Plan と CORNERSTONE は主要が on/off だが off-AAD の副次を別途報告（Marshall-Plan 84.7% vs 66.1%, P=0.022／CORNERSTONE P=.223）。CAPLA は on/off のみで3年時に27-33%がAAD継続。**外科の4編（Pyo・Guo・Nitta・Goings）はいずれも AAD の扱いを定義していない。** 外科成績とカテーテル成績を並べるときの最大の落とし穴。

---

## 統合レビューで使える一文（引用可能な形）

1. 僧帽弁手術に同時施行された外科的AFアブレーション1825例（左房のみ529例 vs 両心房1296例）の韓国5施設IPTW解析では、両心房アブレーションが中期のAF再発を抑制した（5年累積発生 28.6% vs 34.2%、SHR 1.256, 95%CI 1.121-1.406, P<.0001）一方、早期ペースメーカ植込みは 2.2%（29/1296）vs 0.4%（2/529）と多く（調整OR 0.16, 95%CI 0.07-0.38, P<.001）、死亡・脳卒中には差がなかった（晩期死亡 調整HR 1.171, 95%CI 0.735-1.863, P=.507）。

2. しかし同研究で三尖弁手術を要さなかった719例（左房のみ397 vs 両心房322）に限ると、AF再発の優劣は逆転し左房限局アブレーションが優位となり（調整SHR 0.76, 95%CI 0.62-0.93, P=.009）、ペースメーカ植込みの差も消失した（早期 調整OR 0.38, 95%CI 0.12-1.18, P=.095）ことから、右房lesionの追加は右房病変・三尖弁手術を伴う症例に選択的に適用すべきである。

3. 同時心臓手術における外科的アブレーションのRCT 19試験2031例（AF freedom解析1823例）のBayesian network meta-analysisでは、PVI（OR 5.02, 95% Cr.I 2.72-10.02）・左房lesion set（OR 7.97, 4.93-14.29）・両心房Maze（OR 8.29, 4.90-14.86）のいずれも非アブレーションに優ったが、3術式間には有意差がなく（random-effects）、エビデンスの確信度はGRADEでLow〜Very lowにとどまるため、「右房lesion不要」の証明ではなく「右房病変のない症例では左房限局で妥当」という限定的示唆と読むべきである。

4. Maze術後に心房頻拍を発症した36例中33例（92%）に電気生理学的検査を施行した単施設研究では、24例（67%）が焼灼線の不完全性によるマクロリエントリーであり、そのギャップ部位は冠静脈洞が16例（67%）と最多、次いで僧帽弁峡部5例・肺静脈隔離3例・三尖弁峡部2例であった。心内膜側の焼灼に心外膜側からの追加冠静脈洞焼灼を加えた症例では術後AT発症が14%から3%へ減少し（P<.001、多変量OR 0.21, 95%CI 0.06-0.82, P=.03）、エネルギー源による差はなかった（cryo 5% vs RF 3%, N.S.）。

5. 同研究では術中に肺静脈ペーシングによる伝導ブロック確認を行った211例中11例（5.2%）で焼灼線を越える伝導残存が検出され、ペーシング施行はlesion set（box vs U lesion, OR 0.50, 95%CI 0.21-1.15, P=.11）よりも強い術後AF再発の独立予測因子であった（OR 0.32, 95%CI 0.13-0.71, P=.004）。すなわちlesion setの選択より各lesionの完成度の検証が予後を規定する。

6. Maze後に再発しカテーテルアブレーションに至った86例の高密度マッピングでは、肺静脈再伝導が PVI施行例の78.3%（65/83）に認められ、その頻度は cut-and-sew 5%（40 PV）に対し radiofrequency 56%（172 PV, OR 0.11, P<.0001）・cryothermal 67%（156 PV, OR 0.07, P<.0001）と熱源lesionで著明に高かった。一方 lesion 別の再伝導率は左房 roof line 3/48（6.3%）・posterior box 3/47（6.4%）・mitral isthmus 5/44（11.4%）に対し、cavotricuspid isthmus line 8/28（28.6%）・intercaval line 3/15（20%）と右房lesionが最も破綻しやすかった。

7. 同研究で左心耳と僧帽弁輪をつなぐlesionを置いた20例は全例（100% vs 71.2%, P=.005）が粗動を再発し、左房粗動は80% vs 36.4%（P=.001）であった。このライン自体の再伝導は2/21（9.5%）と低いにもかかわらず粗動が多発した背景には、30%（6/20）で annulus-to-LIPV ラインが併施されずライン連続性が断たれていたことがあり、左心耳に繋ぐlesionは完全透壁・解剖学的連続性・電気的アンカリングを担保できないなら置かない方がよい。

8. 持続性AFに対する初回radiofrequencyカテーテルアブレーションでPVIに左房後壁隔離を追加したCAPLA試験の長期追跡（333例、中央値3.6年、IQR 3.2-4.3年）では、心房性不整脈非再発は 35.5%（59/169）vs 42.1%（68/164）とむしろ数値上劣り（HR 1.15, 95%CI 0.88-1.51, P=.55）、AF burden中央値も両群0%であった。ただし再アブレーション時の後壁再伝導が75.0%（39/52）に達しており、検証されたのは「耐久性のない後壁隔離」であって、心外膜側から食道を避けて透壁病変を作れる外科的box lesionを否定するものではない。

9. 日本16施設513例のCORNERSTONE AF試験でも、持続性/長期持続性AFに対する経験的な左房後壁隔離の追加は18か月の心房性不整脈非再発を有意には改善せず（80.9% vs 76.8%、HR 0.76, 95%CI 0.53-1.09, P=.110、絶対リスク差4.1%、NNT 24）、後壁再伝導は再手技70例中66.7%に認められた。加えて症候性胃不全麻痺が後壁隔離群のみ3例（1.2%）に発生しており、外科でも後壁・食道近傍のエネルギー印加時には迷走神経（胃前庭部枝）損傷を意識すべきである。

10. 一方、Cox-Maze由来の「線状焼灼による心房コンパートメント化」はカテーテル領域で2つのRCTが陽性を示した。PROMPT-AF（495例、中国12施設）ではMarshall静脈エタノール注入＋僧帽弁峡部・左房ルーフ・CTIの3ラインの追加により、12か月・抗不整脈薬非使用下の心房性不整脈非再発が 70.7%（174/246）vs 61.5%（153/249）（絶対差 9.2%, 95%CI 1.0-17.6、HR 0.73, 95%CI 0.54-0.99, P=.045）と改善し、Marshall-Plan試験（118例、単施設）では 86.4%（51/59）vs 66.1%（39/59）（絶対差 +20.3%, P=0.012、HR/95%CIの報告なし）であった。

11. ただしこれら2試験でも僧帽弁峡部の完全ブロックはPROMPT-AFで215/246（87.4%）、Marshall-Planで55例（全体93%）にとどまり、前者では62.6%（154/246）で冠静脈洞内からの追加焼灼を要した。Marshall-Plan試験では左房ルーフラインのみでブロックが得られたのは30例（全体51%）に過ぎず、44%（26/59）でフロアラインを追加してはじめてdome transectionが92%に達しており、外科的にもroof line単独ではなくroof＋floorのbox lesionを作るべきことを支持する。

12. 「線状焼灼は医原性心房頻拍を増やす」という懸念は、ブロックを電気生理学的に確認した場合には支持されなかった。PROMPT-AFではAFL/ATからの非再発が 86.2%（212/246）vs 82.7%（206/249）（HR 0.79, 95%CI 0.51-1.24, P=.25）、Marshall-Plan試験でも再発様式は両群とも持続性AFが主体（P=0.67）であり、再発例の再手技所見ではPV隔離は全例維持されラインのギャップ（僧帽弁3例・ルーフ2例・CTI 3例）のみが原因であった。すなわち催不整脈性をもたらすのはlesionの追加ではなくlesionの不完全性である。

13. Marshall-Plan試験では広範な線状lesionを追加しても左房A波速度は12か月時 61±20 cm/s へ改善し（P<0.001）PVI単独群（67±16 cm/s, P<0.001）との差はなく、重大合併症も1.7% vs 1.7%（P=1.0）と同等であったことから、「広範なlesion setは心房収縮を失わせる」という懸念に対する反証となる。

14. 本セクションの成績を横並びに読む際は、リズム判定手段の差に注意が必要である。外科系4編はいずれも間欠的12誘導ECG（Pyoは3・6・12・18・24か月→年1回で洞調律例のみ24時間Holter追加、Nittaは外来受診時ECGと症状時Holterのみ）に依存し、カテーテル系4編は週1回30秒の経電話心電図（Marshall-Plan）、毎週24時間の単誘導ECGパッチ（PROMPT-AF、実測平均13.0時間/週）、6/12/18か月の7日間モニタリング（CORNERSTONE AF）、TTM/CIED/28日連続ECGの混在（CAPLA）と異なる。CAPLAでは監視法によりAF burden中央値が有意に異なった（CIED 0.2% vs Kardia 0% vs 28日 0%, P=.008）ため、成功率の見かけ上の差の相当部分はlesion setではなく監視強度に由来する。

15. 抗不整脈薬の扱いも統一されていない。本セクション8編のうち成功の必須条件をAAD非使用としているのはPROMPT-AFのみ（3か月ブランキング後のclass I/III薬の継続・再開をtreatment failureと定義）で、CAPLAは on-or-off AAD で3年時に27-33%がAADを継続していた。外科の4編（Pyo・Guo・Nitta・Goings）はいずれもAADの扱いを成功定義に明記しておらず、外科成績とカテーテル成績を同一の物差しで比較することはできない。

16. なおCAPLAでは「>30秒の心房性不整脈の非再発」が35.5% vs 42.1%であったのに対し、「最終臨床受診時の洞調律」は85.1% vs 87.1%、3年時のAF burden中央値は両群0%、AFEQTは術前から+34〜36点改善していた。外科文献で報告される「洞調律率85%」は後者に相当する指標であり、厳格な非再発率と混同してはならない。
