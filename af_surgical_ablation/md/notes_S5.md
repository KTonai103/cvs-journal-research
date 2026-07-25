# 精読ノート S5 — エネルギー源とデバイス／新規デバイス（nsPFA含む）

> セッションB / 対象 5編 / 作成 2026-07-23
> 本ノートは統合レビュー執筆（セッションF）で**これだけを読めば足りる**ことを目指す。

## このセクションの結論（3-5行）

1. **RF vs Cryo は決着していない。** 8,293例・60研究のメタ解析（Baudo 2025）は Cryo 単独が bipolar RF（BRF）より良好（4年 freedom from AF 76.7%±2.2% vs 60.9%±2.2% vs BRF+Cryo 66.3%±1.6%、log-rank p<0.0001）と報告したが、**リズム判定手段・blanking period・>30秒閾値・AAD の扱いが各原著任せで全く統一されておらず**、4年 BRF は 2編78例しかない。因果ではなく仮説である。実務に落ちる部分は「双極クランプの jaw 先端が届かない僧帽弁輪・冠静脈洞・三尖弁輪は cryo で補完する」という技術論のみ。
2. **nsPFA（ナノ秒パルスフィールド）クランプは、透壁性と時間短縮において前臨床データが一貫している。** 3つの独立した慢性ブタ実験で透壁率 315/315切片(100%)（Serra 2023）、251/252切片=99.6%（Yi 2026）、lesion depth＝tissue thickness（回帰の傾き1.0、0–20mm）（Dunnington 2025）。焼灼時間は 1回 1.25–2.5秒（RF クランプは同一実験内で 28.6±16.7秒／1 lesion、7 lesion 合計 8.75秒 vs 200.5±24秒、P<.01）。
3. **周囲組織の安全性は「熱源より良い」方向のシグナルが揃っている**が、**冠動脈上の焼灼だけは現時点で禁忌扱い**。Dunnington では RF 群のみに LV 穿孔死・心内血栓・腎梗塞・食道粘膜下線維化が発生（device-related SAE 16.7%=1/6頭 vs nsPFA 0%=0/6頭）、横隔神経麻痺は両群とも0（35日生存10頭の左右＝20神経で麻痺なし）、食道内腔温上昇は両群 <1℃。一方 Yi 2026 では**経弁的（isthmus 代用）焼灼で 9頭中2頭(22%)が通電1秒以内の難治性VFで死亡**し、著者は "ablation over coronary arteries should not be performed" と明記。
4. **beating heart での box lesion は「できる」段階に到達した。** 心房切開なし・心外膜からクランプ1回設置・通電 5秒（2×2.5秒）で左房後壁＋PV box が透壁 59/59切片(100%)、30日 exit block は PV 5/5・LAA 6/6・RAA 5/6 の計 16/17(94%)。ただし **mitral isthmus / CTI line はクランプ形状上作れず**、単一エネルギー源での beating heart 完全 Cox-maze IV は未達。
5. **ヒト臨床データは事実上ゼロ。** 唯一のヒト報告は心外膜 GP（神経節叢）への PFA 12例の単群 feasibility（Musikantow 2024）で、これは lesion set ではなく除神経であり、Cox-maze/PVI の代替ではない。**nsPFA クランプのヒト成績は本ノート時点で未発表**であり、臨床採用判断は in-human trial 待ち。

---

## 論文別ノート

### [PMID 39674689] Baudo M, et al. 2025, Heart Lung Circ — 試験名なし（システマティックレビュー/メタ解析、PROSPERO CRD42022384218）

- **デザイン**: PRISMA準拠システマティックレビュー＋メタ解析。60編・8,293例（RCT 6編、PSM 7編、IPTW 1編、非調整観察研究 46編、出版年2001–2022）。統合は random intercept logistic regression による pooled event rate (PER)、晩期は Poisson regression、KM曲線が得られた18編は WebPlotDigitizer→R "IPDfromKM" で IPD再構成し統合KM＋log-rank＋4年landmark。異質性は Q・I²、I²>50%で leave-one-out。メタ回帰（単変量→多変量）。品質は Newcastle-Ottawa（NOS<6は1編のみ）と Cochrane RoB I。**出版バイアス評価（funnel plot / Egger / Begg）の記載なし**。R 4.2.2。
- **対象**: N=8,293（Cryo 3,364 / BRF 1,937 / BRF+Cryo 2,992）。**biatrial Cox-maze に限定**（uni-/monopolar RF、left maze等の縮小 lesion set、10例未満は除外）。AF病型内訳・LA径の実数は**本文に記載なし**（Supplementary Table S5/S6）。ただし本文は3群が「性別・糖尿病・高血圧・再手術・**AF病型**・**左房径**・同時手術」で有意に異なると明記しており、**直接比較に強い交絡がある**。考察の記述からは Cryo 群の方が平均LA径は大きかったと読める。
- **追跡**: 全体 mean 32.4±24.2ヶ月。**median (IQR) の記載なし**。個々の研究の追跡期間分布も記載なし。4年時点の解析対象は激減（BRF は 2編78例）。
- **エンドポイント定義**:
  - blanking period — **記載なし**（"blanking" の語が全文に出現しない）
  - AF/AT/AFL >30秒閾値 — **記載なし**
  - AAD off/on の扱い — **本メタ解析の定義としては記載なし**（考察で Ad らの他研究を "without antiarrhythmic drugs" と紹介する二次的記述があるのみ）
  - AFL/AT を再発に含めるかの統一規定 — **記載なし**（アウトカム名は一貫して "AF"）
  - 決定的な限界として原文は "The paper's definition of freedom from AF was used for each included study." と述べる＝**統一定義を設けていない**。
  - Early＝AF at discharge、Late＝(a) timepoint PER、(b) KM由来 freedom from AF。副次＝術後CVA、術後PPM、30日死亡、晩期CVA/PPM/死亡。
- **リズム判定**: ★**本文に記載なし。** 12誘導ECG・Holter（24/48/72h）・7日イベントレコーダ・ILR/PPM のいずれを用いたか、実施頻度がどうかについて Methods/Results/Discussion のどこにも記述がない。原著60編それぞれのモニタリング法を抽出も統一もしておらず、その異質性を限界として論じてもいない。→ "6ヶ月 6.73% vs 25.52%" という群間差が真の洞調律維持率の差なのか detection bias なのかを**本論文からは区別できない**。多くのタイムポイントで I² 70–95% という高異質性はこれと整合する。
- **主要結果**:
  - AF発生率 6ヶ月 — Cryo 6.73% (95% CI 3.59–12.25, 13編1,058例, I²=75.9%) vs BRF 25.52% (95% CI 10.93–44.88, 7編712例, I²=94.0%) vs BRF+Cryo 16.79% (95% CI 12.01–22.99, 10編1,329例, I²=65.4%)、3群 p=0.0112（C vs R p=0.0124、C vs C+R p=0.0086、R vs C+R p=0.3451）
  - AF発生率 1年 — Cryo 11.28% (8.09–15.51, 17編2,071例) vs BRF 19.80% (10.74–33.61, 10編1,038例) vs BRF+Cryo 15.66% (12.88–18.92, 11編1,585例)、3群 **p=0.1352（有意差なし）**
  - AF発生率 2年 — Cryo 12.91% (5.74–24.52, 8編701例) vs BRF 26.75% (10.60–52.94, 5編491例) vs BRF+Cryo 22.81% (16.37–30.85, 7編1,173例)、3群 **p=0.3319（有意差なし）**
  - AF発生率 3年 — Cryo 16.02% (7.85–29.94, 7編605例) vs BRF 56.50% (20.77–86.55, **2編112例**) vs BRF+Cryo 21.42% (18.28–24.93, 8編1,234例)、C vs R p=0.0359、3群 p=0.1103
  - AF発生率 4年 — Cryo 6.14% (0.98–30.13, 4編469例, I²=0.0%) vs BRF 51.39% (20.40–81.69, **2編78例**, I²=87.5%, LOO 31–77%) vs BRF+Cryo 16.09% (10.97–22.97, 5編593例)、3群 p=0.0392（※Abstract は BRF 51.59% と記載、本文/Table 1 は 51.39%＝原文内の不一致）
  - Freedom from AF（再構成IPD、18/60編）1年 — Cryo 91.1%±1.3% vs BRF 88.6%±1.3% vs BRF+Cryo 85.5%±1.0%（±はSE）
  - Freedom from AF 4年 — Cryo 76.7%±2.2% vs BRF 60.9%±2.2% vs BRF+Cryo 66.3%±1.6%、log-rank p<0.0001（Cryo vs BRF p<0.0001、Cryo vs BRF+Cryo p<0.0001、**BRF vs BRF+Cryo p=0.450 で差なし**）
  - 4年 landmark（4年以降のイベント） — Cryo vs BRF log-rank p<0.001、Cryo vs BRF+Cryo p<0.001、BRF vs BRF+Cryo p=0.178
  - メタ回帰（Cryo=参照）— 6ヶ月 BRF OR 4.82 (1.74–13.34, p=0.0025) / BRF+Cryo OR 2.70 (1.08–6.74, p=0.0333)；1年 BRF OR 2.06 (1.07–3.96, p=0.0294)；3年 BRF OR 6.23 (1.80–21.62, p=0.0039)；4年 BRF OR 12.04 (2.15–67.6, p=0.0047)
  - AF再発の独立予測因子（全体・多変量）— **平均LA径 OR 1.04 (95% CI 1.01–1.08, p=0.0159)＝1mm増ごとに4%増**（多変量で唯一有意。LVEF OR 0.96 (0.91–1.01, p=0.1320) は非有意化）
  - BRF群サブグループ（多変量）— 脳血管障害既往% OR 1.13 (1.07–1.19, p<0.0001)、平均LA径 OR 1.02 (1.01–1.05, p=0.0496)、**LAA閉鎖% OR 0.92 (0.88–0.97, p=0.0004)＝保護因子**
  - Cryo群サブグループ — 単変量で高LVEF OR 0.90 (0.83–0.97, p=0.0074)・lone ablation OR 0.89 (0.81–0.98, p=0.0218) が保護因子、多変量では LVEF のみ有意 OR 0.85 (0.74–0.98, p=0.0218)
  - BRF+Cryo群サブグループ（単変量）— 三尖弁同時手術 OR 1.01 (1.00–1.03, p=0.0188)、大動脈同時手術 OR 1.17 (1.02–1.34, p=0.0260)、および "two or more concomitant procedures" に対し OR 1.02 (1.00–1.04, p=0.0492) と OR 1.05 (1.04–1.06, p<0.0001) の2つが並記（原文の記述が "and two or more concomitant procedures (OR 1.02 … and OR 1.05 …, respectively)" と曖昧で、**どちらがどの変数かは原文で確認できず**）。多変量は推定パラメータ数超過で実施不能（N/A）
  - 術後PPM — BRF 1.06% (95% CI 0.60–1.86) vs BRF+Cryo 3.91% (95% CI 2.07–7.27)、p=0.0025。**Cryo群単独の値は本文になし**（Supplementary Table S8）
  - 晩期死亡 incidence rate — BRF 0.06%/月 (0.02–0.12) vs BRF+Cryo 0.22%/月 (0.12–0.41)、p=0.0084
  - **退院時AF（early outcome）は3群間で有意差なし（p=0.6620）**。術後CVA・30日死亡・晩期CVA・晩期PPM も有意差なし
