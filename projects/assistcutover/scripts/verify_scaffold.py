#!/usr/bin/env python3
"""Fail fast when the public project scaffold is incomplete."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "SPEC.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".beads/config.yaml",
    ".beads/issues.jsonl",
)

missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
if missing:
    raise SystemExit("missing scaffold files: " + ", ".join(missing))

for path in ("README.md", "SPEC.md"):
    if not (ROOT / path).read_text(encoding="utf-8").strip():
        raise SystemExit(f"empty required document: {path}")

print("scaffold verification passed")
