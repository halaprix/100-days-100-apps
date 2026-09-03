# Day 070 — WebPushFit

Date: 2026-09-03
Status: idea-only

## One-line pitch

A local WordPress web-push preflight that checks whether a low-resource,
self-hosted deployment can accept a real browser subscription and send one
non-production test notification before a site owner exposes an opt-in prompt.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS fallback | https://www.reddit.com/r/selfhosted/comments/1w5zv4a/self_hosted_alternative_of_pushengage_one_signal/ | On September 3, a WordPress site owner asked for a self-hosted PushEngage/OneSignal alternative that could run on a 2 GB VPS and register browser opt-ins for new-post alerts. This is a single request, not proof of broad demand. |
| MDN — Push API | https://developer.mozilla.org/en-US/docs/Web/API/Push_API | First-party browser documentation says web push relies on an active service worker and a per-service-worker subscription containing an endpoint and encryption key; it also warns that the endpoint is a capability URL and calls out CSRF/XSRF protection. |
| Perfecty Push WP | https://github.com/perfectyorg/perfecty-push-wp | A maintained open-source WordPress plugin already sends web push directly from a WordPress server without a third-party dependency. It is strong evidence that delivery itself is not whitespace. |
| WordPress.org — PushEngage | https://wordpress.org/plugins/pushengage/ | The category is mature: PushEngage offers browser push, automatic post alerts, segmentation, and WooCommerce workflows from WordPress. |

## Problem

A small WordPress publisher who wants browser alerts without another hosted
provider has to join together service-worker scope, HTTPS, VAPID keys,
subscription storage, WordPress hooks, and the practical resource ceiling of a
small VPS. The visible failure comes late: an opt-in prompt appears but a real
subscriber does not receive a post alert.

The fresh report describes a constrained deployment decision rather than a
request for another campaign dashboard. A preflight could prevent a launch or
subscriber-trust failure, but there is only one fresh buyer report and existing
self-hosted plugins may already be good enough.

## Target user

A WordPress publisher or small site operator who wants self-hosted browser push
for new-post alerts and is deliberately operating on a small VPS.

## MVP scope

- Run locally against a user-supplied staging URL and optional WordPress/plugin
  configuration export; never collect subscribers, send campaigns, or retain
  credentials.
- Check HTTPS, service-worker URL and scope, manifest references, VAPID public
  key shape, subscription endpoint origin, and whether configured endpoints are
  reachable.
- Provide a browser fixture page that creates one disposable opt-in and records
  a non-production delivery attempt as pass, fail, or inconclusive.
- Estimate only the tool's own probe footprint; do not claim to certify server
  capacity or browser delivery guarantees.
- Emit a Markdown/JSON packet with reproducible findings and links to native
  browser and plugin configuration documentation.

## Shortlist and wedge-first gate

1. **WebPushFit — selected, idea-only.** WordPress publisher on a 2 GB VPS →
   PushEngage, Perfecty Push WP, Push Notifications for WP, and manual browser
   DevTools checks → mature plugins deliver and automate notifications but do
   not establish that every site-specific service-worker/subscription path is
   ready before a public opt-in → local staging-only readiness packet with one
   disposable subscription test → exact WordPress/self-hosted push searches,
   plugin support forums, and hosting-constraint content → a fresh request
   explicitly combines self-hosting, WordPress, browser opt-in, and a 2 GB
   server. **Kill:** a maintained plugin already produces an equivalent
   staging-ready service-worker, subscription, and delivery proof, or five
   target users report that manual verification takes under 30 minutes and has
   never blocked an alert launch.
2. **GalleryReindex — rejected.** Android user trying to find and move objects
   in a stale/recent gallery folder → Google Photos, OEM galleries, Aves, and
   local ML gallery apps → the reported freshness problem is specific to one
   product and mature gallery/search apps already address the broad job → local
   media-index health check → Android-app searches → no proof of a repeatable
   developer or operator pain. **Kill:** crowded consumer gallery category and
   no concrete first-user channel.
3. **ZoomAudioCapture — rejected.** Android tablet user recording a Zoom meeting
   with audio → built-in recorder, screen-recording apps, and Zoom settings →
   the missing audio is described as Zoom's privacy restriction, so a third-party
   recorder cannot honestly promise to bypass it → policy explainer only →
   Android support discussions → no viable software wedge without encouraging a
   privacy-control bypass. **Kill:** platform restriction, not an underserved
   workflow.
