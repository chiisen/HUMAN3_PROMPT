# 維護指南

[返回繁體中文首頁](../README.md)｜[简体中文](../README.zh-CN.md)｜[English](../README.en.md)

本文件供維護者使用；一般讀者只需複製提示詞，不必安裝下列工具。所有命令都在專案根目錄執行，文中檔名也以根目錄為準。目前的雙語檢查對象是社群修訂版，不代表對原作者版本或忠實翻譯的驗證。

## 提示詞維護

- `PROMPT.md` 為主要維護來源；修改後再將相同意義同步至 `PROMPT_TW.md`，最後依繁中修訂版更新 `PROMPT_CN.md` 並校對。三者皆為社群修訂版，簡中版不使用自由改寫或去 AI 味處理。
- 三份提示詞以 `prompt-parity` 區段標記對應的重要內容，不要求翻譯逐字一致；新增或重組重要區段時，請在三份文件保留相同的標記 ID：`model-fundamentals`、`high-risk-safety`、`interview-flow`、`report-format`。
- 使用 Python 標準函式庫執行 `python scripts/check_prompt_parity.py`，檢查必要區段是否在兩種語言中成對存在、標記唯一、內容非空，並比對兩語區段順序及巢狀關係，無需安裝額外套件。此檢查不判斷翻譯品質或語意是否完全等價，仍需人工校閱；請使用 [重要規則雙語對照](PROMPT_RULES.md) 逐項檢查。
- 上述預設命令檢查英文與繁中；另執行 `python -B scripts/check_prompt_parity.py PROMPT_TW.md PROMPT_CN.md` 檢查繁中與簡中的區段。這沿用現有工具，不新增測試框架或 CI。

### 簡中版本來源與校對

- `PROMPT_CN.md` 首次轉換依 [1606b7cdf59cbd57a7277af842f5bbe9334dd538 的 PROMPT_TW.md](https://github.com/chiisen/HUMAN3_PROMPT/blob/1606b7cdf59cbd57a7277af842f5bbe9334dd538/PROMPT_TW.md) 進行；該歷史來源檔案的 Git blob SHA 為 `9d0a2bb79a37cc46273e790c771b971e0e12f78e`。
- #14 後續同步將三份提示詞的框架名稱由 HUMAN 3.01 更正為 HUMAN 3.0，並加上非官方來源註記；這些是初次轉換後的修訂。框架名稱沿用原作者的 HUMAN 3.0，本專案修訂以 Git 提交追溯，不另設官方版本號。
- 本次使用 Windows PowerShell 7 中的 `Microsoft.VisualBasic.Strings.StrConv`，指定 `VbStrConv.SimplifiedChinese` 與 LCID `2052`，僅轉換漢字並保留其餘字元，避免舊式轉換損失圖示。另校正殘留字形與用語：`後→后`、`於→于`、`徵→征`、`麽→么`、`谘→咨`、`蒐→搜`、`重覆→重复`、`反覆→反复`、`回覆→回复`、`计画→计划`。後續更新須同步記錄來源版本，不能把本次 SHA 當成永遠適用的來源。
- 逐段核對否定詞、題數、跳過／停止、證據規則、摘要確認與高風險行為界線；保留段落、標記、數字、專有名詞與網址。這是修訂版的簡中轉換，不是原作者原文的忠實翻譯。
- 字形、結構與內容對照不證明不同語言的模型行為等價；簡中版的實際模型對話驗收尚未執行。

## 驗證方式

在專案根目錄執行 `python -B -m unittest discover -s tests -v` 與 `python -B scripts/check_prompt_parity.py`。Python 版本以 `.python-version` 為準；Git 設定測試需要 Git 與 PowerShell 7，且只操作臨時倉庫。

這些測試包含靜態規則文字檢查與工具行為測試，不能證明模型遵循提示詞。請另依 [對話行為驗收案例](CONVERSATION_ACCEPTANCE.md) 在新對話逐輪執行，使用 [結果模板](ACCEPTANCE_RESULT_TEMPLATE.md) 記錄模型、設定、提示詞 SHA、原始輸出及判定理由。雙語、不同模型與不同版本分開記錄；未執行或未覆蓋的情境不能標為通過。本次建立案例時尚未執行外部模型驗收。

Python 快取由 `.gitignore` 忽略，不需刪除既有檔案。

## Git 推送遠端設定

在本專案 Git checkout 或其子目錄內，用腳本實際路徑執行 `pwsh -File ./setup_git_sync.ps1`（根目錄範例），可設定預期的五個 `origin` 推送目的地。任何寫入前會檢查所有 `origin` fetch URL；缺少 origin、主機／擁有者／專案名稱不符時直接拒絕，保留原設定。

支援以下格式，專案名稱限 `HUMAN3_PROMPT`，`.git` 可省略：

- HTTPS：`https://github.com/<owner>/HUMAN3_PROMPT.git`，owner 限 `chiisen`、`edwin45168899`、`edwiin1688`、`NathanEvans1221`；GitLab 限 `https://gitlab.com/chiisen/HUMAN3_PROMPT.git`。
- SSH：`git@<host>:<owner>/HUMAN3_PROMPT.git` 或 `ssh://git@<host>/<owner>/HUMAN3_PROMPT.git`。正式主機使用上述 owner；既有 SSH 別名僅接受 `github.com-chiisen/chiisen`、`github.com-edwiin1688/edwiin1688`、`github.com-NathanEvans1221/NathanEvans1221`、`gitlab.com-chiisen/chiisen` 的配對（此處以斜線表示主機／擁有者，SCP 格式實際使用冒號）。
- 不接受本機路徑、自訂埠、其他主機或 owner、附帶查詢參數的 URL；新增目的地需先更新腳本與測試，不能用同名目錄代替來源檢查。

這是本機 URL 白名單防誤操作，不能證明遠端擁有權或排除 Git／SSH 的額外 URL 重寫設定。腳本只替換本機 `remote.origin.pushurl`，不修改 fetch URL、其他 remote 或全域設定；可重複執行，不會連線遠端或推送。本次只測試臨時倉庫，未對目前 checkout 執行設定腳本。
