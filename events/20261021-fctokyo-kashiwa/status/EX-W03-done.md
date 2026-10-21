# EX-W03 執筆10件｜完了・検証記録

- 対象：2026年10月21日（水）19:00 JST、味の素スタジアム、FC東京対柏レイソル。**試合前原稿**。
- 作業・一次資料確認日：**2026-10-21 JST**。クラブ・リーグ・規則の公表時点と、こちらの確認日は区別する。
- 原稿数：**10/10**。L1×2、L2×8。各記事を別コミットで新規保存。
- PR：**[#222](https://github.com/SideBySite/guide/pull/222)**。専用ブランチ：`work/ex-w03-20261021-whistles-free-kicks`。
- 編集範囲：下表の10ファイルとこのstatusのみ。固定64問・LOCAL18問、共有候補・割当表・別担当本文、ルートの旧野球記事を変更していない。02/03・FCT-PREPの再実行なし。
- 個人の観戦経験、ユーザーや製作者の回想・生活の物語を調査・転載・掲載していない。

## 必須先行（資料の存在だけではなくmain保存を確認）

- mainの実ファイル：`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`status/00-I-done.md`をすべて閲覧。起点はすべて`events/20261021-fctokyo-kashiwa/`配下。
- **00-I追補PR #191**は2026-10-21 05:12:32 UTC（14:12:32 JST）に**mainへマージ済み**：https://github.com/SideBySite/guide/pull/191
- 参照：`docs/question-tree.md`、`docs/prompt-pack/baseline-question-tree.md`、`shared-style.md`、`manifest.json`、`foundation-v2/spec/content-template.md`、`docs/current-foundation.md`、既存`content/2/2-03.md`と`2-02-b.md`、柏・小西雄大名鑑。
- **00-Iのanswer_scope/why_distinct/fact_checkを10件個別に照合**。再開の笛の要否／医療処置後／笛で止める理由／続行判断／後から警告／蹴るまでの待機／FK地点・種類／壁／片腕の合図／早い再開を分離した。

## 記事別検証（記事本文の空白・マークダウン装飾除外の概算字数）

| ID（保存場所） | 階層・本文概算 | 原典・論点の確認 | 要点・残す注意 |
|---|---:|---|---|
| 2-04-a（content/1） | L2・453字 | IFAB笛ガイド・JFA、UEFA | スローイン等とキックオフの笛を分離。聞こえないことと吹かないことを同一視しない |
| 2-04-b（content/1） | L2・370字 | IFAB第5条・2026/27改正・Jリーグ8/25告知 | 治療・原則1分の待機、復帰許可と例外。全員に一律適用しない |
| 2-04（content/2） | L1・825字 | JFA・IFAB主審・FC東京/Jリーグ公式試合 | 停止理由、接触と反則の違い、笛後の腕／再開権。個別判定は断定しない |
| 2-04-c（content/2） | L2・348字 | JFA・IFAB第5条 | アドバンテージと「反則なし」の区別。腕と続いた攻撃を一緒に見る |
| 2-04-d（content/2） | L2・366字 | JFA・IFAB第12条・2026/27変更 | 続行後の警告と適用例外。具体的な選手のカードは予想しない |
| 2-06-a（content/1） | L2・386字 | JFA・IFAB第13条・改正 | 位置、9.15m、再開合図、周囲の動き。秒数規則は全再開共通ではない |
| 2-06（content/2） | L1・826字 | JFA・IFAB第13条、山形・Jリーグ公式 | 場所と直接／間接FK。小西雄大#21は出場を条件としている |
| 2-06-b（content/2） | L2・403字 | JFA・IFAB第13条 | 相手9.15m、3人以上の壁から攻撃側1m、クイックFKとの違い |
| 2-06-c（content/2） | L2・346字 | JFA・IFAB第13条 | 間接FKの片腕合図、オフサイド後と別の選手のタッチ |
| 2-06-d（content/2） | L2・399字 | JFA・IFAB第13条・笛ガイド | 急いで蹴れる場合と笛待ちを告げられた場合、守備の準備・球外の走者 |

検査：10記事すべて見出し「ひとことで」「しくみ」「今日の試合で見るなら」、出典URL・checked_at・関連IDを含む。L1 500〜1000字／L2 250〜600字の範囲。各記事の`==`は4〜6組。画像は作者・ライセンスを確認できないため追加せず。場面と選手の行動は未来の仮定形で書き、実際の判定・先発・交代と取り違えない。

## 調査とエピソード候補の比較

日英合わせて5回以上、①2026/27 JFA/IFAB笛と再開、②2026/27医療退場・Jリーグ適用、③advantageとカードの2026年変更、④quick corner Liverpool Barcelona UEFA、⑤小西雄大 山形千葉 2023年FK、⑥Arsenal Barcelona van Persie second yellow whistle、⑦Henry Chelsea quick free kick 2004、のテーマで原典と記録を検索・照合した。

評価軸は **驚き／今夜見たい／理由が解ける／情景／原典の確かさ**。各5点、計25点満点。採用と見送りは、得点数字だけではなく「誰が／どの場面／何をしてどうなった」を確かめて決めた。

| 候補 | 各5点の評価／計 | 判定と理由 |
|---|---|---|
| 2019-05-07 リバプールのアレクサンダー＝アーノルドが素早くCKを蹴りオリギが得点 | 5/5/5/5/5＝25 | **2-04-a採用**。笛が不要な再開を一瞬の得点とつなげられ、UEFA公式で照合 |
| 2023-08-12 山形の小西雄大が雨の千葉戦でFKを直接狙い、相手に当たって決勝点 | 4/5/5/5/5＝24 | **2-06採用**。今夜の柏#21の再開観察に直結、山形・Jリーグ公式で確認 |
| 2011年アーセナルのファン・ペルシーがバルセロナ戦、笛後に蹴り2枚目の警告 | 4/2/3/4/4＝17 | **不採用**。観衆の騒音・異議・個別判定が絡み、初心者の一般規則例に誤用しやすい |
| 2004年アーセナルのアンリ対チェルシーの素早いFK | 3/3/3/4/3＝16 | **不採用**。古い論争と審判の管理状況の裏付けを十分に分離できない |

採用出典：UEFA https://www.uefa.com/uefachampionsleague/match/2027160--liverpool-vs-barcelona/events/ ／山形 https://www.montedioyamagata.jp/match/p/2023081213/ ／Jリーグ https://www.jleague.jp/match/j2/2023/081213/review/

見送り照合元：アーセナル公式 https://www.arsenal.com/news/fc-barcelona-3-1-arsenal-match-report-ahkOd3Y1rlT9 ／2004年事例は採用可能な公式原典まで再確認できず、記事には載せない。

## 一次出典と確認日

**閲覧・照合日：2026-10-21 JST**。公開日が確認できたJリーグ負傷者対応の記事は**2026-08-25**。2023・2019年の逸話はその当時の試合記録であり、2026/27 J1の当日結果ではない。

- JFA 2026/27競技規則：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB 主審：https://theifab.com/laws/latest/the-referee/
- IFAB フリーキック：https://www.theifab.com/laws/latest/free-kicks/
- IFAB 笛の使い方：https://www.theifab.com/laws/latest/guidelines/body-language-communication-and-whistle/
- IFAB 2026/27改正：https://theifab.com/law-changes/latest/
- Jリーグ負傷者場外待機告知（2026-08-25）：https://www.jleague.jp/news/article/34731/
- FC東京公式当日案内：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- Jリーグ公式当日試合：https://www.jleague.jp/match/j1/2026/102108/
- 柏#21公式プロフィール：https://www.reysol.co.jp/team/players/2026/21.php

## 未解決・試合前に確定できない事項

- 2026-10-21の**確定先発・控え**、小西雄大の実際の起用、交代時刻・理由、当日の主審による具体的判定・笛の回数。試合前記事は予想・観察例としてのみ扱う。
- 会場の音量で笛が聞こえるか、どの反則・負傷・フリーキックが現実に起こるか。本文は出来事の発生を保証しない。
- 処分の細かな例外はJFA/IFABの適用条文を優先する。一般化できない具体場面を予測で判定しない。
- 他担当の次工程、実試合後の追記、公開サイトへの組み込みはこの担当範囲外。PRのmainマージを成果保存の条件とする。
