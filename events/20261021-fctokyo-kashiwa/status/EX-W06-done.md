# EX-W06 執筆9件：作業完了記録

- 対象：2026-10-21 19:00 JST 味の素スタジアム FC東京×柏レイソル、試合前公開記事。
- 確認基準日：**2026-10-21 JST（キックオフ前）**。規則ページの公表日とは区別。
- 必須先行：`discovery/00-I/proposed-tree.json`・`decisions.csv`・`coverage.md`、`status/00-I-done.md`をmainで実体確認。**00-I PR #191（2026-10-21 14:12 JSTにmainマージ）**をGitHubのPR状態で確認。manifestの00-I検証記録も確認した。
- 00-IのB-08/B-10/B-11/B-13/B-14/B-28/B-29/B-30/B-31の`answer_scope`・`why_distinct`・`fact_check`を確認。旧64問・LOCAL18問、02/03/FCT-PREPの再実行・共有ファイルの編集は行っていない。
- 資料：イベント内の`docs/prompt-pack/{baseline-question-tree.md,shared-style.md,manifest.json}`、`docs/question-tree.md`、`content/2/2-01.md`・`2-01-a.md`・`2-02-b.md`、`teams/{kashiwa,fctokyo}/roster.md`、`foundation-v2/basics/rules-start.md`。人物カードは追加していない。

## 1問ごとの編集結果

| ID | 00-I対応 | 確認した論点 | 結果 |
|---|---|---|---|
| 2-05 | B-08/B-12統合 | 味方接触時、相手陣、ボールと後方2人目、腕を除く、関与。後ろへのパスの誤解も説明 | 執筆・確認済み |
| 2-05-a | B-10 | GK視界・競り合いの妨害と単なる位置を分離。FIFAの実例を確認 | 執筆・確認済み |
| 2-05-b | B-11 | 跳ね返り／制御可能な意図的プレー／意図的セーブの3分岐 | 執筆・確認済み |
| 2-05-c | B-13 | スローイン・ゴールキック・CK直受けの例外、FKとの違い、次のタッチ | 執筆・確認済み |
| 2-05-d | B-14/H10統合 | 明白な得点機会に限る遅延フラッグ、VAR手順、主審が最終判定 | 執筆・確認済み |
| 2-07 | B-28 | 自陣エリア内の直接FK相当の反則、11m、接触だけでは未確定。JFAの実例 | 執筆・確認済み |
| 2-07-a | B-29 | 白線はエリア内、反則地点と転倒地点、つかみ続ける場合 | 執筆・確認済み |
| 2-07-b | B-30 | GKの片足の一部がライン上・同一面・後方、他選手の距離、再実施の影響要件 | 執筆・確認済み |
| 2-07-c | B-31 | GK反発後の再触球可、枠だけでは二度触り不可、PK戦と区別。UEFA実例 | 執筆・確認済み |

## 調査記録：日英5検索以上と逸話選定

検索（2026-10-21 JST）：(1)「JFA サッカー競技規則 2026 2027 オフサイド 第11条 PK 第14条」、(2)「IFAB 2026 offside deliberate play deliberate save rebound」、(3)「IFAB penalty kick goalkeeper line second touch rebound」、(4)「IFAB VAR delayed flag offside clear attacking situation」、(5)「FIFA Ecuador Netherlands 2022 Preciado goalkeeper obstruct offside」、(6)「JFA Japan Colombia 2018 Carlos Sanchez handball penalty」、(7)「UEFA 2005 Xabi Alonso penalty Dida saved rebound」、(8)「FIFA Ecuador Qatar disallowed offside VAR 2022」。検索原典の本文まで確認。

採点：笑える・驚ける／今日確かめたくなる／なぜが解ける／情景が浮かぶ／出典で確認できる（各5点、満点25）。

