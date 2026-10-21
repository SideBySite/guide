# FIX-02 — 選手カード37枚へのYAML front matter補完

- 対象リポジトリ：`SideBySite/guide`
- 作業ディレクトリ：`events/20261021-fctokyo-kashiwa/`
- 検証・記録日時（日本時間）：`2026-10-21T17:02:05.011+09:00`
- 編集対象：指定選手カード37枚とこのstatusファイルのみ。カード本文・既存13枚・共通仕様は変更していない。

## 事前チェック

- 指定37枚の先頭行を全件確認：**37/37枚で `---` がなく、front matter欠落**（柏19、FC東京18）。
- 既にfront matterがあったため除外した指定ファイル：**0枚**。
- 参照確認：`teams/kashiwa/people/koya-yuruki.md` と `teams/fctokyo/people/seung-gyu-kim.md` を開いて比較した。FC東京側の代表例には必須キーの一部不足があったため、追加37枚には依頼で指定された5キーを採用した。
- 対象37枚の本文「出典」節：**37/37枚で存在**。列挙URLを `sources` に移し、本文側の出典節は残した。

## 追加した37ファイルのid・title

| ファイル（作業ディレクトリ相対） | id | title |
| --- | --- | --- |
| `teams/kashiwa/people/daiki-sugioka.md` | `ksw-daiki-sugioka` | 杉岡大暉（柏レイソル・背番号26） |
| `teams/kashiwa/people/hayato-nakama.md` | `ksw-hayato-nakama` | 仲間隼斗（柏レイソル・背番号19） |
| `teams/kashiwa/people/hiromu-mitsumaru.md` | `ksw-hiromu-mitsumaru` | 三丸拡（柏レイソル・背番号2） |
| `teams/kashiwa/people/keita-endo.md` | `ksw-keita-endo` | 遠藤渓太（柏レイソル・背番号5） |
| `teams/kashiwa/people/kengo-nagai.md` | `ksw-kengo-nagai` | 永井堅梧（柏レイソル・背番号29） |
| `teams/kashiwa/people/kenshin-yuba.md` | `ksw-kenshin-yuba` | 弓場堅真（柏レイソル・背番号44） |
| `teams/kashiwa/people/masaki-watai.md` | `ksw-masaki-watai` | 渡井理己（柏レイソル・背番号11） |
| `teams/kashiwa/people/nobuteru-nakagawa.md` | `ksw-nobuteru-nakagawa` | 中川敦瑛（柏レイソル・背番号39） |
| `teams/kashiwa/people/ryosuke-kojima.md` | `ksw-ryosuke-kojima` | 小島亨介（柏レイソル・背番号25） |
| `teams/kashiwa/people/sachiro-toshima.md` | `ksw-sachiro-toshima` | 戸嶋祥郎（柏レイソル・背番号28） |
| `teams/kashiwa/people/shusuke-furuya.md` | `ksw-shusuke-furuya` | 古谷柊介（柏レイソル・背番号30） |
| `teams/kashiwa/people/taiyo-koga.md` | `ksw-taiyo-koga` | 古賀太陽（柏レイソル・背番号4） |
| `teams/kashiwa/people/tojiro-kubo.md` | `ksw-tojiro-kubo` | 久保藤次郎（柏レイソル・背番号24） |
| `teams/kashiwa/people/tomoya-inukai.md` | `ksw-tomoya-inukai` | 犬飼智也（柏レイソル・背番号13） |
| `teams/kashiwa/people/yoshio-koizumi.md` | `ksw-yoshio-koizumi` | 小泉佳穂（柏レイソル・背番号8） |
| `teams/kashiwa/people/yudai-konishi.md` | `ksw-yudai-konishi` | 小西雄大（柏レイソル・背番号21） |
| `teams/kashiwa/people/yuki-kakita.md` | `ksw-yuki-kakita` | 垣田裕暉（柏レイソル・背番号18） |
| `teams/kashiwa/people/yusei-yamanouchi.md` | `ksw-yusei-yamanouchi` | 山之内佑成（柏レイソル・背番号32） |
| `teams/kashiwa/people/yusuke-segawa.md` | `ksw-yusuke-segawa` | 瀬川祐輔（柏レイソル・背番号20） |
| `teams/fctokyo/people/dani-gomez.md` | `fctokyo-dani-gomez` | ダニ ゴメス（FC東京・背番号99） |
| `teams/fctokyo/people/fuki-yamada.md` | `fctokyo-fuki-yamada` | 山田 楓喜（FC東京・背番号71） |
| `teams/fctokyo/people/hayato-inamura.md` | `fctokyo-hayato-inamura` | 稲村 隼翔（FC東京・背番号4） |
| `teams/fctokyo/people/kashif-bangnagande.md` | `fctokyo-kashif-bangnagande` | バングーナガンデ 佳史扶（FC東京・背番号6） |
| `teams/fctokyo/people/kein-sato.md` | `fctokyo-kein-sato` | 佐藤 恵允（FC東京・背番号10） |
| `teams/fctokyo/people/kento-hashimoto.md` | `fctokyo-kento-hashimoto` | 橋本 拳人（FC東京・背番号18） |
| `teams/fctokyo/people/kota-tawaratsumida.md` | `fctokyo-kota-tawaratsumida` | 俵積田 晃太（FC東京・背番号33） |
| `teams/fctokyo/people/kyota-tokiwa.md` | `fctokyo-kyota-tokiwa` | 常盤 亨太（FC東京・背番号27） |
| `teams/fctokyo/people/marcelo-ryan.md` | `fctokyo-marcelo-ryan` | マルセロ ヒアン（FC東京・背番号9） |
| `teams/fctokyo/people/masato-morishige.md` | `fctokyo-masato-morishige` | 森重 真人（FC東京・背番号3） |
| `teams/fctokyo/people/motoki-nagakura.md` | `fctokyo-motoki-nagakura` | 長倉 幹樹（FC東京・背番号26） |
| `teams/fctokyo/people/rio-omori.md` | `fctokyo-rio-omori` | 大森 理生（FC東京・背番号15） |
| `teams/fctokyo/people/shion-homma.md` | `fctokyo-shion-homma` | 本間 至恩（FC東京・背番号19） |
| `teams/fctokyo/people/shuto-nagano.md` | `fctokyo-shuto-nagano` | 永野 修都（FC東京・背番号20） |
| `teams/fctokyo/people/soma-anzai.md` | `fctokyo-soma-anzai` | 安斎 颯馬（FC東京・背番号7） |
| `teams/fctokyo/people/takahiro-ko.md` | `fctokyo-takahiro-ko` | 高 宇洋（FC東京・背番号8） |
| `teams/fctokyo/people/teruhito-nakagawa.md` | `fctokyo-teruhito-nakagawa` | 仲川 輝人（FC東京・背番号39） |
| `teams/fctokyo/people/wataru-goto.md` | `fctokyo-wataru-goto` | 後藤 亘（FC東京・背番号58） |

