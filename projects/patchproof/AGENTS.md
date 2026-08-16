# Agent Instructions — PatchProof

PatchProof is a local-first patch-compliance evidence packet builder for small-team sysadmins.

## Rules

- Keep examples public-safe: no real hostnames, IP addresses, user names, email addresses, ticket IDs, asset tags, vulnerability IDs tied to private systems, screenshots, or internal environment details.
- Do not add live platform credentials, API-token handling, endpoint control, patch deployment, remote remediation, or scanner control in the MVP.
- Prefer static fixture imports, deterministic classification, and reproducible Markdown/HTML exports over dashboards or cloud sync.
- Treat disagreements between patch tools, scanners, tickets, and endpoint last-seen data as first-class product states.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice ingests synthetic static exports, classifies sample assets, and renders a local evidence packet. It must not connect to real endpoint, RMM, scanner, ticketing, or identity systems.
