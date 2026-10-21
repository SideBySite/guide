# EX-W05 執筆10件・検証記録

- 対象：2026-10-21（水）19:00 JST、味の素スタジアム、FC東京対柏レイソル。**確認基準日：2026-10-21 JST、試合開始前**。
- 対象リポジトリ：`SideBySite/guide`、保存ルート：`events/20261021-fctokyo-kashiwa/`。
- **必須先行 00-I：達成**。`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`の実ファイルを`main`で確認。追補PR #191は`main`へマージ済み（PR #183もマージ済み）。`docs/prompt-pack/manifest.json`のEX-W05依存は00-Iのみ。
- `docs/question-tree.md`（イベント配下）、`docs/prompt-pack/baseline-question-tree.md`、`shared-style.md`、`manifest.json`、既存`content/1/1-03.md`と`1-03-a.md`、両クラブのroster・assignments、確認できた`foundation-v2/basics/stadium.md`を参照。
- **結果：10件の初稿・逸話判定・推敲・検証を完了**。変更は対象10本文とこのstatusの計11ファイルのみ。固定64問、LOCAL18問、共有ツリー・候補表・割当表・02/03・FCT-PREPは変更も再実行もしない。
- PR：**#226 https://github.com/SideBySite/guide/pull/226**（専用ブランチ `ex-w05-articles-20261021`、`main`向け）。

## 記事ごとの確認

文字数は原稿本文・見出し等を対象にMarkdown装飾を除いた概数。10件すべて`ひとことで`・`しくみ`・`今日の試合で見るなら`、関連ID、出典、確認日、要点マーカー3〜4個を備える。見出し`おもしろエピソード`は成立する原典を選べた記事だけに置いた。

| ID（保存先） | L/本文概数 | 00-Iの範囲・独立性と検証結果 | 事実と未確認の区分 |
|---|---|---|---|
| 1-03-c (`content/6/1-03-c.md`) | L2/563字 | `00-A-34`、タッチ・ゴール・中央線と内側の線の役割を確認。00-A-36の弧、00-A-37の角・旗も集約。1-03の「外へ出た後の処理」と分離 | 視角による見え方は席次第 |
| 1-03-d (`content/6/1-03-d.md`) | L2/572字 | `00-A-35`、16.5mの広いペナルティーエリア／5.5mのゴールエリアを区別。1-03-cの全体図と分離 | 永井#29のGK出場・該当プレーは未確定 |
| 1-03-e (`content/2/1-03-e.md`) | L2/526字 | `B-18`、両足の一部／両手・頭上／違反時は相手のスローイン、利益適用も確認。1-03-aの一般説明と分離 | 柏が長く投げるかは不明。2008年デラップ逸話は出典で確認 |
| 1-03-f (`content/2/1-03-f.md`) | L2/505字 | `B-20`、ゴールエリアで蹴り球が明らかに動けば再開。PA内の短い受け手／相手の立ち位置例外を確認。1-03-bの再開種別と分離 | 永井#29は候補であって当日先発確定ではない |
| 1-03-g (`content/2/1-03-g.md`) | L2/512字 | `H07`（B-16を統合）、地上・空中とも球全体が境界を越える条件。1-03の再開手段と分離 | 遠い席からのぎりぎりの境界は断定しない |
| 7-05-a (`content/6/7-05-a.md`) | L2/554字 | `00-A-40`（G-18を統合）、球を供給する人と再開する選手を分けた。1-03のルールと分離 | ボールパーソンの人数・配置・供給方式は会場運用次第 |
| 7-05 (`content/7/7-05.md`) | L1/853字 | `G-15`（H39を統合）、自席の方向・二つのゴール・ベンチ・ボール外の動きを選ぶ。6-01の「最初の10分」の見方と分離 | 読者の席、選手の出場、ベンチや画面の視界は未知 |
| 7-05-b (`content/7/7-05-b.md`) | L2/466字 | `G-16`、ゴール裏の奥行きと長辺席の横幅を対比。7-05の初期位置把握と分離 | 見え方の具体度は席の高さ・列による |
| 7-05-c (`content/7/7-05-c.md`) | L2/470字 | `G-20`、大型画面・交代時の視線切替を説明。進行規則と分離 | 交代選手表示／リプレーは当日の演出次第で確約しない |
| 2-02-c (`content/2/2-02-c.md`) | L2/492字 | `B-05`（B-06を統合）、脇下境界・故意・不自然な拡大。2-02-a一般説明と分離 | 個別のハンド判定をスタンドから断定しない |

## 規則・現地情報の原典（確認：2026-10-21 JST）

