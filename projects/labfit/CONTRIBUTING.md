# Contributing

Thanks for helping with LabFit.

## Development principles

- Keep the tool local-first and safe by default.
- Do not add telemetry, hosted services, or account auth.
- Do not store secrets or real homelab inventory details.
- Add fixtures for placement rules before adding broader catalog behavior.
- Keep reports public-safe: redact hostnames, usernames, IPs, paths, share names, and private URLs.

## Workflow

1. Pick or create a Beads issue with `bd`.
2. Make one logical change.
3. Run tests and `bd list --json >/tmp/labfit-beads.json`.
4. Commit using Conventional Commits.

## Commit format

```text
type(scope): short description

Optional body explaining why.

Refs: lfit-xxxx
```
