# Day 095 — NetnsCarry

Date: 2026-10-31
Status: idea-only

## One-line pitch

A local, offline CLI that carries an operator's temporary kernel-mitigation review across Docker/LXC network-namespace recreation, showing which observations are stale or missing without claiming that a host is protected.

## Market research brief

- **Decision:** retain a narrowly scoped software hypothesis or create a dedicated project; do not build another general vulnerability scanner.
- **Target customer:** small Linux infrastructure teams operating Docker or Proxmox/LXC during a temporary kernel-mitigation window.
- **Geography:** global; no jurisdiction-specific compliance claim.
- **Category/substitutes:** native namespace/firewall inspection, an incident worksheet, existing mitigation scripts and configuration-management jobs.
- **Time horizon:** a 1–3 day offline comparison MVP, only after validation; the immediate incident window may close sooner.
- **Must-answer questions:** does container recreation invalidate evidence operators actually rely on; does a separate receipt beat a short native script; can those operators be reached repeatedly?
- **Evidence bar:** primary advisory for technical timing, full community context for demand, original substitute documentation for the gap. No inferred willingness to pay, market-size estimate or invented operator interviews.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public community report, 2026-10-31 06:15 UTC; discovered through Reddit RSS, full page and visible comments retrieved | [r/selfhosted: Ubuntu kernel mitigation window](https://www.reddit.com/r/selfhosted/comments/1xk2qbb/ubuntu_kernel_cve202698432_cvss_98_no_fixed/) | The author asks whether to apply a temporary nftables workaround while waiting for Ubuntu kernels. Comments range from waiting to shutting down a server. This is an AI-assisted advisory post, not an independently measured customer incident or proof of demand for this app. |
| Original distribution advisory | [Red Hat RHSB-2026-016](https://access.redhat.com/security/vulnerabilities/RHSB-2026-016) | Describes CVE-2026-98432 and a temporary IPv4 TCP/IP-options filter. Explicitly says filtering reduces exposure but cannot fully prevent it; kernel updates are the complete solution. Warns to test workload compatibility. |
| Original distribution tracker, last updated 2026-10-30 when retrieved | [Ubuntu CVE-2026-98432](https://ubuntu.com/security/CVE-2026-98432) | The `linux` rows for 22.04, 24.04 and 26.04 show vulnerable/work-in-progress status. Other package/flavor rows differ. This is a dated vendor snapshot, not an assertion that every Ubuntu kernel flavor has identical status. |
| Original independent implementation and its author's reported measurements | [typhoon1217/cve-2026-98432-mitigation](https://github.com/typhoon1217/cve-2026-98432-mitigation) | Already supplies apply, revert, namespace injection and active verification scripts. Reports injection into 64 container namespaces across five hosts, but says injection is not persistent after container restart. Measurements are the author's, not reproduced here; no vendor endorsement or real-exploit validation is claimed. |
| Original Linux interface documentation | [network_namespaces(7)](https://man7.org/linux/man-pages/man7/network_namespaces.7.html) | Firewall rules and networking sysctls are namespace-isolated. Establishes why a host-only observation cannot describe every container namespace; does not prove any particular workaround is effective. |
| Original native-tool documentation; strong substitute | [lsns(8)](https://man7.org/linux/man-pages/man8/lsns.8.html), [nftables ruleset operations](https://wiki.nftables.org/wiki-nftables/index.php/Operations_at_ruleset_level) | Native tools already enumerate accessible namespaces and export rulesets as JSON. `lsns` warns about unprivileged/incomplete visibility and stable-column selection. A separate app must beat those tools plus a prepared worksheet, not merely wrap their output. |

**Evidence confidence:** high for the documented isolation and mitigation limitations; moderate for immediate operational relevance; low for incremental product demand. The community post and advisory are not independent customer validations. Repeated lifecycle risk is technically plausible and the implementation documents a restart limitation, but repeated operator pain and paid demand have not been established.

## Shortlist and wedge-first gate — before scoring

Constraint: **Automate the annoying thing** — remove repeated reconciliation, not add a dashboard. Three software candidates were checked. Only the narrowed first candidate is scored; the others fail the gate and receive no cosmetic numeric ranking.

### 1. NetnsCarry — narrowed and retained for validation

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Docker/LXC incident owner using temporary per-namespace rules → existing mitigation scripts plus `lsns`, nft JSON and an incident worksheet → injection output is a point-in-time result and the implementation explicitly warns that restart loses injected state; whether the worksheet is actually inadequate is unproven → compare workload-to-namespace observations across acquisitions and reopen stale review items after recreation → maintainer-reviewed fixture/example contribution alongside the existing mitigation project and a precise “Docker/LXC namespace restart mitigation review” technical article; no posting performed, access not secured → a current kernel advisory creates a short temporary-control window.

- **Direct competitor:** the [existing mitigation repository](https://github.com/typhoon1217/cve-2026-98432-mitigation) already performs the substantive operational work, including namespace injection and checks. Do not rebuild it or imply it lacks verification.
- **Indirect substitute:** native inspection collected by a short script or existing configuration-management job, with a prepared worksheet carrying container identity, acquisition time, reviewer and follow-up.
- **Status quo:** re-run existing approved checks after lifecycle events, or wait for vendor patches under the team's incident process. No evidence that every operator does this badly.
- **Pain test:** stale review evidence during a security incident can matter even without a demonstrated 30-minute weekly tax. This is a risk rationale, not a measured failure or proof that a new product reduces risk.
- **Gate result:** reject a generic scanner/autofix wrapper; retain only the concrete cross-acquisition lifecycle comparison as an unvalidated idea. Wedge and distribution remain below creation gates.
- **Kill condition:** a small addition to the existing script/worksheet catches the same lifecycle gaps as quickly, or operators do not maintain these controls long enough to need repeated review.

### 2. ReleaseNudge — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Navidrome/Jellyfin listener leaving Spotify → artist-following release alerts and self-hosted discovery software → the author says their existing library is satisfactory but discovery is missing; no demonstrated incumbent failure → hypothesized local artist-list import into a release digest → Navidrome migration/setup content, but no evidenced repeatable user access → a fresh Spotify-exit question, not a verified new platform deadline.

- **Signal:** [r/selfhosted: Get updates for new music releases](https://www.reddit.com/r/selfhosted/comments/1xk4gis/get_updates_for_new_music_releases/), posted 2026-10-31 08:04 UTC. Full post and visible comments retrieved. A commenter suggests Aurral; another describes a Spotify API dependency problem in their own project, not independently verified here.
- **Direct/adjacent competitors:** [Aurral](https://github.com/lklynet/aurral) documents self-hosted discovery; [MusicButler](https://www.musicbutler.io/) search results advertise artist release notifications. MusicButler's current operation was not independently checked, so it is not relied on to establish present availability.
- **Indirect substitute:** artist/label feeds, newsletters and occasional manual discovery. **Status quo:** continue using a library the author explicitly likes.
- **Why reject:** no meaningful time, money, launch or security pain shown, and a relevant existing project is already recommended in the thread. Do not turn a discovery preference into an urgent replacement-product story. Aurral's exact notification/import coverage was not verified, so no absence claim is made.
- **Kill condition:** existing discovery tools or feeds satisfy the request; status-quo pain remains tolerable. Both are sufficient to stop this candidate today.

### 3. QuoteHandoff — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Small service business receiving website quote enquiries in WhatsApp → WAButton forms/routing, Wati Flows, or a prefilled link → repeated questions are proposed by a builder, not measured by an independent business → hypothetical minimal job-brief form without forced email → website-agency integration guides, with no acquired channel → fresh builder promotion, no demonstrated platform shift.

- **Signal:** [WAButton's disclosed team post](https://www.reddit.com/r/SideProject/comments/1xk4jxu/wabutton_what_should_a_website_collect_before/), 2026-10-31 08:10 UTC. This is competitor evidence, not unmet buyer demand.
- **Direct competitor:** [WAButton](https://wabutton.app/) already documents pre-chat forms, saved answers, routing and WhatsApp handoff. Forms are on paid plans; a free button exists. No price-under-cutting wedge is established.
- **Adjacent substitute:** [Wati's WhatsApp Flows](https://support.wati.io/en/articles/11463180-how-to-create-and-use-whatsapp-flows-in-wati) collect structured responses inside WhatsApp. Its documented prerequisites differ from a website click-to-chat widget; it is not identical functionality.
- **Indirect substitute:** a small website form, a prefilled WhatsApp message or staff follow-up. **Status quo:** ask the customer in chat, avoiding pre-chat abandonment.
- **Why reject:** the source promotes an existing implementation of the proposed job. No observed lost sales or repeatable first-user channel justifies another widget.
- **Kill condition:** current form/routing products already do the job and no niche-specific workflow gap is evidenced. Fired.

## Problem

A successful temporary-rule injection and a later container restart are different observations. An operator could retain an earlier “done” result after the namespace it described has disappeared. A replacement container with the same display name does not inherit that evidence merely because its name matches.

The documented restart limitation makes this a specific reconciliation hypothesis. It does **not** establish that an operator has been compromised, that their worksheet failed, or that collecting more receipts would improve security. The existing script's explicit warning is also counterevidence: its users may already know to re-run it.

## Target user

The person responsible for a small Docker or Proxmox/LXC estate's incident review, already following approved distribution guidance and collecting namespace-local evidence. Not Kubernetes fleet management, general vulnerability assessment, a home-user panic button or an automatic firewall administrator.

## MVP scope

Proposed only; no software or project repo created in this run. Python standard library plus an offline JSON/HTML report is a plausible 1–3 day slice after validation.

1. Import two operator-supplied, redacted acquisition bundles: workload inventory, accessible namespace inventory, namespace-local nft JSON, collection errors/timestamps, and an explicitly selected review recipe.
2. Record host/boot context, workload identity, shared namespace membership and namespace observation identity. A namespace inode or PID alone is not a durable global identifier; reuse, racing collection and missing identity must become ambiguity, not a confident match.
3. Compare **observations**, reporting `unchanged observation`, `recreated or remapped — review required`, `expected observation missing`, `collection incomplete`, and `recipe changed — not comparable`.
4. Carry reviewer, exception reason and next review trigger forward only where identity and scope are defensible. Host-network workloads can share the host namespace; do not invent a separate namespace requirement per container.
5. Preserve raw recipe identity: Red Hat's published example uses an `input` hook; the independent repository describes `prerouting` and bridge handling. Do not silently normalize them or claim equal packet-path coverage. Unknown expressions or unsupported versions remain unreviewed.
6. Export a local review receipt with explicit unknowns. Rule presence is not effective protection; missing the selected recipe is not proof of exploitability. File hashes, if used, only describe bundle integrity, not completeness or authenticity of acquisition.

**Non-goals:** apply/delete rules; inject namespaces; restart services; change sysctls; probe endpoints; run exploit checks; certify mitigation; decide when to remove a control; infer livepatch or running-kernel fix status from an upstream version string. Collection may require privileges even though the MVP analysis is offline. No production checks or mitigations were run today.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct operational substitute | [Existing CVE mitigation project](https://github.com/typhoon1217/cve-2026-98432-mitigation) | Already includes apply/revert, Docker/LXC namespace injection, active checks and limits. Any incremental value must be lifecycle review continuity, not rediscovery of namespace-local rules. Its active tools are outside this proposed passive MVP. |
| Native substitute | [lsns](https://man7.org/linux/man-pages/man8/lsns.8.html) plus [nft JSON](https://wiki.nftables.org/wiki-nftables/index.php/Operations_at_ruleset_level) | Already supplies the inventory/evidence primitives. Permissions and visibility are material; default output columns are unsuitable as a stable contract. |
| Indirect substitute | Prepared incident worksheet plus a short approved collection/diff script | Can carry boot/workload identities, review timestamps and exceptions. This is the baseline to beat; an empty spreadsheet is not a fair comparison. |
| Adjacent substitute | Existing configuration-management checks and incident/change tickets | A team may already re-check controls after restarts. No assertion that named enterprise platforms lack this workflow. |
| Status quo | Re-run approved checks after changes, or wait for fixed kernels with an explicit incident decision | May be adequate. A receipt must not delay patching or encourage an unreviewed workaround. |

## Wedge

A narrow, offline **namespace-lifecycle comparison**, not a CVE verdict. Separate “observed earlier,” “same workload now mapped elsewhere,” and “could not collect.” The distribution hypothesis is an upstream-adjacent fixture and technical example for the exact Docker/LXC restart problem, not a generic security launch.

That is a concrete testable wedge, but not a validated market advantage. The existing mitigation author has already explained the restart caveat and supplied verification. A small upstream improvement may be preferable to a standalone app. Distribution remains **3/5**: a relevant project and community exist, but maintainer interest, repeat use and repeatable acquisition have not been demonstrated.

This differs from the earlier PatchProof patch-compliance idea: it would not assess patch compliance. Reject it if it expands into that crowded reporting category.

## Kill condition

Stop or contribute a small upstream example instead if any of these holds:

- A prepared worksheet plus a short native inventory/diff catches recreated, shared and unreadable namespaces with equivalent accuracy and review time.
- Two qualified operators cannot demonstrate repeated reconciliation work or a meaningful stale-review risk in their actual process.
- Ruleset semantics, identity races or missing visibility cannot be represented honestly without false green output.
- Fixed vendor kernels close the incident window before operators need the comparison, and no independent recurring use case is validated.
- The only distribution plan is to promote a new security tool into the original help thread. No unsolicited outreach or social writes are authorized.

## Scoring

Assigned only after the substitute and wedge-first gates above, to the narrowed retained hypothesis.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Potential stale-control-review risk during an actual advisory window; operational relevance is real, but recurring customer pain is not measured. |
| Feasibility | 4/5 | Bounded offline comparison is small; trustworthy acquisition and live semantic verification are intentionally excluded. |
| Demo potential | 4/5 | A before/after fixture can visibly invalidate a receipt after recreation without displaying a misleading protected badge. |
| Distribution | 3/5 | Specific Docker/LXC audience and upstream-adjacent example path; no repeatable access or committed maintainer/operator audience. |
| Competitive wedge / timing | 2/5 | Strong immediate timing, weak demonstrated addition over scripts/native tools/worksheet; the window may be brief. |
| Total | 17/25 | Below 18/25; both distribution and wedge dimension gates also fail. |

## Decision

**Winner: NetnsCarry. Status: idea-only. No dedicated project repo or scaffold created.**

It is the most actionable research hypothesis in this small sample, not a build recommendation. Generic scanning/autofix was rejected; only the bounded lifecycle review survives. The weakest dimension is competitive wedge/timing at **2/5**. Neither a security advisory nor a fresh Reddit post establishes a market.

What would change the recommendation: a reproducible timed advantage over the prepared native-tool baseline, two operator confirmations of repeated need, and a maintainer-approved recurring distribution route. Prefer a documentation/script contribution if that is the smallest useful outcome. Follow-up is tracked in Beads `apps-0iv`; this daily research run is `apps-hik`.

## Next build step

Before any project creation, prepare a redacted lifecycle comparison fixture and timed review protocol: stable namespace, recreated namespace under the same workload name, host-network sharing, collection failure, and changed rule recipe. Benchmark against explicit-column `lsns`/nft JSON plus a prepared worksheet. Require every incomplete case to remain unreviewed, no false continuity, and a proposed acceptance target of at least 30% lower review time with no missed cases. This target is a future validation criterion, not a measured result. Any namespace experiments must use an explicitly approved disposable environment, not production.

## Source access caveats

- Canonical Reddit helper first: JSON was blocked with HTTP 403; RSS returned five posts each for r/selfhosted and r/SideProject. RSS scores/comment-count zeroes mean unknown, not no engagement. The same helper reported JSON/RSS unavailable with HTTP 429 for r/sysadmin, r/webdev and r/SaaS.
- One subsequent small r/selfhosted listing returned HTTP 429; no tight retry loop followed. Reddit-constrained web searches for the affected communities returned no results. That is a retrieval limitation, not evidence that no pain exists there.
- Web extraction subsequently retrieved the three selected full Reddit posts and visible comment context. It does not guarantee an exhaustive comment tree; unrelated recommendations/ads are not evidence.
- X authentication status showed no OAuth2 user. A cheap account read succeeded, but search returned HTTP 401. No interactive auth was attempted. X-constrained web search returned adjacent migration chatter, not evidence for this winner; **no X demand validation** is claimed.
- Primary Red Hat/Ubuntu pages, the independent mitigation README, Linux/native-tool docs and shortlisted substitute pages were retrieved. No external scripts were executed. Advisory and repository statements are dated observations, not security advice or independently reproduced results.
