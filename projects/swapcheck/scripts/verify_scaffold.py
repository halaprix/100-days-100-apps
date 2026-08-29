"""Focused verifier for the public SwapCheck scaffold."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "SPEC.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/workflows/ci.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".beads/config.yaml",
)


def main() -> None:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    if missing:
        raise SystemExit(f"missing required scaffold files: {', '.join(missing)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    for required_text, content, name in (
        ("local, read-only CLI", readme, "README.md"),
        ("## Validation plan", spec, "SPEC.md"),
        ("No GitHub API write access", readme, "README.md"),
        ("September 1, 2026", readme, "README.md"),
    ):
        if required_text not in content:
            raise SystemExit(f"{name} is missing {required_text!r}")

    print("SwapCheck scaffold verified")


if __name__ == "__main__":
    main()
