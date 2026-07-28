# Contributing

HeaderPass is currently in scaffold/spec stage.

## Development rules

- Keep examples public-safe and redacted.
- Prefer fixture-based tests over live calls to private infrastructure.
- Do not commit real access headers, cookies, hostnames, account IDs, tunnel IDs, or tokens.
- Use Conventional Commits.
- Track work with Beads only.

## Local validation

Run the project-specific test command once code exists. Until then, validate docs and repository state with:

```bash
git status --short
bd list --json >/tmp/headerpass-beads.json
```
