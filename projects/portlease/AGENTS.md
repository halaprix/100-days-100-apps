# Agent Instructions — PortLease

PortLease is a public, local-first UPnP/NAT-PMP exposure reporting tool for self-hosters.

## Rules

- Keep the project public-safe: no secrets, private IP screenshots, router dumps, home hostnames, MAC addresses from real networks, or personal infrastructure details.
- Do not claim PortLease proves compromise or replaces a security assessment. Output is diagnostic support.
- v0 is read-only. Do not add router-changing behavior without a dedicated spec update and explicit task.
- Prefer synthetic fixtures and local protocol tests over credentialed router integrations.
- Evidence must link to public docs, public product pages, or public community posts.
- Use Beads (`bd`) for task tracking. Do not create markdown task lists.
- Use conventional commits.

## Product boundary

In scope:

- UPnP IGD / NAT-PMP / PCP mapping discovery.
- Risk classification for common exposed services.
- Local host enrichment from safe LAN signals.
- Markdown/JSON reports.
- Synthetic fixtures and demos.

Out of scope for v0:

- Automatic router configuration changes.
- Credentialed router admin scraping.
- Internet-wide scanning.
- Cloud accounts or telemetry.

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

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
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
