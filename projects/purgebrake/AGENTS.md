# Agent Instructions — PurgeBrake

PurgeBrake is a local-first preflight packet generator for risky email remediation searches.

## Scope

- Keep v0 deterministic, fixture-driven, and read-only.
- Generate blockers, warnings, approval packets, preview/export requirements, and rollback checklists.
- Treat vendor docs as references; do not pretend generated packets were executed.
- Prefer safety over automation. Destructive live actions are out of scope for v0.

## Public safety

Do not commit:

- secrets, tokens, passwords, private keys, cookies, OAuth details, or service tokens;
- real email addresses, mailbox names, tenant names, customer names, incident IDs, message IDs, or domains;
- screenshots or exports from a real mailbox, eDiscovery case, PhishRIP query, or security incident;
- private conversations or support tickets.

Use synthetic labels and reserved domains such as `example.test`.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests before changing safety rules.
- Keep outputs deterministic and easy to diff.

## Safety boundary

PurgeBrake may generate human-reviewable query summaries, packet checklists, and provider-specific risk notes. It must not connect to mailbox, tenant, eDiscovery, PhishRIP, Defender, Google Workspace, Proofpoint, Mimecast, SIEM, SOAR, or ticketing APIs in v0.

