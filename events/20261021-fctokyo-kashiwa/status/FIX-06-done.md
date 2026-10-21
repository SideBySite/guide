# FIX-06 完了記録：FC東京×柏の記事4件の文章修正

- 対象：`events/20261021-fctokyo-kashiwa/`
- 作業日：2026-10-21
- 状態：完了
- 本文修正PR：https://github.com/SideBySite/guide/pull/235 （マージ済み）
- 本文修正マージコミット：`2cdd00926a97e2c4aabed277d63aaac25a818eed`

## 完了した4件

1. `content/5/5-02.md`：ひとことで節を「戦略→監督→攻守」の流れに整理。パスをつなぐだけでは成功が保証されない理由を明確化。10/17名古屋戦の中川敦瑛の振り返りを、柏公式談話に沿って補足。
2. `content/5/5-07.md`：4/29はFC東京所属だった遠藤渓太が、6/30に柏へ完全移籍した事実を追記。FC東京・柏の公式発表URLを`sources`および本文出典に追加。
3. `content/4/4-08.md`：2022年日本対スペインの決勝点を、三笘薫の折り返しから田中碧が決めたと明記し、`content/1/1-03.md`と整合。
4. `content/5/5-05-b.md`：2003/11/29柏戦のFC東京の得点を、65分石川直宏、79分阿部吉朗、83分・85分アマラオの時系列で補完。

## 編集基準・変更範囲

- `docs/content-template.md`と`docs/prompt-pack/shared-style.md`を参照（shared-styleは本イベント配下）。
- 読み手はサッカー初心者の大人。文体・専門語の説明・見出し・既存の装飾を維持。
- 元の試合日、得点時刻、得点者、スコア、既存の出典URLを維持。追加出典は遠藤の移籍に関する両クラブの公式発表のみ。
- PR #235の差分は指定の本文4ファイルだけ。他の記事、制作途中の下書き・メモ・分析ノート・点検ログには変更なし。
- 本status記録はPR #235のマージ後に追加したものであり、本文修正PRには含めていない。

## 追記：FIX-06 — 既存選手カード10枚のfront matter契約統一（2026-10-21）

> **記録の区別**：このstatusには以前の「FC東京×柏の記事4件の文章修正」のFIX-06記録が存在したため、既存内容を維持して今回の同番号タスクを追記した。今回の記事本文修正は行っていない。

### 対象・事前チェック
- 作業先：`events/20261021-fctokyo-kashiwa/`。対象は柏3枚、FC東京7枚の計10枚と、このstatusのみ。別カード・本文・ファイル名・共通仕様は変更しない。
- 現行値は指定表に**10/10一致**。カード本文冒頭の`#背番号`と指定のtitle内番号も**10/10一致**（食い違い0件）。既に正しかったキーは変更しない。
- 変更対象から外した正しい値：`id`は室屋成・キム スンギュ・石原 広教・アレクサンダー ショルツの**4枚**、`sources`は山内・藤尾・原田・田中颯・鈴木楓・田中希和・室屋成の**7枚**。既存`checked_at`は**全10枚**保持。
- `scripts/build_football_site.py`はカードの相対ファイル名を収集し、同相対パスからサイト内の`read-...`識別子を生成する（front matter の`id`は参照に使用しない）。`docs/prompt-pack/runtime/manifest.json`のEX-P01〜EX-P17の`person_ids`も`slug`と`path`を参照し、front matterの`id`値を参照していない。ファイル名を変更しないため参照は維持。
- `sources`欠落の3枚は本文の「出典」節を確認し、そのURL全件を順序を維持して重複なしで転記した：キム スンギュ**11件**、石原 広教**11件**、アレクサンダー ショルツ**13件**。本文側の出典節は変更なし。

### 修正一覧（id・title・categoryの変更前→変更後）

