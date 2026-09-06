# Contributing

## Before opening a change

1. Create or claim a Beads issue with `bd`.
2. Keep the change within ConfigReceipt's local-only product boundary.
3. Use synthetic configuration fixtures. Never add real exports, credentials,
   private addresses, hostnames, or topology details.
4. Add or update tests for behavioral changes.

## Commit and validation

Use Conventional Commits. Before submitting, run the project checks, `git diff
--check`, and a focused review for accidental sensitive fixture data.
