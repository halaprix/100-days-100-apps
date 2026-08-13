# Agent Instructions — SyncBrake

SyncBrake is a local-first packet generator for Microsoft Entra Connect pending-export and break-glass readiness review.

## Rules

- Keep examples public-safe: no real tenant names, domains, UPNs, hostnames, private paths, support-case IDs, screenshots, IP addresses, `.env` contents, API keys, or personal infrastructure details.
- Do not connect to Microsoft Graph, Microsoft 365 tenants, Entra Connect servers, domain controllers, admin centers, or production identity exports in the first slice.
- Do not automate remediation, threshold disabling, exports, deletes, or support escalation.
- Prefer deterministic markdown/HTML output over dashboards or SaaS integrations.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice parses synthetic or sanitized CSV/YAML fixtures and emits a deterministic preflight packet. It must not inspect live systems or make network calls.
