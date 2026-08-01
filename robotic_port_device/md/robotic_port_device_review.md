# ロボット心臓手術用「止血機能つき・バルーン固定ポート」構想
## 背景・先行技術・新規性の検討

*作成: 2026-08-01 ／ 対象: ロボット支援心臓手術（僧帽弁形成・ASD・MAZE 等）の胸壁ポート*
*改訂: 2026-08-01（敵対的検証フェーズの所見を反映。§7 の特許・事業性は判定が反転した）*

> **表記ルール**：〔一次確認済〕＝本調査で PMID/DOI/特許請求項/FDA 510(k)/SEC 提出書類の原文を直接当たって確認したもの。〔要一次確認〕＝並列調査エージェントの報告で独立の裏取りが取れていないもの。〔未確認〕＝調べたが確認できなかったもの。後二者は必ず自分で確認してから対外資料に使うこと。

---

## 0. 結論（先に書く）

| 構想要素 | 判定 | 根拠 |
|---|---|---|
| **問題設定**：ポート／胸壁刺入部からの出血が臨床的に重要 | **正しい。ただし決定的な数字はロボットではなく非ロボット MICS から来ている** | 右小開胸 MIMVS 151例で出血再開胸6例の内訳が **肋間動脈4・心筋保護カニュレーション部位1・左房縫合線1**（Pojar 2019）。埼玉医大の MICS 僧帽弁形成98例では**再開胸3例が全例 chest wall bleeding**（Aizawa 2026）。VATS の RCT では **ポート創面出血で手術が中断されるのが対照群の 51.8%**（Shimizu/Tanaka 2020） |
| **① 先端バルーンで migration 予防＋タンポナーデ止血** | **新規性は無い。日本市場でも既に売られている** | **株式会社八光「E・ZバルーンⅡ」（認証番号 229ADBZX00064000、2017年10月発売）が公式に「トロッカーの逸脱を防止」「止血圧迫効果」と謳っている**。Applied Medical の Kii も英日公式で「切開部が圧迫されることでポート部位の出血を低減します」。Applied Medical は **[US 8,142,467](https://www.freepatentsonline.com/8142467.html)「Tamponade trocar device and method」**（2008出願）を保有。臨床応用も 2025年に報告済（Balkhy ら）— **ただしこの報告は無調整の前後比較で因果は未証明**（§2.3） |
| **② 止血材をポート外周にあらかじめ装着** | **製品・登録特許としては白地。ただし公開文献は既にあり、材料側に強い反対材料がある** | **複数DB・複数検索式で「止血材を外周に事前装着したトロカール」の製品も登録クレームも 0件**（§3.2）。しかし ⑴神戸大が創縁保護材に酸化再生セルロース（ORC）リングを組み込む手法を報告（2016）→ **RCT n=108**（2020）で検証済、⑵**WO 2019/122487 が「バルーン＋酸化セルロース」を公開済（ただし失効）**、⑶ **[US 7,018,392](https://www.freepatentsonline.com/7018392.html)（2001出願・2006登録・満了）が「バルーンの外周を止血材で覆う」構造をクレーム済** 。⑵⑶は新規性・進歩性の壁になる |
| **③ 電メ切開による熱傷創の解決** | **主張として弱い。前面に出すべきでない** | 皮膚切開線に関する限り、Cochrane・複数のメタ解析はいずれも「電メは同等ないし優位」。ただし **「ポート孔を全層焼き広げる」操作を評価した研究は世界的に皆無** なので、否定ではなく**未検証** |

### 残る新規性は「組合せ」だけ

要素ごとに分解すると次のとおり。**単独では全て既知であり、特許性が残るのは掛け算の部分だけである。**

| 要素 | 判定 |
|---|---|
| バルーンで体壁内側に引っ掛けて逸脱防止＋圧迫止血 | **新規性なし**（八光 E・ZバルーンⅡ、Applied Medical Kii、US 8,142,467、Balkhy の臨床実装） |
| 止血材をアクセスデバイス外周に事前装着 | **製品ゼロ・登録クレームゼロ＝白地**。ただし WO 2019/122487（失効）と US 7,018,392（満了）が公開文献として存在 |
| 胸腔／肋間専用 | **バルーン式の胸腔専用ポートは製品として不存在**。ただし機械式の肋間アンカーは US 5,776,110（1996）が公知 |
| **上記3つの掛け算 ＋ ロボットアーム荷重下での保持** | **ここに特許性が残る** |

そのうえで、実務上の勝ち筋は次の3点：

1. **全身ヘパリン化＋体外循環という条件での設計**。ORC リング RCT も Applied Medical のタンポナーデトロカールも、土俵は非ヘパリン下の一般外科／呼吸器外科である
2. **「バルーンを抜いた後どうするか」への解**。Balkhy らのバルーンタンポナーデは抜けば終わりで、重度凝固障害例では ICU まで留置している。**抜去時の再出血は、頸部外傷のバルーンタンポナーデでも再探索の主因として報告されている**（§9）。抜去と同時に刺入路へ止血材を残置する構造（tract sealant の発想）は、確認できた範囲のどの製品もカバーしていない
3. **肋間という特殊な解剖への最適化**。腹壁ではない。肋骨に挟まれ、肋間神経が並走し、呼吸で動く

### 事業面 — ユーザーの懸念は事実として反証された

「ロボットのポートはアームと連結するから Intuitive に特許で囲われている」という懸念について、検証の結果は次のとおり。**§7 で初版の判定を撤回する。**

1. **最も価値の高いポートは、そもそもアームに繋がっていない。** EACTS のロボット僧帽弁推奨（Palmen ら）の逐語：「**the working port is created in the third or fourth intercostal space by performing a 1.5- to 4-cm long skin incision. A soft-tissue retractor is placed…**」。最も径が大きく（1.5〜4 cm）、最も肋間の剥離が大きく、したがって最も出血しやすい working port は**ロボットアームに一切ドッキングしない**。Intuitive のカニューラ特許はいずれも「アーム連結界面（bowl＋tube＋attachment portion）」を要件とするため、**この部位には一切かからない**〔一次確認済〕
2. **第三者製の da Vinci 用アクセサリは実在し、FDA クリアランスを取得している。** ConMed **AirSeal® dV Solution（AirSeal Cannula Cap）[K211104](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K211104), 2021-08-19** は Intuitive 純正カニューラに被せる第三者製キャップで、**胸腔適応込み**。さらにロボットアームに直結する器具ですら Restore Robotics（[K252926](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K252926), 2026-03-26）・Iconocare Health（[K210478](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K210478) / [K242610](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K242610)）・Rebotix（[K241872](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K241872) ほか）がクリアランス済み〔一次確認済：openFDA 510(k) API〕
3. **反トラスト訴訟は「Intuitive 勝訴で確定」ではない。** SIS 事件は 2025-01-28 に一審で Intuitive 勝訴だが第9巡回区に控訴中（2026-06-25 口頭弁論済・判断待ち）、Restore Robotics Repairs 事件も第11巡回区で係属中〔一次確認済：Intuitive 10-Q〕。**そしてこれらの争点はいずれも EndoWrist の修理・再製造役務であって、アクセサリの新規製造ではない。本構想の可否とは論理的に無関係である**
4. **真の FTO 障壁は Intuitive ではなく Applied Medical のバルーントロカール特許群**である（§2.2）
5. hinotori は**アームとトロカールがドッキングしない**設計なので、そもそもポートが自由（§8）

---

## 1. 背景 — ポート／胸壁刺入部の出血はどれくらい問題なのか

### 1.1 心臓手術全体での「出血再開胸」の位置づけ〔一次確認済〕

成人心臓手術後の再開胸（出血/タンポナーデ）のメタ解析（Biancari F ら, J Cardiothorac Vasc Anesth 2018;32(4):1618-24, [PMID 29338997](https://pubmed.ncbi.nlm.nih.gov/29338997/), 18研究 51,497例）：

- 再開胸率 **4.6%**（95%CI 3.9–5.2）
- 再開胸例の院内/30日死亡 **9.3% vs 2.3%**、リスク比 **3.30**（95%CI 2.52–4.32）
- 外科的出血源が同定できたのは **65.7%**
- 出血部位の内訳：グラフト本体 20.2%、胸骨 17.0%、血管縫合部 12.5%、内胸動脈採取床 13.0%、吻合部 9.9%

> **⚠ 初版の誤りを訂正**：初版はここから「胸骨17.0%＋IMA採取床13.0%＝胸壁由来30%であり、MICS ではこれが肋間ポート孔に置き換わる」と外挿したが、**この外挿は成立しない**。胸骨骨髄面と IMA 剥離床は**胸骨切開に固有の出血源で、MICS では消滅する**。同じ論理を使えば「胸壁アプローチにすると出血は減る」という逆の結論が出るし、実際 RCT のメタ解析（Spadini 2026, [PMID 41592916](https://pubmed.ncbi.nlm.nih.gov/41592916/)、8試験1,248例、ロボット除外）では MIMVS の再開胸が **RR 0.24（95%CI 0.06–0.92）** と 1/4 に減っている。この論文は「再開胸は死亡リスクを3.3倍にする重大イベントである」という一般論の根拠としてのみ使うべきである。

### 1.2 ロボットの出血再開胸は本当に多いのか — 証拠は割れている〔一次確認済〕

| 研究 | データ | 結果 |
|---|---|---|
| Santos K ら, Asian Cardiovasc Thorac Ann 2026;34(1):57-66, [PMID 41212734](https://pubmed.ncbi.nlm.nih.gov/41212734/) | 傾向スコアマッチ研究のみのメタ解析、8研究3,352例 | ロボット vs 従来型 MICS で **出血再開胸 OR 1.86（95%CI 1.1–3.2, p=0.02）**、胸骨切開への移行 OR 2.9、CPB +21.8分、在院 −1.8日 |
| **Mori M ら, Ann Thorac Surg 2024;117(1):96-104, [PMID 37595861](https://pubmed.ncbi.nlm.nih.gov/37595861/)** | **STS 全米データベース 2015-2021、変性 MR 僧帽弁形成 61,322例。ロボット vs 小開胸 5,540ペア／ロボット vs 胸骨切開 6,962ペアの PSM** | **死亡率・罹病率に有意差なし。むしろロボットで開胸転換が少ない（1.2% vs 3.1%／1.0% vs 3.7%）** |
| Eranki A ら, Ann Cardiothorac Surg 2026 | ロボット変性僧帽弁形成の SR/MA、11研究 | 出血再手術 **2.34%**（95%CI 1.41–3.84、62/3,131例） |
| Fatehi Hassanabad A ら, Innovations 2022;17(6) | ロボット vs 胸骨切開／vs 右小開胸の SR/MA | 出血再手術に**有意差なし** |

**読み方**：Santos の OR 1.86 は 95%CI 下限が 1.1 と 1 に近く、母集団も 3,352例。一方 STS の 61,322例・PSM では差が出ていない。**「ロボットにすると出血再開胸が増える」と単独で断ずるには弱く、両者を併記すべきである。** ニーズの主張は疫学の差ではなく、**出血源の内訳**（§1.3）に置いたほうが強い。

参考：Cleveland Clinic（Cullen P ら, MMCTS 2025）は再開胸率が **2.5% → 1.3%** に低下、「ほぼ常に右胸から対処できる」＝熟練施設では制御可能でもある。

### 1.3 出血源の内訳 — 3件の一次データが存在する〔一次確認済〕

初版では「MICS/ロボットの出血再開胸の出血源内訳を報告した論文は無い」と書いたが、**これは誤りだった**。以下は全文で逐語確認した。

| 研究 | 対象 | 逐語 |
|---|---|---|
| **Pojar M ら, Ann Thorac Cardiovasc Surg 2019;25(1):18-25, [PMID 30232298](https://pubmed.ncbi.nlm.nih.gov/30232298/) / PMC6388298** | 右小開胸 MIMVS 連続151例（チェコ） | 「Re-exploration was performed in six patients (4.0%) as a result of bleeding. In all cases, the revision was possible through the same minithoracotomy… **Bleeding sources included intercostal artery in four**, cardioplegic cannulation site in one and left atrial suture line in one.」→ **再開胸6例中4例（67%）が肋間動脈** |
| **Aizawa H ら, Ann Thorac Cardiovasc Surg 2026;32(1):25-00208, [PMID 41730659](https://pubmed.ncbi.nlm.nih.gov/41730659/) / PMC12950296（埼玉医大国際医療センター）** | MICS 僧帽弁形成98例 vs 胸骨切開70例（2015-2024） | 「In the MIMVr group, complications included **postoperative chest wall bleeding requiring re-exploration (n = 3)**…」。表：Re-exploration for bleeding **3 (3%) vs 0 (0%)**, p=0.267 → **MICS 群の再開胸3例は全例が胸壁出血。日本の施設データ** |
| **Chen Y ら, J Cardiothorac Surg 2021;16(1):91, [PMID 33865420](https://pubmed.ncbi.nlm.nih.gov/33865420/) / PMC8052820** | 完全内視鏡下僧帽弁手術188例 | 再開胸1例＝**創部（incision site）出血** |

**合算すると 437例中の再開胸10例のうち8例（80%）が胸壁／肋間／創部由来。** ただし次の限界を必ず併記すること：

- **3件とも非ロボットの小開胸／内視鏡**であり、**ロボットの 8mm ポート孔に限った内訳データは依然としてゼロ**
- 分子が計10例であり、点推定として使えない（信頼区間が極端に広い）
- 後ろ向き・単施設・報告バイアス（「肋間から出た」と書く施設は書く）

→ **これが構想のニーズ根拠として最も強い材料である。同時に、自施設で前向きに「出血源」を記録することが最初の研究テーマになる理由でもある。**

### 1.4 ポート創面出血は「手術を中断させる」〔一次確認済〕

VATS の単施設無作為化試験（Shimizu N, Tanaka Y ら, Interact Cardiovasc Thorac Surg 2020;30(3):346-52, [PMID 31747012](https://pubmed.ncbi.nlm.nih.gov/31747012/)、n=108、ORC群54 / 非ORC群54）：

| アウトカム | ORC群 | 非ORC群 | p |
|---|---|---|---|
| **ポート創面からの血液滲出による手術の中断** | **11.1%** | **51.8%** | <0.001 |
| 閉創時に創面の止血処置を要した | 44.4% | 72.2% | 0.003 |
| 手術時間（分） | 149.3 | 168.8 | 0.083 |

**非ORC群の 51.8% で「ポート創面から垂れる血で手術が中断された」。** ただしこれは**ヘパリン化していない呼吸器外科**の数字である。心臓外科で同じ指標を測った報告は無い。

### 1.5 心臓外科での止血材使用の先行 — Kiani/Poston 2012〔要一次確認：本文未入手〕

**Kiani S, Poston R ら. "Managing port-site bleeding during less invasive coronary artery bypass grafting." Heart Surg Forum 2012 Oct;15(5):E272-6, [PMID 23092664](https://pubmed.ncbi.nlm.nih.gov/23092664/)**

- ロボット支援 CABG のポート孔に**流動性止血材を注入**するプロトコル
- **輸血率 40.8% → 24.2%**
- ⚠ **有意差が出たのは輸血率のみで、再開胸率・胸腔ドレーン量・在院日数には有意差なし**〔要一次確認〕。**「止血材で再開胸が減る」根拠として引用してはならない**
- 著者の結論：「ポート穿刺部からの検出されない出血は、過小評価された morbidity の原因である」

### 1.6 ロボット心臓手術に特異的な増悪因子

| 因子 | 内容 | 出典 |
|---|---|---|
| 全身ヘパリン化・体外循環 | ACT 400秒超が数時間。血小板機能低下・希釈性凝固障害 | 自明（一次文献での定量なし） |
| 触覚フィードバックの欠如 | 軽微な血管損傷が術中に気づかれず、遅発性のポート部位出血になる | Kawata Y ら, Cureus 2026, [PMID 41913831](https://pubmed.ncbi.nlm.nih.gov/41913831/)（hinotori 使用の婦人科手術で POD5 に 9cm 皮下血腫、下腹壁動脈穿通枝から）〔一次確認済〕 |
| 単肺換気＋CO2 送気 | 陽圧・虚脱肺の下では胸壁からの静脈性出血が見えにくく、肺再膨張・陽圧解除後に顕在化 | 機序としては妥当だが**一次文献での直接記載は見つからなかった**〔未確認〕 |
| ロボットアームの可動 | ポート創に持続的な機械的ストレス。Intuitive 自身が「カニューラの体壁保持」を特許化している（§7） | US 10485582 / US 12491005〔一次確認済〕 |
| **日本人の小柄な体格** | 日本の多施設前向き研究で、RATS はポート数 5.0・損傷肋間数 2.9 で VATS に対し POD30 の疼痛の非劣性を証明できず、**身長が低いほどポート痛が残る（OR 0.907/cm）** | Tokuishi ら 2024, Lung Cancer, [PMID 39340899](https://pubmed.ncbi.nlm.nih.gov/39340899/)〔要一次確認〕 |
| 肋間動脈の走行変異 | 後方ほど肋骨下縁から離れて肋間中央を走り損傷リスクが上がる。超音波でスクリーニング可能 | [PMID 23521021](https://pubmed.ncbi.nlm.nih.gov/23521021/), [40944085](https://pubmed.ncbi.nlm.nih.gov/40944085/)〔一次確認済〕 |

### 1.7 ただし競合する出血源がある — 鼠径／大腿〔要一次確認〕

MICS のアクセス関連合併症の主役は胸壁ではなく**大腿カニュレーション部位**である可能性がある。

- Sromicki J ら, Interdiscip Cardiovasc Thorac Surg 2026;41(7):ivag185, [PMID 42386682](https://pubmed.ncbi.nlm.nih.gov/42386682/) / PMC13390282（MICS 僧帽弁823例）：複合効率エンドポイントの差は主に access-site complication（大腿カニュレーション）で説明された
- Speziale ら 2026, [PMID 41960123](https://pubmed.ncbi.nlm.nih.gov/41960123/) / PMC13059993（MICS 僧帽弁140例）：**groin cannulation 関連合併症 11.3%（16/140）に対し出血再開胸 3.6%（5/140）**

→ **胸壁ポートだけを解決しても MICS のアクセス関連合併症の大半は残る。** 提案書ではこれを認めたうえで「それでも胸壁は解ける」と論じるほうが強い。

---

## 2. 先行技術A — バルーン付きトロカールは完全に枯れた技術である

### 2.1 商用製品 — 「逸脱防止＋圧迫止血」は既に製品の売り文句である〔一次確認済〕

| 製品 | メーカー | 公式に謳われている効能 |
|---|---|---|
| Blunt Tip Surgical Trocar | Origin Medsystems | [K924011](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K924011)（1993）＝ この分野の起源〔要一次確認〕 |
| **Kii® Balloon Blunt Tip** | **Applied Medical** | 英語公式：「**The retention disk and balloon compress the incision site, potentially reducing port-site bleeding.**」<br>日本語公式：「**切開部が圧迫されることで、ポート部位の出血を低減します**」〔一次確認済〕 |
| **E・ZバルーンⅡ** | **株式会社八光（国産）** | 認証番号 **229ADBZX00064000**、JMDN 37148002（単回使用トロカールスリーブ）、**2017年10月販売開始**。公式：「弾力性に優れたバルーンと可動ストッパーで腹壁を確実に固定でき、**トロッカーの逸脱を防止**します。バルーンと可動ストッパーで**止血圧迫効果**が得られ腹壁からの出血や損傷を抑えることができます。」規格 5–65mm シャープ／ブラント〔一次確認済〕 |
| VersaOne™ Optical Trocar with Fixation Balloon Cannula | Medtronic/Covidien | [K213818](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K213818)〔要一次確認〕 |
| SoftFix | Unimax | [K211577](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K211577)〔要一次確認〕 |
| ADAPT Balloon Open Access Port | Teleflex | 〔要一次確認〕 |

> **これが構想①にとって最も厳しい事実である。** 「バルーンで固定して逸脱を防ぎ、同時に圧迫で止血する」というコンセプトは、Applied Medical だけでなく **国産メーカー（八光）が9年前から同じ言葉で販売している**。**日本市場での新規性・進歩性をこの要素で主張することは不可能**である。
>
> 差別化できるとすれば「腹壁ではなく**肋間**」「**止血材の併載**」「ヘパリン化・体外循環下」の3点に限られる。

### 2.2 特許 — 障壁になるのは US 8,142,467 系だけ〔一次確認済〕

| 特許 | 名称 | 権利者 | 出願／登録 | 状態と射程 |
|---|---|---|---|---|
| **[US 8,142,467](https://www.freepatentsonline.com/8142467.html)** | **Tamponade trocar device and method** | **Applied Medical Resources** | 2008-04-21／2012-03-27 | **有効。これが本丸。** 明細書に「a trocar device that **significantly reduces or prevents bleeding at the trocar penetration site in the body wall**」「substantially eliminates bleeding at the trocar site」と明記。"tamponade" が57回出現。満了は概ね2028年見込〔要一次確認〕。継続 [US 8,834,505](https://www.freepatentsonline.com/8834505.html) / [US 8,951,277](https://www.freepatentsonline.com/8951277.html) |
| [US 8,287,503](https://www.freepatentsonline.com/8287503.html) | Balloon trocar | Applied Medical Resources | 2007-03-08／2012-10-16 | 有効（満了予定 2030-07-10〔要一次確認〕）。**ただし明細書に bleeding / hemostasis / tamponade / migration の語が1つも無く、目的は「切開部のシール」**。止血目的の権利範囲は及ばない〔要一次確認：エージェントの全文 grep 結果〕 |
| **[US 7,018,392](https://www.freepatentsonline.com/7018392.html)** | **Hemostatic system for body cavities** | **Arthrocare Corporation** | 2001-11-28／2006-03-28 | **満了済（Expired-Lifetime）。しかし「バルーンの外周を止血材で覆う」構造そのもののクレーム。** 要旨逐語「Bleeding is controlled … by inserting into the cavity **an expandable balloon which is covered by a hemostatic shroud**, expanding the balloon, and compressing the shroud against the site of bleeding.」請求項1「an insertable shaft … comprised of **a hemostatic shroud disposed around an inner component**」／請求項3「said inner component comprises **a balloon**」／請求項4「said balloon is **rolled around said central tube**」。適用は鼻腔・体腔（Rapid Rhino 型）で体壁ポートではないため**新規性は壊さないが、進歩性審査で最初に引かれる文献**〔一次確認済〕 |
| **[US 5,776,110](https://www.freepatentsonline.com/5776110.html)** | **Thoracic port** | **United States Surgical** | 1996-01-26／1998-07-07 | **満了済。肋間内側アンカリングの先行技術。** 要旨逐語「The thoracic port is inserted into the **intercostal space between two ribs** and turned to a locking position wherein the legs may bias the ribs … and the **wings abut the distal surface of the ribs to prevent inadvertent withdrawal of the port**.」バルーンではなく機械式ウィング〔要一次確認〕 |
| KR 10-2058617 B1 | Medical trocar and hemostatic system using the same | **ソウル大学校病院** | 2017-07-18／2019-12-26 | **Active、満了見込2037年。** ワイヤ操舵式フレキシブルトロカール＋体壁穿刺孔を通して出血部位を圧迫する「圧迫部」。構造は異なるが**「トロカール＋止血機能の一体化」の権利化が既に進行している**〔要一次確認〕 |
| [US 8,382,707](https://www.freepatentsonline.com/8382707.html) | 二段バルーン | Applied Medical Resources | — | 〔要一次確認〕 |
| [US 12,251,130](https://www.freepatentsonline.com/12251130.html) | Surgical access device having a balloon | Covidien | ／2025登録 | 〔要一次確認〕 |
| [US 5,147,316](https://www.freepatentsonline.com/5147316.html) | Laparoscopic trocar with self-locking port sleeve | — | 1990出願 | **2009満了＝自由に使える**〔要一次確認〕 |
| [US 7,235,064](https://www.freepatentsonline.com/7235064.html) | — | — | 優先1994 | **2014満了＝自由に使える**〔要一次確認〕 |

**含意**：

1. **FTO の主障壁は Intuitive ではなく Applied Medical、しかも US 8,142,467 系1本に絞られる。** US 8,287,503 は止血を目的としていないので射程外
2. **「バルーン＋止血材」の組合せ自体は 2001年出願・2006年登録の US 7,018,392 が既にクレームしている**（満了済）。新規性（体壁ポートでない）は壊れないが、**進歩性の壁になる**
3. **「肋間の内側に引っ掛けて抜けを防ぐ」着想も 1996年から公知**（US 5,776,110、機械式・満了済）
4. → **特許性が残るのは「肋間専用形状 ×止血材の事前装着 × ロボットアーム荷重下での保持」という組合せに絞られる**

### 2.3 臨床応用の先行報告と、その限界〔一次確認済〕

**Qi SS, Grady K, Kitahara H, Nisivaco S, Johnson B, Tsukioka Y, Balkhy HH. "Control of Port Site Bleeding With Liberal Use of Catheter Balloon Tamponade in Robotic Mitral Valve Surgery." Innovations (Phila) 2025. [doi:10.1177/15569845251365733,](https://doi.org/10.1177/15569845251365733,) [PMID 40913323](https://pubmed.ncbi.nlm.nih.gov/40913323/)**（シカゴ大 Balkhy グループ）

焼灼で止まらないポート部位出血に**バルーン付き coudé カテーテル**を当てるプロトコルの導入前（対照 n=127）／導入後（バルーン n=188）を比較。体外循環離脱中にバルーンを当て、通常はプロタミン投与後に抜去。重度凝固障害例では留置したまま ICU に上げる。

| アウトカム | バルーン群 | 対照群 | p |
|---|---|---|---|
| 出血による再手術 | **0%** | **4.7%** | 0.004 |
| ペースメーカー植込み | 0.5% | 3.9% | 0.04 |
| POD1 でのドレーン抜去 | 83% | 70% | 0.01 |
| 術中・術後輸血率、在院日数 | 有意差なし | | |

> **⚠ 初版はこれを「構想①の臨床的正しさをほぼ証明している」と評価したが、格下げする。** 検証で以下が判明した：
> - **無調整の前後比較（before-after）**。2016年からの6年間の学習曲線・術式変更と完全に交絡する
> - **決定的な内的妥当性の破綻：ペースメーカー植込みが 3.9% → 0.5%（P=0.04）と有意に低下している。** ポート孔のバルーンタンポナーデが房室ブロックを減らす生物学的機序は存在しない。この「起こり得ない差」が出ている以上、両群は介入以外の要因で系統的に異なると考えるのが自然で、再開胸 4.7% → 0% も同じ交絡で説明されうる
> - **輸血率も在院日数も同等**。ポート孔出血が再開胸の主因なら輸血も減るはずで、この不整合は因果鎖を弱める
> - **対照群の再開胸6例の出血源がポート孔だったかは抄録に一切書かれていない**（本文は購読制で未入手）
> - **Husam H. Balkhy は Intuitive Surgical の proctor**（COI 文に明記）
>
> → **「概念実証が済んでいる」ではなく「仮説生成レベルの前後比較」。** ユーザーにとっては追い風でも逆風でもなく、**新規デバイスの臨床試験を設計する余地がまだ大きい**ことを意味する。

### 2.4 心臓外科×肋間×バルーンの報告〔要一次確認〕

Tian ら（Front Cardiovasc Med 2025, [PMID 40495985](https://pubmed.ncbi.nlm.nih.gov/40495985/)）：右腋窩開胸による VSD 閉鎖後の**第6肋間刺入部からの出血**を、**10Fr Foley・バルーン5mL・胸壁への牽引固定のみ**で止め、再開胸を回避した。要精読。

---

## 3. 先行技術B — 止血材を組み込んだアクセスデバイスも既にある（日本発）

### 3.1 神戸大の ORC リング付き創縁保護材〔一次確認済〕

1. **Tanaka Y, Tane S, Hokka D, Ogawa H, Maniwa Y. Ann Thorac Surg 2016;101(2):786-8. [PMID 26777946](https://pubmed.ncbi.nlm.nih.gov/26777946/)** — 創縁保護材に ORC のリングを組み込む。「ORC リングは術中の創面出血を完全に止め、閉創前に創面の止血処置を要さなかった」
2. **Shimizu N, Tanaka Y ら. Interact Cardiovasc Thorac Surg 2020;30(3):346-52. [PMID 31747012](https://pubmed.ncbi.nlm.nih.gov/31747012/)** — 上記を単施設 RCT（n=108）で検証（§1.4）

**「止血材をあらかじめアクセスデバイスに装着しておく」という発想は、2016年に日本で報告され、2020年に RCT で有効性が示されている。** 材料はまさにユーザーが挙げた酸化セルロース系である。

### 3.2 構想を直撃する国際特許 — 実在するが、いずれも失効している〔要一次確認〕

| 出願 | 内容 | 法的地位 |
|---|---|---|
| **WO 2019/122487「DEVICE FOR HAEMOSTASIS OF AN INTRAPERITONEAL TROCAR ORIFICE」**（Servicio Andaluz de Salud） | 腹腔内トロカール孔の止血デバイス。遠位部に**2つの膨張式バルーン**を持つプローブ。WIPO PATENTSCOPE に実在を確認〔一次確認済〕。**請求項3で「バルーンおよび／またはプローブ遠位部に抗出血物質（好ましくは酸化セルロース）を含浸させる」**とされる〔要一次確認〕＝**構想①＋②の統合そのもの** | **Status: Ceased（失効）。各国移行なし。** 関連権利はスペイン実用新案 ES1203693Y / ES1204712Y のみ（スペイン国内限定、2027年頃満了）〔要一次確認〕 |
| WO 2019/075326「Hemostatic Port Cuff」（Generations International Asset Management Company LLC） | 膨張式トロカールスリーブ。止血・エアリーク防止＋トロカール migration 防止を明示し、胸腔鏡・ロボット手術を適用範囲に含むとされる | **Status: Ceased（失効）。** 親は米国仮出願 US 62/572,365 のみで正規出願なし〔要一次確認〕 |

**含意（重要）**：

- **FTO 上の障壁ではない。** 両者とも権利化されておらず、実施の自由を妨げない
- **しかし「新規性を否定する公知文献」ではある。** 特に WO 2019/122487 は「バルーン＋酸化セルロース＋トロカール孔の止血」を公開文献として世に出しているため、**同一構成での特許取得はできない**
- → 特許を取るなら、**肋間形状への最適化・留置中に接触し続ける構造・非酸性材料・抜去時の残置機構**など、この公開内容を回避する構成に限定される
- ⚠ **上記の法的地位は Google Patents 表示に基づくエージェント報告であり、事業判断の前に Espacenet / INPADOC で確定させること**

### 3.3 「ニューニット」の正体と、材料側からの重大な反対材料

**「ニューニット」は独立した製品名ではなく、サージセル®・アブソーバブル・ヘモスタットMD（Ethicon/J&J、酸化再生セルロース ORC）の剤形名（SURGICEL NU-KNIT）**である。織布・高密度・高強度で**縫合が可能**なタイプ。承認番号 30400BZX00112000（2022年5月）、2022年12月に医薬品から特定保険医療材料へ移行、織布型は 1 cm² あたり48円。〔一次確認済：本プロジェクトの `hemostatic_agents/md/sections/04_orc_cellulose.md`〕

「巻く・縫う」ために設計された ORC なので材料的な相性は良い。**しかし添付文書と文献には、構想の中核を否定する記載が並ぶ。**

| # | 問題 | 内容 |
|---|---|---|
| 1 | **骨・神経近傍は禁忌** | 添付文書【禁忌・禁止】：「骨・骨の境界・脊髄・視神経および視交叉の内部/周囲/近傍、管状構造組織の近傍（膨潤による圧迫で麻痺・神経障害）」。**肋間はまさに「骨に挟まれ神経が並走する狭い間隙」** |
| 2 | **パッキング目的の留置は禁忌** | 「パッキング/充填目的での留置（後で除去する場合を除く）」。止血達成後は余剰分を可能な限り取り除くことが【警告】 |
| 3 | **「開胸創の肋間に ORC を置く」は既報の対麻痺機序そのもの**〔要一次確認〕 | Brodbelt AR ら, Ann R Coll Surg Engl 2002;84(2):97-99, [PMID 11995773](https://pubmed.ncbi.nlm.nih.gov/11995773/)：開胸時に使用した Surgicel が椎間孔を通過して脊髄を圧迫し**対麻痺3例**。Dogan S ら, Spinal Cord 2005;43(7):445-447, [PMID 15897919](https://pubmed.ncbi.nlm.nih.gov/15897919/)：22歳女性、左開胸後 T6 硬膜外腫瘤、緊急椎弓切除で ORC 塊を摘出。ほかに [PMID 37436267](https://pubmed.ncbi.nlm.nih.gov/37436267/)（T4-5 パッキング後の対麻痺、除圧後も回復せず）〔PDF取得済〕 |
| 4 | **膨潤圧迫だけでなく酸による化学毒性** | ORC の pH は 2.6〜3.5。神経障害は物理的膨潤だけでなく酸の拡散でも起こる〔要一次確認〕 |
| 5 | **創傷治癒を妨げうる** | ORC は線維芽細胞の TGF-β シグナルと遊走を阻害する〔要一次確認〕。**ユーザーの主訴の一つが「創が綺麗に治らない」であることを考えると、致命的な矛盾になりうる** |
| 6 | **術後 CT で腫瘤に見える** | 肺癌術後13例18領域で ORC 由来の異物肉芽腫が再発と紛れ EBUS 生検に至った（Türk İ ら, Updates Surg 2024, [PMID 37558972](https://pubmed.ncbi.nlm.nih.gov/37558972/)）。11例で PET/CT 偽再発（median SUVmax 6.2、消失まで中央値334日）（Sayan M ら, Mol Imaging Radionucl Ther 2023, [PMID 36816516](https://pubmed.ncbi.nlm.nih.gov/36816516/)）〔いずれも要一次確認〕。ほか SURGICEL 合併症の系統的レビュー [PMID 37526076](https://pubmed.ncbi.nlm.nih.gov/37526076/)、脊椎手術後の大量膨潤 [PMID 22278791](https://pubmed.ncbi.nlm.nih.gov/22278791/)〔PDF取得済〕 |
| 7 | **血管に巻くと狭窄** | 添付文書：血管ラッピングではきつく締めすぎない（血管狭窄の報告あり） |
| 8 | **サージフローとの併用不可** | ORC は酸性でトロンビンを失活させる。サージフローは**術中2剤混合キット**でそもそも事前装着自体が不可能 |
| 9 | **乾燥必須・再滅菌不可**〔要一次確認〕 | 乾燥状態でないと効果が出ない |
| 10 | **タコシールも代替にならない** | 添付文書に「**タンポンや栓の代わりに使用しないこと**」と明記 |

**ただし工学的一体化そのものは可能である。** ORC をプラスチック部材へ積層した既承認品として PROCEED® メッシュ（Ethicon）が存在する〔要一次確認〕。

→ **材料選定が構想②の成否を決める。** ORC を肋間に留置する設計は上記1〜5と正面衝突するため、①非膨潤・中性 pH の材料に変える、②量を極小にする、③**抜去時に一緒に回収される／刺入路に薄く残るだけ**の構造にする、のいずれかが必須。

---

## 4. 前提の検証 — 「電メで開けるから治らない」は成立するか

**「否定された」のではなく「そもそも誰も調べていない」**が正確な答えである。

### 4.1 海外の標準手技もむしろ電気メスを使っている〔一次確認済〕

Cleveland Clinic のロボット僧帽弁の公式手技記載（Cullen P, Malas T, Gillinov M. MMCTS 2025, [PMID 40900082](https://pubmed.ncbi.nlm.nih.gov/40900082/)）：

- "…completing the incision with **electrocautery for haemostasis**"（胸腔進入時、**止血のため**電気メスで切開を完成させる）
- "We use **limited Bovie cautery for coagulation** and proceed to insert the angiocaths blindly"

「海外＝メス、日本＝電メ」という対比は、ロボット僧帽弁の主要施設の記載とは一致しない。**電気メスは「雑に開けている」のではなく「出血させないために意図的に使われている」**。

### 4.2 皮膚切開線については電メが同等ないし優位〔一次確認済〕

| 文献 | 対象 | 結論 |
|---|---|---|
| Ly J ら. **Br J Surg 2012;99(5):613-20**（SR/MA、[PMID 22367850](https://pubmed.ncbi.nlm.nih.gov/22367850/)） | 皮膚切開全般 | **電メのほうが速く出血量が少ない。創合併症率・術後疼痛に差なし** |
| Hajibandeh S ら. Int J Surg 2020;75:35-43（SR/MA、[PMID 31978649](https://pubmed.ncbi.nlm.nih.gov/31978649/)） | 鼠径ヘルニア | SSI・漿液腫・術後疼痛に**差なし**。電メは切開時間が短く血腫リスクを下げうる |
| Dos Santos Pimenta N ら. Cir Esp 2025;103(1):3-10（SR/MA、[PMID 39304130](https://pubmed.ncbi.nlm.nih.gov/39304130/)） | 腹部正中切開 | 電メで**出血量が有意に減少**、創感染・早期疼痛に差なし。**電メを推奨** |
| Stupart DA ら. **ANZ J Surg 2016;86(4):303-6**（二重盲検クロスオーバー RCT、[PMID 24165306](https://pubmed.ncbi.nlm.nih.gov/24165306/)） | 腹部皮膚切開の**瘢痕整容** | **整容的に同等**。「電メの日常使用は正当化される」 |
| Kearns SR ら. Br J Surg 2001;88(1):41-4（RCT、[PMID 11136307](https://pubmed.ncbi.nlm.nih.gov/11136307/)） | 待機的正中開腹 | 電メは切開時間・出血量・早期疼痛・鎮痛薬必要量で**有意に有利** |
| Franchi M ら. Am J Surg 2001;181(2):128-32（多施設、[PMID 11425052](https://pubmed.ncbi.nlm.nih.gov/11425052/)） | 正中開腹 | 早期・晩期の創合併症は**同等** |
| Cochrane 2017（16 RCT・2,769例）〔要一次確認〕 | 腹部正中創 | 創感染 RR 1.07、整容性も同等。**ただし「創治癒時間」を報告した研究はゼロ** |

### 4.3 それでも構想を救う余地はある〔要一次確認〕

- ヒト組織学（Ruidiaz 2011）では、通常設定の電メは有意な熱損傷層・炎症・低い創破断強度・広い瘢痕幅を残すとされる
- そして決定的に、**「一線の皮膚切開」と「全層を焼き広げてポート孔を作る操作」は別物である**。後者を比較した研究は世界的に皆無

→ **戦略**：「電メは悪い」と主張するのではなく、**「ポート孔の作り方は誰も比較していない — 我々が最初に測る」**と位置づけるほうが強く、かつ正直である。ただし**製品の主たる売り文句にはしないこと**。主戦場は**出血と migration** に置くべきである。

---

## 5. 先行技術C — 競合は「トロカールを使わない」と「無償の手技的工夫」

### 5.1 硬性トロカールをやめる潮流〔一次確認済〕

- **Raveglia F ら（J Vis Surg 2018;4:66, [PMID 29780712](https://pubmed.ncbi.nlm.nih.gov/29780712/) / PMC5945854）の前向き比較（創縁保護材 WR 20例 vs 11.5mm 硬性トロカール 20例）**：WR 群で**術後疼痛・モルヒネ使用量が有意に少ない（P<0.001）**。硬性トロカールの欠点の筆頭に「**カニューラが肋間神経を強く圧迫し術後疼痛を惹起する**」を挙げ、WR は「**肋間を押し広げず、肋間筋と神経を保護する**」と述べる。WR の利点として「**胸壁からの少量出血からカメラを保護する**」ことも挙げている
- 創縁保護材を硬性トロカールの代わりにカメラポートへ使う：[PMID 27449461](https://pubmed.ncbi.nlm.nih.gov/27449461/)（Ann Thorac Surg 2016）
- **Alexis／Lap Protector 等の soft tissue retractor はロボット心臓手術でも標準**：Cleveland Clinic は working port に Alexis を入れる（MMCTS 2025）
- **hinotori でトロカールを一切使わない胸部手術**：Nakamura A, Kuroda A, Hashimoto M, Kondo N, Funaki S. "Trocarless Thoracic Surgery Using the Hinotori Surgical Robot System With a Wound Retractor." Asian J Endosc Surg 2025;18(1):e70213. [PMID 41399246](https://pubmed.ncbi.nlm.nih.gov/41399246/)（兵庫医科大）。2025年1〜7月に14例、**4ポート全てに Lap Protector Mini Mini を使用、トロカールスリーブは使わない**。可能な理由は hinotori のソフトウェア制御ピボット点（ドッキング不要）。利点として**切開部の出血コントロール**を明記

### 5.2 既存の「無償の解決策」が高容量施設では確立している〔一次確認済〕

Romary DJ, Jefferson HL, Hodges KE（Northwestern 大）. Ann Cardiothorac Surg 2026;15(1):4, [PMID 41669172](https://pubmed.ncbi.nlm.nih.gov/41669172/) / PMC12884191 の逐語：

- 「Three, 8-mm robotic trocars are inserted into the 3rd, 4th, and 6th interspaces, respectively. **We use blunt-tipped obturators to avoid port site bleeding.**」
- 「(B) **using camera to check for port-site bleeding**」（アンドック後の工程図）

→ **①鈍的オブチュレーター、②創プロテクター、③終刀時のカメラによる全ポート点検、という追加コストゼロの手技的解決策が既に確立している。** デバイスはこれらを上回る便益を示す必要がある。**これが最大の競合であり、提案書で最初に潰しておくべき論点。**

---

## 6. 先行技術D — 「刺入路に止血材を残置する」という既存カテゴリ

構想の中で最も新規性が残る部分。隣接領域に **tract sealant（刺入路シーラント）** という確立したカテゴリがある。

- **BioSentry™**（CT ガイド下肺生検の刺入路に自己拡張型ヒドロゲルプラグを留置し気胸・出血を減らす）：前向き比較 [PMID 27826786](https://pubmed.ncbi.nlm.nih.gov/27826786/)／実臨床 [PMID 34178246](https://pubmed.ncbi.nlm.nih.gov/34178246/), [39512979](https://pubmed.ncbi.nlm.nih.gov/39512979/)／SR/MA [PMID 41897557](https://pubmed.ncbi.nlm.nih.gov/41897557/)（2026）／自己血パッチとの RCT [PMID 30480487](https://pubmed.ncbi.nlm.nih.gov/30480487/)／プラグ周囲の組織反応の病理 [PMID 31054891](https://pubmed.ncbi.nlm.nih.gov/31054891/)〔いずれも PDF取得済〕
- 腹腔鏡ポート閉鎖での **Surgicel プラグ法**：[PMID 37062549](https://pubmed.ncbi.nlm.nih.gov/37062549/)（Saudi Med J 2023、n=397）〔PDF取得済〕
- ポート部位の **biological plug** 閉鎖：[PMID 36071329](https://pubmed.ncbi.nlm.nih.gov/36071329/)（Obes Surg 2022）〔PDF取得済〕
- ロボット CABG のポート孔への流動性止血材注入：[PMID 23092664](https://pubmed.ncbi.nlm.nih.gov/23092664/)（§1.5）

**含意**：「デバイスを抜くときに刺入路へ吸収性材料を置いてくる」という設計思想には確立した前例と規制上の前例（BioSentry は FDA クリア済み）がある。**これを肋間ポート版に翻訳するのが、構想の中で最も筋の良い部分である。**

---

## 7. 特許・事業性 — 初版の判定を撤回する

> **初版は「da Vinci に第三者アクセサリで入る道は技術的にも法的にも険しい」と書いたが、これは誤りである。** 検証の結果、①最も価値の高いポートはアームに繋がっていない、②第三者製アクセサリは実在し FDA クリアランスを得ている、③反トラスト訴訟の争点は本構想と無関係、が判明した。以下に訂正版を示す。

### 7.1 決定打 — working port はロボットアームにドッキングしない〔一次確認済〕

EACTS のロボット僧帽弁推奨（Palmen M ら, [PMID 35748726](https://pubmed.ncbi.nlm.nih.gov/35748726/) / PMC9724768）の逐語：

> 「Basically, under single left-lung ventilation, **the working port is created in the third or fourth intercostal space by performing a 1.5- to 4-cm long skin incision. A soft-tissue retractor is placed** to prevent fatty tissue or debris from entering the heart during the procedure. Then, an 8-mm trocar is placed more anteriorly in the same intercostal space to serve as the camera port.」

**最も径が大きく（1.5〜4 cm）、最も肋間の剥離が大きく、したがって最も出血しやすい working port（助手ポート）は、ロボットアームに一切ドッキングしない。** Intuitive のカニューラ特許はいずれも「bowl＋tube＋attachment portion」というアーム連結界面を要件とするため、**working port 向けのバルーン付き止血ポートには一切かからない。**

→ **ユーザーの懸念は、開発対象の中で最も価値の高い部位については前提から成立していない。**

### 7.2 Intuitive のカニューラ特許は「磁石によるID」が必須要件〔一次確認済：請求項を実読〕

| 特許 | クレーム対象 | 請求項1の必須要素 | 出願／登録 |
|---|---|---|---|
| **[US 10,172,687](https://www.freepatentsonline.com/10172687.html) B2** | カニューラ本体 | attachment portion に **identification device、それが one or more magnets** | 優先2014-03-17／登録2019-01-08。満了見込 2035-03-17、Active |
| **[US 12,138,130](https://www.freepatentsonline.com/12138130.html) B2** | カニューラ本体 | attachment portion に配置された **one or more magnets** が識別情報をエンコード | 出願2023-06-23／登録2024-11-12 |
| [US 10,456,208](https://www.freepatentsonline.com/10456208.html) B2 | **カニューラマウント本体**（アーム側） | — | — |
| [US 11,678,945](https://www.freepatentsonline.com/11678945.html) B2 | **カニューラマウント本体**（pivotable clamping arm、latch assembly） | — | — |
| **[US 11,197,729](https://www.freepatentsonline.com/11197729.html) B2** | **滅菌アダプタ** | 「A sterile adaptor for **engaging a cannula mount at a manipulator arm**」 | 登録2021-12-14、存続は概ね2035年 |
| **US 2025/0025249 A1（係属中）** | **磁石なしのカニューラ本体**：bowl section＋tube＋テーパ状 attachment portion のみ | — | 出願18/777,746。**Status: Pending**。審査経過は本調査では確認できず〔未確認〕 |
| [US 10,485,582](https://www.freepatentsonline.com/10485582.html) / [US 12,491,005](https://www.freepatentsonline.com/12491005.html) | カニューラの**くびれ＋リブ**（体壁保持） | — | 2019/2025登録 |

**読み取れること**：

1. **登録済みのカニューラ本体クレームは全て磁石ID必須** → 磁石を持たないカニューラは文言侵害しない
2. **しかし「外付けスリーブなら安全」は無条件には成立しない。** [US 11,197,729](https://www.freepatentsonline.com/11197729.html) B2 は「**マウント界面に噛む部材そのもの**」をクレームしている。回避が成立するのは「カニューラの**管部（tube）／体壁側**に装着する部材」に限られる
3. **最大の不確実要因は係属中の US 2025/0025249 A1**（磁石を要件としないカニューラ本体）。登録されれば形状のみで抵触しうる。**アーム直結カニューラ本体を作る路を選ぶなら、出願 18/777,746 の file wrapper 確認が最優先事項**
4. Intuitive 自身が「カニューラが体壁からズレる／体壁を痛める」問題を認識し 2017→2025 と特許を積んでいる（[US 10,485,582](https://www.freepatentsonline.com/10485582.html) / [US 12,491,005](https://www.freepatentsonline.com/12491005.html) のくびれ＋リブ）。**ユーザーの problem statement はロボット企業も同意している**

### 7.3 第三者製 da Vinci 用アクセサリは実在する〔一次確認済：openFDA 510(k)〕

| 510(k) | 決定日 | 申請者 | 製品 |
|---|---|---|---|
| **[K211104](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K211104)** | **2021-08-19** | **Conmed Corporation** | **AirSeal® dV Solution — AirSeal® Cannula Cap ＋ Bifurcated Filtered Tube Set**。Intuitive 純正カニューラに被せる第三者製キャップ。**腹部・胸腔・小児（≥20kg）適応**。2026-07-22 に da Vinci 5 の 8mm hex cannula へ拡大、「Intuitive と共同で技術適合性試験を実施」と明記〔後段は要一次確認〕 |
| [K252926](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K252926) | 2026-03-26 | Restore Robotics | Permanent Cautery Hook / Spatula。「intended for use with the **da Vinci X/Xi Surgical System**」 |
| [K242610](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K242610) / [K210478](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K210478) | 2025-03-11 / 2022-09-30 | Iconocare Health | 8mm Monopolar Curved Scissors |
| [K241872](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K241872) ほか（[K250399](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250399) / [K250539](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250539) / [K250387](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250387) / [K250417](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250417)） | 2024-11-07 〜 2025-08 | Rebotix | Remanufactured EndoWrist 各種 |

（product code QSM、21 CFR 876.1500、Class II）

**ConMed AirSeal dV は、本構想が採りうる「純正カニューラに被せる外付けデバイス」の規制上の実在前例であり、しかも胸腔適応を既に取っている。** これ以上の追い風はない。

### 7.4 反トラスト訴訟は味方でも敵でもない〔一次確認済：Intuitive 10-Q〕

| 事件 | 状況（2026-08-01時点） |
|---|---|
| **SIS v. Intuitive** | 2021-05-10 提訴 → 2025-01-28 一審で Intuitive 勝訴（JMOL）→ 2025-02-27 控訴 → **第9巡回区で 2026-06-25 に口頭弁論済み、判断待ち。未確定** |
| **Restore Robotics Repairs v. Intuitive** | 2024-09-18 提訴 → 2025-11-07 却下認容 → 第11巡回区へ控訴、**係属中** |
| In Re: da Vinci Surgical Robot Antitrust Litigation（病院クラス） | 2025-03-31 クラス認証、**トライアル 2027-09-14 設定** |

> **初版は「2025年1月に Intuitive 勝訴」と断定したが、いずれも控訴審係属中で確定していない。訂正する。**
>
> さらに重要なのは、**これらの争点はすべて EndoWrist 器具の service / repair / remanufacturing であって、アクセサリの新規製造ではない**という点である。10-Q の記載は SIS＝「relating to EndoWrist service, maintenance, and repair processes」、Restore＝「relating to the service and replacement of X/Xi EndoWrist instruments」。**したがってこれらの勝敗は、新規ポートを作れるかどうかの根拠にも障害にもならない。**

### 7.5 まとめ：作れるか

| 対象 | 判定 |
|---|---|
| **working port／助手ポート／左房リトラクタ用ポート向けのバルーン付き止血ポート** | **Intuitive の IP は無関係。自由に作れる。**（真の障壁は Applied Medical のバルーントロカール特許群） |
| **Intuitive 純正 8mm カニューラの管部に被せる外付けスリーブ**（バルーン＋止血材） | **作れる。** ConMed AirSeal dV（[K211104](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K211104)、胸腔適応込み）が規制上の実在前例。ただし**マウント／滅菌アダプタ界面に噛む形状は [US 11,197,729](https://www.freepatentsonline.com/11197729.html) B2 に抵触しうる**ため回避設計が必要 |
| **アームに直結する純正代替カニューラ本体の新規製造** | **条件付き＝要注意。** 登録済み請求項は全て磁石ID必須なので磁石なし品は文言侵害しないが、それではシステムがカニューラ種別を認識できず実用性に疑問。加えて **US 2025/0025249 A1 が係属中**。この路を選ぶなら file wrapper 確認が最優先 |
| **hinotori 向け／プラットフォーム非依存の汎用胸腔ポート** | **最も自由度が高い**（§8） |

---

## 8. 事業戦略 — hinotori に売り込むという案について

### 8.1 hinotori の現況〔一次確認済：公式サイト・報道〕

- 開発・製造：**メディカロイド**（川崎重工業＋シスメックスの合弁、神戸）
- 日本：2020年8月 泌尿器科で製造販売承認 → 2022年10月 消化器外科 → 婦人科 → **呼吸器外科**（2024年に保険適用。「2024年4月時点で4科」「2024年6月1日 呼吸器外科保険適用」「2024年11月 厚労省承認」と情報源で記載が揺れており、**正確な日付は要確認**）
- 海外：シンガポール 2023、マレーシア 2024、ベトナム 2026、**CE マーク 2026年7月（MDR 2017/745、泌尿器・一般外科・婦人科・胸部外科）**
- **心臓外科は未承認**。ただし欧州（ルーヴェン、Oosterlinck ら）が hinotori による両側内胸動脈採取を人体解剖体で実施して報告（Algoet M ら, Innovations 2026, [doi:10.1177/15569845251408012](https://doi.org/10.1177/15569845251408012)）＝**心臓外科参入の初期段階**
- 技術的特徴：**8軸アーム／ソフトウェアによるピボット点設定でドッキング不要／トロカール周囲のワークスペースが開いている**（公式）

### 8.2 なぜ hinotori なのか

1. **ポートを縛っていない** — アームがトロカールに結合しないので「純正カニューラ」に相当する縛りが構造的に無い
2. **心臓外科がこれから** — 完成した da Vinci の心臓外科エコシステムに割り込むより、これから心臓外科適応を取りに行くプラットフォームに「心臓外科向け専用ポート」を持ち込むほうが相手にとっての価値が高い
3. **国内の開発支援制度に乗る** — AMED の医療機器開発推進／医工連携イノベーション推進事業、PMDA の開発前相談

### 8.3 ただし注意すべき点

- **da Vinci を捨てる必要は無い**（§7.5）。working port 向けなら da Vinci でも自由に作れるし、ConMed のような外付けキャップの前例もある。**「hinotori 専用」に絞るのはむしろ市場を狭める**
- **hinotori の心臓外科適応が取れる保証はない**。専用設計だとプラットフォームの適応拡大が止まった時点で心中する
- → **「汎用の胸腔ポート／スリーブとして設計し、hinotori とも da Vinci とも相性が良い」**が最適解。VATS・MICS・ロボットのどれでも使えるなら単独で薬事も市場も成立する
- 競合として、**兵庫医大の「トロカールレス＋創縁保護材」（[PMID 41399246](https://pubmed.ncbi.nlm.nih.gov/41399246/)）と Northwestern の「鈍的オブチュレーター＋カメラ点検」（[PMID 41669172](https://pubmed.ncbi.nlm.nih.gov/41669172/)）はいずれも追加コストゼロ**である。これを上回る理由（心臓外科特有のヘパリン下での止血、8mm 径での適用、抜去後の止血）を明示できなければ勝てない
- **兵庫医大（Nakamura/Funaki）と神戸大（Tanaka/Maniwa）は、いずれも兵庫県内でメディカロイド（神戸）と同じ圏内**。共同研究の座組として最も自然

---

## 9. 設計上の技術課題とリスク

| # | 課題 | 内容 |
|---|---|---|
| 1 | **肋間神経の圧迫（最大のリスク）** | 硬性トロカールの肋間圧迫が術後疼痛を増やすことは前向き比較で示済（Raveglia 2018, §5.1）。**バルーンで肋間を内側から押し広げる設計はこの唯一のランダム化データと真逆のベクトルを持つ。** ただし「肋間でのバルーン圧迫の神経障害」を直接検証した文献は独自検索でも見つからず〔未確認＝空白〕。設計解はバルーンを**肋間の中に収めない**こと — 胸腔側の胸壁内面に平たく当たる円盤/キノコ型にして、力を肋骨ではなく胸壁内面の広い面積で受ける |
| 2 | **ORC の膨潤・酸性・治癒阻害・画像偽陽性** | §3.3。骨・神経近傍は添付文書上の禁忌で、**開胸創の肋間に ORC を置くことは既報の対麻痺機序そのもの**。材料選定が構想②の成否を決める |
| 3 | **バルーン抜去時の再出血** | Balkhy らの弱点そのもの（§2.3）。**一次データもある**：穿通性頸部外傷のバルーンタンポナーデ 95例中、48–72時間で抜去した72例のうち**2例が抜去時に出血**（Scriba M ら, World J Surg 2020, [PMID 32246186](https://pubmed.ncbi.nlm.nih.gov/32246186/)）〔要一次確認〕。9研究1,658例のメタ解析では、その後の外科的探索を要した 53.47% の主因が「主要血管損傷と **rebleeding at removal**」、合併症 11.70%・死亡 6.30%（Tan L ら, Ann R Coll Surg Engl 2026, [PMID 41396248](https://pubmed.ncbi.nlm.nih.gov/41396248/)）〔要一次確認〕。→ **手術終了時に必ず抜くポートでは「抜いた瞬間に元に戻る」。抜去と同時に止血材を刺入路へ残す機構が構想の中核的新規性になりうる**（§6） |
| 4 | **止血材が挿入時に削れる** | 8mm ポートを肋間に押し込む際、外周の止血材が摩擦で剥落し胸腔内に散る。挿入時はシース／オブチュレータで覆い、**留置位置で初めて露出させる**機構が要る |
| 5 | **血液がないと働かない／濡れると即固まる** | ORC は湿潤で即座に膨潤・ゲル化。TachoSil 系は乾燥面に接着しない。**「乾燥保存 → 挿入時は無反応 → 留置後に機能」** という時間制御が最大の技術課題 |
| 6 | **感染巣化** | ORC は低 pH で抗菌性がある一方、コラーゲン/ゼラチン系は感染巣化が添付文書に明記。MICS の創感染自体が 3–7% 台と決して低くなく、異物量を増やす設計はここに影響する〔要一次確認〕 |
| 7 | **バルーン破裂・遺残** | 胸腔内でのバルーン断片遺残を報告した文献は検索で0件〔該当報告なし＝安全性データが皆無〕。**動物試験で自前に取る必要がある** |
| 8 | 器具交換の運用 | ロボットではポートは留置したままで器具のみ交換するのでバルーンは1回でよい。ただしカメラ／アシストポートは径が違う |
| 9 | CO2 送気とのシール | 胸腔は密閉腔でないので腹腔ほどのシールは不要。CO2 送気施設ではバルーンがシールも兼ねられる |
| 10 | 滅菌・保存安定性 | 止血材装着状態での滅菌耐性、貯蔵中の失活。ORC は再滅菌不可とされる〔要一次確認〕。PROCEED メッシュに前例あり |
| 11 | **コスト／競合** | 対抗馬は「Lap Protector＋既存 ORC」「尿道カテーテル」「鈍的オブチュレーター」。**いずれも安いか無料**。償還を取れるだけの臨床的優位性の証明が要る |

---

## 10. 未解決の空白（＝この構想が主張できる場所）

1. **ロボットの 8mm ポート孔に限定した出血源内訳データはゼロ。** 非ロボットの小開胸／内視鏡には3件ある（§1.3）が、ロボットポートに限れば存在しない。**自施設で前向きに出血源を記録することが最初の研究テーマ**
2. **心臓外科（全身ヘパリン化・体外循環下）のポート創面出血を定量した報告が無い。** §1.4 の RCT は呼吸器外科
3. **「ポート孔をどう作るか（電メ vs メス vs 鈍的）」を比較した研究が世界的に皆無**（§4.3）
4. **8mm 径の胸腔ポートに対する止血ソリューションが無い。** 創縁保護材は working port（1.5–4cm）にしか入らない
5. **止血材を外周に事前装着したトロカール／ポートは、製品も登録特許クレームも存在しない**（FreePatentsOnline 専門家検索・Google Patents XHR API・openFDA GUDID・openFDA 510(k)・PubMed の複数検索式でいずれも 0件）。ただし WO 2019/122487（失効）と [US 7,018,392](https://www.freepatentsonline.com/7018392.html)（満了）が公開文献として存在するため、**特許を取るならこれらを回避する構成が必要**
6. **抜去時に止血材を刺入路へ残置する肋間ポートは存在しない**
7. **肋間でのバルーン圧迫が神経障害を起こすかどうかを検証した文献が無い**（リスクでもあり、自前で埋めるべき空白でもある）

---

## 11. 次にやるべきこと（優先順）

| 優先 | 内容 |
|---|---|
| **1** | **WO 2019/122487 の全文と法的地位を Espacenet / INPADOC で確定**（§3.2）。「請求項3に酸化セルロース含浸」「失効・各国移行なし」はいずれもエージェント報告で一次未確認。**新規性の生死を決める** |
| **1'** | **J-PlatPat での国内先行技術調査**。本調査では J-PlatPat に直接アクセスできず、**日本国内出願の悉皆性が未担保**。八光 E・ZバルーンⅡ の関連出願は必ず確認すること |
| **2** | **係属出願 US 2025/0025249 A1（18/777,746）の file wrapper 確認**（弁理士）。アーム直結カニューラ本体を作る路の帰趨を決める。ただし §7.1 の通り working port 狙いなら不要 |
| **3** | **Applied Medical の公式サイト（日英）で「Tamponade Effect」の記載を自分の目で確認**し、[US 8,142,467](https://www.freepatentsonline.com/8142467.html) / [US 8,287,503](https://www.freepatentsonline.com/8287503.html) の明細書全文と満了日を精査。**ここが真の FTO 障壁** |
| **4** | **Kiani/Poston 2012（[PMID 23092664](https://pubmed.ncbi.nlm.nih.gov/23092664/)）と Balkhy 2025（[PMID 40913323](https://pubmed.ncbi.nlm.nih.gov/40913323/)）の本文入手**。前者は「有意なのは輸血だけ」の確認、後者は対照群6例の出血源の確認 |
| **5** | **自施設のロボット心臓手術データの後ろ向き集計** — 再開胸出血の症例で「どこから出ていたか」。§10-1 の空白を自分で埋める |
| **6** | ConMed に AirSeal dV の開発経緯をヒアリング（Intuitive とどう折り合いをつけたか）。**外付けデバイスの実務的な進め方の最良の教師** |
| **7** | 神戸大（Tanaka/Maniwa）・兵庫医大（Nakamura/Funaki）へのコンタクト。ORC リング付き創縁保護材と hinotori トロカールレスの両方が兵庫県内で走っている |
| **8** | メディカロイドへの打診（PMDA 開発前相談の前にプラットフォーム側の意向を確認） |
| **10** | 〔要一次確認〕〔未確認〕と付した項目の裏取り |

---

## 12. 参考文献

- 取得状況：[download_status.md](download_status.md)（取得済 46 / 未取得 71）
- 未取得文献の抄録：[abstracts_not_downloaded.txt](abstracts_not_downloaded.txt)
- PDF：`pdf/` ／ テキスト：`pdf_text/` ／ 特許 PDF・HTML：`patents/`
