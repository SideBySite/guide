# 工程24 完了総括：ルールと大会のエピソード（6記事）

- **完成状態**：工程24は先行して **24-R（5記事）／24-C（1記事）** に分担され、両方のPRが **mainへマージ済み**。今回はそれらを再執筆せず、指定名の統合statusを補った。
- **原稿を完成させたPR**：[24-R #189](https://github.com/SideBySite/guide/pull/189)（2026-10-21 14:02 JSTマージ）／[24-C #184](https://github.com/SideBySite/guide/pull/184)（同13:54 JSTマージ）。
- **この統合記録**：`soccer/20261021-24`を最新mainから作成し、このファイルだけを1コミットで追加。担当記事・旧資料・foundation-v2・02/03・別担当の成果は改変しない。
- **調査の基準**：24-C＝2026-10-21 **13:49〜13:52 JST**、24-R＝同 **13:50 JST以降**。統合照合＝同 **17:05 JST**。いずれも19:00開始前の情報のみを使用。
- **対象試合**：2026-10-21（水）19:00 JST、味の素スタジアム、2026/27明治安田J1第11節 FC東京×柏レイソル。[FC東京公式](https://www.fctokyo.co.jp/match/schedule/info/20261021/)・[Jリーグ公式](https://www.jleague.jp/match/j1/2026/102108/)で統合時に再照合。
- **先行条件**：17・18・19の `status/*-done.md` と実記事をmainで確認。foundation-v2の完成も確認。初版01・先行02/03を巻き戻していない。

## 完成記事と採用件数

すべて `events/20261021-fctokyo-kashiwa/` 以下。**6本すべてに `episode: v2` と話の出典URL**を収録。元の「ひとことで」「しくみ」「今日の試合で見るなら」、既存の図・関連IDを保持している。

| 記事 | 採用件数 | 原稿の実体 | 完了PR |
|---|---:|---|---|
| 1-01 サッカーってどんな競技？ | 1 | `content/1/1-01.md` | #189 |
| 1-02 試合はどう進む？ | 1 | `content/1/1-02.md` | #189 |
| 1-03 外に出たボールはどうなる？ | 2 | `content/1/1-03.md` | #189 |
| 2-01 オフサイドって何？ | 1 | `content/2/2-01.md` | #189 |
| 2-02 反則はどう決まる？ | 2 | `content/2/2-02.md` | #189 |
| 3-01 今日、何を決めるために戦う？ | 2 | `content/3/3-01.md` | #184 |

**計：候補18件／採用9件／見送り9件。**記事5本は24-Rで各記事ごとにコミットし、3-01は24-Cで独立コミット。後から同じ記事の内容を再生成・再保存していない。

## 候補の一行要約、5観点採点、出典、見送り理由

点数は **驚き・笑える／今日見たくなる／なぜが解ける／情景の具体性／出典で確認できる** の順。各5点、計25点。24-R・24-Cの採点と判断を転記・統合したものであり、今回採点し直したものではない。詳細は[24-Rのstatus](24-R-done.md)と[24-Cのstatus](24-C-done.md)に保存されている。

### 1-01：11人と得点するGK
- **採用 5/5/4/5/5＝24**：2013年、ストークのGKベゴヴィッチが開始13.64秒に自陣から得点。[プレミアリーグ公式](https://www.premierleague.com/en/news/4504669/who-has-scored-the-fastest-goal-of-the-202526-premier-league-season)。GKも得点できる意外さ。
- **見送り 4/4/3/5/5＝21**：2021年、GKアリソンがCKに飛び込みヘッドで決勝点。[プレミアリーグ公式](https://www.premierleague.com/en/news/2145933/alisson-joins-goalscoring-goalkeepers-with-liverpool-winner)。GK得点という型が重複。
- **見送り 5/3/2/5/5＝20**：2002年マダガスカル、抗議による149点のオウンゴール。[ギネス](https://www.guinnessworldrecords.com/world-records/101619-most-own-goals-in-a-domestic-league-football-match)。通常の試合像から離れすぎる。

### 1-02：追加時間に起きた逆転
- **採用 5/5/4/5/5＝24**：1999年、マンチェスターUの途中出場2人が欧州決勝の追加時間に連続得点し逆転。[UEFA公式](https://www.uefa.com/uefachampionsleague/news/0161-0e6a261d85bb-05dbbb7741b5-1000--united-super-subs-floor-bayern-at-the-death/)。終了の笛と交代の見方が変わる。
- **見送り 5/5/3/5/5＝23**：2012年アグエロの最終節追加時間決勝点。[プレミアリーグ公式](https://www.premierleague.com/en/news/59706)。1999年の追加時間逆転と説明が重複。
- **見送り 4/4/4/4/5＝21**：2014年、富山第一が高校選手権決勝で追いつき延長戦で逆転。[JFA](https://www.jfa.jp/match/news/00024091/)。今夜のJ1にはない延長制度の説明が増える。

### 1-03：ラインとスローイン
- **採用 5/5/5/4/5＝24**：2022年日本対スペイン、三笘がぎりぎりのボールを折り返し田中の得点が認められる。[AP配信](https://www.espn.co.uk/football/report/_/gameId/633828)。線とボールの関係が分かる。
- **採用 5/5/3/5/5＝23**：2018年イラン代表モハマディが前転スローインを試み、放さず普通に投げ直す。[BBC](https://www.bbc.co.uk/sport/football/44555796)。再開前にも見どころがある。
- **見送り 5/4/4/4/3＝20**：2002年エンケルマンGKがスローインのボールを止め損ね失点。[Independent](https://www.independent.co.uk/sport/football/premier-league/enckelman-adamant-blunder-was-not-a-goal-177319.html)。本人と判定側で接触の事実に争い。

### 2-01：GKの前にいる相手を数える
- **採用 5/5/5/4/5＝24**：2010年W杯南アフリカ対メキシコ、GKクネが前へ出た位置関係からベラの得点がオフサイドで取り消し。[MLSの解説](https://www.mlssoccer.com/news/mexicos-goal-wasnt)。2人目の相手がGKとは限らない。
- **見送り 5/4/4/4/5＝22**：2010年テベスのオフサイド得点が見逃される。[Guardian](https://www.theguardian.com/football/2010/jun/28/carlos-tevez-offside-mexico-opener)。正しい位置関係より誤審の話になる。
- **見送り 4/4/4/4/4＝20**：2018年エザトラヒの得点が取り消し。[BBC](https://www.bbc.co.uk/sport/football/44555796)。「後ろから2人目」を示す具体性が採用話より弱い。

### 2-02：反則とカードの珍事
- **採用 5/5/5/4/5＝24**：2010年W杯、スアレスがガーナのシュートを手で防ぎ退場、ギャンのPKは失敗。[Guardian](https://www.theguardian.com/football/2010/jul/02/uruguay-ghana-world-cup-report)。ハンド・退場・PKの関係が分かる。
- **採用 5/5/4/5/5＝24**：2006年W杯、ポール主審がシムニッチに黄カードを3回提示、3回目の後に退場。[Guardian](https://www.theguardian.com/football/2006/jun/23/worldcup2006.match2)。処理の不備とカードの実物に目が向く。
- **見送り 5/4/3/5/5＝22**：2016年ドゥルスンが主審の赤カードを奪って逆に見せる。[NBC Sports](https://www.nbcsports.com/soccer/news/turkish-club-reduced-to-7-men-midfielder-shows-referee-red-card-after-being-sent-off)。抗議の珍事が主題となり反則の説明から外れる。

### 3-01：リーグ優勝と他会場
- **採用 5/5/5/5/5＝25**：2012年最終節、アグエロがQPR戦の追加時間に決め、シティが同勝点のユナイテッドを得失点差で上回って優勝。[プレミアリーグ公式](https://www.premierleague.com/en/news/4638196/could-the-premier-league-title-be-won-on-goal-difference)。勝点と得失点差の重み。
- **採用 5/5/5/5/5＝25**：2016年、レスター選手がヴァーディ宅で別会場の2-2を見て、自分たちはプレーせず優勝決定。[レスター公式](https://www.lcfc.com/media-article/champions-leicester-city-secure-premier-league-title)、[Sky Sports](https://www.skysports.com/football/news/10267516/watch-leicesters-players-celebrate-premier-league-title-win)。他会場結果の意味。
- **見送り 5/4/5/5/5＝24**：2001年シャルケは優勝と早合点するが、別会場でバイエルンが終盤に追いつく。[ブンデスリーガ公式](https://www.bundesliga.com/en/bundesliga/news/bayern-munich-schalke-most-dramatic-title-finish-2001-24146)、[DFB](https://www.dfb.de/news/detail/saison-20002001-meister-der-herzen-254147)。2012年の最終盤逆転と重なり説明が過密。

## 探索、出典の扱い、削除理由

- **検索**：24-Rは5記事それぞれ日英計5回以上、24-Cは3-01について8つの検索語を記録。[24-Cの検索クエリ](24-C-done.md)を参照。統合時はすでに完成した調査を無駄に再実行していない。
- **確認の区分**：試合日程・当季規則はクラブ/Jリーグ/IFABの公式資料、過去の逸話はリーグ・クラブの公式資料または当時の取材記事に依拠。過去のPK戦の勝敗決定を今夜のJ1リーグ戦に混ぜない。
- **削除した逸話**：**なし**。6記事とも元の逸話見出しがなく、今回選定した9件を追加した。見送り9件は本文に採らず、理由を上表に明記。既存の仕組み説明・図・今日の観察提案を削除していない。
- **写真**：採用なし。出典と画像利用条件を個別照合していない写真は使用していない。

## 不明事項と後工程

- 今夜の確定先発・交代・個々の意図・実際の追加時間は、既存記事の確認基準時には**公開情報が見つかりませんでした**。今後の発表や試合中の出来事を既成事実として追加していない。
- 記録時の独立したすべての検索レスポンスや映像原本までは、この統合statusに複製していない。採否と出典URL、5検索以上を行った旨は両担当のstatus・PRに残る。
- 後工程ではスマホ表示で字数・黄色マーカー・リンク・写真なしのレイアウトを確認すること。3-01の2012年アグエロ話は、1-02で**見送った理由が局所的な重複**であり、3-01では勝点と得失点差を説明する異なる観点で採用された。
- **衝突回避**：24-R／24-Cの完成記事とstatusは変更しない。02/03および他担当の原稿・ブランチ・PRは変更もマージもしない。
