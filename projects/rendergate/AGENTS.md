# Agent Instructions — RenderGate

RenderGate is a local-first access packet generator for temporary collaborator access to one render workstation or job API.

## Scope

- Keep v0 deterministic, fixture-driven, and read-only.
- Generate plans, warnings, snippets, acceptance tests, and rollback checklists.
- Prefer least-privilege defaults and explicit non-goals.
- Treat provider docs as references; do not pretend generated snippets were applied.

## Public safety

Do not commit:

- secrets, tokens, passwords, private keys, cookies, OAuth details, or service tokens;
- private IP addresses, domains, hostnames, usernames, email addresses, or device names;
- real tailnet, tunnel, firewall, SSH, IdP, or collaborator configuration;
- screenshots or logs from a real network.

Use synthetic labels such as `render-box`, `external-editor`, and `job-api`.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests before changing access rules.
- Keep outputs deterministic and easy to diff.

## Safety boundary

RenderGate may generate human-reviewable policy snippets and test checklists. It must not apply live Tailscale, Cloudflare, SSH, firewall, IdP, or reverse-proxy changes in v0.
