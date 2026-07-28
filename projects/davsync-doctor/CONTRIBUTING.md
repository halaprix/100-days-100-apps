# Contributing

Thanks for helping improve DavSync Doctor.

## Development principles

- Reproduce DAV failures with synthetic fixtures or local test servers.
- Do not paste real contacts, passwords, Authorization headers, or private server URLs into issues or tests.
- Keep diagnostics explainable: every check should say what it proves and what it cannot prove.
- Prefer small pull requests with tests.

## Commit style

Use Conventional Commits, for example:

```text
feat: add well-known carddav check
fix: redact usernames in markdown reports
```

## Reporting issues

A good issue includes:

- Server type and version if public-safe.
- Client type, e.g. iOS native Contacts or macOS Contacts.
- DavSync Doctor redacted report.
- What you expected and what happened.

Never include secrets or private contact data.
