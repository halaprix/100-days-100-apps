# Day 029 — TicketScrub

Date: 2026-07-17
Status: repo-created

## One-line pitch

A Jira draft-side PII preflight that warns users before they submit risky issue text, comments, or pasted email dumps, with local-only rules, redaction suggestions, and an admin policy pack for teams that are not ready to buy full enterprise DLP.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback + web extraction — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uys0ua/how_do_you_stop_users_from_accidentally_adding/ | Fresh sysadmin post asks for a tool that checks PII in real time while users create or edit Jira tickets because existing tools scan after the ticket already exists and may have been seen. Comments confirm users paste whole customer emails, IDs, and passwords into tickets and that blocking before entry is not something they have seen. |
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uyskn0/custom_account_creation_entra_for_1st2nd_line/ | Adjacent fresh signal: admins want safer front doors for junior teams because raw admin portals are too easy to use incorrectly; reinforces the pattern of pre-submit guardrails over after-the-fact cleanup. |
| Atlassian Marketplace | https://marketplace.atlassian.com/apps/1225698/pii-protection-and-dlp-for-jira | Existing paid DLP apps scan Jira issues, attachments, and images and can trigger remediation, proving budget and category demand but also showing the market is mostly instance-scan/remediate oriented. |
| Atlassian Marketplace | https://marketplace.atlassian.com/apps/1235792/data-pii-scanner-dlp-for-jira | miniOrange lists real-time scanning, redaction, masking, encryption, dashboards, and Forge-native deployment for Jira; this is a strong direct competitor and forces a narrower wedge. |
| Atlassian Developer Docs | https://developer.atlassian.com/platform/forge/understanding-ui-modifications/ | Forge UI Modifications can alter Jira Global issue create, issue view, issue transition, and Jira Service Management request-create portal behavior, making a pre-submit/admin-policy MVP technically plausible. |
| Atlassian Developer Docs | https://developer.atlassian.com/cloud/admin/dlp/about/ | Atlassian's own DLP framing centers classification, policy, monitoring, and governance across cloud products; good context for why smaller teams may still need a lighter workflow-specific preflight. |
| Nightfall AI | https://www.nightfall.ai/guide/the-essential-guide-to-data-loss-prevention-dlp-jira | Nightfall explains that Jira issues can contain PII, PHI, passwords, API keys, cookies, certificates, and other sensitive data, and that out-of-the-box SaaS apps require extra visibility and controls. |

Source access notes: Reddit public JSON endpoints returned `HTTP 403 theme-beta`, so Reddit collection used the read-only skill's public RSS fallback and one public web extraction of the Reddit thread. Several subreddit RSS feeds returned `HTTP 429`; no retry loop was used. X `whoami` worked, but X search returned `401 Unauthorized`, so X was not used as evidence. Repo files referenced by the README (`docs/PROCESS.md`, `docs/SCORING.md`, and `sources.yml`) were not present in this checkout; this run followed `AGENTS.md`, loaded project context, and the requested workflow rules.

## Shortlist and wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| TicketScrub | Jira admins/security leads at small regulated teams → Jira Marketplace DLP apps, Atlassian Guard, Nightfall, training, and after-the-fact ticket scans → substitutes often detect after sensitive data is already stored, are overkill for teams not ready for enterprise DLP, or do not coach the user at draft time → lightweight browser/Forge preflight that flags obvious PII/secrets before create/update and suggests safe redactions without storing ticket contents → r/sysadmin, Atlassian Community, Jira admin searches, security-awareness content, and Marketplace/extension demos → fresh sysadmin thread asks for exactly real-time Jira draft checking now. | Winner; scored, but wedge is narrow because direct DLP competitors exist. |
| AccountMint | Entra admins delegating account creation to 1st/2nd line teams → Entra portal, Microsoft Forms + Power Automate, PowerShell Universal, custom scripts → substitutes either expose too many knobs or require procurement/approval → constrained account-create form that emits policy-checked Graph actions and an audit packet → r/sysadmin and M365 admin content → fresh post asks for a friendly form before junior staff make mistakes. | Rejected/held: real workflow pain, but the best MVP is close to Power Automate templates and procurement-specific internal tooling. |
| ExchangeGhost | Hybrid Exchange admins stuck with orphaned contact/mailbox remnants → Exchange Admin Center, PowerShell cmdlets, Microsoft docs, manual AD attribute spelunking → substitutes require knowing which object/attribute layer is lying → read-only tracer that maps AD, Exchange on-prem, EXO, DL expansion, and bounceback evidence into a cleanup checklist → r/sysadmin and M365 admin searches → fresh post shows a confusing bounceback after mailbox removal. | Strong narrow admin-tool idea; held because it requires lab coverage of hybrid Exchange edge cases and has lower demo speed today. |
| SmartSAS Verdict | Homelab/ZFS builders using refurb SAS disks → `smartctl`, badblocks, vendor docs, forum replies → raw SAS SMART counters are hard to interpret before pool creation → read-only SAS/HBA health report that explains defect lists, non-medium errors, link stats, and burn-in steps → r/selfhosted, r/homelab, ZFS content → fresh post asks whether a drive with SAS SMART errors is trustworthy. | Rejected for today: useful, but overlaps recent hardware-diagnostic winners and risks being advice around `smartctl` rather than a durable app. |
| VaultSyncMap | Obsidian users self-hosting full vault/config/plugin sync → Obsidian Sync, Syncthing, Git, Remotely Save, cloud drives → substitutes either miss mobile/config details or create conflict risk → wizard that recommends a sync topology and tests plugin/config drift across devices → r/selfhosted, Obsidian forums/search → fresh post wants reliable notes + settings + plugins sync without babysitting. | Rejected: notes/sync space is crowded and the pain is tolerable unless narrowed to a specific regulated/offline workflow. |

