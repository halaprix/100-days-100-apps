# Day 030 — MxCutover

Date: 2026-07-18
Status: repo-created

## One-line pitch

A local Microsoft 365 email-gateway cutover readiness packet generator for SMB/MSP admins moving between Mimecast, Proofpoint, or similar secure email gateways before mail-flow, DNS, SSO, permissions, and rollback gaps break a change window.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uzc2fg/for_those_who_have_migrated_from_mimecast_to/ | Fresh sysadmin post says a Mimecast-to-Proofpoint move followed price increases and false negatives, then describes Proofpoint onboarding as archaic: manual Azure app registrations, SSO setup, a separate pod/portal feel, and old-looking processes. |
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uzgwbr/automated_app_patching_recommendations/ | Adjacent fresh signal: sysadmins are actively asking for budget-conscious tooling recommendations before operational maintenance work; supports the broader pattern of small teams needing practical decision packets, not sales decks. |
| Proofpoint Docs | https://help.proofpoint.com/Essentials/Product_Documentation/Account_Management/Integrations/Microsoft_365_Integration_MX | Proofpoint's Microsoft 365 integration docs show the real cutover surface: global admin credentials, tenant app permissions, Exchange connectors/rules, DNS/SPF next steps, and a recommendation to use a planned change-control window. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/saas-apps/proofpoint-ondemand-tutorial | Microsoft documents Proofpoint on Demand SSO prerequisites and Entra setup, confirming that identity configuration is part of the migration risk surface. |
| Sherweb Helpdesk | https://helpdesk.sherweb.com/en-us/knowledge-base/articles/KA-03891 | Sherweb says Proofpoint onboarding changes now give customers full control and self-service provisioning responsibility, which shifts more readiness burden to SMB/MSP admins. |
| Proofpoint comparison page | https://www.proofpoint.com/au/compare/proofpoint-vs-mimecast | Proofpoint markets a five-step migration framework away from Mimecast, proving vendor-recognized demand while also showing the MVP must not compete with full migration services. |
| Transvault | https://www.transvault.com/email-archive-migrations/proofpoint-migrations/ | Archive-migration specialists support Proofpoint/Mimecast migration scenarios and cite compliance, integrity, downtime, compatibility, and cost risks; useful boundary evidence for what MxCutover should not automate in v0. |

Source access notes: Reddit public JSON endpoints returned `HTTP 403 theme-beta`, so Reddit collection used the read-only skill's public RSS fallback where available. Several subreddit RSS feeds returned `HTTP 429`; no retry loop was used. Reddit comment/thread JSON fetches returned `HTTP 403`, so the Reddit evidence is limited to RSS titles/snippets and public permalinks. X `whoami` worked, but X search returned `401 Unauthorized`, so X was not used as evidence. Web search was sparse for some targeted queries, so competitor validation used direct public vendor/docs pages returned by broader searches and web extraction.

