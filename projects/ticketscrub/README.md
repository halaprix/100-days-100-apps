# TicketScrub

TicketScrub is a lightweight Jira draft-side PII and secret preflight. It warns users before they submit risky issue text, comments, or pasted email dumps, then suggests safer redactions without storing ticket contents.

## Problem

Jira tickets often receive customer emails, passwords, API keys, screenshots, IDs, health or financial context, and long forwarded threads. After the ticket is created, the data may already be stored, indexed, notified, and visible to broad project roles.

Full DLP platforms help, but small teams often need a low-friction first guardrail: catch obvious mistakes at draft time and teach users what to remove.

## Target user

- Jira Cloud and Jira Service Management admins.
- Security/compliance owners in small regulated teams.
- Helpdesk managers who want point-of-entry coaching instead of after-the-fact cleanup.

## MVP

- Browser extension content script for configured Jira sites and a local fixture form.
- Draft-time detectors for common PII and secrets.
- Inline warning panel with category, severity, and redaction suggestion.
- Admin policy JSON import/export.
- Optional Forge UI Modifications spike for supported Jira create/request views.
- Markdown audit report for a demo submission.

## Non-goals

- Replacing enterprise DLP, SIEM, CASB, or full compliance workflows.
- Uploading ticket contents to a hosted classifier by default.
- Promising perfect PII detection or legal compliance.
- Supporting every Jira UI variant in the first prototype.

## Source evidence

- Fresh r/sysadmin thread: <https://www.reddit.com/r/sysadmin/comments/1uys0ua/how_do_you_stop_users_from_accidentally_adding/>
- Atlassian Forge UI Modifications: <https://developer.atlassian.com/platform/forge/understanding-ui-modifications/>
- miniOrange Jira PII scanner: <https://marketplace.atlassian.com/apps/1235792/data-pii-scanner-dlp-for-jira>
- Polymetis PII Protection and DLP for Jira: <https://marketplace.atlassian.com/apps/1225698/pii-protection-and-dlp-for-jira>
- Nightfall Jira DLP guide: <https://www.nightfall.ai/guide/the-essential-guide-to-data-loss-prevention-dlp-jira>

## Current status

Scaffold only. Next step: build a local extension/fixture prototype that blocks a synthetic Jira submit and exports a redaction report.
