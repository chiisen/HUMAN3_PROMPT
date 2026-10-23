# 維護指南

[返回繁體中文首頁](../README.md)｜[简体中文](../README.zh-CN.md)｜[English](../README.en.md)

本文件供維護者使用；一般讀者只需複製提示詞，不必安裝下列工具。所有命令都在專案根目錄執行，文中檔名也以根目錄為準。目前的雙語檢查對象是社群修訂版，不代表對原作者版本或忠實翻譯的驗證。

## 人工檢查清單

只檢查本次變更涉及的項目，不要求每次跑完整案例。這份清單取代原先的安全、證據與示例固定句子測試，判斷意思與相互衝突，不要求指定字串：

- [ ] 來源與版本：三語 README 與提示詞能辨識 Dan Koe HUMAN 3.0、非官方修訂及 Git 版本；原文、忠實譯本、社群修訂分開，來源指紋可追溯。原文／忠實譯本不強套下列修訂政策。
- [ ] 翻譯：以英文修訂版對照繁中，再對照簡中，檢查否定、題數、條件、退出方式與風險界線；原文譯本另依來源校譯，不混入社群規則。詳細定位見[雙語規則](PROMPT_RULES.md)。
- [ ] 判讀：反思定位、回答依據／假設／信心理由／替代解釋／未知分開；不足或矛盾不捏造原因、引文或強行歸級，不隱藏計分，不強填欄位或必然災難預測。
- [ ] 流程：一次一題、3 題為目標及 8 題上限；追問與拒答計數，不重設；尊重跳過、略過象限、暫停與停止。先摘要供更正，再依確認範圍產出，不重複確認。
- [ ] 建議：不以層級批准迷幻藥、PEDs／類固醇或刻意財務困境，不提供個人化適用性判斷或操作指示；保留專業求助方向。AI 使用依實際情境討論隱私、依賴及自主判斷。
- [ ] 報告與示例：預設一個有依據、可行且自願可逆的實驗及回顧條件，更多規劃須有需求與依據；兩份示例使用同一虛構案例，保留合成、非真實訪談及非效度證據標示，不混入可識別個資或當成模型實測。
- [ ] 說明與證據：一般讀者可直接複製提示詞，保留隱私提醒與非心理測驗／診斷限制；不把人工校閱、工具通過或使用者確認稱為模型行為、心理測量有效性或作者認可。重要變更同步差異對照及 CHANGELOG，未跑的模型案例標示未執行。

## 提示詞維護

- 根目錄三份 `PROMPT*.md` 是社群修訂版；`reference/` 的[英文參考與繁中譯本](../reference/README.md)獨立保存，來源及指紋以該目錄說明為準。更新修訂版時不要同步改寫參考文字，也不要為了套用現行安全政策或區段標記而修改原文。
- `PROMPT.md` 為主要維護來源；修改後再將相同意義同步至 `PROMPT_TW.md`，最後依繁中修訂版更新 `PROMPT_CN.md` 並校對。三者皆為社群修訂版，簡中版不使用自由改寫或去 AI 味處理。
- 三份提示詞以 `prompt-parity` 區段標記對應的重要內容，不要求翻譯逐字一致；新增或重組重要區段時，請在三份文件保留相同的標記 ID：`model-fundamentals`、`high-risk-safety`、`interview-flow`、`report-format`。
- 維護者可選用 Python 標準函式庫執行 `python scripts/check_prompt_parity.py`，檢查必要區段是否在兩種語言中成對存在、標記唯一、內容非空，並比對兩語區段順序及巢狀關係，無需安裝額外套件。此檢查不判斷翻譯品質或語意是否完全等價，仍需人工校閱；請使用 [重要規則雙語對照](PROMPT_RULES.md) 逐項檢查。
- 上述預設命令檢查英文與繁中；另執行 `python -B scripts/check_prompt_parity.py PROMPT_TW.md PROMPT_CN.md` 檢查繁中與簡中的區段。這沿用現有工具，不新增測試框架或 CI。

### 簡中版本來源與校對

