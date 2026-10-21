# EX-W10｜執筆10件・検証記録

- **状態**：10件の本文を新規執筆、記事別照合・逸話採否・推敲を実施。PR [#228](https://github.com/SideBySite/guide/pull/228)。main反映の最終確認はPRマージ後に行う。
- **対象**：2026-10-21（水）19:00 JST、味の素スタジアム、FC東京×柏レイソル。**確認基準**：2026-10-21 JST、キックオフ前。2026/27 J1第11節。
- **必須先行**：mainの `discovery/00-I/proposed-tree.json`（対象C-21〜26、D-24、C-28〜30のanswer_scope/why_distinct/fact_check）、`decisions.csv`、`coverage.md`、`status/00-I-done.md` を実ファイルとして確認。00-IのPR #183・#191はstatusとmanifestにmain反映記録あり。00-Jの正式ID・担当表も確認。
- **参照**：`docs/question-tree.md`、`docs/prompt-pack/baseline-question-tree.md`（固定64問）、`docs/prompt-pack/shared-style.md`、`docs/prompt-pack/manifest.json`、`docs/prompt-pack/runtime/prompts/EX-W10.md`、FC東京／柏のroster・lineup・assignments、完成済みの`content/5/5-02.md`等。
- **非編集**：02/03・FCT-PREPは再実行していない。共有候補表、割当表、固定64問、LOCAL18問、別担当の原稿・人物カード、本人・製作者の逸話・旧maker導線は変更していない。
- **区別**：10/10、10/17の選手登録・出場・得点は記録を根拠とする確定情報。今夜の先発、選手配置、交代、観察したいプレーの実現は予想・条件付き観察であり、試合結果を先取りしていない。

## 記事別検証結果

文字数は見出しを含む本文の簡易計数（Markdown記号除外）。全件に `ひとことで`、`しくみ`、`今日の試合で見るなら` を設置し、要点マーカー3〜5箇所、初出用語の説明、今日の場面と留保を確認した。

| ID | レベル／本文字数 | 00-I候補 | 検証と範囲の切り分け | 結果 |
|---|---|---|---|---|
| 4-08 | L1／824 | C-21 | 幅・出口・離れ過ぎる弱点／遠藤・久保の出場は条件付き。2022年日本対スペインの出典付き逸話。 | 合格 |
| 4-08-a | L2／442 | C-22 | 横幅の一般論ではなく遠くに残る準備と目線。左端担当は未確定。 | 合格 |
| 4-08-b | L2／456 | C-23 | ボールを端へ動かした後の中央守備のズレ。必ず空くとは断定しない。 | 合格 |
| 4-08-c | L2／440 | C-24 | 外側の2人対1人／守備者の助け方を観察。遠藤の相方は未確定。 | 合格 |
| 4-08-d | L2／456 | C-25 | 外から追い越す走りと守備の選択、失った後の備え。安斎の実走は未確定。 | 合格 |
| 4-08-e | L2／485 | C-26 | 横方向の大きな移動・飛行中の守備・受け手の止め方。久保→遠藤は仮定の例。 | 合格 |
| 4-08-f | L2／457 | D-24 | 端で待つ人が中央へ侵入する瞬間と背後の死角。規則参照、得点率は断定せず。 | 合格 |
| 4-09 | L1／866 | C-28 | 前線の人が縦の空間を作る仕組みと無視された場合。2018年ベルギー対日本の出典付き逸話。 | 合格 |
| 4-09-a | L2／439 | C-29 | 二人の守備者の境目と受け渡し。選手の心理は顔の向きから断定しない。 | 合格 |
| 4-09-b | L2／484 | C-30 | 出し手との走り出しの同期。オフサイド位置と反則を分け、2026/27規則を照合。 | 合格 |

## 調査ログ・逸話の選定

**日本語と英語を合わせて12検索以上**（2026-10-21 JST）。検索語の例：`FC東京 柏 10月21日 公式`、`柏 10/17 遠藤 久保 藤尾 小泉`、`football-lab formation 柏 FC東京`、`オーバーラップ サイドチェンジ サッカー`、`IFAB offside first point of contact`、`football width switch of play tactical explanation`、`2018 Belgium Japan Lukaku dummy Chadli`、`2022 Japan Spain Mitoma Tanaka FIFA`、`2014 Brazil Germany Müller Klose screen`。各評価は「驚き／今日見たくなる／なぜが解ける／情景／出典確実性」各5点、満点25点。

| 候補 | 点数（5軸、合計） | 採否・根拠 |
|---|---|---|
| 2022年日本対スペイン：右から来た球を逆側の三笘が折り返し田中が得点 | 5/5/4/5/5＝24 | **採用：4-08**。幅を使って逆側の選手が関わる具体例。FIFA公式で人・場面・結果まで確認。 |
| 2018年ベルギー対日本：ルカクが低いパスを通し、後方のシャドリが決勝点 | 5/5/5/5/5＝25 | **採用：4-09**。先頭の選手が触らなくても結果を変えた試合。FIFA公式で途中交代から得点まで確認。 |
| 2014年ドイツ対ブラジル：コーナーキック時のクローゼの動きでミュラーが空いて得点 | 4/4/4/5/5＝22 | **見送り**。史実と局面は確認できるが、今回の端・前線の流れに比べセットプレーの説明へ逸れやすい。記録だけで無理に採用しない。 |

採用した逸話以外のL2は、条件にかなう逸話で埋めず仕組み・今夜の観察に集中した。

## 出典URLと確認基準日

すべて**2026-10-21 JST・試合開始前に閲覧・照合**した。元ページの更新日と執筆確認日を混同しない。各記事のfront matterにも記事別出典と`checked_at`を残す。

- FC東京 10/21試合前案内（19時・味スタ）：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- Jリーグ 10/21試合：https://www.jleague.jp/match/j1/2026/102108/
- Jリーグ 10/10出場表：https://www.jleague.jp/match/j1/2026/101009/lineup/
- 柏 10/17対名古屋公式記録（遠藤、久保、藤尾、小泉、古賀）：https://www.reysol.co.jp/game/results/202627/1017.php
- 柏 2026/27配置（サイト更新表示2026-10-12）：https://www.football-lab.jp/kasw/formation
- FC東京 2026/27配置（サイト更新表示2026-10-19）：https://www.football-lab.jp/fctk/formation
- JFA 競技規則2026/27：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB Law 11／Offside：https://www.theifab.com/laws/latest/offside/
- FIFA 2022年日本対スペイン回顧（2026-01-17公開）：https://www.fifa.com/en/articles/world-cup-upsets-japan-spain-2022
- FIFA 2018年ベルギー対日本回顧：https://inside.fifa.com/news/worldcupathome-belgium-japan-russia2018-3071468
- Opta Analyst 2014年ドイツ対ブラジル（見送り候補検証）：https://theanalyst.com/articles/brazil-1-7-germany-stats-story

## 未解決事項・最終確認

- 試合直前の**正式先発・控え、左右の配置、当日の実際の交代、勝敗・得点**は未確定。本文は「出場すれば」など条件で留保し、今後の公式発表の再確認対象とする。
- フォーメーション集計は開始時の傾向で、今日の動作の実証ではない。選手の意図、声の内容、心理、因果関係の確定はしていない。
- PR：https://github.com/SideBySite/guide/pull/228
- 編集許可範囲：`content/4/4-08{,-a,-b,-c,-d,-e}.md`、`content/6/4-08-f.md`、`content/4/4-09{,-a,-b}.md`、本statusのみ。差分検証の後、自分のPRだけmainへマージする。