## 検証結果

先頭の `---` ～ `---` ブロックを機械的に解析し、`id` / `title` / `category` / `sources` / `checked_at` の5キーを検査した。さらに今回の37枚では、`id` とファイル名、`title` と本文冒頭の選手名・背番号、`category: people`、`sources` のHTTP(S) URLリスト（1件以上）、`checked_at` のJST ISO8601形式を検証した。

| 検証対象・条件 | 成功 | 失敗 |
| --- | ---: | ---: |
| 指定37枚：必須5キーの存在・値・形式すべての契約準拠 | **37** | **0** |
| 全50枚（旧13＋新37）：必須5キーの存在 | **47** | **3** |
| 全50枚：必須キーの値・形式を含む完全契約準拠 | **40** | **10** |
| 指定37枚：front matterだけ挿入され、元の本文がそのまま続くこと | **37** | **0** |

### 既存13枚の範囲外不一致

既存13枚は先頭にfront matterがあるが、うち次の3枚には `sources` キーがないため、全50枚の必須キー検証は47成功・3失敗だった。

- `teams/fctokyo/people/alexander-scholz.md` — `sources` 欠落
- `teams/fctokyo/people/hirokazu-ishihara.md` — `sources` 欠落
- `teams/fctokyo/people/seung-gyu-kim.md` — `sources` 欠落

必須キー自体は存在するが契約の `id` / `title` / `category` が一致しない既存の7枚：

- 柏：`hinata-yamauchi.md`、`shota-fujio.md`、`wataru-harada.md`
- FC東京：`hayate-tanaka.md`、`kaede-suzuki.md`、`kio-tanaka.md`、`sei-muroya.md`

上記10枚はすべて今回の編集範囲外なので**未修正**。よって「全50枚の必須5キーを読み取れる」完了条件のみ、今回許された変更範囲内では達成できない。

## 差分・コミット確認

- 選手カードは**1枚ずつ独立して計37コミット**（`main`）。先頭コミット：`7503a2fd62781f80154e906a957c96bbd131047a`、最終カードコミット：`00b3ac354ae1c46733fd9c15ec0d4079e5b3aa27`。
- 全37枚で書き込み時に**元の本文との文字列完全一致**を検査。GitHubの比較でも37枚すべて追加行のみ・削除行0（合計追加862行）。
- 比較したコミット範囲には別作業による対象外ファイルへの変更も混在したが、FIX-02として操作したのは指定37枚とこのstatusファイルだけ。
- statusはカード37コミットとは別にコミットする。
