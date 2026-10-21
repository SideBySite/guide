# 25-T 完了記録：戦略4問のおもしろエピソード

## 実施範囲・前提

- 対象試合：**2026年10月21日（水）19:00 JST／FC東京×柏レイソル／味の素スタジアム／2026/27明治安田J1第11節**。
- **調査・照合基準：2026-10-21 13:56 JST**（キックオフ前）。情報の発表年・対象試合年を区別し、2026-10-21の試合の事後情報を採用しない。
- 必須先行 **15・16・20**：`status/15-done.md`、`16-done.md`、`20-done.md`および対象4記事がmain上に保存済みと確認した。02・03は再実行していない。
- ブランチ：`soccer/20261021-25-T`。変更対象はこのstatusと以下の4記事だけ。共有候補表・割当表・テンプレート、旧野球ガイド、個人的なユーザー／製作者逸話は対象外。
- 原稿の既存段落・見出し・「今日の試合で見るなら」は保持し、**「おもしろエピソード」だけを挿入**。各記事に `episode: v2`、根拠の `sources` を追記。各記事1回の初稿保存・コミット後、参照と表現の確認のため必要な記事のみ個別推敲コミットを追加した。写真なし。

## 完成ファイル・個別コミット

| 対象 | 採用した場面 | 初稿コミット | 確認後の処理 |
|---|---|---|---|
| `content/4/4-01.md` | 2019年リバプールの機転を利かせたCK | `927683f3d942f71cb9eacce06366e6e35ee9cd84` | UEFA本人談URLに精密化 `100c16a` |
| `content/4/4-02.md` | 1970年ブラジルの左への囮と右からの得点 | `5c16dbae49bc793bdf99db39303e5b6bccaf0502` | FIFA証言の主語を明示 `a7d3d82` |
| `content/5/5-01.md` | 2004年FC東京、10人で120分守って杯を獲得 | `f342300d4d9507ca9aae00966da685454c7dd528` | 初稿のまま |
| `content/5/5-02.md` | 2025年柏、準決勝で途中出場者が逆転に寄与 | `4453359d5321f9522b49ce5d69161fb7335ff165` | 既存マーカー総数に合わせて整理 `3c632ad` |

## 探し方・採点規則

各テーマについて日本語・英語を合わせ**5回以上**検索し、3候補以上を比較した。括弧内の点数は順に **①笑える・驚ける／②今日見たくなる／③なぜが解ける／④場面が浮かぶ／⑤出典で確認できる**。各5点、合計25点。同点は①→②→③→④→⑤の順で比較。**点数は事実そのものではなく編集判断**である。採用候補は対象のクラブ・FIFA・UEFA・Jリーグ等の出典で実名・場面・行動・結果を確かめた。

### 4-01「サッカーの作戦は何を取り合う？」

検索例（計5件以上）：`Japan Belgium 2018 World Cup counterattack corner FIFA`／`Liverpool Barcelona corner taken quickly Origi Alexander Arnold UEFA`／`2005 Istanbul Liverpool tactical switch Hamann Gerrard UEFA`／`サッカー 作戦 珍しい 逸話 人数 位置 守備 カウンター`／`weird football tactical moment goalkeeper counterattack`。

| 候補 | ①/②/③/④/⑤＝計 | 採否・理由 |
|---|---|---|
| **2019年リバプール×バルセロナ**：アレクサンダー＝アーノルドの素早いCK→オリギ得点。背後の備えをしていたヘンダーソンも見逃しかけた | **5/5/5/5/5＝25** | **採用**。時間・場所の関係を、選手本人の証言で確認できる |
| 2018年W杯ベルギー×日本：日本のCK後、GKクルトワから速攻、シャドリ決勝点 | 5/5/4/5/5＝24 | 見送り。CK後の速攻として強いが、「速さと空間」の採用話と観察導線が重なる |
| 2005年欧州CL決勝リバプール×ACミラン：後半からハマンを起用、0-3から追いついてPK勝ち | 4/5/5/5/5＝24 | 見送り。先発・配置変更の説明が増え、初観戦者の1分読みに重い。合計同点で①の差もある |

