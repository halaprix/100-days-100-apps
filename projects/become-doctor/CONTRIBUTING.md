# Contributing

Thanks for helping with BecomeDoctor.

## Development principles

- Keep the tool local-first and safe by default.
- Do not add telemetry or hosted services.
- Do not store secrets or inventory credentials.
- Add fixtures for compatibility rules before adding remote probing behavior.
- Keep reports public-safe: redact hostnames, usernames, IPs, paths, inventory group names, and full command lines.

## Workflow

1. Pick or create a Beads issue with `bd`.
2. Make one logical change.
3. Run tests and `bd list --json >/tmp/become-doctor-beads.json`.
4. Commit using Conventional Commits.

## Commit format

```text
type(scope): short description

Optional body explaining why.

Refs: bdoc-xxxx
```
