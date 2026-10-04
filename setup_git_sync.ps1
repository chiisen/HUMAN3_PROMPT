# Configure the push destinations managed for this repository's origin remote.
# Run from inside a Git checkout with an existing origin. Only the local
# remote.origin.pushurl entries are replaced; fetch URLs and other remotes stay unchanged.

$ErrorActionPreference = "Stop"

$RepoName = "HUMAN3_PROMPT"
$PushUrls = @(
    "git@github.com:edwin45168899/$RepoName.git"
    "git@github.com-chiisen:chiisen/$RepoName.git"
    "git@github.com-edwiin1688:edwiin1688/$RepoName.git"
    "git@github.com-NathanEvans1221:NathanEvans1221/$RepoName.git"
    "git@gitlab.com-chiisen:chiisen/$RepoName.git"
)

$repoRoot = git rev-parse --show-toplevel 2>$null
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoRoot)) {
    throw "Run this script from inside a Git repository."
}

$fetchUrls = @(git config --local --get-all remote.origin.url 2>$null)
if ($LASTEXITCODE -ne 0 -or $fetchUrls.Count -eq 0) {
    throw "The current repository has no origin remote; no configuration was changed."
}

Write-Output "Repository: $repoRoot"
Write-Output "Before (all remotes):"
git remote -v
if ($LASTEXITCODE -ne 0) {
    throw "Could not read the current remote configuration."
}

$existingPushUrls = @(git config --local --get-all remote.origin.pushurl 2>$null)
if ($LASTEXITCODE -eq 0 -and $existingPushUrls.Count -gt 0) {
    git config --local --unset-all remote.origin.pushurl
    if ($LASTEXITCODE -ne 0) {
        throw "Could not clear the existing origin push URL list."
    }
}

foreach ($pushUrl in $PushUrls) {
    git config --local --add remote.origin.pushurl $pushUrl
    if ($LASTEXITCODE -ne 0) {
        throw "Could not add expected push URL: $pushUrl"
    }
}

$finalFetchUrls = @(git config --local --get-all remote.origin.url 2>$null)
if ($LASTEXITCODE -ne 0 -or ($finalFetchUrls -join "`n") -cne ($fetchUrls -join "`n")) {
    throw "The origin fetch URL changed unexpectedly."
}

Write-Output "After (all remotes):"
git remote -v
if ($LASTEXITCODE -ne 0) {
    throw "Could not display the final remote configuration."
}

Write-Output "Configured $($PushUrls.Count) origin push URLs; origin fetch URL and other remotes were preserved."
