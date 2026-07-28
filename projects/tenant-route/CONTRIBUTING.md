# Contributing

Contributions are welcome once the MVP direction is validated.

## Ground rules

- Keep examples synthetic or public. Do not submit real tenant IDs, customer names, domains, support cases, or billing exports.
- Add source links for any rule that references Microsoft, CSP, or migration behavior.
- Keep output language conservative: decision support, not legal/tax/compliance advice.
- Use conventional commits.

## Local workflow

```bash
bd ready
bd update <id> --claim
# make changes
# run validation
bd close <id> --reason "Done in <commit>"
```
