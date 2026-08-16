# Day 056 — PatchProof

Date: 2026-08-16
Status: repo-created
Repo: [`projects/patchproof`](../projects/patchproof)

## One-line pitch

PatchProof turns messy patch-tool, vulnerability-scan, and endpoint last-seen exports into a manager/auditor-ready evidence packet that explains what was patched, what is offline, what broke, and what needs an exception.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vpgyxr/new_boss_is_an_arrogant/ | Fresh sysadmin reports being blamed for a high vulnerability score even though patches were deployed; field tech PCs being offline and a legacy patch tool breaking developer apps created a management conflict. |
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vpmof4/it_administering_core_enterprise_system/ | Fresh sysadmin asks how mature IT teams handle limited admin access to core business systems; the common pattern is governance evidence, access boundaries, and auditability rather than informal ownership arguments. |
| PDQ | https://www.pdq.com/blog/vulnerability-management-for-it-audits-prove-patch-compliance/ | Patch-compliance evidence is a recognized job: auditors want asset inventory, remediation history, deployment records, and exception logs tied to devices and dates. |
| Microsoft Intune docs | https://learn.microsoft.com/en-us/intune/device-management/reports/overview | Intune already has device health/compliance reports, confirming that endpoint evidence exists but usually lives inside platform dashboards. |
| Qualys docs | https://docs.qualys.com/en/vm/latest/reports/patch_reports/win_patch_report.htm | Qualys patch reports identify fixes for detected vulnerabilities; another signal that teams need to reconcile scanner findings with remediation status. |
| Rapid7 docs | https://docs.rapid7.com/insightvm/working-with-vulnerability-exceptions/ | Vulnerability exception workflows exist, but they assume the organization is already inside a vulnerability-management platform. |

## Problem

Small and mid-size IT teams often have more than one truth about patching: a patch/RMM tool says deployment succeeded, a vulnerability scanner still shows risk, field laptops have not checked in, and a legacy updater or business app creates breakage risk. When leadership sees a high vulnerability score, the sysadmin has to manually assemble screenshots, CSV exports, ticket notes, last-seen data, rollback notes, and exception rationale to prove that the issue is offline endpoints, scanner lag, unsupported software, or a real remediation gap.

The status quo is painful because it can waste hours per review cycle, creates public blame inside the company, and can turn a technical nuance into a performance or compliance fight. The daily evidence does not need another full patch-management platform; it needs a neutral, local packet that explains the difference between "not patched," "patched but not rescanned," "offline," "rolled back due breakage," and "accepted exception."

## Target user

Solo and small-team Windows/sysadmin operators responsible for patch management who must defend remediation progress to managers, auditors, security teams, or business owners without buying another enterprise vulnerability platform.

## MVP scope