- **限界**:
  - 【著者記載】3群のベースライン・同時手術が多項目で有意に異なる／freedom from AF は 60編中18編のみ、しかも実IPDではなくKM曲線からの再構成／真のIPD欠如のため予測因子解析不能／BRF+Cryo群は観測数不足で多変量不能／4年時点の timepoint 解析と生存曲線解析が一致しない（BRF の曲線報告研究が少ないためと著者自身が推測）。
  - 【読み手として】(a) **リズムモニタリングの方法・頻度が全く記載も統一もされていない**——2001–2022年の60編を跨いだ統合で、退院時ECGのみの研究と定期Holterの研究が混在しているはずだが抽出も感度解析もない。Cryo優位の相当部分が detection bias で説明可能であり、本論文からは排除できない。(b) blanking period・>30秒閾値・AAD の統一定義がなく、STS/HRS の標準報告基準に準拠していない。(c) 最も派手な差（4年 BRF）が **2編78例**、95% CI 20.40–81.69、LOO 31–77%、I²=87.5%＝結論を駆動しているのが最も薄いデータ。メタ回帰 OR 12.04 (2.15–67.6) も同様。(d) 出版バイアス評価が本文に記載なし。(e) 60編中46編が非調整観察研究で、エネルギー源の選択が術者・施設と強く交絡（実質的に施設間比較）。(f) 検索は2022年12月まで＝2023–2024年の hybrid/PFA 文献を含まない。(g) lesion set 完遂度（mitral isthmus / CTI / coronary sinus line を実際に置いたか、LAA処置の有無）が統合されておらず、エネルギー源よりも lesion set 完遂度の差が効いている可能性を排除できない。(h) COI：S.B. は AtriCure（bipolar RF clamp の主要メーカー）・Artivion・Medtronic、C.M. は Estech・Corcym のコンサルタント料を申告。
- **推奨クラス**: **該当なし。** 本論文自身は Class/LOE を提示せず、他ガイドラインの Class/LOE 表記の引用も本文中に存在しない（"Class"/"level of evidence" の語が全文で検出されない）。唯一のガイドライン言及は方法論上の PRISMA 2020 のみ。考察の "Both BRF and Cryo are the most frequently recommended energy sources for AF ablation." は出典を伴わない一般的言明。
- **外科への含意**:
  1. **双極RFクランプの構造的弱点が実務的に最も有用な記述**。endocardial jaw の先端は僧帽弁輪・三尖弁輪に到達できず isthmus line に gap を残しうる（Castellá JTCVS 2008 を引用）。ヒンジ開閉構造のクランプは jaw 先端での接触圧が低下し先端側の ablation 効果が落ちる（Varzaly ICVTS 2019 を引用）。心外膜脂肪・肥厚心房も透壁性を阻害する。→ **僧帽弁輪部・冠静脈洞・三尖弁輪部は cryo で仕上げる**のが本論文が支持する最も実務的な結論。
  2. **Cryo の安全性と代償**。冠動脈近傍・冠静脈洞への直接適用でも凝固壊死を起こさず線維組織・コラーゲンを温存する。ただし房室溝の冠動脈枝損傷は cryo を含む全エネルギー源で報告があり免罪符ではない。凍結・解凍時間および解凍後に組織が数分硬いままである分**手術時間が延びる**。
  3. **PPM と晩期死亡の数値は交絡込みで読む**。術後PPM BRF 1.06% < BRF+Cryo 3.91% (p=0.0025)、晩期死亡 0.06%/月 < 0.22%/月 (p=0.0084) はいずれも同時手術の複雑度差を反映している可能性が高い。
  4. **LAA閉鎖がリズム転帰の保護因子**（BRF群 OR 0.92, 95% CI 0.88–0.97, p=0.0004）——塞栓予防だけでなく再発抑制の観点からも Cox-maze IV に LAA 処置を必ず組み込む根拠を補強する。
  5. **引用時の注意**：絶対値（例：4年 freedom from AF 76.7%）を厳格モニタリングの前向き登録や Khiabani らの Cox-maze IV 長期成績と横並びに比較してはならない。**群内の相対比較（Cryo vs BRF）の傾向を示す仮説生成的エビデンス**として引用するのが妥当。

---

### [PMID 41005435] Yi J, ..., Damiano RJ Jr, Zemlin C. 2026, J Thorac Cardiovasc Surg — 試験名なし（前臨床動物実験、Pulse Biosciences 資金）

