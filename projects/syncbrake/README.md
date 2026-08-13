# SyncBrake

SyncBrake turns Microsoft Entra Connect pending-export deletes plus break-glass readiness facts into a safe preflight packet before a hybrid identity sync mistake locks an organization out.

## Problem

Hybrid identity admins can stage a normal-looking Entra Connect change that becomes a mass-delete or mass-disable export. Microsoft provides the raw controls: accidental-delete threshold, staging mode, Synchronization Service Manager, `csexport`, `CSExportAnalyzer`, and emergency access guidance. Small teams still need a compact go/no-go packet before disabling thresholds, promoting staging servers, or changing OU scope.

## Target user

Small and mid-market Microsoft 365 / hybrid identity admins who run Entra Connect or Entra Cloud Sync without a dedicated identity engineering team.

## MVP

- Read a sanitized `CSExportAnalyzer` CSV or fixture-format pending-export file.
- Read a small YAML readiness checklist for threshold and break-glass facts.
- Classify pending deletes/disables by object type, privileged/admin-looking accounts, and cloud-only emergency access coverage.
- Render a deterministic markdown/HTML packet with blast radius, go/no-go banner, review questions, rollback prompts, and safe next steps.
- Redact tenant names, UPNs, domains, hostnames, and support-case details by default.

## Non-goals

- No live Microsoft Graph, tenant, Entra Connect, domain controller, or admin-center access in the first slice.
- No automated remediation or threshold-disabling commands.
- No replacement for Microsoft support, Entra Connect Health, backup/recovery suites, or formal change approval.
- No storage of production identity exports.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vn3inw/entra_connect_sync_appears_to_have/ | Fresh lockout incident: Entra Connect appears to have deleted/disabled users including Global Admins. |
| Microsoft Learn / Prevent accidental deletes | https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-prevent-accidental-deletes | Documents accidental-delete threshold, pending-export delete inspection, and warning event ID 116. |
| Microsoft Learn / Staging server | https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-staging-server | Documents staging mode and `csexport` / `CSExportAnalyzer` preview before export. |
| Microsoft Learn / Emergency access | https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access | Recommends two or more cloud-only emergency access accounts to reduce lockout impact. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only, consolidated in the 100-days master repo.
