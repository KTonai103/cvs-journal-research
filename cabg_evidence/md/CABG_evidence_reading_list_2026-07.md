# CABG 最新エビデンス 網羅的サーベイ & ダウンロード用文献リスト

作成日: 2026-07-26 / 対象: 冠動脈バイパス術（OPCAB vs ONCAB を軸に、史的背景・導管選択・教育・薬物療法まで）

## 0. 本リストの作り方（再現可能）

- PubMed E-utilities で **66クエリ**（RCT / メタ解析 / レジストリ / 史的 / 導管 / 教育 / 薬物 / ガイドライン等の各アングル）を機械実行
- 収集 **3,112 レコード**（タイトル・雑誌・年・publication type・DOI・抄録）→ 雑誌ランク × publication type × 新しさ × タイトル語でスコアリング → 792編を目視トリアージ
- 最終選抜 **266編**（うちユニーク 261 PMID）。**全PMIDのタイトルはPubMedから機械取得したもので、手打ち転記なし**
- 中間ファイル: `search_ids.json` / `records.json` / `shortlist*.txt`（scratchpad）

---

## 1. まず最重要：ご提示ソースの3研究の照合結果

ソースに出てくる3つの発表について一次文献を突き合わせました。**2つは特定でき、1つは論文として存在しません。**

### ✅ Mr. Shahzad Raja「25年生存 57% vs 42%」→ 特定・数値も一致

**PMID 42266971** — Raja SG. *Long-Term Survival and Mortality Predictors of Off-Pump vs On-Pump Coronary Artery Bypass Grafting: A 25-Year Cohort Study.* Ann Thorac Surg Short Rep. 2026

抄録実数: 13,626例（off-pump 7,408 / on-pump 6,218）→ PSM 11,368例（各5,684）。25年生存は **未調整 58.2% vs 42.2%、マッチ後 57.5% vs 42.7%（いずれも P<.001）**。ソースの「57% / 42%」はマッチ後の数字と一致します。Harefieldの単施設・OPCAB専用プログラムという文脈も記載どおりです。

### ⚠️ Dr. André Lamy「3試験（ROOBY・CORONARY・GOPCABE）約10,000例の統合」→ 統合論文としては未発見

各試験の30日・1年・5年成績（PMID 22449296 / 23477676 / 27771985 / 19890125 / 28813218 / 23477657 / 30732456）は全て揃っていますが、**この3試験を1本にまとめたLamy名義の統合解析（IPDまたはaggregate）はPubMedに存在しません**。学会発表段階の可能性が高いと考えます。同趣旨を担う既刊のメタ解析としては PMID 29495998（Smart JACC 2018）、38522653（Comanici 2024, 10年死亡）、30373421（Gaudino JAHA 2018, 術者経験で層別）が最も近く、リストの §3 に収録しました。

### ❌ Dr. John Puskas「STSデータベース 184,550ペア・15年生存が完全同一」→ 該当論文なし。かつ既刊データは逆方向

「184,550組のPSM・15年生存曲線が重なる」という論文はPubMedに見当たりません（Puskas氏の全近著、STSデータベース系、Medicare連結系を個別に検索済み）。学会発表（STS/AATS）と思われます。

**ここは注意が必要です。**現時点で公刊されている最大の同種解析は逆の結論です：

**PMID 34411544** — Squiers JJ. *Long-Term Survival After On-Pump and Off-Pump CABG.* Ann Thorac Surg 2022。Medicare **1,235,089例**（off-pump 209,085）。IPTW後も off-pump が長期死亡で不利（**生存中央値 9.8年 vs 10.2年、差 −134日、log-rank P<.001**）。ただし**術者症例数との交互作用**があり、高volume術者では差が縮小します。

つまりソースの「15年完全同一」は、公刊エビデンスでは**まだ裏が取れていない主張**です。引用される場合は Squiers 2022 と Chikwe 2018（PMID 30236310、経験豊富な術者に限定した解析）を必ず併記されることをお勧めします。

なお「不完全血行再建 HR 1.33 / MAG HR 0.60 が相殺する」という構造そのものは、別々の論文で裏付けがあります → PMID 30686645（off/on の長期差は血行再建の不完全性で説明される）と PMID 28119382 / 30699314（多枝動脈グラフトの生存効果）。§8・§5 に収録しました。

---

## 2. 領域別 文献リスト

凡例: **★ = 最優先（Tier A）** / 無印 = 二次（Tier B）。各行は `[PMID] 著者 (年) 雑誌 — タイトル` + 日本語コメント。

### §1. 史的背景 — CABGの誕生と50年の軌跡

- ★ **[9714098]** Favaloro RG (1998) *Circulation* — Landmarks in the development of coronary artery bypass surgery.
  - Favaloro自身による回顧。Vineberg→Sones冠動脈造影→1967 Cleveland Clinicの伏在静脈グラフト。一次資料として必携
- **[4642307]** Favaloro R (1972) *Circulation* — Direct and indirect coronary surgery.
  - Favaloro 1972 Circulation。直接/間接冠動脈手術の初期分類。歴史一次資料
- ★ **[24086085]** Head SJ (2013) *Eur Heart J* — Coronary artery bypass grafting: Part 1--the evolution over the first 50 years.
  - Head EHJ 2013 Part 1「最初の50年の進化」。歴史レビューの決定版・前半
- ★ **[24086086]** Head SJ (2013) *Eur Heart J* — Coronary artery bypass grafting: Part 2--optimizing outcomes and future prospects.
  - Head EHJ 2013 Part 2「アウトカム最適化と将来展望」。Part 1と対
- ★ **[34294272]** Mack MJ (2021) *J Am Coll Cardiol* — Myocardial Revascularization Surgery: JACC Historical Breakthroughs in Perspective.
  - Mack JACC 2021「JACC Historical Breakthroughs」。心筋血行再建術の歴史的ブレークスルー総括
- ★ **[35912444]** Doenst T (2022) *Dtsch Arztebl Int* — The Treatment of Coronary Artery Disease—Current Status Six Decades After the First Bypass Operation.
  - Doenst 2022「初回バイパス手術から60年」。独語圏からの60年総括・現在地
- ★ **[30369328]** Gaudino M (2018) *J Am Heart Assoc* — Off-Pump Coronary Artery Bypass Grafting: 30 Years of Debate.
  - Gaudino JAHA 2018「OPCAB: 30 Years of Debate」。off-pump論争の30年史。本テーマの導入に最適
- ★ **[38941506]** Calafiore AM (2024) *Eur J Cardiothorac Surg* — Controversy. On pump or off pump: what will I do when I grow up? A narrative systematic review.
  - Calafiore EJCTS 2024「on pumpかoff pumpか、大人になったら何をする?」narrative systematic review。OPCABの隆盛と幻滅、そして今後を叙述
- **[41210677]** Gorton AJ (2025) *Int J Angiol* — The History of Coronary Artery Disease.
  - Gorton 2025「The History of Coronary Artery Disease」冠動脈疾患そのものの歴史
- **[41210676]** Glazier CR (2025) *Int J Angiol* — Coronary Intervention: History and Current Status.
  - Glazier 2025「Coronary Intervention: History and Current Status」PCI側の歴史。対比用
- **[39783258]** Valdes-Socin HG (2025) *Acta Cardiol* — René Gerónimo Favaloro (1923-2000): the challenging dream of a heart surgeon.
  - Favaloro評伝 (1923-2000)。人物史
- **[38919214]** Mohyeldin M (2024) *Cureus* — F. Mason Sones Jr.: The Serendipitous Discovery of Coronary Angiography and Its Lasting Impact on Cardiology.
  - Mason Sones と冠動脈造影の偶然の発見。CABG誕生の前提条件
- **[22893280]** Lee JD (2012) *Circ J* — History and current status of robotic totally endoscopic coronary artery bypass.
  - ロボットTECABの歴史と現状 (2012)
- **[39157182]** Bonatti J (2024) *Ann Cardiothorac Surg* — Historical landmarks in the development of robotic coronary bypass grafting.
  - Bonatti 2024「ロボット冠動脈バイパスの歴史的マイルストーン」
- **[20869314]** Tatoulis J (2011) *Heart Lung Circ* — Giant leaps in surgical myocardial revascularisation.
  - Tatoulis「Giant leaps in surgical myocardial revascularisation」
- **[39552037]** Lee DY (2025) *J Chest Surg* — Historical Perspectives of the Korean Society for Thoracic and Cardiovascular Surgery: Sung Nok Hong (1927-2017) Who Performed the First Coronary Artery Bypass Graft in Korea.
  - 韓国初のCABGを行ったSung Nok Hong。アジアの歴史

### §2. OPCAB vs ONCAB — 主要RCTと長期追跡 (一次データ)

- ★ **[19890125]** Shroyer AL (2009) *N Engl J Med* — On-pump versus off-pump coronary-artery bypass surgery.
  - ★ROOBY 本体 NEJM 2009。VA多施設2203例、1年で off-pump 劣位。OPCAB批判の起点
- ★ **[28813218]** Shroyer AL (2017) *N Engl J Med* — Five-Year Outcomes after On-Pump and Off-Pump Coronary-Artery Bypass.
  - ★ROOBY-FS 5年 NEJM 2017。5年死亡 off-pump 15.2% vs on-pump 11.9%と有意に劣位
- ★ **[35171210]** Quin JA (2022) *JAMA Surg* — Ten-Year Outcomes of Off-Pump vs On-Pump Coronary Artery Bypass Grafting in the Department of Veterans Affairs: A Randomized Clinical Trial.
  - ★ROOBY 10年 JAMA Surg 2022 (Quin)。10年死亡 34.2% vs 31.1%（RR 1.05, 95%CI 0.99–1.11, P=.12）で**死亡の有意差は消失**。ただし複合エンドポイント到達までの期間は off-pump が約4.3か月短く（P=.03）、著者の結論は依然 off-pump に否定的。5年（PMID 28813218: 15.2% vs 11.9%, RR 1.28）との差分の読み方が要点
- ★ **[22449296]** Lamy A (2012) *N Engl J Med* — Off-pump or on-pump coronary-artery bypass grafting at 30 days.
  - ★CORONARY 30日 NEJM 2012 (Lamy)。4752例、複合エンドポイント差なし
- ★ **[23477676]** Lamy A (2013) *N Engl J Med* — Effects of off-pump and on-pump coronary-artery bypass grafting at 1 year.
  - ★CORONARY 1年 NEJM 2013 (Lamy)
- ★ **[27771985]** Lamy A (2016) *N Engl J Med* — Five-Year Outcomes after Off-Pump or On-Pump Coronary-Artery Bypass Grafting.
  - ★CORONARY 5年 NEJM 2016 (Lamy)。差なし。ユーザー提示ソースの根拠の中核
- ★ **[23477657]** Diegeler A (2013) *N Engl J Med* — Off-pump versus on-pump coronary-artery bypass grafting in elderly patients.
  - ★GOPCABE NEJM 2013 (Diegeler)。高齢者2539例、30日/1年差なし
- ★ **[30732456]** Diegeler A (2019) *Circulation* — Five-Year Outcome After Off-Pump or On-Pump Coronary Artery Bypass Grafting in Elderly Patients.
  - ★GOPCABE 5年 Circulation 2019。5年でも差なし
- ★ **[32339504]** Yang L (2020) *Ann Thorac Surg* — Long-Term Graft Patency After Off-Pump and On-Pump Coronary Artery Bypass: A CORONARY Trial Cohort.
  - CORONARY コホートの長期グラフト開存 (Ann Thorac Surg 2020)
