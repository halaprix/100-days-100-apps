# Agent Instructions — DiskTrace

DiskTrace is a local-first planning tool for Windows Server disk-I/O incident collection.

## Scope

- Keep v0 read-only and fixture-driven.
- Prefer deterministic rules over opaque AI output.
- Use public documentation links and synthetic examples only.
- Do not collect, upload, or commit real production traces.

## Public safety

Do not commit:

- secrets, tokens, passwords, or credentials,
- private hostnames, private IPs, domains, usernames, or file shares,
- real ProcMon/WPR/PerfMon logs,
- customer or incident data,
- local machine paths beyond generic placeholders.

Examples must use synthetic names like `SERVER01`, `APP01`, and `C:\\Example\\...` only when needed.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests for every rule before changing behavior.
- Keep command output deterministic so support packets are easy to diff.

## Safety boundary

DiskTrace may generate command templates and warnings. It must not run live tracing, install drivers/tools, modify services, or change collector configuration unless a future milestone explicitly changes the scope and adds tests/safety prompts.
