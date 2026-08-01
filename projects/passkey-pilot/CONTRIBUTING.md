# Contributing

PasskeyPilot is currently an incubator scaffold. Contributions should stay small, deterministic, and public-safe.

## Rules

- Use Conventional Commits.
- Track work with Beads.
- Do not add live Microsoft Graph access before the fixture-driven MVP works.
- Do not commit real tenant data, domains, UPNs, app registrations, tickets, screenshots, or credentials.
- Add tests before changing rule classifications or packet wording.

## Local verification

```bash
python3 scripts/verify_scaffold.py
```

Future implementation work should add a normal test command here.
