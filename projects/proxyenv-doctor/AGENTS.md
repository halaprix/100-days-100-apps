# Agent Instructions — ProxyEnv Doctor

## Mission

ProxyEnv Doctor is a small public CLI for diagnosing proxy-environment drift in self-hosted CI and Docker workflows.

## Rules

- Keep the project public-safe: no tokens, proxy credentials, private hostnames, private IPs, or local machine details in committed files.
- Use fixture data for examples and tests.
- Redact any proxy URL credentials before printing or storing diagnostic output.
- Beads is the only task tracker. Use `bd ready`, `bd update <id> --claim`, and `bd close <id>`.
- Conventional Commits only. Do not add LLM co-author trailers.
- Prefer a tiny standard-library CLI before adding dependencies.

## Verification

Before claiming completion, run:

```bash
bd list --json >/tmp/proxyenv-doctor-beads.json
python3 scripts/verify_scaffold.py
git status --short --branch
git log --oneline --decorate -5
```