- **デザイン**: 慢性生存ブタモデル、**単群・非対照の feasibility study**。統計は記述統計のみ（R 4.4.1 / Prism 10、mean ± SD）。血管・弁の対照は同一個体内の ablated vs unablated セグメント（自己対照）。デバイス＝CellFX Parallel Clamp（nsPFA、カーブ jaw 4mm幅×53mm長、ジェネレータが組織厚に応じ最大15 kV まで自動調整、パルス列2.5秒）。
- **対象**: Yorkshire-Landrace豚 **9頭**（45.1±3.2 kg、雄5・雌4）。健常若齢豚・洞調律の正常心で **AF誘発モデルではない**（AF病型・LA径・同時手術は該当なし）。lesion set＝(1) LAA および RAA midbody 周状（各2.5秒）、(2) 左房後壁＋PV box（SVC背側/横洞と IVC 下にガイドを通し、**クランプ1回設置で 2×2.5秒＝5秒、心房切開なしの心外膜アプローチ**）、(3) transmitral（僧帽弁輪を跨ぐ）、(4) transtricuspid（三尖弁前尖を横断）。(3)(4)は mitral isthmus / CTI line の **surrogate**。生存 7頭（2頭が経弁的焼灼直後の難治性VFで術中死、1頭は胃潰瘍出血で早期安楽死）。組織解析は 7心・33 lesion・252断面。
- **追跡**: 生存7頭の平均 **26±7日**（本文）／26±8日（Abstract、**原文内で不一致**）。評価は術後30日時点。IQR/range 記載なし。
- **エンドポイント定義**: ヒト臨床のAF再発エンドポイントではないため、**blanking period・>30秒閾値・AAD off/on の規定はいずれも存在しない（該当概念なし）**。主要エンドポイントは (1) 透壁性＝"a continuous region of nonviable tissue (pale on TTC and turquoise on GT) from endocardium to epicardium"、lesion は全対応切片が透壁なら透壁と判定。5mm 間隔切片、TTC 10%を耳静脈から10分かけて生体内静注、Gomori trichrome 染色、ImageJ で実測。(2) exit block＝RAA・LAA・左PV の3か所で焼灼前／焼灼直後／30日の計3回。周術期に amiodarone 150mg を sternotomy 前に予防投与しているが**リズム成功判定ではなく術中不整脈予防目的**。著者自身が「exit block が確認されても組織学的透壁性と必ずしも一致しない」と明記（RAA で1切片が非透壁だが30日 exit block は成立）。
- **リズム判定**: ★ヒト臨床でいう 12誘導ECG/Holter/イベントレコーダ/ILR は**一切行われていない（本文に記載なし）**。代替は (a) 心外膜 pacing による exit block testing（3部位、焼灼前/直後/30日の**計3回のみ**）、(b) 心外膜心エコー（Philips iE33、apical 4-chamber 心外膜view、baseline と terminal の2時点のみ、盲検化された心臓麻酔科医が none/trace/mild/moderate/severe で逆流評価）。→ **94%(16/17) は「30日時点の pacing 部位あたり exit block 率」であって AF 非再発率ではない**。30日で testing site が減った理由は「濃厚な瘢痕内で pacing site が見つからなかった(n=1)」と「terminal surgery 前の動物死亡」。
- **主要結果**:
  - 切片レベル透壁性 — **251/252 = 99.6%**（心房 215/216=99.5%、心室 36/36=100%）
  - lesion レベル透壁性 — **32/33 = 97%**（非透壁は心房 lesion 1本のみ。TTC で非透壁→GT で焼灼域を横切る viable myocardium の band を確認）
  - 部位別透壁切片率 — RAA 54/55 (98%, 7 lesions)、LAA 39/39 (100%, 7)、**LAPW box 59/59 (100%, 7)**、transmitral 48/48 (100%, 6; 心房33/33・心室15/15)、transtricuspid 51/51 (100%, 6; 心房30/30・心室21/21)
  - 焼灼深度・幅 — ablation depth 6.7±3.3 mm、ablated tissue thickness 6.7±3.3 mm、lesion width 5.1±1.8 mm、jaw distance 2.0±1.8 mm、**最大焼灼深度 17.5 mm（心室 lesion、透壁）**
  - 部位別組織厚 — RAA 5.0±1.7 / LAA 4.6±1.1 / box 5.3±1.7 / transmitral 9.8±3.5（心房8.0±2.4・**心室12.3±3.3**）/ transtricuspid 9.2±3.5（心房8.2±2.7・心室10.0±4.0）mm
  - Exit block 焼灼直後 — **21/21部位 = 100%**（RAA 7/7、LAA 7/7、左PV 7/7）
  - Exit block 30日 — **16/17部位 = 94.1%**（RAA 5/6=80%、LAA 6/6=100%、PV/box 5/5=100%）。失敗した1部位は非透壁切片を含む lesion とは別部位
  - box lesion 焼灼時間 — **クランプ1回設置・心外膜のみ・心房切開なしで 2×2.5秒＝計5秒**。自験 EnCompass RFクランプ 72秒との対比（同一実験内比較ではなく既報との対比）
  - **術中死/VF（最重要の安全性シグナル）** — **9頭中2頭(22%)が経弁的焼灼中の難治性VFで死亡**。いずれも PFA 通電から1秒以内に発症、8–10回の除細動に不応。VF誘発 lesion の心室側焼灼長は非誘発例より長くはなかった（21.7 mm と 10.3 mm vs 30.1±9.9 mm）
  - 心房性不整脈 — PFA 起因のものは観察されず（9頭中0頭、率の分母提示は "No atrial arrhythmias" のみ）
  - 弁逆流（baseline vs 30日）— TR (N=6) p=.78、MR (N=5) p=.67 で有意な増悪なし。GT染色でも collagen disruption・炎症・壊死なし
  - 冠動脈（ablated vs 非ablated、0–4スケール盲検病理）— neointima p=.25 (N=9 vs 9)、inflammation p=.66、intimal thickness p=.27、collagen p=.32、elastin p=.25 (N=8 vs 8)。血栓・狭窄・解離・機械的損傷いずれもなし。VF死2頭の冠動脈も特記所見なし
  - 30日瘢痕 — ほぼ全切片で心筋線維が成熟しつつある線維性瘢痕に全層置換
- **限界**:
  - 【著者記載】数十年の併存疾患を経たヒト心と若齢健常豚心の差（豚は心外膜脂肪が少なく心房が薄い）／冠攣縮仮説の検証にはニトログリセリン併用/非併用の in vivo 経弁的焼灼が必要／冠動脈焼灼・経弁的焼灼の安全性は本研究では確立できず、晩期リモデリング（cryo で晩期内膜肥厚の既報あり）除外には 3–6ヶ月の慢性実験が必要。
  - 【読み手として】(a) n=9（解析7心）と極小、統計は記述のみで検出力は事実上なく、p=.78/.67 のような「差なし」は安全性の証明にならない。(b) **22%の術中VF死は前臨床として重大**。(c) transmitral/transtricuspid は実際の mitral isthmus・CTI line そのものではなく surrogate であり、冠静脈洞や回旋枝との位置関係の再現性は担保されていない。(d) このクランプでは実際の isthmus line が作れず「nsPFA を linear probe に適応させる必要がある」と著者も明記＝**単一エネルギー源による beating heart 完全 Cox-maze IV は未達**。(e) AFモデルではないため AF停止・洞調律維持の効果は一切評価されていない。(f) 生存日数が本文26±7日と Abstract 26±8日で不一致。(g) COI：Pulse Biosciences 資金、Zemlin 氏は同社株式保有、Damiano 氏は AtriCure 等からの資金。(h) TTC全身静注＋5mm間隔切片では 5mm未満の gap を見逃しうる。
- **推奨クラス**: **該当なし。** 本論文自身は Class/LOE を提示しない。2024 EHRA/HRS/APHRS/LAHRS expert consensus (Tzeis, Europace 2024) と Ad/Damiano/Badhwar 2017 STS-AATS expert consensus (JTCVS 2017;153:1330) を引用しているが、**本文中に Class I/IIa 等の具体的表記は現れない**（二次引用にすら Class 表記なし）。規制上の記述として「CMP IV は FDA が外科的AF治療として承認した唯一の術式」との言及があるが、これも著者自身の推奨ではなく事実の引用（二次引用）。
- **外科への含意**:
  1. **box lesion のゲームチェンジャー候補**。心房切開なし・心外膜アプローチ・クランプ1回設置・通電5秒で左房後壁＋PV の完全隔離が透壁 59/59切片(100%)。現行 EnCompass RFクランプ（自験72秒）、bipolar RF の20–40秒×2サイクル、cryo の2–3分と桁違いに短く、しかも**拍動心で成立**している。体外循環・大動脈遮断を追加せずに CMP IV の core lesion を置ける可能性を示す＝concomitant 症例で AF ablation が敬遠される最大の理由（CPB時間延長）に直接効く。
  2. **厚みへのロバストネス**。1mm未満から 17.5mm まで、房室溝で急に厚くなる部位（transmitral 心室側 12.3±3.3 mm、transtricuspid 心室側 10.0±4.0 mm）でも 2.5秒単発で透壁。心外膜脂肪や肥厚心房でも通用しうる根拠。
  3. **isthmus line はまだ渡ってはいけない橋**。臨床の mitral isthmus line は回旋枝・冠静脈洞の直上、CTI line は右冠動脈近傍を走るため、9頭中2頭の通電1秒以内 VF は外科的にそのまま警告として読むべき。**現状 mitral/CTI line は依然として endocardial cryo が標準であり、本研究はそれを覆さない。**
  4. **弁近傍への安心材料（限定的）**。弁尖では逆流増悪なし（TR p=.78, N=6／MR p=.67, N=5）・線維骨格の構造保持あり。nsPFA が細胞膜脂質二重層に選択的で細胞外マトリックスを温存する機序と整合するが、n=5–6・30日という限界を忘れないこと。

---

### [PMID 39644967] Dunnington GH, ..., Ad N. 2025, J Thorac Cardiovasc Surg — 試験名なし（Pulse Biosciences CellFX Parallel Clamp の前臨床GLP試験、Open access CC BY-NC-ND）