## Shortlist and wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| MxCutover | Microsoft 365 SMB/MSP admins switching Mimecast/Proofpoint-style email gateways → vendor onboarding, MSP professional services, migration partners, Microsoft/Proofpoint docs, spreadsheets/change tickets → substitutes are accurate but scattered across DNS, Exchange connectors, Entra app permissions, SSO, mail-flow mode, change window, and rollback assumptions; they do not create one internal readiness packet before the vendor call → local read-only packet generator for SEG/M365 cutovers with synthetic examples, checklists, vendor-question list, and rollback plan → r/sysadmin, MSP/M365 admin content, and search/reply strategy around Mimecast-to-Proofpoint/Proofpoint onboarding/checklists → fresh post shows price/false-negative-driven switching plus frustration with manual onboarding now. | Winner; clears threshold if kept as readiness-packet tooling, not migration automation. |
| PatchBudget | Budget-constrained sysadmins choosing application patch management → Action1, ManageEngine, NinjaOne, PDQ, Patch My PC, Intune, Chocolatey, Winget, spreadsheets → substitutes already solve patching or selection well enough if budget and estate are known → comparison worksheet that maps estate size, app catalog, Intune state, and budget to shortlist → r/sysadmin and MSP admin content → fresh post asks for patch-management recommendations. | Rejected: crowded patch-management category and the wedge is mostly buyer's-guide content, not a durable app. |
| VmdkSplit | VMware admins deciding whether to grow a multi-terabyte VMDK or move data to iSCSI/SAN LUN → VMware docs, storage vendor advice, consultants, forum replies, manual robocopy plans → substitutes are environment-specific and risk data-loss advice without enough context → read-only capacity/cutover checklist for large VMDK vs guest iSCSI decisions → r/sysadmin/VMware communities and storage SEO → fresh post asks for caveats before expanding a 2.6 TB virtual disk. | Held/rejected for today: useful but overlaps recent storage-diagnostic winners and may become advisory content rather than a small app. |
| AlarmLock | Android users who oversleep and need an alarm that cannot be dismissed from bed → Alarmy, Sleep as Android, NFC/barcode tasks, built-in Digital Wellbeing/Interaction Control, Play Store alarm apps → substitutes have ads/pro gates or can be gamed, but the category is crowded and platform restrictions are tricky → minimalist F-Droid alarm that locks dismissal for 5-10 minutes with transparent permissions → r/androidapps and F-Droid communities → fresh post asks for exactly this. | Rejected: consumer alarm space is crowded, device policy restrictions are brittle, and status-quo pain is personal rather than a strong app-lab wedge. |
| MicroVmail | De-Googled Android/LineageOS users tied to carrier voicemail apps that break with microG → stock carrier app, Voxist, Google services, carrier visual voicemail, manual call-in voicemail → substitutes fail for no-GMS users who still need old voicemails/export, but app/provider compatibility is fragmented → local voicemail export/compatibility checklist and fallback guide for microG/LineageOS → r/androidapps, F-Droid, LineageOS/microG communities → fresh post asks how to recover access/export after app install breaks. | Held: narrow and interesting, but carrier/app-specific risk is high and first MVP may be a support guide rather than software. |

## Problem

Email security gateway switches sit at the intersection of mail delivery, DNS, identity, app permissions, and vendor-specific portals. A small team moving from Mimecast to Proofpoint, or from any legacy SEG to a Microsoft 365-integrated model, has to reconcile:

- current and planned MX routing,
- SPF/DKIM/DMARC changes and TTL timing,
- inbound/outbound Exchange Online connectors and transport rules,
- Entra app registration or enterprise app prerequisites,
- SSO/user provisioning assumptions,
- vendor portal/pod/account handoffs,
- pilot/coexistence steps,
- rollback owners and communication plan.

The status quo is a messy change ticket assembled from vendor docs, Microsoft docs, screenshots, emails, and tribal knowledge. That wastes hours before every migration and creates real risk: broken inbound/outbound mail, over-broad app permissions, weak authentication posture, or no crisp rollback when the change window goes sideways.

## Target user

- Microsoft 365 admins at SMBs and mid-market orgs switching secure email gateways.
- MSP engineers onboarding customers to Proofpoint Essentials, Mimecast, Defender/EOP, or similar gateways.
- Security leads approving mail-flow changes who need a readable packet rather than scattered vendor docs.

## MVP scope

