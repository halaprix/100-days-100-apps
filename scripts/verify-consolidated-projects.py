#!/usr/bin/env python3
"""Focused verifier for consolidated 100-days project snapshots.

This intentionally uses project-aware allowlists instead of the old top-level
plain grep scan. Several archived project repos contain their own secret-scan
patterns or synthetic network fixtures, which are not secrets.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "projects" / "MANIFEST.json"
INDEX = ROOT / "index.json"
README = ROOT / "README.md"
REMOVE_SCRIPT = ROOT / "scripts" / "remove-dedicated-github-repos.sh"

SECRET_MARKERS = [
    "github_pat_",
    "ghp_",
    "sk_live_",
    "whsec_",
    "BEGIN PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
]

# These files intentionally contain detector strings or synthetic examples.
ALLOW_MARKER_PATH_SUFFIXES = (
    "/scripts/verify_scaffold.py",
    "/.github/workflows/ci.yml",
    "/scripts/verify-consolidated-projects.py",
)

# Beads config files include commented examples such as `linear.api_key`; they
# are local tracker configuration templates, not credentials.
ALLOW_PATH_PARTS = {".git", ".beads"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path):
    return json.loads(path.read_text())


def main() -> None:
    index = load_json(INDEX)
    manifest = load_json(MANIFEST)
    projects = manifest["projects"]
    slugs = {project["slug"] for project in projects}

    assert len(projects) >= 32, f"expected at least 32 snapshots, got {len(projects)}"
    assert "disktrace" in slugs, "disktrace snapshot missing"

    remote_projects = [p for p in projects if p.get("source_remote")]
    script_text = REMOVE_SCRIPT.read_text()
    script_repos = re.findall(r"^  '([^']+)'", script_text, re.MULTILINE)
    assert len(script_repos) == len(remote_projects), (
        f"delete script targets {len(script_repos)} repos, manifest has "
        f"{len(remote_projects)} remote-backed projects"
    )
    assert "100-days-100-apps" not in script_repos, "delete script targets master repo"

    for project in projects:
        canonical = ROOT / project["canonical_path"]
        assert canonical.is_dir(), f"missing {project['canonical_path']}"
        assert not (canonical / ".git").exists(), f"nested .git copied for {project['slug']}"
        snapshot = load_json(canonical / ".snapshot.json")
        assert snapshot["source_commit"] == project["source_commit"], project["slug"]

    entries = index["entries"]
    assert any(e["day"] == 39 and e["repo"] == "projects/disktrace" for e in entries), (
        "DiskTrace index entry missing"
    )
    for entry in entries:
        repo = entry.get("repo")
        if isinstance(repo, str) and repo.startswith("projects/"):
            slug = repo.split("/", 1)[1]
            assert slug in slugs, f"index references missing snapshot: {repo}"

    readme = README.read_text()
    assert "[`projects/disktrace`](./projects/disktrace)" in readme
    assert "projects/PROJECTS.md" in readme

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.parts)
        if parts & ALLOW_PATH_PARTS:
            continue
        path_rel = "/" + rel(path)
        try:
            text = path.read_text(errors="ignore")
        except UnicodeDecodeError:
            continue
        if path_rel.endswith(ALLOW_MARKER_PATH_SUFFIXES):
            continue
        for marker in SECRET_MARKERS:
            assert marker not in text, f"marker {marker!r} found in {rel(path)}"

    print(
        "verified consolidated snapshots: "
        f"{len(projects)} projects, {len(remote_projects)} deletion targets, "
        "index/readme consistent, no nested .git, no disallowed secret markers"
    )


if __name__ == "__main__":
    main()
