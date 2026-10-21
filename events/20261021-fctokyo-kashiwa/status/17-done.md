# 新工程17：初心者ルール／試合の流れと再開 — 完成報告

- **対象**：2026年10月21日（水）19:00 JST、味の素スタジアム、FC東京×柏レイソル、2026/27明治安田J1リーグ第11節。
- **確認基準**：2026-10-21 **12:55 JST**（キックオフ前の公開情報と2026/27競技規則）。
- **作業ブランチ**：`soccer/20261021-17`。旧01、02、03、04、ほかの担当成果を改変しない。
- **記事方針**：L1 3本、L2 6本。1問1Markdown、見出し・初出説明・マーカー・太字・今日の具体的な観察を収録。エピソードは成立する裏付けを確保できず、見出しを作らなかった。写真は被写体・ライセンスを個別確証できず採用していない。

## 完成ファイル（1記事1コミット）

| ID | 題名 | パス |
|---|---|---|
| 1-01 | サッカーってどんな競技？ | `content/1/1-01.md` |
| 1-01-a | 人数とポジション | `content/1/1-01-a.md` |
| 1-01-b | 勝敗と同点 | `content/1/1-01-b.md` |
| 1-02 | 試合はどう進む？ | `content/1/1-02.md` |
| 1-02-a | 前後半と追加時間 | `content/1/1-02-a.md` |
| 1-02-b | 攻める方向と交代 | `content/1/1-02-b.md` |
| 1-03 | 外に出たボールはどうなる？ | `content/1/1-03.md` |
| 1-03-a | スローイン | `content/1/1-03-a.md` |
| 1-03-b | ゴールキックとCK | `content/1/1-03-b.md` |

上記パスはすべて `events/20261021-fctokyo-kashiwa/` の下。記事の `checked_at` と `sources` に一次資料を個別に記録した。

## 先行資料と公式出典

- 既存01の要約（保持）：`basics/rules.md`、`facts/match.md`。試合日付・大会方式は以下の複数の公式発表と照合。
- FC東京の試合情報・開始19:00：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏レイソルの試合情報・第11節：https://www.reysol.co.jp/game/results/202627/1021i.php
- Jリーグの公式試合ページ・選手情報と事前見どころ：https://www.jleague.jp/match/j1/2026/102108/
- 味の素スタジアム公式日程：https://www.ajinomotostadium.com/schedule/2026/1021_16099.php
- J1の大会方式：**90分／同点引き分け／勝点3・1・0／延長戦・勝敗決定PK戦なし**：https://www.jleague.jp/outline/j1/
- JFA競技規則2026/27の入口：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB規則第3条（11人と交代）：https://www.theifab.com/laws/latest/the-players/
- 第7条（前後半・追加時間）：https://www.theifab.com/laws/latest/the-duration-of-the-match/
- 第8条（キックオフ・攻撃方向の反転）：https://www.theifab.com/laws/latest/the-start-and-restart-of-play/
- 第9条（ボール全体が線を越える条件）：https://www.theifab.com/laws/latest/the-ball-in-and-out-of-play/
- 第10条（得点）：https://www.theifab.com/laws/latest/determining-the-outcome-of-a-match/
- 第15条（スローイン）：https://www.theifab.com/laws/latest/the-throw-in/
- 第16条（ゴールキック）：https://www.theifab.com/laws/latest/the-goal-kick/
- 第17条（コーナーキック）：https://www.theifab.com/laws/latest/the-corner-kick/
- 遅延に対する5秒カウントの条件：https://theifab.com/laws/latest/throw-in-and-goal-kick-countdown-protocol/
- 2026/27の改正確認：https://theifab.com/law-changes/latest/
- FC東京の選手登録：https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27
- 柏の選手登録：https://www.reysol.co.jp/team/players/

## 判断・未確認

- **確認済み**：日付、19:00、会場、大会第11節と90分同点時の引き分け、前後半の長さ、休憩上限、追加時間の最低表示、攻撃方向の反転、ボール全体と線、標準の3再開、2026/27の故意遅延時5秒手続き。2026年上半期の別大会のPK方式を持ち込んでいない。
- **選手の出演は条件付きの観察提案**：長倉幹樹、瀬川祐輔、古賀太陽、久保藤次郎、安斎颯馬の名はクラブ・Jリーグの事前資料に依拠する。10/21の**公式先発／控え確定一覧は基準時に公開情報が見つかりませんでした**。今夜の実出場やプレー場面は断定していない。
- **不明**：正確な終了時刻、実際の前後半の追加時間、実際の交代選手と回数、担当審判の具体的な判断。現時点で公開情報が見つかりませんでした／事前確定できない項目。席種・応援側は創作しなかった。
- **図**：`1-01-a`に人数・位置、`1-02-a`に時間線、`1-03`にラインと3種類の再開、`1-03-b`にゴールライン際の2再開の図仕様をHTMLコメントで収録。写真はなし。
- **後工程へ**：証拠のある笑える／意外なルール逸話を独立に再調査する余地がある。未検証の話を本記事には記載していない。オフサイド・反則やVARは工程18、交代枠の詳説は`2-03-b`の担当に委ねる。初版01の本文は温存した。
