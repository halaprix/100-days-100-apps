#!/usr/bin/env python3
"""Focused scaffold checks for WeatherFork."""

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
    "examples/ecowitt-sample.json",
    "examples/weatherfork.yml",
]

REQUIRED_README_PHRASES = [
    "Ecowitt",
    "Home Assistant",
    "Competitor / Substitute Check",
    "WeeWX",
    "ecowitt2mqtt",
    "Status",
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

    sample = json.loads((ROOT / "examples/ecowitt-sample.json").read_text(encoding="utf-8"))
    for key in ["station_id", "observed_at", "tempf", "humidity"]:
        if key not in sample:
            fail(f"sample fixture missing key: {key}")

    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    if "python3 scripts/verify_scaffold.py" not in ci:
        fail("CI workflow does not run scaffold verifier")

    print("verify_scaffold: ok")


if __name__ == "__main__":
    main()
