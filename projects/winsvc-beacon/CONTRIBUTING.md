# Contributing

This is an early incubator project. Contributions should stay narrow, safe, and easy to verify.

## Workflow

1. Open or claim a Beads issue with `bd`.
2. Make one logical change.
3. Run focused verification.
4. Commit with a Conventional Commit message.
5. Avoid committing secrets, real Uptime Kuma push URLs, hostnames, IPs, or private environment details.

## Commit style

Use Conventional Commits:

```text
feat: add fixture-backed service plan command
fix: redact push urls in packet output
docs: clarify powershell generation scope
```

Do not add LLM co-author trailers.
