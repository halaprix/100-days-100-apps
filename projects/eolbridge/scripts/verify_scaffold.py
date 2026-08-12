#!/usr/bin/env python3
"""Ad-hoc scaffold verifier for the EolBridge snapshot."""
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
    "fixtures/drupal10/composer.lock",
    "fixtures/drupal10/site.yml",
    "tests/golden/sample-packet.md",
]
FORBIDDEN = [
    "BEGIN PRIVATE KEY",
    "AWS_SECRET_ACCESS_KEY",
    "GITHUB_TOKEN=",
    "DATABASE_URL=",
    "ghp_",
    "sk_live_",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    lock = json.loads((ROOT / "fixtures/drupal10/composer.lock").read_text())
    packages = lock.get("packages", [])
    assert any(pkg.get("name") == "drupal/core-recommended" for pkg in packages)

    for rel in REQUIRED:
        text = (ROOT / rel).read_text(errors="ignore")
        for marker in FORBIDDEN:
            if marker in text:
                raise SystemExit(f"forbidden marker {marker!r} in {rel}")

    readme = (ROOT / "README.md").read_text()
    assert "Drupal 10" in readme
    assert "budget-ready" in readme
    assert "Competitor / Substitute Check" in readme

    print("EolBridge scaffold verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
