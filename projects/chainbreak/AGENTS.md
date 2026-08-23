# Agent Instructions — ChainBreak

ChainBreak is a local-first recovery-dependency preflight for remote maintenance windows.

## Rules

- Keep examples public-safe: no real site names, hosts, IP addresses, device serials, network diagrams, credentials, log dumps, or customer topology.
- The MVP reads only explicitly selected local fixtures and produces deterministic findings.
- Do not add network discovery, sockets, device control, VPN/firewall mutation, remote-console access, cloud accounts, telemetry, or credential handling.
- State limitations plainly: a declared graph is an operator assertion, not proof that a recovery path will function.
- Beads is the only task tracker. Use `bd` for work items.
- Use Conventional Commits. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice evaluates synthetic directed recovery dependencies and renders a review packet. It does not discover, connect to, modify, or monitor a real environment.
