# Day 003 — HumanMark

Date: 2026-06-21
Status: idea-only

## One-line pitch

A tiny log-import tool that estimates "real human visitor" confidence from Cloudflare/server logs, explains the uncertainty, and suggests concrete bot-filtering fixes.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1ubdwug/how_do_i_count_how_many_real_human_visitors_my/ | Fresh webdev thread asking how to count real human visitors; commenters converge on "you can't know perfectly" because GA, Cloudflare, ad blockers, bots, AI agents, crawlers, and scanners all distort counts. |
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1ubigm6/whats_the_most_repetitive_thing_you_do_on_your/ | Same day's webdev signal: small repeated workflow annoyances and manual data cleanup are accepted until someone scripts them. HumanMark should be a scriptable audit, not another analytics dashboard. |
| Competitor check / Plausible | https://plausible.io/ | Privacy-first analytics is a crowded category; HumanMark cannot win as another generic analytics product. |
| Competitor check / Pravaxio | https://pravax.io/ | Some analytics tools already claim bot detection and human/bot scoring. The wedge must be narrower: one-off confidence report from existing logs. |
| Competitor check / Moonito | https://moonito.net/features/smart-analytics | "Bot-free analytics" positioning already exists; this reduces novelty and keeps the idea below repo threshold today. |

## Problem

Small site owners and developers want to know whether their traffic is real, but the modern web makes visitor counts ambiguous. Client-side analytics miss ad-blocked users, CDN analytics include bot traffic, raw logs are noisy, and AI crawlers/security scanners inflate numbers. The honest answer is not "exact visitors" but "confidence bands plus why this count is uncertain."

## Target user

Indie developers, small SaaS founders, newsletter operators, and web developers running low-to-medium traffic sites who already have Cloudflare, Vercel, Netlify, nginx, or Apache logs and do not want to install a full analytics suite just to answer: "Were these visits humans?"

## MVP scope

- CLI-first or single-page local web app.
- Import Cloudflare CSV/log export, Vercel/Netlify request logs, or nginx combined logs.
- Classify traffic with transparent heuristics: user-agent category, ASN/cloud-hosting hints, known crawler paths, burst patterns, missing asset behavior, and honeypot hits.
- Output a report: human-confidence range, top suspicious traffic sources, actionable fixes, and "do not overclaim" caveats.
- Generate optional uBlock-style or server-rule snippets for honeypot paths and common scanner traps.
- No persistent tracking script, no cookies, no hosted analytics database in v1.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Plausible, Fathom, Cloudflare Web Analytics | Mature analytics products; they are better if the user wants ongoing dashboards. HumanMark should not compete there. |
| Direct competitor | Pravaxio, Moonito | Already position around bot filtering / real-human analytics, so a generic "bot-free analytics" pitch is weak. |
| Indirect substitute | GA4 + Cloudflare + manual spreadsheet cleanup | Common but gives conflicting answers; the pain is reconciling the numbers. |
| Indirect substitute | Server log scripts, GoAccess, AWStats, custom Python notebooks | Good for technical users but usually report visits, not uncertainty/explainable human confidence. |
| Status quo | Ignore raw visitor count and track CTA/sign-up events only | This is often the right advice, but early projects still need a sanity check on whether traffic is fake. |
| Wedge | A one-off, local-first "traffic confidence audit" that imports logs the user already has and says what can/cannot be known. No tracking script, no dashboard migration, no privacy/legal surface. |
| Kill condition | If Cloudflare/Plausible/Fathom ship a simple exported-log human-confidence report with transparent bot heuristics, HumanMark loses its wedge. |

## Wedge

The wedge is **honest uncertainty, not perfect analytics**. Existing tools sell dashboards or bot-free tracking. HumanMark would sell a lightweight audit: import logs, get a confidence band, see the reasons, and apply fixes. That is demoable in a 30-second before/after report and can be built without asking users to replace their analytics stack.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The pain is real and timely: bots, AI crawlers, ad blockers, and privacy tooling make visitor counts less trustworthy. |
| Feasibility | 4/5 | Log parsing plus transparent heuristics is buildable in 1-3 days for one or two formats. |
| Demo potential | 4/5 | Strong demo: noisy log file in, human-confidence report and suspicious sources out. |
| Distribution | 3/5 | r/webdev, self-hosted communities, indie-hacker analytics debates, and privacy-first analytics users are reachable. |
| Competitive wedge / timing | 2/5 | Crowded analytics/bot-detection space; Pravaxio and Moonito already claim human/bot scoring. Narrow audit wedge is credible but not strong enough yet. |
| Total | 17/25 | Useful idea, but below repo-creation threshold because competition is heavy and today's public demand signal is one strong thread, not repeated demand. |

## Decision

**Save as idea-only.** HumanMark is the best daily idea because it turns a fresh, concrete r/webdev pain into a buildable tool with a narrow wedge. It does **not** clear the 18/25 repo threshold today: the category is crowded, and direct competitors already market bot-filtered analytics.

Create a repo only if one of these happens:

1. another fresh thread asks for log-based human/bot traffic reconciliation,
2. a developer explicitly wants a one-off audit rather than a dashboard, or
3. a quick spike proves the report is unusually compelling from public sample logs.

## Shortlist considered

| Idea | Source signal | Competitor / substitute gate | Score | Decision |
|---|---|---|---:|---|
| HumanMark — real-human visitor confidence audit | r/webdev human-visitor counting thread | Plausible/Fathom/Cloudflare plus Pravaxio/Moonito crowd the analytics category; narrow log-audit wedge survives. | 17/25 | Winner, idea-only. |
| FocusSlot — Pomodoro sessions tied to Google Calendar events | r/productivity asks for Google Calendar sync + event-level Pomodoro | TickTick, Toggl Track, FocusCommit, and a Chrome extension for Google Calendar Pomodoro already exist. Wedge would need event-level time writeback and ultra-light setup. | 16/25 | Hold. Useful but likely solved enough. |
| FilterForge — generated uBlock packs for intentional video use | r/productivity shares uBlock rules to make a streaming site less addictive | Unhook and many browser extensions already hide YouTube recommendations/Shorts. Wedge as copy-paste uBlock recipes is too thin. | 14/25 | Reject for now. |
| FrictionProof — validation checklist for real pain vs overthinking | r/SaaS founder asks how to validate pain | Many validation tools and templates exist; the best advice is customer conversations and commitments, not another app. | 13/25 | Reject. |
| CaseShiftlet — API JSON casing transformer | r/webdev repetitive-work thread mentions manual snake_case to camelCase cleanup | Online converters and npm packages like axios-case-converter already solve this directly. | 10/25 | Reject. |

## Next build step

Run a 2-hour spike before creating a repo: collect or synthesize a public-safe sample log, parse it locally, and produce a static HTML report with a confidence band, bot reasons, and recommended fixes. If the report is visually obvious and useful, rescore the idea.

## Research access note

Reddit public JSON/RSS access was partially throttled today: the `reddit-readonly` script used RSS fallback where available, and several subreddits returned HTTP 429. X search via `xurl` returned 401 even though `whoami` worked, so X was not used as evidence. Web search was used for competitor discovery and fallback validation.
