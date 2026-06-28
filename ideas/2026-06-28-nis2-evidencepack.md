# Day 010 — NIS2 EvidencePack

Date: 2026-06-28
Status: blocked

## One-line pitch

A local-first evidence binder that turns exports, screenshots, and policy files into an auditor-ready NIS2 evidence pack for small EU IT teams without connecting cloud admin credentials to a SaaS GRC platform.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1uhokqz/we_built_a_free_opensource_nis2_compliance/ | Fresh post describes a free/open-source NIS2 platform built because closed-source tools charge thousands per year for checklist workflows. It frames the target as 50–250 person companies with no CISO and often one IT owner. |
| NISD2 pricing | https://nisd2.eu/en/pricing | The product offers hosted NIS2 checklist workflows, evidence upload, audit trail, PDF export, registers, reminders, and a paid self-host license. This validates the checklist/evidence workflow while also showing the manual evidence-upload surface. |
| ENISA | https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance | ENISA’s NIS2 technical guidance includes practical advice, examples of evidence, and mappings of security requirements. Evidence is not incidental; it is part of implementation. |
| Reglyze comparison | https://reglyze.com/en/best-nis2-compliance-software | NIS2 compliance software is already crowded: Reglyze, Vanta, Drata, Secfix, Formalize, ComplyCloud, Heimdal, Make IT Safe, EGERIE, Oodrive, and OneTrust are compared. The wedge cannot be “another checklist.” |
| Vanta NIS2 | https://www.vanta.com/products/nis2 | Vanta positions NIS2 around automated tests, 400+ integrations, evidence reuse, control mapping, vendor risk, and inspection readiness. This is the high-end direct substitute. |
| Drata NIS2 | https://drata.com/frameworks/nis-2 | Drata emphasizes centralized evidence, continuous monitoring, workflow orchestration, and controls linked to risks. This confirms evidence collection is a core paid GRC value. |
| Microsoft NIS2 | https://www.microsoft.com/en-us/trust-center/compliance/nis2-compliance | Microsoft says 77% of EMEA organizations are not fully ready for NIS2 and points to Purview Compliance Manager as one way to track compliance status and evidence. |

Research note: Reddit public JSON was unavailable in this environment; collection used the Reddit RSS fallback. RSS returned usable fresh r/SideProject posts, but most configured subreddit RSS calls returned `HTTP 429`, so the run stopped retrying and used web search/product pages for validation. X search was attempted via `xurl` and returned `401 Unauthorized`, so X was not used as evidence.

## Problem

For newly in-scope EU SMEs, NIS2 work is not only understanding a legal/control checklist. A small IT team also needs to prove what is already in place: which Microsoft 365 controls are enabled, where supplier reviews live, when incident procedures were approved, who owns each control, and whether the evidence is fresh enough to survive a management or regulator review.

The status quo is a folder of screenshots, CSV exports, policy PDFs, and spreadsheet rows assembled by one overloaded IT owner or consultant. That clears the status-quo pain test: it can easily waste more than 30 minutes per week during preparation, create compliance risk, and block management sign-off or customer procurement.

## Target user

Small EU companies and MSPs serving 50–250 person clients that are newly in scope for NIS2 and primarily run Microsoft 365, Google Workspace, GitHub/GitLab, endpoint screenshots, shared drives, and policy documents.

## MVP scope

- CLI/local desktop workflow: `evidencepack new --profile de-sme-m365-github`.
- Local inbox for CSV/JSON exports, PDFs, screenshots, Markdown, and policy files.
- Static NIS2/ENISA control catalog with evidence examples, owners, and freshness expectations.
- Artifact index: filename, hash, captured date, owner, source system, detected control keywords, and confidence.
- Review screen or generated Markdown where the user accepts/edits suggested control mappings.
- Export `evidence-pack.zip` with a coverage matrix, missing-evidence report, artifact index, and consultant/auditor README.
- CSV/Markdown rows that can be pasted into NISD2, spreadsheet trackers, or consultant templates.

Non-goals for v0.1: legal advice, compliance certification, cloud admin credential storage, continuous monitoring, or replacing Vanta/Drata/NISD2/Reglyze.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Vanta / Drata | Strong automated evidence collection and continuous control monitoring. They are broad GRC platforms with many integrations; the wedge is a cheaper offline binder for teams that are not ready to buy or connect a full SaaS GRC system. |
| Direct competitor | NISD2 / Reglyze / NIS2 Pro-style tools | Purpose-built NIS2 checklists, registers, evidence upload, and exports. EvidencePack should complement these by preparing importable evidence bundles, not compete as another checklist. |
| Direct competitor | Microsoft Purview Compliance Manager | Strong if the organization is Microsoft-centric and licensed for it. EvidencePack’s wedge is cross-artifact packaging and consultant handoff without becoming Microsoft-only. |
| Indirect substitute | NIS2 SME Toolkit, spreadsheets, shared drives | Cheap and understandable, but mapping evidence to controls, owners, and freshness is manual and fragile. |
| Indirect substitute | Consultant-led implementation | Helps interpretation, but recurring evidence collection and handoff can remain expensive and manual. |
| Status quo | One IT owner manually gathers screenshots/exports before review | Low software cost, high coordination cost, stale evidence risk, and weak traceability. |

