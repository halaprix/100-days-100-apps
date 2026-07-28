# Agent Instructions — BackupLocksmith

BackupLocksmith is a public, local-first software project. Keep all work safe for a public repository.

## Scope

- Build a read-only recovery packet generator for self-hosted backup-console lockouts.
- Start with UrBackup lockout/reset readiness.
- Prefer fixture-driven, public-safe examples before touching real host detection.

## Safety rules

- Never commit secrets, passwords, tokens, private hostnames, private IPs, backup contents, or personal paths.
- Do not add commands that modify UrBackup configuration, databases, containers, or backup storage in v0.
- Any generated example must use synthetic domains, hostnames, paths, and user names.
- Default to reporting findings and references, not performing recovery.

## Task tracking

Use Beads only:

```bash
bd ready
bd update <id> --claim
bd close <id> --reason "Done in <commit>"
```

Do not use markdown TODO lists or other trackers.

## Git workflow

- Conventional Commits only.
- One logical change per commit.
- Run available tests or focused ad-hoc verification before claiming completion.
- Never force-push `main`.
