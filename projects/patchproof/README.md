# PatchProof

PatchProof turns messy patch-tool, vulnerability-scan, and endpoint last-seen exports into a manager/auditor-ready evidence packet that explains what was patched, what is offline, what broke, and what needs an exception.

## Problem

Small and mid-size IT teams often have multiple conflicting truths about patching: a patch/RMM tool says deployment succeeded, a vulnerability scanner still shows risk, field laptops have not checked in, and legacy apps create rollback risk. When leadership sees a high vulnerability score, the sysadmin has to manually assemble screenshots, CSV exports, ticket notes, last-seen data, and exception rationale.

## Target user

Solo and small-team Windows/sysadmin operators responsible for patch management who must defend remediation progress to managers, auditors, security teams, or business owners without buying another enterprise vulnerability platform.

## MVP

- Local-first CLI that ingests static CSV/JSON exports from patch tools, vulnerability scanners, endpoint inventory, and ticket notes.
- Asset mapping file to reconcile scanner names with patch/RMM names.
- Classifications: patched, pending reboot, offline/stale, not applicable, rollback/breakage, exception needed, unknown.
- Markdown/HTML evidence packet with executive summary, stale endpoint list, per-asset appendix, and exception-ready language.
- Fixture-driven adapters for generic CSV plus starter shapes for Intune, PDQ, Action1/other RMM exports, and Qualys/Tenable/Rapid7-style scanner exports.

## Non-goals

- No endpoint control, patch deployment, or remediation automation in the first slice.
- No live API credentials or SaaS account connection.
- No claim that a patch was applied unless imported evidence says so.
- No storage of real asset identifiers, internal hostnames, IP addresses, user names, tickets, or vulnerability data in public fixtures.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vpgyxr/new_boss_is_an_arrogant/ | Fresh sysadmin reports being blamed for a high vulnerability score despite deployed patches and offline field PCs. |
| PDQ | https://www.pdq.com/blog/vulnerability-management-for-it-audits-prove-patch-compliance/ | Patch-compliance evidence needs asset inventory, remediation history, deployment records, and exception logs. |
| Microsoft Intune reports | https://learn.microsoft.com/en-us/intune/device-management/reports/overview | Endpoint evidence exists inside platform dashboards but often needs reconciliation. |
| Qualys patch reports | https://docs.qualys.com/en/vm/latest/reports/patch_reports/win_patch_report.htm | Scanner-side patch reports are a real substitute and integration source. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only, consolidated in the 100-days master repo.
