# ReplayFence

Local-first webhook retry/idempotency chaos tests for small teams before duplicate deliveries make bots, billing, or integrations process the same event twice.

## Problem

Webhook consumers are often tested once on the happy path. Production delivery is at-least-once: providers retry, redeliver, timeout, send concurrent duplicates, and sometimes deliver related events out of order. A naive handler can send duplicate emails, double-process an order, create a bot loop, or drift customer/account state.

The usual workaround is manual curl scripts, provider dashboard redelivery, and log inspection. That is not repeatable enough for small teams shipping payment, bot, CRM, or marketplace integrations.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/webdev | https://www.reddit.com/r/webdev/comments/1v2snih/a_webhook_retry_from_a_third_party_broke_our/ | A third-party webhook retry bypassed single-use dedup logic and caused a bot to treat its own outbound message as new inbound input. |
| Hookdeck comparison | https://hookdeck.com/webhooks/platforms/webhook-delivery-guarantees-comparison | Managed webhook services still expose at-least-once delivery; receivers must build idempotent handlers. |
| Stripe docs | https://docs.stripe.com/webhooks | Stripe documents duplicate handling, retries, ordering, fast 2xx responses, and asynchronous processing. |
| GitHub docs | https://docs.github.com/en/webhooks/using-webhooks/handling-webhook-deliveries | GitHub documents local webhook forwarding and handler response requirements. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Hookdeck, Svix, webhook.site, Webhook Relay, ngrok, Stripe CLI | Strong forwarding/inspection/replay tools, but not a focused local assertion harness for receiver-side idempotency. |
| Indirect substitute | Manual curl scripts, Postman collections, provider dashboard redelivery, queue/DLQ dashboards, app logs | Flexible but brittle, hard to repeat in CI, and easy to forget until a production duplicate appears. |
| Status quo | Test one successful delivery and debug retries after launch | Risky for payments, bots, customer emails, inventory, and CRM sync. |

## Wedge

ReplayFence is not a hosted webhook gateway. It is a launch preflight for receiver code: replay captured payloads under duplicate, retry, concurrent, delayed, malformed, and out-of-order scenarios, then require explicit side-effect assertions before production launch.

## Target user

Small SaaS and agency developers receiving third-party webhooks from Stripe, GitHub, Shopify, Slack/Discord, CRMs, or marketplaces without a dedicated reliability platform.

## MVP

- CLI reads webhook payload/header fixtures from JSON or stdin.
- Scenario presets for duplicate, concurrent retry, delayed retry, out-of-order pair, and permanent-failure event.
- POST runner targets localhost or staging and records status codes, latency, response bodies, and retries.
- User-supplied side-effect probes check whether state changed more than once.
- JSON/Markdown report suitable for CI artifacts and launch checklists.

## Non-goals

- Not a hosted webhook gateway.
- Not a replacement for Hookdeck, Svix, ngrok, or provider dashboards.
- No live provider credentials in the MVP.
- No production event storage service in the MVP.

## Status

v0.1.0-alpha.1 — scaffold/spec only; CI smoke self-match fixed.
