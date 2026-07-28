# Agent Instructions — Llama CUDA Doctor

This is a public app repo generated from `halaprix/100-days-100-apps`.

## Mission

Build a read-only CLI diagnostic for NVIDIA/CUDA/llama.cpp environment mismatches. Prefer simple, inspectable checks over magic installers.

## Safety

- Do not commit secrets, private hostnames, private paths, full environment dumps, or machine IDs.
- Diagnostic fixtures must be synthetic or explicitly sanitized.
- The CLI must not install drivers, edit shell profiles, run privileged commands, or mutate system state in v0.1.
- Reports should redact home-directory usernames by default.

## Workflow

- Use `bd` for all task tracking.
- Use Conventional Commits.
- One logical change per commit.
- Keep local-first if GitHub push is blocked; do not retry permission failures in a loop.

## Verification

Before claiming completion, run the relevant tests plus:

```bash
bd list --json >/tmp/llama-cuda-doctor-beads.json
git status --short
git log --oneline --decorate -5
```
