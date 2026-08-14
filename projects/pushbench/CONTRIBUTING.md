# Contributing

PushBench is in scaffold/spec stage.

## Local workflow

1. Create or claim a Beads issue before changing behavior.
2. Keep tests fixture-only; do not hit public push servers.
3. Run `python3 scripts/verify_scaffold.py` before committing scaffold changes.
4. Use Conventional Commits and reference the bead in the commit body.

## Public-safety expectations

Use synthetic device IDs, sample payloads, and local fixture URLs only. Do not commit real push tokens, hostnames, domains, IP addresses, payloads, logs, or credentials.