- **デザイン**: 慢性ブタモデル、**前向き・バランス化・1:1 無作為化比較（GLP準拠）**。介入＝nsPFA CellFX Parallel Clamp（Pulse Biosciences）、**対照＝バイポーラRFクランプ（AtriCure Isolator Synergy Clamp）**。組織病理は board-certified histopathologist の**盲検判定**。→ 本セクション5編中、**唯一 RF と nsPFA を同一プロトコルで直接比較したランダム化デザイン**。
- **対象**: 雌 domestic swine (Yorkshire Cross) **計12頭（nsPFA 6 / RFA 6）**、体重 56–64.8 kg、全頭 median sternotomy。1頭あたり 7 lesion＝①SVC周状、②RA/RAA（purse-string 経由 linear 1本＋RAA周状1本）、③LA/LAA（purse-string 経由 linear 1本）、④左PV周状、⑤LV（purse-string 開口部経由）、⑥RV。完遂は各群5頭・計10頭（nsPFA 1頭は術後15日に procedure-related but non-device-related な心嚢液貯留で予定外安楽死、**RFA 1頭は術後24日に LV 焼灼部の erosion→穿孔による大量血心膜で死亡＝device-related SAE**）。AF患者ではないため AF病型・LA径・同時手術は該当なし。
- **追跡**: 計画 **35±5日**。実際は各群5頭が35日到達、nsPFA 1頭は15日で終了、RFA 1頭は24日で死亡。図の記載では nsPFA の成熟瘢痕評価が36日、RFA代表例が37日。**median (IQR) の記載なし**。
- **エンドポイント定義**: ヒトのAF再発エンドポイントではなく前臨床代替。主要＝(1) exit block（SVC・RAA・左PV でペーシング、術中および術後35日 preterminal）、(2) 盲検組織病理による lesion width/depth/transmurality、(3) 一般安全性（device-related SAE、undesirable histopathologic alterations＝穿孔・臨床的に有意な erosion・周囲組織障害・熱障害所見）。副次＝食道内腔温度（各焼灼サイクル中の上昇が1℃未満か、**単一サーミスタ1点測定**）、横隔神経麻痺。**blanking period の設定なし（記載なし）／>30秒閾値の定義なし（記載なし）／AAD off-on の扱いも記載なし（AAD投与の記述自体が本文に存在しない）。「成功」は AF-free ではなく exit block + 透壁性瘢痕で定義**。
- **リズム判定**: ★ヒト試験でいうリズムモニタリングは実施されていない。行われたのは (a) ベースライン心電図（誘導数の記載なし）、(b) ベースライン／焼灼後／術後35日再開胸時の pacing による exit block testing。ペーシング条件は **120 PPM、3.0–10.5 V、第3パラメータ 1.0**（Table 1 の列見出しは原文で "mV" と表記されており、pulse width 1.0 ms を指すかは**原文で確認できず**）（注記 "Voltage increased to 10 V, exit block still observed."）。横隔神経評価も 10.0 V / 120 PPM / 1.0（同上）。**Holter・7日イベントレコーダ・ILR/PPM 等の連続モニタリングは一切なし（本文に記載なし）**→本論文から「AF non-recurrence rate」は読み取れない。
- **主要結果**:
  - Exit block（術後35日 preterminal）— 生存10頭×3部位＝**30/30部位 (100%) で block あり、両群とも**。p値の記載なし
  - device-related SAE — **nsPFA 0%（0/6頭）vs RFA 16.7%（1/6頭＝術後24日の LV 穿孔死）**。統計検定・95%CI の記載なし
  - 望ましくない組織病理学的変化（盲検判定）— **nsPFA 0% vs RFA 7.1%**。RFA 群では焼灼部位の **3/42 (7%)** に tissue erosion 関連の有害転帰（LV穿孔死1＋erosion 2）
  - 血栓・塞栓 — RFA 群の erosion した LV lesion 2つに血栓性物質、うち1頭は**腎梗塞（全身性血栓塞栓）**を合併。nsPFA 群 0件（分母は各群6頭）
  - 1回あたり焼灼時間 — **nsPFA 1.25秒/箇所（組織厚に依存せず一定、SD 0）vs RFA 28.6±16.7秒**。7 lesion 合計で **nsPFA 8.75秒 vs RFA 200.5±24秒、P<.01**（95%CI 記載なし）
  - Lesion 幅／深さ（mean±SD、n=切片数）— 左房 nsPFA 4.9±1.7 / 4.7±2.1 mm・1.25±0秒 (n=43) vs RF 6.2±2.7 / 5.1±1.5・23.4±2.6秒 (n=30)；右房 5.3±1.5 / 3.3±1.6 (n=61) vs 5.3±2.5 / 3.7±1.7・16.1±3.6秒 (n=65)；左PV 4.1±1.2 / 1.7±0.7 (n=21) vs 4.1±2.1 / 3.1±1.6・30±5.8秒 (n=37)；**LV 7.6±1.7 / 11.1±2.1 (n=29) vs 17.9±5.8 / 12.7±2.9・58.4±11.7秒 (n=31)**；RV 7.2±1.3 / 5.6±1.6 (n=32) vs 8.1±3.8 / 4.9±0.8・35.4±14.2秒 (n=33)；SVC 4.0±1.7 / 1.2±0.4 (n=35) vs 3.7±1.8 / 1.8±0.8・16.8±4.2秒 (n=36)。**部位別の群間 p値・95%CI は表に記載なし**
  - 透壁性 — nsPFA では全 lesion が透壁。**lesion depth vs tissue thickness の回帰直線の傾き＝1（tissue thickness 0–20 mm の範囲）**（TTC 10%心臓灌流後、クランプ顎に垂直に切片、H&E＋Masson trichrome）
  - 瘢痕成熟／炎症 — 軽微〜軽度（原文 "minimal-to-mild"）の炎症細胞浸潤 RFA 100% vs nsPFA 23%；線維化領域内の壊死心筋細胞残存 RFA 77% vs nsPFA 11%；多巣性石灰化 RFA 43% vs nsPFA 0%（**各分母 lesion 数の明記なし、p値なし**）
  - 早期瘢痕成熟 — nsPFA 群で15日安楽死の**1頭のみ (n=1)** で透壁性線維化が完成、ただし壊死心筋細胞の残存巣も併存
  - 横隔神経 — 両群とも左右いずれも麻痺なし（生存10頭全例、10.0V刺激で確認）
  - 食道内腔温度 — **両群とも全焼灼で上昇 <1℃**（成功基準を満たす）。**にもかかわらず RFA 群の24日死亡例の食道には軽度粘膜下線維化＋中等度炎症あり**
  - 投入エネルギー量 — 2mm厚の焼灼で **nsPFA 約1.6 J vs RF 約430 J（約270倍）**で同等の焼灼寸法
- **限界**:
  - 【著者記載】食道温は単一サーミスタ1点測定で食道外側の損傷を反映しない可能性／臨床の maze lesion set に必要な transmitral / transtricuspid の弁輪部 lesion が作成可能かは**本研究では設計上検証されていない**（"The present study was not designed to answer this question"）／至適 application 回数は未確定（位置ずれ補正のため各部位2回以上が望ましいかもしれないが本研究は1回のみ検証）／実臨床の bipolar RFA クランプは複数サイクル適用するのが通例で本研究の RFA 時間は臨床実態と異なる可能性。
  - 【読み手として】(a) N=12頭（完遂各5頭）と極小で、SAE 16.7% vs 0% は 1頭の事象に依存、95%CI も検定もない。(b) 正常心ブタで、線維化・拡大したヒト慢性AF心房とは組織条件が全く異なり、臨床の durability は推定できない。(c) リズム評価は exit block のみ＝AF治療効果の直接エビデンスにならない。(d) **RFA の主要安全性シグナル（穿孔・血栓）はデバイス評価目的の人工的な LV lesion 由来**で、心房のみを扱う実臨床の RFA クランプ安全性への一般化は慎重を要する。(e) COI が濃厚（Pulse Biosciences 支援、著者7名中6名が同社株式/ストックオプション保有、うち3名は同社所属）。(f) Table 2 の n（21–65）が lesion 数ではなく切片単位と考えられるが単位定義が不明確で、動物内クラスタリングを考慮した統計処理がない。(g) 幅・深さの群間比較に p値/95%CI が一切示されず "SDが小さい" という記述的比較にとどまる。
- **推奨クラス**: **該当なし。** 前臨床動物研究であり Class/LOE の提示は一切ない。Badhwar V, et al. STS 2017 clinical practice guidelines (Ann Thorac Surg 2017;103:329-341) を導入部で引用しているが**二次引用**であり、Class・LOE の数値表記は本文に出てこない。「RFA を弁輪部 lesion に使うことは推奨されない」（"As we know it is not recommended to use RFA in that manner"）も**出典の明示がない著者の一般論**であり、二次引用扱いとすべき。
- **外科への含意**:
  1. **クランプ焼灼時間の劇的短縮**。組織厚に依存せず1回1.25秒、7 lesion 合計 8.75秒 vs RFA 200.5±24秒（P<.01）。RFA は厚い LV で 58.4±11.7秒、左PV で 30±5.8秒と部位差が大きく、実臨床では複数サイクルでさらに延長する。cross-clamp 中の LA lesion set 短縮＝「時間がかかるから concomitant AF 手術を省略する」という現場の最大の障壁に直接効く。
  2. **熱源由来合併症の構造的回避**。**食道内腔温が両群とも <1℃だったにもかかわらず RFA 群で食道の粘膜下線維化＋炎症が生じた**点は、術中温度モニタリングでは熱傷を検出しきれないことを示す実務的警告。
  3. **透壁性の予測可能性**。lesion depth ＝ tissue thickness（傾き1.0）で厚い LV（深さ11.1±2.1 mm）まで透壁。幅の SD が RFA より小さい（LV幅 7.6±1.7 vs 17.9±5.8 mm）＝再現性が高く目的外組織への過剰焼灼が少ない。Maze IV で問題となる「非透壁 lesion による gap→AT/AFL 再発」の低減が期待される。
  4. **未解決**：クランプ型のため mitral isthmus / CTI の弁輪部 lesion は本デバイス単独では作れず、著者も未検証・cryo 等の併用が必要な領域と明記。現時点の nsPFA クランプは **PVI＋posterior wall box（＋SVC/RAA）までの置換**であり full Cox-maze IV の完全置換ではない。ヒトでの AF free 生存は in-human trial の結果待ち（"We now await the results of in-human trials"）。

---

### [PMID 37920983] Serra F, ..., Zemlin CW. 2023, Circ Arrhythm Electrophysiol — 試験名なし（Research Letter）

