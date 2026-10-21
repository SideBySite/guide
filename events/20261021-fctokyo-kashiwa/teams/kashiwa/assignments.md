---
id: kashiwa-assignments
title: 柏の人物カードをA〜Eへどう分ける？
category: kashiwa
sources:
  - https://www.reysol.co.jp/team/players/
  - https://www.jleague.jp/club/kashiwa/player/
  - https://www.reysol.co.jp/game/results/202627/1017.php
  - https://www.reysol.co.jp/game/results/202627/1014.php
  - https://www.reysol.co.jp/game/results/202627/1009.php
  - https://www.reysol.co.jp/game/results/202627/1003.php
  - https://www.reysol.co.jp/game/results/202627/0920.php
checked_at: 2026-10-21T11:56:00+09:00
---

# 柏の人物カード：固定担当表（新工程04）

## ひとことで

==**A〜Eの5担当、各5人、合計25人**で固定する==。このファイルは人物カード本文ではなく、**次の執筆者が迷わず1人1ファイルで書くための仕様**だ。25人を割り当てたのでEも実施対象となる。

**A・B・C**には、[先発11人の予想](lineup.md)を全員入れた。**D・E**には、先発を争う人、交代の有力候補、控えGKなどを置く。「スター」「控え」という評価で人物の面白さを決めない。

## A〜Eと、最初から動かさない保存先

以下の保存先は**イベントルート `events/20261021-fctokyo-kashiwa/` からの相対パス**。人物ファイルは別担当が作るため、この工程では作らない。==割り当て後にslugを変えたり、A〜E間で選手を動かしたりしない==。

| 担当 | 背番号・選手 | 当日の読みどころ／予想上の役割 | 固定の保存先 |
|---|---|---|---|
| **A** | 29 永井堅梧 | 予想先発GK／10/17途中、10/14先発 | `teams/kashiwa/people/kengo-nagai.md` |
| **A** | 4 古賀太陽 | 予想先発／後方の中心 | `teams/kashiwa/people/taiyo-koga.md` |
| **A** | 26 杉岡大暉 | 予想先発／左後方 | `teams/kashiwa/people/daiki-sugioka.md` |
| **A** | 24 久保藤次郎 | 予想先発／右側 | `teams/kashiwa/people/tojiro-kubo.md` |
| **A** | 28 戸嶋祥郎 | 予想先発・原田との競争 | `teams/kashiwa/people/sachiro-toshima.md` |
| **B** | 21 小西雄大 | 予想先発／中央 | `teams/kashiwa/people/yudai-konishi.md` |
| **B** | 39 中川敦瑛 | 予想先発／中央 | `teams/kashiwa/people/nobuteru-nakagawa.md` |
| **B** | 8 小泉佳穂 | 予想先発／前方の接続 | `teams/kashiwa/people/yoshio-koizumi.md` |
| **B** | 5 遠藤渓太 | 予想先発／左側 | `teams/kashiwa/people/keita-endo.md` |
| **B** | 87 山内日向汰 | 予想先発／前線 | `teams/kashiwa/people/hinata-yamauchi.md` |
| **C** | 15 藤尾翔太 | 予想先発／前線先頭 | `teams/kashiwa/people/shota-fujio.md` |
| **C** | 42 原田亘 | 先発競争・後方交代 | `teams/kashiwa/people/wataru-harada.md` |
| **C** | 18 垣田裕暉 | 先発競争・10/14先発FW | `teams/kashiwa/people/yuki-kakita.md` |
| **C** | 20 瀬川祐輔 | 主要交代／J1途中から8得点 | `teams/kashiwa/people/yusuke-segawa.md` |
| **C** | 44 弓場堅真 | 先発競争・主要交代 | `teams/kashiwa/people/kenshin-yuba.md` |
| **D** | 9 細谷真大 | 主要交代・FW先発競争 | `teams/kashiwa/people/mao-hosoya.md` |
| **D** | 40 原川力 | 中盤入替・交代 | `teams/kashiwa/people/riki-harakawa.md` |
| **D** | 16 汰木康也 | 先発競争・外側 | `teams/kashiwa/people/koya-yuruki.md` |
| **D** | 2 三丸拡 | DFの控え | `teams/kashiwa/people/hiromu-mitsumaru.md` |
| **D** | 13 犬飼智也 | DFの控え・10/14途中 | `teams/kashiwa/people/tomoya-inukai.md` |
| **E** | 25 小島亨介 | 控えGK候補 | `teams/kashiwa/people/ryosuke-kojima.md` |
| **E** | 32 山之内佑成 | DF控え・10/14途中 | `teams/kashiwa/people/yusei-yamanouchi.md` |
| **E** | 19 仲間隼斗 | MF控え・10/3途中 | `teams/kashiwa/people/hayato-nakama.md` |
| **E** | 30 古谷柊介 | MF控え・10/17ベンチ | `teams/kashiwa/people/shusuke-furuya.md` |
| **E** | 11 渡井理己 | MF控え・9/20途中 | `teams/kashiwa/people/masaki-watai.md` |

