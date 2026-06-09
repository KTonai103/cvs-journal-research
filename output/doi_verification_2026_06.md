# DOI検証ログ — 2026年6月号ジャーナルアップデート

> 検証日: 2026-06-09
> 方法: 全候補DOIを CrossRef `works/{DOI}` で個別取得しタイトル・著者を確認、さらに PubMed E-utilities（esearch `{DOI}[AID]` → efetch）でabstractを取得し、**abstract本文中に記載されたDOIが期待DOIと一致するか**を機械照合。
> 対象: JTCVS 28件 / JHLT 18件 / EJCTS 5件 = 計51件
> 結果: **誤リンク（別論文を指すDOI）0件**。49件はCrossRef↔PubMed↔abstract本文DOIが完全一致。2件はPubMed未収載（CrossRefメタデータで確認、タイトル一致）。

## 検証中に検出・除去した問題

PubMed esearch の `[AID]`（Article Identifier）フィールドで一致しなかった新着Online-First論文に対し `term={DOI}`（フィールド無指定）でフォールバック検索したところ、以下2件が **無関係な論文（PMID 38826717 = 2024年 *Heliyon* のCOVID抗体に関する論文）** を誤って返した。これを検出し、両件のPMIDを破棄・PubMed未収載として扱った（タイトル・メタデータはCrossRefで確認済み）。

| DOI | 誤返却PMID | 検出方法 | 最終扱い |
|---|---|---|---|
| 10.1016/j.healun.2026.05.036 (Ren, DCD donor injury) | 38826717（無関係） | abstract本文DOI不一致 | PubMed未収載→CrossRef使用 |
| 10.1016/j.healun.2026.06.004 (Kapnadak, CLAD管理) | 38826717（無関係） | abstract本文DOI不一致 | PubMed未収載→CrossRef使用 |

## JTCVS（Vol.171 Issue 6 + Online First）

| # | タイトル（短縮） | DOI | 検証結果 |
|---|---|---|---|
| 1 | 10°C SCS×ドナー年齢（Williams） | 10.1016/j.jtcvs.2025.12.013 | ✅ 一致 |
| 2 | バソプレシンvsノルエピRCT（Geube） | 10.1016/j.jtcvs.2025.11.009 | ✅ 一致 |
| 3 | Impella 5.5 AMI-CS（Anderson） | 10.1016/j.jtcvs.2025.12.034 | ✅ 一致 |
| 4 | 妊娠合併A型解離60例（Zhu）🔓 | 10.1016/j.jtcvs.2025.12.030 | ✅ 一致 |
| 5 | 境界域LV（Asanuma, Commentary） | 10.1016/j.jtcvs.2026.02.016 | ✅ 一致 |
| 6 | No-touch SVG長期（Sugaya）🇯🇵 | 10.1016/j.jtcvs.2026.01.018 | ✅ 一致 |
| 7 | TMVrvs外科（Danesh, Commentary） | 10.1016/j.jtcvs.2025.10.007 | ✅ 一致 |
| 8 | AFアブレーション×リウマチ僧帽弁（Park） | 10.1016/j.jtcvs.2025.12.033 | ✅ 一致 |
| 9 | PVAT×ITA抗攣縮（Zhang） | 10.1016/j.jtcvs.2025.10.033 | ✅ 一致 |
| 10 | Fontan failure ML calculator（Marathe） | 10.1016/j.jtcvs.2025.12.032 | ✅ 一致 |
| 11 | 小児重症AR+上行拡大（Konstantinov） | 10.1016/j.jtcvs.2026.01.002 | ✅ 一致 |
| 12 | 経心尖myectomy方法論（Xu, Letter） | 10.1016/j.jtcvs.2026.01.016 | ✅ 一致 |
| 13 | リウマチMS修復vs置換（Jia） | 10.1016/j.jtcvs.2026.01.024 | ✅ 一致 |
| 14 | Glenn段階的VAD（Keizman） | 10.1016/j.jtcvs.2026.01.033 | ✅ 一致 |
| 15 | VSRR ITT解析（Sanadgol） | 10.1016/j.jtcvs.2025.11.005 | ✅ 一致 |
| 16 | Fontan経路径×運動（Cao） | 10.1016/j.jtcvs.2026.02.027 | ✅ 一致 |
| 17 | AATS2026 肺サイズマッチ指針（Chang）🔓 | 10.1016/j.jtcvs.2026.03.620 | ✅ 一致 |
| 18 | VISION心臓外科合併症×死亡（Lamy） | 10.1016/j.jtcvs.2026.04.056 | ✅ 一致 |
| 19 | TAVI後再介入Medicare（Alabbadi） | 10.1016/j.jtcvs.2026.04.053 | ✅ 一致 |
| 20 | 術後AF長期1.9万例（Jacquemyn） | 10.1016/j.jtcvs.2026.05.005 | ✅ 一致 |
| 21 | NEHP冠灌流量（Alexander） | 10.1016/j.jtcvs.2026.05.006 | ✅ 一致 |
| 22 | DCD心移植1年死亡リスクスコア（Barile） | 10.1016/j.jtcvs.2026.05.010 | ✅ 一致 |
| 23 | EURECAH大動脈homograft心内膜炎（Galeone） | 10.1016/j.jtcvs.2026.05.011 | ✅ 一致 |
| 24 | 機能性TR弁輪拡大機序（Kawada）🇯🇵 | 10.1016/j.jtcvs.2026.05.016 | ✅ 一致 |
| 25 | MV修復失敗モード（Ferrel）🔓 | 10.1016/j.jtcvs.2026.05.020 | ✅ 一致 |
| 26 | 重症TR治療アルゴリズムTRI-SCORE（Dreyfus） | 10.1016/j.jtcvs.2026.05.023 | ✅ 一致 |
| 27 | Norwood RV-PA左右（Yamashita） | 10.1016/j.jtcvs.2026.05.024 | ✅ 一致 |
| 28 | 単段階Fontan ANZ（Marathe）🔓 | 10.1016/j.jtcvs.2026.06.001 | ✅ 一致 |

