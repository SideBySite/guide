# EX-W16 執筆8件 完了記録

- 対象：2026年10月21日（水）19:00 JST、味の素スタジアム FC東京対柏レイソル、2026/27明治安田J1第11節。**出典の確認基準日：2026-10-21（JST、試合開始前）**。
- 成果：content/5/5-10.md、5-10-a.md、5-10-b.md、5-10-c.md、5-11.md、5-11-a.md、5-11-b.md、5-11-c.md の8件を新規執筆。1問1ファイル。
- 保存先：Google Drive 共有フォルダ Yamato/Wekoto 内「20261021-fctokyo-kashiwa」： https://drive.google.com/drive/folders/1fqZMXOg07w2lywdDizp5YBorgl-b8BTg
- **PR番号：#237**（GitHubへの反映はGPTが行う。今回はDrive納品）。

## 必須先行チェック結果

- events/20261021-fctokyo-kashiwa/discovery/00-I/ に proposed-tree.json／proposed-tree.md／decisions.csv／coverage.md が存在し、GitHubのデフォルトブランチ（main）上で実取得・内容確認済み＝**mainマージ済み**（2026-10-21 16:51 JST時点、両担当で確認）。
- status/00-I-done.md あり：277疑問＝L1 64／L2 213（固定64＋採用210＋補完3）。追補はPR #191と明記（ファイルがmainに存在するため反映済みと判断）。
- 02/03・FCT-PREPは再実行していない。別チャットの会話履歴を前提にしていない。
- 執筆前に E-10〜E-17 の answer_scope／why_distinct／fact_check を確認。baseline-question-tree.md に5-10・5-11の記載はなし（新規L1のため正常）。
- 固定64問・LOCAL18問・共有候補表・割当表・テンプレート・他担当原稿は未変更。events配下 content/5 には 5-01〜5-04 系列のみ存在し、5-10・5-11系列は今回新規。
- 参照：docs/question-tree.md、docs/prompt-pack/baseline-question-tree.md、docs/prompt-pack/shared-style.md、docs/prompt-pack/manifest.json、現行status一式、teams/fctokyo・kashiwa、現行原稿5-01・5-01-a（文体雛形）、foundation-v2完成分。
- 文体はshared-style準拠（==マーカー3〜6か所、太字、引用の資料区分、「今日の試合で見るなら」必須）。本人・製作者の逸話は扱っていない。

## 記事別検証結果（5-10系列：担当A）

### 5-10.md（L1「試合がない日も、選手と街の人は会うの？」、本文約873字）
- Drive： https://drive.google.com/file/d/14Mpb14_lPAGXQGXxW4Zt30qO43monCOv/view?usp=drivesdk
- 出典（確認日2026-10-21）： https://www.fctokyo.co.jp/club/hometown/ ／ https://www.reysol.co.jp/club/clubinfo/ ／ https://reysol.co.jp/qa.php
- 逸話候補（笑える／今日確かめ／なぜ解ける／情景／出典、各5点）：
  1. あおあかドリル（FC東京制作の運動ドリルが小学校の体育で採用、コーチが活用授業）3/4/4/4/5＝採用（今日欄「配布物を誰が運営か」と直結）
  2. 柏の練習見学＋練習後ファン対応 3/3/4/4/5＝しくみ節に採用（逸話としては展開が薄い）
  3. 選手による首長への表敬訪問 2/2/3/3/5＝見送り（情景が弱く今日の見え方に直結しない）
  4. 日立製作所サッカー部1940創部・1986小平→柏移転 2/3/4/3/5＝「歴史・由来」節に採用
- 未確認：ホームタウン活動の年間回数・ドリル配布校数（公式ページの数値が画像のため取得不可・本文未記載）、今夜の会場ブース・募金の実施有無（当日告知依存、本文で現地確認と明記）。

### 5-10-a.md（L2「地元の子どもが、プロの同じユニフォームを着ることはあるの？」、本文約591字）
- Drive： https://drive.google.com/file/d/1nnDEQrTf_Meh68XUk-1yFG2hWXOMSUI0/view?usp=drivesdk
- 出典（確認日2026-10-21）： https://reysol.co.jp/academy/about.php ／ https://reysol.co.jp/qa.php ／ https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27 ／ https://www.reysol.co.jp/team/players/202627/04.php
- 逸話候補：
  1. マブチモーターがアカデミー単独スポンサー（2011年、クラブ史上初。U-18背中／U-15・U-12胸）3/4/4/4/5＝採用（ユニフォームが主題の問いに直結）
  2. 柏はアカデミー・トップの練習場が同じ敷地で、高校生からトップと練習する選手がほとんど（公式QA）3/4/4/5/5＝見送り（5-10-b・5-10-cの人物話と重複、しくみ節で制度説明に充当）
  3. 古賀太陽がU-12から柏一筋 2/4/3/3/5＝しくみ節に採用（逸話本体は5-10-bへ）