- **デザイン**: 前臨床・慢性生存動物実験、**Research Letter 形式・単群記述研究**。対照群（RF/cryo等）**なし**。ランダム化・盲検化の記載なし。統計学的仮説検定は行われておらず、**効果量・95%CI・p値の記載は一切なし（mean±SD のみ）**。資金＝Pulse Biosciences 社研究助成、Zemlin 医師は同社株式保有。
- **対象**: Yucatan ミニブタ **n=14**（雌雄、月齢4–7ヶ月）。コホート＝術後**6週 harvest n=6**、術後**6ヶ月 harvest n=8**。ヒト患者は含まない（AF病型・LA径・同時手術は該当なし）。手技＝胸骨正中切開、心膜クレードル、クランプ内側 jaw に矩形電極（長さ30mm、幅**3mm または 6mm**）。右心耳・左心耳に double-layer lesion 各1本、右心耳近傍 purse string からクランプ挿入し向きを2–3方向変えて lesion 作成、左房も同様に2–3 lesion、1心臓あたり計6–8 lesion。**総 ablation 数 105**。
- **追跡**: 6週（n=6頭）と6ヶ月（n=8頭）の固定2コホート。median/IQR は該当なし（あらかじめ定めた harvest 時点のため）。
- **エンドポイント定義**: 主要は臨床的リズムアウトカムではなく**組織学的透壁性**。各 lesion につき3枚の横断切片、TTC染色で焼灼＝白色/生存＝赤色と判定（105 ablations × 3切片 = **315 cross-sections**）。副次＝lesion depth/width 実測、Gomori trichrome／smooth muscle actin (SMA) による残存組織同定、connexin-43 による伝導能推定、Ki-67 による増殖能評価。**>30秒閾値・blanking period・AAD 継続例の扱いはいずれも設定されていない（該当概念が本文に存在しない）。**さらに **lesion の電気生理学的伝導ブロック確認も行われていない**："functional electrophysiological testing of the lesions was not performed in this study"。
- **リズム判定**: ★**本文に記載なし。** 12誘導ECG／Holter／イベントレコーダ／ILR による洞調律維持モニタリングは一切なし。唯一のリズム関連記述は急性期安全性の「>100 atrial ablations consisting of 6 to 36 shocks, no arrhythmias were induced」のみ（術中の不整脈誘発の有無の観察で、モニタリング手段・記録時間の詳細は記載なし）。**慢性期の心電図モニタリングも lesion の伝導ブロック検証も未実施**。
- **主要結果**:
  - 透壁性（主要）— **315/315 cross-sections (105 ablations × 3切片、14頭) が透壁＝100%**。95%CI・p値の記載なし（記述統計のみ）
  - 6ヶ月 lesion の深さ — **4.26±1.54 mm**（全 lesion 透壁のため組織厚と同値）
  - lesion 幅 — 3mm電極で **4.02±1.67 mm**、6mm電極で **6.90±1.41 mm**（いずれも電極幅より約0.9–1.0mm 広いだけ）
  - lesion 内組織構成 — 主にコラーゲンと脂肪。**脂肪含有量は可変で range 20%–70%**（定量法・分母の記載なし）
  - 心内膜下の残存生存組織 — 焼灼域の心内膜下に少量の生存組織をしばしば認めたが、追加染色で **全例（in all cases）平滑筋（SMA陽性）と同定＝心筋の残存ではない**
  - 残存平滑筋の分布（6ヶ月 lesion **55本**を解析）— no/minimal **9/55 (16.4%)**、thin focal **27/55 (49.1%)**、thick and wide **2/55 (3.6%)**。残り17/55は thick focal と thin wide に分布するが**内訳の数値は本文に記載なし**（Figure Q のヒストグラムのみ）
  - 残存平滑筋の伝導能 — 残存平滑筋を含む lesion では **connexin-43 が検出されず**、生存組織は一貫して connexin-43 陽性→残存平滑筋は活動電位を伝導しないと推定（**ただし機能的EP検証は未実施**）
  - 増殖活性 — **全 lesion が Ki-67 陰性**＝lesion 内組織はもはや増殖しておらず成熟済み
  - 血管壁平滑筋 — 周囲平滑筋は **intact**（nsPFA を生き延びたか完全回復したかのいずれか）
  - 安全性 — 術中・術後を通じ合併症ゼロ。**>100 atrial ablations（1部位あたり6–36ショック）で不整脈誘発なし**（分母は "＞100" と曖昧表記）
  - 焼灼パラメータ（再現に必要）— **300 ns幅パルスを18発、6 Hz、振幅10–12 kV、CellFX パルス発生器**
- **限界**:
  - 【著者記載】lesion の機能的電気生理学的検証を行っていない。残存平滑筋が伝導しないという結論は connexin-43 染色所見からの推定にとどまる。
  - 【読み手として】(a) Research Letter で方法記載が極めて簡潔、統計解析の記述が一切なく 95%CI・p値・比較対照が存在しない。(b) **対照群がなく既存デバイスへの優越性・非劣性は言えない**。(c) **6週コホート (n=6) の lesion depth/width が本文に示されておらず**、6週 vs 6ヶ月の経時変化（lesion の収縮・成熟）の定量比較がない。(d) 残存平滑筋解析が「55 of our 6-month lesions」と一部に限られ、**55本という分母の選択基準が不明**、thick focal・thin wide の実数も本文になし。(e) **焼灼部位が右心耳・左心耳および左房の一部に限られ、実際の Maze で問題となる部位（PV入口部、僧帽弁輪-冠静脈洞、右房峡部、crista terminalis）は評価されていない**。(f) 正常・薄い（4.26 mm）若齢ミニブタ心房での評価で、AF患者の拡大・線維化・肥厚した心房での透壁性は不明。(g) 脂肪含有20–70%は心外膜脂肪が厚い部位でのエネルギー到達性の懸念を残す（ただし本研究では全例透壁）。(h) COI（Pulse Biosciences 助成、責任著者が同社株式保有）があり、単群かつ100%成功という結果の解釈には注意。(i) 14頭では稀な合併症（食道・冠動脈・横隔神経損傷）を検出する検出力はなく、そもそも周辺臓器の組織学的評価が記載されていない。
- **推奨クラス**: **該当なし。** Research Letter で Class/LOE の記載は一切なく、他ガイドラインの引用もない（引用文献5編はすべて基礎・前臨床研究）。
- **外科への含意**:
  1. **既存ワークフローをそのまま踏襲できる**。クランプ幅3mm/6mm、電極長30mm、心耳・purse string からのクランプ挿入という手順は現行の bipolar RF クランプと同一で、Cox-maze IV のクランプ由来 lesion をエネルギー源だけ置換できる可能性を示す。学習曲線・器具レイアウト変更が最小。
  2. **焼灼時間**：1部位 300 ns × 18発 @ 6 Hz ＝実質数秒。RF の複数回 clamp-and-hold より大幅に短く、CPB／大動脈遮断時間の短縮に直結しうる。
  3. **lesion 幅が電極幅とほぼ一致**（3mm→4.02±1.67 mm、6mm→6.90±1.41 mm）＝lesion が電極から大きく外側に広がらない。RF の熱伝導による予測困難な広がりと対照的で、**僧帽弁輪近傍や右房 lesion の安全域設計に有利**（回旋枝・食道・横隔神経・洞結節動脈への巻き添えが小さい）。
  4. **組織選択性の直接的証拠**：血管壁平滑筋が intact＝PFA が心筋を選択的に殺すという主張を組織レベルで裏付ける。冠動脈狭窄・食道瘻という重大合併症リスク低減の理論的根拠。
  5. **鵜呑みにしない点**：(a) 外科医が求めるのは「白く染まった」ことではなく「伝導しない」ことであり、**本研究はその決定的証拠を出していない**。(b) 正常・薄い（4.26 mm）ブタ心房の結果で、長期持続性AF・僧帽弁疾患による拡大線維化心房は未検証。(c) 脂肪含有20–70%は房室溝周辺での適用に留保を残す。

---

### [PMID 39066781] Musikantow DR, ..., de Groot JR. 2024, JACC Clin Electrophysiol — **NEURAL-AF-2**（NCT05426759）

> ※本編は lesion set の論文ではなく **心外膜 GP（ganglionated plexi）除神経**の論文。S5 に置くのは「PFA という新規エネルギー源をヒトの開胸下で使った唯一の報告」だからであり、Cox-maze/PVI の代替を論じたものではない。

