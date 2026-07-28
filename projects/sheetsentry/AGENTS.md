# Agent Instructions — SheetSentry

SheetSentry is a public, local-first CLI project incubated from `halaprix/100-days-100-apps`.

## Rules

- Keep the MVP read-only and public-safe: no OAuth, cookies, API keys, service-account JSON, or private sheet credentials.
- Use Beads (`bd`) for all task tracking. Do not use markdown TODOs, Kanban, or ad-hoc issue lists.
- Conventional Commits only.
- Do not add LLM co-author trailers.
- Prefer deterministic checks and fixtures over network-dependent tests.

## Verification

Before claiming work is complete, run the relevant tests plus:

```bash
bd list --json >/tmp/sheetsentry-beads.json
git status --short
git log --oneline --decorate -5
```
