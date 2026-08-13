#!/usr/bin/env python3
"""Ad-hoc scaffold verifier for the SyncBrake snapshot."""
from __future__ import annotations

import csv
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
    "fixtures/pending-export.csv",
    "fixtures/readiness.yml",
    "tests/golden/sample-packet.md",
]
FORBIDDEN = [
    "BEGIN PRIVATE KEY",
    "AWS_SECRET_ACCESS_KEY",
    "GITHUB_TOKEN=",
    "DATABASE_URL=",
    "ghp_",
    "sk_live_",
    "@contoso.com",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    rows = list(csv.DictReader((ROOT / "fixtures/pending-export.csv").open()))
    assert rows, "fixture has no pending-export rows"
    assert any(row["object_modification_type"] == "delete" for row in rows)
    assert any("admin" in row["display_name"].lower() for row in rows)

    snapshot = json.loads((ROOT / ".snapshot.json").read_text())
    assert snapshot["slug"] == "syncbrake"
    assert snapshot["canonical_path"] == "projects/syncbrake"

    for rel in REQUIRED + [".snapshot.json"]:
        text = (ROOT / rel).read_text(errors="ignore")
        for marker in FORBIDDEN:
            if marker in text:
                raise SystemExit(f"forbidden marker {marker!r} in {rel}")

    readme = (ROOT / "README.md").read_text()
    assert "Entra Connect" in readme
    assert "go/no-go packet" in readme
    assert "Evidence" in readme

    print("SyncBrake scaffold verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
