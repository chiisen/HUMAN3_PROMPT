# 維護指南

[返回繁體中文首頁](../README.md)｜[简体中文](../README.zh-CN.md)｜[English](../README.en.md)

本文件供維護者使用；一般讀者只需複製提示詞，不必安裝下列工具。所有命令都在專案根目錄執行，文中檔名也以根目錄為準。目前的雙語檢查對象是社群修訂版，不代表對原作者版本或忠實翻譯的驗證。

## 提示詞維護

- `PROMPT.md` 為主要維護來源；修改後再將相同意義同步至 `PROMPT_TW.md`。
- 兩份提示詞以 `prompt-parity` 區段標記對應的重要內容，不要求翻譯逐字一致；新增或重組重要區段時，請在兩份文件保留相同的標記 ID：`model-fundamentals`、`high-risk-safety`、`interview-flow`、`report-format`。
- 使用 Python 標準函式庫執行 `python scripts/check_prompt_parity.py`，檢查必要區段是否在兩種語言中成對存在、標記唯一、內容非空，並比對兩語區段順序及巢狀關係，無需安裝額外套件。此檢查不判斷翻譯品質或語意是否完全等價，仍需人工校閱；請使用 [重要規則雙語對照](PROMPT_RULES.md) 逐項檢查。

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
