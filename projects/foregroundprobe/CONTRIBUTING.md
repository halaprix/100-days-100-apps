# Contributing

## Scope

Keep contributions within the local, deterministic Android foreground-service preflight boundary. Do not add device control, cloud accounts, telemetry, credentials, or real customer/device data.

## Workflow

1. Create or claim a Beads issue with `bd`.
2. Add or update a synthetic fixture and its expected packet.
3. Run `python3 scripts/verify_scaffold.py` and future project tests.
4. Use a Conventional Commit and reference the issue.

## Public safety

Never commit tokens, app secrets, real Logcat exports, private paths, device IDs, internal package names, or OEM support conversations.