- ★ **[22592900]** Hattler B (2012) *Circulation* — Off-Pump coronary artery bypass surgery is associated with worse arterial and saphenous vein graft patency and less effective revascularization: Results from the Veterans Affairs Randomized On/Off Bypass (ROOBY) trial.
  - ROOBY 血管造影サブ解析 Circulation 2012 (Hattler)。off-pumpで開存率不良かつ血行再建不完全。「不完全血行再建」論の一次データ
- ★ **[39098613]** Koop Y (2024) *Int J Cardiol* — Octopus follow-up: 20 year prognosis in patients randomized to on-pump CABG, off-pump CABG or PCI.
  - ★Octopus試験 20年追跡 (Int J Cardiol 2024)。RCT最長級。20年全死亡 on-pump 50.0% vs off-pump 46.5%、複合アウトカムに差なし（HR 0.82, 95%CI 0.59–1.12）。PCI比較群では off-pump CABG の再介入が有意に少ない（HR 0.52）
- **[11591611]** van Dijk D (2001) *Circulation* — Early outcome after off-pump versus on-pump coronary bypass surgery: results from a randomized study.
  - Octopus 早期成績 Circulation 2001
- **[12556542]** Nathoe HM (2003) *N Engl J Med* — A comparison of on-pump and off-pump coronary bypass surgery in low-risk patients.
  - Octopus 低リスク患者 NEJM 2003 (Nathoe)
- **[17312289]** van Dijk D (2007) *JAMA* — Cognitive and cardiac outcomes 5 years after off-pump vs on-pump coronary artery bypass graft surgery.
  - Octopus 認知機能5年 JAMA 2007
- **[11903027]** Van Dijk D (2002) *JAMA* — Cognitive outcome after off-pump and on-pump coronary artery bypass graft surgery: a randomized trial.
  - Octopus 認知機能 JAMA 2002。「off-pumpは認知機能を守る」仮説の否定
- ★ **[20837925]** Hueb W (2010) *Circulation* — Five-year follow-up of a randomized comparison between off-pump and on-pump stable multivessel coronary artery bypass grafting. The MASS III Trial.
  - MASS III 5年 Circulation 2010 (Hueb)
- ★ **[35953640]** Tadokoro N (2023) *Gen Thorac Cardiovasc Surg* — 15-year outcomes of the JOCRI study (JOCRIED study): a randomised comparison of off-pump and on-pump multiple arterial coronary revascularisation.
  - ★JOCRI 15年 (JOCRIED) 2023。日本発・多枝動脈グラフトでのon/off RCT長期。日本の文脈で必読
- **[20083683]** Møller CH (2010) *Circulation* — No major differences in 30-day outcomes in high-risk patients randomized to off-pump versus on-pump coronary bypass surgery: the best bypass surgery trial.
  - Best Bypass Surgery 高リスク30日 Circulation 2010
- **[21415073]** Møller CH (2011) *Heart* — Three-year follow-up in a subset of high-risk patients randomly assigned to off-pump versus on-pump coronary artery bypass surgery: the Best Bypass Surgery trial.
  - BBS 3年追跡 Heart 2011
- **[22523305]** Houlind K (2012) *Circulation* — On-pump versus off-pump coronary artery bypass surgery in elderly patients: results from the Danish on-pump versus off-pump randomization study.
  - DOORS 高齢者 Circulation 2012
- **[24613160]** Houlind K (2014) *J Thorac Cardiovasc Surg* — Graft patency after off-pump coronary artery bypass surgery is inferior even with identical heparinization protocols: results from the Danish On-pump Versus Off-pump Randomization Study (DOORS).
  - DOORS グラフト開存 JTCVS 2014。同一ヘパリン化でもoff-pumpの開存が劣る
- **[15557371]** Widimsky P (2004) *Circulation* — One-year coronary bypass graft patency: a randomized comparison between off-pump and on-pump surgery angiographic results of the PRAGUE-4 trial.
  - PRAGUE-4 1年開存 Circulation 2004
- **[14992872]** Straka Z (2004) *Ann Thorac Surg* — Off-pump versus on-pump coronary surgery: final results from a prospective randomized study PRAGUE-4.
  - PRAGUE-4 最終結果 2004
- **[11955537]** Angelini GD (2002) *Lancet* — Early and midterm outcome after off-pump and on-pump surgery in Beating Heart Against Cardioplegic Arrest Studies (BHACAS 1 and 2): a pooled analysis of two randomised controlled trials.
  - BHACAS 1&2 プール解析 Lancet 2002 (Angelini)。初期の代表的RCT
- **[15100202]** Puskas JD (2004) *JAMA* — Off-pump vs conventional coronary artery bypass grafting: early and 1-year graft patency, cost, and quality-of-life outcomes: a randomized trial.
  - Puskas SMART試験 JAMA 2004。1年開存・コスト・QOL
- **[21619980]** Puskas JD (2011) *Ann Thorac Surg* — Off-pump and on-pump coronary artery bypass grafting are associated with similar graft patency, myocardial ischemia, and freedom from reintervention: long-term follow-up of a randomized trial.
  - SMART長期追跡 Ann Thorac Surg 2011。開存・虚血・再介入で同等
- **[31395122]** Benedetto U (2019) *J Am Coll Cardiol* — Off-Pump Versus On-Pump Bypass Surgery for Left Main Coronary Artery Disease.
  - 左主幹部病変でのoff vs on (JACC 2019, Benedetto)
- **[24886787]** Garg AX (2014) *JAMA* — Kidney function after off-pump or on-pump coronary artery bypass graft surgery: a randomized clinical trial.
  - CORONARY 腎機能 JAMA 2014 (Garg)
- ★ **[28082464]** Stevens LM (2017) *Eur J Cardiothorac Surg* — Conversion after off-pump coronary artery bypass grafting: the CORONARY trial experience.
  - CORONARY試験のconversion解析 EJCTS 2017。術中コンバージョンの実像
- **[37624649]** Sajja LR (2023) *Asian Cardiovasc Thorac Ann* — Five-year outcomes of off and on-pump CABG: Insights from PROMOTE Patency Trial.
  - PROMOTE Patency Trial 5年 (2023)

### §3. メタ解析・システマティックレビュー (OPCAB vs ONCAB)

- ★ **[29495998]** Smart NA (2018) *J Am Coll Cardiol* — Long-Term Outcomes of On- Versus Off-Pump Coronary Artery Bypass Grafting.
  - ★Smart JACC 2018。長期アウトカムのSR/MA。頻用される中核メタ解析
- ★ **[38522653]** Comanici M (2024) *Am J Cardiol* — 10-Year Mortality of Off-Pump Versus On-Pump Coronary Artery Bypass Grafting: An Updated Systematic Review, Meta-Analysis, and Meta-Regression.
  - ★Comanici Am J Cardiol 2024。10年死亡の最新SR/MA+メタ回帰
- ★ **[28942940]** Takagi H (2017) *Am J Cardiol* — Meta-Analysis Comparing ≥10-Year Mortality of Off-Pump Versus On-Pump Coronary Artery Bypass Grafting.
  - Takagi 2017。≥10年死亡に絞ったメタ解析
- ★ **[30373421]** Gaudino M (2018) *J Am Heart Assoc* — Off- Versus On-Pump Coronary Surgery and the Effect of Follow-Up Length and Surgeons' Experience: A Meta-Analysis.
  - ★Gaudino JAHA 2018。追跡期間と『術者経験』で層別したメタ解析。経験依存性を定量化した重要論文
- ★ **[28958597]** Filardo G (2018) *J Thorac Cardiovasc Surg* — Efficacy and effectiveness of on- versus off-pump coronary artery bypass grafting: A meta-analysis of mortality and survival.
  - Filardo JTCVS 2018。efficacy(RCT) vs effectiveness(実臨床)を分けたメタ解析
- ★ **[35041977]** Zhou Z (2022) *Int J Surg* — Randomized evidence on graft patency after off-pump versus on-pump coronary artery bypass grafting: An updated meta-analysis.
  - Zhou Int J Surg 2022。グラフト開存に関するRCTエビデンスの更新メタ解析
- ★ **[21987177]** Afilalo J (2012) *Eur Heart J* — Off-pump vs. on-pump coronary artery bypass surgery: an updated meta-analysis and meta-regression of randomized trials.
  - Afilalo EHJ 2012。メタ回帰付き。古典的だが引用頻度が高い
- **[18628261]** Møller CH (2008) *Eur Heart J* — Clinical outcomes in randomized trials of off- vs. on-pump coronary artery bypass surgery: systematic review with meta-analyses and trial sequential analyses.
  - Møller EHJ 2008。trial sequential analysis併用
- **[16139139]** Wijeysundera DN (2005) *J Am Coll Cardiol* — Off-pump coronary artery surgery for reducing mortality and morbidity: meta-analysis of randomized and observational studies.
  - Wijeysundera JACC 2005。RCT+観察研究
- **[20167334]** Kuss O (2010) *J Thorac Cardiovasc Surg* — Off-pump versus on-pump coronary artery bypass grafting: a systematic review and meta-analysis of propensity score analyses.
  - Kuss JTCVS 2010。傾向スコア解析だけを集めたSR/MA
- **[26276839]** Deppe AC (2016) *Eur J Cardiothorac Surg* — Current evidence of coronary artery bypass grafting off-pump versus on-pump: a systematic review with meta-analysis of over 16,900 patients investigated in randomized controlled trials†.
  - Deppe EJCTS 2016。RCT 16,900例
- **[38626442]** He L (2024) *Int J Surg* — Clinical outcomes of on-pump versus off-pump coronary-artery bypass surgery: a meta-analysis.
  - He Int J Surg 2024。最新の総合メタ解析
- ★ **[26433633]** Kowalewski M (2016) *J Thorac Cardiovasc Surg* — Off-pump coronary artery bypass grafting improves short-term outcomes in high-risk patients compared with on-pump coronary artery bypass grafting: Meta-analysis.
  - ★Kowalewski JTCVS 2016。高リスク患者でoff-pumpが短期成績を改善。ユーザーの『高リスクで恩恵』論の直接根拠
- ★ **[21664624]** Kuss O (2011) *J Thorac Cardiovasc Surg* — Do higher-risk patients benefit from off-pump coronary artery bypass grafting? Evidence from an ecologic analysis of randomized trials.
  - Kuss JTCVS 2011。RCTのecologic解析で『高リスクほどoff-pumpが有利か』を検証
- **[29608874]** Zhou P (2018) *Ann Thorac Surg* — Meta-Analysis of Repeat Revascularization of Off-Pump and On-Pump Coronary Artery Bypass Surgery.
  - 再血行再建に関するメタ解析 (Ann Thorac Surg 2018)
- **[25791924]** Altarabsheh SE (2015) *Ann Thorac Surg* — Off-pump coronary artery bypass reduces early stroke in octogenarians: a meta-analysis of 18,000 patients.
  - 80歳以上で早期脳卒中を減らす (Ann Thorac Surg 2015)
- **[35266173]** Sun L (2022) *Clin Cardiol* — Off-pump versus on-pump coronary artery bypass grafting for octogenarians: A meta-analysis involving 146 372 patients.
  - 八十歳代 146,372例のメタ解析 (2022)
- **[21801945]** Mukherjee D (2011) *Ann Thorac Surg* — Meta-analysis of organ damage after conversion from off-pump coronary artery bypass procedures.
  - コンバージョン後の臓器障害メタ解析
- **[21684171]** Mukherjee D (2012) *Eur J Cardiothorac Surg* — Intra-operative conversion is a cause of masked mortality in off-pump coronary artery bypass: a meta-analysis.
  - コンバージョンが『隠れた死亡』を生む (EJCTS 2012)
