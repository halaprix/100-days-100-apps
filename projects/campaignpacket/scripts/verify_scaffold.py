#!/usr/bin/env python3
"""Focused scaffold verifier for CampaignPacket."""

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
    ".editorconfig",
    ".gitignore",
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


def require_contains(path: str, needles: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"{path} missing {needle!r}")


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    require_contains(
        "README.md",
        [
            "CampaignPacket",
            "Microsoft Teams SMS",
            "Competitor / Substitute Check",
            "MVP",
            "Non-goals",
        ],
    )
    require_contains("SPEC.md", ["User story", "Core flow", "Data model", "Validation plan"])
    require_contains("AGENTS.md", ["Beads is the only task tracker", "Do not automate Teams Admin Center"])

    scanned: list[Path] = []
    for path in REQUIRED:
        candidate = ROOT / path
        if candidate.is_file() and candidate.suffix in {".md", ".yml", ".yaml", ".jsonl", ""}:
            scanned.append(candidate)

    for path in scanned:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in PUBLIC_SAFETY_MARKERS:
            if marker in text:
                raise SystemExit(f"public-safety marker {marker!r} found in {path}")

    print("scaffold verification passed")


if __name__ == "__main__":
    main()
