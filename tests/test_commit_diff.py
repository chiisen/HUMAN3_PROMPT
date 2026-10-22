from pathlib import Path
import subprocess
import tempfile
import unittest

from test_setup_git_sync import PWSH, git


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_commit_diff.ps1"


class CommitDiffTests(unittest.TestCase):
    def check_commits(self, contents, base_index=None, base_override=None):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            git(repo, "init", "--quiet")
            revisions = []
            for index, content in enumerate(contents):
                (repo / f"file-{index}.txt").write_text(content, encoding="utf-8")
                git(repo, "add", ".")
                git(repo, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                    "commit", "--quiet", "-m", "fixture")
                revisions.append(git(repo, "rev-parse", "HEAD"))
            args = [PWSH, "-NoProfile", "-File", str(SCRIPT)]
            if base_override is not None:
                args += ["-BaseRevision", base_override]
            elif base_index is not None:
                args += ["-BaseRevision", revisions[base_index]]
            return subprocess.run(args, cwd=repo, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace")

    def test_clean_initial_tree_passes(self):
        result = self.check_commits(["clean\n"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_range_detects_whitespace_from_non_tip_commit(self):
        result = self.check_commits(["base\n", "trailing space \n", "clean tip\n"], base_index=0)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("trailing whitespace", result.stdout)

    def test_new_branch_zero_base_checks_entire_tree(self):
        result = self.check_commits(["trailing space \n", "clean tip\n"], base_override="0" * 40)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("trailing whitespace", result.stdout)

    def test_missing_base_fails_instead_of_silently_passing(self):
        result = self.check_commits(["clean\n"], base_override="missing-revision")
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
