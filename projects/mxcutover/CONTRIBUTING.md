# Contributing

MxCutover is early-stage. Keep contributions small, public-safe, and testable.

## Workflow

1. Create or claim a Beads issue with `bd`.
2. Make one logical change.
3. Run validation.
4. Commit with Conventional Commits.
5. Open a PR with evidence and test output.

## Commit style

Use Conventional Commits:

```text
feat: add packet schema
fix: correct dmarc finding severity
docs: expand proofpoint checklist notes
```

Do not add LLM co-author trailers.

## Public-safety rules

Do not commit real tenant names, customer domains, email headers, OAuth tokens,
API keys, DNS screenshots, private portal exports, or vendor support tickets.
Use synthetic fixtures only.
