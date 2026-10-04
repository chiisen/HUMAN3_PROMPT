from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class EvidenceGroundingTests(unittest.TestCase):
    def test_english_prompt_requires_traceable_interpretations(self):
        prompt = (ROOT / "PROMPT.md").read_text(encoding="utf-8")
        requirements = (
            "Evidence from the user's answers",
            "Interpretation (hypothesis)",
            "Confidence",
            "Alternative explanations",
            "Do not fabricate quotes",
            "not enough information to assess",
        )

        for requirement in requirements:
            with self.subTest(requirement=requirement):
                self.assertTrue(requirement in prompt, f"Missing evidence rule: {requirement}")

    def test_traditional_chinese_prompt_requires_traceable_interpretations(self):
        prompt = (ROOT / "PROMPT_TW.md").read_text(encoding="utf-8")
        requirements = (
            "使用者實際回答",
            "解讀（假設）",
            "信心程度",
            "替代解釋",
            "不得捏造引文",
            "資訊不足，無法判斷",
        )

        for requirement in requirements:
            with self.subTest(requirement=requirement):
                self.assertTrue(requirement in prompt, f"Missing evidence rule: {requirement}")

    def test_each_quadrant_output_calls_for_evidence_and_uncertainty(self):
        english = (ROOT / "PROMPT.md").read_text(encoding="utf-8")
        chinese = (ROOT / "PROMPT_TW.md").read_text(encoding="utf-8")

        self.assertTrue("Repeat for Body, Spirit, and Vocation" in english)
        self.assertTrue("身體、靈性與職業象限也重複上述證據與不確定性欄位。" in chinese)

    def test_both_prompts_require_summary_confirmation_before_full_report(self):
        english = (ROOT / "PROMPT.md").read_text(encoding="utf-8")
        chinese = (ROOT / "PROMPT_TW.md").read_text(encoding="utf-8")

        self.assertIn("Do not generate the full report until the user confirms", english)
        self.assertIn("先只提供簡短摘要", chinese)
        self.assertIn("不得產生完整報告", chinese)
        self.assertIn("explicitly asks to continue", english)


if __name__ == "__main__":
    unittest.main()