4. **MailCostRoute — rejected.** Owner of several custom domains paying for
   email → hosted mail providers, Cloudflare Email Routing, and self-hosted mail
   stacks → the fresh item is a builder's product announcement, not independent
   evidence of a repeated buyer problem; running outbound mail remains an
   operationally heavy category → cost/route planner → Cloudflare-email searches
   → no validated status-quo cost beyond one promotional claim. **Kill:** weak,
   non-independent demand evidence.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Perfecty Push WP | Open-source, self-hosted WordPress web-push delivery with no third-party dependency. Its existence sharply narrows the bet to preflight evidence rather than sending notifications. |
| Direct competitor | Push Notifications for WP | WordPress.org plugin that advertises self-hosted web push, automatic post/update notifications, a dashboard, and reporting. It may already cover enough setup feedback to kill the product. |
| Direct competitor | PushEngage | Mature hosted WordPress push product with post automation, segmentation, and WooCommerce workflows. It solves the job for users willing to use a provider. |
| Indirect substitute | Browser DevTools, service-worker inspectors, plugin docs, and a staging site | Operators can manually inspect registrations and send a test; the drawback is scattered evidence and no reusable handoff packet. |
| Status quo | Install a plugin, enable a public opt-in, and learn from missed notifications | This can block an alert launch or create a visible subscriber-trust failure, but the real time cost and frequency remain unmeasured. |

## Wedge

WebPushFit would not be another sender, subscriber database, or marketing
console. Its narrow job is a credential-free, staging-only proof of the browser
path before the public prompt goes live. The output could be attached to a site
handoff or change review, while existing plugins remain responsible for delivery.

That is not yet a sufficient wedge. Self-hosted plugins already market quick
setup and native campaign dashboards, and the only direct demand evidence is one
fresh question. This is deliberately held until a plugin audit and interviews
show that the setup-to-delivery proof is routinely missing.

## Kill condition

Reject the bet if Perfecty Push WP, Push Notifications for WP, or another
maintained WordPress push plugin can already generate a comparable staging proof
covering service-worker scope, a disposable subscription, and a delivery result.
Also reject if five small WordPress operators say manual checks take less than
30 minutes per launch and missed push delivery has not delayed a launch, lost
traffic, or caused subscriber complaints.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A failed opt-in path can block a notification launch and erode subscriber trust, but direct evidence is one fresh report. |
| Feasibility | 4/5 | Static checks plus a disposable browser fixture fit a small local tool; cross-browser delivery makes absolute certification out of scope. |
| Demo potential | 5/5 | A staging page can visibly move from bad scope/VAPID configuration to a clear readiness packet with a recorded test result. |
| Distribution | 3/5 | Exact WordPress/self-hosted-push and small-VPS searches plus plugin support forums are concrete, but no repeatable first-user channel is proved. |
| Competitive wedge / timing | 2/5 | Existing self-hosted plugins solve most of the job; the preflight distinction is plausible but unvalidated and has no platform deadline. |
| Total | 18/25 | Total clears the numeric threshold, but both required dimension gates fail. |

## Decision

**idea-only.** WebPushFit reaches 18/25 but fails the repo gates: Distribution is
3/5 (minimum 4) and Competitive wedge / timing is 2/5 (minimum 3). No dedicated
project repository was created. The correct next move is validation, not a
scaffold.

## Next build step

Audit the setup/test flows of Perfecty Push WP and Push Notifications for WP,
then interview five WordPress operators who run browser push on constrained
hosting; promote only if their native/plugin flow cannot produce a staging
subscription-and-delivery proof and the workaround has caused a launch or
subscriber-trust failure.

## Source access caveats

Reddit public JSON was blocked. RSS fallback supplied fresh posts for
r/selfhosted and r/androidapps; r/SaaS, r/startups, r/webdev, and r/sysadmin
returned HTTP 429 in this run and were not retried. RSS does not expose reliable
scores or comment context, so this brief does not claim engagement or consensus.

X `xurl` could read the account identity but the default app had no OAuth 2
credential and the read-only search probe returned `401 Unauthorized`. No X
signal is used. Web research was used for competitor and platform-documentation
validation.
