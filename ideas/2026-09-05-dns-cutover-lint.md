# Day 072 — DNSCutoverLint

Date: 2026-09-05
Status: idea-only

## One-line pitch

A local-first linter that turns a planned move away from a DNS-O-Matic-style
single-update endpoint into a redacted, reviewable DDNS cutover packet before a
home-service hostname goes stale.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS/direct-page fallback | https://www.reddit.com/r/selfhosted/comments/1w7c4c4/dnsomatic_shutting_down/ | A fresh self-hosted operator reports a 30-day DNS-O-Matic shutdown notice and asks how to update multiple domains. Replies recommend qdm12/ddns-updater, ddclient, and one-off scripts—evidence of a concrete replacement decision, not evidence of broad demand. |
| DNS-O-Matic product page | https://dnsomatic.com/ | DNS-O-Matic describes its job as distributing one dynamic-IP update to multiple chosen services through a common API. This clarifies the migration surface; the page fetched for this run does not itself announce a shutdown. |
| qdm12/ddns-updater | https://github.com/qdm12/ddns-updater | The established container updates A/AAAA records across multiple DNS providers and includes a DNS-resolution health check. It is a strong direct substitute. |
| ddclient documentation | https://ddclient.net/ | ddclient supports a wide range of dynamic-DNS services, 30+ documented protocols, environment-variable configuration, and several scheduler integrations. |
| Cloudflare documentation | https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/ | Cloudflare explicitly recommends automated dynamic record updates and points users to scripts or ddclient, confirming that a provider-specific updater is already a well-served path. |

## Problem

An operator who used one endpoint to fan a changing public IP out to several
hostnames may need to reassemble that setup under a new provider or updater.
The immediate failure mode is not a cosmetic migration: a stale hostname can
make a remotely used service unreachable until the operator discovers it.

The fresh report proves one timely replacement decision and the comments show
that the workaround is usually manual configuration of an existing tool. It
does **not** prove a recurring, >30-minute-per-week pain across a broad cohort.
The current pain is a one-time cutover with an outage risk, so this is a
validation bet rather than a build mandate.

## Target user

A self-hoster with several dynamic-DNS hostnames who is replacing a
single-update service and is willing to run an existing updater such as
qdm12/ddns-updater or ddclient.

## MVP scope

- Run locally against an operator-supplied, redacted YAML manifest; never
  import DNS-O-Matic accounts, call provider APIs, retain credentials, or
  update DNS records.
- Capture intended hostnames, record families, current public resolution,
  proposed target provider, selected updater, and scheduler/health-check plan.
- Lint for duplicate hostname ownership, missing A/AAAA intent, missing secret
  references, missing scheduler/health checks, and record resolution that does
  not match the stated intent.
- Generate a Markdown cutover packet and a reversible, redacted starter config
  for either ddns-updater or ddclient. Mark unsupported providers as manual
  review rather than guessing.
- Do not become a DDNS daemon, a DNS migration service, or a credential vault.

## Shortlist and wedge-first gate

1. **DNSCutoverLint — selected, idea-only.** Self-hoster replacing a
   single-update DDNS endpoint → qdm12/ddns-updater, ddclient, Cloudflare
   scripts, and handwritten jobs → they update and monitor records well, but
   leave an operator to reconstruct and review a multi-hostname cutover plan →
   credential-free lint/report for an explicit migration manifest → exact
   "DNS-O-Matic alternative", ddns-updater, and ddclient configuration searches
   plus the fresh r/selfhosted replacement thread → a reported 30-day notice
   creates a narrow time window. **Kill:** qdm12/ddns-updater or ddclient
   already produces the same cross-host intent, scheduler, and resolution
   preflight from a redacted manifest, or five affected operators complete the
   move safely in under 30 minutes without a review artifact.
2. **ArchivePair — rejected.** Family archivist digitizing tapes and photos →
   Immich, Jellyfin, PhotoPrism, and manual NAS folders → Immich and Jellyfin
   already compose through external libraries, and the fresh thread reports
   that running both is the cleanest setup → shared-library layout checker →
   family-archive/self-hosting searches → the thread itself supplies a workable
   substitute and no proof that layout planning is a recurring paid problem.
   **Kill:** tolerated setup process and mature media apps solve the serving
   job; do not score as a daily winner.
3. **AccessStack Reducer — rejected.** Homelab operator considering replacing
   reverse proxy, WAF, and identity services → Pangolin, authentik, Traefik,
   CrowdSec, and manual architecture review → Pangolin already presents
   integrated secure access while authentik provides extensive identity
   workflows → stack-consolidation recommender → self-hosted networking
   searches → the proposed MVP would make high-stakes security assertions from
   incomplete configuration and has no credible 1–3 day wedge. **Kill:**
   security-sensitive, crowded category with mature direct products.
