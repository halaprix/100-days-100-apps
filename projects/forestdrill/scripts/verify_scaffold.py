#!/usr/bin/env python3
"""Focused scaffold verifier for ForestDrill."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "SPEC.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".beads/issues.jsonl",
    "examples/small-org-ad-backup.yaml",
]
FORBIDDEN_PATTERNS = [
    re.compile("GITHUB" + r"_TOKEN"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk_live_[A-Za-z0-9_]+"),
    re.compile(r"whsec_[A-Za-z0-9_]+"),
    re.compile(r"\b(?:10|172\.(?:1[6-9]|2\d|3[0-1])|192\.168)\.\d{1,3}\.\d{1,3}\b"),
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        print(f"missing required files: {missing}", file=sys.stderr)
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    example = (ROOT / "examples/small-org-ad-backup.yaml").read_text(encoding="utf-8")

    required_phrases = [
        "Active Directory backup and recovery-drill packet",
        "Competitor / Substitute Check",
        "fixture-driven and read-only",
        "not connecting to Active Directory",
    ]
    for phrase in required_phrases:
        if phrase not in readme:
            print(f"README missing phrase: {phrase}", file=sys.stderr)
            return 1

    if "forestdrill plan --answers" not in spec:
        print("SPEC missing core CLI flow", file=sys.stderr)
        return 1
    if "Do not commit:" not in agents:
        print("AGENTS missing public-safety section", file=sys.stderr)
        return 1
    if "example.test" not in agents:
        print("AGENTS should require synthetic example domains", file=sys.stderr)
        return 1
    if "backup_manager_joined_to_ad: true" not in example:
        print("example fixture should exercise the AD-joined backup-manager risk", file=sys.stderr)
        return 1

    scan_paths = [ROOT / path for path in REQUIRED]
    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in scan_paths
        if path.is_file()
    )
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(combined):
            print(f"forbidden public-safety marker matched: {pattern.pattern}", file=sys.stderr)
            return 1

    print("ForestDrill scaffold verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