- Local CLI or small local web app that reads a synthetic-safe YAML/JSON `cutover-profile`.
- Profile fields for current provider, target provider, domains, mail-flow mode, MX/SPF/DKIM/DMARC state, Exchange connector assumptions, Entra/SSO prerequisites, change window, rollback owner, and vendor contacts/questions.
- Rules that classify missing prerequisites as `blocker`, `warning`, or `info`.
- Markdown packet export with readiness summary, cutover sequence, rollback checklist, DNS/identity/mail-flow TODOs, and vendor/MSP question list.
- Sample profiles for Mimecast-to-Proofpoint, Proofpoint-to-Defender/EOP, and generic SEG-to-SEG moves using synthetic domains only.
- No writes to DNS, Microsoft 365, Proofpoint, Mimecast, or customer systems in v0.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Proofpoint migration framework, onboarding docs, and support | Best source of product-specific truth. Proofpoint publicly describes a migration framework and detailed M365 integration steps. MxCutover must complement this by preparing the customer's internal readiness packet, not replacing vendor guidance. |
| Direct competitor | MSP/professional services migration partners | Stronger for complex migrations and production execution, but expensive/opaque for teams that need to prepare before kickoff or sanity-check a vendor plan. |
| Direct competitor | Transvault and archive-migration specialists | Relevant for archive/PST/journal migrations into or out of Proofpoint/Mimecast. MxCutover should explicitly avoid archive data movement and focus on SEG/M365 cutover readiness. |
| Indirect substitute | Microsoft Learn, Proofpoint docs, Sherweb helpdesk docs, spreadsheets, change tickets, and one-off runbooks | Accurate but scattered across identity, DNS, Exchange connectors, mail-flow rules, and rollback assumptions. Admins still have to assemble the packet manually. |
| Status quo | Trust vendor onboarding, copy docs into a ticket, and discover gaps during the cutover window | Creates avoidable downtime/security risk when DNS, connectors, app permissions, SSO, or rollback assumptions are wrong. |

## Wedge

MxCutover should not pretend to be a migration platform. The wedge is a narrow, local-first readiness packet generator for Microsoft 365 secure email gateway cutovers.

Why this can still work despite existing options:

- Vendor docs tell admins what is possible, but not whether their specific change packet is complete.
- MSP/pro-services teams execute migrations, but customers still need pre-kickoff questions, internal approvals, rollback ownership, and risk evidence.
- A 1-3 day MVP can generate useful value from structured inputs and public checklists without privileged API access.
- The output is shareable: a Markdown packet can be attached to a change ticket or vendor email, which creates a natural demo artifact.
- Distribution is specific: r/sysadmin threads about Proofpoint/Mimecast, MSP communities, M365 admin searches, and content targeting "email gateway cutover checklist" / "Mimecast to Proofpoint migration checklist".

## Kill condition

Kill or narrow if Proofpoint/Mimecast/MSP onboarding already provides a free customer-facing readiness export that covers DNS, Exchange connectors, Entra permissions, SSO, cutover sequence, rollback, and vendor-question lists in one packet. Also kill any scope that requires storing tenant credentials, real mail logs, or direct production writes before the app proves value as a local read-only packet generator.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A bad email gateway cutover can break mail flow or create security gaps; the workaround can easily burn hours across admins, vendors, and change boards. |
| Feasibility | 5/5 | v0 is a local packet generator with schemas, public checklists, and Markdown output; no private APIs required. |
| Demo potential | 4/5 | Synthetic Mimecast-to-Proofpoint profile can produce a clear before/after readiness packet and blocker list. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin, MSP/M365 admin communities, and search/reply content around Proofpoint onboarding and SEG cutover checklists. |
| Competitive wedge / timing | 3/5 | Fresh source plus vendor/self-service onboarding shift is timely, but vendors/MSPs are strong substitutes; wedge must stay preflight/readiness-packet focused. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create `halaprix/mxcutover` as a dedicated project repo. The score clears the 18/25 threshold, Distribution is 4/5, and Competitive wedge/timing is 3/5. Repo status is `repo-created`: scaffold pushed to GitHub and tagged `v0.1.0-alpha.0`.

## Next build step

Implement `mxcutover packet examples/mimecast-to-proofpoint.yaml` so it validates a synthetic cutover profile, emits blockers for missing SPF/DKIM/DMARC/SSO/rollback fields, and writes a Markdown readiness packet suitable for a change ticket or vendor kickoff email.