| ファイル（イベント相対パス） | id | title | category | sources | 個別コミット |
| --- | --- | --- | --- | --- | --- |
| `teams/kashiwa/people/hinata-yamauchi.md` | `hinata-yamauchi` → `ksw-hinata-yamauchi` | 山内日向汰は、前線のどこを見ると面白い？ → **山内日向汰（柏レイソル・背番号87）** | `kashiwa` → `people` | 既存を保持 | [dea66303](https://github.com/SideBySite/guide/commit/dea6630328be8fd03f98d0591a17566e904418c3) |
| `teams/kashiwa/people/shota-fujio.md` | `shota-fujio` → `ksw-shota-fujio` | 藤尾翔太の一歩を追うと、ゴール前で何が見える？ → **藤尾翔太（柏レイソル・背番号15）** | `kashiwa` → `people` | 既存を保持 | [23f4736c](https://github.com/SideBySite/guide/commit/23f4736cc51af6762f942ae57c0a607c5e4457d3) |
| `teams/kashiwa/people/wataru-harada.md` | `wataru-harada` → `ksw-wataru-harada` | 原田亘を追うと、守る前の準備が見えてくる → **原田亘（柏レイソル・背番号42）** | `kashiwa` → `people` | 既存を保持 | [d3fee9ab](https://github.com/SideBySite/guide/commit/d3fee9ab3fa7033d1ab2998d0f6797fe62a18758) |
| `teams/fctokyo/people/hayate-tanaka.md` | `fctokyo-player-hayate-tanaka` → `fctokyo-hayate-tanaka` | 田中 颯｜FC東京 #1 → **田中 颯（FC東京・背番号1）** | `fctokyo-people` → `people` | 既存を保持 | [ac274e65](https://github.com/SideBySite/guide/commit/ac274e656565c4b4fccfa0d3528d0632ebaab88e) |
| `teams/fctokyo/people/kaede-suzuki.md` | `fctokyo-player-kaede-suzuki` → `fctokyo-kaede-suzuki` | 鈴木 楓｜FC東京 #44 → **鈴木 楓（FC東京・背番号44）** | `fctokyo-people` → `people` | 既存を保持 | [dfff936b](https://github.com/SideBySite/guide/commit/dfff936b22ff4f0b1a88cc7b4c55955cec9e74e5) |
| `teams/fctokyo/people/kio-tanaka.md` | `fctokyo-player-kio-tanaka` → `fctokyo-kio-tanaka` | 田中 希和｜FC東京 #38 → **田中 希和（FC東京・背番号38）** | `fctokyo-people` → `people` | 既存を保持 | [17367b28](https://github.com/SideBySite/guide/commit/17367b28a5285d6ed6259a9cc8de7ba9c99c918b) |
| `teams/fctokyo/people/sei-muroya.md` | `fctokyo-sei-muroya` → `fctokyo-sei-muroya` | 室屋成はどんな選手？ けがで欠場見込みでも知りたい守備と経歴 → **室屋 成（FC東京・背番号2）** | `5` → `people` | 既存を保持 | [eb52e3bd](https://github.com/SideBySite/guide/commit/eb52e3bd1446e08761a758f7b370ae7e9597dc7c) |
| `teams/fctokyo/people/seung-gyu-kim.md` | `fctokyo-seung-gyu-kim` → `fctokyo-seung-gyu-kim` | FC東京 #81 キム スンギュ詳細名鑑 → **キム スンギュ（FC東京・背番号81）** | `5` → `people` | 11 URL追加 | [145ad950](https://github.com/SideBySite/guide/commit/145ad9501fb7720793bcb68e5bc3a0fb125d7518) |
| `teams/fctokyo/people/hirokazu-ishihara.md` | `fctokyo-hirokazu-ishihara` → `fctokyo-hirokazu-ishihara` | FC東京 #22 石原 広教詳細名鑑 → **石原 広教（FC東京・背番号22）** | `5` → `people` | 11 URL追加 | [cedf1c92](https://github.com/SideBySite/guide/commit/cedf1c9287c6e447c8cc9c406af42dbf9844fdd7) |
| `teams/fctokyo/people/alexander-scholz.md` | `fctokyo-alexander-scholz` → `fctokyo-alexander-scholz` | FC東京 #24 アレクサンダー ショルツ詳細名鑑 → **アレクサンダー ショルツ（FC東京・背番号24）** | `5` → `people` | 13 URL追加 | [47224523](https://github.com/SideBySite/guide/commit/47224523a4465e1724fff708f87d1857e8b4197d) |

### 全50枚の機械検証・差分検証
- 母集団：`teams/kashiwa/people/*.md`の選手25枚と`teams/fctokyo/people/*.md`の選手25枚。両チームの`manager.md`各1枚は選手カードではないため除外。
- 検証手順：50枚すべてをGitHubから再取得し、冒頭の`---`区間を機械的に解析。`id/title/category/sources/checked_at`の必須5キーと値の存在、`sources`のHTTP(S) URLリスト1件以上、`id`のチーム別接頭辞、`category: people`、`title`の`選手名（柏レイソル・背番号N）`または`選手名（FC東京・背番号N）`形式を検査。
- 結果：**必須5キー 50/50、sources URLリスト 50/50、id接頭辞 50/50、category 50/50、title形式 50/50、統一契約の総合合格 50/50**（柏25/25、FC東京25/25）。修正前の完全契約準拠40/50から50/50に改善。
- 対象10枚の本文冒頭番号とtitle番号：**10/10一致**。食い違い・例外なし。
- 対象の10個の独立コミットを1個ずつ取得し、各コミットの変更ファイルが指定選手カード1枚だけであること、Git差分の変更行が`id/title/category`と新設`sources`のみに限られることを機械検査：**10/10合格**。本文の変更**0件**、ファイル名変更**0件**、その他既存キーの変更**0件**。`checked_at`は事実確認記録として全件保持。
- カード変更コミット数：**10**（各カード1コミット）。このstatusの追記のみを別コミットで記録する。サイト生成・manifest・EX-P等のファイルは変更していない。
