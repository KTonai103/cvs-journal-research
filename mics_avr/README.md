# mics_avr — MICS AVR（AR症例）オペレコ作図用 図譜

大動脈弁閉鎖不全（AR / AI）に対する低侵襲大動脈弁置換術（右小開胸 / 部分胸骨切開 / 完全内視鏡下）の
**手術記録（オペレコ）作図に使える図**を、PMC のオープンアクセス論文からのみ集めたもの。

## 成果物

| ファイル | 内容 |
|---|---|
| `md/MICS_AVR_figure_atlas.md` | 本体（55KB、図73点） |
| `output/MICS_AVR_figure_atlas.html` | HTML版（サイドバー目次付き、92KB） |
| `figures/mics_*.jpg` | 原著から取得した図 73 点 |

## 構成

0. AR に対する MICS AVR — 押さえるべき5点
1. 術前評価とアプローチ選択（7図）
2. 体位（4図）
3. 皮切・ポート配置（20図）
4. 送脱血・心筋保護（AR で最重要）（13図）
5. 大動脈切開・弁露出・弁縫着（14図）
6. 人工弁（Avalus ほか）（3図）
7. 大動脈弁・大動脈基部の解剖（3尖弁）（12図）
8. 図表一覧 / 9. 出典文献 / 10. 図は無いが必読の文献

## ライセンス方針

- **PMC OA Web Service（`oa.fcgi`）で 1 編ずつライセンスを機械照合**し、
  CC BY / CC BY-NC / CC BY-NC-ND が確認できた論文のみを採用（34編）。
- 図は PMC 記事 HTML 内の `cdn.ncbi.nlm.nih.gov/pmc/blobs/` URL から原寸で取得。
- 他文献からの転載図が混ざっていないことをキャプションのキーワード（reproduced / adapted /
  with permission ほか）で機械確認済み（該当 0 件）。
- **本図譜で新規に作図したイラストは 1 点も無い**（原著図のみ）。
- 個人の学習・診療参考目的での利用に限る。

## ビルド

```bash
python3 scripts/build_md.py                     # figsel.py + figs_index.json → md/
cd .. && python3 convert_to_html.py mics_avr/md/MICS_AVR_figure_atlas.md \
                                    mics_avr/output/MICS_AVR_figure_atlas.html
```

## スクリプト

| ファイル | 役割 |
|---|---|
| `scripts/pmsearch.py` | PubMed/PMC 検索 → PMCID・DOI・誌名の一覧 |
| `scripts/oacheck.py` | `oa.fcgi` で OA subset 収載とライセンスを並列照合 |
| `scripts/harvest.py` / `harvest2.py` | PMC 記事 HTML から図 URL＋キャプションを収集 → `figs_index.json` |
| `scripts/figsel.py` | 採用図の選定表（図ID, PMCID, 図index, 日本語キャプション） |
| `scripts/dl_figs.py` | 選定図のダウンロード → `figures/` |
| `scripts/build_md.py` | 章構成・本文・引用行を組んで MD を生成 |

- `candidates.txt` / `cand2.txt` / `cand3.txt` … 検索で拾った候補 PMCID
- `oa_status.tsv` / `oa_all.tsv` … OA 判定結果（63編が CC ライセンス）
- `figs_index.json` … 63編・263図のキャプション索引（採用は73図）

## 注意点（次回の作業者へ）

- **PMC OA package（`ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/…tar.gz`）は 404 で落ちない。**
  図は記事 HTML の `cdn.ncbi.nlm.nih.gov/pmc/blobs/` URL から取る（`harvest.py` の方式）。
- PMC は連続アクセスで reCAPTCHA を返す。`harvest2.py` のようにリトライ＋sleep を入れる。
- `scripts/select.py` という名前は stdlib の `select` を隠して壊れる → `figsel.py` に改名済み。
- convert_to_html.py の CJK 強調処理は `**太字**の直後に日本語`が続くとキャプションを取りこぼす
  ことがある。ビルド後に `<img>` 直後が `<em>` になっているか 73/73 で確認すること。
- Ann Cardiothorac Surg 2015;4(1)(2) の MIAVR 特集（Miami Method 等）は
  PMC で全文は読めるが **OA subset 外**のため図は採用していない（§10 にリンクのみ）。