- **[21937020]** Jarral OA (2011) *Ann Thorac Surg* — Off-pump coronary artery bypass in patients with left ventricular dysfunction: a meta-analysis.
  - 左室機能低下例でのoff-pump (Ann Thorac Surg 2011)
- **[33016239]** Zhang P (2021) *Perfusion* — Off-pump versus on-pump redo coronary artery bypass grafting: a systematic review and meta-analysis.
  - 再手術CABGでのoff vs on SR/MA (2021)
- ★ **[26371452]** Puskas JD (2015) *Innovations (Phila)* — ISMICS Consensus Conference and Statements of Randomized Controlled Trials of Off-Pump Versus Conventional Coronary Artery Bypass Surgery.
  - ★ISMICS コンセンサス会議声明 (Puskas, Innovations 2015)。RCTを総括した公式コンセンサス
- **[37720926]** Zhu L (2023) *Int J Surg* — Comparative efficacy on outcomes of C-CABG, OPCAB, and ONBEAT in coronary heart disease: a systematic review and network meta-analysis of randomized controlled trials.
  - C-CABG / OPCAB / ONBEAT のネットワークメタ解析 (2023)
- **[36349729]** Hwang B (2022) *J Card Surg* — Coronary artery bypass surgery for acute coronary syndrome: A network meta-analysis of on-pump cardioplegic arrest, off-pump, and on-pump beating heart strategies.
  - ACSに対する3戦略のネットワークメタ解析 (2022)

### §4. 大規模レジストリ・傾向スコア (超長期・実臨床)

- ★ **[42266971]** Raja SG (2026) *Ann Thorac Surg Short Rep* — Long-Term Survival and Mortality Predictors of Off-Pump vs On-Pump Coronary Artery Bypass Grafting: A 25-Year Cohort Study.
  - ★★Raja 25年コホート (Ann Thorac Surg Short Rep 2026)。13,626例→PSM 11,368例。25年生存 off 57.5% vs on 42.7%。ユーザー提示ソースの『25年57%/42%』の一次文献
- ★ **[34411544]** Squiers JJ (2022) *Ann Thorac Surg* — Long-Term Survival After On-Pump and Off-Pump Coronary Artery Bypass Grafting.
  - ★★Squiers Ann Thorac Surg 2022。Medicare 1,235,089例。全体ではoff-pumpが長期死亡不利 (生存中央値9.8 vs 10.2年) だが術者症例数と交互作用。ソースの『15年生存完全同一』とは逆方向で、必ず対で読むべき
- ★ **[30236310]** Chikwe J (2018) *J Am Coll Cardiol* — Long-Term Outcomes After Off-Pump Versus On-Pump Coronary Artery Bypass Grafting by Experienced Surgeons.
  - ★Chikwe JACC 2018。『経験豊富な術者』に限定した長期比較。術者経験で結論が変わることを示す
- ★ **[31740974]** Kirmani BH (2019) *Eur J Cardiothorac Surg* — Long-term survival following on-pump and off-pump coronary artery bypass graft surgery: a propensity score-matched analysis.
  - Kirmani EJCTS 2019。傾向スコアマッチング長期生存
- **[27777290]** Kirmani BH (2016) *Circulation* — Long-Term Survival and Freedom From Reintervention After Off-Pump Coronary Artery Bypass Grafting: A Propensity-Matched Study.
  - Kirmani Circulation 2016。長期生存と再介入回避
- ★ **[24703910]** Kim JB (2014) *J Am Coll Cardiol* — Long-term survival following coronary artery bypass grafting: off-pump versus on-pump strategies.
  - Kim JACC 2014。off vs on の長期生存 (アジア大規模)
- **[17709642]** Hannan EL (2007) *Circulation* — Off-pump versus on-pump coronary artery bypass graft surgery: differences in short-term outcomes and in long-term mortality and need for subsequent revascularization.
  - Hannan Circulation 2007。NY州レジストリ。短期利得と長期の再血行再建
- **[22965976]** Marui A (2012) *Circulation* — Benefits of off-pump coronary artery bypass grafting in high-risk patients.
  - Marui Circulation 2012 (CREDO-Kyoto)。高リスク患者でのoff-pumpの利益。日本のデータ
- ★ **[34800223]** Numata S (2022) *Gen Thorac Cardiovasc Surg* — Comparison of long-term outcomes between off-pump and on-pump coronary artery bypass grafting using Japanese nationwide cardiovascular surgery database.
  - ★Numata 2022。JCVSD 日本全国データベースでのoff vs on 長期比較。日本の実態把握に必須
- **[31256329]** Saito A (2019) *Gen Thorac Cardiovasc Surg* — Current Status of cardiovascular surgery in Japan, 2015 and 2016: a report based on the Japan Cardiovascular Surgery Database. 2-Isolated coronary artery bypass grafting surgery.
  - JCVSD 年次報告 (孤立性CABG) 2019
- **[41403064]** Ju MH (2026) *J Chest Surg* — Nationwide Trends in Coronary Artery Bypass Grafting in the Republic of Korea, 2005-2022: A Comparison with International Data.
  - 韓国のCABG全国動向 2005-2022 (2026)。国際比較付き
- ★ **[41619148]** Komiya T (2026) *Gen Thorac Cardiovasc Surg* — The 20-year long-term outcomes of coronary artery bypass grafting: An off-pump first approach.
  - ★Komiya 2026。『off-pump first』方針での20年長期成績 (日本・倉敷)
- ★ **[25043865]** Bakaeen FG (2014) *J Thorac Cardiovasc Surg* — Trends in use of off-pump coronary artery bypass grafting: Results from the Society of Thoracic Surgeons Adult Cardiac Surgery Database.
  - Bakaeen JTCVS 2014。STS成人心臓外科データベースにおけるoff-pump使用率の推移。米国でOPCABが衰退した実態
- **[35229663]** Deo SV (2022) *J Am Heart Assoc* — Off-Pump Coronary Artery Bypass Grafting: Department of Veteran Affairs' Use and Outcomes.
  - VA におけるoff-pump使用と成績 (JAHA 2022)
- **[42288779]** Pikkujämsä A (2026) *BMC Cardiovasc Disord* — Comparable survival over an extended follow-up after on-pump versus off-pump coronary artery bypass grafting: a propensity score-matched cohort.
  - Pikkujämsä 2026。延長追跡でのPSM比較 (フィンランド)
- **[34333605]** Deutsch MA (2021) *Interact Cardiovasc Thorac Surg* — Risk-adjusted analysis of long-term outcomes after on- versus off-pump coronary artery bypass grafting.
  - Deutsch 2021。リスク調整長期アウトカム
- **[25648476]** Grau JB (2015) *J Thorac Cardiovasc Surg* — Impact of pump status and conduit choice in coronary artery bypass: A 15-year follow-up study in 1412 propensity-matched patients.
  - Grau JTCVS 2015。ポンプ有無×導管選択の15年追跡 1412 PSM例
- **[41330389]** Beckmann A (2025) *Thorac Cardiovasc Surg* — German Heart Surgery Report 2024: The Annual Updated Registry of the German Society for Thoracic and Cardiovascular Surgery.
  - German Heart Surgery Report 2024。ドイツ全国年次レジストリ

### §5. 多枝動脈グラフト (MAG) / 導管選択 — 長期開存とアウトカム

- ★ **[30699314]** Taggart DP (2019) *N Engl J Med* — Bilateral versus Single Internal-Thoracic-Artery Grafts at 10 Years.
  - ★ART 10年 NEJM 2019 (Taggart)。BITA vs SITA。ITT解析で差なしという衝撃の結果
- **[20805116]** Taggart DP (2010) *Eur Heart J* — Randomized trial to compare bilateral vs. single internal mammary coronary artery bypass grafting: 1-year results of the Arterial Revascularisation Trial (ART).
  - ART 1年 EHJ 2010。試験デザインと初期結果
- ★ **[25217501]** Taggart DP (2015) *Eur J Cardiothorac Surg* — Effects of on-pump and off-pump surgery in the Arterial Revascularization Trial.
  - ★ART内のon-pump/off-pump解析 EJCTS 2015。両テーマの交点
- ★ **[32305186]** Taggart DP (2022) *J Thorac Cardiovasc Surg* — Effect of total arterial grafting in the Arterial Revascularization Trial.
  - ART内の total arterial grafting 効果 (JTCVS 2022)
- ★ **[33413936]** Gaudino M (2021) *J Am Coll Cardiol* — Association of Age With 10-Year Outcomes After Coronary Surgery in the Arterial Revascularization Trial.
  - ART 10年アウトカムと年齢の関連 (JACC 2021, Gaudino)。若年ほど動脈グラフトの利得
- **[34586338]** Gaudino M (2021) *JAMA Cardiol* — Comparison of Long-term Clinical Outcomes of Skeletonized vs Pedicled Internal Thoracic Artery Harvesting Techniques in the Arterial Revascularization Trial.
  - ART: skeletonized vs pedicled ITA の長期比較 (JAMA Cardiol 2021)
- **[28566338]** Taggart DP (2017) *Circulation* — Associations Between Adding a Radial Artery Graft to Single and Bilateral Internal Thoracic Artery Grafts and Outcomes: Insights From the Arterial Revascularization Trial.
  - ART: BITA/SITAへの橈骨動脈追加の効果 (Circulation 2017)
- ★ **[29708851]** Gaudino M (2018) *N Engl J Med* — Radial-Artery or Saphenous-Vein Grafts in Coronary-Artery Bypass Surgery.
  - ★RADIAL patient-level pooled NEJM 2018 (Gaudino)。橈骨動脈 vs 伏在静脈のRCT統合。橈骨動脈優位を確立
- ★ **[32662861]** Gaudino M (2020) *JAMA* — Association of Radial Artery Graft vs Saphenous Vein Graft With Long-term Cardiovascular Outcomes Among Patients Undergoing Coronary Artery Bypass Grafting: A Systematic Review and Meta-analysis.
  - ★Gaudino JAMA 2020。橈骨動脈 vs 伏在静脈の長期臨床アウトカム SR/MA
- ★ **[33017209]** Buxton BF (2020) *Circulation* — Long-Term Results of the RAPCO Trials.
  - ★RAPCO 長期結果 Circulation 2020 (Buxton)。橈骨動脈 vs 右ITA vs 伏在静脈の希少なRCT長期
- **[15564545]** Desai ND (2004) *N Engl J Med* — A randomized comparison of radial-artery and saphenous-vein coronary bypass grafts.
  - Desai NEJM 2004。橈骨動脈 vs 伏在静脈のRCT (RAPS)
- ★ **[31934782]** Gaudino M (2019) *Circulation* — Arterial Grafts for Coronary Bypass: A Critical Review After the Publication of ART and RADIAL.
  - ★Gaudino Circulation 2019「ARTとRADIAL公表後の動脈グラフト批判的レビュー」。この分野の総括に最適
- ★ **[33686866]** Gaudino M (2021) *J Am Heart Assoc* — Angiographic Patency of Coronary Artery Bypass Conduits: A Network Meta-Analysis of Randomized Trials.
  - ★Gaudino JAHA 2021。導管別の血管造影開存率ネットワークメタ解析。開存率の一覧表として実用的
- ★ **[30636525]** Gaudino M (2019) *J Am Heart Assoc* — Radial Artery Versus Right Internal Thoracic Artery Versus Saphenous Vein as the Second Conduit for Coronary Artery Bypass Surgery: A Network Meta-Analysis of Clinical Outcomes.
  - 第2導管としての橈骨動脈 vs 右ITA vs 伏在静脈のネットワークメタ解析 (JAHA 2019)
