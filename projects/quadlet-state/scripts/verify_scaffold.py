#!/usr/bin/env python3
"""Focused scaffold checks for QuadletState."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
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
    "examples/quadlet-state.yml",
    ".snapshot.json",
]

REQUIRED_README_PHRASES = [
    "Podman Quadlet",
    "Competitor / Substitute Check",
    "Podlet",
    "quadlet-nix",
    "Status",
]

FORBIDDEN_MARKERS = [
    "GITHUB_TOKEN=",
    "ghp_",
    "sk_live_",
    "whsec_",
    "BEGIN PRIVATE KEY",
]


def fail(message: str) -> None:
    print(f"verify_scaffold: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            fail(f"missing required file: {relative}")
        if path.is_file() and path.stat().st_size == 0:
            fail(f"empty required file: {relative}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in REQUIRED_README_PHRASES:
        if phrase not in readme:
            fail(f"README.md missing phrase: {phrase}")

    fixture = (ROOT / "examples/quadlet-state.yml").read_text(encoding="utf-8")
    for phrase in ["version: 1", "rootless: true", "containers:", "jellyfin", "gatus"]:
        if phrase not in fixture:
            fail(f"fixture missing phrase: {phrase}")

    snapshot = json.loads((ROOT / ".snapshot.json").read_text(encoding="utf-8"))
    if snapshot.get("slug") != "quadlet-state":
        fail("snapshot slug mismatch")
    if snapshot.get("canonical_path") != "projects/quadlet-state":
        fail("snapshot canonical path mismatch")

    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    if "python3 scripts/verify_scaffold.py" not in ci:
        fail("CI workflow does not run scaffold verifier")

    for relative in ["README.md", "SPEC.md", "AGENTS.md", "examples/quadlet-state.yml"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                fail(f"public-safety marker in {relative}: {marker}")

    print("verify_scaffold: ok")


if __name__ == "__main__":
    main()
