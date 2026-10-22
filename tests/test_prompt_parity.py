from pathlib import Path
import subprocess
import sys
import re
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_prompt_parity.py"
REQUIRED_SECTIONS = (
    "model-fundamentals",
    "high-risk-safety",
    "interview-flow",
    "report-format",
)


def render_prompt(text_by_section):
    parts = []
    for section in REQUIRED_SECTIONS:
        parts.extend(
            (
                f"<!-- prompt-parity:{section}:start -->",
                text_by_section[section],
                f"<!-- prompt-parity:{section}:end -->",
            )
        )
    return "\n".join(parts) + "\n"


class PromptParityTests(unittest.TestCase):
    def test_pair_rejects_different_section_order(self):
        sections = {section: "content" for section in REQUIRED_SECTIONS}
        english = render_prompt(sections)
        blocks = english.strip().split("\n")
        chinese = "\n".join(blocks[3:6] + blocks[:3] + blocks[6:])
        result = self.run_checker(english, chinese)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("structure", result.stdout)

    def test_pair_rejects_different_nesting(self):
        english = render_prompt({section: "content" for section in REQUIRED_SECTIONS})
        chinese = english.replace("<!-- prompt-parity:model-fundamentals:end -->\n", "")
        chinese = chinese.replace(
            "<!-- prompt-parity:high-risk-safety:end -->",
            "<!-- prompt-parity:high-risk-safety:end -->\n<!-- prompt-parity:model-fundamentals:end -->",
        )
        result = self.run_checker(english, chinese)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("structure", result.stdout)

    def test_evidence_policy_is_inside_interview_section_in_both_languages(self):
        """Static placement check, not a semantic translation assessment."""
        for filename, heading in (("PROMPT.md", "Evidence-Grounded Assessment Rules"),
                                  ("PROMPT_TW.md", "以回答依據進行判讀")):
            prompt = (ROOT / filename).read_text(encoding="utf-8")
            section = re.search(
                r"<!-- prompt-parity:interview-flow:start -->(.*?)<!-- prompt-parity:interview-flow:end -->",
                prompt, re.DOTALL,
            ).group(1)
            with self.subTest(filename=filename):
                self.assertTrue(heading in section, f"Evidence policy outside interview section: {filename}")

    def test_unknown_and_improperly_nested_markers_fail(self):
        english = render_prompt({section: "content" for section in REQUIRED_SECTIONS})
        cases = (
            english + "<!-- prompt-parity:unknown:start -->x<!-- prompt-parity:unknown:end -->",
            english.replace("<!-- prompt-parity:model-fundamentals:end -->", "").replace(
                "<!-- prompt-parity:high-risk-safety:end -->",
                "<!-- prompt-parity:model-fundamentals:end -->\n<!-- prompt-parity:high-risk-safety:end -->",
            ),
        )
        for chinese in cases:
            with self.subTest(chinese=chinese):
                self.assertNotEqual(self.run_checker(english, chinese).returncode, 0)

    def run_checker(self, english, traditional_chinese):
        with tempfile.TemporaryDirectory() as temp_dir:
            english_path = Path(temp_dir) / "PROMPT.md"
            chinese_path = Path(temp_dir) / "PROMPT_TW.md"
            english_path.write_text(english, encoding="utf-8")
            chinese_path.write_text(traditional_chinese, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(CHECKER), str(english_path), str(chinese_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

    def test_repository_prompts_have_required_sections(self):
        result = subprocess.run(
            [sys.executable, str(CHECKER)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_different_language_text_is_allowed_when_section_ids_match(self):
        english = render_prompt({section: f"English section: {section}" for section in REQUIRED_SECTIONS})
        chinese = render_prompt({section: f"繁體中文內容：{section}" for section in REQUIRED_SECTIONS})

        result = self.run_checker(english, chinese)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_section_marker_fails_with_section_name(self):
        sections = {section: f"內容：{section}" for section in REQUIRED_SECTIONS}
        chinese = render_prompt(sections).replace(
            "<!-- prompt-parity:high-risk-safety:end -->\n", ""
        )

        result = self.run_checker(render_prompt(sections), chinese)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("high-risk-safety", result.stdout + result.stderr)

    def test_duplicate_section_marker_fails(self):
        sections = {section: f"內容：{section}" for section in REQUIRED_SECTIONS}
        english = render_prompt(sections).replace(
            "<!-- prompt-parity:report-format:start -->",
            "<!-- prompt-parity:report-format:start -->\n<!-- prompt-parity:report-format:start -->",
        )

        result = self.run_checker(english, render_prompt(sections))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("report-format", result.stdout + result.stderr)

    def test_empty_section_fails(self):
        sections = {section: f"內容：{section}" for section in REQUIRED_SECTIONS}
        sections["high-risk-safety"] = ""

        result = self.run_checker(render_prompt(sections), render_prompt(sections))

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("high-risk-safety", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
