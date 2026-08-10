# Day 050 — WeatherFork

Date: 2026-08-10
Status: repo-created
Repo: [`projects/weatherfork`](../projects/weatherfork)

## One-line pitch

WeatherFork is a local-first Ecowitt upload relay that keeps Home Assistant fed while storing durable weather history and rendering last-year-vs-this-year comparison views.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vk6fmv/weather_station_data_storage_and_comparison/ | Fresh post from an Ecowitt owner asking for a dashboard alongside Home Assistant that stores data "forever," supports last-year-vs-this-year comparisons, and can relay because Ecowitt appears to send to a single custom endpoint. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1dccewx/api_repeater_endpoint_replicator/ | Older matching workaround request: duplicate an Ecowitt/custom-endpoint payload to multiple Home Assistant instances for weather comparison; suggested substitutes were Caddy glue, RabbitMQ, Node-RED, shared MQTT, webhook.site, and n8n. |
| Home Assistant docs | https://www.home-assistant.io/integrations/ecowitt/ | Home Assistant's Ecowitt integration works by creating a callback endpoint that the Ecowitt console sends data to; this validates the one-endpoint plumbing constraint. |
| Home Assistant Community | https://community.home-assistant.io/t/ecowitt2mqtt-send-data-from-an-ecowitt-device-to-mqtt/231169 | ecowitt2mqtt has long-running community demand for local Ecowitt data outside cloud APIs and into MQTT/Home Assistant. |
| WeeWX | https://weewx.com/ | Mature open-source weather-station software already covers graphing, reports, databases, upload targets, and extensibility; the wedge must avoid trying to replace it. |

## Problem

Self-hosted weather-station owners want three things at once: Home Assistant automations, durable local history, and human-friendly seasonal comparisons. The current substitute path makes them stitch together Home Assistant, WeeWX, MQTT bridges, Node-RED/n8n, or custom scripts. That is tolerable for one-off tinkering, but bad enough when changing the upload endpoint risks losing weather history or breaking automations the household already depends on.

## Target user

Home Assistant users with Ecowitt-compatible weather stations who want durable local history and comparison dashboards without running a full weather-site stack or hand-building webhook relays.

## MVP scope

- HTTP endpoint that accepts Ecowitt-compatible form or JSON payloads.
- Normalize common weather fields and store samples locally before forwarding.
- Forward the original or normalized payload to one or more configured sinks, including a Home Assistant callback endpoint.
- Static report showing current readings, upload gaps, and last-year-vs-this-year overlays from fixture data.
- Dry-run command that reads a captured/synthetic payload and prints what would be stored and forwarded.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | WeeWX | Strong incumbent for weather-station archiving, reports, HTML pages, uploads, skins, SQLite/MySQL, and extensibility. WeatherFork should not compete as a full weather-station platform. |
| Direct competitor | ecowitt2mqtt / Ecowitt MQTT Bridge add-ons | Good for feeding Ecowitt data into MQTT/Home Assistant discovery. They do not appear positioned as a single-purpose archive + multi-sink relay + year-over-year comparison packet. |
| Indirect substitute | Home Assistant long-term statistics and dashboards | Already present for the target user, but relay/fan-out plus comparison reporting is not a simple first-class workflow. |
| Indirect substitute | Node-RED, n8n, Caddy, RabbitMQ, shared MQTT, custom script | Flexible and often suggested, but they turn a weather-station owner into an integration maintainer. |
| Status quo | Pick one receiver, then glue the rest | Users either make Home Assistant the receiver and lose easy long-term weather reports, or add WeeWX/MQTT glue and risk brittle plumbing. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| WeatherFork | Home Assistant + Ecowitt owners → WeeWX/Home Assistant/ecowitt2mqtt/Node-RED → each solves only archive, automation, or relay separately → Ecowitt-shaped store-first relay with seasonal comparison → r/selfhosted, Home Assistant Community, Ecowitt/WeeWX search content → fresh one-endpoint relay + comparison request repeated by older thread | Winner; clear narrow workflow and distribution. |
| AlertQuiet | Small-team sysadmins clearing noisy security alerts → SIEM/SOAR suppression rules and ticket queues → too heavy or risky for teams without a tuned SOC → local recurring-alert evidence pack that separates known noise from novel alerts → r/sysadmin alert-fatigue threads and small-business security checklists → fresh post about closing repeated false positives | Rejected for today: crowded security-alert tooling and wedge risks becoming another generic security dashboard. |
| VpsHardening Packet | New self-hosters exposing VPS/WireGuard/Cloudflare Tunnel services → generic hardening guides → advice is fragmented and unsafe to paste blindly → read-only local checklist packet for common VPS exposure mistakes → r/selfhosted questions and guide searches → fresh VPS security thread | Held: useful, but too close to generic hardening checklist unless tied to one stack. |
| LicenseLift | On-prem admins facing VMware/hardware price hikes → spreadsheets, reseller quotes, migration calculators → hard to compare pause/renew/migrate scenarios under maintenance constraints → quote-normalized scenario packet for small on-prem estates → r/sysadmin VMware price-hike discussions and search traffic → ongoing Broadcom/VMware pricing pressure | Held: strong pain, but first MVP needs better current competitor and pricing evidence. |

## Wedge

WeatherFork can win only by being narrower than every substitute: one Ecowitt-shaped endpoint that stores first, fans out second, and produces comparison views immediately. The wedge is not "better weather software"; it is fewer moving pieces for a specific Home Assistant + Ecowitt workflow.

## Kill condition

Reject or narrow if a maintained WeeWX extension, Home Assistant add-on, or Ecowitt bridge already provides store-first multi-sink relay plus last-year-vs-this-year views in under 15 minutes of setup. Also reject if fresh users only want generic charts and do not care about preserving the Home Assistant feed.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The workaround can burn a weekend and risks losing data or breaking automations, but it is not usually a compliance or revenue problem. |
| Feasibility | 4/5 | A 1-3 day MVP can be a small Python HTTP receiver, local archive, forwarder, and static report using synthetic fixtures. |
| Demo potential | 4/5 | Easy to show: point fixture payload at the endpoint, forward to a test sink, then render seasonal comparison and gap report. |
| Distribution | 4/5 | Specific communities and search paths exist: r/selfhosted, Home Assistant Community, Ecowitt/WeeWX/MQTT queries, and how-to content around one-endpoint relay. |
| Competitive wedge / timing | 3/5 | Competitors are real and mature, especially WeeWX. The credible wedge is the narrow relay/archive/comparison workflow rather than full platform breadth. |
| Total | 19/25 | Clears repo threshold and both dimension gates. |

## Decision

Create repo. WeatherFork scored 19/25 with distribution 4/5 and competitive wedge/timing 3/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/weatherfork`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Implement `weatherfork ingest --fixture examples/ecowitt-sample.json` to normalize a synthetic Ecowitt payload, write one local archive record, and render the first static comparison JSON/HTML artifact.

## Source access caveats

Reddit public JSON was blocked by `HTTP 403 theme-beta`, so r/selfhosted and r/sysadmin collection used the skill's Reddit RSS fallback. Some other subreddit RSS probes returned `HTTP 429`, so web search and direct web extraction were used as fallback. X/Twitter was read-only and not used for search because `xurl auth status` showed no OAuth2 user on the default app; no social writes were attempted.
