# Agent Instructions — PasskeyPilot

PasskeyPilot is a deterministic Microsoft Entra passkey rollout packet generator.

## Scope

- Keep v0 fixture-driven, read-only, and useful without Microsoft Graph credentials.
- Inputs are synthetic/public-safe YAML or CSV fixtures, not live tenant data.
- Generate recommendations, blockers, guardrails, pilot phases, helpdesk notes, and open questions.
- Treat Microsoft Learn and practitioner docs as references; do not claim a packet was executed against a tenant.

## Public safety

Do not commit:

- tokens, cookies, OAuth details, app registrations, tenant IDs, client IDs, secrets, certificates, or private keys;
- real domains, UPNs, group names, tenant names, device IDs, serial numbers, or support-ticket exports;
- screenshots or dumps from a real Microsoft tenant unless fully sanitized;
- private conversations or customer data.

Use synthetic domains such as `example.test` and fake group names such as `standard-users`.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests before changing classification or safety rules.
- Keep report output deterministic and easy to diff.

## Safety boundary

PasskeyPilot may generate human-reviewable rollout packets and policy notes. It must not connect to Microsoft Graph, read local credential stores, or change Entra policy in v0.