## JHLT（Vol.45 Issue 6 + Online First）

| # | タイトル（短縮） | DOI | 検証結果 |
|---|---|---|---|
| 29 | SCAI SHOCK連続評価（Baldan）🔓 | 10.1016/j.healun.2025.12.027 | ✅ 一致 |
| 30 | status2 tMCS×inotrope/LVAD（Ahn） | 10.1016/j.healun.2025.11.002 | ✅ 一致 |
| 31 | 心肺同時移植40年（Koh）🔓 | 10.1016/j.healun.2026.02.1664 | ✅ 一致 |
| 32 | TA-NRP神経モニタリング（Tur） | 10.1016/j.healun.2026.01.020 | ✅ 一致 |
| 33 | VA-ECMO LVアンロード（Beurton） | 10.1016/j.healun.2026.02.001 | ✅ 一致 |
| 34 | MMDx ABMR検出（Fernandez Valledor） | 10.1016/j.healun.2025.12.002 | ✅ 一致 |
| 35 | EVLP費用対効果（Peel） | 10.1016/j.healun.2026.01.032 | ✅ 一致 |
| 36 | CLAD空間トランスクリプトミクス（Goda） | 10.1016/j.healun.2026.01.028 | ✅ 一致 |
| 37 | RV回復力LVAD（Grinstein, Editorial） | 10.1016/j.healun.2026.05.008 | ✅ 一致 |
| 38 | mAFP後dLVADのAI/RHF（Grinstein） | 10.1016/j.healun.2026.05.011 | ✅ 一致 |
| 39 | NIHP2019 HOPEベイズ再解析（Heuts）🔓 | 10.1016/j.healun.2026.05.014 | ✅ 一致 |
| 40 | DCD donor injury UNOS（Ren） | 10.1016/j.healun.2026.05.036 | ⚠️ PubMed未収載→CrossRef確認 |
| 41 | CLAD予防管理北米（Kapnadak） | 10.1016/j.healun.2026.06.004 | ⚠️ PubMed未収載→CrossRef確認 |
| 42 | 自動深層表現型心移植登録（Patel） | 10.1016/j.healun.2026.05.024 | ✅ 一致 |
| 43 | レシピエント-ドナーリスク適合肺（Olson） | 10.1016/j.healun.2026.05.007 | ✅ 一致 |
| 44 | DEVOL灌流液EVLP延長（Arnold） | 10.1016/j.healun.2026.05.005 | ✅ 一致 |
| 45 | Sotatercept vs プロスタサイクリン（Genecand） | 10.1016/j.healun.2026.05.028 | ✅ 一致 |
| 46 | mAFP前置のHM3橋渡し（Goldstein, Editorial） | 10.1016/j.healun.2026.05.020 | ✅ 一致 |

## EJCTS（Vol.68 Issue 6 + Issue 5 Online First）

| # | タイトル（短縮） | DOI | 検証結果 |
|---|---|---|---|
| 47 | 肺動脈肉腫ESTS多施設（Lauk）🔓 | 10.1093/ejcts/ezag133 | ✅ 一致 |
| 48 | 先天性術後ECMO（Schaeffer）🔓 | 10.1093/ejcts/ezag123 | ✅ 一致 |
| 49 | 人工膵臓×SSI予防（Arai）🇯🇵🔓 | 10.1093/ejcts/ezag166 | ✅ 一致 |
| 50 | QUACS術後QoL（Nashef）🔓 | 10.1093/ejcts/ezag159 | ✅ 一致 |
| 51 | 機能評価CABG（de Waha, Editorial） | 10.1093/ejcts/ezag167 | ✅ 一致 |

---

*検証完了: 2026-06-09 ｜ 誤リンク 0件 ｜ PubMed未収載 2件（CrossRefで確認） ｜ フォールバック誤マッチ 2件を検出・除去*
