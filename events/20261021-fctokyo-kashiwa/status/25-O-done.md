# 工程25-O 完了記録：戦略の対比・観察2問の逸話

- **対象試合**：2026年10月21日（水）19:00 JST、味の素スタジアム、FC東京×柏レイソル、2026/27明治安田J1第11節。
- **採用史料の確認基準時刻**：2026-10-21 **15:22:18 JST**（試合開始前）。歴史上の競技逸話は当日の結果・先発予想と切り離して確認。
- **必須先行**：main上の `status/21-done.md`、`status/22-done.md`、実原稿 `content/5/5-03.md`、`content/6/6-02.md` を確認済み。02・03を再実行していない。
- **ブランチ**：`soccer/20261021-25-O`（作成時のmain起点）。
- **編集範囲**：`content/5/5-03.md`、`content/6/6-02.md`、本statusの3ファイルのみ。既存の本文・表・「今日の試合で見るなら」・関係リンクは維持。

## 完成と独立コミット

1. `content/5/5-03.md`：**1982年アヤックスの2人で蹴ったPK**を「おもしろエピソード」に採用。相手GKがオルセンに引きつけられ、クライフに空いたゴールができた具体場面。出典URL・`episode: v2`・確認日時を追記。コミット：`ff23b0755c4b0a71f9b2e0f809085c39a7940cbb`。
2. `content/6/6-02.md`：**2019年リバプールのヘンダーソンは決勝進出を決めた得点を見逃しかけた**話を採用。仲間とCK後の反撃への備えを整えていた本人談と、オリギのゴールの記録を分離。出典URL・`episode: v2`・確認日時を追記。コミット：`063003cc321334d67a912e43dda6d2d02159dbcc`。
3. 本statusを別コミットで保存。もとからエピソード見出しがなかったため、**既存の逸話を削除したものはない**。候補の見送りは下記に記録。

## 検索と採点（各テーマ日英5検索以上）

**5-03のテーマ**：相手を引きつけて別の人が空く意外な戦術／試合途中の作戦変更。英語の「Cruyff Olsen penalty」「Tim Krul substitution」「football tactical masterstroke」「football famous strategic plan」「site:ajax.nl Cruijff Olsen」「site:fifa.com two man penalty」と、日本語の「戦術 奇策 サッカー クライフ PK」など**7検索以上**を実施。

**6-02のテーマ**：主役以外の準備・無球の役割が見える珍場面。英語の「Thomas Muller falls over free kick」「Liverpool Barcelona 2019 corner」「football quiet player off the ball」「Jordan Henderson corner protection」「Nemanja Matic Liam Rosenior」「Messi walking off ball」と、日本語の「サッカー ボールを持たない おとり フリーキック」「リバプール ヘンダーソン CK 守備」など**8検索以上**を実施。

評価の順番は **驚き・笑い／今日の観察に役立つ／なぜが解ける／情景の浮かびやすさ／出典確度**（各0〜5、最大25）。同点なら左から優先。事実未確認は得点にかかわらず採用不可。

| 対象 | 候補 | 5軸の点数 | 合計 | 判断と理由 |
| --- | --- | --- | ---: | --- |
| 5-03 | クライフ／オルセン、1982年アヤックス対ヘルモント・スポルト | 5/5/5/5/5 | **25** | **採用**。GKがオルセンに寄るとクライフが空く。誰・いつ・結果が当時のクラブとFIFAで照合可能。 |
| 5-03 | ピレス／アンリ、2005年アーセナル対マンチェスター・シティで2人PK失敗 | 5/4/4/5/5 | **23** | **見送り**。失敗例として面白いが、選手と空いた受け手を読む本記事の入口では成功例の方が直接的。 |
| 5-03 | ファン・ハール／クルル、2014年オランダ対コスタリカPK戦前のGK交代 | 5/4/3/5/5 | **22** | **見送り**。交代の妙が主で、中央・サイドの噛み合いより別記事の題材に向く。 |
| 6-02 | ヘンダーソン、2019年リバプール対バルセロナで反撃への備えの最中に得点 | 5/5/5/5/5 | **25** | **採用**。得点時にボールを見ていない守備準備の具体場面を本人が説明。 |
| 6-02 | ミュラー、2014年ドイツ対アルジェリアのFKで転んだふりをするが失敗 | 5/4/3/5/5 | **22** | **見送り**。無球のおとりとしては分かりやすいが、日常の支える役割より特別な奇策に偏る。 |
| 6-02 | マティッチ、2017年マンチェスター・ユナイテッド対ブライトンで守備を支えたが試合後にほぼ話題にされなかった | 2/5/5/4/5 | **21** | **見送り**。元対戦選手の実感は貴重だが、やや抽象的で、短い一場面の起承転結は採用案に劣る。 |