## 人物カードを受け取る人への仕様

カードの先頭には**氏名／読み／背番号／クラブの公式登録位置と試合での役割／年齢／当日の予想出場**を分ける。**2026/27の所属・番号・生年月日**は [柏公式選手一覧](https://www.reysol.co.jp/team/players/) と [Jリーグ選手登録](https://www.jleague.jp/club/kashiwa/player/) で照合する。

**当日の出場見込み**は [出場候補25人](roster.md) と [予想先発](lineup.md) を参照する。自分のカードの根拠は [直近5公式戦](recent-matches.md) の一次試合記録から引き、名前・背番号の公式情報と混ぜて一文の「確認済み」にしない。

人物カードは1人につき**Markdown 1ファイル**。元01の最小 front matter は `id`、`title`、`category`、`sources`（URLリスト）、`checked_at`（JST ISO）である。移籍しても変えない小文字英字のslugをファイル名に使い、本文は最初に短い答えを置く。

口調は初心者へ説明する「〜だ／〜なのだ」調。「**ひとことで**」「**しくみ**」「**今日の試合で見るなら**」を基本とし、今日の場面はその選手が出場したときに何を見るかを書こう。==意図や気持ちは、外から見えた動きだけで言い切らない==。実話の条件を満たす出典がないなら「おもしろエピソード」を作らない。

> **画像方針**：写真は本人だと確かめられ、Wikimedia Commons の作者・利用条件まで確認できる場合のみ。別人や一般的なスタジアム写真で埋めず、必要なら画像なし。公式写真を無断転載しない。

## 機械的に照合する3つの集合

- **A**＝永井、古賀、杉岡、久保、戸嶋（5）。
- **B**＝小西、中川、小泉、遠藤、山内（5）。
- **C**＝藤尾、原田、垣田、瀬川、弓場（5）。
- **D**＝細谷、原川、汰木、三丸、犬飼（5）。
- **E**＝小島、山之内、仲間、古谷、渡井（5）。

**検算**：5×5＝**25**。同じslugの重複は**0件**、[roster.md](roster.md)の25人との漏れは**0件**。予想先発11人はAの5＋Bの5＋Cの藤尾1、合計11人で、全員ここにいる。

## 25人の外に置いた人の引き継ぎ

**馬場晴也#88**・**熊坂光希#27**はクラブの負傷発表を優先して、本編の候補には入れない。**若原智哉#77**は10/17の脳震盪交代後の復帰状況が不明。**長南開史#23**は10/14 ACL途中出場があり、25人以上へ候補が広がる場合の優先的な補足対象。その他ACLベンチの加茂・岩永などは [roster.mdの補足表](roster.md) へ。

今夜の公式名簿にこれらの選手が載ったら、それを**発表済みの事実として上書き優先**する。すでに固定したA〜Eの担当先を、事後的に別人物へ付け替えない。追加対象は補足表から別の担当調整とする。

## 今日の試合で見るなら

最初の発表で**AのGK永井**と**Eの控えGK小島**の登録を確認する。==控えGKも、前に誰が立つかで役割が変わる==のだ。後半に**Cの瀬川**か**Dの細谷**が入ったら、味方の前線の並びがどう変わるかを追ってみよう。

関連： [候補者・根拠・年齢](roster.md)／[予想先発と競争](lineup.md)／[直近の試合記録](recent-matches.md)。
