# EX-W02 執筆7件：完了記録

- 対象：2026年10月21日（水）19:00 JST開始予定、味の素スタジアム FC東京×柏レイソル。**確認基準は同日試合前**。
- 担当：`1-02-c`〜`1-02-i`のL2新規7記事と本statusのみ。完了：**7/7件**。
- 専用ブランチ：`soccer/20261021-ex-w02-writing`
- 自分のPR：**#217** https://github.com/SideBySite/guide/pull/217
- 先行確認：`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`がmainに実在。00-I追補PR #191がmainへマージ済み（merge commit `2f93f435acac7ede5031978da909a9566f5212be`）。文書が存在することと必須先行の完了を別々に照合した。
- 参照：`docs/question-tree.md`、`docs/prompt-pack/baseline-question-tree.md`、`shared-style.md`、`manifest.json`、既存`content/1/1-02.md`・`1-02-a.md`、`docs/prompt-pack/runtime/README.md`。foundation-v2の`basics/rules.md`はmainで未発見のため、その存在を前提とせず公式規則を照合。チーム個人出場情報を確定扱いしない。
- 範囲：固定64問、LOCAL18問、02/03、FCT-PREP、共有表、別担当稿、人物カード、本人・製作者の個人体験は**未編集・未採用**。

## 記事別の検証

文字数はMarkdownのfrontmatter・見出し・装飾・関連ID行を除く本文相当の簡易集計。L2目安250〜600字、見出し「今日の試合で見るなら」、見える観察行動、初出専門語の説明、強調、出典、確認日を7件確認した。

| ID | 本文字数 | 00-I候補 | 独立する答え・検証 | 結果 |
|---|---:|---|---|---|
| 1-02-c | 470 | 00-A-08 | トス勝者はキックオフか前半の攻撃ゴールを選択。先に蹴るチーム・トス結果は未確定 | OK |
| 1-02-d | 591 | 00-A-15 | 通常の中断中の補水と審判による飲水／冷却中断を区別。今夜の実施は未確認 | OK |
| 1-02-e | 456 | 00-A-18 | **認められた得点**の後、失点側が中央から再開。歓声と確定判定を区別 | OK |
| 1-02-f | 509 | 00-A-20 | 休憩15分以内、選手の出入りと場内企画を区別。19:50頃は公式**予定**であり実績ではない | OK |
| 1-02-g | 464 | 00-A-24 | ＋4は最低4分であり終了時刻を保証しない。＋4は例示で今夜の表示値ではない | OK |
| 1-02-h | 513 | 00-A-25 | 前半の笛／反則の笛／試合終了を区別。J1は同点なら延長・PKなし | OK |
| 1-02-i | 385 | H06 | 前後半の攻撃方向変更ではなく、奪取ごとの攻守の入れ替わりと近くの3人の守備準備を観察 | OK |

各記事の`checked_at: 2026-10-21`と`sources`に記事固有のURLを収録。確認日・公式の発表時刻・実際の試合進行を混同していない。

## 公式出典・確認日

以下は**2026-10-21 JST、試合開始前に参照先と記述を照合**した入口。資料の発行年・試合が行われた年とは別の確認日である。

