# Contributing

## Scope

Contributions must preserve EnrollFence's local, read-only boundary. Do not add
tenant authentication, policy writes, device actions, or real customer exports.

## Development checks

Before opening a change:

```bash
python3 scripts/verify_scaffold.py
git diff --check
```

Use Conventional Commits and create a Beads issue before substantive work.

## Fixtures and documentation

Use only synthetic, public-safe fixture values. Cite public Microsoft
documentation for enrollment-path and policy-behavior claims, including a source
date when behavior may change.
