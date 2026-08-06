# Contributing

RelayTrace is currently in scaffold/spec mode.

## Development workflow

1. Pick or create a Beads issue with `bd`.
2. Keep fixtures synthetic and public-safe.
3. Make one logical change per commit.
4. Run the verifier before committing:

```bash
python3 scripts/verify_scaffold.py
```

## Commit style

Use Conventional Commits, for example:

```text
feat: add offline header parser
fix: classify missing recipient headers
chore: refresh scaffold verifier
```

Do not add co-author trailers for agent-generated work.
