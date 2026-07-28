# TenantRoute

Local-first Microsoft 365 tenant-country/CSP-region decision packets for admins who need to know whether they can avoid a tenant-to-tenant migration.

## Problem

Microsoft 365 tenant country and CSP regional rules can trap small IT teams after a company relocation, billing-entity change, or inherited tenant mistake. The admin has to decide whether local CSP licensing is possible, whether direct billing can continue, or whether a new tenant plus migration is unavoidable.

Existing migration vendors help once the organization is ready to migrate. TenantRoute focuses on the decision before that: gather tenant facts, flag likely country/CSP risks, and generate a packet the admin can take to Microsoft, a CSP, or a migration partner.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uv1z34/m_365_hk_tenant_to_uae_migration/ | Admin asks whether a Hong Kong-created Microsoft 365 tenant can buy UAE licenses/CSP billing after the company relocated. |
| Microsoft Learn — CSP global markets | https://learn.microsoft.com/en-us/partner-center/enroll/regional-authorization-overview | CSP regional restrictions depend on tenant country/region, not just physical company location. |
| Microsoft Learn — tenant-to-tenant migration planning | https://learn.microsoft.com/en-us/microsoft-365/migration/microsoft-365-tenant-to-tenant-migrations?view=o365-worldwide | Tenant-to-tenant migration requires architecture, identity, workload, and dependency planning. |
| Microsoft Q&A — tenant country | https://learn.microsoft.com/en-us/answers/questions/5324136/m365-tenant-country | Public answer says Microsoft 365 tenant country is set at creation and cannot be changed afterwards. |
| ShareGate migration-tool comparison | https://sharegate.com/blog/microsoft-365-tenant-to-tenant-migration-tools | The migration-execution market is crowded; the pre-migration decision packet is the narrow wedge. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft migration and Partner Center docs | Authoritative, but scattered and not packaged as a decision memo. |
| Direct competitor | BitTitan, Quest, AvePoint, ShareGate | Strong migration-execution products; not focused on avoid-or-scope country/CSP preflight. |
| Indirect substitute | CSP/MSP discovery call | Useful but can be slow, sales-biased, and hard to prepare for. |
| Indirect substitute | Admin spreadsheet assembled from docs and Reddit | Flexible but easy to miss dependencies and not repeatable. |
| Status quo | Ask Reddit, open tickets, call CSPs, wait | Wastes time and can delay or overbuy a migration decision. |

## Wedge

TenantRoute does not migrate data. It produces a local, no-credential decision packet for tenant-country, CSP-region, subscription-transfer, identity, domain, and workload risks before the organization talks to migration vendors.

## Target user

- Sole Microsoft 365 / Azure admin.
- Small IT team after relocation, new regional HQ, billing-entity change, or inherited wrong-country tenant.
- MSP/CSP consultant preparing a small customer for discovery.

## MVP

- Local questionnaire for tenant country, target country, billing/CSP state, subscriptions, domains, user count, identity model, and workloads.
- YAML rules for country/CSP mismatch and migration-pressure flags.
- Markdown outputs:
  - executive decision memo,
  - CSP/Microsoft support question list,
  - migration scoping packet,
  - action register.
- Sample HK→UAE scenario for demos.

## Non-goals

- No mailbox, SharePoint, Teams, OneDrive, or Entra migration execution.
- No credentialed Graph or Partner Center access in v0.
- No legal, tax, or compliance advice.
- No replacement for Microsoft support, CSPs, or migration partners.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
