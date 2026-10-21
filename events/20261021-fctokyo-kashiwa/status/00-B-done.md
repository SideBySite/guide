# 00-B「ルール・判定・再開」完了記録

**対象**：2026年10月21日（水）19:00 JST、味の素スタジアム、FC東京×柏レイソル、2026/27明治安田J1リーグ第11節。**確認と執筆**：同日、試合前（JST）。試合後の結果を前提にしていない。

## 完了範囲と編集対象

- `discovery/00-B/candidates.json`：候補45問（L1 14、L2 31、★ 21）。仮ID B-01〜B-45。各候補に指定の12キー、答える具体事項、当日見る動作、類似問との違い、要確認事項と手掛かりURLを収録。正式記事IDなし。
- `discovery/00-B/review.md`：まとまり・近接問の差・未充足と見送り。
- `status/00-B-done.md`：本記録。
- 上記以外のファイルは変更しない。02・03の再調査、04、01R、候補割当、記事本文、サイトの改変は行わない。

## 一次資料と編集上の境界

- 対象試合：https://www.fctokyo.co.jp/match/schedule/info/20261021/ と https://www.jleague.jp/match/j1/2026/102108/
- 2026/27競技規則（JFA）：https://www.jfa.jp/laws/soccer/2026_27/
- 2026/27競技規則改正（IFAB）：https://www.theifab.com/law-changes/latest/
- J1公式大会概要（通常交代5人・最大3回、脳振盪、VAR全380試合、90分引き分け）：https://www.jleague.jp/outline/j1/
- 柏10/17公式試合記録：https://www.reysol.co.jp/game/results/202627/1017.php （6人の交代とGK交代は当日の事実でなく**前戦の例**）
- 元01の `basics/rules.md` と過去野球版 `docs/question-tree.md` `docs/content-template.md` `scripts/build_prompts.py` は読み取りのみ。

## 残る不確実性と引き継ぎ

- 指定された `docs/prompt-pack/baseline-question-tree.md` と `shared-style.md` がmainと確認した01R-A/Bブランチにないため、**基本64問との完全一致・重複検算は未完**。存在が確認できた時点で統合担当が比較すること（この担当は新しい共有仕様を作らない）。
- J1が競技規則2026/27の**選択制VAR拡張（明らかに誤ったCKなど）**を実際に採用したか未確認。GK8秒と遅延再開5秒は**適用場面が別**。けがによる場外治療時間、退出10秒の例外は原規則・大会運用を要照合。
- 本件の**先発・控え、判定の発生、退場、PK、VARレビュー**は未確認の未来の出来事として扱い、記事では『起きたら見る』と書く。柏選手への言及も出場条件つきで、実際の意図・審判の内心を断定しない。
- 今日の試合は90分同点で引き分けるJ1であり、2026年春の百年構想リーグ式PK戦を前提にしない。原稿着手前の個別 `fact_check` 消し込みが必要。

**ブランチ**：`soccer/discovery-00-B`。変更はこの3ファイルのみ。
