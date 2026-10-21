# 新工程28 完了記録：戦略の基礎・FC東京 推敲と装飾③

## 担当と完了範囲

- 対象：2026年10月21日（水）19:00 JST／2026/27明治安田J1リーグ第11節／FC東京×柏レイソル／味の素スタジアム。
- 作業ブランチ：`soccer/20261021-28`（作成時の最新mainから分岐）。
- 先行確認：`status/15-done.md`、`status/20-done.md`、`status/25-T-done.md` がmainに保存済み。02・03は再実行せず、本人・製作者の逸話も扱っていない。
- 修正記事13件（イベント配下、各記事ごとに初回保存・独立コミット、必要な後続推敲も個別コミット）：
  - `content/4/4-01.md`、`4-01-a.md`、`4-01-b.md`
  - `content/4/4-02.md`、`4-02-a.md`、`4-02-b.md`
  - `content/4/4-03.md`、`4-03-a.md`、`4-03-b.md`
  - `content/5/5-01.md`、`5-01-a.md`、`5-01-b.md`、`5-01-c.md`
- 編集したのは上記13記事と本statusのみ。候補表・割当表・共通仕様・監督カード・別担当の原稿には触れていない。

## 推敲・装飾チェック

- 読者はサッカー初観戦の大人を想定し、長い文を区切り、同じ語尾の繰り返し、曖昧な主語・述語、専門語の初出説明を修正。観察対象はボールを持たない選手、パスの前の位置、奪われた直後、交代による配置、コーナーキック前の準備を維持。
- `4-01`から`4-03-b`までの9記事に`styled: true`を追記。`5-01`から`5-01-c`は既存の`styled: true`を保持。
- 黄色マーカーは記事ごとに3〜6組。太字は本文の初出用語、重要な数字、選手名を優先し、表以外の通常段落でおおむね1〜2か所に整理。関連疑問ID、補足引用、三つの基本見出し、裏付けのある2記事の逸話を保持。
- 図1（攻守二軸の表）と10/17先発に基づく配置表を保持。図2・図3の文字図は`4-02`・`4-03`に当初から存在せず、本工程での追加もしていない。図1と配置表はいずれも今日の確定布陣ではない。
- 写真：**追加なし**。Wikimedia Commonsの対象・作者・許諾を今回確証できる画像がなく、別人・別試合の代用写真を載せなかった。
- front matterのID、level、parent/children、sources、checked_at、episode、needs_check、related、既存の数値・日時・人名、未確認の留保は維持。文体・読みやすさの調整であり、新たな結果や推測を加えていない。

## 確認時刻・根拠

- 先行記事の出典基準：戦略基礎9記事 `2026-10-21T12:56:00+09:00`、FC東京4記事 `2026-10-21T13:00:00+09:00`（既存front matterの `checked_at` を保持）。
- 本工程での公式日程・ステータス確認：**2026年10月21日 15:26 JST前後**（試合前）。本文の既存一次出典および先行statusを根拠とし、前述の基準時刻を改竄していない。
- [FC東京試合情報](https://www.fctokyo.co.jp/match/schedule/info/20261021/)／[Jリーグ公式試合](https://www.jleague.jp/match/j1/2026/102108/)／[FC東京10/20当日券告知](https://www.fctokyo.co.jp/news/details/342829/)：2026/10/21 19:00、会場、対戦、2026/27 J1第11節を照合。
- [FIFA Training Centre：戦術の基本原則](https://www.fifatrainingcentre.com/en/game/game-analysis/landing-page-core-principles.php)／[守備組織](https://www.fifatrainingcentre.com/en/game/game-analysis/out-of-possession/team-organisation--out-of-possession-.php)／[カウンター](https://www.fifatrainingcentre.com/en/game/game-analysis/transition-to-attacking/the-counter-attack.php)：戦術の一般的な原理。
- [IFAB競技規則](https://www.theifab.com/laws/latest/offside/)：オフサイドと背後の区別。その他の再開規則は各記事 `sources` を参照。
- [FC東京10/20柏戦前評](https://www.fctokyo.co.jp/fan/fanzone/detail/342859/)／[10/17東京V戦評](https://www.fctokyo.co.jp/fan/fanzone/detail/342709/)／[10/14水戸戦評](https://www.fctokyo.co.jp/fan/fanzone/detail/342581/)／[10/10浦和戦評](https://www.fctokyo.co.jp/fan/fanzone/detail/342374/)／[10/7湘南戦評](https://www.fctokyo.co.jp/fan/fanzone/detail/342178/)：人物と直近の試合描写。別大会（10/14ルヴァン杯）をリーグ戦と混同しない。
- 逸話の裏付け：[2019年リバプール×バルセロナ UEFA試合記録](https://www.uefa.com/uefachampionsleague/match/2027160%E2%80%93liverpool-vs-barcelona/events/)／[ヘンダーソン本人談](https://www.uefa.com/uefachampionsleague/news/0251-0e99b5c0f828-65a8602dd792-1000--jordan-henderson-on-liverpool-s-madrid-mission/)／[FIFA 1970年決勝](https://inside.fifa.com/en/tournaments/mens/worldcup/1970mexico/news/brazil-s-history-making-hurricane-2865951)／[FC東京2004年カップ決勝](https://www.fctokyo.co.jp/match/schedule/result/20041103/)。

## 不明事項・後工程へ

1. **当日の確定先発・控え・交代・実際の配置**：今回の推敲では検証済みの確定情報を得ていない。**公開情報が見つかりませんでした**（先行記事の照合時点）。記事中の人物名は出場時の観察例であって先発確約ではない。公式発表と照合する後工程31・33・35に引き継ぐ。
2. **起用理由・守備判断・攻撃時の固定フォーメーション**：本人の内心や個別の指示は未確認。クラブの試合評と、文章中で示した観察仮説を分ける。独自の全試合映像確認はしていない。
3. 10/17東京V戦の**前半18分の相手退場**を残した。10/14水戸戦は別大会の敗戦であり、直近の4–0を11人同士の標準例とみなさない。
4. **今日の先発更新時**には、遠藤渓太、マルセロ ヒアン、満田誠、FC東京の中盤・サイドの起用例を、発表された11人・交代と照合する。表・文字図をそのまま今日の布陣として掲載しない。
5. 記事ごとの出典URLは全件front matterで保持。逸話は過去の試合の事実として置き、2026年の作戦が必ず再現されるとは説明していない。
