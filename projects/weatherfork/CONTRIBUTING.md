# Contributing

WeatherFork is currently an incubator scaffold. Contributions should keep the MVP narrow and public-safe.

## Workflow

1. Use Beads for task tracking: `bd ready`, `bd show <id>`, `bd update <id> --claim`.
2. Make one logical change per branch/commit.
3. Run `python3 scripts/verify_scaffold.py` before committing scaffold changes.
4. Use Conventional Commits.
5. Do not commit real weather-station identifiers, coordinates, private hostnames, or credentials.

## Good first changes

- Add synthetic Ecowitt fixture coverage.
- Implement a dry-run parser for common Ecowitt upload fields.
- Render a static comparison report from fixture data.