## Problem

Jira and Jira Service Management tickets are magnets for sensitive data. Users paste customer emails, screenshots, account identifiers, passwords, logs, tokens, third-party conversations, and medical or financial context into tickets because it feels like the fastest way to get support.

The painful part is timing: once a ticket is created or a comment is saved, the data has already entered Jira, may have triggered notifications, may be visible to broad project roles, and may require admin cleanup or audit evidence. Training and after-the-fact scans help, but they do not stop the first bad paste.

The status quo wastes time and creates real risk: admins review alerts after storage, manually redact, close tickets, warn users, and hope compliance evidence is good enough. For regulated support desks, the failure mode is not annoyance; it is a security/compliance incident.

## Target user

- Jira Cloud and Jira Service Management admins in healthcare, finance, education, MSP, BPO, and customer-support teams.
- Security/compliance owners at small and mid-sized orgs that cannot justify broad enterprise DLP yet.
- Helpdesk managers who need user coaching at the point of ticket creation, not another dashboard of violations.

## MVP scope

- Browser extension first: detect Jira create/edit/comment fields on configured Atlassian sites and run local rules before submit.
- Optional Forge UI Modifications proof-of-concept for Jira Global issue create and JSM request-create portal where supported.
- Built-in detectors for common PII/secrets: SSNs, credit cards, IBANs, API keys, passwords, private keys, birth dates, phone/email over-sharing, full email-thread dumps, and configurable regexes.
- Inline warning panel with severity, matched category, safe redaction suggestion, and a "submit anyway with reason" audit note.
- Admin policy JSON export/import so teams can publish a small rules pack without sending ticket contents to a third party.
- Demo fixture that simulates a Jira issue form locally and shows before/after redaction guidance without needing a real Jira tenant.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | miniOrange Data - PII Scanner (DLP) for Jira | Strong competitor: claims real-time scanning, redaction, masking, encryption, dashboards, custom regexes, and Forge-native operation. TicketScrub must avoid generic DLP and focus on draft-side user coaching, low-friction evaluation, and local/no-storage deployment. |
| Direct competitor | Polymetis PII Protection and DLP for Jira | Scans issues, attachments, and images, supports remediation via Jira Automation, and offers site scans. More complete for paid governance; less positioned as a tiny pre-submit training/preflight tool. |
| Direct competitor | Atlassian Guard / Atlassian DLP capabilities | Native governance and policy context, but the public docs frame classification, policies, monitoring, and data security controls rather than a lightweight user-facing draft preflight. |
| Direct competitor | Nightfall and broader SaaS DLP platforms | Powerful cross-SaaS detection and response, but sales-led/enterprise-weight for teams that just need a focused Jira ticket guardrail. |
| Indirect substitute | Training, warning banners, ticket templates, automation rules, and closing bad tickets | Cheap and common, but still relies on users remembering policy and usually reacts after bad content is pasted or saved. |
| Status quo | Let tickets be created, scan later, redact manually, and warn repeat offenders | Creates a stored-data event, notification/audit trail, and manual cleanup burden; exactly the timing problem raised in the source thread. |

## Wedge

TicketScrub should not pretend to beat full DLP platforms. The wedge is narrower:

- first-run in minutes as a browser extension against a single Jira tenant or demo form,
- local-only detection by default so admins can evaluate without granting a vendor broad Jira access,
- pre-submit coaching that teaches users what to remove before data is stored,
- policy-as-JSON for teams that want a lightweight guardrail before they buy or configure full DLP,
- a demo/report artifact security leads can use to justify a later Marketplace or enterprise DLP rollout.

This is enough for a 1-3 day MVP because the first demo can be a content-script preflight and synthetic Jira form, not a full Marketplace app. The distribution path is concrete: the r/sysadmin thread, Atlassian Community discussions, Jira admin SEO pages for "PII in Jira tickets", and security-awareness demos around pasted emails/passwords in helpdesk workflows.

## Kill condition

Kill or narrow if a Jira Marketplace competitor demonstrates reliable pre-storage blocking with inline user coaching at a price/friction level suitable for small teams, or if Forge/browser limitations prevent intercepting create/update/comment submits without brittle selectors. In that case, narrow to a demo/audit tool for security-awareness training rather than a production guardrail.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | Preventing PII/secrets from entering Jira can avoid compliance incidents, cleanup work, and broad internal exposure. |
| Feasibility | 4/5 | Browser-extension MVP is straightforward; production-grade Forge/JSM coverage and false-positive tuning need more work. |
| Demo potential | 4/5 | A fake Jira form with pasted customer email, credentials, and screenshots can show warnings/redaction clearly. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin, Atlassian Community, Jira admin searches, security-awareness posts, and compliance/helpdesk operators. |
| Competitive wedge / timing | 3/5 | Fresh source is strong, but direct Jira DLP apps already exist and one claims real-time scanning; the wedge must stay pre-submit/local/coaching-focused. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create `halaprix/ticketscrub` as a dedicated project repo. The score clears the 18/25 threshold, Distribution is 4/5, and Competitive wedge/timing is 3/5. This is a repo-worthy bet only if it stays a lightweight draft preflight, not a generic Jira DLP clone.

## Next build step

Implement a local browser-extension prototype that injects into a fixture Jira issue form, detects risky PII/secrets before submit, suggests redactions, and exports an admin policy JSON plus a short audit report.
