# 原文與社群修訂版差異對照

[返回首頁](../README.md)｜[來源與譯註](../reference/README.md)｜[對話案例](CONVERSATION_ACCEPTANCE.md)｜[結果模板](ACCEPTANCE_RESULT_TEMPLATE.md)

本文件比較 Dan Koe 公開提示詞的英文參考與本專案社群修訂版。修訂包含翻譯、流程整理及設計取捨，不能一律稱為「更準確」。維護者在此負責文字、翻譯與指令一致性維護；本倉庫未提供可支持心理評估專業資格、臨床能力或原作者背書的證據，不以維護行為暗示具備這些資格。

This comparison is mainly in Traditional Chinese. It documents editorial and behavioral design choices, not demonstrated improvements in psychological accuracy. Model comparisons have not been run, and neither professional validation nor the author's endorsement is established.

## 比較基準與引用

本次兩側都固定在提交 `34d8926f989a321d00e42e82fcef5ed007d72fda`（PR #23 合併後）。以下連結固定該提交，不隨 `main` 改動：

| 材料 | 固定版本與用途 |
|---|---|
| 原文側 | [英文參考](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md)，研究原作規則 |
| 翻譯側 | [非官方繁中譯本](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/TRANSLATION_TW.md)，輔助閱讀原文，不套用修訂版政策 |
| 修訂側 | [英文](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md)、[繁中](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT_TW.md)、[簡中](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT_CN.md)，各自獨立執行與記錄 |

英文參考正文 SHA-256 為 `f982a69c5d97b8075cfaeb1808ec885e61dcf9a56d04d65b7050b55348fbb0c4`；繁中譯本正文為 `f1253d11d691278be9cbccd890359a400ba7a22a8642d7a0fc5f902c4c216c56`。提取範圍、來源核對日期與空白正規化方法見[來源說明](../reference/README.md)。這是核對時的提示詞文字參考，不能當成發布當日未修改的網頁封存。

引用或重跑時，記錄提交 SHA、檔名、語言與實際輸入範圍。原文與譯本只取 `reference-body` 標記之間的正文；修訂版略過首段來源註記，保留其餘完整內容並記錄是否保留 `prompt-parity` 註解。不要把此比較文件、譯註或某一版的補充規則貼進另一版的系統指令。後續提示詞若有變動，須另記新基準，不能沿用本表代表新版。

## 導覽

