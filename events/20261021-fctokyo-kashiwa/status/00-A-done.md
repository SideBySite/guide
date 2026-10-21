# 00-A 初観戦の時間の流れから疑問を掘る — 完了記録

## 完成範囲
- `discovery/00-A/candidates.json`：**44候補**（カテゴリ1＝27、カテゴリ6＝17、★優先19）。仮候補ID`00-A-01`〜`00-A-44`のみ。
- `discovery/00-A/review.md`：まとまり・欠落する視点・他担当との違い・見送った案を記録。
- 全候補の必須キー：`candidate_id`、`question`、`level_hint`、`parent_question_or_existing_id`、`category_hint`、`trigger`、`answer_scope`、`today_watch`、`priority`、`novice_value`、`distinct_from`、`fact_check`、`sources`。
- この担当では**記事本文・選手カード・サイト・正式ID・共有候補表を作成していない**。

## 根拠と基準
- 対象は2026-10-21（水）19:00、FC東京×柏レイソル、味の素スタジアム、2026/27 J1第11節。**試合前公開情報**を採用。
- FC東京の当日公式時間表で**ピッチ内練習18:20・選手入場18:58・キックオフ19:00・ハーフタイムショー19:50頃**（すべて予定）を確認： https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏側の当日試合ページ： https://www.reysol.co.jp/game/results/202627/1021i.php
- J1大会概要： https://www.jleague.jp/outline/j1/
- JFA 2026/27競技規則： https://www.jfa.jp/laws/soccer/2026_27/
- IFAB 2026/27改正： https://theifab.com/law-changes/latest/
- 編集仕様：イベント`docs/prompt-pack/baseline-question-tree.md`・`shared-style.md`、旧`docs/question-tree.md`・`docs/content-template.md`・`scripts/build_prompts.py`、初版01の`facts/match.md`・`basics/rules.md`・`basics/stadium.md`を参照。

## 不確実性
- 先発発表の正確な時刻・画面の左右・試合前の円陣・入場や挨拶の演出・球の供給方法・会場でのビブスとベンチの配置は未確認。
- 負傷、医療介入、交代、VAR、PK、一斉給水が発生するかは予測しない。2026/27の場外治療や選択制のVAR拡張等の**国内運用細部**は記事化時に再確認する。
- 選手の内心、指差しの具体的な意味、観客の歓声の理由を観察だけで確定しない。これらは各候補の`fact_check`と`review.md`にも記録した。

## 編集範囲
ブランチ`soccer/discovery-00-A`。カテゴリ1、カテゴリ6を別々にコミットし、`review.md`とこの専用statusだけを追加。既存02/03・04、初版01と01R、共有仕様・割当表・PLAN・ルートの旧記事は変更しない。