- 未確認：FC東京側アカデミーのスポンサー有無（未調査のため本文未言及）。

### 5-10-b.md（L2「柏で小さいころから育った選手が、今のキャプテンなの？」、本文約607字 ※L2目安600字を微超過・理解に必要な範囲）
- Drive： https://drive.google.com/file/d/1kQmmD2v7afgjD15AfcbVK52HjP70WIf0/view?usp=drivesdk
- 出典（確認日2026-10-21）： https://www.reysol.co.jp/team/players/202627/04.php ／ https://www.reysol.co.jp/news/topteam/202627-8.html ／ https://www.footballista.jp/special/153722 ／ https://web.gekisaka.jp/news/jleague/detail/?454993-454993-fl=
- 逸話候補：
  1. 2023年初就任時「監督から直接言われたわけではなく、さっきスタッフからキャプテンマークを渡されました」会見が笑いに 5/3/3/5/5＝採用（フットボリスタ確認済み、大谷秀和15年キャプテンからの継承と一体）
  2. 「レイソル＝太陽王」と古賀「太陽」の名前の一致 3/3/2/3/5＝引用形式の補足として採用（「何をしてどうなった」未充足のため本文逸話にはせず）
  3. 副キャプテン戸嶋祥郎「1つ大きく変わったのは古賀太陽がキャプテンになったこと」3/2/2/3/5＝見送り（公式発表引用で代替）
- 未確認：今夜の古賀#4の出場と腕章装着者（公式先発発表・現地で確認、本文は予想と明記）。

### 5-10-c.md（L2「FC東京の子どもチームから来た選手を、今日見つけられる？」、本文約511字）
- Drive： https://drive.google.com/file/d/1MgxfHBR0nLzg7Hh3OVDqlJQFobVLYOxm/view?usp=drivesdk
- 出典（確認日2026-10-21）： https://www.fctokyo.co.jp/news/details/313787/ ／ https://www.fctokyo.co.jp/news/details/316313/ ／ https://www.fctokyo.co.jp/academy/u18/match/284200/ ／ https://www.jleague.jp/news/article/7398/ ／ https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27
- 逸話候補：
  1. 俵積田晃太が2021/6/5のU-18公式戦で柏レイソルU-18相手に2得点（3-1勝利）4/5/3/4/5＝採用（今夜の相手が柏＝今日の見え方が最も変わる。公式試合記録で確認）
  2. 久保建英が2016年に15歳5か月1日でJリーグ最年少デビュー 4/3/3/4/5＝しくみ節に採用（今夜出場しないため逸話の主役にはせず）
  3. 俵積田がU-18時代、毎日練習の1時間前にグランドへ行き左足クロスを自主練（本人FANZONEインタビュー）3/4/3/5/5＝見送り（字数と主題の関係）
  4. 永野修都がU-15深川→U-18→2025年昇格 2/4/2/3/5＝しくみ節に採用
- 未確認：今夜の俵積田#33・永野#20の出場と俵積田のポジション（直近は中盤左の例あり、当日発表待ち。本文は予想と明記）。

## 記事別検証結果（5-11系列：担当B）

### 5-11.md（L1「両チームの監督は、選手だった人なの？」、本文828字）
- Drive： https://drive.google.com/file/d/1iZDnUoVEa33GinhH9xuxxIAWqwCv_Yak/view
- 検証：松橋の選手歴＝FC東京公式で一致。リカルド指導歴（1998年24歳〜）＝柏公式で一致。新潟2022年J2優勝＝日刊スポーツ＋アルビ公式で一致。
- 逸話：松橋・新潟監督1年目J2優勝（20点、採用）／リカルド24歳コーチ開始（20点、しくみ節に統合）／天皇杯2021決勝（17点、見送り）／「スペイン人監督として日本初タイトル」（15点、一次出典不足で見送り）
- 出典（確認日2026-10-21）： fctokyo.co.jp/news/details/316882/ ／ fctokyo.co.jp/team/players/202627/298271/ ／ reysol.co.jp/team/staff/s01.php ／ nikkansports.com/soccer/news/202210160001275.html