- **デザイン**: 単施設・**単群（single-armed）前向き feasibility**、Research Letter。**対照群なし・盲検なし**。介入＝開胸下・心外膜アプローチで心臓神経節叢へ pulsed field ablation（open chest epicardial deganglionation system, AtriAN Medical Ltd）、CABG または弁手術に付随して施行。実施地は Tbilisi Heart and Vascular Clinic（ジョージア）。統計は paired t-test のみ、mean±SD。**多重比較補正の記載なし**（著者自身 "the small sample size and multitude of testing raise the potential for both type I and type II errors" と明記）。
- **対象**: **N=12**（全例解析）。年齢 63.6±5.1歳、男性 83%(10/12)、LVEF 48%±4.4%、**左房径 3.6±0.6 cm**。AF病型は**全例 paroxysmal AF の既往あり**（持続性/長期持続性の組入れなし）。AF確認は心電図 n=10、Holter n=2。ベースラインで **7/12例(58%)** がカルディオバージョンまたは AAD 治療を要していた。ターゲットは **5か所の心外膜GP、合計60発のECG同期パルス（1,000 V、100 µs）**。同時手術は CABG n=10、AVR n=2。**PVI も Cox-maze lesion set も一切行っていない。** CHA2DS2-VASc・AF罹病期間の記載なし。ベースライン Holter では**12例全例で AF が検出されず（実質 burden 0%）**。主要HRV解析は「β遮断薬一定」サブグループ（3例除外＝**実質 n=9**）。
- **追跡**: **12か月**（ベースライン、30日、3・6・12か月のプロトコル固定）。median (IQR/range) の記載なし。脱落・打ち切りの記載なし（HR/HRV は "available for all patients"）。
- **エンドポイント定義**: **正式な primary endpoint の定義文が存在しない**（目的は "to assess the efficacy of PF energy targeted at GP in patients undergoing CABG or valve surgery" のみ）。**blanking period の設定・長さの記載は一切なし**（術後30日 Holter もそのままイベント判定に用いている）。**AF/AT/AFL >30秒等の持続時間閾値の定義も記載なし**（代わりに AF burden 0.30% が報告されている）。**追跡期間中の AAD 継続例を成功に含めるか否かの定義も記載なし**（ベースラインで58%が cardioversion/AAD を要した記述のみ、フォロー時の AAD 使用状況・中止プロトコルは記載なし）。β遮断薬は術後3例で有意に増量され、HRV 解析ではこの3例を除いた感度解析が主表。→ **ガイドライン準拠の rhythm outcome 定義を満たしておらず、Cox-maze 等の外科成績との直接比較は不可能。**
- **リズム判定**: ★**24時間Holter のみ**（連続モニタでも ILR/PPM でもない）。頻度は術前ベースライン1回＋術後 **30日・3・6・12か月の計4回**。入院中は "postoperative monitoring as standard of care"（詳細記載なし）。**12か月で合計わずか96時間（4日分）のサンプリング**であり、発作性AFの検出感度は極めて低い。12誘導ECGは AF既往の確認（n=10）に用いられたのみで定期フォローの頻度は記載なし。ILR等の植込み型連続モニタリングは不使用。→「1例のみ再発、burden 0.30%」は**大幅な過小評価の可能性**。
- **主要結果**:
  - 退院前の臨床的AF再発 — **0/12例 (0%)**。デバイス関連有害事象も 0件
  - 術後Holter(4回)でのAF再発 — **1/12例 (8.3%)** のみ、burden 0.30%、4回中3か月時点の1回のみで検出。**ベースラインHolterでは12例全例 AF 検出なし**
  - 術中AERP変化 — **+6.9%±19.6%、P=0.38（非有意）**（右房および/または左心耳ペーシングで焼灼前後に測定）
  - 平均HR（β遮断薬一定群 実質n=9）30日 — **84.4±12.1 vs 70.3±8.2 bpm、P=0.03**（有意上昇）
  - 平均HR 12か月 — 75.2±8.8 vs 70.3±8.2 bpm、**P=0.10（トレンドのみ）**
  - **rMSSD（副交感神経指標）12か月 — 42±15 vs 59±18 ms、P=0.01**（有意低下＝迷走神経活動の持続的減弱）
  - **HF power 12か月 — 198±153 vs 321±189 ms²、P=0.05**
  - その他HRV（12か月 vs baseline、いずれも非有意）— 最小HR 65.6±9.6 vs 60.7±8.6 (P=0.19)、SDNN 95±27 vs 95±22 ms (P=0.99)、SDANN 145±106 vs 129±45 ms (P=0.44)、pNN50 4.4±3.1% vs 6.5±4.1% (P=0.208)、LF 239±171 vs 284±176 ms² (P=0.35)、VLF 1,446±959 vs 1,439±692 ms² (P=0.98)、ULF 3,127±2,141 vs 2,131±1,026 ms² (P=0.28)、最大HR 85.0±9.3 vs 86.6±18.2 (P=0.80)
  - **全例(n=12、β遮断薬変更例含む)ではすべて非有意** — 平均HR 72±9.6 vs 70.8±7.4 (P=0.66)、SDNN 111±40 vs 98±22 ms (P=0.33)、rMSSD 44±15 vs 55±17 ms (P=0.09)、HF 208±146 vs 281±179 ms² (P=0.19)
  - AFEQT総合 12か月 — **84.8±4.7 vs 74.4±6.4、P<0.01**（30日85.2±4.5 / 3か月87.0±2.8 / 6か月86.9±3.9）
  - AFEQT症状サブスコア — 30日で改善（95.8±5.0 vs 86.1±10.4、P<0.01）だが **12か月では有意差消失**（89.6±6.3 vs 86.1±10.4、P=0.26）
  - 安全性 — デバイス関連有害事象 **0件/12例**。CABG 10例・AVR 2例すべてで手技完遂
- **限界**:
  - 【著者記載】サンプルサイズが小さく検定回数が多いため type I／type II エラー双方のリスク／ベースライン AF burden が低く burden についての結論を導きにくい／AERP が非有意なのは SD が大きく標本が小さいため／**「心臓手術そのものの影響」と「PF ablation の効果」を区別できない**ため大規模対照試験が必要。
  - 【読み手として】(a) 単群12例・対照なし・単施設で、CABG/AVR 自体の抗不整脈効果や周術期β遮断薬・術後管理の交絡を排除できない。(b) **リズム監視が24時間Holter×4回のみ（12か月で計96時間）**と極端に疎で、発作性AFの再発を系統的に見逃す設計。ILR を用いた同種研究との比較は不可。(c) blanking period・>30秒閾値・AAD off での成功といった標準定義が一切なく、「1例のみ再発」は他の外科的AF治療成績と同一土俵で比較できない。(d) **ベースラインで12例全例が Holter で AF 陰性＝事実上「AFがほとんど出ていない集団」**であり、天井効果で efficacy を示せない。(e) AFEQT は非盲検単群の PRO で、心臓手術後の全般的QOL改善・プラセボ効果と分離不能（症状サブスコアは12か月で有意差消失）。(f) 一次エンドポイント未定義のまま20行超のHRV指標がテストされており、rMSSD P=0.01・HF P=0.05 は多重性補正なしでは仮説生成レベル。(g) 主要HRV解析が「β遮断薬一定群」という **post hoc サブグループ（実質n=9）**。(h) COI が濃厚（AtriAN Medical 社員3名が著者、施設は同社から grant support、Mayo Clinic が関連特許を保有）。(i) Research Letter のため GP同定法・PF出力設定の全容・透壁性確認法・**GP ablation の完遂判定基準が不明**。
- **推奨クラス**: **該当なし。** Class/LOE の記載は一切なく、他ガイドラインの引用もない（引用文献4本はいずれも原著論文）。
- **外科への含意**:
  1. **何を扱っていて何を扱っていないか**。これは Cox-maze/PVI の lesion set ではなく、心房筋に lesion を作らず PFA の tissue selectivity で GP を選択的に傷害する「外科的除神経」の第2報である。外科医が想起すべきは「maze/PVI に GP ablation をアドオンする」という既存概念。
  2. **実現可能性は示された**：開胸・拍動下で CABG 10例・AVR 2例に付加でき、デバイス関連有害事象 0/12。5点×計60パルスの ECG同期照射という手技負荷は小さい（ただし付加時間・CPB時間の記載はなし）。
  3. **生理学的エンドポイントは達成**：rMSSD（59±18→42±15 ms、P=0.01）と HF power（321±189→198±153 ms²、P=0.05）が12か月まで持続低下＝**GP除神経の耐久性をヒトで示した初のデータ**。従来の RF/cryo による GP ablation は効果の持続性が疑問視されてきたため、「PFA なら耐久性がある」という仮説を支持する。
  4. **急性完遂の指標がない**：AERP は有意に延長せず（+6.9%±19.6%、P=0.38）。外科的に「どこまで焼けば十分か」の術中中止基準が存在しないのは臨床導入上の弱点。
  5. **臨床的AF抑制の主張は受け取ってはいけない**：12例・対照なし・ベースラインHolterでAF 0例・監視は24時間Holter×4回のみ。「1例0.30%のみ再発」は成功率データとして使えず、併施 Cox-maze IV あるいは少なくとも PVI＋LAA閉鎖という現行標準を置き換える根拠には全くならない。
  6. **症例選択**：LA径 3.6±0.6 cm と小さく発作性のみ＝左房拡大例・持続性AFに外挿できない（そうした症例こそ Cox-maze IV の適応）。位置づけとしては POAF 予防や、maze に踏み切れない併施症例の low-burden AF への低侵襲アドオンという**仮説段階**。

---

## 横断比較表

### 表1. エネルギー源別の透壁性・焼灼時間・周囲組織安全性（★リズム判定手段の列に注目）

