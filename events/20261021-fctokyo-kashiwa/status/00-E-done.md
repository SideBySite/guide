# 00-E 完了記録：両チーム・選手・監督の物語から掘る

- 担当：00-E（カテゴリ5・6の問い候補のみ）
- 対象：2026年10月21日（水）19:00 JST、FC東京×柏レイソル、味の素スタジアム、2026/27 J1第11節
- 基準：2026年10月21日の試合前に確認できた資料。19:00以降の結果を前提にしない。
- ブランチ：`soccer/discovery-00-E` → `main`

## 完了範囲

1. `discovery/00-E/candidates.json`：仮ID E-01〜E-40 の**40問**。カテゴリ5=20、カテゴリ6=20、L1=21、L2=19、star=16。各問について trigger / answer_scope / today_watch / novice_value / distinct_from / fact_check / sources を記録。
2. `discovery/00-E/review.md`：話題のまとまり、既存64問との違い、逸話化の候補評価、見送った案、未確認情報を記録。
3. 本ファイル：完了範囲と確認事項の引き継ぎ。

形式検査：40件・40種の仮ID、必須13フィールド全件存在、URLはいずれもHTTPS文字列、L2の親は同ファイルに存在、L1は親なし、問の完全一致重複は0。手動編集は上記の専用フォルダと本ファイルのみ。

## 調べた主な根拠

- 当日試合・前提：<https://www.fctokyo.co.jp/match/schedule/info/20261021/>、<https://www.jleague.jp/match/j1/2026/102108/>
- FC東京の来歴・育成・地元・監督：<https://www.fctokyo.co.jp/club/profile/>、<https://www.fctokyo.co.jp/club/philosophy/>、<https://www.fctokyo.co.jp/club/hometown/>、<https://www.fctokyo.co.jp/news/details/316882/>
- 柏の来歴・育成・地域・監督：<https://www.reysol.co.jp/club/clubinfo/>、<https://www.reysol.co.jp/club/history/chronology/1115.php>、<https://reysol.co.jp/academy/about.php>、<https://reysol.co.jp/team/staff/s01.php>
- 主将・人物接点：<https://www.reysol.co.jp/news/topteam/202627-8.html>、<https://www.jleague.jp/player/801425/>、<https://www.reysol.co.jp/game/results/202627/1017.php>
- 参考仕様：`docs/prompt-pack/shared-style.md`、`docs/prompt-pack/baseline-question-tree.md` とルートの旧 `docs/question-tree.md`・`docs/content-template.md`・`scripts/build_prompts.py`。

## 不確実性・次工程への注意

- 当日の先発・控え・腕章の着用者、各選手の起用、試合中の挨拶やジェスチャーは事前に確定しない。名前入りの `today_watch` は**出場した場合の観察案**。
- 柏の若原智哉、馬場晴也、熊坂光希らの出場可否や回復時期を断定しない。試合中の交代を予告しない。
- 2004年のFC東京決勝、1986年の前身柏クラブの移転、過去に同じ監督と選手が所属した時期の細部は、各候補の `fact_check` に残した。
- サインや会話の意味、仲の良さ、監督の動機、選手の心理は外から決めつけず、本人談が見つかるまで仮説として扱う。
- 02/03/01Rは再実行していない。04の柏候補表（PR #149でmain反映済み）は参照だけ。foundation-v2完成を前提条件にしていない。
- 共有候補表・割当表・テンプレート・`docs/question-tree.md`・`PLAN.md`や、別担当原稿は一切編集していない。正式な記事ID・本文・人物カード・サイトは作成していない。
