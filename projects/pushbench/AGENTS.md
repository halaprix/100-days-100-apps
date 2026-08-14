# Agent Instructions — PushBench

PushBench is a local-first benchmark and readiness-packet generator for self-hosted UnifiedPush backends.

## Rules

- Keep examples public-safe: no real device tokens, user identifiers, domains, hostnames, IP addresses, notification payloads, `.env` contents, API keys, or private infrastructure details.
- Do not load-test public ntfy, Mozilla, UnifiedPush, or third-party push infrastructure in the MVP.
- Do not store real push subscriptions, device identifiers, or message payloads.
- Prefer deterministic markdown/JSON output over dashboards or SaaS integrations.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice parses synthetic local fixtures and emits a deterministic push readiness packet. It must not target public/default push servers.
