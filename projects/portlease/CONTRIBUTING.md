# Contributing

Contributions are welcome once the MVP direction is validated.

## Ground rules

- Keep examples synthetic or public. Do not submit real router dumps, private IP screenshots, home hostnames, MAC addresses, or personal infrastructure details.
- Add source links for protocol, router, or security claims.
- Keep output language conservative: diagnostic support, not proof of compromise or security advice.
- Use conventional commits.
- Use Beads for task tracking.

## Local workflow

```bash
bd ready
bd update <id> --claim
# make changes
# run validation
bd close <id> --reason "Done in <commit>"
```
