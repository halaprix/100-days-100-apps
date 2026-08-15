# Agent Instructions — DrivePing

DrivePing is an Android head-unit connectivity sentinel and local drop-log exporter.

## Rules

- Keep examples public-safe: no real route traces, SSIDs, BSSIDs, phone numbers, precise locations, IP addresses, hostnames, device identifiers, or user traffic captures.
- Do not request background location, contacts, SMS, microphone, camera, VPN, packet-capture, or accessibility permissions in the MVP.
- Prefer local-only logs and deterministic exports over dashboards or cloud sync.
- Treat Android foreground-service, boot, and overlay restrictions as product constraints, not bugs to bypass.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice proves foreground notification state and local export from synthetic/fake probe results. It must not collect location or inspect user traffic.
