# Agent Instructions — TenantRoute

TenantRoute is a public, local-first Microsoft 365 tenant-country/CSP-region decision-packet tool.

## Rules

- Keep the project public-safe: no secrets, tokens, tenant IDs, customer names, private domains, private hostnames, screenshots, or support-ticket dumps.
- Do not claim legal, tax, compliance, or Microsoft support authority. Output is decision support, not advice.
- Prefer local files and sample scenarios over credentialed APIs for v0.
- Evidence must link to public Microsoft docs, public product pages, or public community posts.
- Use Beads (`bd`) for task tracking. Do not create markdown task lists.
- Use conventional commits.

## Product boundary

In scope:

- Questionnaire-driven decision packets.
- YAML rules with source links.
- Markdown/CSV exports.
- Sample scenarios.

Out of scope for v0:

- Tenant/data migration execution.
- Graph/Partner Center credentialed access.
- Storing customer tenant data in a hosted service.

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
