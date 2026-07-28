# Contributing

Thanks for considering a contribution.

## Development rules

- Use synthetic data only.
- Do not commit real tickets, logs, secrets, screenshots, or customer examples.
- Keep detector changes covered by tests once code exists.
- Use Conventional Commits.

## Local validation

For now, run the scaffold checks locally:

```bash
test -f README.md
test -f SPEC.md
test -f AGENTS.md
test -f CHANGELOG.md
test -f LICENSE
test -f CONTRIBUTING.md
test -f SECURITY.md
test -f .github/PULL_REQUEST_TEMPLATE.md
grep -q "TicketScrub" README.md
grep -q "User story" SPEC.md
```

This workflow is scaffold-only and will be replaced when the implementation lands.
