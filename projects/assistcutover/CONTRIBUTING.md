# Contributing

## Development principles

- Keep scans deterministic and offline.
- Add a fixture and a golden report for every detection rule.
- Prefer a documented false-positive control to a speculative automatic rewrite.
- Do not add credentials, customer code, or copied private reports to the repo.

## Before opening a change

1. Track the task in Beads.
2. Run the relevant tests and `python3 scripts/verify_scaffold.py`.
3. Use a Conventional Commit message.
