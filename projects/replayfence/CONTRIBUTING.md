# Contributing

ReplayFence is currently in scaffold/spec stage.

## Development rules

- Keep fixtures synthetic or fully public.
- Do not commit real webhook payloads, signing secrets, account IDs, customer data, cookies, tokens, or private endpoint URLs.
- Prefer deterministic local tests over live provider calls.
- Use Conventional Commits.
- Track work with Beads only.

## Local validation

Run the project-specific test command once code exists. Until then, validate docs and repository state with:

```bash
git status --short
bd list --json >/tmp/replayfence-beads.json
```
