#!/usr/bin/env python3
"""Focused scaffold verifier for QueryGap."""

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
    ".beads/issues.jsonl",
]

PUBLIC_SAFETY_MARKERS = [
    "GITHUB_TOKEN=",
    "x-access-token:",
    "ghp_",
    "github_pat_",
    "sk_live_",
    "whsec_",
    "/home/pkl/",
]


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    for needle in ["QueryGap", "AdGuard Home", "Competitor / Substitute Check", "MVP"]:
        if needle not in readme:
            raise SystemExit(f"README missing {needle!r}")

    for needle in ["User story", "Core flow", "Data model", "Validation plan"]:
        if needle not in spec:
            raise SystemExit(f"SPEC missing {needle!r}")

    if "Beads is the only task tracker" not in agents:
        raise SystemExit("AGENTS.md missing Beads rule")

    scanned = []
    for path in REQUIRED:
        p = ROOT / path
        if p.is_file() and p.suffix in {".md", ".yml", ".yaml", ".jsonl", ""}:
            scanned.append(p)

    for path in scanned:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in PUBLIC_SAFETY_MARKERS:
            if marker in text:
                raise SystemExit(f"public-safety marker {marker!r} found in {path}")

    print("scaffold verification passed")


if __name__ == "__main__":
    main()
