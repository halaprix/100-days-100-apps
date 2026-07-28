# Contributing

ReportChain is early-stage. Keep changes small, reviewed, and public-safe.

## Commit style

Use Conventional Commits:

```text
feat: add csv report tree parser
fix: handle manager cycles in preview
chore: update scaffold metadata
```

## Development rules

- Do not add live tenant data to tests or fixtures.
- Do not require Microsoft 365 credentials for the default test suite.
- Keep tenant-writing operations out of the default path.
- Add tests for any traversal, filtering, or command-packet behavior.

## Pull requests

Include:

- Summary of the change.
- Verification commands and output.
- Public-safety note if the change touches auth, Graph, or PowerShell command generation.