- [IFAB第8条相当・FA公式（開始／再開）](https://www.thefa.com/football-rules-governance/lawsandrules/laws/football-11-11/law-8---the-start-and-restart-of-play)：コイントス・キックオフ・得点後、相手9.15m。
- [IFAB第7条相当・FA公式（試合時間）](https://www.thefa.com/football-rules-governance/lawsandrules/laws/football-11-11/law-7---the-duration-of-the-match)：前後半45分、休憩15分以内、飲水中断、最低追加時間。
- [IFAB公式2026/27 第7条](https://www.theifab.com/laws/latest/the-duration-of-the-match/) ／ [IFAB公式2026/27 第8条](https://www.theifab.com/laws/latest/the-start-and-restart-of-play/) ／ [JFA2026/27競技規則](https://www.jfa.jp/laws/soccer/2026_27/)：現行規則の突き合わせ。
- [FC東京10/21当日案内](https://www.fctokyo.co.jp/match/schedule/info/20261021/)：19:00開始、味スタ、19:50頃ハーフタイムショー**予定**。
- [Jリーグ2026/27 J1大会概要](https://www.jleague.jp/outline/j1/)：90分で引き分けの扱い・勝点。
- [Jリーグ10/21試合ページ](https://www.jleague.jp/match/j1/2026/102108/)：対戦カードの入口。結果は試合前には記述しない。
- [FIFA：2014年オランダ対メキシコ](https://inside.fifa.com/tournaments/mens/worldcup/2018russia/news/taking-a-break-in-fortaleza-2947640) ／ [同試合・監督の戦術変更](https://inside.fifa.com/tournaments/mens/worldcup/2014brazil/news/worldcupathome-huntelaar-ruins-mexican-party-3069987)：冷却休憩の実施と活用。
- [UEFA：2005年リバプール対ミラン](https://www.uefa.com/news/025d-0f782b45c942-3e20b8c30dfa-1000--miracle-of-istanbul-an-oral-history/)：休憩中の交代・配置変更と後半同点。
- [FIFA：2018年ベルギー対日本](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/belgium-japan-comeback-2018)：GKの再開から11秒で決勝点。
- [FIFA：2022年日本対ドイツ](https://www.fifa.com/ja/articles/germany-japan-group-e-world-cup-qatar-2022-match-report-asano-doan-gundogan-ja)：交代選手による逆転例、今回は見送り。

## 逸話候補の調査・採点

日本語・英語を合わせて、競技規則、当日運用、2014年冷却休憩、2005年ハーフタイム、2018年攻守転換、2022年途中交代など**5検索以上**実施。全候補を各5点、合計25点で採点。

| 候補 | 驚き | 今日見たい | なぜ解ける | 情景 | 一次確認 | 計 | 採否と根拠 |
|---|---:|---:|---:|---:|---:|---:|---|
| 2014年W杯オランダ×メキシコ、主審による初の冷却休憩 | 5 | 4 | 5 | 5 | 5 | 24 | **採用：d**。給水が審判の管理する中断であることが見える。今夜実施は別問題 |
| 2005年CL決勝、リバプールがハーフタイムに交代・配置変更 | 5 | 5 | 5 | 5 | 5 | 25 | **採用：f**。前半と後半で人と配置が変わる理由が具体的 |
| 2018年W杯ベルギー×日本、GKの素早い展開から11秒で決勝点 | 5 | 5 | 5 | 5 | 5 | 25 | **採用：i**。ボール奪取後の近い人の走りを観察する価値が強い |
| 2022年W杯日本×ドイツ、交代した堂安・浅野が逆転得点 | 4 | 3 | 4 | 4 | 5 | 20 | **見送り**。交代論としては良いが、本担当iの「笛なしの攻守交代」とは焦点が違い、短文で混ぜない |

採用は出来事の人物・場面・行動・結果が出典から確かめられるものに限定。ユーザー・製作者の逸話、未出典の会話や心理は一切採用していない。

## 未解決／公開後に確認すべき点

- 今夜のコイントス結果、最初に蹴るチーム、攻撃方向、選手・控えの出場、交代は現時点で未確定。
- 飲水／冷却の一斉中断が今夜実施されるかは未確認。通常の短い補水と公式中断を混同しない。
- ハーフタイムショーは19:50頃の**開催予定**。開始時刻や実施結果、選手の動線は当日の進行で変動する。
- ＋4や2-1／1-1は仕組みを説明する**例**であり今夜の実際の表示・得点ではない。
- 試合終了時刻・スコア・出来事・審判の判定は試合後の公式記録が出るまで確定扱いしない。

## 保存・変更境界

- **PR:** https://github.com/SideBySite/guide/pull/217
- **変更予定ファイル数:** 8（記事7＋本status）。
- 本担当ファイルのみ追加。固定64・LOCAL18、共有割当／候補表、別担当の原稿への変更なし。
- 別工程との同時作業は行わない。次工程EX-E/EX-D/EX-Qはこの担当では着手しない。
