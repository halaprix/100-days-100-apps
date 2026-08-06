# Day 048 — RelayTrace

Date: 2026-08-06
Status: repo-created

## One-line pitch

A local-first SMTP forwarding and catch-all envelope probe that tells self-hosted mail admins whether their front relay preserved enough recipient evidence to route mail safely.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vgtyki/smtp_forwarding/ | Fresh self-hosted mail user describes ISP SMTP forwarding for a catch-all domain, with original recipients passed through an `X-Envelope` header, and asks for replacement patterns that keep the home server shielded while preserving per-address processing. |
| Swaks | https://www.jetmore.org/john/code/swaks/ | Mature SMTP probe tool confirms the test surface is scriptable, but it remains a generic SMTP transaction tool rather than a catch-all relay verdict packet. |
| MXToolbox SMTP Diagnostics | https://mxtoolbox.com/diagnostic.aspx | Online SMTP diagnostics test public server connectivity, open relay behavior, PTR, and response time, not private relay envelope-recipient preservation. |
| MXToolbox Email Header Analyzer | https://mxtoolbox.com/EmailHeaders.aspx | Header parsing is a known diagnostic workflow, but forwarding-specific recipient headers still require manual interpretation. |
| Postfix Address Rewriting docs | https://www.postfix.org/ADDRESS_REWRITING_README.html | Postfix documents address rewriting, virtual aliasing, local catch-all behavior, and debugging; admins still have to turn that into relay-specific evidence manually. |
| Mail-stack substitutes | https://github.com/docker-mailserver/docker-mailserver | Popular self-hosted mail stacks such as docker-mailserver, mailcow, Mailu, and maddy confirm the target ecosystem is active, but they do not validate an upstream relay's custom handoff by themselves. |

## Problem

Self-hosted mail admins often avoid exposing a home server directly by placing an ISP, VPS, spam-filtering service, or custom relay in front of it. That relay accepts mail for a domain, scans or buffers it, then forwards it inward. For catch-all domains and spam-source tracing, the downstream server must know the original SMTP envelope recipient, but providers expose that through inconsistent headers such as `X-Envelope`, `X-Original-To`, `Delivered-To`, or `Original-Recipient`.

The failure mode is quiet and expensive: mail still arrives, but aliases collapse, per-recipient rules misroute, spam-source attribution breaks, or a future relay replacement strips the only header the local processor depended on. The current workaround is manual test messages plus raw-header inspection, which passes the status-quo pain test because wrong mail routing can lose important messages and debugging easily burns more than 30 minutes.

## Target user

- Self-hosted mail admins using a front SMTP relay to shield a home or small-team mail server.
- Postfix/mailcow/docker-mailserver/Mailu/maddy users who rely on catch-all addresses, plus-addressing, or per-recipient spam-source tracing.
- Small operators who need a sanitized packet to discuss with a provider or community before changing MX records.

## MVP scope

- `relaytrace check --plan examples/catchall-relay.yaml --inbox examples/messages/`.
- YAML probe plan with expected aliases, accepted envelope-header names, and route labels.
- Offline RFC822 parser for saved raw messages.
- Header checks for `X-Envelope`, `X-Original-To`, `Delivered-To`, `Original-Recipient`, and configured custom names.
- Markdown packet and JSON summary with statuses: preserved, missing, ambiguous, overwritten, or untested.
- Synthetic fixtures only in v0; no real credentials, domains, message bodies, DNS changes, or live SMTP auth.

## Shortlist screened before winner

