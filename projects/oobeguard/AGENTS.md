# Agent Instructions — OOBEGuard

## Mission

Build OOBEGuard as a public-safe, local-first CLI that checks redacted Windows imaging plans for documented setup-phase, OEM-key, and driver-staging traps.

## Product boundaries

Allowed:

- Deterministic rules over fictionalized YAML fixtures.
- Public links to Microsoft Learn, FOG, and product docs.
- Markdown reports that explain blockers and safer alternatives.

Forbidden:

- Collecting private fleet inventory, hostnames, serials, IP addresses, activation data, or production logs.
- Advising on licensing circumvention, activation bypass, or DRM/security bypass.
- Shipping scripts that modify production Windows images or registries before the diagnostic MVP is proven.

## Workflow

- Use Beads (`bd`) for task tracking only.
- Keep commits conventional.
- Prefer simple deterministic code over AI-dependent diagnosis.
- Every rule needs a public source link and a synthetic fixture.
- Run validation before claiming completion.

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
