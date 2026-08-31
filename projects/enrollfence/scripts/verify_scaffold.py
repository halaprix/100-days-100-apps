#!/usr/bin/env python3
"""Verify the public EnrollFence research scaffold."""

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
    ".beads/issues.jsonl",
)


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing required scaffold files: {', '.join(missing)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for heading in ("## Problem", "## Target user", "## MVP", "## Non-goals", "## Evidence"):
        if heading not in readme:
            raise SystemExit(f"README is missing required heading: {heading}")

    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    for heading in ("## User story", "## Feature slices", "## Data model", "## Build plan", "## Validation plan"):
        if heading not in spec:
            raise SystemExit(f"SPEC is missing required heading: {heading}")

    print("enrollfence scaffold verification passed")


if __name__ == "__main__":
    main()
