# Day 037 — CampaignPacket

Date: 2026-07-26
Status: repo-created

## One-line pitch

Local-first CLI that prepares Microsoft Teams SMS / 10DLC campaign approval packets before small-business admins burn weeks on vague carrier rejection codes.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v68o5k/losing_my_mind_teams_phone_w_calling_plan_cannot/ | Fresh admin/attorney says Teams Phone SMS is business-critical, the campaign keeps getting rejected with `CallToActionInvalidOrIncomplete`, and the situation is embarrassing. |
| Microsoft Learn | https://learn.microsoft.com/en-us/microsoftteams/sms-setup-campaign | Teams SMS campaign registration requires detailed campaign description, target audience, opt-in/out, sample messages, privacy policy, terms, and compliance details; approval outcome depends on accuracy and completeness. |
| Microsoft Learn | https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/phone-system/sms-calling-errors | Microsoft lists many rejection codes and says `CallToActionInvalidOrIncomplete` requires brand name, HELP, STOP, message frequency, fees, and privacy-policy elements. |
| Princeton IT Services | https://princetonits.com/blog/microsoft-teams-collaboration-tools/configuring-sms-on-microsoft-teams-calling-plan-numbers/ | Recent Teams SMS guide frames 10DLC registration as compliance preparation, not just toggling SMS on a Teams number. |
| Microsoft 365 Message Center mirror | https://mc.merill.net/message/MC1134740 | Microsoft is adding clearer rejection handling and customer-update flows, showing campaign approval friction is active enough to warrant product changes. |

## Problem

Microsoft Teams SMS for Calling Plan numbers requires Brand and Campaign approval before administrators can enable texting. The campaign form asks for opt-in flow, privacy policy, terms, HELP/STOP language, message frequency, sample messages, and use-case limits. When one field is incomplete, the rejection code can be broad, the approval loop can take weeks, and SMB admins may not know what evidence to collect before resubmitting.

The current debugging loop is bad enough to matter: the admin reads long docs, copies examples into a doc, asks Reddit or an MSP, resubmits, and waits. For law firms, clinics, trades, and service businesses, delayed client SMS can block a Teams Phone migration, fragment customer communication, or create public embarrassment.

## Target user

Small-business Microsoft Teams Phone admins, law/healthcare/professional-service owners, and MSP technicians enabling low-volume one-to-one SMS on Teams Calling Plan numbers in the US or Canada.

## MVP scope

- `campaignpacket check --fixture rejected-cta` demo mode with synthetic Teams campaign fields.
- `campaignpacket check campaign.yaml --format markdown,json` for local preflight checks.
- Rules for CTA, brand-name consistency, opt-in method, HELP/STOP instructions, message frequency, fees disclosure, privacy policy, terms, sample message alignment, and Teams UCaaS low-volume limitations.
- Markdown/JSON missing-fields report plus a resubmission packet the admin can review before pasting into Teams Admin Center.
- Redaction guard for phone numbers, addresses, client names, and private business data in shared reports.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| CampaignPacket | Small-business Teams Phone admins and MSPs → Microsoft docs, Teams Admin Center, MSP advice, 10DLC provider help centers → authoritative info is scattered and rejected campaigns can take weeks to correct → offline Teams-SMS-specific packet checker for CTA/privacy/terms/HELP/STOP/sample-message fields → search/reply strategy for exact rejection phrases plus r/sysadmin/Microsoft Teams admin communities/MSP blogs → Teams SMS rollout and new rejection-handling docs make the pain timely | Pass; scored as winner. |
| SAML Support Packet | Enterprise IT support staff collecting SSO traces from nontechnical users → SAML-tracer, Auth Inspector, Microsoft/Twilio support docs → capture tools exist, but user handoff/redaction is still painful → guided support packet that validates required trace artifacts without becoming another tracer → r/sysadmin replies, IdP/SaaS support docs, Chrome extension search → fresh r/sysadmin feedback request confirms the workflow pain | Held: strong pain, but direct browser-extension competitors are established and the wedge overlaps a crowded extension surface. |
| HomeDrop Map | Self-hosted families uploading phone files to a home server → Nextcloud auto-upload, Syncthing, Immich, SMB/WebDAV apps → generic sync works but folder routing for nontechnical family members is confusing → tiny upload portal with per-person/date/type routing map and rollback → r/selfhosted replies/search pages for phone-to-server uploads → fresh r/selfhosted request asks for idiot-proof remote upload and auto-sort | Rejected: useful but substitutes are mature; wedge risks becoming another file-sync app. |
| AgentLeash | Solo SaaS builders using coding agents in the background → manual supervision, terminal notifications, agent dashboards → long tasks get stuck on questions or solve the wrong version of the problem → stop-at-decision-point wrapper with checkpoints and resumable prompts → AI-builder communities and agent CLI users → fresh r/SaaS post asks whether agents really free time if watched constantly | Held: real itch, but category is crowded and distribution would be generic unless tied to one agent runtime. |
| SlackAnswer Capture | Sysadmins losing solved answers in Slack threads → Slack search, pins, Canvas, Workflow Builder, Notion, knowledge bots → answers disappear after conversation moves on → emoji-triggered problem/solution capture with slash-command recall → r/sysadmin/Slack admin communities → fresh update says multiple teams share the pain | Held: pain is validated, but the source poster is already building the same wedge and Slack app distribution is slower than today's CLI. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Teams Admin Center and Microsoft Learn | Authoritative, but the workflow spans setup docs, rejection tables, templates, and status flows. It does not produce a reusable pre-submission packet. |
| Direct competitor | MSP / telecom consultant 10DLC help | Strong for paid deployments, but overkill for solo firms and small offices trying to fix one rejected campaign. |
| Direct competitor | 10DLC provider help centers such as JustCall, RingLogix, TextUs, CallHub, SkySwitch | Useful checklists, but usually written for their own SMS platforms rather than Teams UCaaS low-volume one-to-one SMS fields. |
| Indirect substitute | Copy Microsoft examples into a document, ask Reddit, resubmit repeatedly | Free but slow and brittle; one missing HELP/STOP/privacy/terms clause can restart a multi-week loop. |
| Status quo | Keep the campaign rejected, use Grasshopper or another SMS product outside Teams, or abandon Teams SMS | Keeps client texting fragmented and can block a Microsoft Teams Phone migration. |

