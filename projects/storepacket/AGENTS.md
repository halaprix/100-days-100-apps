# Agent Instructions — StorePacket

StorePacket is a public, local-first CLI project. Keep contributions small, testable, and public-safe.

## Scope

Build a no-credentials release packet generator for App Store submission prep. The project may reference Apple documentation and third-party tooling, but it must not automate authenticated App Store Connect actions in the MVP.

## Rules

- Use Beads (`bd`) for task tracking.
- Use Conventional Commits.
- Do not commit secrets, API keys, credentials, private screenshots, private app metadata, or personal infrastructure details.
- Prefer deterministic fixtures and snapshot tests over network-dependent tests.
- Keep claims narrow: StorePacket helps prepare a submission packet; it does not guarantee App Review approval.

## Validation

Before claiming work is complete, run the available tests or validation scripts and include the real output in the handoff.
