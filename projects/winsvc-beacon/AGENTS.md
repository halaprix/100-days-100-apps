# Agent Instructions — WinSvcBeacon

WinSvcBeacon is a public, lightweight Windows Service monitoring bridge for Uptime Kuma.

## Rules

- Keep the project public-safe: no real push URLs, credentials, hostnames, IPs, customer names, or private screenshots.
- Use Beads (`bd`) for all task tracking. Do not use markdown task lists, Kanban, or ad-hoc issue lists.
- Prefer small, auditable CLI slices over clever automation.
- Keep write-like operations explicit. Dry-run and packet generation should work before any install/register command exists.
- Treat Uptime Kuma push URLs as secrets. Examples must use placeholders or environment variable names only.
- Conventional Commits only. Do not add LLM co-author trailers.

## Validation

Before claiming completion, run the relevant focused checks and at minimum:

```bash
bd list --json >/tmp/winsvc-beacon-beads.json
git status --short --branch
```
