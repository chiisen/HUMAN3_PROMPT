# TODO

## HUMAN 3.0 提示詞優化

以下七項任務已透過 GitHub CLI（`gh`）建立為本專案 Issues。實作時依建議順序處理，並以各 Issue 的完成條件驗收：

1. [ ] [#4 建立英文與繁中提示詞的一致性檢查](https://github.com/chiisen/HUMAN3_PROMPT/issues/4) — 先建立雙語維護方式，避免後續規則只更新單一版本。
2. [ ] [#1 移除以 HUMAN 3.0 分級判定高風險加速器適用性的建議](https://github.com/chiisen/HUMAN3_PROMPT/issues/1) — 優先處理迷幻藥、PEDs／類固醇及極端財務壓力等安全界線。
3. [ ] [#2 要求發展判讀附上對話依據與不確定性](https://github.com/chiisen/HUMAN3_PROMPT/issues/2) — 讓結論可追溯，並在資料不足時保留判斷。
4. [ ] [#3 將長篇評估改為摘要確認後再展開](https://github.com/chiisen/HUMAN3_PROMPT/issues/3) — 先讓使用者確認摘要，再按需要產出完整分析。
5. [ ] [#5 澄清提示詞用途並補上使用與隱私說明](https://github.com/chiisen/HUMAN3_PROMPT/issues/5) — 依照完成後的提示詞安全規則更新 README。
6. [ ] [#7 標示評估報告為示例並確認個人資料已去識別化](https://github.com/chiisen/HUMAN3_PROMPT/issues/7) — 確認來源與授權；若無法確認，改為合成案例或移除敏感細節。公開分享前應優先處理。
7. [ ] [#6 讓 Git 多遠端同步腳本可安全重複執行](https://github.com/chiisen/HUMAN3_PROMPT/issues/6) — 與提示詞內容無依賴，可獨立排後處理。

### Issue 關閉規則

- 以上任務都是由 `gh` 建立的 GitHub Issues，完成狀態以各 Issue 的驗收條件為準。
- **每項任務完成並驗收後，立即為該 Issue commit+push 並關閉。** 逐項處理，不必等七項全部完成才關閉；每次關閉後確認遠端 Issue 狀態。
