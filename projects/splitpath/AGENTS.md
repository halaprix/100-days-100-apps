# Agent Instructions — SplitPath

SplitPath is a public, read-only diagnostic CLI for split-DNS and private reverse-proxy setups.

## Rules

- Public-safe only: never commit secrets, tokens, cookies, private hostnames, private IP inventories, or user config dumps.
- Beads is the only task tracker. Use `bd` for all work.
- MVP checks must be read-only. Do not mutate DNS, firewall, router, Cloudflare, Tailscale, NetBird, Caddy, or Nginx Proxy Manager config.
- Prefer small deterministic fixtures before real network probing.
- Conventional Commits only. No LLM co-author trailers.

## Initial product scope

Build a CLI that diagnoses whether a hostname fails because of public DNS, split DNS, overlay resolver routing, reverse-proxy reachability, or TLS/SNI mismatch.