## Wedge

CampaignPacket should stay narrow: not a CPaaS sender, not SMS marketing, not legal advice, and not Teams Admin Center automation. The wedge is a Microsoft Teams SMS campaign packet preflight that checks exactly the fields admins paste into the Teams flow and maps missing parts to documented rejection codes.

The first-user path is concrete: publish examples for `CallToActionInvalidOrIncomplete`, `Teams SMS campaign rejected`, and `10DLC Teams Calling Plan SMS`; answer public r/sysadmin / Microsoft Teams community support threads with synthetic packets; and give MSPs a copy/paste checklist they can use before filing support cases.

## Kill condition

Narrow or reject if Microsoft ships a built-in pre-submission validator that catches CTA/privacy/terms/sample-message omissions before submission, or if admins report that rejection turnaround becomes short enough that a local preflight packet no longer saves material time.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Rejections can delay business-critical SMS, block Teams Phone migration, and create public embarrassment; the workaround can easily exceed 30 minutes and may take weeks of elapsed time. |
| Feasibility | 5/5 | MVP is deterministic rule checks over local YAML/JSON plus Markdown/JSON output; no private API is required. |
| Demo potential | 4/5 | Synthetic rejected campaign → highlighted missing CTA/HELP/STOP/privacy terms → fixed packet is easy to show in terminal screenshots. |
| Distribution | 4/5 | Specific communities and search phrases exist: r/sysadmin, Microsoft Teams admins, MSP blogs, Microsoft Q&A, and exact rejection-code SEO/reply strategy. |
| Competitive wedge / timing | 4/5 | Teams SMS campaign approval is current, Microsoft is updating rejection flows, and generic 10DLC checklists are not Teams-specific packet builders. |
| Total | 21/25 | Clears repo threshold and dimension gates. |

## Decision

Create the repo. CampaignPacket clears 18/25 with Distribution 4/5 and Competitive wedge/timing 4/5. Status is `repo-created` because the scaffold was created, pushed, verified, and tagged.

Repo: https://github.com/halaprix/campaignpacket

## Next build step

Implement `campaignpacket check --fixture rejected-cta` with synthetic Teams SMS campaign fields, rules for CTA/privacy/terms/HELP/STOP/sample-message omissions, Markdown/JSON output, and tests that prove shareable reports redact phone numbers, addresses, emails, and client names.

## Research access note

Reddit public JSON returned HTTP 403; the run used the `reddit-rss-fallback` path for r/sysadmin, r/selfhosted, r/SaaS, and r/androidapps where available. Some subreddit RSS calls returned HTTP 429, so I stopped looping and used web search/extraction for competitor checks. X `whoami` worked, but X search returned 401 Unauthorized, so X was not used as evidence.
