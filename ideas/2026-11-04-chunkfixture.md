# Day 099 — ChunkFixture

Date: 2026-11-04
Status: idea-only

## One-line pitch

A local CLI that turns an operator-prepared HTTP/1 chunked-response case into a native HAProxy VTC fixture and a two-build comparison, without treating an older build's acceptance as proof of protocol correctness or safety.

## Research brief

- **Decision:** retain a narrow incident-to-regression-fixture hypothesis; do not build another proxy monitor or security scanner.
- **Target customer:** an Ubuntu/HAProxy operator maintaining an HTTP backend who needs a sanitized, repeatable case for upstream or distribution support.
- **Geography:** English-language open-source infrastructure support; no geography-specific compliance claim.
- **Substitute set:** HAProxy `show errors`, native vtest/VTC tests, a short socket script, a prepared issue template and vendor support.
- **Time horizon:** one-to-three-day bounded CLI only after a timed native-baseline comparison.
- **Must-answer question:** does a constrained fixture generator reduce total reproduction preparation, including acquisition and sanitization, enough to justify software beyond a VTC example?
- **Evidence bar:** one complete fresh public incident report plus original distribution, vendor and native testing documentation. No independent reproduction, repeated buyer requests, interviews or willingness-to-pay evidence; no defensible market-size estimate.
- **Creative constraint:** “Nothing new except glue” — reuse native vtest rather than inventing an HTTP testing engine.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public operator report; discovered through RSS, short HTML post retrieved | [Ubuntu 22.04 HAProxy intermittent 502 after security update](https://www.reddit.com/r/sysadmin/comments/1xniryv/ubuntu_2204_haproxy_24300ubuntu022043_returns/) | Posted 2026-11-04 at 08:13 UTC. Author reports 26/30 failures on `2.4.30-0ubuntu0.22.04.3` and 0/30 on `.2` against the same FME Flow backend/config, with `MSG_CHUNK_SIZE` in `show errors`. These are the author's results, not ours. The retrieved post contained no raw response, configuration or reproducer and no visible replies. |
| Original distribution advisory, published 2026-11-03 | [Ubuntu USN-8972-1](https://ubuntu.com/security/notices/USN-8972-1) | Lists `2.4.30-0ubuntu0.22.04.3` as the Jammy fixed package for HTTP/1 chunked-request and HTTP/2 PING denial-of-service issues. Confirms timely patch pressure, not that the update caused the reported backend-response failure. |
| Original vendor security bulletin | [HAProxy October 21, 2026 bulletin](https://www.haproxy.com/blog/haproxy-security-bulletin-oct-21-2026) | Documents HTTP/1 chunk-parser and HTTP/2 vulnerabilities and recommends updated products. An older package that accepts a case is not a safe production recommendation. Upstream versions and Ubuntu backported package revisions must not be compared as equivalent strings. |
| Original native diagnostic documentation | [HAProxy 2.4 management guide: show errors](https://docs.haproxy.org/2.4/management.html#9.3-show%20errors) and [Runtime API reference](https://www.haproxy.com/documentation/haproxy-runtime-api/reference/show-errors/) | Already exposes last known request/response protocol errors, parser context and escaped bytes with offsets. This substantially weakens a diagnostic-collection wedge. It is an error-buffer snapshot, not a promised full session capture or wire-timing trace. The retrieved rolling 2.4 guide identifies itself as 2.4.36, not the exact Ubuntu build under discussion. |
| Original native regression-testing documentation | [HAProxy regression-testing guide](https://raw.githubusercontent.com/haproxy/haproxy/master/doc/regression-testing.txt) | vtest already launches HAProxy with embedded configs, local listeners and server/client fixtures; `HAPROXY_PROGRAM` selects the executable, and logs can be retained. A two-build test does not require a new engine. The current development guide is a baseline to verify against the selected vtest and distro binaries, not proof of exact version compatibility. |

**Confidence:** medium that patch-adjacent interoperability triage is consequential; low that a standalone fixture app is needed. The vendor and distribution advisories are related technical context, not two more independent customers. Repeated occurrence across different operators has not been established. No public source here confirms root cause or malformed backend output.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked. Rejected candidates are not numerically scored.

### 1. ChunkFixture — narrowed and retained

**Wedge-first line:** Ubuntu HAProxy operator preparing an upstream backend-response incident → native `show errors`, vtest/VTC and a short socket script → native tools already collect parser context and replay fixtures, but translating a sanitized incident case into a reproducible two-distro-build test may still cost time; this is unmeasured → generate only a constrained chunked-response VTC and versioned comparison manifest → an exact `MSG_CHUNK_SIZE`/Ubuntu-package troubleshooting recipe and maintainer-reviewed VTC example in relevant HAProxy or distribution support discussions where invited → a fresh operator report follows yesterday's distribution security update, making secure resolution more useful than casually reverting.

- **Direct functional competitor:** native vtest plus an existing or adapted VTC; it already controls the executable and test topology.
- **Indirect substitutes:** `show errors`, a prepared support issue, a raw socket script and vendor/distribution support.
- **Status quo:** the author already ran a 30-request version comparison; missing evidence is a transferable isolated reproducer, not a lack of counts or monitoring. That existing work is counterevidence to replacing the workflow.
- **Gate result:** reject a generic proxy diagnostic wrapper. Retain only constrained fixture authoring; the wedge is a hypothesis, not a verified native feature gap.
- **Kill condition:** a prepared native VTC example and issue template provide equivalent outcomes at equal or lower end-to-end effort. Prefer an upstream test contribution.

### 2. TenantTakeover — rejected before scoring

**Wedge-first line:** junior inheriting solo Microsoft 365 administration → documented policy descriptions, maintenance checklist, CIPP and Microsoft365DSC → the fresh author lacks a structured handover but has already found descriptions explaining policies; no missing drift capability is demonstrated → candidate was a dated policy-review/handover app, but a standalone product wedge does not survive → a specific M365 takeover checklist and baseline tutorial for junior tenant administrators → a fresh handover, not a verified new platform requirement.

- **Signal:** [Inherited solo M365 admin responsibilities as a junior](https://www.reddit.com/r/sysadmin/comments/1xni9ai/inherited_solo_m365_admin_responsibilities_as_a/), full post and visible comments retrieved. Author asks for a maintenance procedure and later reports policy descriptions and an existing emergency account. A claimed emergency account is not proof its recovery path has been tested.
- **Direct competitors:** [CIPP Standards & Drift](https://docs.cipp.app/user-documentation/tenant/standards) already documents reporting, scheduled deviations and accept/deny review. Its page also describes a Baselines feature flag replacing that interface; do not infer a missing successor. [Microsoft365DSC drift monitoring](https://microsoft365dsc.com/user-guide/get-started/monitoring-drifts/) already compares desired configuration and logs changed properties.
- **Indirect substitute / status quo:** approved checklist, existing descriptions, native audit logs and a supervised handover; no auto-remediation is needed to answer the initial procedural request.
- **Wedge and kill:** reject generic tenant drift/reporting and checklist-as-an-app. Existing tools cover the mechanics; the source does not establish that a prepared procedure fails. No tenant access, policy changes or recovery-account tests performed.

### 3. PhoneGuide — rejected before scoring

**Wedge-first line:** IT helper supporting nontechnical phone users ad hoc → FaceTime screen sharing and TeamViewer QuickSupport → the fresh question asks whether a feature exists, while visible replies already identify working options → candidate was an attended phone-viewing app, but no unmet workflow remains → a platform-specific setup guide for the same support question → fresh feature-discovery confusion rather than a new capability gap.

- **Signal:** [Is there a way to remote view iOS / Android devices?](https://www.reddit.com/r/sysadmin/comments/1xnhqf9/is_there_a_way_to_remote_view_ios_android_devices/), full post and visible comments retrieved. Replies identify FaceTime, existing RMM tooling and Teams; one commenter describes FaceTime as saving time.
- **Direct competitor:** [TeamViewer attended mobile support](https://www.teamviewer.com/en/global/support/knowledge-base/teamviewer-remote/mobile/provide-attended-remote-support-for-mobile/) already documents QuickSupport installation, explicit access approval and Android/iOS screen-sharing initiation. Do not generalize its broad control wording into unrestricted remote control on every iOS device.
- **Indirect substitute / status quo:** an existing call with screen sharing, screenshots or an approved helpdesk/RMM session. Visible reports of a successful substitute weaken replacement demand.
- **Wedge and kill:** reject a new mobile remote-support product. No evidence that these choices fail the stated job, and platform/security complexity is unsuitable for a one-to-three-day replacement.

## Problem

A post-update 502 can be observed without a reusable test that a maintainer can run. Version strings, escaped error bytes, backend framing, configuration and individual attempts need enough context to distinguish a narrow interoperability change from a generic outage. A normal HTTP client may normalize the very framing the operator needs to preserve.

The actual remaining pain is unproven: the author already compared versions. Native tooling can reproduce traffic and expose errors. The product must beat a prepared VTC, not an empty document.

**Status-quo pain test:** failed backend requests create availability risk, while an unexamined rollback can reintroduce security exposure. That is consequential enough for investigation. No verified weekly time cost, lost revenue, launch blockage or recurring demand is claimed. If native reproduction is quick enough, reject the app.

## Target user

An operator already responsible for an Ubuntu HAProxy service who can prepare a permitted sanitized backend-response fixture and identify the exact distribution packages under comparison. Not a general uptime-monitoring buyer, vulnerability-scanner user or someone seeking an automated downgrade recommendation.

## MVP scope

Proposed software only; **not implemented or behavior-tested in this research run**:

1. A local Python CLI accepting a small declarative case manifest and operator-prepared synthetic/raw response fixture. Record exact distro package identity, architecture, `haproxy -vv` output, chosen vtest version, minimal config and fixture revision. Never assume a generic upstream container image equals an Ubuntu package.
2. Generate a constrained, human-reviewable VTC using native vtest and a minimal backend. Preserve declared HTTP bytes rather than silently fixing chunk lengths, line endings or headers. Unknown capture completeness stays unknown. Do not claim a `show errors` snapshot automatically reconstructs a complete conversation.
3. Run each approved executable separately in an isolated local test environment with bounded attempts, process timeouts and cleanup. Old vulnerable builds belong only in disposable, non-public test environments. No production backend calls, live admin-socket connections, package installation, patching or traffic capture by default.
4. Report per-attempt status, received response bytes, timeout/crash distinctions and native error output where available. Keep not-run/build-unavailable distinct from pass; retain exact config/fixture correspondence and controls. Never fabricate the source author's 26/30 result as a local test.
5. Export the VTC, a comparison manifest and a human-reviewed issue draft. Local data only; no telemetry or automatic issue posting. Raw buffers/logs may contain identifiers, credentials or body data and must not be published automatically. Redacted derivatives must be tested separately because sanitization can change parser behavior.

**Boundary:** request-parser security advisories are timing and risk context, not proof of a response-parser regression. `MSG_CHUNK_SIZE` is an observed state label, not a diagnosis. TCP write boundaries do not guarantee receive segmentation, and an error-buffer replay does not reproduce timing, connection reuse, TLS or load unless explicitly modeled. Differential acceptance proves only observed behavior under that fixture; neither acceptance nor rejection alone establishes RFC conformance, vulnerability status or backend blame.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | HAProxy vtest/VTC | Already supports local client/server cases, embedded config, executable selection and retained logs. Main benchmark; prefer contributing a fixture if it solves the need. |
| Native diagnostic substitute | `show errors` | Already reports parser context and escaped error bytes. Last-error context is not continuous capture, and collection needs operator/admin socket permissions even if later analysis is offline. |
| Indirect substitute | Short socket script plus prepared issue template | Can preserve deliberately constructed response bytes and exact package/config details with little machinery. Include the author's already-completed version comparison in the baseline. |
| Service substitute | HAProxy/distribution support | Can investigate backports and expected parser behavior; this CLI cannot certify a patched version or replace maintainer diagnosis. |
| Status quo | Keep the existing incident record and submit a minimal native test | May be adequate. No demonstrated demand for a separate app or paid service. |

## Wedge

A possible wedge is **incident-to-native-test authoring for one response-framing family**, not another collector, security scanner or test engine. A constrained manifest could reduce omissions and make the result directly usable as an upstream VTC.

This remains a weak competitive claim: native vtest already supplies most mechanics, the author already performs version comparisons, and a good example may be the entire product. Fresh security-update pressure justifies careful investigation, not a production rollback or a new repository.

## Kill condition

Reject the standalone app if any condition holds:

- Native vtest plus a prepared VTC/issue template handles equivalent two-build cases at equal or lower total acquisition, sanitization, preparation and reporting effort.
- Three relevant operators cannot supply recurring cases, or fewer than two achieve a provisional 30% reduction in end-to-end preparation without losing byte/config fidelity. This is a validation target, not a measured result.
- Useful reproduction requires reconstructing unavailable bytes, preserving production secrets, unbounded malformed-input testing or contacting live services.
- The reported incident resolves with one upstream test or backend fix and there is no recurring fixture-authoring need.
- Distribution remains a one-off support reply rather than repeatable adoption of a useful native-test recipe.

## Scoring

Assigned after the competitor and narrowing gates above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Availability and patch-security tradeoffs matter; recurring fixture-preparation burden is unmeasured. |
| Feasibility | 4/5 | A constrained VTC generator and local comparator is plausible in one to three days; automatic capture reconstruction and universal reproduction are excluded. |
| Demo potential | 4/5 | One reviewed fixture and two exact-build outcomes are easy to show, once actually executed. No behavioral demo or reproduction was produced today. |
| Distribution | 3/5 | Exact package/parser-state troubleshooting content and HAProxy/distribution maintainer discussions identify users, but no proven recurring access or adopted integration exists. |
| Competitive wedge / timing | 2/5 | Timely patch context, but native vtest and `show errors` already supply the hard capabilities. A prepared example may eliminate the app. |
| Total | 17/25 | Below 18/25; Distribution and competitive-wedge gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** ChunkFixture is today's strongest retained validation hypothesis, not a validated product or a confirmed HAProxy regression. Weakest dimension: competitive wedge/timing, 2/5 versus the required 3/5. Distribution is 3/5 versus the required 4/5.

The evidence supports investigating a reproducible native testcase while respecting security updates. It does not support a new general diagnostic product, a safe-downgrade claim or charging for a missing feature we have not demonstrated.

## Next build step

If taken forward, make one validation-sized commit containing a synthetic chunked-response VTC, a two-exact-build result template and the equivalent prepared native-script/issue baseline. Include a valid-response control, explicitly malformed control and repeated-run outcomes; do not claim these synthetic cases reproduce FME Flow. Time complete case preparation with three relevant operators and require two to meet the improvement target before app implementation. Prefer an upstream fixture contribution if the native baseline is sufficient. No outreach, HAProxy execution, exploit test or production change occurred during this research run.

Follow-up is tracked in Beads (`apps-qhl`).

## Source access caveats

- Canonical `reddit-readonly find` requested five recent posts each from r/sysadmin, r/selfhosted and r/webdev with a 48-hour window. r/sysadmin JSON returned HTTP 403/theme-beta; RSS returned five posts. RSS zero scores/comment counts mean unavailable metadata, not zero engagement.
- The same probe reported r/selfhosted and r/webdev JSON/RSS unavailable with HTTP 429. No tight retry loop. Reddit-constrained web searches for additional webdev and HAProxy demand returned empty results; this is not evidence that those communities or additional cases do not exist.
- Selected sysadmin posts and visible comments were recovered through HTML extraction. Collapsed replies were not exhaustively retrieved. The winner's short visible post had no raw reproduction or visible replies; one operator report is not repeated market demand.
- `xurl whoami` succeeded; read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured; no interactive authentication was attempted. An X-constrained web search returned unrelated M365 results and was not used as validation. No X evidence supports the winner.
- Original vendor/distribution documentation and public repository files were readable. Some exact-demand searches returned no results. Retrieved documentation establishes substitute capabilities, not hands-on product performance; no paid subscription or private account was accessed.

## Repository verification caveat

The existing repository-wide snapshot verifier still fails with `KeyError: 'source_commit'`, tracked separately in Beads (`apps-mq0`). No snapshot or verifier code changed in this daily run. Daily brief/index consistency and JSON/privacy checks are verified separately; the repository-wide suite must not be described as green.