| 論文 | 対象・N | エネルギー源 | 焼灼時間（1 lesion / 1 set） | 透壁性（分母つき） | 周囲組織の安全性 | ★リズム判定手段と頻度 | 「成功」の実体 |
|---|---|---|---|---|---|---|---|
| Baudo 2025 (PMID 39674689) | ヒト 8,293例／60研究 | BRF / Cryo / BRF+Cryo | 記載なし | 組織学的評価なし（臨床メタ解析） | 術後PPM BRF 1.06% (0.60–1.86) vs BRF+Cryo 3.91% (2.07–7.27), p=0.0025；術後CVA・30日死亡は3群差なし | **記載なし**（Holter/ECG/ILR いずれも不明、頻度も不明、"The paper's definition of freedom from AF was used for each included study"） | 4年 freedom from AF：Cryo 76.7%±2.2% / BRF 60.9%±2.2% / BRF+Cryo 66.3%±1.6%（log-rank p<0.0001、18/60編のKM再構成IPD） |
| Dunnington 2025 (PMID 39644967) | ブタ 12頭（nsPFA 6 / RF 6、1:1 RCT） | nsPFA vs bipolar RF | nsPFA **1.25秒/箇所（SD 0）** vs RF 28.6±16.7秒；7 lesion 計 **8.75秒 vs 200.5±24秒, P<.01** | nsPFA 全 lesion 透壁、**lesion depth＝tissue thickness（回帰の傾き1.0、0–20mm）** | **横隔神経麻痺なし（35日生存10頭の左右＝20神経、両群）**、食道内腔温上昇 <1℃（両群）だが RF の1頭に食道粘膜下線維化＋中等度炎症；device-related SAE nsPFA 0/6頭 vs RF 1/6頭(16.7%)＝LV穿孔死、RF で心内血栓2＋腎梗塞1 | **pacing による exit block のみ**（120 PPM, 3.0–10.5 V）、焼灼前／直後／35日の3回。**Holter・ILR 一切なし** | 35日 exit block **30/30部位 (100%)、両群とも** |
| Yi 2026 (PMID 41005435) | ブタ 9頭（解析7心、単群） | nsPFA（CellFX Parallel Clamp、最大15 kV） | 1回 2.5秒、**box は 2×2.5秒＝5秒**（自験 EnCompass RF 72秒との対比） | **切片 251/252 = 99.6%**、**lesion 32/33 = 97%**、box は **59/59切片 = 100%**、最大深度 17.5mm | 冠動脈 ablated vs 非ablated で neointima p=.25 / inflammation p=.66 / intimal thickness p=.27 / collagen p=.32 / elastin p=.25（いずれも N=8–9 vs 8–9）、血栓0；弁逆流 TR p=.78 (N=6) / MR p=.67 (N=5)。**ただし経弁的焼灼で 2/9頭(22%)が通電1秒以内の難治性VF死** | **pacing exit block（RAA/LAA/左PV）を焼灼前・直後・30日の3回＋心エコー2時点のみ。Holter・ILR 一切なし** | 30日 exit block **16/17部位 = 94.1%**（RAA 5/6・LAA 6/6・PV 5/5）；焼灼直後 21/21 = 100% |
| Serra 2023 (PMID 37920983) | ミニブタ 14頭・105 ablations（単群） | nsPFA（300 ns × 18発、6 Hz、10–12 kV） | 実質数秒（18発 @ 6 Hz） | **315/315 cross-sections = 100%**（6週 n=6・6ヶ月 n=8 とも）、6ヶ月 lesion depth 4.26±1.54 mm | 周辺臓器の組織学的評価は**記載なし**（食道・冠動脈・横隔神経の評価なし）。血管壁平滑筋は intact。lesion 幅は電極幅＋約1mm（3mm→4.02±1.67、6mm→6.90±1.41 mm） | **一切なし（記載なし）。伝導ブロックの機能的EP検証も未実施**（"functional electrophysiological testing of the lesions was not performed"） | 組織学的透壁性のみ。残存心内膜下組織は全例 SMA陽性平滑筋で connexin-43 陰性＝非伝導と**推定** |
| Musikantow 2024 (PMID 39066781) | ヒト 12例（単群、CABG 10 / AVR 2） | PFA（1,000 V、100 µs、5 GP に計60発）＝**除神経、lesion set ではない** | 記載なし | 透壁性評価なし（GP ターゲット） | デバイス関連有害事象 **0/12例** | **24時間Holter のみ、術前1回＋術後30日/3/6/12か月の計4回＝12か月で合計96時間** | AF再発 **1/12例 (8.3%)**、burden 0.30%（ただし**ベースラインHolterで12例全例 AF 陰性**＝天井効果） |

### 表2. nsPFA 3研究の設計上の強度（何がどこまで示され、何が示されていないか）

| 検証項目 | Serra 2023 | Dunnington 2025 | Yi 2026 |
|---|---|---|---|
| 対照群 | なし（単群） | **あり（bipolar RF、1:1 randomized、GLP、盲検病理）** | なし（同一個体内の自己対照のみ） |
| 生存期間 | 6週 / **6ヶ月** | 35±5日 | 26±7日（30日評価） |
| 拍動心（beating heart）での lesion 作成 | 記載なし（開胸下、心耳・purse string） | 記載なし（開胸下、purse string） | **あり（心房切開なしの心外膜 box）** |
| 電気的ブロックの検証 | **なし** | あり（pacing exit block、35日 30/30） | あり（pacing exit block、30日 16/17） |
| 食道・横隔神経の評価 | **なし** | **あり**（食道温 <1℃、横隔神経麻痺 0／生存10頭の左右20神経） | 記載なし（冠動脈・弁のみ評価） |
| 冠動脈の評価 | 血管壁平滑筋 intact（記述のみ） | 記載なし | **あり（盲検0–4スケール、全項目 p>0.2）** |
| 弁近傍・弁輪部 lesion | 未検証（部位＝心耳・左房のみ） | **未検証と著者明記**（"not designed to answer this question"） | **surrogate として検証→2/9頭 VF死** |
| ヒトでの AF free 生存 | 未検証 | 未検証（"We now await the results of in-human trials"） | 未検証 |
| 企業COI | Pulse Biosciences 助成＋責任著者が株式保有 | Pulse Biosciences 資金、著者7名中6名が株式/SO保有、3名は同社所属 | Pulse Biosciences 資金、Zemlin 氏が株式保有 |

### 表3. カテーテルAF ablation RCT の知見を「外科の box lesion / 線状焼灼」にどう翻訳するか

> 本セクションはカテーテル論文を1編も含まないが、S5 の論点（後壁隔離の追加価値、線状焼灼の透壁性・durability）はカテーテル領域の RCT が先行しているため、外科側の解釈に翻訳して整理しておく。**以下の CAPLA/PROMPT-AF/Marshall-Plan 等の数値は本セクション5編の一次資料には含まれず、S3/S4 のノートから引くこと。**

| カテーテル側の論点 | 外科への翻訳（本セクション5編から言えること） |
|---|---|
| PVI に後壁隔離（posterior wall isolation）を足しても持続性AFの再発を減らせなかった（CAPLA 等） | カテーテルの後壁隔離は **durable でなかった可能性**が常につきまとう。外科の box lesion は Yi 2026 で **59/59切片 (100%) 透壁・30日 PV exit block 5/5** と、少なくとも急性〜亜急性の完全性が桁違い。「後壁隔離は無効」という結論をそのまま外科に持ち込むのは、**lesion の完成度が別物**という理由で成立しない。逆に言えば、外科側は「うちの box は本当に透壁か」を示さない限り同じ土俵に乗れない。 |
| 線状焼灼（mitral isthmus / Marshall vein 併用等）の追加価値と、不完全 line による医原性 AT/AFL | Baudo 2025 が指摘する **bipolar clamp の jaw 先端が僧帽弁輪・三尖弁輪に届かない**という構造問題（Castellá JTCVS 2008、Varzaly ICVTS 2019 の二次引用）は、カテーテルの「不完全 mitral line が AT を生む」問題と同型。外科の解は cryo による補完であり、nsPFA クランプは**現時点でこの部分を解決していない**（Dunnington は未検証、Yi は surrogate で 22% VF死）。 |
| PFA の tissue selectivity（食道・横隔神経の温存） | 外科でも同方向のデータ：Dunnington で横隔神経麻痺 0（生存10頭の左右20神経）、食道温上昇 <1℃（ただし**RF でも <1℃なのに食道組織障害が出た**＝温度モニタリングは安全性の担保にならない）。Serra で血管壁平滑筋 intact、Yi で冠動脈の全病理項目が有意差なし。**外科クランプでも PFA の選択性は再現される。** |
| PFA 後の冠攣縮・VF | カテーテル領域で CTI・右下PV 近傍の PFA で冠攣縮が報告されている（Yi 2026 が二次引用）。外科でも **mitral isthmus line＝回旋枝・冠静脈洞の直上、CTI line＝右冠動脈近傍**であり、Yi の 2/9頭 VF死は同じ機序が外科 lesion set でも起こることを示唆。**外科でも「冠動脈の上は焼かない」原則が必要。** |

---

## 議論の対立点・未解決事項

1. **「Cryo は BRF より優れる」（Baudo ら, Brescia）vs 「エネルギー源より lesion set 完遂度と透壁性」（Damiano/Zemlin ら, Washington University; Ad ら）**
   - Baudo らは 8,293例のメタ解析で Cryo 優位（4年 76.7%±2.2% vs 60.9%±2.2%、log-rank p<0.0001）と主張。しかし同論文は**リズム判定手段を一切記載・統一しておらず**、決定的な4年 BRF は 2編78例（95% CI 20.40–81.69）。
   - 一方 Washington University 系（Yi 2026、Serra 2023）と Ad ら（Dunnington 2025）は、エネルギー源の議論を「透壁性が確保できるか／どれだけ速く確保できるか」という工学的問題に置き換えており、**RF の弱点は熱源であることではなく jaw 先端の接触圧と組織厚依存性にある**という立場。Dunnington の RF 群 lesion 幅の SD が大きい（LV 17.9±5.8 vs nsPFA 7.6±1.7 mm）ことがこの主張を支持する。
   - **決着していない。** ただし両陣営は「僧帽弁輪・冠静脈洞・三尖弁輪の line はクランプ単独では不十分」という点では一致しており、実務上の帰結（cryo で補完する）は共通。
   - なお Baudo 論文の COI（S.B. が AtriCure＝bipolar RF クランプの主要メーカーのコンサルタント）と、nsPFA 3編の COI（全編 Pulse Biosciences 資金・株式保有）は**互いに逆方向**であり、どちらの結論も企業利益と整合する点に注意が必要。

