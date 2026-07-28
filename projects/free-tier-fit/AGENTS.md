# Agent Instructions — FreeTierFit

FreeTierFit is a public, local-first CLI project incubated from `halaprix/100-days-100-apps`.

## Rules

- Keep the MVP read-only and public-safe: no cloud credentials, SSH access, tokens, cookies, provider API keys, or private host details.
- Use Beads (`bd`) for all task tracking. Do not use markdown task lists, Kanban, or ad-hoc issue lists.
- Conventional Commits only.
- Do not add LLM co-author trailers.
- Prefer deterministic fixtures and local Compose files over live-network tests.
- Unknown app requirements must be reported as unknown; do not invent resource numbers.

## Verification

Before claiming work is complete, run the relevant tests plus:

```bash
bd list --json >/tmp/free-tier-fit-beads.json
git status --short
git log --oneline --decorate -5
```
