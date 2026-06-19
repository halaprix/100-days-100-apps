# Agent Instructions — 100 Days, 100 Apps

> Audience: Hermes, Claude Code, Codex, Grok, or any other coding/research agent working in this repository for `halaprix`.

## 1. Mission

This repo is the **master index** for a 100-day build-in-public product lab.

Every day we:

1. Read public signals from Reddit, X/Twitter, and the web.
2. Extract repeated pain points and timely product opportunities.
3. Generate a shortlist of practical app ideas.
4. Score ideas with a consistent rubric.
5. Pick one winner.
6. Record the daily brief in this repo.
7. Create a dedicated project repo only when the winner clears the threshold or Marian explicitly says to build it.

The goal is **not** 100 empty GitHub repos. The goal is 100 researched product bets with enough evidence to decide what deserves real implementation.

## 2. Current operating mode

- Work **local-first** while GitHub write permissions are blocked or unavailable.
- Still keep the repository clean: update files, run validation, commit locally.
- Do not fake remote success. If push fails, record the blocker plainly and leave the local commit ready.
- Once write access is restored, push accumulated commits and tags.

## 3. Public-safety rules

This is a public build-in-public repo. Keep the public surface narrow.

Allowed:

- Public links to Reddit, X/Twitter, GitHub, docs, and product pages.
- Short summaries of public posts.
- Repo names under `halaprix/*`.
- Generic tooling notes.

Forbidden:

- Tokens, API keys, cookies, OAuth details, session dumps.
- Private IPs, hostnames, home-lab details, local filesystem paths, machine IDs.
- Private conversations or screenshots containing personal data.
- Paid API credentials or platform secrets.
- Claims based on inaccessible sources.

If a source cannot be fetched, say so. Do **not** invent evidence.

## 4. Beads is the only task tracker

Use `bd` for all work in this repo.

Never use:

- markdown TODO lists as task tracking,
- Hermes Kanban,
- TodoWrite / TaskCreate-style tools,
- ad-hoc issue lists in docs.

Required pattern:

```bash
bd ready
bd create "Short task title" -t task -p 1 -d "Context and acceptance criteria"
bd update <id> --claim
# work + validate + commit
bd close <id> --reason "Done in <commit>"
```

Priority mapping:

| Priority | Meaning |
|---|---|
| P0 | Blocks daily run or corrupts index/data |
| P1 | Needed for the next useful milestone |
| P2 | Useful but not blocking |
| P3 | Nice-to-have |

## 5. Daily run workflow

Each daily run must produce one `ideas/YYYY-MM-DD-short-name.md` file.

Daily brief structure:

```markdown
# Day NNN — Product Name

Date: YYYY-MM-DD
Status: idea-only | repo-created | rejected | blocked

## One-line pitch

## Evidence

| Source | Link | Signal |
|---|---|---|

## Problem

## Target user

## MVP scope

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | /5 | |
| Feasibility | /5 | |
| Demo potential | /5 | |
| Distribution | /5 | |
| Novelty/timing | /5 | |
| Total | /25 | |

## Decision

## Next build step
```

After writing the brief, update:

1. `README.md` index table,
2. `index.json`,
3. beads status.

## 6. Sources

Canonical source config lives in `sources.yml`.

Reddit:

- Read-only only.
- Use public JSON endpoints or web search fallback.
- Prefer posts/comments from the last 48 hours.
- Include permalinks for evidence.

X/Twitter:

- Use `xurl` only if already authenticated and the endpoint works.
- Search may be paid/credit-gated; if it fails, fall back to web search.
- Do not post, reply, like, repost, follow, DM, or bookmark unless Marian explicitly approves a specific action.

Web:

- Use search as fallback and for validation.
- Prefer original sources over AI-generated summaries.

## 7. Scoring and repo creation

Default threshold for creating a dedicated project repo: **18/25**.

Create a dedicated repo when either:

1. winner score is `>= 18`, or
2. Marian explicitly says to build/create it.

Do not create a repo for low-signal ideas just to satisfy a daily streak.

Repo naming:

- lowercase kebab-case,
- short and memorable,
- product-like when possible,
- no private/personal names,
- no trademarks unless clearly descriptive and safe.

## 8. Dedicated project repo scaffold

A project repo should start with:

```text
README.md
SPEC.md
AGENTS.md
CHANGELOG.md
LICENSE
CONTRIBUTING.md
SECURITY.md
.github/workflows/ci.yml
.github/PULL_REQUEST_TEMPLATE.md
.beads/
```

Minimum README:

- problem,
- target user,
- MVP,
- non-goals,
- source evidence links,
- current status.

Minimum SPEC:

- user story,
- feature list,
- data model if relevant,
- build plan,
- validation plan.

## 9. Git workflow

- Conventional Commits only.
- One logical change per commit.
- Reference beads in commit bodies when applicable.
- Push when remote write access is available.
- Never force-push `main`.
- Never add LLM co-author trailers.

Example:

```bash
git add AGENTS.md docs/REPO_TEMPLATE.md
git commit -m "docs: clarify local-first incubator workflow

Documents the daily idea pipeline, Beads-only tracking, and repo creation gate.

Refs: apps-apz"
```

## 10. Verification before completion

Before saying work is complete, run fresh checks:

```bash
python3 -m json.tool index.json >/tmp/100-days-index.json
bd list --json >/tmp/100-days-beads.json
git status --short
git log --oneline --decorate -5
```

If remote push is unavailable, say **local commit ready; remote push blocked**. Do not imply it shipped.

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

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until either `git push` succeeds or the current local-first blocker is explicitly recorded.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE when available**:
   ```bash
   git pull --rebase
   git push
   git status
   ```
5. **If push is blocked** - Record the blocker and keep the local commit ready
6. **Clean up** - Clear stashes, prune remote branches when safe
7. **Verify** - All changes committed locally, and pushed if credentials permit
8. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until it is committed locally and either pushed or explicitly blocked
- NEVER say "ready to push when you are" — push when credentials permit
- If push fails due permissions, stop retrying and report the exact blocker
<!-- END BEADS INTEGRATION -->
