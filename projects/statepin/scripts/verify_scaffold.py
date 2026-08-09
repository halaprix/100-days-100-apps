#!/usr/bin/env python3
"""Verify the StatePin scaffold invariants."""

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
    "examples/statepin.yml",
]
PUBLIC_SAFE_FILES = [
    "README.md",
    "SPEC.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "examples/statepin.yml",
]
FORBIDDEN_MARKERS = [
    "PRIVATE KEY",
    "BEGIN RSA",
    "password=",
    "webhook.site",
    "discord.com/api/webhooks",
    "192.168.",
    "10.0.",
    "172.16.",
]


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    rows = [
        json.loads(line)
        for line in (ROOT / ".beads/issues.jsonl").read_text().splitlines()
        if line.strip()
    ]
    if len(rows) < 2:
        raise SystemExit("expected at least two scaffold beads")

    for rel in PUBLIC_SAFE_FILES:
        text = (ROOT / rel).read_text(errors="replace")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                raise SystemExit(f"public-safety marker {marker!r} found in {rel}")

    plan = (ROOT / "examples/statepin.yml").read_text()
    required_terms = ["Homelab current state", "backups", "max_age", "PT6H"]
    missing_terms = [term for term in required_terms if term not in plan]
    if missing_terms:
        raise SystemExit(f"example state file missing terms: {missing_terms}")

    print("StatePin scaffold verification passed")


if __name__ == "__main__":
    main()