- ★ **[37535847]** Gaudino M (2023) *Eur J Cardiothorac Surg* — Expert systematic review on the choice of conduits for coronary artery bypass grafting: endorsed by the European Association for Cardio-Thoracic Surgery (EACTS) and The Society of Thoracic Surgeons (STS).
  - ★★EACTS/STS 共同 Expert systematic review「CABGの導管選択」EJCTS 2023 (Gaudino)。現時点の最上位の統合文献
- ★ **[37542480]** Gaudino M (2023) *J Thorac Cardiovasc Surg* — Expert systematic review on the choice of conduits for coronary artery bypass grafting: endorsed by the European Association for Cardio-Thoracic Surgery (EACTS) and The Society of Thoracic Surgeons (STS).
  - 同上のJTCVS版 (内容同一・引用先の使い分け用)
- ★ **[26680310]** Aldea GS (2016) *Ann Thorac Surg* — The Society of Thoracic Surgeons Clinical Practice Guidelines on Arterial Conduits for Coronary Artery Bypass Grafting.
  - ★STS Clinical Practice Guidelines on Arterial Conduits (Ann Thorac Surg 2016, Aldea)。動脈導管の公式ガイドライン
- ★ **[39656609]** Sandner S (2024) *Eur J Cardiothorac Surg* — Intra-operative and post-operative management of conduits for coronary artery bypass grafting: a clinical consensus statement of the European Society of Cardiology Working Group on Cardiovascular Surgery and the European Association for Cardio-Thoracic Surgery Coronary Task Force.
  - ★ESC WG コンセンサス「導管の術中・術後マネジメント」EJCTS 2024 (Sandner)
- ★ **[28119382]** Gaudino M (2017) *Circulation* — Three Arterial Grafts Improve Late Survival: A Meta-Analysis of Propensity-Matched Studies.
  - Gaudino Circulation 2017。3本動脈グラフトが遠隔生存を改善 (PSM研究メタ解析)
- **[32771552]** Saraiva FA (2020) *Int J Cardiol* — Multiple versus single arterial grafting in coronary artery bypass grafting: A meta-analysis of randomized controlled trials and propensity score studies.
  - MAG vs SAG のRCT+PSMメタ解析 (2020)
- **[36394709]** Magouliotis DE (2023) *Gen Thorac Cardiovasc Surg* — Differences in long-term survival outcomes after coronary artery bypass grafting using single vs multiple arterial grafts: a meta-analysis with reconstructed time-to-event data and subgroup analyses.
  - 再構築time-to-eventデータによるSAG vs MAG メタ解析 (2023)
- **[41334602]** Abdillah AH (2026) *Asian Cardiovasc Thorac Ann* — Optimization in long-term survival after multiple arterial grafting in coronary artery bypass: A systematic review and meta-analysis.
  - MAG後の長期生存最適化 SR/MA (2026)
- ★ **[30239376]** Gaudino MFL (2018) *Curr Opin Cardiol* — The ROMA trial: why it is needed.
  - ★ROMA trial: why it is needed (Gaudino 2018)。進行中の決定版RCTの背景
- **[37330205]** Gaudino M (2024) *J Thorac Cardiovasc Surg* — Randomized Comparison of the Outcome of Single Versus Multiple Arterial Grafts trial (ROMA):Women-a trial dedicated to women to improve coronary bypass outcomes.
  - ROMA:Women。女性に特化した派生試験
- **[33779716]** Masterson Creber R (2022) *Eur Heart J Qual Care Clin Outcomes* — Randomized comparison of the clinical Outcome of single versus Multiple Arterial grafts: Quality of Life (ROMA:QOL) - Rationale and Study Protocol.
  - ROMA:QOL プロトコル
- ★ **[39389436]** Rankin JS (2025) *Semin Thorac Cardiovasc Surg* — Techniques and Results of Multiple Arterial Bypass Grafting: Towards More "Curative" Coronary Revascularizations.
  - Rankin 2025「多枝動脈バイパスの手技と成績 — より根治的な血行再建へ」
- ★ **[40348256]** Lamy A (2025) *Ann Thorac Surg* — The Downfall of Right Internal Thoracic Artery as a Second Conduit in Coronary Artery Bypass Surgery.
  - ★Lamy 2025「第2導管としての右ITAの凋落」。RITA再評価の論争。41794094/39938583/41628842/41865963と併読
- ★ **[41628842]** Raja SG (2026) *Ann Thorac Surg* — Reexamining Conduit Selection and Evidence Interpretation in Coronary Artery Surgery.
  - Raja 2026「導管選択とエビデンス解釈の再検討」。上記への反論
- ★ **[41865963]** Lamy A (2026) *Ann Thorac Surg* — Evidence Interpretation in Coronary Artery Surgery: Be Rigorous and Stay With the Evidence.
  - Lamy 2026「エビデンス解釈は厳密に」。上記への再反論。2026年最新の論争
- **[31672179]** Chikwe J (2019) *J Am Coll Cardiol* — Outcomes of Second Arterial Conduits in Patients Undergoing Multivessel Coronary Artery Bypass Graft Surgery.
  - Chikwe JACC 2019。第2動脈導管の実臨床アウトカム
- **[31976863]** Bakaeen FG (2020) *J Am Coll Cardiol* — Coronary Artery Target Selection and Survival After Bilateral Internal Thoracic Artery Grafting.
  - Bakaeen JACC 2020。BITAのターゲット選択と生存
- **[29661948]** Gaudino M (2018) *Circulation* — Continuing Conundrum of Multiple Arterial Conduits for Coronary Artery Bypass Grafting.
  - 多枝動脈導管の『続く難題』(Circulation 2018)
- **[36229295]** Ren J (2024) *J Thorac Cardiovasc Surg* — Long-term observational angiographic patency and perfect patency of radial artery compared with saphenous vein or internal mammary artery in coronary bypass surgery.
  - 橈骨動脈の長期造影開存・perfect patency (JTCVS 2024)

### §6. 伏在静脈グラフト — no-touch・採取法・グラフト不全

- ★ **[30417737]** Zenati MA (2019) *N Engl J Med* — Randomized Trial of Endoscopic or Open Vein-Graft Harvesting for Coronary-Artery Bypass.
  - ★REGROUP NEJM 2019 (Zenati)。内視鏡 vs 直視下静脈採取のRCT。差なし
- ★ **[39969129]** Thelin S (2025) *Eur Heart J* — No-touch vein grafts in coronary artery bypass surgery: a registry-based randomized clinical trial.
  - ★SWEDEGRAFT Eur Heart J 2025 (Thelin)。レジストリベースRCTでのno-touch静脈
- ★ **[40306935]** Tian M (2025) *BMJ* — No-touch versus conventional vein in coronary artery bypass grafting: three year follow-up of multicentre randomised PATENCY trial.
  - ★PATENCY trial 3年 BMJ 2025 (Tian)。no-touch vs 従来法の多施設RCT
- ★ **[40929150]** Sandner S (2025) *Eur J Cardiothorac Surg* — Outcomes of No-Touch Vs Conventionally Harvested Saphenous Veins for Coronary Artery Bypass Surgery: A Meta-Analysis of Randomized Trials.
  - Sandner EJCTS 2025。no-touch vs 従来採取のRCTメタ解析。上記2試験を統合
- ★ **[34460327]** Xenogiannis I (2021) *Circulation* — Saphenous Vein Graft Failure: From Pathophysiology to Prevention and Treatment Strategies.
  - Xenogiannis Circulation 2021「伏在静脈グラフト不全: 病態から予防・治療まで」
- ★ **[31455868]** Caliskan E (2020) *Nat Rev Cardiol* — Saphenous vein grafts in contemporary coronary artery bypass graft surgery.
  - Caliskan Nat Rev Cardiol 2020「現代CABGにおける伏在静脈グラフト」
- ★ **[29084780]** Gaudino M (2017) *Circulation* — Mechanisms, Consequences, and Prevention of Coronary Graft Failure.
  - ★Gaudino Circulation 2017「グラフト不全の機序・帰結・予防」。総説の定番
- ★ **[37417248]** Gaudino M (2023) *Circulation* — Graft Failure After Coronary Artery Bypass Grafting and Its Association With Patient Characteristics and Clinical Events: A Pooled Individual Patient Data Analysis of Clinical Trials With Imaging Follow-Up.
  - ★Gaudino Circulation 2023。RCT統合の個票データによるグラフト不全と臨床イベントの関連
- **[35675092]** Goldstein DJ (2022) *JAMA Cardiol* — External Support for Saphenous Vein Grafts in Coronary Artery Bypass Surgery: A Randomized Clinical Trial.
  - VEST試験 JAMA Cardiol 2022。静脈グラフト外部支持デバイスのRCT
- **[41135855]** Squiers JJ (2026) *Ann Thorac Surg* — All-Venous Grafting and Very Long-Term Survival After Coronary Artery Bypass Grafting.
  - Squiers 2026。全静脈グラフトでの超長期生存
- **[38606620]** Deng MX (2024) *Curr Opin Cardiol* — No-touch saphenous vein: current understanding of the conduit 'less handled'.
  - no-touch伏在静脈の現在の理解 (Curr Opin Cardiol 2024)

### §7. No-touch aorta / anaortic 技術と脳卒中

- ★ **[28231944]** Zhao DF (2017) *J Am Coll Cardiol* — Coronary Artery Bypass Grafting With and Without Manipulation of the Ascending Aorta: A Network Meta-Analysis.
  - ★Zhao JACC 2017。上行大動脈操作の有無別のネットワークメタ解析。anaorticが脳卒中最少。ユーザーの問いの直接回答
- ★ **[21281950]** Misfeld M (2011) *J Thorac Cardiovasc Surg* — Neurologic complications after off-pump coronary artery bypass grafting with and without aortic manipulation: meta-analysis of 11,398 cases from 8 studies.
  - Misfeld JTCVS 2011。大動脈操作あり/なしの神経合併症メタ解析 (11,398例)
- ★ **[26892526]** Pawliszak W (2016) *J Am Heart Assoc* — Cerebrovascular Events After No-Touch Off-Pump Coronary Artery Bypass Grafting, Conventional Side-Clamp Off-Pump Coronary Artery Bypass, and Proximal Anastomotic Devices: A Meta-Analysis.
  - Pawliszak JAHA 2016。no-touch OPCAB vs サイドクランプ vs 近位吻合デバイスの脳血管イベント比較
- ★ **[34977717]** Vallely MP (2021) *JTCVS Tech* — Total-arterial, anaortic, off-pump coronary artery surgery: Why, when, and how.
  - ★Vallely JTCVS Tech 2021「Total-arterial, anaortic, off-pump: なぜ・いつ・どのように」。実践の指針
- ★ **[33502822]** Ramponi F (2021) *J Card Surg* — Toward stroke-free coronary surgery: The role of the anaortic off-pump bypass technique.
  - Ramponi 2021「脳卒中ゼロの冠動脈外科へ: anaortic off-pumpの役割」
- ★ **[41619278]** Prapas S (2026) *Eur J Cardiothorac Surg* — Anaortic Coronary Artery Bypass Grafting With and Without Saphenous Vein: 20-Year Clinical Results.
  - ★Prapas EJCTS 2026。anaortic CABG の20年臨床成績 (静脈併用あり/なし)
- **[31504374]** Sandner SE (2020) *Eur J Cardiothorac Surg* — Routine preoperative aortic computed tomography angiography is associated with reduced risk of stroke in coronary artery bypass grafting: a propensity-matched analysis.
  - 術前大動脈CTAが脳卒中を減らす (EJCTS 2020, Sandner)
- **[8837572]** Dávila-Román VG (1996) *J Am Coll Cardiol* — Intraoperative transesophageal echocardiography and epiaortic ultrasound for assessment of atherosclerosis of the thoracic aorta.
  - Dávila-Román JACC 1996。術中TEE/epiaortic超音波による大動脈粥腫評価。古典
