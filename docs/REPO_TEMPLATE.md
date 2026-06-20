# Dedicated Project Repo Template

Use this when a daily idea clears the repo-creation gate.

## Creation gate

Create a dedicated repo only when:

- the winning idea scores **18/25 or higher**, or
- Marian explicitly says to create/build it.

## Required files

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

## README skeleton

```markdown
# Product Name

One-line pitch.

## Problem

Who has the pain, what repeats, and why existing options are bad.

## Evidence

| Source | Link | Signal |
|---|---|---|

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor |  |  |
| Indirect substitute |  |  |
| Status quo |  |  |

## Wedge

Why this can still work despite existing options.

## Target user

## MVP

- Feature 1
- Feature 2
- Feature 3

## Non-goals

- Not doing X yet
- Not integrating Y yet

## Status

v0.1.0-alpha.0 — scaffold/spec only.
```

## SPEC skeleton

```markdown
# SPEC — Product Name

## User story

As a <user>, I want <capability>, so that <benefit>.

## Core flow

1. ...
2. ...
3. ...

## Data model

## Technical approach

## Validation plan

Include how we will validate the wedge against competitors/substitutes, not just whether the app runs.

## Milestones

- v0.1.0-alpha.0 — repo scaffold
- v0.1.0-alpha.1 — MVP skeleton
- v0.2.0-alpha.1 — usable demo
```

## Beads setup

```bash
bd init --prefix <short-prefix> --quiet
bd create "Implement MVP skeleton" -t task -p 1 -d "Create the first runnable slice."
bd create "Add validation and demo data" -t task -p 2 -d "Make the project demonstrable."
```

## First commit

```bash
git add .
git commit -m "chore: bootstrap repo structure

Initial scaffold for <repo>.

Refs: <bead-id>"
```

## Public-safety checklist

- [ ] No secrets
- [ ] No private paths
- [ ] No private IPs or hostnames
- [ ] No personal infrastructure details
- [ ] All evidence links are public
- [ ] Claims match fetched sources
