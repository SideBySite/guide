# 00-I 統合編集 完了記録

- 対象：2026年10月21日（水）19:00 JST、味の素スタジアム FC東京対柏レイソル、2026/27明治安田J1第11節。**確認基準：同日試合開始前**。
- 必須先行：00-A〜Hのcandidates.jsonとreview.mdをすべて確認し、候補合計344件を照合。固定64問はdocs/prompt-pack/baseline-question-tree.mdのまま保持。
- 参照：初版01のPLAN・facts/match・facts/stakes・basics/rules・competitions・stadium、およびmainにある01R-A〜Eの土台・9問単位の稿／status。01R-Fの完成や02/03再実行は条件にしていない。
- 成果：discovery/00-I/proposed-tree.json、proposed-tree.md、decisions.csv、coverage.md。このstatus以外は編集しない。
- 採用：**277疑問＝L1 64／L2 213**（固定64＋00-A〜H 210＋00-I独自補完3）。元候補の採用210／統合125／保留9。人物カードと両監督名鑑は加算しない。
- 編集の選択：現行記事IDは不変、追加は候補IDのまま、親はL1に限定。近接する答え・同じ見る先はdecisions.csvで代表を指定し、差が残る場合のみ独立記事を提案。初読14問・★・通常を分離。

## 資料と確認日

- FC東京 10/21当日時間表・対戦：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏 当日案内：https://www.reysol.co.jp/game/results/202627/1021i.php
- J1大会概要・試合・順位：https://www.jleague.jp/outline/j1/ ／ https://www.jleague.jp/match/j1/2026/102108/ ／ https://www.jleague.jp/j1/standings/2026-27/
- JFAサッカー競技規則2026/27：https://www.jfa.jp/laws/soccer/2026_27/
- J1の26/27規則適用告知：https://www.jleague.jp/news/article/34484/
- 10/14会場マナー・10/20券種：https://www.fctokyo.co.jp/news/details/342462/ ／ https://www.fctokyo.co.jp/news/details/342829/
- 補完の根拠：https://www.fctokyo.co.jp/ticket/disabilities/ ／ https://www.ajinomotostadium.com/overview/barrier-free.php
- 試合前順位の公開データ更新日は**2026-10-18 18:16 JST**、FC東京の会場変更案内は**2026-10-14掲載**、当日券案内は**2026-10-20掲載**。これらとこちらの**2026-10-21試合前確認**を混同しない。

## 未確定と次の工程

- 現場での実際の入場口、車椅子席・磁気ループ席の当日利用、授乳室などの利用可能区画は現地案内で再確認する。
- 当日の先発・布陣・交代・判定・試合結果とVAR選択制の運用は公表・実施を待って記述する。元候補の選手名を出場確定と扱わない。
- 「同じ親にL2多数」の表示順の調整、正式ID割当、原稿担当への切分は00-Jの所管。既存64ID削除・改名は行っていない。
- PR URLはこのブランチの専用PR本文に記録する。自分のPRだけをmainへマージする。

## 追加編集の確認（PR #191）

- 既存のPR #183の編集・事実確認を引き継ぎ、独立した観察価値が残る追加11疑問を採用。合計277問へ更新。
- JSONは既存の配列形式、CSVは既存の列名・列順を維持し、00-Jの入力互換性を守る。元候補344件の採否と統合先を全件記録。
- 試合前の未確定事項・対象外の個人体験・他担当の作業範囲は不変。変更は自担当の5ファイルのみ。
- 本追補のPR：https://github.com/SideBySite/guide/pull/191
