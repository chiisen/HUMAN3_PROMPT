param([string]$BaseRevision)

$ErrorActionPreference = "Stop"

# GitHub repositories use SHA-1. An initial push or manual run has no base;
# compare the whole current tree to Git's empty tree in that case.
if ([string]::IsNullOrWhiteSpace($BaseRevision) -or $BaseRevision -match '^0+$') {
    $BaseRevision = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
}

git diff --check $BaseRevision HEAD --
exit $LASTEXITCODE
