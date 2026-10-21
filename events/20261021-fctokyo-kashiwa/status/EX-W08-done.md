# EX-W08 執筆8件 完了記録

- **対象**：2026年10月21日（水）19:00 JST、味の素スタジアム、2026/27明治安田J1リーグ第11節 FC東京×柏レイソル。
- **確認基準日**：2026-10-21 JST、試合開始前。記事内の「今日」はこの試合を指す。以下の資料公開日と照合日を混同しない。
- **成果**：指定の8記事を1問1ファイルで新規作成。本人・製作者の個人的体験は収録しない。
- **担当境界**：このstatusとEX-W08指定8記事のみ編集。固定64問・LOCAL18問、共有候補/割当、他担当原稿、02/03、FCT-PREPは無変更。
- **先行検証**：mainの`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`の実在を確認。00-I追補PR [#191](https://github.com/SideBySite/guide/pull/191)は**merged**。00-Jの`status/00-J-done.md`と`docs/prompt-pack/manifest.json`のEX-W08記事割当も確認。資料があることと先行必須条件を区別し、00-Iだけを必須条件とした。
- **PR**：[**#223：EX-W08 執筆8件**](https://github.com/SideBySite/guide/pull/223)。専用ブランチ`soccer/ex-w08-gk-build-up-20261021-01`からmainへ。マージ結果はGitHub PRの状態を正とする。

## 00-Iの境界と8記事の検証

| ID / ファイル | 00-I | 主に答える範囲（差別化） | 本文字数（Markdown記号・見出し・関連注記込み） | 検証結果 |
|---|---|---|---:|---|
| `6-05-a` / `content/2/6-05-a.md` | B-40 | インプレー中の手・腕による8秒保持、最後の5秒の主審表示。アウト後の再開と混同しない | 498 | 2026/27競技規則第12・17条の8秒、最後の5秒、相手CKを照合。違反の発生は予想しない |
| `6-05` / `content/6/6-05.md` | D-01 | ボールが遠い時のGKの縦横移動と後方支援。一般の守備準備`6-03-a`よりGK一人へ限定 | 902 | FIFAの高い位置・味方の守備列との関係と規則上の手の扱いを照合。GKの当日先発と行動理由は未確定 |
| `6-05-b` / `content/6/6-05-b.md` | D-02 | 短く出す時の味方の開き方。再開規則そのものを説明する`1-03-b`とは区別 | 530 | 競技規則第16条とFIFA配球分類を照合。短い配球を選ぶ頻度は未確定 |
| `6-05-c` / `content/6/6-05-c.md` | D-03 | 前進の効用と無人の背後というリスク。D-01の広い行動説明より距離と危険に絞る | 483 | FIFA GK位置解説、2026-10-18実例を照合。GK本人の意図は推定しない |
| `6-05-d` / `content/6/6-05-d.md` | D-04 | シュート前の横移動、立つ角度と反応の構え。前進のリスクとは分離 | 419 | FIFAのセットポジションを照合。マルセロ ヒアンが出場する場合のみ観察 |
| `4-04` / `content/4/4-04.md` | C-01 | 後方で回す理由、反対側の空き、奪われた時の危険。一般戦術`4-01`とは区別 | 923 | FC東京監督の公開インタビューとFIFAの後方支援の仕組みを照合。当夜の実施は仮説 |
| `4-04-a` / `content/4/4-04-a.md` | C-02 | GK経由で変わるパス経路と意図的な味方の足からの戻しを手で扱えない規則 | 473 | JFA/IFAB第12条とFIFA後方配球を照合。実際の起用と戻す回数は未確定 |
| `4-04-b` / `content/4/4-04-b.md` | C-03 | 相手を近づけることで生まれる背中側の空間と失敗の危険 | 438 | FIFAの圧力下でのパス経路づくりを照合。相手を「意図的に引きつけた」は断定しない |

- **体裁検証**：全8ファイルに`## ひとことで`、`## しくみ`、`## 今日の試合で見るなら`、出典を含むYAML、関連IDを付与。黄色マーカーは各3〜5箇所。L1は各500〜1000字、L2は250〜600字（上記はMarkdown込みの機械的な文字数）。「おもしろエピソード」は出典のある2記事のみ。
- **差分確認対象**：上記8ファイルと本status、合計9ファイル。固定64問、LOCAL18問、既存02/03やFCT-PREPの原稿は変更しない。

## 出典URLと確認日

**以下のウェブ根拠を2026-10-21 JST（試合開始前）に照合**。公開日が別に判明するものは併記する。各記事の`sources`に個別の採用先を記録。

- 2026/27 JFA公式競技規則（GK手の8秒、最後の5秒、相手CK、バックパス、ゴールキック）：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB 第12条（GK保持と意図的な足のパス）：https://www.theifab.com/laws/latest/fouls-and-misconduct/
- IFAB 第16条（ゴールキック、ボールが明確に動くとインプレー）：https://www.theifab.com/laws/latest/the-goal-kick/
- IFAB 2025/26変更点（8秒保持導入経緯）：https://www.theifab.com/law-changes/2025-26/
- FC東京 10月21日試合案内：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏 10月21日試合案内：https://www.reysol.co.jp/game/results/202627/1021i.php
- Jリーグ該当試合公式：https://www.jleague.jp/match/j1/2026/102108/
- FC東京 松橋力蔵監督インタビュー（**公開日2026-06-20**、今夜の戦法確約ではない）：https://www.fctokyo.co.jp/fan/fanzone/detail/336734/
- FIFA GKの位置・配球分析（**公開日2022-12-03**）：https://www.fifatrainingcentre.com/en/fwc2022/fifa-insight/fifa-insight-ep03.php
- FIFA GKの後方サポート練習：https://www.fifatrainingcentre.com/en/practice/elite-sessions/goalkeeper/goalkeepersbuildup.php
- FIFA GKシュート前セット姿勢：https://www.fifatrainingcentre.com/en/game/tournaments/fifa-womens-world-cup/2023/post-tournament-analysis/goal-preventions.php
- FIFA キャッチのための足の運び・横移動：https://www.fifatrainingcentre.com/en/environment/fifa-goalkeeper-training/goalkeeping-fundamentals/learning-to-catch.php
- FC東京 2026/27公式名簿：https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27
- 柏 2026/27公式名簿：https://www.reysol.co.jp/team/players/
- FC東京 10月17日記録：https://www.fctokyo.co.jp/match/schedule/result/20261017/
- 柏 10月17日記録：https://www.reysol.co.jp/game/results/202627/1017.php

## 逸話調査（日本語・英語合わせて5検索以上）

実施した検索群（少なくとも12検索）：`IFAB goalkeeper 8 seconds 2026`、`IFAB keeper backpass 2026`、`FIFA goalkeeper positioning`、`FIFA goalkeeper distribution`、`FC東京 柏 2026 10月21日`、`keeper 8 second offence 2025`、`site:liverpoolfc.com Alisson Salah 2020`、`site:fifa.com Neuer Algeria 2014`、`2026 halfway line goalkeeper goal`、`site:fctokyo.co.jp 松橋力蔵 後方ビルドアップ`、`site:theifab.com goal kick law 16`、`site:fifatrainingcentre.com goalkeeper set position`。候補は「誰が、いつどこで、何をしてどうなったか」を確認。5項目は各5点満点。

| 候補・根拠 | 笑い/驚き | 今日見たくなる | なぜが解ける | 情景 | 出典で確認 | 採否と理由 |
|---|---:|---:|---:|---:|---:|---|
| **2020-01、リバプールGKアリソンからサラーへの長いパスと得点** [クラブ公式](https://www.liverpoolfc.com/news/first-team/383826-alisson-becker-form-expectation-jurgen-klopp)（記事公開2020-01-22） | 4 | 5 | 5 | 5 | 5 | **採用／6-05-b**。短い配球との対比で「距離より空き」を具体化 |
| **2026-10-18、ブライトンのディエゴ・ゴメスが前に出たGKの上を越える51mの得点** [Reuters](https://www.reuters.com/sports/soccer/brightons-gomez-scores-spectacular-goal-halfway-line-2026-10-18/)（同日公開） | 5 | 5 | 4 | 5 | 5 | **採用／6-05-c**。前進の危険を可視化。ただしGKの前進自体を失策と断定しない |
| **2014ドイツ対アルジェリア、ノイアーが前へ出てパスを防ぐ** [参考：FIFA GK一般分析](https://www.fifatrainingcentre.com/en/fwc2022/fifa-insight/fifa-insight-ep03.php) | 4 | 4 | 4 | 5 | 2 | **見送り**。当該試合の動作と結末を十分に裏付ける一次資料を今回確保できないため数字や場面を本文へ使わない |

**逸話を無理に増やさない判断**：審判の8秒やGKのシュート前姿勢は規則・技術説明で十分。エピソード欄を形式だけで置かない。選手・クラブの歴史に限り、公開根拠のある第三者の話を用いた。制作者の体験・回想は調査も転載もしていない。

## 未解決・試合開始後にしか確定できない点

- FC東京**キム スンギュ**、柏**永井堅梧**、FC東京**マルセロ ヒアン**は、2026-10-17起用と試合前の公式登録名簿に基づく観察候補。**10/21当日の出場・先発・位置は未確認**。発表後は実際の選手を使って観察する。
- FC東京や柏が今夜短くつなぐか、どの位置までGKが前進するか、何秒球を持つか、主審の実際の判定は未確定。記事中では一般原理と「今日確かめる問い」を区別した。
- 00-Iの`fact_check`にある審判の手の表示、ゴールキックの再開とバックパスの手の禁止はルールとして確認済み。ただし具体的な判定発生、指示、心理は外から断定しない。