- Local-first CLI that ingests CSV/JSON exports from patch tools, vulnerability scanners, ticket systems, and endpoint inventory.
- Mapping file for asset identifiers so the user can reconcile scanner asset names with patch-tool or RMM asset names without uploading data.
- Classification engine for each finding/asset: patched, pending reboot, offline/stale, not applicable, rollback/breakage, exception needed, or unknown.
- Markdown/HTML evidence packet with executive summary, per-asset appendix, stale endpoint list, rollback notes, and exception-ready language.
- Fixture-driven adapters for generic CSV plus starter shapes for Intune, PDQ, Action1/other RMM exports, Qualys/Tenable/Rapid7-style scanner exports.
- No credentials, no live API calls, no endpoint control, and no claims that a patch was applied unless present in imported evidence.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | PDQ, Action1, ManageEngine, NinjaOne, Intune | These platforms deploy patches and expose dashboards/reports. They are the system of record for many teams, but each mostly explains its own view; PatchProof is a neutral reconciliation/export layer for mixed tools and blame-heavy review meetings. |
| Direct competitor | Qualys, Tenable, Rapid7 InsightVM | Strong vulnerability-management platforms with reporting and exception workflows. They are expensive/operationally heavy for small teams and still need reconciliation with patch/RMM evidence and offline endpoint reality. |
| Indirect substitute | Spreadsheets, screenshots, ticket notes, ad-hoc PowerShell | Common current workaround. Flexible, but slow, brittle, hard to rerun, and easy to argue about when a vulnerability score conflicts with patch-tool status. |
| Indirect substitute | Audit-prep consultants or internal security analysts | Can produce defensible reports, but overkill for routine patch-review disputes and not available to many small teams. |
| Status quo | Manually defend patching in meetings | The sysadmin exports CSVs, takes dashboard screenshots, cites stale devices, and explains breakage history repeatedly. This can waste hours and cause reputational damage. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| PatchProof | Small-team Windows/sysadmins blamed for high vulnerability scores → patch/RMM dashboards, Qualys/Tenable/Rapid7, spreadsheets/screenshots → substitutes either live inside one platform or require manual reconciliation when endpoints are offline or patches broke apps → local packet builder that reconciles patch, scanner, last-seen, rollback, and exception evidence without credentials → r/sysadmin support/search threads, MSP forums, PDQ/Intune/Action1 admin content, and search pages around “prove patch compliance” → fresh r/sysadmin post shows patch evidence becoming a management conflict | Winner; strong status-quo pain and concrete channels despite incumbent tools. |
| BanRace | Self-hosters behind CGNAT who CrowdSec-ban their own changing home IP → CrowdSec allowlists, DDNS cron scripts, crowdsec-ddns-monitor, VPS console → substitutes exist and the race condition is specific but narrow → dry-run/rescue packet for dynamic allowlist changes → r/selfhosted and CrowdSec forums → fresh self-ban post | Held/rejected; useful, but very close to the earlier BanLift idea and GitHub/web results already show a direct DDNS monitor. |
| MailJudge | Self-hosted email operators whose Gmail delivery still lands in spam after SPF/DKIM/DMARC/PTR look correct → Mail Tester, MXToolbox, happyDeliver, Google Postmaster Tools → substitutes diagnose authentication but cannot guarantee Gmail reputation or inboxing → original-source evidence packet plus DNS/reputation checklist → r/selfhosted and mailadmin SEO → fresh self-hosted email complaint | Held; real pain, but direct deliverability tools are strong and the wedge needs a Gmail-specific proof path that a small MVP may not access. |
| AccessRACI | IT leaders denied admin access to ERP/core business systems → IAM/IGA suites, RACI templates, policy docs → substitutes are too heavy for a single access-boundary negotiation → least-privilege access request packet with audit/control language → r/sysadmin, IT governance templates, MSP content → fresh post asks how mature teams handle business-owned core apps | Idea-only candidate; compliance pain is real, but product scope drifts toward consulting/templates unless narrowed to one system family. |
| LogNudge | Small Node/Nest backends where important logs are ignored → Wotchi, Sentry, Better Stack, Datadog, OpenTelemetry → incumbents and fresh side-project already solve alerting → narrow “single-file Telegram webhook alerts” has weak differentiation → Node communities → fresh r/SideProject post validates pain | Rejected; crowded observability/alerting category with no sharp wedge. |

## Wedge

PatchProof does not try to replace patch deployment, RMM, Intune, or vulnerability-management platforms. It wins because the painful moment is cross-tool explanation: the patch tool, scanner, ticket system, and business-risk story disagree. A 1–3 day MVP can ingest static exports, classify the disagreement, and produce a reproducible packet that a sysadmin can attach to a review thread without granting another SaaS access to endpoint or vulnerability data.

The narrow wedge is defensive evidence for small teams: "show me why the score is still high" becomes a local report with stale devices, deployed fixes awaiting rescan, rollback-caused exceptions, and true gaps.

## Kill condition

Reject or narrow if PDQ/Action1/Intune plus Qualys/Tenable/Rapid7 already produce a combined cross-tool packet that handles offline endpoints, scanner lag, rollback/breakage notes, and exception-ready language from static exports in under 10 minutes without platform credentials. Also reject if sysadmins say screenshots/CSV spreadsheets already take less than 30 minutes per review cycle.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The workaround can waste hours and damage trust when patch compliance becomes a management/security argument. |
| Feasibility | 4/5 | Static CSV/JSON ingestion, mapping, classification, and Markdown/HTML rendering are buildable quickly; live API adapters are explicitly out of scope. |
| Demo potential | 4/5 | A demo can show conflicting sample exports becoming a clear executive summary, stale endpoint list, and exception appendix. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin threads, MSP/admin communities, PDQ/Intune/Action1 search content, and direct replies to “prove patch compliance” / “vulnerability score high” problems. |
| Competitive wedge / timing | 4/5 | Strong incumbents exist, but the local cross-tool reconciliation packet is narrower than patch deployment or vulnerability management and fits small teams that cannot add another platform. |
| Total | 20/25 | Clears repo threshold and both dimension gates; weakest dimensions are tied at 4/5. |

## Decision

Create repo. PatchProof scored 20/25 with distribution 4/5 and competitive wedge/timing 4/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/patchproof`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Build the first local parser/rendering spike: ingest three fixture CSVs (patch status, scanner findings, endpoint last-seen), classify five sample assets, and render a Markdown evidence packet with executive summary plus per-asset appendix.

## Source access caveats

Reddit public JSON was blocked with `theme-beta`, and the run used `reddit-rss-fallback` for r/sysadmin, r/selfhosted, and r/SideProject. Several subreddit RSS probes hit `HTTP 429`, and Reddit thread JSON for comments returned `HTTP 403`, so no Reddit scores/comment counts or comments were used. X/Twitter `whoami` worked, but `xurl search` returned `401 Unauthorized`; no X posts were used and no social writes were attempted. Competitor validation used web search and original vendor documentation where available.
