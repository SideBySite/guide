# FCT-PREP 完了記録｜FC東京の候補・直近起用・9担当の準備

**担当**：FCT-PREP／2026-10-21 FC東京×柏レイソル／味の素スタジアム／19:00 JST、2026/27明治安田J1第11節。  
**情報の基準**：**2026-10-21 13:50 JST**（対象試合前）。先発11人は公式未確認、**予想**と明示。キックオフ後の結果を利用していない。  
**ブランチ**：`soccer/20261021-FCT-PREP`（開始時main `0a630442f390f9eea4639d582949f8edc984345e`）。  
**段階別確認コミット**：[候補・直近起用・予想・固定割当](https://github.com/SideBySite/guide/commit/c2bf6ef5003a4dce2a921522bb649af7a81ed3f6)、[実名指示・割当データ・まとめ・描画スクリプト](https://github.com/SideBySite/guide/commit/65962ea9e0ad51d7faa5ac4fa94175e1fb6466e1)。本status・manifest・再生成HTMLは次のコミットで保存。別担当のPRはマージしない。

## 保存物・完了範囲

- `teams/fctokyo/recent-matches.md`：**10/7天皇杯湘南、10/10 J1浦和、10/14ルヴァン杯水戸、10/17 J1東京V**の先発・交代・約分数・見取り図を公式試合記録に結び付けた。2026年春の百年構想リーグ／2026/27 J1／各カップ戦を区別。
- `teams/fctokyo/roster.md`：候補**25人**。予想先発11人→主要交代・先発競争→控えGKを含むその他の順。各人に氏名・読み・番号・公式位置と実際の役割・生年月日・10/21年齢・近況・出場見込み・負傷／停止の確認限界・出典URL・時点・固定slug。
- `teams/fctokyo/lineup.md`：**予想先発11人**、4-4-2風の配置の目安、競争相手、根拠。公式先発・控え未確認を予想と分離。リーグ前節は相手に前半退場があったことに注意。
- `teams/fctokyo/assignments.md`：固定順25人、**FCT-01〜09の9担当**。01〜08は各3人、09は1人。重複0、割当漏れ0。監督は15の担当。
- `docs/prompt-pack/prompts/FCT-01.md`〜`FCT-09.md`：**実名・人数・固定パス**と試合前予想の区別を追加。既存の調査条件・全文名鑑の8主要見出し／全項目・各3人以下の執筆条件は保持。FCT各担当の別チャット並行開始を可能にした。
- `docs/prompt-pack/player-assignments-3.json`、`manifest.json`、`players-3.md`、`README.md`、`scripts/render_dashboard.py`、`index.html`：候補・プロンプト・担当カード表示・準備状況を同期。**KSW-01〜09の25人の配列と他担当の進行記録は変更せず**、FCT-PREPのみ保存確認済みへ移行した。

## 既存成果と今回の新規調査

- **引き継ぎ**：`facts/match.md`の試合情報、`status/15-done.md`のFC東京監督・戦略・最近の4試合の公式記録と観察の観点、`docs/prompt-pack/shared-style.md`の文体と詳細名鑑全項目。柏の人物25件はPR #149ほかで既存資料として保持。
- **02・03の扱い**：`docs/prompt-pack/running-02-03.md`とmanifestに**実行完了の報告**がある。共有mainでFC東京の`roster.md`／`assignments.md`を確認できず、関連PR #151、#181およびFCT/03の候補ブランチも探索したが、その**実ファイルを発見できなかった**。番号だけで担当を決めず、02・03をやり直さず、今回新しく資料を調べて固定した。既存の固定選手slugはFC東京では発見できなかった（既存本文は監督カードのみ）。
- **不在の補助資料**：root・イベント・docs・prompt-pack階層の`AGENTS.md`、イベント`docs/player-template.md`と`execution-plan.md`は対象mainに未存在。既存FCT指示とshared-styleの全項目を採用した。
- **新規調査**：2026/27 FC東京公式選手名簿、Jリーグ選手名簿の背番号・生年月日・登録位置、直近4公式戦の先発・交代、当日公式試合案内、負傷公表の一次出典を照合。独自の全試合映像分析はしていない。

## 主な公式出典（試合前）

- [10/21 FC東京開催案内](https://www.fctokyo.co.jp/match/schedule/info/20261021/)／[Jリーグ当日試合](https://www.jleague.jp/match/j1/2026/102108/)／[柏公式](https://www.reysol.co.jp/game/results/202627/1021i.php)。
- [FC東京2026/27名簿](https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27)／[Jリーグ FC東京選手一覧](https://www.jleague.jp/club/ftokyo/player/)（名簿には2026/10/16更新表示）。
- [10/7天皇杯湘南 4–0](https://www.fctokyo.co.jp/match/schedule/result/20261007/)／[10/10 J1浦和 3–0](https://www.fctokyo.co.jp/match/schedule/result/20261010/)／[10/14ルヴァン杯水戸 0–1](https://www.fctokyo.co.jp/match/schedule/result/20261014/)／[10/17 J1東京V 4–0](https://www.fctokyo.co.jp/match/schedule/result/20261017/)。
- [室屋成の10/11負傷公表](https://www.jleague.jp/news/article/35090/)／[本間至恩の9/21負傷公表](https://www.jleague.jp/news/article/34966/)／[長友佑都の9/21負傷公表](https://www.jleague.jp/news/article/34968/)／[橋本健人の9/15負傷公表](https://www.jleague.jp/news/article/34909/)。

## 予想の限界・次の確認

- **確認済み**：過去の公式試合の登録選手・先発交代の記録、名簿に掲載された氏名／番号／生年月日、公式の負傷リリース。
- **解釈・予想**：予想先発11人、4-4-2風の左右配置、ベンチ起用、ボールがないときに見る位置。公式発表のリスト順から配置を断定していない。
- **未確認**：10/21当日の正式先発と控え・発表時刻、全員の負傷／累積警告停止／登録状態の網羅的な最終確認、復帰発表と当日招集、交代理由や選手の心理。#2室屋・#19本間は負傷公表あり、候補末尾に置くが出場見込みは低い。欠場確定とは断定しない。
- **試合前後の区別**：10/17の4–0は相手が前半18分に退場した試合。10/14は別大会で0–1、リーグの連続無失点とは別。試合後記録を10/21事前予想へさかのぼって混ぜない。

## 機械・編集の照合

- **25候補=25割当**、全候補の人物パスの一意性25/25、重複0・漏れ0、**9担当すべて1〜3人**（最終1人）。
- 各FCTプロンプト本文・タイトル・JSON・一覧の実名とslugを突合、詳細名鑑の見出しと調査／保存条件を省略しない。既存KSW25人と旧05〜14の状態は不変更。
- `scripts/render_dashboard.py`のテンプレート／manifestから`index.html`を再描画し、FCT-PREPを保存済みにし、実名の9カードが開始可能となる出力を確認。ユーザー本人・製作者本人の逸話、旧野球のmaker導線は追加していない。
- 後続者は候補順・固定slugを変えず、**氏名が入ったFCT担当カード同士は並行して開始できる**。人物本文は本担当で作成しておらず、各FCT担当が一人ずつ原稿とstatusを保存する。

