# Contributing

Contributions are welcome once the MVP direction is validated.

## Ground rules

- Keep examples synthetic or public. Do not submit real host inventories, private IPs, hostnames, customer names, tenant names, or infrastructure dumps.
- Add source links for timezone, platform, runtime, or legislative claims.
- Keep output language conservative: operational decision support, not legal or compliance advice.
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