### 5-11-a.md（L2「松橋監督は、子どもたちを教えていた時期が長いの？」、本文469字）
- Drive： https://drive.google.com/file/d/1pgR1G9JYRvExxnKXTgynJTlUNEFdWfd3/view
- 検証：マリノス育成年代2004〜2016（約13年）＝FC東京公式で一致。新潟J2優勝・2025年東京就任＝公式で一致。
- 逸話：遠藤渓太#5が育成年代の教え子（21点、採用・football-zone報道ベースと明記）／ユース監督時代の発言（20点、採用・ゲキサカ）／水沼・天野・喜田らの名前（14点、ファンメディアベースで限定列挙）
- 出典（確認日2026-10-21）： fctokyo.co.jp/news/details/316882/ ／ fctokyo.co.jp/team/players/202627/298271/ ／ fctokyo.co.jp/fan/fanzone/detail/342859/ ／ football-zone.net/archives/46109 ／ web.gekisaka.jp/news/clubyouth/detail/?194284-194284-fl ／ nikkansports.com/soccer/news/202210160001275.html

### 5-11-b.md（L2「柏のリカルド監督は、どんな国で仕事をしてきたの？」、本文490字）
- Drive： https://drive.google.com/file/d/1AEe0hamS1MolaAf1pgoXotLQ4gY_-mhe/view
- 検証：6か国（西・墨・サウジ・タイ・日・中）＝柏公式で完全一致。徳島2019PO敗退→2020J2優勝＝Jリーグ公式で一致。天皇杯2021・J1優秀監督賞2021＝JFA・Jリーグ公式で一致。
- 逸話：徳島2019PO惜敗→翌年J2優勝（22点、採用）／天皇杯2021＋J1優秀監督賞（18点、しくみ節）／レアル・マドリード メキシコアカデミー（18点、しくみ節）／ACL2022（15点、線引き未確認で見送り）
- 出典（確認日2026-10-21）： reysol.co.jp/team/staff/s01.php ／ reysol.co.jp/team/staff/ ／ jleague.jp/news/article/18835/ ／ jleague.jp/news/article/19260/ ／ jleague.jp/awards/2021/winners.html ／ jfa.jp/eng/match/emperorscup_2021/news/00028676/

### 5-11-c.md（L2「柏には、監督の前のチームから来た選手もいるの？」、本文454字）
- Drive： https://drive.google.com/file/d/16g7jBjDcfZKFM3qoNpnKH-HVsdOo3TGY/view
- 検証：小泉佳穂#8＝浦和2021-24在籍（リカルド期と重複）、2025年1月柏へ完全移籍＝両クラブ・Jリーグ公式で一致。大久保智明#14＝浦和2021〜在籍、2025年12月15日柏へ完全移籍＝公式発表で一致。現行背番号は柏公式で一致。
- 逸話：小泉はFC東京U-15むさし出身（21点、採用）／小泉2025年35試合7得点・ベストイレブン（18点、数字として採用）／大久保の特別指定選手（14点、見送り）／加入コメント（15点、見送り）
- 出典（確認日2026-10-21）： reysol.co.jp/news/topteam/post-951.html ／ reysol.co.jp/news/topteam/post-1013.html ／ reysol.co.jp/team/players/202627/08.php ／ reysol.co.jp/team/players/202627/14.php ／ reysol.co.jp/team/players/ ／ reysol.co.jp/team/staff/s01.php ／ fctokyo.co.jp/match/schedule/info/20261021/

## 未解決・未確認事項

- 今夜の先発・出場メンバー（古賀#4、俵積田#33、永野#20ほか）と腕章装着者：未発表。各記事は条件形・予想と明記。
- 今夜の会場での地域紹介ブース・配布物・募金活動の実施有無：当日告知依存（00-I fact_check）。5-10本文は現地確認を促す記述。
- FC東京ホームタウン活動の年間回数・あおあかドリル配布校数：公式ページの数値が画像で取得不可のため本文未記載。
- FC東京アカデミーのスポンサー有無：未調査のため本文未言及。
- リカルドの選手歴の有無：柏公式に記載なし。断定せずその旨明記。
- 大久保智明の2021-22出場実績数：未確認（在籍事実のみ記述）。
- 遠藤渓太の教え子話・松橋の教え子個別名：報道／ファンメディアベースで限定表記。

## 調査実績

- 担当A（5-10系列）：日英合わせて検索10回＋公式ページ9件を直接取得・照合。00-I指定の参考原典は全件確認済み。
- 担当B（5-11系列）：日英6検索＋公式直接取得。

## PR・反映

- PR番号：**#237**。GitHub専用ブランチへのcommit・PR・mainマージは行わず、Google Drive共有フォルダへ納品。GitHubへの反映はGPTが行う。
