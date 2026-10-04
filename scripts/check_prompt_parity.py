"""Check that required paired sections exist in both prompt languages."""

from collections import Counter
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = {
    "model-fundamentals",
    "high-risk-safety",
    "interview-flow",
    "report-format",
}
MARKER = re.compile(r"<!-- prompt-parity:([a-z0-9-]+):(start|end) -->")


def validate_document(text, label):
    matches = list(MARKER.finditer(text))
    counts = Counter((match.group(1), match.group(2)) for match in matches)
    errors = []

    for section, _ in counts:
        if section not in REQUIRED_SECTIONS:
            errors.append(f"{label}: unexpected section marker '{section}'")

    for section in sorted(REQUIRED_SECTIONS):
        start_count = counts[(section, "start")]
        end_count = counts[(section, "end")]
        if start_count != 1:
            errors.append(f"{label}: section '{section}' needs exactly one start marker; found {start_count}")
        if end_count != 1:
            errors.append(f"{label}: section '{section}' needs exactly one end marker; found {end_count}")

    stack = []
    for match in matches:
        section, marker_type = match.groups()
        if section not in REQUIRED_SECTIONS:
            continue
        if marker_type == "start":
            stack.append((section, match.end()))
            continue

        if not stack or stack[-1][0] != section:
            errors.append(f"{label}: section '{section}' markers are out of order or improperly nested")
            continue

        _, content_start = stack.pop()
        if not text[content_start:match.start()].strip():
            errors.append(f"{label}: section '{section}' is empty")

    for section, _ in stack:
        errors.append(f"{label}: section '{section}' start marker has no matching end marker")

    return errors


def check_prompt_pair(english_text, chinese_text):
    return (
        validate_document(english_text, "PROMPT.md")
        + validate_document(chinese_text, "PROMPT_TW.md")
    )


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) not in (0, 2):
        print("Usage: python scripts/check_prompt_parity.py [PROMPT.md PROMPT_TW.md]")
        return 2

    english_path, chinese_path = (
        (Path(args[0]), Path(args[1]))
        if args
        else (ROOT / "PROMPT.md", ROOT / "PROMPT_TW.md")
    )

    try:
        english_text = english_path.read_text(encoding="utf-8")
        chinese_text = chinese_path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Unable to read prompt file: {error}")
        return 2

    errors = check_prompt_pair(english_text, chinese_text)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: required prompt sections are present, paired, and non-empty in both languages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
