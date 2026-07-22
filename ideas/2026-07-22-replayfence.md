# Day 033 — ReplayFence

Date: 2026-07-22
Status: repo-created

## One-line pitch

Local-first webhook retry/idempotency chaos tests for small teams before duplicate deliveries make bots, billing, or integrations process the same event twice.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/webdev | https://www.reddit.com/r/webdev/comments/1v2snih/a_webhook_retry_from_a_third_party_broke_our/ | A developer described a third-party webhook retry bypassing single-use dedup logic, causing their bot to treat its own outbound message as a new inbound event. |
| Reddit r/webdev | https://www.reddit.com/r/webdev/comments/1v2q98j/whats_one_tool_your_team_adopted_that_actually/ | Fresh thread asks which dev tools actually stick; reliability/debugging tools are explicitly in scope. |
| Hookdeck comparison | https://hookdeck.com/webhooks/platforms/webhook-delivery-guarantees-comparison | Managed webhook services still expose at-least-once delivery; receivers must build idempotent handlers. |
| Stripe docs | https://docs.stripe.com/webhooks | Stripe tells webhook consumers to return 2xx quickly, handle duplicate events, retries, event ordering, and asynchronous processing. |
| GitHub docs | https://docs.github.com/en/webhooks/using-webhooks/handling-webhook-deliveries | GitHub documents local webhook forwarding and response-time requirements; webhook handlers need local testing before deployment. |
| X/Twitter | xurl search attempted | `xurl whoami` worked, but search returned 401 Unauthorized; no X search evidence used. |

## Problem

Webhook consumers are usually tested on the happy path: one provider sends one payload and the handler returns 200. Production delivery is messier. Providers retry, redeliver, timeout, send concurrent duplicates, or deliver related events out of order. Small teams often discover their idempotency mistake only after a bot replies to itself, a customer receives duplicate email, inventory updates twice, or billing/reconciliation drifts.

The painful workaround is manual: capture a payload, paste curl commands, hand-edit headers, retry in a dashboard, inspect logs, and guess whether the handler is truly idempotent. For teams with payments, bots, CRM sync, or marketplace events, a missed duplicate can cause public embarrassment or lost money.

## Target user

Small SaaS and agency developers who receive third-party webhooks from Stripe, GitHub, Shopify, Slack/Discord bots, CRMs, or marketplaces, but do not want to adopt a full webhook gateway just to test receiver-side idempotency.

## MVP scope

- CLI command that reads a captured webhook payload plus headers from JSON files or stdin.
- Scenario presets: duplicate retry, concurrent retry, delayed retry, out-of-order pair, and malformed permanent-failure event.
- Local target runner that POSTs scenarios to `localhost`/staging and records status codes, latency, response bodies, and side-effect probes supplied by the user.
- Idempotency report: which deliveries produced duplicate side effects, inconsistent status codes, slow acknowledgements, or retry-hostile 4xx/5xx behavior.
- Provider notes for Stripe and GitHub headers/retry expectations; no live provider credentials required.

