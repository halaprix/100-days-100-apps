# Contributing

## Scope

Keep contributions within the deterministic, local recovery-dependency preflight boundary. Do not add network discovery, device control, cloud accounts, telemetry, credentials, or real network data.

## Workflow

1. Create or claim a Beads issue with `bd`.
2. Add or update a synthetic fixture and expected packet.
3. Run `python3 scripts/verify_scaffold.py` and future project tests.
4. Use a Conventional Commit and reference the issue.

## Public safety

Never commit credentials, real hostnames, IP addresses, VPN configuration, topology exports, site locations, remote-console screenshots, or customer incident material.