4. **RefurbServerFit — rejected.** Prospective home-server buyer → vendor
   specifications, Quick Sync documentation, homelab advice, and capacity
   calculators → the source asks for a hardware purchase recommendation, and a
   generic chooser would depend on incomplete workload measurements → hardware
   fit calculator → refurbished-server searches → rejected by scope: this lab
   ships software bets, not hardware sourcing or shopping advice. **Kill:**
   physical-product / purchasing route is out of scope.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | qdm12/ddns-updater | A mature multi-provider DDNS container with a Web UI and DNS-resolution health check. It solves the ongoing update job; it materially weakens any claim that a new updater is needed. |
| Direct competitor | ddclient | Mature dynamic-DNS client with broad protocol support, scheduler integrations, and environment-variable secret handling. It solves the same ongoing record-update job. |
| Direct competitor | Cloudflare scripts/API | Cloudflare documents scripts and ddclient for updating dynamic records. A user who can standardize on Cloudflare may not need a migration helper at all. |
| Indirect substitute | A hand-written provider API script, Docker Compose file, and a manual DNS lookup | This is exactly the workaround suggested in the fresh thread. It is inexpensive but produces no standard, shareable cutover review. |
| Status quo | Keep DNS-O-Matic until the reported deadline, then configure an updater per provider and discover omissions from failed remote access | A stale record can block access, but this run has only one public account reporting the deadline and replacement question. |

## Wedge

DNSCutoverLint must **not** compete as another record updater. Its smallest
credible job is a static preflight: make an operator write down every hostname,
record family, updater, schedule, health-check, and current resolution before
switching. The output is a redacted review packet and starter configuration,
not another daemon with DNS credentials.

That distinction is weak. qdm12/ddns-updater already spans providers and checks
DNS resolution; ddclient already spans providers and integration routes. The
remaining gap—cross-host migration intent—is plausible but unproven and may be
better served by a checklist in either project.

## Kill condition

Reject the bet if either incumbent accepts an explicit desired-host manifest and
reports missing record families, scheduler/health gaps, and post-cutover
resolution without writing a custom config first. Also reject if five operators
who received the reported notice can complete a multi-host migration safely in
under 30 minutes and would not use a review packet.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | A stale remote hostname can be consequential, but evidence here is one timely, likely one-off migration rather than repeated weekly pain. |
| Feasibility | 5/5 | A local manifest parser, DNS resolution checks, rule set, and Markdown/config output fit a narrow CLI. |
| Demo potential | 4/5 | A before/after cutover packet can clearly show an omitted AAAA record or missing scheduler before it causes an outage. |
| Distribution | 4/5 | The first-user path is specific and repeatable for the narrow event: exact migration/configuration searches and the r/selfhosted replacement thread, with educational content comparing a preflight against manual setup. |
| Competitive wedge / timing | 2/5 | The timing is narrow and real for the report, but qdm12/ddns-updater, ddclient, and provider scripts already solve the core job. The proposed lint layer has not been independently demanded. |
| Total | 18/25 | The numeric threshold is met, but the competitive-wedge gate fails. |

## Decision

**idea-only.** DNSCutoverLint reaches 18/25, and distribution is sufficient for
a validation attempt, but its 2/5 competitive-wedge score is below the required
3/5 gate. No dedicated project repository was created. Building another DDNS
updater would be unjustified; the only defensible scope is a narrowly proven
migration preflight.

## Next build step

Find five operators who report an imminent or completed multi-host dynamic-DNS
move. Collect only redacted desired-state manifests, time their manual setup,
and compare the findings with qdm12/ddns-updater and ddclient. Promote only if
at least three manifests reveal a missing record family, unowned hostname, or
absent schedule/health check that neither incumbent exposes before execution.

## Source access caveats

The bundled `reddit-readonly` command was not discoverable in this environment,
so the documented public RSS/direct-page fallback was used. The r/selfhosted
feed and direct pages were accessible; contemporaneous r/sysadmin, r/webdev,
and r/SaaS feed requests failed in the fetch layer and were not retried. Reddit
public JSON engagement data was unavailable, so this brief makes no score,
volume, or consensus claim.

X account identity was reachable through `xurl`, but the read-only search probe
returned `402 credits depleted`; no X signal is used. Web search did not return
fresh Reddit fallback results, so evidence is limited to the accessible public
sources linked above.
