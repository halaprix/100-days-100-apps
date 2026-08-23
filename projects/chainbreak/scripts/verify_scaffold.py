#!/usr/bin/env python3
"""Focused public-safe scaffold verifier for ChainBreak."""

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
    ".beads/issues.jsonl",
]

missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
if missing:
    raise SystemExit(f"missing required scaffold files: {', '.join(missing)}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
for marker in ("## Problem", "## Target user", "## MVP", "## Evidence"):
    if marker not in readme:
        raise SystemExit(f"README missing section: {marker}")
for marker in ("## User story", "## Feature list", "## Data model", "## Build plan", "## Validation plan"):
    if marker not in spec:
        raise SystemExit(f"SPEC missing section: {marker}")

forbidden = ("github" + "_pat_", "g" + "hp_", "BEGIN " + "PRIVATE KEY", "/" + "home/")
public_files = [ROOT / "README.md", ROOT / "SPEC.md", ROOT / "AGENTS.md"]
for path in public_files:
    text = path.read_text(encoding="utf-8")
    if any(marker in text for marker in forbidden):
        raise SystemExit(f"public-safety marker found in {path.name}")

print("ChainBreak scaffold verification passed")