- `PROMPT_CN.md` 首次轉換依 [1606b7cdf59cbd57a7277af842f5bbe9334dd538 的 PROMPT_TW.md](https://github.com/chiisen/HUMAN3_PROMPT/blob/1606b7cdf59cbd57a7277af842f5bbe9334dd538/PROMPT_TW.md) 進行；該歷史來源檔案的 Git blob SHA 為 `9d0a2bb79a37cc46273e790c771b971e0e12f78e`。
- #14 後續同步將三份提示詞的框架名稱由 HUMAN 3.01 更正為 HUMAN 3.0，並加上非官方來源註記；這些是初次轉換後的修訂。框架名稱沿用原作者的 HUMAN 3.0，本專案修訂以 Git 提交追溯，不另設官方版本號。
- 本次使用 Windows PowerShell 7 中的 `Microsoft.VisualBasic.Strings.StrConv`，指定 `VbStrConv.SimplifiedChinese` 與 LCID `2052`，僅轉換漢字並保留其餘字元，避免舊式轉換損失圖示。另校正殘留字形與用語：`後→后`、`於→于`、`徵→征`、`麽→么`、`谘→咨`、`蒐→搜`、`重覆→重复`、`反覆→反复`、`回覆→回复`、`计画→计划`。後續更新須同步記錄來源版本，不能把本次 SHA 當成永遠適用的來源。
- 逐段核對否定詞、題數、跳過／停止、證據規則、摘要確認與高風險行為界線；保留段落、標記、數字、專有名詞與網址。這是修訂版的簡中轉換，不是原作者原文的忠實翻譯。
- 字形、結構與內容對照不證明不同語言的模型行為等價；簡中版的實際模型對話驗收尚未執行。

## 修訂透明度

[原文／修訂差異對照](REVISION_COMPARISON.md)固定來源與修訂版本，分開記錄翻譯、流程及評分／判讀／風險政策取捨。提示詞重要行為變更時，同步更新相關差異、固定版本與驗證狀態；不能只因靜態測試通過就宣稱更準確。維護角色限於已揭露的文字與指令維護，不暗示專業資格或作者認可。

原文比較不套用社群版的固定句子或政策作為合格門檻。依[比較操作方式](CONVERSATION_ACCEPTANCE.md)及[結果模板](ACCEPTANCE_RESULT_TEMPLATE.md)保存雙方版本、設定與原始對話；本機檢查、人工校閱、模型行為與心理測量有效性須分別記錄。

## 驗證方式

一般讀者不需要 Python、PowerShell、Git 腳本或測試。以下僅供維護者依變更選用；Python 版本以 `.python-version` 為準，無額外套件依賴，不設定 CI。

| 保留工具／測試 | 用途與執行方式 |
|---|---|
| `scripts/check_prompt_parity.py` | 可選的社群修訂版區段完整性檢查，預設只讀根目錄英文／繁中；另指定繁中／簡中。只判定標記、非空、順序與巢狀，不檢查句子或語意。保留原因是可找出翻譯維護時的區段遺漏。 |
| `tests/test_prompt_parity.py` | 使用臨時合成文字測試區段工具的成功／錯誤處理，不鎖定提示詞句子。命令：`python -B -m unittest discover -s tests -p 'test_prompt_parity.py' -v`。 |
| `setup_git_sync.ps1`／`tests/test_setup_git_sync.py` | 個人多遠端設定工具與防誤操作測試；保留唯一副本及錯倉庫拒絕、fetch／其他 remote 保留、重複執行等保護。測試只操作臨時倉庫，需要 Git 與 PowerShell 7；命令：`python -B -m unittest discover -s tests -p 'test_setup_git_sync.py' -v`。與提示詞使用無關，詳見下節。 |

若同時維護兩個工具，可執行 `python -B -m unittest discover -s tests -v`。提交前直接執行 `git diff --check`；若已暫存則另用 `git diff --cached --check`。不再保留專為 CI 封裝的提交差異工具及其測試。測試數量只記錄工具驗證範圍，不作提示詞成效證據。

人工內容校閱依上方清單；模型行為觀察可從既有[對話案例](CONVERSATION_ACCEPTANCE.md)選少量與變更相關的代表案例，例如改摘要流程選 C05／C06，改風險界線選 C08。使用[結果模板](ACCEPTANCE_RESULT_TEMPLATE.md)記錄版本、語言、模型設定、原始輸入輸出與判定；其餘未跑案例保留未執行。工具檢查不能替代人工翻譯校閱或模型觀察，三者也不證明心理測量有效性。本次未執行外部模型驗收。

Python 快取由 `.gitignore` 忽略，不需刪除既有檔案。

## 個人 Git 同步工具（與提示詞使用無關）

在本專案 Git checkout 或其子目錄內，用腳本實際路徑執行 `pwsh -File ./setup_git_sync.ps1`（根目錄範例），可設定預期的五個 `origin` 推送目的地。任何寫入前會檢查所有 `origin` fetch URL；缺少 origin、主機／擁有者／專案名稱不符時直接拒絕，保留原設定。

支援以下格式，專案名稱限 `HUMAN3_PROMPT`，`.git` 可省略：

- HTTPS：`https://github.com/<owner>/HUMAN3_PROMPT.git`，owner 限 `chiisen`、`edwin45168899`、`edwiin1688`、`NathanEvans1221`；GitLab 限 `https://gitlab.com/chiisen/HUMAN3_PROMPT.git`。
- SSH：`git@<host>:<owner>/HUMAN3_PROMPT.git` 或 `ssh://git@<host>/<owner>/HUMAN3_PROMPT.git`。正式主機使用上述 owner；既有 SSH 別名僅接受 `github.com-chiisen/chiisen`、`github.com-edwiin1688/edwiin1688`、`github.com-NathanEvans1221/NathanEvans1221`、`gitlab.com-chiisen/chiisen` 的配對（此處以斜線表示主機／擁有者，SCP 格式實際使用冒號）。
- 不接受本機路徑、自訂埠、其他主機或 owner、附帶查詢參數的 URL；新增目的地需先更新腳本與測試，不能用同名目錄代替來源檢查。

這是本機 URL 白名單防誤操作，不能證明遠端擁有權或排除 Git／SSH 的額外 URL 重寫設定。腳本只替換本機 `remote.origin.pushurl`，不修改 fetch URL、其他 remote 或全域設定；可重複執行，不會連線遠端或推送。本次只測試臨時倉庫，未對目前 checkout 執行設定腳本。
