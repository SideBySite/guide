# 00-H 完了：初心者の盲点と次に湧く疑問

- 対象：2026年10月21日（水）19:00 FC東京×柏レイソル／味の素スタジアム。試合前に確認した情報で制作。
- 状態：**担当候補完成**。42候補（カテゴリ1=6、2=6、3=5、4=7、5=6、6=8、7=4）。仮ID H01–H42。
- 保存：`discovery/00-H/candidates.json`、`discovery/00-H/review.md`、この `status/00-H-done.md` のみを担当対象として作成。
- 原稿・名鑑・正式記事IDは未制作。共有 `docs/question-tree.md`、`docs/prompt-pack/*`、`PLAN.md`、02/03/01Rの担当ファイルは変更しない。
- 先行：必須なし。初版01の `facts/match.md` / `facts/stakes.md` と baseline 64問を参考にしたが、02/03を再実行せず、foundation-v2/完成も条件にしていない。

## 方法と出典
- 基礎参照：`docs/prompt-pack/baseline-question-tree.md`、`docs/prompt-pack/shared-style.md`、過去の `docs/question-tree.md`、`docs/content-template.md`、`scripts/build_prompts.py`（L1/L2の導線、追加と記事分割）。
- 当日の事実：[FC東京公式](https://www.fctokyo.co.jp/match/schedule/info/20261021/)、[柏公式](https://www.reysol.co.jp/game/results/202627/1021i.php)、[Jリーグ公式試合](https://www.jleague.jp/match/j1/2026/102108/) を照合。今夜は2026/27明治安田J1第11節であり、19:00開始。
- 規則：[IFAB 2026/27](https://www.theifab.com/laws/latest/)、[J1大会概要](https://www.jleague.jp/outline/j1/)、[J1順位表](https://www.jleague.jp/j1/standings/2026-27/) を参照。今夜は90分のリーグ戦で引き分けあり、勝利3・引分1・敗戦0の勝点。
- 観客導線：[FC東京初観戦](https://www.fctokyo.co.jp/first_time_guide/)、[10/21観戦マナー変更](https://www.fctokyo.co.jp/news/details/342462/)、[当日券・開門](https://www.fctokyo.co.jp/news/details/342829/) を参照。
- 各候補に発問時点、回答範囲、今夜の観察行動、既存問との差分、未確認項目、個別の手掛かりURLを残した。本文の事実断定と観察仮説を区別した。

## 後工程で確認する不確実性
1. 当日のスタメン、背番号、ユニフォーム色、布陣、交代、攻める向きは発表または実際の試合で確かめる。
2. 2026/27のVAR・遅延フラッグ・審判シグナル運用を当該Jリーグ試合に結びつける際は公式情報を再確認。
3. 10/21固有の入退場・座席エリア、ビジョン表示、終了後の挨拶は当日の告知を優先。
4. 選手の首振り、囮の走り、監督の指示、ミス後の声掛けは、映像・本人発言がない限り意図を断定しない。
5. 試合前勝点は2026-10-18終了時点の表を使用。試合開始直前に順位表更新があれば読み替える。

次工程の00-Iが採否・統合を検討できる候補であり、共有一覧の編集権限は引き継がない。
