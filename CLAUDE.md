# CVS Journal Research

心臓外科（CVS: CardioVascular Surgery）関連ジャーナルの最新号を定期的にレビューし、
注目論文をまとめるプロジェクト。

## プロジェクト構成

```
MD/                          # ジャーナルまとめMarkdownファイル
  cardiothoracic_journals_schedule.md  # 各誌の公開スケジュール
  cardiac_surgery_journals_YYYY_MM.md  # 月別論文まとめ
output/                      # 生成HTMLレポート
  journal_report_YYYY_MM.html
.claude/commands/            # カスタムスラッシュコマンド
  journal-update.md          # /journal-update コマンド
```

## 対象ジャーナル

| 雑誌 | ISSN | 分野 |
|---|---|---|
| JTCVS | 0022-5223 | 心臓血管外科全般（AATS/WTSA） |
| JHLT | 1053-2498 | 心臓移植・MCS（ISHLT） |
| EJCTS | 1010-7940 | 心臓胸部外科（EACTS/ESTS） |

## 注目分野

- MCS（Mechanical Circulatory Support）/ LVAD
- 心臓移植（DCD含む）
- 弁膜症外科
- 大動脈外科
- ECMO
- 不整脈外科
- 周術期管理

## データソース

- **CrossRef API**: DOI・メタデータ取得（MCP paper-search経由、ISSN filterで各誌を検索）
- **PubMed**: Abstract取得（MCP paper-search経由）

## ワークフロー

1. `/journal-update` コマンドを実行
2. MCPツール（CrossRef + PubMed）で最新号の論文一覧・メタデータ・Abstractを自動取得
3. MDファイルとHTMLレポートを自動生成