- **[12970201]** Sharony R (2003) *Circulation* — Off-pump coronary artery bypass grafting reduces mortality and stroke in patients with atheromatous aortas: a case control study.
  - 粥腫性大動脈症例でoff-pumpが死亡・脳卒中を減らす (Circulation 2003)
- **[21420873]** Biancari F (2011) *Eur J Cardiothorac Surg* — Meta-analysis on the use of the Heartstring anastomotic device to prevent stroke in patients undergoing off-pump coronary artery bypass grafting.
  - HEARTSTRING近位吻合デバイスのメタ解析
- **[33002935]** Weiss AJ (2020) *Curr Opin Cardiol* — Temporal improvements in perioperative stroke rates following coronary artery bypass grafting.
  - CABG後脳卒中率の経時的改善 (Curr Opin Cardiol 2020)
- **[40725570]** Plonek T (2025) *J Clin Med* — No-Touch Aorta Off-Pump LIMA-Radial Artery Y-Graft CABG as a Safe Strategy for All-Comers: Long-Term Survival.
  - No-touch aorta LIMA-橈骨動脈Y-graftの長期生存 (2025)

### §8. 血行再建の完全性 (Incomplete Revascularization)

- ★ **[33067581]** Gaba P (2021) *Nat Rev Cardiol* — Complete versus incomplete coronary revascularization: definitions, assessment and outcomes.
  - ★Gaba Nat Rev Cardiol 2021「完全 vs 不完全血行再建: 定義・評価・アウトカム」。定義論の決定版
- ★ **[23747787]** Garcia S (2013) *J Am Coll Cardiol* — Outcomes after complete versus incomplete revascularization of patients with multivessel coronary artery disease: a meta-analysis of 89,883 patients enrolled in randomized clinical trials and observational studies.
  - Garcia JACC 2013。89,883例のメタ解析
- ★ **[29407133]** Benedetto U (2018) *Int J Cardiol* — Incomplete revascularization and long-term survival after coronary artery bypass surgery.
  - Benedetto Int J Cardiol 2018。CABG後の不完全血行再建と長期生存
- ★ **[30686645]** Thakur U (2020) *Heart Lung Circ* — Off- vs. On-Pump Coronary Artery Bypass Grafting Long-Term Survival is Driven by Incompleteness of Revascularisation.
  - ★Thakur 2020「off vs on の長期生存差は血行再建の不完全性で説明される」。ユーザーのHR 1.33論の直接根拠
- ★ **[30094210]** Leviner DB (2018) *Ann Cardiothorac Surg* — Incomplete revascularization: what the surgeon needs to know.
  - Leviner Ann Cardiothorac Surg 2018「外科医が知るべき不完全血行再建」
- **[38266796]** Belyayev L (2024) *Am J Cardiol* — Complete Coronary Revascularization and Outcomes in Patients Who Underwent Coronary Artery Bypass Grafting: Insights from The REGROUP Trial.
  - REGROUP試験における完全血行再建の解析 (2024)
- **[39144317]** Rufa MI (2024) *J Thorac Dis* — The impact of incomplete revascularization on survival in minimal invasive off-pump coronary artery surgery: a propensity score analysis of 1,149 cases.
  - 低侵襲off-pumpでの不完全血行再建の生存影響 (2024)
- **[17140968]** Lim E (2006) *J Thorac Cardiovasc Surg* — A systematic review of randomized trials comparing revascularization rate and graft patency of off-pump and conventional coronary surgery.
  - Lim JTCVS 2006。off vs on の血行再建率とグラフト開存のSR
- **[30369591]** Lee Y (2018) *Circ J* — Impact of Complete Revascularization on Long-Term Outcomes After Coronary Artery Bypass Grafting in Patients With Left Ventricular Dysfunction.
  - 左室機能低下例での完全血行再建の意義 (Circ J 2018)

### §9. 術中グラフト評価 (TTFM / FFR)

- ★ **[34606302]** Gaudino M (2021) *Circulation* — The Use of Intraoperative Transit Time Flow Measurement for Coronary Artery Bypass Surgery: Systematic Review of the Evidence and Expert Opinion Statements.
  - ★Gaudino Circulation 2021。術中TTFMのSRとエキスパート意見声明。標準化文書
- ★ **[30907418]** Thuijs DJFM (2019) *Eur J Cardiothorac Surg* — Improving coronary artery bypass grafting: a systematic review and meta-analysis on the impact of adopting transit-time flow measurement.
  - Thuijs EJCTS 2019。TTFM導入の影響 SR/MA
- **[27298393]** Niclauss L (2017) *Eur J Cardiothorac Surg* — Techniques and standards in intraoperative graft verification by transit time flow measurement after coronary artery bypass graft surgery: a critical review.
  - TTFMの手技と基準の批判的レビュー (EJCTS 2017)
- **[34166508]** Rosenfeld ES (2021) *Eur J Cardiothorac Surg* — Intraoperative transit-time flow measurement and high-frequency ultrasound in coronary artery bypass grafting: impact in off versus on-pump, arterial versus venous grafting and cardiac territory grafted.
  - off vs on / 動脈 vs 静脈でのTTFMと高周波エコー (EJCTS 2021)
- **[36276694]** Leviner DB (2022) *JTCVS Tech* — Graft flow evaluation with intraoperative transit-time flow measurement in off-pump versus on-pump coronary artery bypass grafting.
  - off-pump vs on-pump のグラフト血流評価 (JTCVS Tech 2022)
- ★ **[34735046]** Fearon WF (2022) *N Engl J Med* — Fractional Flow Reserve-Guided PCI as Compared with Coronary Bypass Surgery.
  - ★FAME 3 NEJM 2022 (Fearon)。FFRガイドPCI vs CABG
- ★ **[40174598]** Fearon WF (2025) *Lancet* — Outcomes after fractional flow reserve-guided percutaneous coronary intervention versus coronary artery bypass grafting (FAME 3): 5-year follow-up of a multicentre, open-label, randomised trial.
  - ★FAME 3 5年 Lancet 2025。CABG優位が持続
- **[34078097]** Thuesen AL (2021) *Circ Cardiovasc Qual Outcomes* — Health-Related Quality of Life and Angina in Fractional Flow Reserve- Versus Angiography-Guided Coronary Artery Bypass Grafting: FARGO Trial (Fractional Flow Reserve Versus Angiography Randomization for Graft Optimization).
  - FARGO試験。FFRガイド vs 造影ガイドCABG
- **[32167555]** Jayakumar S (2020) *Interact Cardiovasc Thorac Surg* — The role of fractional flow reserve in coronary artery bypass graft surgery: a meta-analysis.
  - CABGにおけるFFRの役割メタ解析 (2020)
- **[40376846]** Hansson EC (2025) *Eur Heart J* — Coronary artery bypass grafting with or without preoperative physiological stenosis assessment: a SWEDEHEART study.
  - SWEDEHEART: 術前生理学的評価の有無 (EHJ 2025)

### §10. ロボット支援CABG / MICS-CABG / ハイブリッド

- ★ **[33841980]** Bonatti J (2021) *J Thorac Dis* — Minimally invasive and robotic coronary artery bypass grafting-a 25-year review.
  - ★Bonatti J Thorac Dis 2021「低侵襲・ロボットCABGの25年レビュー」
- ★ **[40434908]** Walton AJ (2025) *Eur J Cardiothorac Surg* — Review of minimally invasive coronary artery bypass grafting.
  - ★Walton EJCTS 2025「低侵襲CABGのレビュー」最新総説
- ★ **[42301235]** Hassan SMA (2026) *Curr Opin Cardiol* — Minimally invasive approaches to coronary artery bypass grafting: techniques, current evidence, and future directions.
  - Hassan Curr Opin Cardiol 2026「MICS CABG: 手技・現行エビデンス・今後」最新
- ★ **[39116933]** Nisivaco S (2025) *J Thorac Cardiovasc Surg* — A decade of robotic beating-heart totally endoscopic coronary bypass (TECAB) at a single institution: Outcomes with 10-year follow-up.
  - ★Nisivaco JTCVS 2025。単施設ロボットbeating-heart TECAB 10年追跡
- ★ **[39157183]** Nisivaco S (2024) *Ann Cardiothorac Surg* — Bilateral internal thoracic artery grafting in robotic beating-heart totally endoscopic coronary artery bypass: 10-year outcomes.
  - ロボットbeating-heart TECABにおけるBITA 10年成績 (2024)
- ★ **[34890572]** Balkhy HH (2022) *Ann Thorac Surg* — Robotic Total Endoscopic Coronary Bypass in 570 Patients: Impact of Anastomotic Technique in Two Eras.
  - Balkhy Ann Thorac Surg 2022。ロボットTECAB 570例・吻合法2時代の比較
- ★ **[39567250]** Zoupas I (2024) *Innovations (Phila)* — Totally Endoscopic Coronary Artery Bypass Graft: Systematic Review and Meta-Analysis of Reconstructed Patient-Level Data.
  - Zoupas Innovations 2024。TECABの再構築個票データSR/MA
- **[29657055]** Leonard JR (2018) *Int J Cardiol* — Totally endoscopic coronary artery bypass surgery: A meta-analysis of the current evidence.
  - Leonard Int J Cardiol 2018。TECABメタ解析
- **[33155975]** Hammal F (2020) *Can J Surg* — Robot-assisted coronary artery bypass surgery: a systematic review and meta-analysis of comparative studies.
  - ロボット支援CABGの比較研究SR/MA (2020)
- **[30885092]** Kitahara H (2019) *Innovations (Phila)* — Graft Patency after Robotically Assisted Coronary Artery Bypass Surgery.
  - ロボット支援CABG後のグラフト開存 (Innovations 2019)
- ★ **[35429509]** Dixon LK (2022) *Int J Cardiol* — Hybrid coronary revascularization versus coronary artery bypass grafting for multivessel coronary artery disease: A systematic review and meta-analysis.
  - Dixon Int J Cardiol 2022。ハイブリッド血行再建 vs CABG のSR/MA
- **[38008347]** Shimamura J (2024) *Am J Cardiol* — Long-Term Outcomes After Hybrid Coronary Revascularization Versus Coronary Artery Bypass Grafting: Meta-Analysis of Kaplan-Meier-Derived Data.
  - ハイブリッド vs CABG の長期アウトカム (KM再構築メタ解析 2024)
- **[38677447]** Willard R (2024) *Ann Thorac Surg* — The Current State of Hybrid Coronary Revascularization.
  - Willard Ann Thorac Surg 2024「ハイブリッド血行再建の現状」
- **[29680218]** Tajstra M (2018) *JACC Cardiovasc Interv* — Hybrid Coronary Revascularization in Selected Patients With Multivessel Disease: 5-Year Clinical Outcomes of the Prospective Randomized Pilot Study.
  - POL-MIDES ハイブリッドRCT 5年 (JACC Interv 2018)
- **[31826727]** Hage A (2019) *J Am Heart Assoc* — Hybrid Coronary Revascularization Versus Off-Pump Coronary Artery Bypass Grafting: Comparative Effectiveness Analysis With Long-Term Follow-up.
  - ハイブリッド vs OPCAB の長期比較 (JAHA 2019)
- **[36130278]** Manuel L (2022) *Interact Cardiovasc Thorac Surg* — LIMA to LAD grafting returns patient survival to age-matched population: 20-year outcomes of MIDCAB surgery.
  - MIDCAB 20年成績。LIMA-LADで年齢調整集団と同等の生存
