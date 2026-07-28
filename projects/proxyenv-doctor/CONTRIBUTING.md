# Contributing

Contributions are welcome once the MVP lands.

## Development principles

- Keep diagnostics read-only by default.
- Redact credentials and private network details in all output.
- Prefer deterministic fixtures over requiring access to a real proxy.
- Add tests for every new rule.

## Commits

Use Conventional Commits:

```text
feat: add fixture scan command
fix: redact proxy credentials in markdown output
```

Do not add co-author trailers for LLM agents.
