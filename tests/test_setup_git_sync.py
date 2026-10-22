from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "setup_git_sync.ps1"
PWSH = shutil.which("pwsh") or r"C:\Program Files\PowerShell\7\pwsh.exe"
FETCH_URL = "https://github.com/chiisen/HUMAN3_PROMPT.git"
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
    def assert_script_is_idempotent(self, seed_duplicate_urls: bool, fetch_url=FETCH_URL,
                                    from_subdirectory=False, extra_fetch_url=None):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            git(repo, "init", "--quiet")
            git(repo, "remote", "add", "origin", fetch_url)
            if extra_fetch_url:
                git(repo, "config", "--add", "remote.origin.url", extra_fetch_url)
            git(repo, "remote", "add", "other", OTHER_FETCH_URL)
            git(repo, "config", "--add", "remote.other.pushurl", OTHER_PUSH_URL)

            if seed_duplicate_urls:
                git(repo, "config", "--add", "remote.origin.pushurl", EXPECTED_PUSH_URLS[0])
                git(repo, "config", "--add", "remote.origin.pushurl", EXPECTED_PUSH_URLS[0])
                git(repo, "config", "--add", "remote.origin.pushurl", "git@example.invalid:stale.git")

            outputs = []
            working_dir = repo
            if from_subdirectory:
                working_dir = repo / "nested" / "docs"
                working_dir.mkdir(parents=True)
            for _ in range(2):
                result = subprocess.run(
                    [PWSH, "-NoProfile", "-File", str(SCRIPT)],
                    cwd=working_dir,
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                )
                outputs.append(result.stdout)

            expected_fetch_urls = [fetch_url] + ([extra_fetch_url] if extra_fetch_url else [])
            self.assertEqual(git(repo, "config", "--get-all", "remote.origin.url").splitlines(), expected_fetch_urls)
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

    def test_running_from_subdirectory_preserves_repository_configuration(self):
        self.assert_script_is_idempotent(False, from_subdirectory=True)

    def test_supported_https_scp_and_ssh_origin_formats(self):
        urls = (
            "https://github.com/edwin45168899/HUMAN3_PROMPT",
            "git@github.com-chiisen:chiisen/HUMAN3_PROMPT.git",
            "ssh://git@github.com-edwiin1688/edwiin1688/HUMAN3_PROMPT.git",
            "git@github.com-NathanEvans1221:NathanEvans1221/HUMAN3_PROMPT.git",
            "https://gitlab.com/chiisen/HUMAN3_PROMPT.git",
            "git@gitlab.com-chiisen:chiisen/HUMAN3_PROMPT.git",
        )
        for url in urls:
            with self.subTest(url=url):
                self.assert_script_is_idempotent(False, fetch_url=url)

    def test_multiple_allowed_fetch_urls_are_preserved(self):
        self.assert_script_is_idempotent(False, extra_fetch_url="git@github.com-chiisen:chiisen/HUMAN3_PROMPT.git")

    def assert_rejected_without_config_changes(self, fetch_urls, expected_error):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            git(repo, "init", "--quiet")
            for url in fetch_urls:
                git(repo, "config", "--add", "remote.origin.url", url)
            git(repo, "config", "--add", "remote.origin.pushurl", "git@example.invalid:keep.git")
            git(repo, "remote", "add", "other", OTHER_FETCH_URL)
            before = (repo / ".git" / "config").read_bytes()
            result = subprocess.run(
                [PWSH, "-NoProfile", "-File", str(SCRIPT)], cwd=repo,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            self.assertNotEqual(result.returncode, 0, "Wrong repository was accepted")
            self.assertIn(expected_error, result.stdout + result.stderr)
            self.assertEqual((repo / ".git" / "config").read_bytes(), before)

    def test_wrong_repository_is_rejected_before_any_write(self):
        urls = (
            "https://github.com/chiisen/another-project.git",
            "https://example.invalid/chiisen/HUMAN3_PROMPT.git",
            "https://github.com/outsider/HUMAN3_PROMPT.git",
            "https://github.com.evil.invalid/chiisen/HUMAN3_PROMPT.git",
            "git@github.com-chiisen:outsider/HUMAN3_PROMPT.git",
            "https://gitlab.com/outsider/HUMAN3_PROMPT.git",
            "C:/repos/HUMAN3_PROMPT.git",
        )
        for url in urls:
            with self.subTest(url=url):
                self.assert_rejected_without_config_changes([url], "Unexpected origin fetch URL")

    def test_one_unexpected_fetch_url_rejects_entire_operation(self):
        self.assert_rejected_without_config_changes(
            [FETCH_URL, "https://example.invalid/other.git"], "Unexpected origin fetch URL",
        )

    def test_missing_origin_fetch_url_preserves_config(self):
        self.assert_rejected_without_config_changes([], "no origin remote")

    def test_non_repository_is_rejected_without_creating_git_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = subprocess.run(
                [PWSH, "-NoProfile", "-File", str(SCRIPT)], cwd=temp_dir,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inside a Git repository", result.stdout + result.stderr)
            self.assertFalse((Path(temp_dir) / ".git").exists())


if __name__ == "__main__":
    unittest.main()