資料：
- [UEFA 2019準決勝公式実況](https://www.uefa.com/uefachampionsleague/match/2027160%E2%80%93liverpool-vs-barcelona/events/) — 79分のCKと得点の経緯。
- [UEFA ヘンダーソン本人インタビュー](https://www.uefa.com/uefachampionsleague/news/0251-0e99b5c0f828-65a8602dd792-1000--jordan-henderson-on-liverpool-s-madrid-mission/) — 振り向いて初めて気付いたとの証言。
- [FIFA ベルギー×日本回顧](https://inside.fifa.com/news/worldcupathome-belgium-japan-russia2018-3071468) — 選外。
- [UEFA 2005決勝の証言集](https://www.uefa.com/news/025d-0f782b45c942-3e20b8c30dfa-1000--miracle-of-istanbul-an-oral-history/) — 選外。

### 4-02「どこを使って攻める？」

検索例：`Japan Spain 2022 Mitoma Tanaka ball line width FIFA`／`1970 Brazil Italy Carlos Alberto Jairzinho Pele width FIFA`／`Barcelona Real Madrid 2009 Messi false nine Guardiola surprise`／`2014 Netherlands Spain Van Persie diving header Blind cross FIFA`／`サッカー 幅 サイド 逸話 歴史 三笘 クロス スペイン`。

| 候補 | ①/②/③/④/⑤＝計 | 採否・理由 |
|---|---|---|
| **1970年W杯ブラジル×イタリア**：監督ザガロがジャイルジーニョを左へ動かしてファケッティを引きつけ、空いた右をカルロス・アウベルトが走って得点 | **5/5/5/5/5＝25** | **採用**。囮の役割を本人がFIFAへ説明し、球のない動きが具体的 |
| 2014年W杯オランダ×スペイン：ブリントの長いクロスからファン・ペルシーの飛び込みヘディング | 5/4/4/5/5＝23 | 見送り。驚けるが「相手を動かして空ける」理由は採用話の方が明確 |
| 2009年バルセロナ×レアル：メッシを中央へ動かす起用と6-2の試合 | 4/5/5/4/5＝23 | 見送り。専門語「偽9番」の説明が必要で読者負担が大きい。同点では①を優先 |

資料：
- [FIFA カルロス・アウベルトの証言を引用した競技史](https://inside.fifa.com/en/tournaments/mens/worldcup/1970mexico/news/brazil-s-history-making-hurricane-2865951) — ザガロの指示、左に動いて右を空ける機序と得点者を確認。
- [FIFA 1970決勝回顧](https://www.fifa.com/pt/tournaments/mens/worldcup/articles/brasil-italia-final-copa-mundo-1970) — 対戦・時期を照合。
- [FIFA 2014年のファン・ペルシー回顧](https://www.fifa.com/en/articles/robin-van-persie-netherlands-spain-2014) — 選外。
- [UEFA 2009年バルセロナ×レアル](https://www.uefa.com/news-media/news/01d9-0f85ba57f4ee-b7ad2a390e68-1000--brilliant-barca-stun-madrid-at-the-bernabeu/) — 選外。

### 5-01「FC東京はどんな戦略を取りがち？」

検索例：`FC Tokyo 2004 Nabisco Cup final ten men Urawa Jaan defence`／`2004 ナビスコカップ FC東京 ジャーン 退場 10人 土肥 PK`／`FC Tokyo 2019 rugby world cup eight straight away games`／`FC東京 2012 天皇杯 決勝 京都 原博実 逆転`／`FC東京 2025 松橋力蔵 戦術 交代 逸話`。

| 候補 | ①/②/③/④/⑤＝計 | 採否・理由 |
|---|---|---|
| **2004年ルヴァン杯の前身大会決勝FC東京×浦和**：原監督の試合前の冗談、29分退場、藤山投入、戸田も守り、120分無失点→PK戦勝利 | **5/5/4/5/5＝24** | **採用**。クラブ一次回顧が残す具体的な意外性と作戦変更。2026年の松橋監督の話とは区別 |
| 2019年ラグビーW杯会場事情によるFC東京の長期アウェー連戦 | 3/4/4/4/5＝20 | 見送り。日程事情が中心で、特定の選手の場面・行動・結果を伴う一話として弱い |
| 2012年天皇杯決勝の京都戦で失点後、FC東京が逆転 | 3/4/3/5/5＝20 | 見送り。得点経過の列挙寄りで「何をして、なぜ面白いか」が弱い |

資料：
- [FC東京 2004年決勝の具体的回顧（2022公開）](https://www.fctokyo.co.jp/fan/fanzone/detail/290475/) — 原監督の発言、退場・藤山投入・戸田の守備、PK決着。
- [FC東京 2004年11月3日公式記録](https://www.fctokyo.co.jp/match/schedule/result/20041103/)・[Jリーグ杯2004年回顧](https://www.jleague.jp/leaguecup/2017/special/report/2004.html) — スコア・大会名。
- [FC東京公式歴史](https://www.fctokyo.co.jp/club/profile/) — 2019選外の背景。
- [FC東京2012年1月1日決勝](https://www.fctokyo.co.jp/match/schedule/result/20120101/) — 選外。

### 5-02「柏はどんな戦略を取りがち？」

検索例：`Kashiwa Reysol 2011 Nelsinho halftime tactical switch Shimizu`／`柏レイソル 2025 ルヴァン 準決勝 川崎 交代 細谷 仲間`／`Ricardo Rodriguez Kashiwa comeback substitution 2025 Kawasaki`／`柏レイソル 2025 東京V ルヴァン 交代 攻撃 監督`／`柏レイソル 2011 優勝 清水 試合中 位置変更`。

| 候補 | ①/②/③/④/⑤＝計 | 採否・理由 |
|---|---|---|
| **2025年10月12日柏×川崎の杯準決勝**：リカルド監督がハーフタイム3人交代、仲間と細谷が得点し4-1。川崎は56分退場 | **5/5/5/5/5＝25** | **採用**。交代と結果が結びつき、監督の試合後談話もある。数的優位の条件を本文に明示 |
| 2011年11月20日柏×清水：後半に工藤・レアンドロ・ドミンゲスの得点で1-2の逆転 | 4/5/5/5/5＝24 | 見送り。2011年のネルシーニョ監督と現在の監督を混同しないため。詳細な位置修正説明も長い |
| 2025年6月8日柏×東京V杯戦、パスの長短の使い分けと交代 | 4/5/4/4/5＝22 | 見送り。戦術分析の比重が高く、交代選手の働きは採用候補の方が明瞭 |

資料：
- [柏公式 2025年10月12日試合記録・監督コメント](https://www.reysol.co.jp/game/results/2025/1012.php) — 4・26・73・77・90+2分の得点、46分3人と67分の交代、56分退場。
- [Jリーグ 2025年杯準決勝結果](https://www.jleague.co/en/news/2025-jleague-ybc-levain-cup-semi-final-second-leg-recap-kashiwa-and-hiroshima-book-places-in-final/) — 2戦合計と決勝進出。
- [柏公式2011年11月20日清水戦](https://www.reysol.co.jp/past-pages/game/results/2011/111120.php) — 選外。
- [Jリーグ2025年6月8日柏×東京V戦評](https://www.jleague.jp/match/leaguecup/2025/060804/review/) — 選外。

## 編集・不確実性・後工程

- **確認済み**：記事内の日付・チーム・選手・監督・行動・結末は掲載資料に基づく。**本人談**：ヘンダーソン、カルロス・アウベルト、クラブ取材内の監督発言。**編集上の解釈**：その場面が場所・人数・時間、幅、交代を見る入口になること。
- これらは**1970・2004・2019・2025年の過去の一場面**で、2026年10月21日当日の戦術再現や先発を予言する証拠ではない。
- 今夜の先発、控え、実際の布陣、個別の交代指示の確約：**公開情報が見つかりませんでした**（この時点で照合した範囲）。記事の既存「今日の試合で見るなら」は条件付きであり、編集していない。
- 正確な直接引用箇所・年・対戦を確認したが、全試合の独自映像検証は未実施。画像は使用しておらず、Wikimedia Commonsの本人写真と利用許諾をそろえて確認できないため画像追加なし。
- 後工程：過去の選手を今夜の先発・固定戦術として扱わない。5-02の2025年の逆転は**相手の退場も条件**として必ず残す。4-01の出典はUEFAのヘンダーソン本人談を優先し、閉鎖・移動した旧クラブURLを引用しない。記事ごとの `episode: v2` を確認する。
- ユーザー・製作者本人の個人的経験や逸話、旧野球ガイドの個人エピソードリンクは調査・転載・掲載していない。
