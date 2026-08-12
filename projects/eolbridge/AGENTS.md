# Agent Instructions — EolBridge

EolBridge is a local-first packet generator for Drupal 10 EOL upgrade planning.

## Rules

- Keep examples public-safe: no real domains, client names, private paths, hostnames, IP addresses, `.env` contents, API keys, database DSNs, or personal infrastructure details.
- Do not connect to production Drupal sites, databases, admin panels, or hosting APIs in the first slice.
- Do not build automated code fixes; Drupal Rector owns that lane.
- Prefer deterministic markdown/HTML output over clever UI.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice parses sanitized Composer/profile fixtures and emits a deterministic EOL decision packet. It must not inspect live systems or make network calls.
