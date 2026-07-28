# Contributing

Thanks for considering a contribution.

## Development principles

- Keep the tool local-first and safe for sensitive backup logs.
- Add fixture tests for every parser, log signature, and redaction rule.
- Do not require live Cloudflare credentials in CI.
- Keep live probes explicit and narrowly scoped.

## Workflow

1. Open or claim a Beads issue with `bd`.
2. Make a small, reviewable change.
3. Run tests and CI hygiene locally where possible.
4. Commit with a Conventional Commit message.

## Public safety

Do not include real credentials, bucket names, account IDs, hostnames, local paths, or raw backup logs in issues, tests, or documentation. Use sanitized fixtures.
