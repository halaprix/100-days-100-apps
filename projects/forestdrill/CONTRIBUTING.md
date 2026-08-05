# Contributing

ForestDrill is currently at scaffold/spec stage.

## Ground rules

- Keep v0 read-only and fixture-driven.
- Do not add live Active Directory, Azure, backup-console, or credential-store access without a design review.
- Use synthetic fixtures only. Do not commit real domains, hostnames, IPs, usernames, tenant IDs, backup IDs, screenshots, or tickets.
- Use Conventional Commits.
- Track work with `bd` inside this repo.

## Local validation

```bash
python3 scripts/verify_scaffold.py
bd list --json >/tmp/forestdrill-beads.json
git status --short --branch
```

## First useful contribution

Implement `forestdrill plan --answers examples/small-org-ad-backup.yaml` and generate a deterministic markdown packet from the fixture.
