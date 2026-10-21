# EX-W07 執筆・検証完了

- 対象：2026-10-21（水）19:00 JST／味の素スタジアム／FC東京 × 柏レイソル／2026/27明治安田J1第11節。
- 調査・原稿確認基準日：**2026-10-21 JST、キックオフ前**。URLの公開日・事象発生日・確認日を区別する。
- 専用ブランチ：`soccer/20261021-ex-w07-referees`。
- 担当PR：**[#219](https://github.com/SideBySite/guide/pull/219)**。
- 完了：**L2 8記事／8記事**。個別記事の本文計数（空白とMarkdown装飾・見出しを除く概数）：d 497字／e 438字／f 420字／g 444字／h 428字／i 453字／j 445字／k 423字。全件250〜600字。1問1ファイル、「ひとことで」「しくみ」「今日の試合で見るなら」を確認。
- 本人・製作者の体験・回想：**一切使用なし**。記事の逸話は選手・クラブに関する出典で検証できる公開事実のみ。
- 書込ファイル：`content/2/2-03-{d,e,f,h,i,k}.md`、`content/3/2-03-{g,j}.md`、本statusの計9ファイル。共有ツリー、固定64問、LOCAL18問、割当表、他担当原稿は変更しない。

## 必須先行・区分けの確認

- **00-Iの実ファイル**：`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`がmainに存在し、内容を確認した。
- **mainマージ**：00-I追補の[PR #191](https://github.com/SideBySite/guide/pull/191)が2026-10-21 14:12 JSTにmainへmerged済みとGitHub APIで確認。00-Jの[PR #194](https://github.com/SideBySite/guide/pull/194)もmerged済み。資料の存在を未完了先行と混同しない。
- `docs/prompt-pack/manifest.json`のEX-W07は`depends_on: ["00-I"]`、許可9パスと一致。現行の`content/2/2-03.md`、`2-03-a.md`、`2-03-b.md`、`2-03-c.md`、スタイル仕様、固定64問の資料を参照。02/03やFCT-PREPは再実行していない。
- 00-I `answer_scope / why_distinct / fact_check`を8件ごとに参照。d=接触方法と処分、e=人数の穴、f=脳振盪の例外、g=同じ選手の復帰、h=四角の合図、i=映像確認の権限、j=審判間の担当、k=得点成立の確認。親の一般説明・他記事と同じ答えにしない。

## 記事別事実確認（全件2026-10-21 JST確認）

| ID・ファイル | 00-I対応 | 検証結果 | 未確認・取り扱い |
|---|---|---|---|
| 2-03-d `content/2/2-03-d.md` | B-33 | JFA第12条の不用意／無謀／過剰な力と懲戒を照合。10/17染野唯月の足裏での退場と10/19懲戒公表を確認 | その実例で「ボールに先に触れた」とは断定しない |
| 2-03-e `content/2/2-03-e.md` | B-35 | JFA第3条：キックオフ後の退場は補充不可、キックオフ前で登録済み控えによる補充は条件付き。GK退場でも人数は戻らない | 10/21に退場者が出るか、柏#4の出場と位置変更は未確定 |
| 2-03-f `content/2/2-03-f.md` | B-37 | J1概要：通常5人・3回、脳振盪各チーム1人と相手の追加1人。10/17柏若原→永井の13分と、名古屋高嶺→佐藤の85分の追加枠をJリーグ公式データの備考で照合 | 10/21の交代理由と負傷状態を予想しない |
| 2-03-g `content/3/2-03-g.md` | B-38 | JFA第5条とIFAB2026/27：負傷停止・場内診察後は原則再開後1分、許可後復帰。再入場する境界線と主な例外を確認 | 個別の傷病・当日の治療判断、例外の該当は現場情報がなければ未確定 |
| 2-03-h `content/2/2-03-h.md` | B-42 | 四角のTVシグナルとチェック／レビューの区別、OFRとVAR情報のみの決定、J1のVAR全380試合を照合 | 四角を描くだけで判定変更とは解釈しない。10/21の発生未確定 |
| 2-03-i `content/2/2-03-i.md` | B-44 | IFAB2026/27の4大対象に加え、明らかに誤った2枚目警告の退場を確認。見逃された2枚目を遡って発行しない | 明らかな誤CKの迅速レビューは大会選択制。J1導入の公開裏付けが見つからず**未確認** |
| 2-03-j `content/3/2-03-j.md` | B-45 | JFA第5・6条で主審／副審／第4の審判の職務を照合 | 当日の審判担当者名、座席からの視認性を断定しない |
| 2-03-k `content/2/2-03-k.md` | H11 | IFAB第10・11条と5/6FC東京対千葉の公式マッチレビュー（稲村隼翔の押し込みがオフサイドにより無効）を確認 | 10/21の得点・場内ビジョン表示・判定内容は未確定 |

## 逸話候補の調査・採否

日英の複数検索（**5検索以上**）を行った。例：`2026 10月17日 柏 若原 永井 脳振盪`、`2026 10月17日 東京ヴェルディ FC東京 退場`、`2026 J1 VAR ゴール取り消し`、`IFAB 2026 27 off field treatment exceptions`、`IFAB 2026 27 second caution VAR optional corner`、`2026 football VAR disallowed goal official`、`site:jfa.jp/laws/soccer/2026_27/ 1分 復帰`。以下は5点満点で「驚き／今日確かめたい／なぜの解消／情景／公式根拠」の順に採点した。

| 実例候補 | 5項目の得点 | 採否と理由 |
|---|---|---|
| 2026-10-17東京V×FC東京、染野唯月の足裏による前半18分退場、10/19の懲戒 | 4 / 5 / 5 / 4 / 5 | **採用 d**。誰がいつ何をして処分されたか揃い、足の入り方を見る理由を具体化。ただしボールへの先触りは未立証なので補わない |
| 2026-10-17柏×名古屋、若原→永井の脳振盪交代と名古屋の85分追加交代 | 5 / 5 / 5 / 5 / 5 | **採用 f**。両クラブがどう動き、交代数がなぜ増えたか、備考で同時確認できる |
| 2026-05-06 FC東京×千葉、稲村隼翔の押し込みがVAR確認後オフサイドとなり無効 | 5 / 5 / 5 / 5 / 5 | **採用 k**。誰・場面・行為・判定の結果が揃い、シュート後の観察が変わる |
| 「VARならすべてのカードを後から取り消せる」とする未特定のSNS談 | 2 / 3 / 1 / 2 / 0 | **見送り**。発言者・試合・原典が特定できず、規則に反するおそれ |

d/f/kの見出し「おもしろエピソード」は上記3例だけ。残り5記事は、無理に雑学を逸話として膨らませなかった。

## 公式出典URLと確認日

以下を**2026-10-21 JST・試合前**に照合。事象の日付と確認日は別。

- JFA 2026/27競技規則（第3・5・6・10・11・12条、VAR実施手順）：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB反則と懲戒：https://www.theifab.com/laws/latest/fouls-and-misconduct/
- IFAB選手・退場：https://www.theifab.com/laws/latest/the-players/
- IFAB主審・負傷者復帰：https://www.theifab.com/laws/latest/the-referee/
- IFAB場外治療・評価：https://www.theifab.com/laws/latest/off-field-treatment-and-assessment-protocol/
- IFAB VARプロトコル：https://www.theifab.com/laws/latest/video-assistant-referee-var-protocol/
- IFAB2026/27変更点：https://www.theifab.com/law-changes/latest/
- IFAB副審・第4審判：https://www.theifab.com/laws/latest/the-other-match-officials/
- IFAB勝敗・得点：https://www.theifab.com/laws/latest/determining-the-outcome-of-a-match/
- IFABオフサイド：https://www.theifab.com/laws/latest/offside/
- J1大会概要・当日試合情報：https://www.jleague.jp/outline/j1/ ／ https://www.jleague.jp/match/j1/2026/102108/
- 柏10/17公式記録：https://www.reysol.co.jp/game/results/202627/1017.php
- Jリーグ公式データ／10/17柏×名古屋の特別交代備考：https://data.j-league.or.jp/SFMS02/?match_card_id=34614
- Jリーグ10/17東京V×FC東京：https://www.jleague.jp/match/j1/2026/101708/
- Jリーグ10/19懲戒発表：https://aboutj.jleague.jp/corporate/news/article/88
- Jリーグ5/6FC東京×千葉のレビュー：https://www.jleague.jp/match/j1/2026/050601/review/
- FC東京10/21試合前案内：https://www.fctokyo.co.jp/match/schedule/info/20261021/

## 終了前チェック・保留

- 原稿8ファイルとstatusの**計9パスのみ**を変更する。新規ファイル以外は変更しない。
- スマホ短時間読了、3段落以下／短文中心、初出専門語の言い換え、強調、各記事3つ以上の`==要点==`、選手と「今日の試合で見るなら」を確認。
- 保留（当日確認）：先発・交代・実際の判定・選手のけがと復帰・会場映像の運用。
- 保留（大会運用）：選択制CKのVAR確認をJ1が採用するか、公式概要だけでは不明。推測で補っていない。
- PR #219の変更パス照合・マージ結果はGitHubのPR履歴を正とする。