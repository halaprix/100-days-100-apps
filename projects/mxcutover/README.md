# MxCutover

MxCutover is a Microsoft 365 email-gateway cutover readiness packet for small IT teams moving between Mimecast, Proofpoint, or similar secure email gateway stacks.

It does not migrate mail or replace vendor professional services. It turns messy prerequisites, DNS/authentication checks, connector risk, SSO setup, and rollback notes into a public-safe plan an admin can review before a change window.

## Problem

Small IT teams still get pushed through surprisingly manual secure email gateway migrations. A fresh r/sysadmin thread described a Mimecast-to-Proofpoint move driven by price increases and false negatives, then called the Proofpoint onboarding archaic: manual Azure app registration, SSO setup, separate portal/pod concepts, and confusing handoffs.

The pain is not just annoyance. A bad cutover can break mail flow, weaken SPF/DKIM/DMARC posture, create over-broad app permissions, or leave admins without a rollback packet during a narrow change window.

## Target user

- Microsoft 365 admins at SMBs and mid-market orgs switching secure email gateways.
- MSP engineers onboarding a customer to Proofpoint Essentials or similar gateway products.
- Security leads who need a readable change packet before approving a mail-flow cutover.

## MVP

- Guided CLI or local web wizard for a single Microsoft 365 tenant and email gateway migration.
- Input current provider, target provider, domains, mail-flow mode, MX/SPF/DKIM/DMARC state, connectors, SSO/app-registration assumptions, and rollback window.
- Generate a Markdown readiness packet with:
  - preflight checklist,
  - DNS and mail-flow TODOs,
  - Entra app permission review checklist,
  - cutover sequence,
  - rollback plan,
  - questions to send to the vendor/MSP.
- Include synthetic examples only; no real tenant credentials or customer mail data.

## Non-goals

- No automated DNS, Microsoft Graph, or Proofpoint API writes in the first MVP.
- No email archive migration, PST migration, or mailbox data movement.
- No claim that the packet replaces vendor support, professional services, or change approval.
- No collection of tenant secrets, OAuth tokens, private mail logs, or customer data.

## Source evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uzc2fg/for_those_who_have_migrated_from_mimecast_to/ | Fresh sysadmin post says a move from Mimecast to Proofpoint followed price increases and false negatives, then describes onboarding as archaic and manual. |
| Proofpoint Docs | https://help.proofpoint.com/Essentials/Product_Documentation/Account_Management/Integrations/Microsoft_365_Integration_MX | Proofpoint's Microsoft 365 integration docs show real mail-flow entities, global admin requirements, app permissions, connectors, rules, DNS/SPF next steps, and change-window risk. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/saas-apps/proofpoint-ondemand-tutorial | Microsoft documents Proofpoint on Demand SSO prerequisites and Entra setup steps, confirming identity setup is part of the migration surface. |
| Sherweb Helpdesk | https://helpdesk.sherweb.com/en-us/knowledge-base/articles/KA-03891 | Sherweb notes onboarding changes now give customers full control and points admins to self-service provisioning guides, increasing the burden on customer/MSP admins. |
| Proofpoint comparison page | https://www.proofpoint.com/au/compare/proofpoint-vs-mimecast | Proofpoint markets a five-step migration framework away from Mimecast, proving vendor-recognized demand but also showing the need to avoid competing with full migration services. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Proofpoint migration framework and support | Best source of product-specific truth; MxCutover should complement it by producing an internal readiness packet, not replace vendor guidance. |
| Direct competitor | MSP/professional services migration partners | Stronger for complex migrations, but expensive and often opaque for small teams that need to prepare before kickoff. |
| Direct competitor | Transvault and archive-migration specialists | Relevant for archive/PST/journal migrations, but MxCutover avoids archive data movement and focuses on SEG/M365 readiness. |
| Indirect substitute | Vendor docs, Microsoft Learn, spreadsheets, change tickets, and one-off runbooks | Cheap but scattered across identity, DNS, Exchange connectors, mail-flow rules, and rollback notes. Easy to miss a step under time pressure. |
| Status quo | Trust vendor onboarding, manually copy docs into a change ticket, and discover gaps during the cutover window | Creates avoidable downtime and security risk when mail flow, DNS, app permissions, or rollback assumptions are wrong. |

## Wedge

MxCutover wins only if it stays narrow: a read-only readiness packet generator for SMB/MSP Microsoft 365 gateway switches. The wedge is not migration automation. It is a faster way to assemble the checklist, risk questions, and rollback packet before a vendor call or change window.

Distribution is concrete: r/sysadmin threads about Mimecast/Proofpoint moves, MSP and Microsoft 365 admin content, and search pages for "Mimecast to Proofpoint migration checklist", "Proofpoint M365 onboarding", and "email gateway cutover rollback plan".

## Current status

v0.1.0-alpha.0 — scaffold/spec only. Next step: implement a local packet generator from a small YAML/JSON tenant-gateway profile and ship synthetic fixtures.
