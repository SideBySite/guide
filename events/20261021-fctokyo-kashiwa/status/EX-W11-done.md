# EX-W11 完了記録：攻守・CK・ベンチ・終盤 10問

- 対象：2026年10月21日（水）19:00 JST、味の素スタジアム FC東京×柏レイソル。すべて**試合前原稿**。
- 実施日・資料確認日：**2026-10-21 JST、試合開始前**。front matterの `checked_at` は `2026-10-21T16:30:00+09:00`。引用先の過去の試合開催日、情報更新日とは区別する。
- 作業ブランチ：`ex/ex-w11-observation-10-20261021`
- PR：**#230** https://github.com/SideBySite/guide/pull/230
- 必須先行の確認：`discovery/00-I/proposed-tree.json`、`decisions.csv`、`coverage.md`、`proposed-tree.md` の実ファイル、`status/00-I-done.md`、[00-I追補PR #191](https://github.com/SideBySite/guide/pull/191)のmainマージを確認。単なる存在と依存の充足を混同していない。
- 調査の照合先：`docs/prompt-pack/baseline-question-tree.md`、`shared-style.md`、`manifest.json`、`docs/question-tree.md`（旧野球版は文体参考のみ）、現行`content/4/4-03*.md`、`content/5/5-03*.md`、`teams/`、`docs/prompt-pack/player-assignments-3.json`、`foundation-v2/README.md`、`discovery/00-I/`の10候補について `answer_scope`／`why_distinct`／`fact_check`。
- 02／03／FCT-PREPは再実行していない。固定64問とLOCAL18問、共有候補・割当表、他担当原稿は無変更。製作者・ユーザーの体験、私生活、回想、旧makerへの導線は無し。

## 記事別の検証結果

本文文字数はMarkdown先頭メタ情報・URL・末尾の出典注・関連ID行を除いた**読む本文（見出し・装飾記号を含む）**の概数。下記10記事は、いずれも独立した1問1ファイルで「ひとことで」「しくみ」「今日の試合で見るなら」を持ち、各3〜6マーカーと出典を備える。各ファイルに「確認済み」「予想」を明示した。

| 記事 | 00-I | 本文字数 | 主な確認済みの根拠と試合での観察 | 結果 |
|---|---|---:|---|---|
| `content/4/4-03-c.md` | C-32 | 396 | [柏10/17](https://www.reysol.co.jp/game/results/202627/1017.php)、[柏の過去の配置](https://www.football-lab.jp/kasw/formation)。久保#24の攻守の高さを条件付き比較 | 合格 |
| `content/4/4-03-d.md` | C-33 | 456 | [東京](https://www.football-lab.jp/fctk/formation)、[柏](https://www.football-lab.jp/kasw/formation)。後ろ3人と4人の外側の補助役を左右で比較 | 合格 |
| `content/4/4-03-e.md` | C-34（B-19統合） | 444 | [東京10/17](https://www.jleague.jp/match/j1/2026/101708/)、[IFAB](https://www.theifab.com/laws/latest/the-corner-kick/)。CK直前のショルツらの走りと柏の追走 | 合格 |
| `content/4/4-03-f.md` | C-35 | 438 | [IFAB](https://www.theifab.com/laws/latest/the-corner-kick/)、[柏配置](https://www.football-lab.jp/kasw/formation)。短いCKの角の2人、東京の対応 | 合格 |
| `content/5/5-03-d.md` | C-36（C-37・H25統合） | 416 | [東京](https://www.football-lab.jp/fctk/formation)、[柏](https://www.football-lab.jp/kasw/formation)。開始5分の前2人対後ろ3人と左右 | 合格 |
| `content/5/5-03-e.md` | C-38 | 425 | [柏10/17](https://www.reysol.co.jp/game/results/202627/1017.php)、[東京配置](https://www.football-lab.jp/fctk/formation)。遠藤が左なら東京の右の2人の距離 | 合格 |
| `content/5/5-03-f.md` | H30 | 415 | [FC東京案内](https://www.fctokyo.co.jp/match/schedule/info/20261021/)、[J公式の監督欄](https://www.jleague.jp/match/j1/2026/101009/lineup/)。身振りと位置変化は観察、指示内容は断定しない | 合格 |
| `content/5/5-04.md` | C-40 | 891 | [J1大会概要](https://www.jleague.jp/outline/j1/)、[当日](https://www.jleague.jp/match/j1/2026/102108/)。1点追うなら前半10分と80分の後方人数を比べる | 合格 |
| `content/5/5-04-a.md` | C-41 | 445 | [2026/27順位表](https://www.jleague.jp/j1/standings/2026-27/)、[J1大会概要](https://www.jleague.jp/outline/j1/)。同点時の縦パスと戻しを比較 | 合格 |
| `content/5/5-04-b.md` | C-42 | 554 | [IFAB](https://www.theifab.com/laws/latest/the-corner-kick/)、[UEFA公式のGK得点記録](https://www.uefa.com/uefachampionsleague/news/0285-1904eabff46a-098cf6778592-1000--highlights-round-up-barcelona-city-paris-win/)。1点差の終盤のCKでGKの位置を確認 | 合格 |

## 調査と逸話候補の選定

日本語と英語を横断して**5テーマ以上**調査。検索軸は、①「サッカー 攻撃 守備 3バック 4バック」、②「ショートコーナー 2対1 守備」、③「FC東京 2026 10月17日 ショルツ コーナーキック」、④「ゴールキーパー ロスタイム CK 得点 実例」、⑤ "goalkeeper last minute corner header Provedel Lazio Atlético UEFA"、⑥ "Alisson Liverpool West Brom goalkeeper corner header 2021"、⑦ "Peter Schmeichel Manchester United 1999 final corner"、⑧ "soccer coach touchline gestures tactical adjustments"。確認先は競技規則・リーグ・クラブ・UEFA公式を優先した。

採点は**驚き／今日確かめたくなる／なぜが解ける／情景が浮かぶ／原典で確認できる**の各5点、合計25点。

| 候補 | 5項目得点 | 合計 | 判断 |
|---|---|---:|---|
| **イヴァン・プロヴェデル**：2023/9/19ラツィオ対アトレティコ、GKがCK後のクロスに頭で合わせ1–1。原典：[UEFA公式](https://www.uefa.com/uefachampionsleague/news/0285-1904eabff46a-098cf6778592-1000--highlights-round-up-barcelona-city-paris-win/) | 5／5／5／5／5 | **25** | **採用**：`5-04-b`。GKが自陣ゴールを空ける選択と直接結びつく。 |
| **アリソン**：2021年リバプール対ウェスト・ブロム、終了間際にGKがヘディング得点。参考：[Guardian写真特集](https://www.theguardian.com/football/2021/may/25/premier-league-2020-21-the-best-photos-from-a-tumultuous-season) | 5／4／5／5／3 | 22 | **見送り**：主題がプロヴェデルと同じで1記事2話は長くなる。提示原典の試合経過説明が短いため追加の一次照合が必要。 |
| **ピーター・シュマイケル**：1999年マンチェスター・U対バイエルン、終盤のCKにGKが参加。原典：[UEFA公式](https://www.uefa.com/uefachampionsleague/news/025d-0f655b4a72b1-ba62ee25d15c-1000--classics-juventus-2-3-manchester-united/) | 4／3／4／4／2 | 17 | **見送り**：リンク先は別試合の回顧で、提示時点では当該決勝のプレー順序を直接裏付けられない。誤解を避けて不採用。 |

そのほかの9記事は、条件を満たす独立の逸話を追加しなかった。直近試合の得点・選手起用は仕組みの具体例か今日の観察根拠であり、「おもしろエピソード」として水増ししない。

## 未解決・公開後の再確認

- **当日未確定**：先発11人、各選手のポジション、柏3バックと東京4バックの採用、CKの有無、交代、監督の身振り、終盤のスコア、GK参加。いずれも現在の原稿で事実にしていない。
- Football LABの配置は過去試合からの独自分析。両クラブ公式発表の当日布陣とは区別する。
- 観客席からの監督の声・意図・指示と選手の行動の因果は、映像や本人発言で裏付けられなければ断定しない。
- 4-03-eで扱う10/17のCKは今夜の得点予告ではない。5-04-bのUEFA逸話は2023年の別大会であり、今夜の出場・結果とは無関係。
- 00-Iの元候補・固定64問・LOCAL18問・既存親記事の子リスト・manifest・roster・assignmentsは変更せず、関連IDの案内のみ付した。サイト導線への組み込みは別担当工程。

## PRとマージ

- 原稿コミット：`347ce1b9cecc9730f5bdac5922e5f416f5f84116`、`17c1ae453e64a00e7674a36da9c7b970a25a4ac8`
- PR：[#230](https://github.com/SideBySite/guide/pull/230)。本statusも同じPRに追加する。
- **変更可能ファイルは10原稿と本statusのみ**。PR差分でその他のファイルがないことを確認し、自分のPRだけmainへマージする。