- **[32818539]** Mastroiacovo G (2021) *Ann Thorac Surg* — Very Long-term Outcome of Minimally Invasive Direct Coronary Artery Bypass.
  - MIDCABの超長期成績 (Ann Thorac Surg 2021)
- **[39434975]** Algoet M (2024) *Ann Cardiothorac Surg* — How to advance from minimally invasive coronary artery bypass grafting to totally endoscopic coronary bypass grafting: challenges in Europe versus United States of America.
  - MICS-CABGからTECABへ進む道: 欧州 vs 米国の課題 (2024)
- ★ **[30474417]** Gaudino M (2018) *Circulation* — New Strategies for Surgical Myocardial Revascularization.
  - Gaudino Circulation 2018「外科的心筋血行再建の新戦略」

### §11. 教育・トレーニング・サブスペシャリティ化

- ★ **[39733961]** Kiaii B (2025) *Semin Thorac Cardiovasc Surg* — CABG Should Be a Subspecialty.
  - ★★Kiaii Semin Thorac Cardiovasc Surg 2025「CABG Should Be a Subspecialty」。ユーザーの『冠動脈外科専門医』論の直球文献
- ★ **[39730082]** Razavi AA (2025) *Semin Thorac Cardiovasc Surg* — Off-Pump Coronary Artery Bypass Grafting is Overutilized.
  - ★★Razavi Semin Thorac Cardiovasc Surg 2025「OPCABは過剰使用されている」。上記と同誌の対論。必ず対で読む
- ★ **[42236427]** Sidik AI (2026) *J Surg Educ* — Simulation-Based Training for Coronary Artery Bypass Grafting: Systematic Review and Meta-analysis.
  - ★★Sidik J Surg Educ 2026「CABGのシミュレーショントレーニング: SR/MA」。11研究372名、技術スコアSMD 2.18・吻合時間SMD 2.00。ユーザーの『2,000回吻合』的な定量指標を探す出発点
- ★ **[34337649]** Whittaker G (2021) *Eur J Cardiothorac Surg* — Recommendations for the use of coronary and valve simulators in cardiac surgical training: a systematic review.
  - ★Whittaker EJCTS 2021「冠動脈・弁シミュレータ使用の推奨」SR。カリキュラム設計の実務文書
- ★ **[35143631]** O'Dwyer M (2022) *BJS Open* — Objective improvement with coronary anastomosis simulation training: meta-analysis.
  - O'Dwyer BJS Open 2022。冠動脈吻合シミュレーション訓練の客観的改善メタ解析
- ★ **[35900153]** Hussein N (2022) *Interact Cardiovasc Thorac Surg* — The use of objective assessments in the evaluation of technical skills in cardiothoracic surgery: a systematic review.
  - Hussein 2022。心臓血管外科の技術評価における客観的指標のSR。評価尺度の一覧
- ★ **[42301733]** Reed GW (2026) *Eur Heart J* — Simulation-based training in cardiovascular intervention and cardiac surgery: bridging skill, safety, and innovation.
  - Reed Eur Heart J 2026「循環器インターベンションと心臓外科のシミュレーション訓練」最新総説
- ★ **[41619927]** Badhwar V (2026) *Ann Thorac Surg* — The Society of Thoracic Surgeons Expert Consensus Pathway for Robotic Cardiac Surgical Training.
  - ★★Badhwar Ann Thorac Surg 2026「STS Expert Consensus Pathway for Robotic Cardiac Surgical Training」。4フェーズの公式訓練パスウェイ。ユーザーの『米国の認定カリキュラム』の直接回答
- ★ **[34474026]** Amabile A (2021) *Ann Thorac Surg* — Off-Pump Coronary Artery Bypass Grafting: How I Teach It.
  - ★Amabile Ann Thorac Surg 2021「OPCAB: How I Teach It」。指導法の具体
- ★ **[39157180]** Sutter FP (2024) *Ann Cardiothorac Surg* — Robotic-assisted coronary artery bypass grafting: how I teach it.
  - Sutter Ann Cardiothorac Surg 2024「ロボット支援CABG: how I teach it」
- ★ **[39157181]** Jonsson AA (2024) *Ann Cardiothorac Surg* — Teaching the next generation of robotic coronary surgeons.
  - Jonsson 2024「次世代ロボット冠動脈外科医を教える」
- ★ **[39209092]** Halkos ME (2025) *Ann Thorac Surg* — Developing Proficiency in Robotic Cardiac Surgery.
  - Halkos Ann Thorac Surg 2025「ロボット心臓外科の習熟」
- ★ **[36848999]** Jonsson A (2023) *Ann Thorac Surg* — Mastering the Learning Curve for Robotic-Assisted Coronary Artery Bypass Surgery.
  - Jonsson Ann Thorac Surg 2023「ロボット支援CABGのラーニングカーブ攻略」
- ★ **[41025333]** Sarfaraz ZK (2025) *Curr Opin Cardiol* — Teaching minimally invasive coronary artery bypass grafting: a structured framework for well tolerated adoption and training.
  - Sarfaraz Curr Opin Cardiol 2025「MICS-CABGの教育: 導入のための構造化フレームワーク」
- ★ **[38580041]** Comanici M (2024) *Am J Cardiol* — Trainee Perceptions of Off-Pump Coronary Artery Bypass Grafting: United Kingdom Training Needs Survey.
  - ★Comanici Am J Cardiol 2024「OPCABに対する研修医の認識: 英国トレーニングニーズ調査」。教育体制の不備の実証データ
- ★ **[42266981]** Raja SG (2026) *Ann Thorac Surg Short Rep* — Ten Commandments of Off-Pump Coronary Artery Bypass Surgery.
  - ★Raja 2026「OPCABの十戒」。技術の言語化・教育用の要点集
- ★ **[26707761]** Virk SA (2016) *J Thorac Cardiovasc Surg* — Equivalent outcomes after coronary artery bypass graft surgery performed by consultant versus trainee surgeons: A systematic review and meta-analysis.
  - Virk JTCVS 2016。指導医 vs 研修医のCABG成績SR/MA。教育と安全性の両立
- **[22698772]** Bakaeen FG (2012) *Ann Thorac Surg* — Coronary artery bypass graft patency: residents versus attending surgeons.
  - Bakaeen Ann Thorac Surg 2012。研修医 vs 指導医のグラフト開存
- **[26470910]** Almassi GH (2015) *J Thorac Cardiovasc Surg* — Resident versus attending surgeon graft patency and clinical outcomes in on- versus off-pump coronary artery bypass surgery.
  - ROOBY内での研修医 vs 指導医比較 (JTCVS 2015)
- **[36098376]** Comanici M (2022) *J Card Surg* — Are there differences in cardiothoracic surgery performed by trainees versus fully trained surgeons?
  - 研修医と指導医の心臓外科手術の差 (J Card Surg 2022)
- **[41121332]** Vo AT (2025) *J Cardiothorac Surg* — Learning curve in off-pump coronary artery bypass graft surgery in a low-income country: a single-center experience.
  - 低所得国におけるOPCABのラーニングカーブ (2025)
- **[31394563]** Yanagawa B (2019) *Curr Opin Cardiol* — See one, simulate many, do one, teach one: cardiac surgical simulation.
  - Yanagawa 2019「See one, simulate many, do one, teach one」心臓外科シミュレーション
- **[42188066]** Nameghi FH (2026) *J Cardiovasc Dev Dis* — Simulation Training in Video-Assisted and Robotic-Assisted Cardiac Surgery: A Narrative Review.
  - ビデオ支援・ロボット心臓外科のシミュレーション訓練 (2026)

### §12. 至適薬物療法 (OMT) — 抗血小板・脂質

- ★ **[40884067]** Sandner S (2026) *Eur Heart J* — Antithrombotic therapy after coronary artery bypass graft surgery: a Clinical Consensus Statement of the ESC Working Group on Cardiovascular Surgery, the ESC Working Group on Cardiovascular Pharmacotherapy, and the European Association for Cardio-Thoracic Surgery (EACTS).
  - ★★Sandner Eur Heart J 2026「CABG後の抗血栓療法」ESC WG臨床コンセンサス声明。最新の到達点
- ★ **[40884083]** Sandner S (2025) *Eur J Cardiothorac Surg* — Antithrombotic therapy after coronary artery bypass graft surgery: a Clinical Consensus Statement of the ESC Working Group on Cardiovascular Surgery, the ESC Working Group on Cardiovascular Pharmacotherapy, and the European Association for Cardio-Thoracic Surgery (EACTS).
  - 同コンセンサスのEJCTS版
- ★ **[40888737]** Jeppsson A (2025) *N Engl J Med* — Ticagrelor and Aspirin or Aspirin Alone after Coronary Surgery for Acute Coronary Syndrome.
  - ★★Jeppsson NEJM 2025 (TACSI)。ACS後CABGでのチカグレロル+アスピリン vs アスピリン単独。大規模RCT最新
- ★ **[29710164]** Zhao Q (2018) *JAMA* — Effect of Ticagrelor Plus Aspirin, Ticagrelor Alone, or Aspirin Alone on Saphenous Vein Graft Patency 1 Year After Coronary Artery Bypass Grafting: A Randomized Clinical Trial.
  - ★DACAB JAMA 2018 (Zhao)。3群比較でのSVG開存
- ★ **[38862179]** Zhu Y (2024) *BMJ* — Antiplatelet therapy after coronary artery bypass surgery: five year follow-up of randomised DACAB trial.
  - ★DACAB 5年追跡 BMJ 2024。臨床イベントへの波及
- ★ **[32862716]** Willemsen LM (2020) *Circulation* — Effect of Adding Ticagrelor to Standard Aspirin on Saphenous Vein Graft Patency in Patients Undergoing Coronary Artery Bypass Grafting (POPular CABG): A Randomized, Double-Blind, Placebo-Controlled Trial.
  - POPular CABG Circulation 2020。アスピリンへのチカグレロル追加
- ★ **[35943473]** Sandner S (2022) *JAMA* — Association of Dual Antiplatelet Therapy With Ticagrelor With Vein Graft Failure After Coronary Artery Bypass Graft Surgery: A Systematic Review and Meta-analysis.
  - Sandner JAMA 2022。チカグレロルDAPTと静脈グラフト不全のSR/MA
- ★ **[31601578]** Solo K (2019) *BMJ* — Antithrombotic treatment after coronary artery bypass graft surgery: systematic review and network meta-analysis.
  - Solo BMJ 2019。CABG後抗血栓療法のネットワークメタ解析
- ★ **[40907505]** Verma S (2025) *Lancet* — Effect of evolocumab on saphenous vein graft patency after coronary artery bypass surgery (NEWTON-CABG CardioLink-5): an international, randomised, double-blind, placebo-controlled trial.
  - ★★Verma Lancet 2025 (NEWTON-CABG CardioLink-5)。エボロクマブによるSVG開存改善を検証した初のRCT。脂質管理×外科の交点
- ★ **[31865057]** Alkhalil M (2020) *Atherosclerosis* — Effects of intensive lipid-lowering therapy on mortality after coronary bypass surgery: A meta-analysis of 7 randomised trials.
  - Alkhalil 2020。CABG後の強力な脂質低下療法と死亡のメタ解析 (7 RCT)
- **[34555373]** Jang YH (2022) *Ann Thorac Surg* — Effects of Statin Intensity on Long-term Outcomes After Coronary Artery Bypass Grafting.
  - スタチン強度と長期アウトカム (Ann Thorac Surg 2022)
- ★ **[38456874]** Moshkovitz Y (2024) *Mayo Clin Proc* — Emulated Trial for Discharge Prescription of Guideline-Directed Medical Therapy and 15-Year Survival After Coronary Artery Bypass Graft Surgery.
  - ★Moshkovitz Mayo Clin Proc 2024。退院時GDMT処方と15年生存のtarget trial emulation。OMTの寄与を定量
