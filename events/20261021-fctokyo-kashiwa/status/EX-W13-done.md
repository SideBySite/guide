# EX-W13｜前線・切り替えの8記事 完了記録

- **状態**：8記事を新規執筆、記事別推敲・根拠照合・逸話採否を完了。専用PR：[#231](https://github.com/SideBySite/guide/pull/231)（このPRのみmainへマージ対象）。
- **対象**：2026-10-21（水）19:00 JST、味の素スタジアム、FC東京×柏レイソル（2026/27 J1第11節）。**全確認基準：2026-10-21 JST、試合開始前**。結果や当日の実際の動作は先取りしない。
- **必須先行の実確認**：mainの `discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md` をそれぞれ実ファイルとして照合。00-I PR #183は2026-10-21 04:51:52 UTC、追補PR [#191](https://github.com/SideBySite/guide/pull/191) は同日05:12:32 UTCにmainマージ済み。資料が存在するだけで先行を満たしたとは判断しなかった。
- **00-Iとの対応**：D-17/18/19/20/26/28/29/30の `answer_scope`・`why_distinct`・`fact_check` を読み、8件それぞれの観察対象を別にした。決定ログでも8候補すべて採用を確認。
- **その他の参照**：`docs/question-tree.md`、`docs/prompt-pack/baseline-question-tree.md`（固定64問）、`shared-style.md`、`manifest.json`、runtimeのEX-W13担当指示、`teams/fctokyo`・`teams/kashiwa` のroster/assignments、`foundation-v2/README.md`、関連済み記事 `6-06.md`・`6-07.md`、EX-W10/12のstatus。
- **変更範囲**：`content/6/6-08{,-a,-b,-c}.md`、`content/6/6-09{,-a,-b,-c}.md`、本statusの9ファイルに限定。固定64問、LOCAL18問、共通候補・割当表、02/03、FCT-PREP、別担当の原稿を変更していない。ユーザー・製作者本人の逸話や旧maker導線は利用していない。

## 記事別検証

「字数」はMarkdown装飾記号を除く見出し・関連導線・引用込みの簡易計数。全件に `ひとことで`／`しくみ`／`今日の試合で見るなら`、1記事3〜6個の==要点マーカー==、初出用語の説明、独立の観察、確認済みと未確定の境界、出典URLと確認日を設置。

| ID | レベル・概算字数 | 00-I | 独立の論点・観察・fact_checkの反映 | 判定 |
|---|---|---|---|---|
| 6-08 | L1・999字 | D-17 | FWの動く・止まる・戻る・守る30秒。出場があれば#9マルセロ ヒアン。『おとり成功』と決めつけない。FIFA確認済み逸話1件 | 合格 |
| 6-08-a | L2・443字 | D-18 | 未受球の背後走りと別の受け手の距離。本人の意図は不明、IFABの関与を伴うオフサイドにも留保 | 合格 |
| 6-08-b | L2・425字 | D-19 | 前線二人が交差した際の相手DF二人の受け渡し。作戦が事前に決まっていたとは断定しない | 合格 |
| 6-08-c | L2・440字 | D-20 | FWが下がって受ける前後5秒と背後へ走る別の味方。中盤が後方へ戻るD-14と分離 | 合格 |
| 6-09 | L1・964字 | D-26 | ボールを失った直後の近く三人・最初の二歩。4-01-bのチーム戦術選択とは区別。FA守備映像例1件 | 合格 |
| 6-09-a | L2・411字 | D-28 | 隣の人が次のパス経路を塞ぐ動き。相手のパス方向だけで因果を確定しない | 合格 |
| 6-09-b | L2・438字 | D-29 | 長い後退走と振り返りの時点。本人の視線の先と指示内容は未確認 | 合格 |
| 6-09-c | L2・419字 | D-30 | 奪取直後の一つ目のパス方向と遠くの味方。止まることを時間稼ぎと断言しない | 合格 |

## 一次根拠・確認時点

以下のURLはいずれも**2026-10-21 JSTのキックオフ前**に照合。記録された過去の試合・資料の公開年と、今夜の起用・行動を混同しない。

- 当日の対戦・19:00・会場の**確認済み予定**：https://www.fctokyo.co.jp/match/schedule/info/20261021/ ／ https://www.jleague.jp/match/j1/2026/102108/
- #9マルセロ ヒアンのFC東京2026/27の**登録名簿**：https://www.fctokyo.co.jp/team/players/ ／ https://www.fctokyo.co.jp/team/players/number/ 。**当日出場確定ではない**。
- 競技規則2026/27の公式入口：https://www.jfa.jp/laws/soccer/2026_27/ 。戦術・本人の意図を規定している資料ではない。
- オフサイドの位置とプレー関与の条件： https://www.theifab.com/laws/latest/offside/ （球に触れなくても相手のプレーへの妨害で反則となる場合）。
- FWの複数回の走り・下がって受ける動き／英FA指導（2020年3月4日公開）：https://www.thefa.com/bootroom/resources/coaching/how-to-coach-forward-movement
- 切り替え直後の近くの助け／英FA指導（2020年3月11日公開）：https://www.thefa.com/bootroom/resources/coaching/how-to-coach-transition
- 英FA守備映像の3人の後退・相手GKの外側への配球・再奪取（2021年3月5日公開）：https://www.thefa.com/bootroom/resources/coaching/how-to-defend-like-england-transition
- 奪取直後の前進／落ち着かせる選択を確認する英FA指導（2016年9月30日公開）：https://www.thefa.com/bootroom/resources/coaching/what-is-transition
- **2014年7月13日 W杯決勝**ドイツ対アルゼンチン：ゲッツェ途中出場、シュールレのクロスから決勝点。FIFA回顧：https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/mario-gotze-goal-germany-argentina-2014
- **2018年 W杯ベルギー対日本**の終盤カウンターとルカクのスルーの照合元：https://inside.fifa.com/news/worldcupathome-belgium-japan-russia2018-3071468

## 調査検索ログとエピソード評価

日本語・英語で計**15以上の検索を実行**（2026-10-21 JST）。主な検索：「FC東京 柏 2026年10月21日 マルセロ ヒアン」「FC東京 登録 2026/27」「前線の走り サッカー スペース」「football forward movement dropping deep making runs」「defending transition losing possession recovery runs」「England Iceland defenders recover passing interception」「Mario Götze Schürrle 2014 final FIFA」「Messi Molina Netherlands 2022 FIFA」「Lukaku dummy Japan Belgium 2018」「IFAB offside interfering with opponent」。見つけられなかった一次資料は採用根拠にしない。

5尺度各5点＝「驚き／今夜見たくなる／なぜが解ける／情景が浮かぶ／一次出典確実性」。

| 逸話候補 | 5尺度採点／合計 | 採否・理由 |
|---|---|---|
| 2014 W杯決勝：88分投入ゲッツェがシュールレの球を胸で受けて決勝点 | 5/5/4/5/5＝24 | **6-08採用**。球を受ける前の準備から受球までの観察を促す。事前の狙いを語らない。FIFA一次確認 |
| 英FA守備教材のイングランド対アイスランド：後方3人が走って道を狭め、その後のパスをMFが奪取 | 4/5/5/5/5＝24 | **6-09採用**。戻る人が奪う人を助ける具体例。FA自身の映像解説に人物役割・行動・結果がそろう |
| 2018 W杯ベルギー対日本：ルカクが球に触れず、シャドリが決勝点 | 5/5/5/5/5＝25 | **見送り**。非常に適合するが、他担当の4-09ですでに採用された逸話の重複。FIFA出典あり。 |

採用しなかった題材を推量で別のL2の逸話にせず、8記事の観察を優先した。

## 予想と保留

- **確認済み**：試合の予定、登録名簿、JFA/IFABの規則、FA教材が説明する一般戦術、FIFA/FAで確認できる過去例。
- **未確認**：10/21の正式先発・控え・布陣・交代・具体的な走り、両チームが実際に最初に奪われる／奪い返す場面、選手の指示・視線の対象・心中、走りと相手の選択の因果。すべて今日欄で条件・観察課題として記述。
- 認識上の注意：ボール外の走りはそれだけで「おとり成功」ではない。守る人が横を選んだという観察は、道をふさいだ本人の影響を証明しない。競技規則は戦術を義務化しない。
- 次工程 EX-E／EX-D／EX-Qや別チャットの担当原稿は実施しない。本PRの変更9ファイルだけを確認しマージする。

PR URL：https://github.com/SideBySite/guide/pull/231
