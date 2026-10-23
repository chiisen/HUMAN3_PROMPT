# TODO

## 目前狀態（2026-10-23）

- [ ] [#27 初次選版入口與提示詞複製指引](https://github.com/chiisen/HUMAN3_PROMPT/issues/27)：已實作，待 PR 審閱合併。

### 前批結案

截至 PR #25 合併，GitHub 已建立的 19 個優化 Issue 均已關閉，沒有待合併的功能 PR，也沒有待實作的既定優化任務。

- [x] [#14 保留原名與非官方定位](https://github.com/chiisen/HUMAN3_PROMPT/issues/14)
- [x] [#15 原文、忠實翻譯與修訂版分流](https://github.com/chiisen/HUMAN3_PROMPT/issues/15)
- [x] [#16 修訂差異對照與驗證界線](https://github.com/chiisen/HUMAN3_PROMPT/issues/16)
- [x] [#17 精簡測試與輔助工具](https://github.com/chiisen/HUMAN3_PROMPT/issues/17)
- [x] [#18 三語 README 與文字精簡](https://github.com/chiisen/HUMAN3_PROMPT/issues/18)
- [x] [#20 簡體中文提示詞](https://github.com/chiisen/HUMAN3_PROMPT/issues/20)

實際模型對話、原文／修訂版比較及外部專業譯者審閱尚未執行，屬已揭露的驗證限制，不是上述 Issue 遺漏的實作。日後若執行，沿用既有案例與模板，另記版本、設定及原始輸出。

下方保留歷史完成項目；#13 當時加入的 CI 已依使用者要求移除，#17 亦移除失去用途的 CI 輔助工具，不表示目前仍有 CI。

## 後續優化（#8～#13）

- [x] [#8 統一提示詞定位與證據優先規則](https://github.com/chiisen/HUMAN3_PROMPT/issues/8)：本機驗收後逐項推送與關閉。
- [x] [#9 明確定義訪談流程](https://github.com/chiisen/HUMAN3_PROMPT/issues/9)
- [x] [#10 校齊雙語區段與規則](https://github.com/chiisen/HUMAN3_PROMPT/issues/10)
- [x] [#11 建立對話行為驗收案例](https://github.com/chiisen/HUMAN3_PROMPT/issues/11)
- [x] [#12 縮減報告負擔與移除無用途分數](https://github.com/chiisen/HUMAN3_PROMPT/issues/12)
- [x] [#13 CI、快取忽略與 Git 腳本防呆](https://github.com/chiisen/HUMAN3_PROMPT/issues/13)

## HUMAN 3.0 提示詞優化

以下七項任務已透過 GitHub CLI（`gh`）建立為本專案 Issues。依安全風險與工作相依性排序，並以各 Issue 的完成條件驗收：

1. [x] [#1 移除以 HUMAN 3.0 分級判定高風險加速器適用性的建議](https://github.com/chiisen/HUMAN3_PROMPT/issues/1) — 移除迷幻藥、PEDs／類固醇及刻意製造財務困境的分級建議。
2. [x] [#7 標示評估報告為示例並確認個人資料已去識別化](https://github.com/chiisen/HUMAN3_PROMPT/issues/7) — 來源與授權無法由 repo 證明，已改為虛構合成案例並標示限制。
3. [x] [#4 建立英文與繁中提示詞的一致性檢查](https://github.com/chiisen/HUMAN3_PROMPT/issues/4) — 已標記必要區段並加入標準函式庫檢查工具。
4. [x] [#2 要求發展判讀附上對話依據與不確定性](https://github.com/chiisen/HUMAN3_PROMPT/issues/2) — 讓結論可追溯，並在資料不足時保留判斷。
5. [x] [#3 將長篇評估改為摘要確認後再展開](https://github.com/chiisen/HUMAN3_PROMPT/issues/3) — 先讓使用者確認摘要，再按需要產出完整分析。
6. [x] [#5 澄清提示詞用途並補上使用與隱私說明](https://github.com/chiisen/HUMAN3_PROMPT/issues/5) — 依照完成後的提示詞安全規則更新 README。
7. [x] [#6 讓 Git 多遠端同步腳本可安全重複執行](https://github.com/chiisen/HUMAN3_PROMPT/issues/6) — 與提示詞內容無依賴，可獨立排後處理。

### Issue 關閉規則

- 以上任務都是由 `gh` 建立的 GitHub Issues，完成狀態以各 Issue 的驗收條件為準。
- **每項任務完成並驗收後，立即為該 Issue commit+push 並關閉。** 逐項處理，不必等七項全部完成才關閉；每次關閉後確認遠端 Issue 狀態。
