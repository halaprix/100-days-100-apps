# Contributing

Thanks for considering a contribution.

## Development rules

- Keep the tool read-only unless a future milestone explicitly changes that scope.
- Use synthetic fixtures for examples and tests.
- Do not include real backup paths, hostnames, usernames, passwords, logs, or customer data.
- Prefer small pull requests with one focused change.
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `ci:`, or `chore:`.

## Local checks

Until the runnable CLI exists, validate scaffold changes with:

```bash
python3 -m json.tool /dev/null >/dev/null 2>&1 || true
bd list --json >/tmp/backup-locksmith-beads.json
```

Future code changes should add and run a real test command.
