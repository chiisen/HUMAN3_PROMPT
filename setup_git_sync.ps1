# setup_git_sync.ps1
# 依據 docs/git同步備份branch.md 建立的同步腳本

$RepoName = "HUMAN3_PROMPT"

$BackupUrl = "git@github.com:edwin45168899/$RepoName.git"
$MainUrl = "git@github.com-chiisen:chiisen/$RepoName.git"
$MainUrl1 = "git@github.com-edwiin1688:edwiin1688/$RepoName.git"
$MainUrl2 = "git@github.com-NathanEvans1221:NathanEvans1221/$RepoName.git"
$MainUrl3 = "git@gitlab.com-chiisen:chiisen/$RepoName.git"

Write-Output "正在設定 Git 遠端同步 (Repo: $RepoName)..."
Write-Output "備份遠端: $BackupUrl"
Write-Output "主要遠端: $MainUrl"
Write-Output "主要遠端1: $MainUrl1"
Write-Output "主要遠端2: $MainUrl2"
Write-Output "主要遠端3: $MainUrl3"

# 1. 加入 backup repo 到 origin 的 push list
git remote set-url --add --push origin $BackupUrl

# 2. 加入主要 repo 到 origin 的 push list
git remote set-url --add --push origin $MainUrl
git remote set-url --add --push origin $MainUrl1
git remote set-url --add --push origin $MainUrl2
git remote set-url --add --push origin $MainUrl3

Write-Output "設定完成。目前的 remote 設定如下："
git remote -v