| Candidate | Wedge-first gate | Gate result |
|---|---|---|
| RelayTrace | Self-hosted mail admins behind an ISP/VPS/filtering relay → Swaks, MXToolbox, raw headers, Postfix docs, full mail-stack UIs → substitutes either test generic SMTP health or require expert manual interpretation of original-recipient headers → offline catch-all relay verdict packet for preserved/missing/ambiguous recipient evidence → r/selfhosted/mail-stack communities plus search content around SMTP forwarding/catch-all headers → fresh r/selfhosted SMTP forwarding thread and ongoing self-hosted email churn | Winner; gates pass. |
| RestoreToast | Self-hosted backup users → backup logs, cron mail, Duplicati/Restic/Borg scripts, manual restore drills → logs can say completed while restores remain untested → tiny restore-reminder/drill packet → r/selfhosted backup threads → fresh restore-test thread | Rejected for today: too close to prior BackupLocksmith/ForestDrill backup-recovery territory; differentiation would be weak. |
| BlobBudget | Web app builders with ~70GB user images → S3/R2/B2/MinIO/UploadThing docs and calculators → pricing and operational tradeoffs are confusing → storage-provider fit worksheet/CLI → r/selfhosted/webdev/search queries → fresh image-storage question | Idea-only/rejected: useful, but crowded storage calculators and provider docs make wedge and distribution weaker. |
| ArrLang Doctor | Sonarr/Radarr/Bazarr users managing multi-language releases → Trash Guides, custom formats, Recyclarr, forum advice → rules are powerful but confusing → config explainer for dual-audio fallback profiles → *arr communities → fresh r/selfhosted thread asks how to handle original+French audio | Rejected: media-release automation is policy-sensitive and the strongest channel is narrow; not the best public app bet for this repo. |
| OPDSSplit | Families hosting ebooks/articles → Calibre/OPDS, Kavita, Audiobookshelf-like libraries, manual libraries → mixed books/articles can become messy → library-shape planner → r/selfhosted ebook posts → fresh OPDS organization question | Rejected: status-quo pain looks tolerable and wedge is soft. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Swaks | Scriptable SMTP testing is strong and mature, but users must design the catch-all relay test, inspect received headers, and write their own verdict logic. |
| Direct competitor | MXToolbox SMTP Diagnostics / Email Header Analyzer | Useful hosted diagnostics for SMTP health and header readability; not local-first and not targeted at validating custom envelope-recipient preservation across a private forwarding relay. |
| Direct competitor | mailcow, docker-mailserver, Mailu, maddy | These can host or manage mail and aliases, but they do not prove what an upstream relay preserved during the handoff. |
| Indirect substitute | Raw header inspection, Postfix maps, provider docs, forum advice | Flexible but expert-heavy; the evidence packet is inconsistent and hard to repeat before/after a provider or MX change. |
| Status quo | Keep the relay and hope the custom header remains stable until a message routes wrong | Quiet mail loss or broken spam-source tracing can be costly, and debugging across provider + local mail stack wastes time. |

## Wedge-first gate

Self-hosted mail admin using an upstream SMTP relay for a catch-all domain → Swaks, MXToolbox, raw headers, Postfix/mail-stack docs → substitutes either test generic SMTP health or leave original-recipient preservation as manual expert interpretation → local fixture-to-verdict packet focused only on catch-all relay handoff evidence → r/selfhosted, mailcow/docker-mailserver/Mailu/maddy communities, and search pages for `SMTP forwarding X-Envelope X-Original-To` → fresh relay-replacement question plus ongoing churn around self-hosted email privacy, spam filtering, and ISP constraints.

## Wedge

RelayTrace wins by avoiding the big mail-server problem. It does not replace Postfix, mailcow, docker-mailserver, Mailu, maddy, Swaks, or MXToolbox. It wraps one under-served diagnostic moment: after sending unique catch-all probes through a front relay, can the admin prove which original recipient evidence survived and which routing assumptions are untested?

That is narrow enough for a 1–3 day MVP, low-trust enough to run offline on sanitized messages, and specific enough to produce a screenshot-worthy before/after packet.

## Kill condition

Reject or narrow if early self-hosted mail reviewers say one of these is true:

- Swaks plus a short shell script already gives them the exact same pass/fail packet;
- their mail-stack UI already exposes upstream original-recipient preservation clearly;
- they will not save raw synthetic probe messages locally for inspection;
- the first demanded feature is live SMTP credential handling before the offline packet proves useful;
- provider-specific header behavior is too fragmented to produce reliable generic guidance.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Broken catch-all routing or stripped recipient headers can lose mail and wreck spam-source tracing; the pain is narrow but real. |
| Feasibility | 4/5 | Offline plan + RFC822 header parser + markdown/json verdicts are straightforward; provider variation needs careful wording. |
| Demo potential | 4/5 | Synthetic raw messages can show preserved vs missing headers and a clean packet in a screenshot/GIF. |
| Distribution | 4/5 | Specific communities and search paths exist: r/selfhosted, mailcow/docker-mailserver/Mailu/maddy users, Postfix catch-all/header queries. |
| Competitive wedge / timing | 3/5 | Strong generic SMTP/header tools and mail stacks exist; the wedge is the narrow relay-handoff verdict packet, not broad diagnostics. |
| Total | 19/25 | Clears repo threshold and both gates. |

## Decision

Create the repo scaffold and consolidate the public-safe snapshot into the master index at [`projects/relaytrace`](../projects/relaytrace).

No dedicated GitHub remote was created for the project during this run; the scaffold/spec snapshot is tracked in the master index repo. Status is `repo-created` because the local project repo and canonical snapshot exist.

Weakest dimension: competitive wedge / timing at 3/5, because Swaks, MXToolbox, and mature mail-stack docs already cover adjacent diagnostics.

## Next build step

Implement the first runnable CLI slice: parse `examples/catchall-relay.yaml`, scan saved RFC822 fixture headers, classify preserved/missing/ambiguous recipient evidence, and write `relaytrace-report.md` plus `relaytrace-summary.json`.

## Research access note

Reddit JSON was blocked by `HTTP 403 theme-beta`; the run used the reddit-readonly RSS fallback for r/selfhosted and web extraction for competitor/documentation validation. Several other Reddit subreddit probes returned `fetch failed`, so the run did not loop on them. X `whoami` worked, but X search returned `401 Unauthorized`; no X write actions were attempted.
