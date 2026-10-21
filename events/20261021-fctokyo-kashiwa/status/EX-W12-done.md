# EX-W12｜7記事執筆・検証記録

- **確認基準：2026-10-21 16:30 JST、19:00試合開始前**。会場：味の素スタジアム、FC東京×柏レイソル。今夜の先発・布陣・交代・試合結果は未確認。
- **先行を実確認**：mainの`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`を読了。00-IのPR [#191](https://github.com/SideBySite/guide/pull/191)はmerge済み（2026-10-21 05:12:32 UTC）。単に資料が存在するだけでは完了とみなさなかった。
- 00-I各候補の`answer_scope`・`why_distinct`・`fact_check`を調査。併せて`docs/question-tree.md`・`docs/prompt-pack/baseline-question-tree.md`・`shared-style.md`・`manifest.json`、既存`6-03.md`・`6-03-a.md`、両クラブ`teams/*/roster.md`・`assignments.md`・`lineup.md`、完成済みfoundation-v2を参照。
- **変更は8ファイル限定**：`content/6/6-06.md`、`6-06-a.md`、`6-06-b.md`、`6-06-c.md`、`6-07.md`、`6-07-a.md`、`6-07-b.md`とこのstatusだけ。固定64問、LOCAL18問、共有表、別担当原稿、02/03、FCT-PREPは無変更。本人・製作者の個人的な経験・回想は使用しない。

## 記事別検証

| ID | 00-I | 独立の答え・観察 | 検査 |
|---|---|---|---|
| 6-06 | D-06 | 後方の守備準備と3人の関係。4-01-bの全体戦術とは別。両チーム30秒ずつ | L1／今日欄／確認・未確認を分離 |
| 6-06-a | D-08 | 端のDFが攻撃に加わる理由と背後の空白。石原の起用は予想 | L2／今日欄／採用逸話1件 |
| 6-06-b | D-09 | 寄る人・覆う人の役割。D-10の対相手の間合いとは分ける | L2／今日欄 |
| 6-06-c | D-10 | 一対一の距離と進路。時間稼ぎという内心は断定しない | L2／今日欄 |
| 6-07 | D-12 | MFの受球直前の数歩・姿勢。6-03-aの一般的準備と分離 | L1／今日欄 |
| 6-07-a | D-13 | 受球前の顔の動きと中央3パスの観察。視線の先は未確定 | L2／今日欄 |
| 6-07-b | D-16 | パスを出した人の次の5秒。D-13の受球前とは時点が違う | L2／今日欄 |

## 事実・戦術解釈・予想の出典

**以下すべて2026-10-21 JSTに確認。** 各原稿にも出典URL・確認日時を保持。資料の公開日と観察基準日を混同しない。

- **試合予定の確認済み事実**：https://www.fctokyo.co.jp/match/schedule/info/20261021/ ／ https://www.jleague.jp/match/j1/2026/102108/ 。19:00、味スタ、対戦カード。今日の選手配置は未発表として記述。
- **10/17の確認済み起用**：https://www.fctokyo.co.jp/match/schedule/result/20261017/ ／ https://www.reysol.co.jp/game/results/202627/1017.php 。石原広教・高宇洋・古賀太陽・小泉佳穂・小西雄大らの記録。**今夜の先発は未確認**。
- **ルール**：https://www.jfa.jp/laws/soccer/2026_27/ 。戦術の義務・特定選手の意図の根拠ではない。
- **戦術の一般的な指導**：https://www.thefa.com/bootroom/resources/coaching/how-to-defend-like-england-roles-and-responsibilities ／ https://www.thefa.com/bootroom/resources/coaching/mastering-defensive-techniques-and-roles ／ https://www.thefa.com/bootroom/resources/coaching/recover-and-stop ／ https://www.thefa.com/bootroom/resources/coaching/out-of-possession-preventing-forward-play ／ https://www.thefa.com/bootroom/resources/coaching/countdown-to-kick-off ／ https://www.thefa.com/bootroom/resources/coaching/take-a-picture 。
- **逸話原典**：https://www.uefa.com/uefachampionsleague/news/0221-0e909116af7b-fe3ef95b6374-1000--messi-double-puts-barca-in-control-against-bayern/ 。

## 逸話調査と採点

日英計5検索以上（公式日本語3系統＋英語FA/FIFA/UEFAほか12検索以上）。各項目5点で「笑える・驚ける／今日確かめたい／なぜが解ける／情景／一次出典で確認」を採点した。

| 候補 | 驚き | 今日 | 理由 | 情景 | 根拠 | 合計 | 採否 |
|---|---:|---:|---:|---:|---:|---:|---|
| 2015 UEFA準決勝 アウヴェスが奪取→メッシ先制 | 4 | 5 | 5 | 5 | 5 | 24 | **採用：6-06-a**。守る人が攻撃の入口となる。外からの追い越しと取り違えない |
| 2014 W杯 ブリントの左からのパス→ファンペルシー同点 | 5 | 4 | 3 | 5 | 5 | 22 | 見送り：外への追い越しの証拠ではない。https://www.fifa.com/en/articles/robin-van-persie-netherlands-spain-2014 |
| 2018 W杯 クルトワの再開から11秒でシャドリ決勝点 | 5 | 3 | 3 | 5 | 5 | 21 | 見送り：パスを出した本人の次の5秒に焦点がない。https://inside.fifa.com/news/worldcupathome-belgium-japan-russia2018-3071468 |
| 2010 W杯決勝 セスクのパス→イニエスタ決勝点 | 4 | 2 | 2 | 4 | 5 | 17 | 見送り：受球前の顔の動きは原典から確認できない。https://www.uefa.com/european-qualifiers/news/0253-0d7c93af1ed8-28be4efeaa14-1000--iniesta-earns-spain-world-cup-crown/ |

## 未解決

- 今夜の正式出場者・配置・交代、実際の守備分担や視線の先は未確認。一般的戦術を当日事実や個人の意図として断言しない。
- **EX-E02／EX-D06／EX-D07**の別工程は実行しない。同じ原稿の別工程を同時に編集しない。
- PR：[#229](https://github.com/SideBySite/guide/pull/229)。指定8ファイルだけの追加を差分で確認。マージ完了判定はPRのmerged状態を基準とする。
