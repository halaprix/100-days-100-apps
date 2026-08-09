# Agent Instructions — StatePin

StatePin is a tiny current-state board for self-hosters who want named status cards updated by scripts without operating a dashboard server.

## Rules

- Keep all examples public-safe: no real domains, webhook URLs, credentials, private hostnames, private IPs, or raw personal infrastructure logs.
- Use only synthetic card names and fixture timestamps in examples/tests.
- Do not build a broad monitoring platform; the wedge is latest-state cards from one-line updates.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice is local/static: read synthetic card state, compute stale/ok/warn/fail verdicts, and render HTML plus JSON. Hosted/serverless ingestion comes after the static contract is proven.
