# EX-W04 執筆9件・検証完了記録

- 基準：**2026-10-21 JST、19:00キックオフ前**。対象は味の素スタジアムの2026/27明治安田J1第11節、FC東京対柏レイソル。
- 成果：**新規9問／9ファイル、執筆・推敲・初版事実確認を完了**。専用ブランチ `soccer/20261021-ex-w04-writing`、PR **#221**（https://github.com/SideBySite/guide/pull/221）。本記録を含めた変更は担当指定の10ファイルのみ。
- 必須先行：`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md` の**実ファイルをmainで確認**。00-IのPR [#191](https://github.com/SideBySite/guide/pull/191) は2026-10-21 05:12:32 UTCにmainマージ済み。00-JのPR [#194](https://github.com/SideBySite/guide/pull/194) もmainマージ済み。対象9候補は00-Iの決定表で全件「採用」。
- 整合：`docs/question-tree.md`、固定64問のbaseline、shared-style、manifestのEX-W04、既存の7-03・1-01・6-03記事、両クラブのroster・assignments、完成済みfoundation-v2/facts/match.mdを参照。**固定64問・LOCAL18問、共有候補表、担当表、テンプレート、他担当の本文は変更なし**。02/03・FCT-PREPの再実行なし。人物詳細名鑑は本担当に含めない。
- 照合方式：各本文にfrontmatter（`sources`、`checked_at: 2026-10-21`、`needs_check`）、見出し「ひとことで」「しくみ」「今日の試合で見るなら」を備える。初出専門語には言い換え、強調・黄色マーカーは各3〜6か所。本文の非空白文字数でL1 500〜1000、L2 250〜600を点検。

## 記事ごとの校正・検証

| 正式IDと保存先 | 本文字数（空白除く） | 調べた相違点／確認済み | 当日まで残る確認 |
|---|---:|---|---|
| 7-03-a `content/1/7-03-a.md` | 529 | 00-A-26：帰路の総論と分離。相手、ベンチ、観客への挨拶の宛先を区別。 | 両クラブの実際の挨拶・順序・実施有無。 |
| 7-03-b `content/7/7-03-b.md` | 527 | G-43：飛田給駅、試合後の特急・急行臨時停車予定、直行シャトルバスなし。 | ダイヤ変更、入場規制、混雑、試合終了・乗車時刻。 |
| 7-03-c `content/7/7-03-c.md` | 516 | G-45：終了後のベンチ・スタッフ・選手と場内マナーに限定。交通とは分離。 | 演出、選手挨拶、誘導開始時刻。 |
| 6-04 `content/6/6-04.md` | 897 | 00-A-28：試合中のスコアの探し方と読み間違いの防止。勝敗の規則とは分離。 | 席から画面の見え方、当日の得点・判定。 |
| 6-04-a `content/6/6-04-a.md` | 463 | 00-A-29：得点欄の左右は固定せずチーム名と数字で判別。 | 今日の会場表示の左右。 |
| 6-04-b `content/6/6-04-b.md` | 521 | 00-A-30：45分×2、追加時間は最短、終了判断は主審。 | 味スタの時計表示方法、実際の追加時間。 |
| 1-01-c `content/6/1-01-c.md` | 585 | 00-A-32：GK服色の識別規則。2019年ウォーカーのGK出場はクラブ公式で検証。 | 両チームGKの服色・先発。 |
| 1-01-d `content/2/1-01-d.md` | 550 | B-39：エリア内外、確保中の保護、保持8秒・CK、味方からの戻し球は別記事へ。 | 柏#29永井の出場とプレー地点。 |
| 1-01-e `content/2/1-01-e.md` | 593 | B-41：意図的な足の戻し球、味方スローイン、跳ね返りとの区別、間接FK。1992年の導入をUEFA資料で確認。 | 当日の故意性や違反認定は主審に依存。 |

※字数は出典メタデータを除くMarkdown本体の非空白文字数。装飾記号・見出し等を含むため本文の見た目の字数は多少少ない。

## 日本語・英語の調査、逸話候補の採否

検索・照合は日英合わせて**11件以上**実施。主な検索語：①「FC東京 柏 飛田給 臨時停車」②「ゴールキーパー バックパス 2026」③「GK 8秒 ルール」④「試合終了後 スタンド 挨拶」⑤「football goalkeeper shirt colour law 4」⑥「football law 7 duration」⑦「Olivier Giroud goalkeeper Genoa」⑧「Kyle Walker Atalanta goalkeeper 2019」⑨「Harry Kane goalkeeper Asteras 2014」⑩「FIFA 1992 back pass rule Denmark」⑪「柏 永井堅梧 29」。

採点は**驚き／今日の見方／なぜが解ける／情景／原典で検証できる**の順に各5点満点。場面・人物・行動・結果がそろうことを確認し、現代のルール・今日の状況へ無理につなげない。

| 候補 | 5項目の点 | 合計 | 採否と理由 |
|---|---|---:|---|
| 2019/11/6：マンチェスター・シティのGK退場後、守備選手カイル・ウォーカーが交代でGKを務め、1-1で終えた | 5/5/5/5/5 | 25 | **採用：1-01-c**。服で識別するGKが予想外の人物に代わる場面。クラブ試合報告で確認できる。 |
| 2014/10/23：トッテナムのハリー・ケインが3得点後、一時GKを担当した | 5/4/3/5/5 | 22 | **見送り**。クラブ史料で確認できるが、緊急GKという主題が前候補と重複し、短いGK服装記事で重ねる意味が薄い。 |
| 1992年のデンマーク代表がGKへの戻し球を多用した欧州選手権（のちのバックパス規則導入期） | 3/5/5/4/5 | 22 | **逸話としては見送り**。個別の因果を単純化しないため。1-01-eの「歴史・由来」だけに、UEFAが確認する1992年の規則導入を採用。 |

事実確認した候補原典：
- Manchester City試合報告：https://www.mancity.com/news/first-team/match-report/2019/november/atalanta-man-city-champions-league-match-report-6-november
- Tottenham公式回顧：https://www.tottenhamhotspur.com/news/1009729/the-archive-spurs-5-1-asteras-tripolis-231014
- UEFA goalkeeper coaching（PDF p.9、1992年導入）：https://editorial.uefa.com/resources/0285-190a81f7e091-323e8bfbc968-1000/uefa_goalkeeper_coaching_en.pdf
- Opta Analyst EURO 1992の戻し球：https://theanalyst.com/articles/european-championship-history-1990s

## 主な公式根拠と確認基準日

以下はすべて**2026-10-21 JST・試合開始前に確認**したページ。各ページの公開日と確認日は別。
- FC東京の10/21試合案内：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏の試合案内：https://www.reysol.co.jp/game/results/202627/1021i.php
- Jリーグ当該試合：https://www.jleague.jp/match/j1/2026/102108/
- **FC東京が2026-10-20に公開**した交通案内：https://www.fctokyo.co.jp/news/details/342758/
- 味スタ当日イベント・臨時停車時刻：https://www.ajinomotostadium.com/schedule/2026/1021_16099.php
- 味スタ交通：https://www.ajinomotostadium.com/access/index.php
- FC東京観戦マナー：https://www.fctokyo.co.jp/stadium/manners/
- JFA 2026/27競技規則：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB第4条・GK服色：https://www.theifab.com/laws/latest/the-players-equipment/
- IFAB第12条・GK手の扱い：https://www.theifab.com/laws/latest/fouls-and-misconduct/
- FA第7条・45分と追加時間：https://www.thefa.com/football-rules-governance/lawsandrules/laws/football-11-11/law-7---the-duration-of-the-match
- 柏#29永井堅梧の所属・位置：https://www.reysol.co.jp/team/players/2026/29.php

## 保留・境界

- **原稿の執筆・検証作業：保留0件。** ただし `needs_check: true` は事実未確認の放置ではなく、試合開始・終了後に初めて確認できる事項（GK先発、得点、画面表示、挨拶、混雑、鉄道変更）の明示。
- 選手の心理、審判の当日判定、試合後イベントの実施を予言しない。FC東京#81キム スンギュ／柏#29永井堅梧などは**候補であり先発確定ではない**。
- 本人・製作者本人の観戦体験・私生活・回想・旧makerへの導線は使用せず、将来の提供も求めない。
- PR：https://github.com/SideBySite/guide/pull/221 。PR #221 のmain反映後、`main`上の10ファイルの存在とPRのmerged状態を確認して完了を確定する。
