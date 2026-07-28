# Agent Instructions — DavSync Doctor

DavSync Doctor is a public, local-first diagnostic tool for CardDAV/CalDAV sync failures.

## Rules

- Keep the project public-safe: never commit credentials, live server URLs, private contact data, logs with Authorization headers, or screenshots containing personal data.
- Prefer local fixture servers and synthetic vCards for tests.
- The MVP must remain diagnostic/read-mostly by default. Any write check must be explicit, isolated, and documented.
- Use conventional commits.
- Use `bd` for task tracking; do not use markdown task lists as a tracker.
- Keep reports redacted by default.

## Verification

Before claiming work is complete, run the relevant tests or focused checks and include the command output in the handoff.
