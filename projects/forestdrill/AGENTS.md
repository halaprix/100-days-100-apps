# Agent Instructions — ForestDrill

ForestDrill is a deterministic Active Directory backup recovery-drill packet generator.

## Scope

- Keep v0 fixture-driven, read-only, and useful without domain or backup-console credentials.
- Inputs are synthetic/public-safe YAML or CSV fixtures, not live AD, Azure, backup-console, or ticket data.
- Generate recommendations, blockers, drill steps, account-verification categories, vendor questions, and open risks.
- Treat Microsoft Learn and practitioner docs as references; do not claim a packet was executed against a real environment.

## Public safety

Do not commit:

- tokens, cookies, OAuth details, app registrations, tenant IDs, client IDs, secrets, certificates, or private keys;
- real domains, hostnames, IP addresses, DC names, backup job IDs, storage account names, usernames, SIDs, serials, or support-ticket exports;
- screenshots or dumps from a real AD, Azure, or backup-console environment unless fully sanitized;
- private conversations or customer data.

Use synthetic domains such as `example.test`, fake account labels such as `break-glass-admin`, and generic products such as `primary-backup-platform` in examples.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests before changing readiness classification or public-safety rules.
- Keep report output deterministic and easy to diff.

## Safety boundary

ForestDrill may generate human-reviewable recovery drill packets and policy notes. It must not connect to AD, Azure, backup consoles, credential stores, or change recovery configuration in v0.
