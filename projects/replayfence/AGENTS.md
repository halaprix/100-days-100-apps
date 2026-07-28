# Agent Instructions — ReplayFence

## Mission

Build a local-first webhook retry/idempotency preflight CLI for small teams receiving third-party webhooks.

## Product boundaries

- Public-safe only: never commit secrets, private webhook payloads, customer data, cookies, tokens, account IDs, or real signing secrets.
- Use reserved domains such as `example.com` or localhost examples only.
- Do not build a hosted webhook relay/gateway in the MVP.
- Do not require live provider credentials for tests or demos.
- Treat provider fixtures as synthetic examples unless explicitly documented as public samples.

## Task tracking

Use Beads only in this repo.

```bash
bd ready
bd create "Short task title" -t task -p 1 -d "Context and acceptance criteria"
bd update <id> --claim
bd close <id> --reason "Done in <commit>"
```

Do not use markdown task lists, Kanban, TodoWrite, or ad-hoc issue lists.

## Git workflow

- Conventional Commits only.
- One logical change per commit.
- Reference bead IDs in commit bodies.
- Never add LLM co-author trailers.

## Verification

Before claiming completion, run the relevant tests plus:

```bash
git status --short
bd list --json >/tmp/replayfence-beads.json
```
