# 原文參考與繁中譯本

[返回繁體中文首頁](../README.md)｜[简体中文](../README.zh-CN.md)｜[English](../README.en.md)

This directory contains an English text reference checked against Dan Koe's public prompt, and its unofficial Traditional Chinese translation. These are separate from the community revisions in the repository root. The source's claims and risky recommendations are preserved for comparison, not endorsed.

## 選擇版本

| 目的 | 文件 |
|---|---|
| 研究作者公開提示詞的文字與規則 | [英文原文參考](ORIGINAL.md) |
| 對照該英文來源的中文意思 | [非官方繁中譯本](TRANSLATION_TW.md) |
| 使用本專案另外修訂的流程與規則 | [英文](../PROMPT.md)、[繁中](../PROMPT_TW.md)、[簡中](../PROMPT_CN.md)社群修訂版 |

參考文字保留原作的隱藏計分、依層級討論高風險加速器、確定性判讀與長期計畫。這些內容不是本專案背書，也沒有因為存檔或翻譯而獲得科學驗證。社群修訂版的安全界線、證據規則、跳過／停止與摘要確認等調整，不會混入原文或譯文。

## 來源與核對範圍

| 欄位 | 記錄 |
|---|---|
| 作者 | Dan Koe |
| 文章 | [Prompt: HUMAN 3.0 Self-Discovery & Metatype Test](https://letters.thedankoe.com/p/prompt-human-30-self-discovery-and) |
| 公開文章資料 | [Substack 公開端點](https://letters.thedankoe.com/api/v1/posts/prompt-human-30-self-discovery-and)，文章 ID `172054418` |
| 來源所列發布時間 | `2025-08-27T15:08:02.493Z` |
| 來源所列更新時間 | `2025-08-27T15:11:04.145Z`；這是來源提供的中繼資料，不是完整修訂紀錄 |
| 本次核對時間 | `2026-10-23T03:58:16.084667+00:00`（UTC） |
| 倉庫既有英文材料 | [e52d88d7d45983b31366b2717fdfd47b5690571d 的 PROMPT.md](https://github.com/chiisen/HUMAN3_PROMPT/blob/e52d88d7d45983b31366b2717fdfd47b5690571d/PROMPT.md)，Git blob `05691f8a4827181e87ae895598811dc6c845d7d2` |
| 舊繁中草稿 | [相同提交的 PROMPT_TW.md](https://github.com/chiisen/HUMAN3_PROMPT/blob/e52d88d7d45983b31366b2717fdfd47b5690571d/PROMPT_TW.md)，Git blob `f2342dd191db923b4d63a55021167a366920de59`；本次以此為草稿重新對照英文校譯 |

英文參考以倉庫既有材料為基礎，補回作者公開頁面中六個指令章節的編號（1～6），並統一為 UTF-8／LF。核對範圍從 `You are a direct, insightful development assessor` 開始，到提示詞最後一段引文結束；不包含文章前面的宣傳介紹、訂閱按鈕、留言或推薦閱讀。

將作者公開內容的 HTML 轉為可見文字，再移除所有空白字元後，與本次英文參考逐字元相同。這個結果確認本次提示詞文字的對應關係，不代表 HTML、字型、換行或列表排版相同，也不能證明它就是發布當日未修改的版本。

公開頁面可能變動；來源日期與文章 ID 不能代替內容版本。需要引用本次材料時，請固定本倉庫的 Git 提交並搭配下列指紋，不只引用會變動的 `main`。

## 內容指紋

兩個參考檔都把檔案標示放在正文之前；正文位於 `<!-- reference-body:start -->` 與 `<!-- reference-body:end -->` 之間。下表的正文 SHA-256 只包含兩個標記之間的文字（不含起始標記後的第一個換行，包含正文末尾換行），不包含來源註記或標記本身。

| 對象 | SHA-256 |
|---|---|
| 本次取得的來源 `body_html`（UTF-8） | `051a0e1313ff9a29fef65fcf0cda542ac9e9976e665c2e303bffc5f1b0dcc298` |
| 英文正文（UTF-8／LF） | `f982a69c5d97b8075cfaeb1808ec885e61dcf9a56d04d65b7050b55348fbb0c4` |
| 英文可見文字移除空白後（UTF-8） | `dbc2d69264f67c5a377194ed2e55183f58fa696b8803a2fc7c25d85a9fee3159` |
| 繁中譯文正文（UTF-8／LF） | `f1253d11d691278be9cbccd890359a400ba7a22a8642d7a0fc5f902c4c216c56` |

空白正規化採 Python `re.sub(r'\s+', '', text)`；比對時沒有忽略標點、大小寫、數字或字詞差異。來源 HTML 的指紋用於記錄這次取得的內容，倉庫未另外保存整份文章 HTML；這是提示詞的文字參考，不是發布當日的完整網頁封存。

## 譯註與校對

繁中譯本是本專案的非官方翻譯，並非原作者審訂版，也沒有經過外部專業譯者審閱。本次逐節對照角色、模型、Glitches、生活方式、訪談六節、約束與輸出格式；不使用去 AI 味或自由改寫來改變原作主張。

- `assessor` 譯為「評估者」，不據此暗示持有專業資格。`Mind／Body／Spirit／Vocation` 沿用「心智／身體／靈性／職業」，`Metatype` 為「元類型」，`Skill` 為「技藝」。這些是對應用語，不是經驗驗證的分類。
- `AI Psychosis`、`Glitches`、`Death Sentence` 等詞保留原作的用語或強度供對照；它們的出現不構成臨床診斷、專業分類或個人風險許可。
- 校譯補回舊草稿漏掉的「理解並接受可能後果」、超出層級造成退步、根因與症狀區分、不粉飾缺口、不輸出數值分數、區分三種特質，以及 Glitch 準備與後果條文。
- 修正 `humanity`、`Lifestyle Impact`、`Cardio Bunny`、`Diet Hopper`、`Ladder Climber` 等舊草稿的誤譯或過度縮限；維持原文的訪談順序、內部分數、最低題數及原始報告要求，不套用目前社群版的替代政策。

以上譯註與維護說明都在正文之外。日後若發現漏譯或誤譯，應對照這份固定英文參考修正譯文並更新其指紋；來源內容變更則另記核對日期、差異與新指紋，不能無聲覆蓋後仍沿用舊版本標示。

## 維護檢查的邊界

`scripts/check_prompt_parity.py` 的預設路徑是根目錄 `PROMPT.md`／`PROMPT_TW.md`；簡中檢查亦明確指定根目錄文件。本目錄不加 `prompt-parity` 標記、不納入社群版固定句子或安全政策的測試範圍，不能為了通過這些檢查改寫原文。

原文與譯文是否對應，依來源指紋、段落校閱與譯註判斷；不同語言的模型行為、評估有效性及使用效果尚未因此獲得驗證。完整的原版／社群修訂差異整理另見 [#16](https://github.com/chiisen/HUMAN3_PROMPT/issues/16)。
