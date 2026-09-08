#!/usr/bin/env python3
"""Check that the public McpRouteCheck scaffold has its required files."""
from pathlib import Path

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
    ".beads/config.yaml",
]

missing = [relative for relative in REQUIRED if not (ROOT / relative).is_file()]
if missing:
    raise SystemExit("missing required scaffold files: " + ", ".join(missing))

for relative in ("README.md", "SPEC.md", "AGENTS.md"):
    if not (ROOT / relative).read_text(encoding="utf-8").strip():
        raise SystemExit(f"empty required document: {relative}")

print("scaffold verification passed")
