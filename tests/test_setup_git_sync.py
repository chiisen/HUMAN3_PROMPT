from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "setup_git_sync.ps1"
PWSH = shutil.which("pwsh") or r"C:\Program Files\PowerShell\7\pwsh.exe"
FETCH_URL = "https://example.invalid/owner/HUMAN3_PROMPT.git"
OTHER_FETCH_URL = "https://example.invalid/other/repo.git"
OTHER_PUSH_URL = "git@example.invalid:other/repo.git"
EXPECTED_PUSH_URLS = [
    "git@github.com:edwin45168899/HUMAN3_PROMPT.git",
    "git@github.com-chiisen:chiisen/HUMAN3_PROMPT.git",
    "git@github.com-edwiin1688:edwiin1688/HUMAN3_PROMPT.git",
    "git@github.com-NathanEvans1221:NathanEvans1221/HUMAN3_PROMPT.git",
    "git@gitlab.com-chiisen:chiisen/HUMAN3_PROMPT.git",
]


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


class GitSyncSetupTests(unittest.TestCase):
    def assert_script_is_idempotent(self, seed_duplicate_urls: bool):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            git(repo, "init", "--quiet")
            git(repo, "remote", "add", "origin", FETCH_URL)
            git(repo, "remote", "add", "other", OTHER_FETCH_URL)
            git(repo, "config", "--add", "remote.other.pushurl", OTHER_PUSH_URL)

            if seed_duplicate_urls:
                git(repo, "config", "--add", "remote.origin.pushurl", EXPECTED_PUSH_URLS[0])
                git(repo, "config", "--add", "remote.origin.pushurl", EXPECTED_PUSH_URLS[0])
                git(repo, "config", "--add", "remote.origin.pushurl", "git@example.invalid:stale.git")

            outputs = []
            for _ in range(2):
                result = subprocess.run(
                    [PWSH, "-NoProfile", "-File", str(SCRIPT)],
                    cwd=repo,
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                )
                outputs.append(result.stdout)

            self.assertEqual(git(repo, "config", "--get-all", "remote.origin.url"), FETCH_URL)
            self.assertEqual(
                git(repo, "config", "--get-all", "remote.origin.pushurl").splitlines(),
                EXPECTED_PUSH_URLS,
            )
            self.assertEqual(git(repo, "config", "--get-all", "remote.other.url"), OTHER_FETCH_URL)
            self.assertEqual(git(repo, "config", "--get-all", "remote.other.pushurl"), OTHER_PUSH_URL)
            self.assertTrue(all("Before" in output and "After" in output for output in outputs))
            self.assertTrue(all(EXPECTED_PUSH_URLS[-1] in output for output in outputs))

    def test_clean_origin_configuration_is_idempotent(self):
        self.assert_script_is_idempotent(seed_duplicate_urls=False)

    def test_duplicate_push_urls_are_replaced_with_expected_set(self):
        self.assert_script_is_idempotent(seed_duplicate_urls=True)


if __name__ == "__main__":
    unittest.main()
