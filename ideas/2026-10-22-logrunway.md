# Day 086 — LogRunway

Date: 2026-10-22
Status: idea-only

## One-line pitch

A local-first CLI that compares the observed history of domain-controller Directory Service, DFS Replication, and DNS Server event logs with an operator's history target, without collecting event messages or changing logging policy.

## Research brief

- **Decision:** retain a narrow software validation bet or create a dedicated project repo; do not build another SIEM or generic security scanner.
- **Target customer:** Windows AD operators reviewing local event-history coverage across multiple domain controllers, especially before changing diagnostic logging or relying on WEF during collector outages.
- **Geography:** not geography-specific; English-language public operator evidence.
- **Substitute set:** native Windows queries, Event Viewer, Windows Event Forwarding, Netwrix guidance, and established log-management products.
- **Time horizon:** a 1–3 day metadata-only MVP if validation justifies it.
- **Must-answer questions:** is the pain material, what is already native, and does a fleet comparison save enough work to deserve its own tool?
- **Evidence bar:** fetched community problem report plus original platform/vendor documentation. Independent customer validation, willingness to pay, and repeatable distribution remain missing. This is a quick scan, not a market-size estimate.
- **Creative constraint:** automate the annoying thing; subtract event ingestion and policy mutation rather than compete on dashboards.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public community report, 2026-10-22 06:43 UTC; discovered through Reddit RSS, then original post fetched as HTML | [r/sysadmin: recommended sizes for Directory Service, DFS Replication and DNS Server logs](https://www.reddit.com/r/sysadmin/comments/1xcbakk/recommended_max_size_for_directory_service_dfs/) | Operator reports reviewing roughly 30 Server 2019 DCs; some busy machines retain only a few days. Asks about a 30-day target, local sizing versus SIEM/WEF, and diagnostic-logging volume. This is one deployment, not 30 independent customers. |
| Original Microsoft platform guidance | [WEF: do clients have a separate buffer?](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection#do-wef-clients-have-a-separate-buffer-for-events) | The local event log is WEF's buffer when a collector is disconnected. Microsoft says overwriting can lose events without a loss notification or gap indicator at the collector. This supports the risk, not proof that this operator lost events. |
| Original Microsoft native-tool documentation | [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent) | Already exposes log mode, maximum size, file size, oldest record number, record count, and oldest-event queries. Multi-server enumeration is explicitly documented. Raw collection is not a product wedge. |
| Original Microsoft command documentation | [wevtutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil) | Already reads log configuration, status, and events. Documents distinct overwrite, retain/discard, and automatic-backup behavior. A size limit alone does not establish a history duration. |
| Original vendor configuration guidance | [Netwrix: adjusting event log size and retention](https://docs.netwrix.com/docs/auditor/10_9/configuration/windowsserver/eventlog) | Warns that undersized source logs can overwrite audit data before collection. Documents manual and policy-based settings, including Directory Service. This corroborates the failure mechanism but is not a second customer interview. |

**Evidence quality:** moderate confidence in the operational problem; low confidence in a standalone product. The repeatable mechanism is supported by Microsoft and Netwrix, but only one fresh, independent customer problem report was established. No measured weekly time saving, pilot, prepayment, or pricing claim.

## Problem

Choosing a size in megabytes does not answer how far back a particular DC's local evidence actually reaches. Operators have to compare channels and machines, distinguish a sparse log from a rolling one, and decide whether local history is adequate for their investigation or collector-outage assumptions.

**Status-quo pain test:** passes on potential loss of investigative/security evidence, not on an invented claim of more than 30 minutes saved per week. The original report identifies short local history; Microsoft documents a way unforwarded history can be lost. Neither establishes a current compliance violation or a confirmed incident in that environment.

**Important distinction:** local history, centrally archived history, and complete event delivery are different facts. A young oldest event may follow log creation or a clear, not insufficient capacity. An old event does not prove continuous coverage or future durability.

## Target user

The AD administrator responsible for a multi-DC logging review who already has authorized access to log metadata and needs a per-machine/per-channel comparison, not a new event-ingestion platform. Start with Directory Service, DFS Replication, and the classic DNS Server log. Do not silently substitute the distinct DNS-Server/Audit channel.

## MVP scope

1. An operator-run Windows PowerShell collector reads only an explicit channel allowlist through `Get-WinEvent` and, where needed, read-only `wevtutil` queries. Export an allowlisted metadata schema: pseudonymous machine label, channel name, collection time, mode, configured size limit, file size, record count, oldest/newest event timestamps and record identifiers, and collection errors. Exclude event messages, event payloads, account names, raw machine names, security descriptors, and filesystem locations.
2. A small local CLI consumes those JSON exports and an operator-supplied per-channel history target. Produce deterministic CSV and a static HTML comparison of observed oldest-event age, newest-event freshness, logging mode, and missing/unknown data. The report must say **observed local history**, not guaranteed retention or compliance.
3. Optionally compare two snapshots to flag changed settings, record-number regression, or changing oldest-event boundaries. These are review cues, not conclusive proof of clearing, uninterrupted coverage, or delivered events.
4. Return explicit unknown states for unreadable, missing, disabled, empty, sparse, or temporally inconsistent logs. Show source timestamps and evidence sufficiency beside every interpretation.
5. Include an explanation of what native tools already show and when WEF/SIEM verification is needed. No automatic size prescription in the first MVP.

**Non-goals:** SIEM, log search, alerts dashboard, breach detection, recovery of overwritten events, retention guarantees, legal certification, event-payload uploads, automatic registry/GPO edits, or enabling verbose diagnostic channels.

**Operational constraints:** upstream collection still needs appropriate Windows log-read permissions and access; an offline parser does not remove that requirement. Do not invoke `wevtutil sl`, `wevtutil cl`, configuration-object `SaveChanges()`, or policy refresh/change commands. Bound collection queries and record partial failure rather than falling back to unrestricted event enumeration. Pseudonymous IDs still require review before any report is shared externally.

**Estimation trap:** EVTX file allocation and circular overwrite make file-size growth a poor general proxy for incoming bytes. A single oldest-event timestamp or two file-size samples cannot justify a forecast of days until loss. Keep capacity forecasts outside this MVP until a separate empirical method is validated.

## Shortlist and wedge-first gate — before scoring

Four software candidates were considered. Failed gates are rejected without numerical scores; an easy MVP does not rescue an unproven wedge.

### 1. LogRunway — narrowed winner, validation only

**Wedge-first line:** Multi-DC AD logging-review owner → Event Viewer, `Get-WinEvent`/`wevtutil`, WEF, Netwrix and log-management products → metadata and guidance already exist, but turning them into a consistent cross-DC history-target review may remain manual; that gap is unmeasured → metadata-only three-channel comparison with explicit uncertainty → exact-workflow PowerShell examples and search content for Directory Service/DFS/DNS history sizing, followed by opt-in AD-operator fixture reviews → today's operator report makes the workflow concrete, while collector-outage buffering makes it consequential.

- **Direct competitors:** [ManageEngine EventLog Analyzer](https://www.manageengine.com/products/eventlog/) collects, imports, analyzes, and manages logs; Netwrix Auditor is also a substantial adjacent audit-data product. No claim that either lacks this exact report was established.
- **Indirect substitutes:** native PowerShell loops, Event Viewer, a CSV/spreadsheet, and Microsoft/Netwrix configuration checklists.
- **Status quo:** compare oldest events manually, pick fixed sizes, or rely on central retention. Adequate central collection plus a short native script may be entirely sufficient.
- **Narrowing:** abandon generic sizing recommendations and a logging dashboard. Retain only explicit multi-machine history-target comparison and uncertainty handling.
- **Distribution gate:** named workflows and content terms exist; no demonstrated repeatable access, search demand, or channel partner. **3/5, not 4/5.** No replies or outreach were sent.
- **Kill condition:** a short native script/checklist or an incumbent report meets the review need with negligible recurring work, or operators do not need the comparison.

### 2. ReissueSweep — reject before scoring

**Wedge-first line:** Small-agency operator replacing affected website certificates → CA replacement notices, [Qualys SSL Labs](https://www.ssllabs.com/ssltest/), and existing TLS checks → no demonstrated failure of these substitutes for installation verification → proposed manifest of before/after certificate identities across an operator-supplied hostname list → incident-specific replacement checklist content for affected hosting agencies, but no established access → today's [Starfield/GoDaddy warning](https://www.reddit.com/r/sysadmin/comments/1xcbri8/godaddy_starfield_certificates_revoked/).

- **Direct competitor/substitute check:** SSL Labs already provides deep public-server TLS configuration analysis; the CA's [original incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2082703) documents affected profiles and mass revocation. An OpenSSL loop and a spreadsheet are inexpensive indirect substitutes.
- **Status quo pain:** browser warnings and inaccessible sites are material; verifying a replacement may nevertheless be a one-time, tolerable checklist task.
- **Kill condition/result:** the report establishes urgency, not a durable software gap or first-user route. Reject rather than create a generic certificate checker. Do not infer that all affected certificates completed revocation simultaneously; the CA report links a separate delayed-revocation record.

### 3. RadiusCutover — reject before scoring

**Wedge-first line:** FreeRADIUS operator moving a CentOS 7/FreeIPA-backed installation → native debugging, package defaults, staged replacement server and an operator runbook → cross-OS backend/configuration omissions are plausible but not established as an unsolved tooling problem → proposed offline dependency inventory and migration comparison → FreeRADIUS/FreeIPA migration how-to search and opt-in operator review, with no proven repeatable access → today's [FreeRADIUS OS/version-upgrade request](https://www.reddit.com/r/sysadmin/comments/1xcaxlz/best_way_to_upgrade_freeradius_version_and_os/).

- **Direct/native competitor check:** official [`radiusd -X` guidance](https://www.freeradius.org/documentation/freeradius-server/3.2.11/radiusd_x.html) already explains loaded configuration/modules and detailed startup/processing failures. A staged server with real authentication tests covers behavior that static inventory cannot prove. Do not describe the debug server as a passive collector.
- **Indirect substitute/status quo:** configuration diff plus a staged migration runbook; continue operating the old installation until validation is complete.
- **Status-quo pain:** an authentication cutover can interrupt access; the source does not quantify repeated migration work or show that native validation failed.
- **Kill condition/result:** without concrete omission fixtures, static checks risk implying authentication readiness they cannot establish. Reject this version; no score and no claim that the suggested target release is validated.

### 4. MondayReady — reject before scoring

**Wedge-first line:** IT team manually preparing about 20 new-hire machines weekly → [PDQ Deploy](https://www.pdq.com/pdq-deploy/), Intune/Autopilot, and deployment scripts → no source evidence that these established substitutes fail the job → proposed role-based setup CLI lacks a defensible narrower wedge → Windows endpoint-deployment tutorials, a channel already served by incumbents → today's [bulk-setup bottleneck report](https://www.reddit.com/r/sysadmin/comments/1xcacvi/looking_for_advice_how_to_automate_bulk_system/).

- **Direct competitor check:** PDQ documents package deployment and targeting; Microsoft's [Autopilot deployment guide](https://learn.microsoft.com/en-us/autopilot/tutorial/user-driven/azure-ad-join-deploy-device) covers application/policy deployment. Fetched thread replies explicitly recommend existing deployment products and workflows.
- **Indirect substitute/status quo:** unattended scripts and a checklist, or repeated manual installation. The latter is explicitly a recurring bottleneck.
- **Kill condition/result:** real pain but an already-solved category at the proposed scope. Recommend adoption of an existing deployment workflow, not another product. Reject before scoring.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct/broader log-management competitor | [ManageEngine EventLog Analyzer](https://www.manageengine.com/products/eventlog/) | Existing agentless/agent-based collection, import, log analysis and management. Do not compete on storing or searching events. Exact metadata-only comparison coverage remains unverified. |
| Adjacent audit product and explicit workflow guidance | [Netwrix Auditor](https://docs.netwrix.com/docs/auditor/10_9/configuration/windowsserver/eventlog) | Already explains overwrite risk and how to configure sizes, including Directory Service. A checklist may solve the need without software. |
| Native competitor | [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent), [wevtutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil), Event Viewer | Already provide collection primitives, oldest-event queries and multi-server enumeration. This is the strongest baseline, not a straw-man competitor. |
| Indirect substitute | [WEF/WEC plus central retention](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection), spreadsheet, operator-authored script | Central storage can satisfy the actual history requirement. Local buffering still matters during disconnection; source-only metadata cannot verify downstream delivery. |
| Status quo | Fixed channel sizes plus occasional manual review | Tolerable if central evidence is complete and native review is quick. Pain must be demonstrated in the target environment rather than assumed. |

No current-price advantage is asserted: fetched material does not establish comparable total costs or willingness to pay for this narrow review.

## Wedge

The only defensible hypothesis is a **small, local, uncertainty-aware fleet review**, not novel collection or universal retention sizing. The specific three-channel request defines a testable scope. A shareable report might help an operator explain where local evidence is short or unknown without handing over event payloads.

That is not yet a proven competitive advantage: Microsoft already documents the primitives and multi-server enumeration, and Netwrix documents the policy workflow. The native baseline must be allowed to win. Competitive wedge/timing is therefore only **2/5** despite fresh timing.

## Kill condition

Reject or fold into a free example if any of these hold:

- A short native PowerShell script plus Microsoft's WEF/Netwrix guidance answers the same review questions in under ten minutes with no material interpretation mistakes.
- Three independent AD operators cannot identify recurring review effort or a consequential local-history blind spot that the proposed comparison resolves.
- A product they already use supplies the comparison without meaningful additional work.
- Correct output requires payload capture, continuous privileged monitoring, or unvalidated forecasts beyond a 1–3 day MVP.
- There is no repeatable, opt-in acquisition route beyond a single Reddit thread.

These are prospective rejection tests, not completed experiments.

## Scoring

Only the narrowed winner is scored, after the gates and substitute checks above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Losing local investigative evidence is consequential; one fresh fleet report plus original documentation supports the mechanism, not broad demand. |
| Feasibility | 4/5 | Metadata export and deterministic comparison are small; Windows permissions, log resets, sparse data and platform validation still matter. No forecast or policy mutation. |
| Demo potential | 4/5 | A synthetic, explicitly labeled multi-DC example can show short/unknown history clearly without sensitive event payloads. No demo was built in this research run. |
| Distribution | 3/5 | Exact AD/PowerShell workflow is identifiable, but repeatable acquisition and user access are unproven. |
| Competitive wedge / timing | 2/5 | Fresh request, strong native primitives, and established log tools; added value over a small script is not validated. Weakest dimension. |
| Total | 17/25 | Below 18/25; Distribution also misses 4/5 and Wedge misses 3/5. |

## Decision

**Winner: LogRunway. Status: idea-only. No dedicated project repo created.**

It is the most concrete surviving validation bet in this shortlist, not a recommendation to build immediately. Do not inflate its score to meet the streak. Both dimension gates and the total threshold fail.

The evidence supports testing a metadata-only history review. It does not establish a business, a retention guarantee, a complete-delivery monitor, or a gap incumbents cannot cover. There is no customer-market sizing claim.

## Next build step

Create one fixture-first comparison spike: define the metadata schema and expected outcomes for circular rollover, cleared/recreated logs, sparse/empty logs, missing channels, denied access and clock anomalies; compare a report with a minimal native PowerShell query/checklist baseline. Label constructed fixtures as synthetic, not customer data. Only after the native baseline comparison and independent operator reviews should a dedicated app repo be reconsidered.

Tracked validation: `apps-tbg`. Daily research: `apps-4bn`.

## Source access caveats

- The canonical Reddit helper used a small four-subreddit probe. Public JSON was blocked with HTTP 403 for r/sysadmin and r/androidapps; RSS supplied recent posts for both. For r/selfhosted and r/webdev, the helper reported JSON/RSS unavailable with HTTP 429. No tight retry loop was used.
- The winner and three shortlisted r/sysadmin posts were subsequently fetched through web extraction as original HTML, providing fuller context; the winner and onboarding threads exposed comments. This is not restored JSON access or complete thread coverage. RSS score/comment-count zero fields are placeholders, not measured engagement.
- `xurl whoami` worked, but the small search returned HTTP 401 Unauthorized. No OAuth2 token was available as a fallback. No X evidence is claimed; a public X-constrained web search returned no results.
- Date-constrained Reddit web searches and several later competitor searches returned no results, including broader retries. That does not prove absence of competitors. Direct original Microsoft, Netwrix, ManageEngine, PDQ, FreeRADIUS, SSL Labs and CA-incident pages supplied the usable checks. An attempted SSL Labs project-information URL returned a 404 page and was not evidence; its working public test page was used instead.
- Read-only research only. No social posts, replies, likes, follows, DMs, production log queries, public TLS test submissions, or customer outreach were performed.
