# Day 025 — TenantRoute

Date: 2026-07-13
Status: repo-created

## One-line pitch

A local-first Microsoft 365 tenant-country/CSP-region decision packet generator for admins who need to know whether they can avoid a tenant-to-tenant migration.

## Source access note

Reddit public JSON was blocked by `HTTP 403 theme-beta`, so Reddit evidence came through the skill's public RSS fallback. Several subreddit RSS requests also returned `HTTP 429`, so I kept the usable RSS sample small. X/Twitter `whoami` worked, but search returned `401 Unauthorized`; no X search results were used.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uv1z34/m_365_hk_tenant_to_uae_migration/ | Fresh sysadmin post: company moved head office from Hong Kong to UAE and cannot tell whether local UAE Microsoft 365 licensing/CSP billing is possible without a tenant migration because the tenant country is locked at creation. |
| Microsoft Learn — CSP global markets | https://learn.microsoft.com/en-us/partner-center/enroll/regional-authorization-overview | Microsoft says CSP regional restrictions depend on the country/region set in the tenant, not necessarily the company's physical location; a customer can be out of sales territory for a local CSP. |
| Microsoft Learn — tenant-to-tenant migration planning | https://learn.microsoft.com/en-us/microsoft-365/migration/microsoft-365-tenant-to-tenant-migrations?view=o365-worldwide | Microsoft frames tenant-to-tenant migration as a planning-heavy project with architecture, identity, workload, dependency, downtime, and partner-tool decisions. |
| Microsoft Q&A — tenant country | https://learn.microsoft.com/en-us/answers/questions/5324136/m365-tenant-country | Public Microsoft answer: the tenant country is set during initial setup and cannot be changed afterwards; if it causes compliance/legal issues, the organization may need a new tenant and migration. |
| ShareGate migration-tool comparison | https://sharegate.com/blog/microsoft-365-tenant-to-tenant-migration-tools | Migration tooling is crowded for actual data moves, but those tools sell migration execution; the pre-migration billing/CSP/country decision remains a messy admin research step. |

## Shortlist and wedge-first gate

1. **TenantRoute** — Regional Microsoft 365 tenant/CSP decision packet.
   - Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now
   - Sole or small-team Microsoft 365 admin after company relocation → Microsoft docs, CSP calls, Reddit, migration vendors → docs are scattered and vendors optimize for selling migrations, not deciding whether migration is avoidable → read-only questionnaire/rules engine that outputs a decision memo, questions for CSPs, and migration-risk packet → search content for exact tenant-country/CSP lock queries plus r/sysadmin/r/Office365 reply strategy → fresh relocation/billing-country post and 2026 migration tooling churn.
   - Gate: **passes**.

2. **RackCheck** — Maintenance interlock for risky rack/disk/cable work.
   - Small infrastructure teams → NetBox/DCIM/runbooks → generic asset tools do not force a last-second two-identifier confirmation before physical action → QR/label printouts plus phone checklist that records “server, bay, port, change ticket” before pull/unplug → r/sysadmin incident writeups and homelab/IT ops content → fresh public mistake story described wrong disk and cable pulls causing downtime.
   - Gate: passes, but hardware-adjacent and less directly software-buying than TenantRoute.

3. **AuditMonth** — One-month endpoint-control remediation planner for tiny Google Workspace shops facing defense compliance audits.
   - 20–50 user org with no MDM → GRC suites, consultants, CIS spreadsheets → full GRC/MDM adoption is too slow for a one-month audit panic → offline prioritizer that turns current controls into week-by-week evidence tasks → compliance/security sysadmin content and search → fresh r/sysadmin audit post with local admin, no central directory, and one month until audit.
   - Gate: narrowed but overlaps with Day 010 NIS2 EvidencePack; avoid repeating the same compliance-evidence bet.

4. **VPSReceipt** — Tiny VPS hardening receipt generator.
   - Side-project VPS owners → generic hardening guides and shell scripts → advice is generic and users cannot show what they actually changed → read-only scanner emits a shareable hardening receipt and next actions → self-hosted/VPS content → fresh security-mistakes post.
   - Gate: rejected for this run; crowded security scanner/autofix adjacent and too close to generic hardening checklists.

5. **BlockSourceMap** — Index manifest linter for shadcn block registries.
   - shadcn registry owners and AI UI builders → Shoogle and manual search → end-user search already exists; registry maintainers still lack a standard discoverability manifest → CLI validates block metadata for search/MCP ingestion → shadcn registry maintainers via GitHub → fresh SideProject post says registries are fragmented and poorly indexed.
   - Gate: interesting but distribution is weaker and the visible product already attacks the user-facing search job.