## 重要な根拠・確認区分

- **確認済み（5-03）**：1982年12月5日のAjax–Helmond Sport、クライフ→オルセン→クライフ、GKオットー・フェルスフェルトの動き。[アヤックス公式2025/12/5](https://www.ajax.nl/artikelen/on-this-day-samenspel-vanuit-penalty)、[FIFA当事者証言](https://inside.fifa.com/news/belgians-invent-the-two-man-penalty-1644041)、[アヤックス2026/3/20オルセン取材](https://english.ajax.nl/articles/olsen-cruijffs-little-hop-shows-he-was-nervous-for-that-penalty-too)。
- **見送り根拠（5-03）**：[UEFA 2005/10/24 ピレス／アンリの不成功](https://www.uefa.com/news-media/news/01ae-0e6d1b90dd9c-b602d09069f1-1000--pires-laughs-off-spot-of-bother/)、[FIFA 2024/7/5 クルル取材](https://www.fifa.com/en/tournaments/mens/worldcup/articles/tim-krul-interview-costa-rica-shootout)、[イングランドFA 2014/7/5](https://www.thefa.com/news/2014/jul/05/world-cup-quarter-final-argentina-belgium-higuain-holland-costa-rica)。
- **確認済み（6-02）**：2019年5月7日のLiverpool–Barcelona準決勝、アレクサンダー＝アーノルドのCKとオリギの得点。[UEFA試合評2019/5/7](https://www.uefa.com/uefachampionsleague/news/0251-0e99aae66a0d-4ef82ebc84f0-1000--liverpool-4-0-barcelona-champions-league-at-a-glance/)。**本人の回想**：ヘンダーソンがCK後の反撃への備えを話しており、振り向いてゴールを見た。[UEFA本人談2019/5/22](https://www.uefa.com/uefachampionsleague/news/0251-0e99b5c0f828-65a8602dd792-1000--jordan-henderson-on-liverpool-s-madrid-mission/)／[Sky Sports 2019/5/21](https://www.skysports.com/football/news/11725437/jordan-henderson-says-he-nearly-missed-divock-origis-winner-vs-barcelona)。
- **見送り根拠（6-02）**：[Reuters 2014/7/1 ミュラーが奇策と説明](https://www.reuters.com/article/sports/mueller-admits-botched-free-kick-was-trick-that-failed-idUSKBN0F65F1/)、[The Guardian 2017/11/30 ブライトンのリアム・ロシニア記](https://www.theguardian.com/football/blog/2017/nov/30/nemanja-matic-water-carrier-liam-rosenior)。
- **試合の公式照合**：[FC東京公式](https://www.fctokyo.co.jp/match/schedule/info/20261021/)／[柏公式](https://www.reysol.co.jp/game/results/202627/1021i.php)／[Jリーグ公式](https://www.jleague.jp/match/j1/2026/102108/)を2026-10-21 15:22 JSTに確認。10月21日19:00、味の素スタジアム、2026/27 J1第11節で一致。

## 不明事項と後工程

- **公開情報が見つかりませんでした**：本確認時点での今夜の確定先発・控え、個別の非公開指示・選手の内心。2つの過去の逸話を今夜の予定や確定戦術と混同しない。
- 1982年のプレーはFIFAの取材に本人談があるが、当時の意図を全員が共有していたかまでは断定しない。2019年の「反撃への備え」はヘンダーソン自身の回想であり、周囲が何を話したかの全記録ではない。
- 写真は不採用。出来事の当該場面でWikimedia Commons作者・再利用条件を確認できる写真がなかった。無関係な写真・図を足していない。
- 後工程：先発発表後は既存本文の当日観察候補を公式名簿と照合すること。今回の歴史的逸話はその日の勝敗や先発に左右されない。両記事の他段落・他担当原稿・共有表は修正していない。
- ユーザー本人・製作者本人の体験／私生活／思い出は調査も収録もしていない。関連導線も作成していない。