- [A：翻譯、命名與結構](#difference-a)
- [B：角色、證據與不確定性](#difference-b)
- [C：題數、拒答、暫停與停止](#difference-c)
- [D：摘要確認與報告範圍](#difference-d)
- [E：移除隱藏評分](#difference-e)
- [F：高風險行為與 AI 使用](#difference-f)
- [G：行動規劃與條件式警示](#difference-g)
- [驗證證據與限制](#evidence)

<a id="difference-a"></a>
## A：翻譯、命名與結構

- **分類／原始設計：** 文字與可讀性。原文使用 HUMAN 3.0 名稱；忠實繁中譯本保留原作訪談、計分、風險與報告要求。
- **修訂與動機：** 社群版也使用 HUMAN 3.0，但加註非官方身分，以 Git 提交識別修訂。根目錄英文為維護來源，繁中同步意思，簡中由繁中轉換並校對；加入區段標記供維護，不是另創作者的框架版本。
- **段落：** 原文與三份修訂版的檔首；翻譯校正項目見[來源說明的「譯註與校對」](../reference/README.md)；區段對照見[雙語規則](PROMPT_RULES.md)，簡中來源見[維護指南](MAINTENANCE.md)。
- **可能影響／取捨：** 可協助讀者分辨版本；譯法或語言差異仍可能改變模型反應。三語修訂版不能當成原文的等價翻譯。
- **證據：** #15 已記錄來源文字核對、正文指紋及本專案校譯；未做外部專業譯者審閱。區段檢查只驗證結構，不能證明翻譯品質、可讀性提升或跨語言行為一致。

<a id="difference-b"></a>
## B：角色、證據與不確定性

- **分類／原始設計：** 判讀取捨。原文定位為發展評估者，要求準確評估、揭示隱藏連結、區分根因與症狀，並以既有模型增加可信度；未規定逐項列出回答依據、假設、信心理由與未知。
- **修訂與動機：** 改為反思引導者，不聲稱能準確測量或由有限回答確立原因。證據與使用者控制優先於角色、框架範例與報告欄位；重要判讀須區分回答、假設、信心與理由、替代解釋及未知，資訊不足可不判定。目的在限制無依據推論與強行填表。
- **段落：** 原文[角色與背景 L8–11](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L8)、[跨象限分析 L688 起](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L688)、[約束 L737–741](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L737)；修訂版[角色 L3–6](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L3)、[Evidence-Grounded Assessment Rules L479–493](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L479)，繁中對應「以回答依據進行判讀」及各象限報告欄位。
- **可能影響／取捨：** 預期更容易檢查判讀根據，也可能增加篇幅或保留更多未知。模型自報 High／Medium／Low 並非經校準的機率，不能由此推論判讀更準確。
- **證據：** 可直接檢視規則及欄位；C01、C02、C07 可觀察資訊不足、衝突與無依據保證，均未執行。沒有錯誤率降低或心理測量有效性的證據。

<a id="difference-c"></a>
## C：題數、拒答、暫停與停止

- **分類／原始設計：** 指令與流程一致性。原文要求一次一題、每象限最少 3 題最多 8 題，另要求持續追問直到有信心；未明定拒答計數、跨象限歸屬、摘要後題數或跳過／暫停／停止優先順序。
- **修訂與動機：** 3 題改為目標，8 題為上限；追問、澄清及拒答均計數，跨象限題須事先歸屬，不重設或轉移預算。可略過問題／象限、暫停與停止，不換句話追索拒答資訊；無可用依據可提早結束。目的在明確處理衝突與退出權。
- **段落：** 原文[Constraints L722–727](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L722)；修訂版[Constraints L656–666](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L656)，繁中對應「約束條件」的題數及停止優先段落。
- **可能影響／取捨：** 訪談可能較短、未知較多；停止追問也可能減少可用資訊。原文沒有明訂退出規則，不代表實際模型必然拒絕使用者停止。
- **證據：** 文字及區段可檢查；C03、C04、C09 為待執行觀察。未證明實際模型一定正確計數、較尊重拒答或讓使用者感到更舒適。

<a id="difference-d"></a>
## D：摘要確認與報告範圍

- **分類／原始設計：** 流程設計取捨。原文列出完整輸出格式，未指定報告前須先顯示摘要並取得確認。
- **修訂與動機：** 新增短摘要、更正、確認及範圍選擇；可選完整報告、指定章節或停在摘要。已確認並選範圍就直接產出，不重複確認；摘要不重設題數。目的在提供更正與控制輸出範圍的機會。
- **段落：** 原文[Output Format L749 起](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L749)；修訂版[Summary Confirmation Before a Full Report L688–697](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L688)，繁中對應「完整報告前的摘要確認」。
- **可能影響／取捨：** 可能減少錯誤資料流入後續報告，但增加至少一次互動，也改變原作直接產出報告的體驗。使用者確認不等於內容客觀正確。
- **證據：** 可核對新增狀態與範圍規則；C05、C06、C10 均未執行。沒有可用性研究或準確性改善證據。

<a id="difference-e"></a>
## E：移除隱藏評分

- **分類／原始設計：** 評分設計取捨。原文按 Level 1／2／3 各給 1／2／3 分，加總除以 12 得出整體發展，要求隱藏分數且不在輸出顯示數值。
- **修訂與動機：** 明定不計算發展分數、隱藏總分與百分比；保留有依據的定性觀察，可省略描述性類型，資料不足不強行歸級。維護者因原文未明訂總分的決策用途、缺漏處理與精確性依據而移除，這是本專案的取捨。
- **段落：** 原文[Metatype & Lifestyle Generation L700–710](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L700)、[不顯示數值 L743](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L743)；修訂版[同名生成段落 L641–642](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L641)，繁中對應「元類型與生活型態生成」。
- **可能影響／取捨：** 失去原作的數值規則，因此需要研究原始評分設計時應使用原文。沒有輸出分數不能證明模型內部沒有計算；保留的層級與類型也未因此成為有效測量。
- **證據：** 文字確認評分指令已移除；C07 僅能觀察是否輸出無依據分數，不能檢查隱藏計算，且尚未執行。未證明移除分數提高判讀效度。

<a id="difference-f"></a>
## F：高風險行為與 AI 使用

- **分類／原始設計：** 建議與風險政策取捨。原文把 Glitches 視為加速器，按層級討論準備、風險與適合的選項；也包含風險警告，並非毫無限制地鼓勵所有人使用。
- **修訂與動機：** 不用 HUMAN 層級批准迷幻藥、PEDs／類固醇或刻意財務困境，不給個人適用性判斷或操作指示，改為說明訪談能力界線、專業求助與可逆替代方向。AI 的隱私、依賴與獨立判斷依實際使用討論，不以層級作許可門檻。目的在避免把框架分類當安全許可。
- **段落：** 原文[Glitches L172–274](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L172)、[Glitch User Detection L676–686](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L676)、[GLITCH ASSESSMENT L836–870](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L836)；修訂版[High-Risk Actions: Safety Boundary L169–201](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L169)、[風險與支持輸出 L759–763](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L759)，繁中對應「高風險行為安全界線」及「風險與支援建議」。
- **可能影響／取捨：** 修訂版刻意不提供原作的層級式加速器建議，故不適合當作原作規則的完整重現。限制指令的存在不保證模型永不產出有害建議，也不證明事故風險降低。
- **證據：** 可檢查替換的知識庫、訪談、約束與報告條文；C08 尚未執行，未做安全性成效研究或個人適用性評估。

<a id="difference-g"></a>
## G：行動規劃與條件式警示

- **分類／原始設計：** 報告與介入設計取捨。原文固定要求 30 天、90 天、6–12 個月規劃、多項每日任務、資源推薦及 24 小時行動；部分警示使用必然崩潰／摧毀的語氣。
- **修訂與動機：** 預設一項有回答依據的優先問題、一個自願可逆實驗及回顧條件；可行性未知時保留條件或在預算內釐清。更多任務與長期規劃須使用者要求且有依據，不強加期限；警示改成有依據的假設，無依據可省略。目的在減少填表式任務與無依據預測。
- **段落：** 原文[規劃 L790–834](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L790)、[警示與即刻行動 L872–894](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/reference/ORIGINAL.md#L872)；修訂版[OPTIONAL NEXT EXPERIMENT L747–757](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L747)、[警示與第一步 L765–787](https://github.com/chiisen/HUMAN3_PROMPT/blob/34d8926f989a321d00e42e82fcef5ed007d72fda/PROMPT.md#L765)，繁中對應「可選的下一個實驗」「警示要點」及「可選的第一步」。
- **可能影響／取捨：** 行動量可能減少，也可能不滿足想一次取得完整路線圖的讀者。可逆與小型不等於對每個人都安全有效；仍須檢查具體內容與條件。
- **證據：** 可核對模板與合成示例；C06 及 C01／C02 的依據限制尚未實測。合成報告不是模型測試輸出，沒有持續改善生活或介入有效性的證據。

<a id="evidence"></a>
## 驗證證據與限制

| 證據層次 | 已有材料／本次範圍 | 不能推論 |
|---|---|---|
| 本機工具／結構檢查 | #16 當時使用區段工具及文字斷言，結果記於 PR；#17 起移除固定文字斷言，只保留可選區段及 Git 工具測試，內容改依[人工清單](MAINTENANCE.md)校閱 | 模型遵循率、語意等價、心理評估準確度 |
| 本專案人工文字／翻譯對照 | #15 的來源指紋與譯註；本表的段落校閱，非外部專業審閱 | 翻譯認證、使用者體驗或專業背書 |
| 實際模型對話 | [C01～C10](CONVERSATION_ACCEPTANCE.md) 及[結果模板](ACCEPTANCE_RESULT_TEMPLATE.md)；原文、譯本與三語修訂版比較均未執行 | 任一版本較佳、通過率、跨語言或跨模型穩定性 |
| 心理測量／臨床與介入效果 | 本專案未建立信度、效度、臨床研究或介入成效證據 | 科學驗證、診斷能力、降低傷害或提升成長效果 |

原文作為另一種設計的比較材料，不預設它會違反規則，也不把缺少修訂版政策直接算成原文失敗。比較時先保存實際行為，再區分各版自身要求與共同觀察項目。原始對話、模型設定、版本與未覆蓋條件的紀錄方式見對話案例文件；不為填滿比較表而編造使用心得、外部評測或模型輸出。

修訂版仍保留四象限、層級、原型及部分強烈框架用語。證據規則要求限制其個人判讀，並未對框架所有主張完成科學查核，也未讓這些分類成為經驗驗證的測量。本文件只列重要行為差異；逐字差異請比較固定提交中的各文件，後續修訂依 [CHANGELOG](../CHANGELOG.md) 與 Git 歷史追溯。
