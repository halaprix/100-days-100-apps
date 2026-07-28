# Agent Instructions — TzDrift

TzDrift is a public, local-first timezone change readiness reporting CLI for sysadmins.

## Rules

- Keep the project public-safe: no secrets, private IPs, private hostnames, real customer inventories, screenshots, tenant names, or infrastructure dumps.
- Do not claim legal, employment, compliance, or legislative authority. Output is operational decision support, not advice.
- v0 is read-only. Do not add patching, SSH automation, or remote collection without a dedicated spec update and explicit task.
- Prefer synthetic fixtures and pasted sample outputs over credentialed integrations.
- Evidence must link to public docs, public product pages, public legislation/news pages, or public community posts.
- Use Beads (`bd`) for task tracking. Do not create markdown task lists.
- Use conventional commits.

## Product boundary

In scope:

- OS tzdata version discovery.
- Container/Dockerfile timezone package hints.
- Java/runtime timezone data hints.
- Cron/systemd timer local-time risk classification.
- Markdown/CSV readiness packets.
- Synthetic fixtures and demos.

Out of scope for v0:

- Automatic patching or package upgrades.
- Credential storage or SSH orchestration.
- Hosted monitoring, telemetry, or accounts.
- Predicting whether a bill becomes law.
- Legal/compliance advice.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown task lists
- Run `bd prime` for detailed command reference
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

Work is complete only when changes are committed locally and either pushed or the push blocker is explicitly recorded.

1. File beads for remaining work.
2. Run quality gates when code changed.
3. Close finished beads and export bead state.
4. Push when credentials permit.
5. If push is blocked, record the blocker and leave the local commit ready.
6. Verify git status and recent log before handoff.
<!-- END BEADS INTEGRATION -->
