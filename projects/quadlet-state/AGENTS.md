# Agent Instructions — QuadletState

QuadletState is a local-first desired-state generator and diff planner for Podman Quadlet files.

## Rules

- Keep examples public-safe: no real server names, private paths, hostnames, IP addresses, `.env` contents, API keys, or personal infrastructure details.
- Do not build a full orchestrator in the first slice; generation and diff planning come before apply/run behavior.
- Do not read or print `.env` contents. Reference env files only by safe placeholder paths or labels.
- Prefer deterministic text output over clever UI.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice parses `examples/quadlet-state.yml`, emits deterministic Quadlet files into a generated directory, and prints a create/update/unchanged plan. It must not run `systemctl`, modify live unit directories, or inspect host-specific state.