- ★ **[29420954]** Pinho-Gomes AC (2018) *J Am Coll Cardiol* — Compliance With Guideline-Directed Medical Therapy in Contemporary Coronary Revascularization Trials.
  - ★Pinho-Gomes JACC 2018。現代の血行再建RCTにおけるGDMT遵守率。『内科治療の進化が外科試験を薄める』論の根拠
- ★ **[34138766]** Eikelboom R (2021) *Curr Opin Cardiol* — Optimal medical therapy after coronary artery bypass grafting: a primer for surgeons.
  - Eikelboom Curr Opin Cardiol 2021「CABG後の至適薬物療法: 外科医のための入門」実務的
- **[33038121]** Paquin A (2020) *Curr Opin Cardiol* — Secondary prevention after CABG: do new agents change the paradigm?
  - Paquin 2020「CABG後の二次予防: 新薬はパラダイムを変えるか」
- **[34710343]** Verma S (2021) *Circulation* — Icosapent Ethyl Reduces Ischemic Events in Patients With a History of Previous Coronary Artery Bypass Grafting: REDUCE-IT CABG.
  - REDUCE-IT CABG (Circulation 2021)。イコサペント酸エチル
- **[39566870]** Verma S (2025) *J Am Coll Cardiol* — Semaglutide Improves Cardiovascular Outcomes in Patients With History of Coronary Artery Bypass Graft and Obesity.
  - セマグルチドとCABG既往患者の心血管アウトカム (JACC 2025)
- **[30654882]** Lamy A (2019) *J Am Coll Cardiol* — Rivaroxaban, Aspirin, or Both to Prevent Early Coronary Bypass Graft Occlusion: The COMPASS-CABG Study.
  - COMPASS-CABG (JACC 2019, Lamy)。リバーロキサバン
- **[37086268]** Liakopoulos OJ (2023) *Eur Heart J* — Statin loading before coronary artery bypass grafting: a randomized trial.
  - CABG前スタチンローディングRCT (EHJ 2023)
- ★ **[39385505]**  (2024) *Eur J Cardiothorac Surg* — 2024 EACTS Guidelines on perioperative medication in adult cardiac surgery.
  - ★2024 EACTS Guidelines on perioperative medication in adult cardiac surgery。周術期薬物の公式指針

### §13. CABG vs PCI — 意思決定の文脈

- ★ **[31488373]** Thuijs DJFM (2019) *Lancet* — Percutaneous coronary intervention versus coronary artery bypass grafting in patients with three-vessel or left main coronary artery disease: 10-year follow-up of the multicentre randomised controlled SYNTAX trial.
  - ★SYNTAX 10年 Lancet 2019 (Thuijs)
- ★ **[23439102]** Mohr FW (2013) *Lancet* — Coronary artery bypass graft surgery versus percutaneous coronary intervention in patients with three-vessel disease and left main coronary disease: 5-year follow-up of the randomised, clinical SYNTAX trial.
  - SYNTAX 5年 Lancet 2013
- **[19228612]** Serruys PW (2009) *N Engl J Med* — Percutaneous coronary intervention versus coronary-artery bypass grafting for severe coronary artery disease.
  - SYNTAX 本体 NEJM 2009 (Serruys)
- ★ **[31562798]** Stone GW (2019) *N Engl J Med* — Five-Year Outcomes after PCI or CABG for Left Main Coronary Disease.
  - ★EXCEL 5年 NEJM 2019 (Stone)
- ★ **[34793745]** Sabatine MS (2021) *Lancet* — Percutaneous coronary intervention with drug-eluting stents versus coronary artery bypass grafting in left main coronary artery disease: an individual patient data meta-analysis.
  - ★★Sabatine Lancet 2021。左主幹部の個票データメタ解析 (4 RCT)
- ★ **[29478841]** Head SJ (2018) *Lancet* — Mortality after coronary artery bypass grafting versus percutaneous coronary intervention with stenting for coronary artery disease: a pooled analysis of individual patient data.
  - ★Head Lancet 2018。CABG vs PCIの死亡に関する個票プール解析
- ★ **[27040723]** Velazquez EJ (2016) *N Engl J Med* — Coronary-Artery Bypass Surgery in Patients with Ischemic Cardiomyopathy.
  - ★STICHES NEJM 2016 (Velazquez)。虚血性心筋症でのCABG 10年
- ★ **[40404111]** White HD (2025) *Am Heart J* — Use of coronary artery bypass graft surgery and percutaneous coronary intervention and associated outcomes in the ISCHEMIA trial.
  - ISCHEMIA試験内でのCABG/PCI使用と成績 (Am Heart J 2025)
- **[39432255]** Bangalore S (2024) *EuroIntervention* — Outcomes with revascularisation versus conservative management of participants with 3-vessel coronary artery disease in the ISCHEMIA trial.
  - ISCHEMIA 3枝病変サブ解析 (2024)
- ★ **[36094460]** Yan W (2022) *Curr Opin Cardiol* — It's not all about ISCHEMIA: the case for coronary artery bypass grafting in stable coronary artery disease.
  - Yan 2022「ISCHEMIAだけが全てではない: 安定冠動脈疾患におけるCABGの論拠」外科側の反論
- ★ **[37121245]** Gaudino M (2023) *Lancet* — Current concepts in coronary artery revascularisation.
  - ★★Gaudino Lancet 2023「Current concepts in coronary artery revascularisation」。現時点の最良の総説
- ★ **[34611327]** Beerkens FJ (2022) *Nat Rev Cardiol* — Contemporary coronary artery bypass graft surgery and subsequent percutaneous revascularization.
  - ★Beerkens Nat Rev Cardiol 2022「現代のCABGとその後のPCI」
- ★ **[37348857]** Kageyama S (2023) *Eur J Cardiothorac Surg* — Impact of on-pump and off-pump coronary artery bypass grafting on 10-year mortality versus percutaneous coronary intervention.
  - Kageyama EJCTS 2023。on/off-pump CABG vs PCI の10年死亡
- **[40947142]** Kawczynski MJ (2026) *Heart* — Revascularisation strategies for non-acute myocardial ischaemic syndromes.
  - 非急性心筋虚血症候群の血行再建戦略 (Heart 2026, ネットワークメタ解析)
- **[41714707]** Chiu N (2026) *Nat Rev Cardiol* — Invasive and medical management approaches to non-acute myocardial ischaemic syndromes.
  - Chiu Nat Rev Cardiol 2026「非急性心筋虚血症候群への侵襲的・内科的アプローチ」最新

### §14. ガイドライン・コンセンサス (現行版)

- ★ **[34882435]** Lawton JS (2022) *Circulation* — 2021 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines.
  - ★★2021 ACC/AHA/SCAI Coronary Artery Revascularization Guideline (Circulation)。米国現行版
- ★ **[34895950]**  (2022) *J Am Coll Cardiol* — 2021 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines.
  - 同JACC版 (Systematic Review併載)
- ★ **[30165437]** Neumann FJ (2019) *Eur Heart J* — 2018 ESC/EACTS Guidelines on myocardial revascularization.
  - ★★2018 ESC/EACTS Guidelines on myocardial revascularization (EHJ)。欧州の血行再建専用ガイドライン最新版
- ★ **[30165632]** Sousa-Uva M (2019) *Eur J Cardiothorac Surg* — 2018 ESC/EACTS Guidelines on myocardial revascularization.
  - 同EJCTS版
- ★ **[39210710]** Vrints C (2024) *Eur Heart J* — 2024 ESC Guidelines for the management of chronic coronary syndromes.
  - ★★2024 ESC Guidelines for the management of chronic coronary syndromes。血行再建の推奨を更新
- ★ **[40900620]** Milojevic M (2025) *Curr Opin Cardiol* — Invasive treatment strategies in the ESC guidelines developed in collaboration with EACTS for the management of chronic coronary syndrome: implications for contemporary clinical practice.
  - Milojevic 2025。2024 ESC/EACTS CCSガイドラインの侵襲的治療戦略の臨床実装解説
- ★ **[37471501]** Virani SS (2023) *Circulation* — 2023 AHA/ACC/ACCP/ASPC/NLA/PCNA Guideline for the Management of Patients With Chronic Coronary Disease: A Report of the American Heart Association/American College of Cardiology Joint Committee on Clinical Practice Guidelines.
  - 2023 AHA/ACC Chronic Coronary Disease Guideline
- ★ **[40014670]** Rao SV (2025) *Circulation* — 2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for the Management of Patients With Acute Coronary Syndromes: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines.
  - 2025 ACC/AHA ACS Guideline
- ★ **[37632756]** Byrne RA (2023) *Eur Heart J* — 2022 Joint ESC/EACTS review of the 2018 guideline recommendations on the revascularization of left main coronary artery disease in patients at low surgical risk and anatomy suitable for PCI or CABG.
  - ★2022 Joint ESC/EACTS review of 2018 LM recommendations (EHJ)。左主幹部推奨の再検討
- ★ **[34272070]** Bakaeen FG (2021) *J Thorac Cardiovasc Surg* — 2021: The American Association for Thoracic Surgery Expert Consensus Document: Coronary artery bypass grafting in patients with ischemic cardiomyopathy and heart failure.
  - ★AATS 2021 Expert Consensus: 虚血性心筋症・心不全におけるCABG
- **[38420786]** Gaudino M (2024) *Eur J Cardiothorac Surg* — European Association of Cardio-Thoracic Surgery (EACTS) expert consensus statement on perioperative myocardial infarction after cardiac surgery.
  - EACTS 2024 コンセンサス: 心臓手術後の周術期心筋梗塞
- **[22070836]** Hillis LD (2011) *J Am Coll Cardiol* — 2011 ACCF/AHA Guideline for Coronary Artery Bypass Graft Surgery. A report of the American College of Cardiology Foundation/American Heart Association Task Force on Practice Guidelines. Developed in collaboration with the American Association for Thoracic Surgery, Society of Cardiovascular Anesthesiologists, and Society of Thoracic Surgeons.
  - 2011 ACCF/AHA CABG Guideline。CABG専用の最後の米国版。歴史的参照
- **[15337239]** Eagle KA (2004) *J Am Coll Cardiol* — ACC/AHA 2004 guideline update for coronary artery bypass graft surgery: summary article. A report of the American College of Cardiology/American Heart Association Task Force on Practice Guidelines (Committee to Update the 1999 Guidelines for Coronary Artery Bypass Graft Surgery).
  - ACC/AHA 2004 CABG guideline update。歴史的参照

### §15. OPCABの現在地 — 論争・立場表明・実践

- ★ **[39730082]** Razavi AA (2025) *Semin Thorac Cardiovasc Surg* — Off-Pump Coronary Artery Bypass Grafting is Overutilized.
  - 再掲: 「OPCABは過剰使用」(2025)
- ★ **[31219874]** Raja SG (2019) *Curr Opin Cardiol* — Total arterial off-pump coronary revascularization: The Holy Grail?
  - Raja Curr Opin Cardiol 2019「Total arterial off-pump: 聖杯か?」
- ★ **[40268129]** Comanici M (2025) *Am J Cardiol* — Comparison of Outcomes Between Total Arterial Off-Pump Versus On-Pump Coronary Artery Bypass Surgery: A Meta-Analysis and Meta-Regression.
  - ★Comanici Am J Cardiol 2025。Total arterial off-pump vs on-pump のメタ解析・メタ回帰。MAG×OPCABの交点
