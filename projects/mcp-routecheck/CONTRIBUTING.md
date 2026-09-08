# Contributing

Thank you for improving McpRouteCheck.

## Before opening a change

1. Create or claim a Beads task for the work.
2. Keep the read-only, explicit-input, no-secret boundary intact.
3. Add synthetic fixtures for every new supported configuration shape.
4. Run `python3 scripts/verify_scaffold.py` and the relevant tests.

## Pull requests

Explain the configuration shape added, the conservative behavior for ambiguous
input, test coverage, and how the change avoids emitting credential material.
Do not attach real configuration files or logs.
