# Contributing

Thanks for helping improve BayTrace.

## Development principles

- Reproduce storage failures with synthetic fixtures whenever possible.
- Do not paste real disk serials, private hostnames, internal mount paths, or full raw logs into issues or tests.
- Keep diagnostics explainable: every check should say what it proves and what it cannot prove.
- Keep the MVP read-only by default.
- Prefer small pull requests with tests.

## Commit style

Use Conventional Commits, for example:

```text
feat: add lsblk scan parser
fix: redact disk serials in markdown reports
```

## Reporting issues

A good issue includes:

- OS and kernel version if public-safe.
- Storage controller model if public-safe.
- BayTrace redacted report.
- What you expected and what happened.

Never include secrets, private paths, real hostnames, or unredacted disk serial numbers.
