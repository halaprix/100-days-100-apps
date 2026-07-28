# Agent Instructions — LabFit

LabFit is a local-first homelab placement planner. It should help self-hosters decide where services belong before deployment; it is not a remote scanner or one-click deployer.

## Rules

- Keep the MVP local-first. Do not add telemetry, hosted dashboards, or account auth.
- Do not store credentials, hostnames, IPs, share paths, private URLs, or real inventory secrets.
- Treat reports as public by default: examples must be fictional and export must support redaction.
- Do not add automatic deployment in the MVP; placement advice and reports come first.
- Prefer fixture-based tests so CI does not need Proxmox, a NAS, privileged containers, or a private network.
- Use Beads (`bd`) for all task tracking. Do not use markdown TODOs or other trackers.
- Use conventional commits.

## Verification

Before claiming work is done, run the relevant tests plus:

```bash
git status --short
bd list --json >/tmp/labfit-beads.json
```

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
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