- IFAB 第1条 フィールド：https://theifab.com/laws/latest/the-field-of-play/
- IFAB 第9条 イン／アウト：https://www.theifab.com/laws/latest/the-ball-in-and-out-of-play/
- IFAB 第15条 スローイン：https://www.theifab.com/laws/latest/the-throw-in/
- IFAB 第16条 ゴールキック：https://www.theifab.com/laws/latest/the-goal-kick/
- IFAB 第12条 ハンド等：https://www.theifab.com/laws/latest/fouls-and-misconduct/
- IFAB 第2条・予備ボール：https://www.theifab.com/laws/latest/the-ball/
- IFAB 2019年ルール変更の解説：https://www.theifab.com/news/laws-of-the-game-2019-20-coming-into-force-1-june-and-new-mobile-application/
- JFA 2026/27公式規則：https://www.jfa.jp/laws/soccer/2026_27/
- FC東京公式当日予定：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- スタジアム概要：https://www.ajinomotostadium.com/overview/stadium.php
- スタジアム利用案内：https://www.ajinomotostadium.com/do/do01/top.php
- スタジアム大型映像設備：https://www.ajinomotostadium.com/do/do01/facilities.php
- 柏公式選手名簿：https://www.reysol.co.jp/team/players/
- 長いスローインの逸話：2008-11-01ストーク2－1アーセナル https://www.rte.ie/sport/soccer/2008/1101/240434-stoke_arsenal/ 、後年の取材記事 https://www.skysports.com/football/news/12028/13213297/stoke-city-how-rory-delaps-undefendable-long-throws-caused-premier-league-chaos 、2009年の監督の規則変更提案 https://www.skysports.com/football/news/5803895/wenger-calls-for-rule-change

## 逸話の調査と選考

日本語・英語で独立した検索を少なくとも5つ以上実施。検索テーマ：
`スローイン 両足 反則 2026 IFAB`、
`ゴールキック ペナルティーエリア内 味方 2019`、
`ハンド 自然な位置 脇 IFAB`、
`Rory Delap Arsenal Stoke 2008 two goals long throw`、
`Wenger kick-ins Rory Delap rule change`、
`Japan Spain 2022 Mitoma ball line VAR`、
`Iran Mohammadi 2018 somersault throw-in`、
`味の素スタジアム 大型映像装置 座席`。

5点満点×5軸で順に〔笑い・驚き／今日見たくなる／なぜが解ける／情景が浮かぶ／出典で確認可能〕を採点。**高得点でも既存原稿との重複なら不採用**とした。

| 候補 | 点数 | 判断と理由 |
|---|---|---|
| 2008年ストーク対アーセナル：ロリー・デラップの長いスローインから2得点、のちにベンゲル監督が規則変更を提案 | 5/5/4/5/5＝24 | **採用：1-03-e**。人物・場面・動き・試合結果が揃い、足元を見る問いにつながる |
| 2022年W杯日本対スペイン：三笘薫がゴールライン際から折り返し、田中碧が得点 | 5/5/5/5/5＝25 | **見送り**：`content/1/1-03.md`がすでに使用。1-03-gへ重複転載しない |
| 2018年W杯イラン対スペイン：ミラド・モハマディが前転して投げようとしたが普通に投げ直す | 5/4/3/5/5＝22 | **見送り**：`content/1/1-03.md`がすでに使用。1-03-eへ重複転載しない |
| 2019年ゴールキック規則変更とGKのショートパス | 3/5/5/3/5＝21 | **逸話として見送り**：制度変更であり人物・具体的な出来事・結末の揃った話ではない。1-03-fのしくみに記載 |

ほかの9記事は、数字・一般的説明で逸話欄を埋めず省いた。読者・製作者本人の経験、回想、私生活の情報・リンクは扱っていない。

## 推敲・差分確認・未解決

- 各記事の初出用語をかっこ内で説明し、サッカー初観戦の大人へ短い段落で記述。太字・黄色マーカー、見出し、関連先、出典を目視・機械的に確認。
- 予想：永井堅梧#29の出場、両クラブの出場選手、ベンチの交代、柏の長いスローイン。**確認済み**なのは制度・会場設備・クラブ公式の開催予定および選手の候補名簿であり、未来のプレーを保証しない。
- 保留：当日公式先発、実際のボールパーソン配置・再開方式、スクリーンの出力内容、座席固有の視界、個々の審判判定。**この記事群の未完成理由にはせず、断定を避ける**。
- 各記事内の`checked_at: 2026-10-21`は執筆時の確認日であって資料そのものの公開日ではない。
