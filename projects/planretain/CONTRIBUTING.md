# Contributing

## Development principles

- Keep all behavior local and read-only.
- Add fixtures rather than real Project Online exports.
- Treat unsupported schemas and missing evidence conservatively.
- Do not add network calls, tenant authentication, or automated migration.

## Before opening a change

1. Create or claim a Beads issue with `bd`.
2. Add focused tests for parser and report changes.
3. Check that reports do not include source values, paths, credentials, or IDs.
4. Use a Conventional Commit message.
