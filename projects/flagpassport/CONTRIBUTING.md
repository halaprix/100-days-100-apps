# Contributing

## Development principles

- Keep all analysis local and read-only.
- Use only synthetic fixtures. Do not add customer projects, tokens, cookies, or
  identifiable source snippets.
- Prefer a false `manual-review` finding to an unsafe false-negative claim.
- Keep the tool focused on the dated Forge client-SDK behavior change.

## Before opening a change

1. Create or claim a Beads issue.
2. Add or update focused tests for the classification you change.
3. Run the documented validation commands.
4. Use a Conventional Commit message and reference the Beads issue.