## Problem

Changing the business country or billing entity behind a Microsoft 365 tenant is not a normal admin toggle. The tenant country can lock CSP eligibility, taxes, billing currency, services, and data-region assumptions. When a company relocates, a small IT team has to decide whether it can keep the existing tenant with a global or original-region CSP, transfer subscriptions, or create a new tenant and run a tenant-to-tenant migration.

The painful part is not only migration execution. It is the decision before the quote: collecting tenant facts, country/CSP constraints, subscription state, identity/domain risks, workload dependencies, questions to ask Microsoft/CSPs, and a stakeholder-friendly recommendation. Today that becomes scattered Microsoft docs, Reddit posts, vendor calls, and spreadsheets.

## Target user

- Sole or small-team Microsoft 365 / Azure admin.
- Company relocated, changed billing entity, opened a new regional HQ, or inherited a tenant created in the wrong country.
- Needs a decision packet before committing to a consultant, CSP, or migration vendor.

## MVP scope

- Guided local-first questionnaire: current tenant country, target billing country, current CSP/direct status, Microsoft Customer Agreement state, subscription list, user count, domains, workloads, identity model, compliance drivers, deadline.
- Rules-based risk classifier for:
  - likely CSP regional mismatch,
  - new-tenant/migration pressure,
  - subscription-transfer questions,
  - domain/identity blockers,
  - workload sequencing risks.
- Outputs:
  - one-page executive decision memo,
  - CSP/Microsoft support question list,
  - migration-vendor scoping packet,
  - CSV/Markdown action register.
- Optional import from manually exported Microsoft 365 admin/Partner Center CSVs. No credentials in v0.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft native migration docs and cross-tenant migration planning | Authoritative but broad; focuses on migration architecture, not a small admin’s billing-country/CSP avoid-or-migrate decision packet. |
| Direct competitor | BitTitan MigrationWiz, Quest On Demand Migration, AvePoint Fly, ShareGate Migrate | Strong for actual tenant/data migration projects. Their incentive and product surface starts after the admin is already leaning toward a migration. |
| Indirect substitute | CSP/MSP discovery call or paid consultant | Good when available, but slow, sales-biased, and hard for a small admin to prepare for without an internal fact pack. |
| Indirect substitute | Spreadsheet/checklist assembled from Microsoft Learn, Q&A, and Reddit | Flexible but easy to miss country/CSP, identity, domain, and workload dependencies. Not repeatable. |
| Status quo | Ask Reddit, open Microsoft support tickets, call CSPs, and wait | Can waste days or weeks and risks either overbuying a migration or delaying a required move until the deadline is worse. |

## Wedge

TenantRoute does **not** try to migrate mailboxes, Teams, SharePoint, or Entra ID. That keeps it out of the most crowded vendor battlefield. The wedge is the pre-migration decision packet for small admins stuck between country-locked tenants, local CSP billing, and scary migration quotes.

It can win attention with public, high-intent content around exact queries like “M365 tenant country cannot change”, “CSP sales territory tenant country”, and “move Microsoft 365 billing country”, then give admins a concrete packet they can take to Microsoft, a CSP, or migration vendor.

## Kill condition

Reject or narrow if Microsoft/CSP APIs and docs cannot support a reliable rule base beyond generic disclaimers, or if admins say a CSP discovery call already produces the same packet quickly for free. Also narrow away from full migration execution; that market is already well served.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Wrong tenant-country decisions can create billing, compliance, data-region, and migration-cost risk. |
| Feasibility | 4/5 | A no-credential questionnaire plus rules engine and Markdown/PDF outputs is a 1–3 day MVP. |
| Demo potential | 4/5 | Easy to demo with an HK→UAE scenario producing risk flags, CSP questions, and a decision memo. |
| Distribution | 4/5 | Specific high-intent search terms plus r/sysadmin/r/Office365/Microsoft CSP content; not just generic indie launch channels. |
| Competitive wedge / timing | 3/5 | Migration tools are strong incumbents, but the avoid-or-scope preflight niche is narrower and timely. |
| Total | 19/25 | Clears repo threshold and both dimension gates. |

## Decision

Create a dedicated repo: `halaprix/tenant-route`.

Status: repo-created; scaffold pushed and tagged `v0.1.0-alpha.0`.

Weakest dimension: competitive wedge/timing at 3/5 because tenant migration vendors and consultants are mature. The MVP must stay sharply pre-migration and decision-packet oriented.

## Next build step

Build a CLI/static web prototype with one sample HK→UAE scenario, a YAML rules file for CSP/tenant-country checks, and Markdown output templates for the executive memo, CSP question list, and migration scoping packet.
