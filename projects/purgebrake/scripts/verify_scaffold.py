#!/usr/bin/env python3
"""Focused scaffold verifier for PurgeBrake."""
from __future__ import annotations

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
]
FORBIDDEN_MARKERS = [
    "github_pat_",
    "ghp_",
    "sk_live_",
    "BEGIN PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
]
PRIVATE_HINTS = [
    "@company.com",
    "tenant.onmicrosoft.com",
]


def main() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        assert path.exists(), f"missing {rel}"
        assert path.read_text().strip(), f"empty {rel}"

    readme = (ROOT / "README.md").read_text()
    spec = (ROOT / "SPEC.md").read_text()
    assert "PurgeBrake" in readme
    assert "Competitor / Substitute Check" in readme
    assert "example.test" in spec
    assert "not connect" in readme.lower() or "no live api calls" in spec.lower()

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.name == "verify_scaffold.py":
            continue
        text = path.read_text(errors="ignore")
        for marker in FORBIDDEN_MARKERS + PRIVATE_HINTS:
            assert marker not in text, f"forbidden marker {marker!r} in {path.relative_to(ROOT)}"

    print("scaffold verification passed")


if __name__ == "__main__":
    main()
