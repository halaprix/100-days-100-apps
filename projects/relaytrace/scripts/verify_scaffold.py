#!/usr/bin/env python3
"""Verify the RelayTrace scaffold invariants."""

from __future__ import annotations

import json
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
    "examples/catchall-relay.yaml",
]
PUBLIC_SAFE_FILES = [
    "README.md",
    "SPEC.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "examples/catchall-relay.yaml",
]
FORBIDDEN_MARKERS = [
    "PRIVATE KEY",
    "BEGIN RSA",
    "password=",
    "smtp://",
    "@gmail.com",
    "@outlook.com",
]


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    beads = ROOT / ".beads/issues.jsonl"
    rows = [json.loads(line) for line in beads.read_text().splitlines() if line.strip()]
    if len(rows) < 2:
        raise SystemExit("expected at least two scaffold beads")

    for rel in PUBLIC_SAFE_FILES:
        text = (ROOT / rel).read_text(errors="replace")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                raise SystemExit(f"public-safety marker {marker!r} found in {rel}")

    plan = (ROOT / "examples/catchall-relay.yaml").read_text()
    if "example.test" not in plan or "accepted_headers" not in plan:
        raise SystemExit("example plan must use synthetic .test domains and accepted headers")

    print("RelayTrace scaffold verification passed")


if __name__ == "__main__":
    main()
