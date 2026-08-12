# Contributing

EolBridge is currently a scaffold/spec project in the 100-days lab.

## Development rules

- Use Conventional Commits.
- Keep fixtures synthetic and public-safe.
- Add tests for deterministic output and redaction behavior before expanding parsing scope.
- Do not add live Drupal, database, hosting, or admin-panel integrations without updating `SPEC.md` and the privacy/security model.

## Local validation

```bash
python3 scripts/verify_scaffold.py
```
