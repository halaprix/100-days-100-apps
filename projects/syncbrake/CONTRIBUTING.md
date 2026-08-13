# Contributing

SyncBrake is an incubator project. Keep contributions small, deterministic, and public-safe.

## Local workflow

1. Create or claim a Beads issue.
2. Make one logical change.
3. Add or update fixture/golden coverage when behavior changes.
4. Run the verifier before committing.
5. Commit with a Conventional Commit message and a bead reference.

## Public-safety requirements

Do not add real identity exports, tenant names, domains, UPNs, hostnames, private paths, screenshots, support-case IDs, tokens, API keys, or `.env` data. Use synthetic fixtures only.