## Wedge

**Wedge-first line:** one-person IT owners and MSP consultants preparing NIS2 binders for 50–250 person EU companies → Vanta/Drata, Microsoft Purview, NISD2/Reglyze, spreadsheets, consultants, and shared-drive folders → high-end tools are overkill or require cloud integrations, checklist tools still need manual evidence upload, and spreadsheets do not preserve freshness/traceability → local evidence-pack generator that maps existing exports/screenshots/policies to NIS2/ENISA rows and exports a clean binder for upload or consultant handoff → NIS2 search/content, MSP/compliance consultant posts, r/SideProject/open-source NIS2 discussions, and replies to SME readiness questions → 2026 NIS2 readiness is active, guidance includes evidence examples, and SMEs are comparing expensive tools against free/open-source checklists now.

The wedge is not “another NIS2 compliance platform.” It is the missing adapter between existing SME artifacts and whichever checklist, consultant, or GRC process the company already uses.

## Kill condition

Reject or narrow if target users say NISD2/Reglyze spreadsheet upload is already good enough, if useful mappings require privileged cloud APIs before a local-file MVP can prove value, or if buyers only want a full continuous-monitoring GRC platform. Also kill if legal/control interpretation becomes the product’s main value; that moves it into compliance advice instead of evidence packaging.

## Shortlist notes

| Candidate | Wedge-first gate result | Score | Decision |
|---|---|---:|---|
| NIS2 EvidencePack | One-person IT owners/MSP consultants preparing NIS2 binders → Vanta/Drata/Purview/NISD2/spreadsheets/consultants → high-end tools are overkill, checklist tools still need evidence, spreadsheets lose freshness/traceability → local evidence-pack generator for exports/screenshots/policies → NIS2 search, MSP/compliance content, and fresh open-source NIS2 threads → 2026 guidance/readiness pressure is active. | 19/25 | Winner. Clears repo-creation threshold and gates; remote repo was created, but scaffold push is blocked by GitHub 403. |
| GitHistClean | Developers fine-tuning local/code models → git2llm, repo-to-prompt tools, raw Git scripts, Unsloth/LLaMA-Factory datasets → the fresh post already ships a direct tool and the painful job is narrow → narrower evaluator/quality report for Git-history datasets → LocalLLaMA/GitHub content → personal code-model fine-tuning is active. | 16/25 | Held. Real pain, but the strongest signal is a competitor launch that already solves much of the job. |
| DevShelf | Developers losing saved technical links → Raindrop, browser bookmarks, Notion, local scripts, the fresh local-LLM bookmark tool → existing bookmark managers and the fresh post cover the core job → offline static dev-library exporter could be useful → dev-tool communities → local LLM privacy angle is timely. | 15/25 | Rejected/held. Bookmark/browser-extension space is crowded and the status quo is often tolerable. |
| ThreadCook | Founders reading long Reddit advice threads → generic AI summarizers, ChatGPT paste, Reddit save, browser extensions → summaries miss nuance/trust and Reddit API/platform rules add risk → chaptered evidence-linked “cookbook” from one thread → side-project communities → fresh post asks for this exact format. | 14/25 | Rejected. Generic AI summarization is crowded and platform trust/API risk weakens the wedge. |
| SME WhatsApp Desk | SMEs managing customer WhatsApp conversations → WhatsApp Business app, official BSP inboxes, Intercom/Zendesk-style messaging, CRMs → many substitutes already exist and official API friction is not enough wedge → niche onboarding/reporting layer would need sharper segment → SME/operator communities → fresh SideProject post shows continued demand. | 13/25 | Rejected. Crowded CRM/inbox category and no sharp first-user channel. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Compliance evidence gathering creates real time cost, sign-off risk, and potential regulatory/customer-procurement exposure. |
| Feasibility | 4/5 | A local-file CLI with a static control catalog, artifact index, and binder export is buildable in 1–3 days. Avoiding live cloud integrations keeps the MVP small. |
| Demo potential | 4/5 | Strong demo: drop sample M365/GitHub/policy files into an inbox, review mappings, export a coverage matrix and evidence zip. |
| Distribution | 4/5 | Specific channels exist: NIS2 readiness/search content, MSP/compliance consultant content, open-source NIS2 communities, and reply strategy around SME NIS2 tool comparisons. |
| Competitive wedge / timing | 3/5 | Timing is strong, but the category is crowded. The wedge only holds if EvidencePack stays an offline evidence adapter rather than becoming another GRC checklist. |
| Total | 19/25 | Clears total, distribution, and wedge gates. |

## Decision

Create the dedicated project scaffold for NIS2 EvidencePack, but mark the day `blocked` rather than cleanly `repo-created`: the GitHub repository was created at https://github.com/halaprix/nis2-evidencepack, the local scaffold commit is ready (`98e199d`), and `git push` failed with GitHub HTTP 403 (`Permission to halaprix/nis2-evidencepack.git denied to halaprix`).

## Next build step

Implement the first runnable slice: `evidencepack new`, a tiny YAML control catalog, fixture import for synthetic Microsoft 365/GitHub/policy files, and `evidencepack export` producing a coverage matrix plus `evidence-pack.zip` without network access or stored admin credentials.
