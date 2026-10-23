# 重要規則雙語對照

英文為社群修訂版的主要維護來源。下表是英繁人工語意校閱入口，簡中另依繁中修訂版對照同項規則；不代表自動翻譯驗證或實際模型驗收，也不套用到原文參考與忠實譯本。修改規則時同步三語、檢視相互衝突；可選少量相關對話案例觀察，未跑者標示未執行。完整人工清單見[維護指南](MAINTENANCE.md)。

| 規則 | 英文定位（PROMPT.md） | 繁中定位（PROMPT_TW.md） | 人工確認重點 |
|---|---|---|---|
| 反思定位 | 首段、Context、Introduction | 首段、背景、簡介 | 不承諾準確測量、診斷或揭露真相 |
| 優先級 | Evidence-Grounded Assessment Rules | 以回答依據進行判讀 | 安全、使用者控制、證據要求優先於模型與模板 |
| 證據及未知 | Evidence / Interpretation / Confidence / Alternative explanations / Unknowns | 實際回答／解讀／信心／替代解釋／未知 | 不捏造引文或原因；衝突與資料不足保留未判定 |
| 題數 | Constraints | 約束條件 | 3 題是目標、8 題是上限；追問與拒答計入、不重設 |
| 單題及停止 | Constraints | 約束條件 | 一次一題；尊重跳過、整象限略過、暫停與停止 |
| 摘要確認 | Summary Confirmation Before a Full Report | 完整報告前的摘要確認 | 先摘要、修正後更新；已選範圍不重複確認 |
| 分數與缺漏 | Metatype & Lifestyle Generation / Never show numerical scores | 元類型與生活型態生成／不計算發展分數 | 不計算隱藏分數或百分比，不補缺漏，不強指定單一層級 |
| 風險界線 | High-Risk Actions: Safety Boundary | 高風險行為安全界線 | 不以層級批准高風險行為，不提供個人化許可 |
| AI 使用 | AI use / Constraints | AI 使用／約束條件 | 依實際使用討論隱私、依賴與自主判斷，非層級許可 |
| 報告及行動 | Output Format | 輸出格式 | 各象限同樣要求依據及不確定性；預設一個可逆實驗與回顧條件，長期規劃須有需求與依據 |

區段標記的對應結構為：`model-fundamentals` 內含 `high-risk-safety`，之後依序為 `interview-flow`、`report-format`。判讀依據、開場與訪談流程均歸入 `interview-flow`。

維護者可選的區段檢查會拒絕缺少、重複、空白、未知、交錯的標記，以及兩語順序或巢狀結構不同。合法標記內即使放入無關內容仍可能通過；語意與模型輸出必須另行檢視。
