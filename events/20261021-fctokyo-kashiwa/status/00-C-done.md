# 00-C 完了記録：戦略の種類と相性から問いを掘る

- **状態**：担当分の候補・レビュー完成（2026-10-21、試合開始前の情報）。
- **保存**：`discovery/00-C/candidates.json`（42件）、`discovery/00-C/review.md`。
- **件数**：42件（カテゴリ4：35／5：7、L1：11／L2：31、star：23）。
- **専用ブランチ**：`soccer/discovery-00-C`。
- **編集範囲**：この二つの候補資料と `status/00-C-done.md` のみ。基本64問・他担当のファイル・既存記事・共有テンプレートは変更していない。
- **コミットの分け方**：保持と速攻10件→前から／下がって守る10件→中央・端・背後10件→数字・CK・当夜の対比・点差12件。その後レビューと本statusを作成。
- **検査**：JSONを再取得し42件・ID重複なし・13フィールド完備・実在しない仮親IDなし・source URL形式を検証。正式記事ID未割当。
- **先行条件**：必須なし。02/03は再実行せず。04の候補表、01R、基礎記事、PLAN、docs類は読み取りのみ。

## 根拠（出所と限界）

- **試合の特定**：Jリーグ公式およびFC東京公式の2026/27明治安田J1・第11節、10月21日（水）19:00、味の素スタジアム。 https://www.jleague.jp/match/j1/2026/102108/ 、https://www.fctokyo.co.jp/match/schedule/info/20261021/
- **比較の手掛かり**：FC東京の松橋監督インタビュー（ボール保持と積極的な守備への言及）。 https://www.fctokyo.co.jp/fan/fanzone/detail/336734/
- **数字の並び**：Football LABの2026/27分類（東京4-4-2、柏3-4-2-1）は独自判断であり、当夜の確定配置ではない。 https://www.football-lab.jp/fctk/formation 、https://www.football-lab.jp/kasw/formation
- **直近の顔ぶれ**：柏10/17公式試合記録とJリーグ当日プレビュー。 https://www.reysol.co.jp/game/results/202627/1017.php 、https://www.jleague.jp/match/j1/2026/102108/
- **規則・終盤**：2026/27 J1は90分同点の場合引き分け、勝点は勝3・分1・負0。 https://www.jleague.jp/outline/j1/ 。オフサイドの参照元は https://www.theifab.com/laws/latest/offside/ 。
- **基準仕様**：`docs/prompt-pack/baseline-question-tree.md` と `shared-style.md`、旧 `docs/question-tree.md`、`docs/content-template.md`、`scripts/build_prompts.py` は参照のみ。

## 未確定として残した点

当夜の実際のスタメン、配列、誰が誰を追うか、CKでの仕込み、誰が交代するか、得点差・時間帯ごとの判断は試合前には確定できない。候補内の `fact_check` に個別の条件を記録した。選手の出場予測を確定情報に昇格させず、観察できない場合の条件も残した。

**対象外**：試合結果の後追い、戦術分析記事の執筆、選手名鑑、サイト化、共有ファイルの編集。
