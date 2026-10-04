from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REPORTS = (ROOT / "docs" / "RESULTS.md", ROOT / "docs" / "RESULTS_EASY.md")
SYNTHETIC_CASE = (
    "案例設定：一位虛構的未具名工作者表示，工作優先順序經常變動讓他感到耗能，"
    "作息大致固定，近期運動偏少，且社群支持有限；他希望重新找回可控感。"
)


class ExampleReportPrivacyTests(unittest.TestCase):
    def test_both_reports_disclose_the_synthetic_nonclinical_status(self):
        for report_path in REPORTS:
            with self.subTest(report=report_path.name):
                report = report_path.read_text(encoding="utf-8")
                for marker in (
                    "合成示例",
                    "並非真實受訪者或真實訪談紀錄",
                    "不是經驗驗證的測驗或心理診斷",
                    "不代表評估準確性",
                ):
                    self.assertTrue(marker in report, f"{marker!r} missing from {report_path.name}")

    def test_both_reports_use_the_same_fictional_case(self):
        for report_path in REPORTS:
            with self.subTest(report=report_path.name):
                report = report_path.read_text(encoding="utf-8")
                self.assertTrue(SYNTHETIC_CASE in report, f"synthetic case missing from {report_path.name}")

    def test_old_personal_profile_and_level_based_glitch_advice_are_removed(self):
        for report_path in REPORTS:
            with self.subTest(report=report_path.name):
                report = report_path.read_text(encoding="utf-8")
                for marker in (
                    "The Dissonant Architect",
                    "Flask/React",
                    "Level 2.5+",
                    "AI 依賴 (AI Dependency)",
                ):
                    self.assertFalse(marker in report, f"{marker!r} remains in {report_path.name}")


if __name__ == "__main__":
    unittest.main()
