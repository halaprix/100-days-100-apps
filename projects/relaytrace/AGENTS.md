# Agent Instructions — RelayTrace

RelayTrace is a local-first diagnostic CLI for SMTP forwarding and catch-all
envelope-recipient preservation.

## Rules

- Keep everything public-safe. Do not commit real email addresses, message
  bodies, domains, server names, credentials, private hostnames, or raw logs.
- Use only synthetic `.test` domains and fixture messages in examples/tests.
- Do not add live SMTP authentication or network sending unless a future spec
  explicitly scopes it.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first usable slice is offline: parse a plan plus saved RFC822 fixtures and
emit a deterministic markdown/json verdict packet. Keep the implementation small
and auditable.