## Shortlist gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ReplayFence | Small SaaS webhook receiver → Hookdeck/Svix/ngrok/manual curl → platforms forward and replay but do not prove the app's own idempotency invariants → local retry-chaos packet with provider presets and side-effect probes → r/webdev, provider-webhook searches, dev-tool launch posts tied to duplicate webhook stories → at-least-once delivery is still the standard and AI/vibe-coded integrations are shipping more webhook handlers. | Winner; status-quo pain can cause money loss or public bot bugs. |
| DateTrap CI | JS app developers → Temporal/date-fns/Luxon/ESLint/manual review → libraries help after migration but do not find legacy `Date` production traps cheaply → static scanner for risky date parsing/math patterns → r/webdev/date bug posts and JS search traffic → Temporal adoption creates migration timing. | Useful, but broad lint/static-analysis space; saved as runner-up. |
| RenderProof | Small tool-site builders → Lighthouse/Screaming Frog/SSR checker extensions → full SEO tools are heavy and generic; users only need proof that public pages have indexable HTML → one-page CSR-vs-SSR packet for tool landing pages → small-tools/webdev SEO threads → more client-heavy app builders chasing organic traffic. | Rejected as too crowded; competitors already cover SSR/CSR checks. |
| SelectorDrift | Browser-extension maintainers → SelectorsHub/Playwright locators/visual regression/manual DOM inspection → tools serve QA automation more than extension breakage triage → watch saved selectors against daily DOM snapshots and suggest stable anchors → extension-maker posts and webdev selector complaints → class-name churn keeps breaking lightweight extensions. | Narrow but distribution weaker; also adjacent to generic browser-extension tooling. |
| DropboxScope Kit | Non-technical small-business builders → Dropbox docs/ChatGPT/manual OAuth experiments → docs explain scopes but not a safe app-folder integration packet → local checklist + generated OAuth scope plan → webdev no-code/vibe-code security questions → vibe-coded internal tools now wire cloud storage directly. | Useful but similar to generic secure-integration checklist; no repo. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Hookdeck, Svix, webhook.site, Webhook Relay, ngrok, Stripe CLI | Excellent for forwarding, inspecting, replaying, and operating webhooks. They do not focus on a local assertion harness that proves the receiver's idempotency and side-effect invariants across retry chaos scenarios. |
| Indirect substitute | Manual curl scripts, provider dashboard redelivery buttons, queue/DLQ dashboards, app logs, Postman collections | Works for senior teams, but brittle and often not repeatable in CI. The Reddit example is exactly the kind of single-use dedup bug manual testing misses. |
| Status quo | Ship after one successful delivery test; debug duplicate behavior after production incidents | Tolerable for hobby-only endpoints, not tolerable for payments, bots, customer emails, inventory, or CRM sync because failures create duplicated side effects. |
| Wedge | A tiny local-first CLI, not a hosted gateway: generate duplicate/concurrent/out-of-order deliveries and require explicit side-effect assertions before launch. | Can be built in 1-3 days with HTTP replay, fixture files, and simple assertion hooks. Does not need provider credentials. |
| Kill condition | If Hookdeck/Svix/Stripe CLI already offer local receiver-side idempotency assertion packs with CI-friendly side-effect probes, narrow to provider-specific fixtures or reject. | Current evidence shows strong platforms, but still room for a focused preflight harness. |

## Wedge

ReplayFence is not trying to replace webhook infrastructure. The wedge is a launch preflight for the receiver code itself: prove that duplicate/retry/out-of-order deliveries do not create duplicate side effects before connecting real customers or production providers. The first audience is reachable through concrete developer channels: reply/search around webhook duplicate incidents, publish provider-specific examples for Stripe/GitHub/Slack, and show a 30-second demo where a naive handler fails and the fixed handler passes.

## Kill condition

Reject or narrow if provider CLIs and managed webhook gateways already provide equivalent CI-friendly idempotency assertions with user-defined side-effect probes, or if initial demos cannot prove a failure that developers recognize as costly.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | Duplicate webhook processing can cause money loss, customer spam, bad bot loops, and reconciliation drift. |
| Feasibility | 4/5 | Core replay runner is straightforward; robust provider presets and side-effect probes need careful design. |
| Demo potential | 4/5 | Easy split-screen demo: naive handler processes twice, ReplayFence flags it, fixed handler passes. |
| Distribution | 4/5 | Specific communities and search paths: r/webdev webhook threads, provider webhook docs/search traffic, indie SaaS launch checklists. |
| Competitive wedge / timing | 4/5 | Strong incumbents exist, but they are platforms; the narrow local assertion/CI preflight wedge is distinct and timely. |
| Total | 21/25 | Clears repo threshold and both gates. |

## Decision

Create repo: `halaprix/replayfence`. Scaffold pushed and tagged `v0.1.0-alpha.1` after a CI smoke self-match fix.

Score is 21/25, with the weakest dimensions at 4/5: feasibility, demo potential, distribution, and competitive wedge. The idea clears the 18/25 threshold, the distribution gate, and the competitive-wedge/timing gate.

## Next build step

Implement `replayfence run --target http://localhost:3000/webhook --fixture fixtures/stripe-payment.json --scenario duplicate,retry,out-of-order` with a JSON report and one sample intentionally non-idempotent handler for the demo.
