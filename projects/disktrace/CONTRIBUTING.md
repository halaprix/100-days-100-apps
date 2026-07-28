# Contributing

Thanks for considering a contribution.

## Development rules

- Keep the tool read-only and fixture-driven until the spec explicitly changes that boundary.
- Use synthetic fixtures for examples and tests.
- Do not include real server names, domains, usernames, file shares, trace logs, hostnames, IP addresses, credentials, or customer data.
- Prefer small pull requests with one focused change.
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `ci:`, or `chore:`.

## Local checks

Until the runnable CLI exists, validate scaffold changes with:

```bash
bd list --json >/tmp/disktrace-beads.json
python3 -m compileall . >/tmp/disktrace-compile.log 2>&1 || true
```

Future code changes should add and run a real test command.
