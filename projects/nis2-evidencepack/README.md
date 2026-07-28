# NIS2 EvidencePack

A local-first evidence binder for small EU IT teams that turns exports, screenshots, and policy files into an auditor-ready NIS2 evidence pack without connecting cloud admin credentials to a SaaS GRC platform.

## Problem

NIS2 compliance tools and open-source checklists help teams understand the control list, but the tedious part for a 50–250 person company is proving what is already true: which Microsoft 365 settings are enabled, where supplier reviews live, which incident playbook was approved, and what evidence maps to each obligation.

Enterprise tools such as Vanta and Drata automate evidence collection, but they are broad GRC platforms with sales-led pricing and cloud integrations. Free/open-source NIS2 tools reduce checklist cost, but still leave one IT owner manually collecting and attaching evidence.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1uhokqz/we_built_a_free_opensource_nis2_compliance/ | Fresh post claims many German/EU SMEs face NIS2 with no CISO, expensive tools, and manual evidence upload/checklists. |
| NISD2 pricing | https://nisd2.eu/en/pricing | Free hosted checklist includes evidence upload, audit trail, PDF export, registers, and reminders; self-host is a paid license. |
| ENISA guidance | https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance | ENISA guidance explicitly includes practical advice, evidence examples, and mappings for NIS2 implementation. |
| Vanta NIS2 | https://www.vanta.com/products/nis2 | Incumbent automates monitoring/evidence across 400+ integrations and positions inspection readiness as the value. |
| Drata NIS2 | https://drata.com/frameworks/nis-2 | Incumbent emphasizes centralized evidence, continuous control monitoring, and workflow orchestration. |
| Microsoft NIS2 | https://www.microsoft.com/en-us/trust-center/compliance/nis2-compliance | Microsoft says many EMEA organizations are not fully ready and points to Purview Compliance Manager for evidence tracking. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Vanta / Drata | Strong automated evidence collection and continuous monitoring, but broad, sales-led GRC systems are overkill for SMEs trying to assemble a first NIS2 binder. |
| Direct competitor | NISD2 / Reglyze / NIS2 Pro-style tools | Purpose-built NIS2 checklists and registers. EvidencePack should not compete as another checklist; it should produce importable evidence bundles for these workflows. |
| Indirect substitute | NIS2 SME Toolkit, spreadsheets, shared drives | Cheap and understandable, but evidence mapping, freshness, and ownership tracking become manual and fragile. |
| Indirect substitute | Consultant-led implementation | Useful for interpretation, expensive for recurring evidence gathering and handoff. |
| Status quo | One IT owner gathers screenshots/exports into folders before review | Wastes repeated time, risks stale proof, and creates compliance exposure if management or auditors ask for traceability. |

## Wedge

Start as an offline adapter, not a GRC platform: import common SME evidence artifacts, map them to ENISA/NIS2 control rows, flag missing ownership/freshness, and export a clean binder that can be uploaded into NISD2, attached to a spreadsheet, or sent to a consultant.

## Target user

Small EU companies and MSPs helping 50–250 person clients that are newly in scope for NIS2 and primarily run Microsoft 365, Google Workspace, GitHub/GitLab, endpoint screenshots, shared drives, and policy documents.

## MVP

- `evidencepack new --profile de-sme-m365-github` creates a local evidence project.
- Import CSV/JSON exports, PDFs, screenshots, and policy files without storing admin credentials.
- Map artifacts to a small NIS2/ENISA control catalog with owner, date, freshness, and confidence.
- Generate `evidence-pack.zip` with an index, missing-evidence report, and auditor/consultant README.
- Export Markdown/CSV rows that can be pasted into existing NIS2 checklist platforms.

## Non-goals

- Not a legal opinion or compliance certification.
- Not a continuous monitoring platform in v0.1.
- Not a replacement for Vanta, Drata, NISD2, Reglyze, or a consultant.
- No secret storage or cloud admin credential collection in the MVP.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