| 候補（公式根拠） | 5観点 | 合計 | 採否・理由 |
|---|---|---:|---|
| 2022 FIFAエクアドル対オランダ、プレシアドがGKの視界を妨げ得点取消 | 4/5/5/5/5 | 24 | **採用**：触っていない妨害の映像的場面、2-05-aに最適 |
| 2018 JFA日本対コロンビア、カルロス・サンチェスの手の反則でPKと退場 | 5/5/5/5/5 | 25 | **採用**：反則場所とPKの理由、2-07へ |
| 2005 UEFAリバプール対ミラン、アロンソがGKに止められたPKを自ら押し込む | 5/5/5/5/5 | 25 | **採用**：枠とGKの違いが理解できる、2-07-cへ |
| 2022 FIFAエクアドル対カタール、VARで早い得点を取消 | 4/2/2/4/5 | 17 | **見送り**：取消自体は確かだがB-08の「パスを出した瞬間」の直接説明に不足し、既存2-01と重複 |

## 出典URL（すべて2026-10-21 JST確認）

- JFA 2026/27競技規則、第11/12/14/17条：https://www.jfa.jp/laws/soccer/2026_27/
- IFAB Law 11（反発／意図的プレー／セーブ／スローイン等）：https://www.theifab.com/laws/latest/offside/
- IFAB Law 14（GKの足、二度触り、侵入）：https://www.theifab.com/laws/latest/the-penalty-kick/
- IFAB VAR protocol（遅延フラッグ条件）：https://www.theifab.com/laws/latest/video-assistant-referee-var-protocol/
- IFAB law changes：https://www.theifab.com/law-changes/latest/
- Jリーグ改正適用告知：https://www.jleague.jp/news/article/34484/
- J1大会概要（引き分けと通常の試合内PK）：https://www.jleague.jp/outline/j1/
- 試合日時・対戦：https://www.fctokyo.co.jp/match/schedule/info/20261021/
- 柏所属・背番号：https://www.reysol.co.jp/team/players/
- FC東京登録：https://www.fctokyo.co.jp/team/players/?sort=number&y=2026_27
- FIFA 2022エクアドル対オランダ：https://www.fifa.com/es/articles/ecuador-paises-bajos-copa-mundial-qatar-2022
- JFA 2018日本対コロンビア：https://www.jfa.jp/eng/samuraiblue/worldcup_2018/news/00017859/
- UEFA 2005アロンソ：https://www.uefa.com/uefachampionsleague/news/0270-13e64fe91745-f5c0ea234512-1000--xabi-alonso-on-liverpool-s-2005-uefa-champions-league-final-/
- FIFA 2022エクアドル対カタール：https://www.fifa.com/en/articles/ecuador-beat-qatar-opening-match-fifa-world-cup-2022-enner-valencia

## 独立性・留保・確認

- 当日の先発、布陣、GK担当、実際のPK・旗・笛・VAR介入・最終判定は未確定。藤尾#15・永井#29らの今日の観察は**仮定または事前予想**で、確認済みの登録番号・過去試合と分離した。
- 細かな前後関係は現地肉眼では確定できないため、判定の正誤・DFの意図・接触の位置は断定しない。
- VAR使用や映像確認の実施を今夜の個別場面について予告・断定しない。遅延フラッグは条件付きの手順。
- 写真は採用しない。適切なWikimedia Commonsの個別ライセンスと被写体を確証できない画像で補わない。
- 本人・製作者の私生活・観戦回想・逸話は調査・執筆・誘導していない。
- 未解決：当日公式先発・控え発表、判定の映像確認、個別VAR稼働・場内合図。いずれも試合前記事には推測を書かない。

## 検証・保存

- 9件1問1ファイル。L1 500–1000字、L2 250–600字（見出しとMarkdown装飾を除いた本文文字数で検査）。「ひとことで」「しくみ」「今日の試合で見るなら」、3–6ハイライトを確認。
- 変更対象は上記記事9件＋このstatusの合計10件のみ。共有候補・割当・元記事・固定64問・LOCAL18問は変更しない。
- PR：**作成後に番号とURLを追記**。
