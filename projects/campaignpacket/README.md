# CampaignPacket

Local-first CLI that prepares Microsoft Teams SMS / 10DLC campaign approval packets before small-business admins burn weeks on vague carrier rejection codes.

## Problem

Microsoft Teams SMS for Calling Plan numbers now requires Brand and Campaign approval before administrators can enable texting. The campaign form asks for opt-in flow, privacy policy, terms, HELP/STOP language, message frequency, sample messages, and use-case limits. When one field is incomplete, the rejection code can be broad, the approval loop can take weeks, and SMB admins may not know what evidence to collect before resubmitting.

The painful case is a business owner or part-time admin who needs compliant one-to-one client texting inside Teams but keeps getting `CallToActionInvalidOrIncomplete` or similar errors. The current workaround is reading long docs, copying examples, asking Reddit, or paying an MSP to translate 10DLC rules into the Teams Admin Center form.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v68o5k/losing_my_mind_teams_phone_w_calling_plan_cannot/ | Fresh admin/attorney says Teams Phone SMS is business-critical, the campaign keeps getting rejected with `CallToActionInvalidOrIncomplete`, and the situation is embarrassing. |
| Microsoft Learn | https://learn.microsoft.com/en-us/microsoftteams/sms-setup-campaign | Teams SMS campaign registration requires detailed campaign description, target audience, opt-in/out, sample messages, privacy policy, terms, and compliance details; approvals can affect timeline and outcome. |
| Microsoft Learn | https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/phone-system/sms-calling-errors | Microsoft lists many rejection codes and says `CallToActionInvalidOrIncomplete` requires brand name, HELP, STOP, frequency, fees, and privacy policy elements. |
| Princeton IT Services | https://princetonits.com/blog/microsoft-teams-collaboration-tools/configuring-sms-on-microsoft-teams-calling-plan-numbers/ | Recent Teams SMS guide frames 10DLC registration as a compliance-preparation step, not just a Teams toggle. |
| Microsoft 365 Message Center mirror | https://mc.merill.net/message/MC1134740 | Microsoft is adding clearer rejection handling and customer-update flows, showing campaign approval friction is active enough to warrant product changes. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Teams Admin Center and Microsoft Learn | Authoritative, but it is spread across setup docs, rejection tables, templates, and status flows. It does not create a reusable pre-submission packet for an SMB admin. |
| Direct competitor | MSP / telecom consultant 10DLC help | Strong for paid deployments, but overkill for solo firms and small offices trying to fix one rejected campaign. |
| Direct competitor | 10DLC provider help centers such as JustCall, RingLogix, TextUs, CallHub, SkySwitch | Useful checklists, but usually written for their own SMS platforms rather than Teams UCaaS low-volume one-to-one SMS fields. |
| Indirect substitute | Copy Microsoft examples into a document, ask Reddit, resubmit repeatedly | Free but slow and brittle; one missing HELP/STOP/privacy/terms clause can restart a multi-week loop. |
| Status quo | Keep the campaign rejected, use Grasshopper or another SMS product outside Teams, or abandon Teams SMS | Keeps client texting fragmented and can block a Microsoft Teams Phone migration. |

## Wedge

CampaignPacket is not a CPaaS sender, SMS marketing tool, or legal advice product. The wedge is a narrow Microsoft Teams SMS preflight packet: collect the exact fields a Teams admin must submit, check them against documented 10DLC rejection patterns, and emit a Markdown/PDF-ready packet with missing disclosures, sample HELP/STOP replies, and resubmission notes.

That is small enough for a 1–3 day MVP because it can run fully offline with fixture data and rule checks. It is also specific enough to distribute through searches and replies for exact phrases like `CallToActionInvalidOrIncomplete` and `Teams SMS campaign rejected`.

## Target user

Small-business Microsoft Teams Phone admins, law/healthcare/professional-service owners, and MSP technicians enabling low-volume one-to-one SMS on Teams Calling Plan numbers in the US or Canada.

## MVP

- `campaignpacket check --fixture rejected-cta` demo mode with synthetic Teams campaign fields.
- `campaignpacket check campaign.yaml --format markdown,json` for local preflight checks.
- Rules for CTA, brand-name consistency, opt-in method, HELP/STOP instructions, message frequency, fees disclosure, privacy policy, terms, sample message alignment, and Teams UCaaS low-volume limitations.
- Output a missing-fields report plus a resubmission packet the admin can review before pasting into Teams Admin Center.
- Redaction guard for phone numbers, addresses, client names, and private business data in shared reports.

## Non-goals

- Not sending SMS messages.
- Not bypassing Microsoft, carrier, or 10DLC review.
- Not providing legal advice or guaranteed approval.
- Not scraping or automating Teams Admin Center.
- Not storing private customer data or campaign submissions remotely.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
