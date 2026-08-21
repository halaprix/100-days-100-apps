# Agent Instructions — DDMPath

DDMPath is a local-first Intune Apple update-policy migration packet builder.

## Rules

- Keep examples public-safe: no tenant names, user details, email addresses, device serials, hostnames, IP addresses, IDs, screenshots, or internal policy exports.
- Do not add Graph credentials, API-token handling, browser automation, live Intune connections, or policy mutation in the MVP.
- Prefer static fixture imports, deterministic findings, and reproducible Markdown/HTML output.
- State that an imported export can be incomplete; never claim tenant-wide correctness from partial evidence.
- Beads is the only task tracker. Use `bd` for all work.
- Use Conventional Commits. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice accepts synthetic static exports, classifies legacy/eligible/conflicting policy evidence, and renders a migration packet. It must not connect to or modify a real Intune tenant.
