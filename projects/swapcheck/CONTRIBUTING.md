# Contributing

## Development rules

- Keep the default command path local and network-free.
- Add fixtures rather than real policy exports or production repositories.
- Never commit credentials, prompts, completions, policy exports, or private
  infrastructure details.
- Add or update tests for behavior changes.
- Use Conventional Commits and reference the relevant Bead.

## Before opening a pull request

```bash
python3 scripts/verify_scaffold.py
git diff --check
```

Describe the user-visible behavior, privacy impact, and validation performed.
