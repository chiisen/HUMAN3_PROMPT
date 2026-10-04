from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PromptSafetyPolicyTests(unittest.TestCase):
    def test_english_prompt_uses_level_independent_safety_boundary(self):
        prompt = (ROOT / "PROMPT.md").read_text(encoding="utf-8")

        self.assertIn("High-Risk Actions: Safety Boundary", prompt)
        self.assertIn("A HUMAN 3.0 level is not a safety clearance", prompt)
        self.assertIn("qualified healthcare professional", prompt)
        self.assertIn("major financial, employment, or legal decisions", prompt)
        self.assertNotIn("Level 2.5-3.0 + Glitch = Calculated Risk", prompt)
        self.assertNotIn("If Level 2.5+: Can discuss conscious risk-taking", prompt)
        self.assertNotIn("Most should avoid Glitches entirely until Level 2.5+", prompt)

    def test_traditional_chinese_prompt_uses_level_independent_safety_boundary(self):
        prompt = (ROOT / "PROMPT_TW.md").read_text(encoding="utf-8")

        self.assertIn("高風險行為安全界線", prompt)
        self.assertIn("HUMAN 3.0 分級不能判定高風險行為是否安全或適合個人", prompt)
        self.assertIn("合格的醫療專業人員", prompt)
        self.assertIn("重大財務、工作或法律決策", prompt)
        self.assertNotIn("Level 2.5-3.0 + Glitch =", prompt)
        self.assertNotIn("如果 Level 2.5+：可討論有意識的風險承擔", prompt)
        self.assertNotIn("大多數人在 Level 2.5 以前應避免 Glitches", prompt)

    def test_readme_does_not_present_level_2_5_as_glitch_eligibility(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertNotIn("須 Level 2.5+", readme)
        self.assertIn("不能判定高風險行為是否適合個人", readme)


if __name__ == "__main__":
    unittest.main()
