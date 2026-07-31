# Contributing

## Commit style

Use Conventional Commits:

```text
type(scope): subject
```

Common types: `feat`, `fix`, `docs`, `chore`, `ci`, `refactor`, `test`.

## Safety rules

- Do not include real Proxmox node names, VM names, IP addresses, private hostnames, tokens, or SSH details.
- Use synthetic fixtures and reserved domains such as `example.test`.
- Keep v0 read-only; configuration-changing automation is out of scope.