2. **「nsPFA は弁輪部・isthmus に使えるか」——同じ Pulse Biosciences デバイスをめぐる3編内での不一致**
   - Dunnington 2025（Ad ら）：弁輪部 lesion の可否は **"The present study was not designed to answer this question"** と明示的に回避し、cryo 併用が必要な領域と位置づけ。
   - Yi 2026（Damiano/Zemlin ら）：あえて transvalvular（surrogate）で検証し、**9頭中2頭(22%)が通電1秒以内の難治性VFで死亡**、"ablation over coronary arteries should not be performed" と結論。
   - Serra 2023（Zemlin ら）：そもそも心耳・左房の一部しか焼いておらず、**僧帽弁輪-冠静脈洞・右房峡部を評価していない**。
   - → 同一技術に対して「未検証（Ad）」「やってみたら致死的（Damiano/Zemlin）」という温度差がある。**外科レビューとしては Yi の VF シグナルを最上位に置くべき**（唯一実際に試した報告であるため）。

3. **透壁性 ≠ 伝導ブロック、伝導ブロック ≠ AF free**
   - Serra 2023 は透壁 315/315切片(100%) を示しながら **EP検証を行っておらず**、残存平滑筋の非伝導性は connexin-43 染色からの**推定**にとどまる。
   - Yi 2026 は逆に、**組織学的に非透壁だった RAA lesion でも30日 exit block は成立**していた例を報告し、両者が一致しないことを自ら明記。
   - そして nsPFA 3編のいずれも **AF モデルではなく、Holter/ILR によるリズム評価をしていない**。「透壁 100%」から「AF free 90%」への飛躍は、本セクションのどの論文もまだ埋めていない。
   - **未解決**：ヒトの線維化・拡大した心房での durability と、それが臨床的 AF free に翻訳されるか。in-human trial 待ち。

4. **リズム判定手段の非対称性が「見かけの成績差」をどこまで作っているか**
   - Baudo（ヒト、モニタリング**記載なし**）: 4年 freedom from AF 76.7%
   - Musikantow（ヒト、**24時間Holter×4回＝96時間/12か月**）: 再発 1/12例、burden 0.30%
   - nsPFA 3編（動物、**pacing exit block のみ、計2–3時点**）: exit block 94–100%
   - → **数値が良い研究ほどモニタリングが疎い**という関係が本セクション内で完全に成立している。統合レビューでこれらを並べるときは、必ず判定手段を併記すること。

5. **GP除神経（Musikantow）を Cox-maze の文脈にどう置くか**
   - 著者らは「PFA なら GP 除神経が12か月持続する」（rMSSD P=0.01、HF power P=0.05）と主張するが、AERP は非有意（+6.9%±19.6%、P=0.38）＝**術中に完遂を確認する指標がない**。
   - ベースライン Holter で 12例全例 AF 陰性という集団に対する「再発1例」は efficacy の根拠にならない。
   - **未解決**：maze lesion set に GP-PFA を追加したときの上乗せ効果を RCT で見る必要がある。現状は POAF 予防や low-burden AF への低侵襲アドオンという仮説段階。

---

## 統合レビューで使える一文（引用可能な形）

1. 両心房 Cox-maze を対象とした60研究8,293例（Cryo 3,364例／bipolar RF 1,937例／併用 2,992例）のメタ解析では、再構成IPDによる4年 freedom from AF が Cryo 76.7%±2.2%、BRF 60.9%±2.2%、BRF+Cryo 66.3%±1.6%（log-rank p<0.0001）と報告されたが、同解析は各原著の成功定義をそのまま採用しており（"The paper's definition of freedom from AF was used for each included study"）、blanking period・>30秒閾値・AAD の扱い・**リズムモニタリング手段と頻度はいずれも本文に記載がない**ため、絶対値の他研究との横並び比較には使えない（Baudo, Heart Lung Circ 2025;34:25-33）。

2. 同メタ解析で AF 再発の唯一の多変量独立予測因子は平均左房径（OR 1.04/mm, 95% CI 1.01–1.08, p=0.0159）であり、bipolar RF サブグループでは左心耳閉鎖が保護因子であった（OR 0.92, 95% CI 0.88–0.97, p=0.0004）——左心耳処置を Cox-maze IV に必ず組み込む根拠を、塞栓予防に加えてリズム転帰の側からも補強する所見である。

3. 同メタ解析で Cryo 優位を最も強く示す4年時点のデータは、BRF 群がわずか2編78例（AF発生率 51.39%, 95% CI 20.40–81.69, I²=87.5%, leave-one-out 変動 31–77%）に依存しており、メタ回帰の OR 12.04（95% CI 2.15–67.6, p=0.0047）も同様に不安定である。したがって「Cryo が BRF より優れる」は因果的結論ではなく、前向き RCT を要する仮説である。

4. 慢性ブタモデルで nsPFA クランプと bipolar RF クランプを1:1にランダム化した GLP 試験（各群6頭、7 lesion/頭）では、nsPFA は組織厚に依存せず1回1.25秒（7 lesion 合計 8.75秒）で全 lesion を透壁化し（lesion depth と tissue thickness の回帰の傾き＝1.0）、RF の合計 200.5±24秒（P<.01）と比べ焼灼時間を約23分の1に短縮した。35日時点の exit block は SVC・RAA・左PV の 30/30部位（100%）で両群とも維持され、横隔神経麻痺も生存10頭の左右20神経すべてで認めなかった（Dunnington, J Thorac Cardiovasc Surg 2025;170:1069-78）。

5. 同試験では device-related SAE が nsPFA 0%（0/6頭）に対し RF 16.7%（1/6頭＝術後24日の左室焼灼部 erosion による穿孔死）、盲検組織病理での有害所見が nsPFA 0% vs RF 7.1% であり、さらに RF 群では焼灼部位 3/42（7%）に erosion 関連の有害転帰、心内血栓2例と腎梗塞1例、食道の粘膜下線維化＋中等度炎症が生じた。**注目すべきは食道内腔温の上昇が両群とも 1℃未満であったにもかかわらず RF 群でのみ食道組織障害が出た点で、術中温度モニタリングは熱傷の非発生を担保しない。**

6. 拍動心ブタ9頭を用いた feasibility 試験では、nsPFA クランプにより**心房切開なしの心外膜アプローチ・クランプ1回設置・通電計5秒（2×2.5秒）**で左房後壁＋肺静脈 box が作成でき、box lesion は 59/59切片（100%）が透壁、30日の肺静脈 exit block は 5/5部位であった。全体では切片 251/252（99.6%）・lesion 32/33（97%）が透壁で、最大焼灼深度は17.5 mm に達した（Yi, J Thorac Cardiovasc Surg 2026;171:632-9）。

7. 一方その同じ試験で、**僧帽弁輪・三尖弁輪を跨ぐ経弁的（isthmus 代用）焼灼により9頭中2頭（22%）が通電1秒以内に難治性心室細動を発症し、8–10回の除細動に不応で死亡した**。著者らは冠攣縮を疑い "Until this work is done, ablation over coronary arteries should not be performed" と明記しており、回旋枝・冠静脈洞の直上を走る mitral isthmus line と右冠動脈近傍の cavotricuspid isthmus line については、現時点でも endocardial cryo が標準であることを本研究は覆さない。

8. Yucatan ミニブタ14頭・105 ablation（バイポーラクランプ、300 ns × 18発、6 Hz、10–12 kV）では、術後6週および6ヶ月の時点で **315/315 cross-sections（100%）が透壁**を維持し、lesion 幅は電極幅とほぼ一致した（3mm 電極で 4.02±1.67 mm、6mm 電極で 6.90±1.41 mm）。心内膜下に残存した生存組織は全例 smooth muscle actin 陽性の平滑筋であり connexin-43 陰性であったが、**伝導ブロックの機能的電気生理学的検証は行われていない**（Serra, Circ Arrhythm Electrophysiol 2023;16:e012300）。

9. ヒトで外科的に PFA を用いた唯一の前向き報告は、CABG（n=10）または AVR（n=2）に併施した心外膜神経節叢への pulsed field ablation 12例の単群試験（NEURAL-AF-2, NCT05426759）で、デバイス関連有害事象なく施行でき、副交感神経指標の rMSSD（59±18→42±15 ms, P=0.01）と HF power（321±189→198±153 ms², P=0.05）の低下が12か月持続した。ただし心房有効不応期の変化は非有意（+6.9%±19.6%, P=0.38）で、リズム監視は24時間Holter 4回（12か月で計96時間）のみ、しかもベースライン Holter で12例全例が AF 陰性であったため、「再発1例（burden 0.30%）」は AF 抑制効果の根拠にはならない（Musikantow, JACC Clin Electrophysiol 2024;10:2097-9）。

10. 本セクションの5編を通じて、**成績数値が良好な研究ほどリズム判定が疎である**という関係が一貫している（Baudo：判定手段の記載なしで4年 freedom from AF 76.7%／Musikantow：24時間Holter 4回で再発1/12例／nsPFA 3編：pacing による exit block を2–3時点のみで 94–100%）。nsPFA の前臨床データはいずれも「透壁性」と「exit block」までしか示しておらず、**線維化した拡大心房での durability と臨床的 AF free 生存は本ノート時点で未検証**である。