- **[27942401]** Raja SG (2016) *J Thorac Dis* — Two decades of off-pump coronary artery bypass surgery: Harefield experience.
  - Raja 2016「off-pump 20年: Harefieldの経験」。25年コホートの前身
- **[31549144]** Raja SG (2020) *Eur J Cardiothorac Surg* — On-pump and off-pump coronary artery bypass grafting for patients needing at least two grafts: comparative outcomes at 20 years.
  - Raja EJCTS 2020。2枝以上を要する患者の20年比較
- **[42027519]** Comanici M (2026) *Ann Thorac Surg Short Rep* — A 27-Year Comparative Analysis of Off-Pump and On-Pump Coronary Artery Bypass Grafting in Octogenarians.
  - Comanici 2026。八十歳代における27年比較
- ★ **[27942402]** Taggart DP (2016) *J Thorac Dis* — Off-pump coronary artery bypass grafting (OPCABG)-a 'personal' European perspective.
  - Taggart 2016「OPCABG — 個人的な欧州の視点」
- **[25237626]** Raja SG (2014) *World J Methodol* — Off-pump coronary artery bypass grafting: Misperceptions and misconceptions.
  - Raja 2014「OPCAB: 誤解と思い込み」
- **[27942397]** Guida GA (2016) *J Thorac Dis* — Off-pump coronary artery bypass grafting in high-risk patients: a review.
  - Guida 2016「高リスク患者におけるOPCAB」レビュー
- ★ **[31125606]** Patel V (2019) *Semin Thorac Cardiovasc Surg* — Current Readings on Outcomes After Off-Pump Coronary Artery Bypass Grafting.
  - Patel Semin Thorac Cardiovasc Surg 2019「OPCAB後アウトカムの現在の読み方」
- ★ **[41016746]** Suyker WJL (2025) *Interdiscip Cardiovasc Thorac Surg* — CABG at a Crossroads: Reinventing the Distal Anastomosis.
  - Suyker 2025「CABG at a Crossroads: 遠位吻合の再発明」。技術革新の方向性
- **[41971856]** Hynes CF (2026) *JTCVS Tech* — Complex composite conduits for anaortic off-pump coronary artery bypass grafting: Lambda and pi grafts.
  - Puskasグループ 2026。anaortic off-pumpのλ/π複合グラフト。当リポジトリのopcab_technique調査と接続
- **[42161480]** Ruel M (2026) *Can J Cardiol* — Stop the Invasion-Advances in Myocardial Revascularization.
  - Ruel Can J Cardiol 2026「Stop the Invasion — 心筋血行再建の進歩」

---

## 3. コピペ用 PMID ブロック

### 3-1. Tier A（最優先）— PubMed 検索窓 / EndNote / Zotero にそのまま貼付

```
9714098 24086085 24086086 34294272 35912444 30369328 38941506 19890125 28813218 35171210 22449296 23477676 27771985 23477657 30732456 32339504 22592900 39098613 20837925 35953640 28082464 29495998 38522653 28942940 30373421 28958597 35041977 21987177 26433633 21664624 26371452 42266971 34411544 30236310 31740974 24703910 34800223 41619148 25043865 30699314 25217501 32305186 33413936 29708851 32662861 33017209 31934782 33686866 30636525 37535847 37542480 26680310 39656609 28119382 30239376 39389436 40348256 41628842 41865963 30417737 39969129 40306935 40929150 34460327 31455868 29084780 37417248 28231944 21281950 26892526 34977717 33502822 41619278 33067581 23747787 29407133 30686645 30094210 34606302 30907418 34735046 40174598 33841980 40434908 42301235 39116933 39157183 34890572 39567250 35429509 30474417 39733961 39730082 42236427 34337649 35143631 35900153 42301733 41619927 34474026 39157180 39157181 39209092 36848999 41025333 38580041 42266981 26707761 40884067 40884083 40888737 29710164 38862179 32862716 35943473 31601578 40907505 31865057 38456874 29420954 34138766 39385505 31488373 23439102 31562798 34793745 29478841 27040723 40404111 36094460 37121245 34611327 37348857 34882435 34895950 30165437 30165632 39210710 40900620 37471501 40014670 37632756 34272070 31219874 40268129 27942402 31125606 41016746
```

（148 件）

### 3-2. 全件（Tier A + B）

```
39434975 31562798 38626442 33017209 18628261 40929150 30885092 40014670 30369328 34890572 42236427 36094460 32339504 16139139 25043865 39098613 34735046 39157181 29710164 9714098 38941506 29657055 36349729 41016746 41025333 22449296 34078097 19228612 37471501 34138766 41330389 32662861 35675092 22592900 40888737 31672179 21987177 41210676 11903027 21801945 38266796 11591611 42266971 40900620 22070836 39385505 36276694 28231944 32167555 32862716 39552037 25648476 22523305 27298393 38677447 41619278 34411544 31934782 40306935 36130278 40174598 21619980 39656609 26470910 38919214 28813218 31394563 24086086 29407133 38456874 23439102 29608874 30699314 39783258 40348256 33067581 26707761 25217501 31826727 38580041 30373421 11955537 34882435 24086085 36848999 20837925 29495998 32305186 28958597 40907505 35429509 30165632 26276839 39116933 41121332 41971856 4642307 34166508 34800223 29661948 30094210 8837572 37417248 17140968 40434908 42188066 34586338 40884067 31219874 12970201 30239376 37632756 26371452 37330205 22893280 20869314 41403064 29420954 39566870 41135855 40404111 33016239 25791924 37720926 24703910 39567250 39157180 35943473 23747787 34895950 37086268 35953640 29708851 40376846 39144317 32818539 39389436 27777290 39157182 28566338 33002935 22698772 24886787 37348857 26680310 21420873 42301733 33038121 34793745 21664624 31504374 33413936 35041977 39432255 36394709 27942402 12556542 15557371 39730082 28082464 21684171 21281950 27771985 15564545 31256329 26433633 17312289 39157183 26892526 35143631 28942940 23477657 14992872 34710343 27942397 21937020 35171210 42288779 33686866 28119382 38420786 30369591 38008347 37121245 31549144 23477676 30474417 31865057 34474026 30165437 31455868 38606620 40268129 27942401 20083683 38522653 20805116 33779716 34460327 34337649 34555373 27040723 34977717 21415073 38862179 41334602 37624649 41714707 34606302 31601578 34333605 15100202 39209092 20167334 41865963 42161480 35912444 41619148 42266981 30686645 33155975 30732456 34272070 31740974 42027519 31125606 40947142 34611327 30907418 35229663 39969129 17709642 15337239 41619927 36098376 33502822 29478841 37535847 39210710 40884083 30636525 35900153 31395122 30417737 33841980 29084780 25237626 34294272 35266173 42301235 39733961 32771552 30236310 22965976 41628842 29680218 30654882 19890125 41210677 37542480 36229295 24613160 31976863 31488373 40725570
```

（265 件）

### 3-3. セクション別ブロック

**§1 史的背景 — CABGの誕生と50年の軌跡**

```
9714098 4642307 24086085 24086086 34294272 35912444 30369328 38941506 41210677 41210676 39783258 38919214 22893280 39157182 20869314 39552037
```

**§2 OPCAB vs ONCAB — 主要RCTと長期追跡 (一次データ)**

```
19890125 28813218 35171210 22449296 23477676 27771985 23477657 30732456 32339504 22592900 39098613 11591611 12556542 17312289 11903027 20837925 35953640 20083683 21415073 22523305 24613160 15557371 14992872 11955537 15100202 21619980 31395122 24886787 28082464 37624649
```

**§3 メタ解析・システマティックレビュー (OPCAB vs ONCAB)**

```
29495998 38522653 28942940 30373421 28958597 35041977 21987177 18628261 16139139 20167334 26276839 38626442 26433633 21664624 29608874 25791924 35266173 21801945 21684171 21937020 33016239 26371452 37720926 36349729
```

**§4 大規模レジストリ・傾向スコア (超長期・実臨床)**

```
42266971 34411544 30236310 31740974 27777290 24703910 17709642 22965976 34800223 31256329 41403064 41619148 25043865 35229663 42288779 34333605 25648476 41330389
```

**§5 多枝動脈グラフト (MAG) / 導管選択 — 長期開存とアウトカム**

```
30699314 20805116 25217501 32305186 33413936 34586338 28566338 29708851 32662861 33017209 15564545 31934782 33686866 30636525 37535847 37542480 26680310 39656609 28119382 32771552 36394709 41334602 30239376 37330205 33779716 39389436 40348256 41628842 41865963 31672179 31976863 29661948 36229295
```

**§6 伏在静脈グラフト — no-touch・採取法・グラフト不全**

```
30417737 39969129 40306935 40929150 34460327 31455868 29084780 37417248 35675092 41135855 38606620
```

**§7 No-touch aorta / anaortic 技術と脳卒中**

```
28231944 21281950 26892526 34977717 33502822 41619278 31504374 8837572 12970201 21420873 33002935 40725570
```

**§8 血行再建の完全性 (Incomplete Revascularization)**

```
33067581 23747787 29407133 30686645 30094210 38266796 39144317 17140968 30369591
```

**§9 術中グラフト評価 (TTFM / FFR)**

```
34606302 30907418 27298393 34166508 36276694 34735046 40174598 34078097 32167555 40376846
```

**§10 ロボット支援CABG / MICS-CABG / ハイブリッド**

```
33841980 40434908 42301235 39116933 39157183 34890572 39567250 29657055 33155975 30885092 35429509 38008347 38677447 29680218 31826727 36130278 32818539 39434975 30474417
```

**§11 教育・トレーニング・サブスペシャリティ化**

```
39733961 39730082 42236427 34337649 35143631 35900153 42301733 41619927 34474026 39157180 39157181 39209092 36848999 41025333 38580041 42266981 26707761 22698772 26470910 36098376 41121332 31394563 42188066
```

**§12 至適薬物療法 (OMT) — 抗血小板・脂質**

```
40884067 40884083 40888737 29710164 38862179 32862716 35943473 31601578 40907505 31865057 34555373 38456874 29420954 34138766 33038121 34710343 39566870 30654882 37086268 39385505
```

**§13 CABG vs PCI — 意思決定の文脈**

```
31488373 23439102 19228612 31562798 34793745 29478841 27040723 40404111 39432255 36094460 37121245 34611327 37348857 40947142 41714707
```

**§14 ガイドライン・コンセンサス (現行版)**

```
34882435 34895950 30165437 30165632 39210710 40900620 37471501 40014670 37632756 34272070 38420786 22070836 15337239
```

**§15 OPCABの現在地 — 論争・立場表明・実践**

```
39730082 31219874 40268129 27942401 31549144 42027519 27942402 25237626 27942397 31125606 41016746 41971856 42161480
```

---

## 4. カバーできなかった/注意点

- **Puskas STSデータベース15年解析**は上記のとおり未刊。公刊され次第の追補が必要です。
- **Lamy 3試験統合**も同様。ClinicalTrials.gov や STS/AATS/EACTS の抄録集を当たれば発表スライドに到達できる可能性があります（PubMed経由では不可）。
- **ROMA試験（MAG vs SAG の決定版RCT）は結果未公表**。現在はデザイン論文（PMID 30239376 ほか）のみで、2020年代後半の最大の空白です。
- Operative Techniques 系など **MEDLINE非採録誌はPMIDが存在しません**（当リポジトリの `opcab_technique` 調査と同じ制約）。手技論文が必要な場合はそちらのCSV（114編）を併用してください。
- 本リストは**臨床エビデンス**に振っています。**手技の how-to**（吻合・スタビライザ・展開・ビデオ）は既存の `opcab_technique/md/OPCAB_technique_review.md`（114編）が既にカバー済みで、意図的に重複を避けました。
