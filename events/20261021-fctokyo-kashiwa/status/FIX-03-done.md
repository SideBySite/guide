# FIX-03 完了報告

- 実施日: 2026-10-21
- リポジトリ: `SideBySite/guide`
- 作業先: `events/20261021-fctokyo-kashiwa/`
- 正式な category: `docs/prompt-pack/runtime/manifest.json` の `questions[].category`（277質問）
- 検証基準コミット: `8687338d9ea2f93f7517eed4c807927952052db8`

## 修正した8件

| ファイル（`content/` 相対） | 修正前 FM category | 修正後 FM category / manifest / ディレクトリ |
| --- | ---: | ---: |
| `1/2-04-a.md` | 2 | 1 |
| `1/2-04-b.md` | 2 | 1 |
| `1/2-06-a.md` | 2 | 1 |
| `1/7-03-a.md` | 7 | 1 |
| `2/1-01-d.md` | 1 | 2 |
| `2/1-01-e.md` | 1 | 2 |
| `2/6-05-a.md` | 6 | 2 |
| `6/1-01-c.md` | 1 | 6 |

- 指定8件すべて修正前の誤値を確認。既に修正済みとして除外したファイルは0件。
- 8件とも `category` の数値1行だけ変更。本文・その他の front matter キー・配置ディレクトリ・manifest は未変更。

## 全件走査

- 対象: `content/1/` ～ `content/7/` の Markdown 記事 **196件**（他の新規記事も含む）。
- 方法: 各記事の front matter の `id` とファイル名を確認し、`category`・配置先ディレクトリ・manifest `questions[].category` を比較。
- 修正前: 一致188件 / 不一致8件（上記8件だけ）。
- 修正後: **一致196件 / 不一致0件**。
- manifest に未登録のID: 0件 / IDとファイル名の不一致: 0件 / front matter 読取エラー: 0件。
- 走査中に追加された記事18件および既存記事更新1件も別途照合し、一致を確認。
- `content/local/` の別系統18記事＋index 1ファイルは、manifest の通常記事の照合対象から除外。

## コミットの変更範囲

- 既存記事8ファイルの front matter `category` 行のみ（各1行）。
- 本ファイル `status/FIX-03-done.md` の追加。
- 上記以外の変更は含めない。
