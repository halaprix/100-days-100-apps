"""Focused public-safe verifier for the DDMPath alpha scaffold."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "SPEC.md", "AGENTS.md", "CHANGELOG.md", "LICENSE",
    "CONTRIBUTING.md", "SECURITY.md", ".github/workflows/ci.yml",
    ".github/PULL_REQUEST_TEMPLATE.md", ".beads/issues.jsonl",
    "fixtures/sample-ddm-migration.json",
]
FORBIDDEN = ("ghp_", "github_pat_", "BEGIN PRIVATE KEY")

missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
if missing:
    raise SystemExit(f"missing required files: {', '.join(missing)}")

public_files = [ROOT / item for item in REQUIRED]
violations = []
for path in public_files:
    text = path.read_text(encoding="utf-8")
    for marker in FORBIDDEN:
        if marker in text:
            violations.append(f"{path.relative_to(ROOT)} contains forbidden marker")
if violations:
    raise SystemExit("; ".join(violations))

print("DDMPath scaffold verification passed")
