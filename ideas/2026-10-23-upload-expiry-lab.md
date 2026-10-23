# Day 087 — UploadExpiryLab

Date: 2026-10-23
Status: idea-only

## One-line pitch

A local Playwright scenario kit that catches presigned multipart-upload URLs expiring while browser work waits for admission, before an uploader change reaches production.

## Research brief

- **Decision:** retain a narrowly testable developer-tool hypothesis or create a project repo; do not build another uploader or AI video app.
- **Target customer:** maintainers of browser-to-object-storage multipart uploaders using short-lived signed URLs, especially HTTP/1.1 endpoints and multiple tabs of the same app.
- **Geography:** not geography-specific; English-language public developer evidence.
- **Substitute set:** Uppy AWS S3, Uppy/Tus, native Web Locks, browser DevTools, and a short project-owned Playwright test.
- **Time horizon:** a 1–3 day fixture-first validation spike, not a production S3 emulator.
- **Must-answer questions:** does a reusable regression scenario add value beyond the already-working workaround and a small test, and can independent uploader maintainers be reached repeatedly?
- **Evidence bar:** a fetched public production-failure report, original uploader documentation and browser/storage documentation. No interviews, paying customers, market sizing or measured weekly savings were established.
- **Creative constraint:** the CLI tool that should exist; subtract storage hosting, upload UI and scheduling implementation, leaving one regression question.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public developer report; original HTML fetched, displayed as 1 day old at retrieval | [r/webdev: signed upload links expiring while queued](https://www.reddit.com/r/webdev/comments/1xbxwkn/chrome_only_sends_6_requests_per_host_and_our/) | Developer describes large multipart uploads, short-lived URLs and an HTTP/1.1 bucket endpoint. Early signing allowed queued requests to expire. The implemented fix signs inside a Web Lock immediately before upload. This is one deployment, not broad market demand. |
| Same reporter's follow-up; not an independent customer signal | [Why one upload slot is acceptable](https://www.reddit.com/r/webdev/comments/1xbxwkn/comment/19rhslv907nlt/) | Reporter explicitly says the uplink is the bottleneck and prefers fail-fast with missing-part resume over automatic retries. A faster cross-tab scheduler is not demonstrated as necessary. This negative evidence caused the candidate to be narrowed. |
| Original uploader documentation | [Uppy AWS S3](https://uppy.io/docs/aws-s3/) | Already provides direct S3-compatible multipart uploads, per-operation signing, a concurrency limit and resumability. Its documented limit matches common HTTP/1.1 connection counts. A new uploader has a weak wedge. |
| Original browser API documentation | [MDN Web Locks](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API) | Documents same-origin coordination across tabs/workers, queued lock requests, callback-scoped release and cancellation. The basic scheduling primitive is already native. |
| Original browser protocol guidance | [MDN HTTP/1.x connection management](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x) | Explains parallel connection limits, commonly six, and HTTP/2 multiplexing. Six is not a universal limit for all browser protocols or contexts. |
| Original storage documentation | [AWS presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) | Documents expiry at HTTP request time, credential-lifetime limits and policy restrictions. URLs are bearer capabilities and must be protected. AWS rules do not establish identical behavior for the reporter's unspecified S3-compatible service. |
| Original test-tool documentation | [Playwright network](https://playwright.dev/docs/network), [multiple pages](https://playwright.dev/docs/pages#multiple-pages) | Already supplies request observation, routing and multiple tabs in one browser context. Routing occurs before the browser network stack; a route callback is not proof of server arrival or real connection-pool saturation. A short native test is the strongest substitute. |

**Confidence:** moderate in the reported failure mechanism; low in a standalone product opportunity. The same thread contains corroborating anecdotes and suggestions, but independent deployments and recurring regression effort were not verified. Protocol documentation supports plausibility, not customer demand.

## Problem

A happy-path test can succeed on a fast connection while a queued signed request becomes unusable on a constrained link. Application-level scheduling, signing and actual server arrival happen at different times. Changes to per-file concurrency or cross-tab behavior can reintroduce the failure even after the application has a sound workaround.

**Status-quo pain test:** the original report describes failed production uploads, a blocked core product action. No revenue loss or more-than-30-minutes-per-week claim is established. Importantly, the reporter now considers the one-slot workaround adequate. Reject a replacement scheduler on that evidence. Only the unvalidated need to prevent recurrence through a reusable test remains eligible for investigation; if a short local test is sufficient, reject this product too.

## Target user

The engineer maintaining an existing custom or Uppy-based direct-to-storage uploader who already runs browser integration tests and must preserve short-lived signing, same-app cross-tab coordination, and explicit retry/resume semantics. Not everyone uploading a file, and not an audience defined merely as indie hackers.

## MVP scope

1. A CLI launches a local HTTP/1.1 test endpoint and a minimal signing fixture with configurable validity and bounded upload admission. Use generated bytes only. Synthetic capabilities model an expiry contract; they are not real cloud signatures or proof of S3 compatibility.
2. A Playwright adapter opens two same-origin tabs in one browser context and exercises a deliberately sign-early implementation versus a sign-after-admission implementation. Coordinate with explicit server barriers rather than arbitrary sleeps. Record signing, admission, server-arrival and completion timestamps using a common fixture-server clock where possible.
3. Separate two scenario classes: deterministic application-queue regression tests, and actual browser HTTP/1.1 contention tests. Do not claim a delayed mock route reproduces socket queueing. In the latter, assert observed server arrivals and protocol behavior instead of assuming a fixed universal connection count.
4. Assert useful invariants: no URL issued for application work still awaiting admission; expired attempts surface accurately; cancelling queued work does not sign it; closing a tab releases coordination without implying that an in-flight server operation was rolled back. Exercise explicit resume of a failed part without silently resending confirmed parts.
5. Produce a small local timeline and CI exit result with pseudonymous upload/part labels. Include an adapter contract so a maintainer can connect their existing uploader; no automatic instrumentation of arbitrary apps.

**Non-goals:** uploader UI, new storage service, cloud proxy, global browser bandwidth manager, security scanner, production traffic capture, universal S3 emulator, performance promises, or automatic changes to bucket policy/URL lifetime.

**Operational boundaries:** run against the fixture only by default. Do not accept production presigned URLs, upload customer files or log query strings, credentials, filenames or object keys. Signed URLs are capabilities even when short-lived. Web Locks coordinate cooperating contexts of the same origin, not every site targeting a bucket. Separate browser profiles/contexts are not a valid same-tab-pool assumption. Fail explicitly when required browser features are unavailable. Test expiration at request arrival; do not invent mid-transfer expiration behavior from a timer. Keep real-provider conformance and background-tab/mobile lifecycle behavior outside the first spike.

## Shortlist and wedge-first gate — before scoring

Three software candidates were checked. Failed candidates are rejected without numerical scores.

### 1. UploadExpiryLab — narrowed winner, validation only

**Wedge-first line:** Maintainer of a short-lived direct-to-storage multipart uploader → Uppy, Web Locks, DevTools and project-owned Playwright tests → the production report shows a queue/signing interaction escaping normal use, but failure of existing regression tooling is unproven → reusable two-tab expiry-regression fixture rather than a scheduler → exact-error technical write-up and an opt-in uploader-maintainer review using a reproducible Playwright/Uppy example → a fresh report exposes a concrete regression scenario, not a new browser limitation or regulatory deadline.

- **Direct job substitute:** [Playwright network and multi-page tests](https://playwright.dev/docs/network) already provide the building blocks. No absence of an existing upload-specific kit is claimed from empty search results.
- **Direct solution competitor:** [Uppy AWS S3](https://uppy.io/docs/aws-s3/) already covers signing, bounded uploads and multipart resume; [Uppy/Tus](https://uppy.io/docs/tus/) provides another resumable-upload architecture with configurable retries and server integration.
- **Indirect substitute:** a few native Web Locks calls, a hand-written regression, DevTools throttling and manual two-tab testing; HTTP/2 where the storage endpoint supports it.
- **Status quo:** keep the working one-slot fix and add a test if needed. That may be completely sufficient.
- **Narrowing result:** reject a replacement scheduler and generic upload SDK. Retain only the reusable regression-fixture hypothesis, with a native-test benchmark before any build promotion.
- **Distribution gate:** exact uploader workflow and content terms exist, but no established maintainer access, demonstrated search demand or repeatable conversion. **3/5**, not 4/5. No comments or outreach were sent.
- **Kill condition:** a short Playwright example covers the same cases with little setup, or independent maintainers do not report repeated regressions. Prefer an upstream example over a standalone product if that is enough.

### 2. HelloRoute — reject before scoring

**Wedge-first line:** Windows admin rolling out passwordless RDP to Windows 11 VMs → Microsoft's RDP authentication guides, native connection settings and certificate deployment → a fresh report shows confusion between PIN, connection-by-address and authentication routes, not a demonstrated tooling gap → proposed offline route selector for an operator-supplied connection profile → exact-error Intune/WHfB troubleshooting content, but repeatable access is unproven → [today's token-authentication-error report](https://www.reddit.com/r/sysadmin/comments/1xcyr61/rdp_token_authentication_error/).

- **Native/direct substitute check:** Microsoft's [WHfB RDP guide](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/rdp-sign-in) explains the certificate-backed route. Its [Entra remote-device guide](https://learn.microsoft.com/en-us/windows/client-management/client-tools/connect-to-remote-aadj-pc) explicitly documents the web-account option and hostname requirement; an IP address is not accepted for that route. [Remote Credential Guard](https://learn.microsoft.com/en-us/windows/security/identity-protection/remote-credential-guard) is a different Kerberos-based option with its own requirements, not a universal fallback.
- **Indirect substitute/status quo:** a native connection-profile checklist, administrator review and a controlled test; continue an approved working authentication route while investigating. Do not recommend weakening NLA or other security controls to make the proposed product useful.
- **Pain:** repeated inability to reach a legacy app is material. The thread contains competing diagnoses and no confirmed resolution; do not assert that a baseline policy caused the error.
- **Kill condition/result:** official documentation already answers the proposed selector's main questions, and no missed fleet workflow was established. Reject rather than package documentation as a generic diagnostic app.

### 3. PhotoStage — reject before scoring

**Wedge-first line:** Darktable film-scan editor working over a remote file mount → native local copies, manual staging and remote desktop → a [fresh report](https://www.reddit.com/r/selfhosted/comments/1xckt0h/advicetroubleshooting_remote_photography/) describes large-image transfer delays, but no proven failure of native staging → proposed selected-roll local cache with XMP return → Darktable remote-editing tutorials, a concrete workflow but no established access → today's remote-photography request.

- **Native/direct competitor check:** Darktable's [local copies documentation](https://docs.darktable.org/usermanual/development/en/overview/sidecar-files/local-copies/) explicitly covers working on a laptop away from main storage and synchronizing XMP sidecars back. This is essentially the proposed job. The fetched page is the development manual; verify the user's installed release before recommending exact UI behavior.
- **Indirect substitute/status quo:** manual selected-roll copying, a file-sync tool or remote editing on the storage-side workstation. The thread includes a remote-desktop workaround from another commenter. None makes the WAN faster.
- **Pain:** the reporter describes slow transfers and multi-second image loading. Units in the report are ambiguous; do not diagnose a bandwidth defect from those numbers or count their stated duplicate r/homelab post as another customer.
- **Kill condition/result:** the native feature already addresses the proposed caching workflow. Reject unless a specific unsupported conflict/sync case is demonstrated. Do not create a new photo-sync app on this evidence.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct test-job substitute | [Playwright](https://playwright.dev/docs/network) | Native network APIs and multiple pages can implement the proposed scenarios. The bar is reduced recurring setup/maintenance, not a claim that cross-tab tests are unavailable. |
| Direct underlying-problem competitor | [Uppy AWS S3](https://uppy.io/docs/aws-s3/) | Mature signing/concurrency/multipart workflow. Test its actual behavior before claiming a missing guarantee; documentation alone does not prove cross-tab behavior. |
| Alternative upload architecture | [Uppy/Tus](https://uppy.io/docs/tus/) | Resumability and retry controls, with a server component. A strong alternative when architecture changes are acceptable, not a drop-in identical presigned-URL flow. |
| Native primitive | [Web Locks](https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API) | Already supports same-origin work coordination; a small lock/sign/upload wrapper may solve the production problem. |
| Indirect substitute | DevTools throttling, native test plus fixture server, HTTP/2-capable endpoint | Existing tools and architecture changes may remove the need for a separate package. Manual testing is weaker regression protection but can be adequate for rare changes. |
| Status quo | Keep the reporter's working serialized just-in-time signing and fail-fast/resume behavior | Explicitly acceptable to the reporter. No speedup, automatic-retry preference or willingness to buy is inferred. |

No current-price advantage is asserted. No comparable pricing or willingness-to-pay evidence was established for this narrow kit.

## Wedge

The plausible addition is a **reusable, server-observed expiry regression fixture**, not another upload scheduler. It would keep application queue delay distinct from browser connection delay and make the failure visible in a small CI test without cloud credentials.

That gap is still hypothetical. Playwright already supplies the primitives, Uppy supplies a mature upload workflow, and the source author is happy with a small native fix. An upstream example may be the right output rather than a product. Competitive wedge/timing remains **2/5**; the fresh report does not justify inventing a durable market.

## Kill condition

Reject or fold into an upstream example if any of these prospective tests fire:

- A plain Playwright test plus small fixture server covers the same two-tab/expiry/cancellation cases with less than an hour of setup and negligible ongoing maintenance.
- Three independent uploader maintainers cannot identify a recurring regression or a missed release case that a reusable kit would prevent.
- An existing test or uploader configuration already handles the target scenario and adopters see no reason to add a dependency.
- Reproduction only works by mocking a browser queue rather than observing real server arrivals, or requires paid cloud accounts/production capabilities before local proof.
- A repeatable opt-in first-user route beyond one thread cannot be established.

These are planned validation criteria, not completed experiments or measured outcomes.

## Scoring

Only the narrowed winner is scored, after substitute checks and scope reduction.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Failed uploads block a core application action. Recurrence prevention is plausible but unvalidated; the current fix is already acceptable. |
| Feasibility | 4/5 | Small local server and Playwright adapter are feasible; real contention, timing, cancellation and integration correctness limit scope. |
| Demo potential | 4/5 | A labeled synthetic two-tab timeline can show an early-sign failure versus admission-first success. No demo was implemented in this research run. |
| Distribution | 3/5 | Specific uploader maintainers and exact-error content path exist; repeatable access and adoption are unproven. |
| Competitive wedge / timing | 2/5 | Native test tooling and a tolerable native production fix are strong substitutes. Fresh evidence is not a proven package gap. Weakest dimension. |
| Total | 17/25 | Below 18/25; Distribution also misses 4/5 and Wedge misses 3/5. |

## Decision

**Winner: UploadExpiryLab. Status: idea-only. No dedicated project repo created.**

Retain as a validation bet, not an immediate build recommendation. The evidence supports testing one concrete regression mechanism. It does not establish a standalone business, recurring demand or a defect in Uppy. The replacement-scheduler idea was killed rather than rescued with an inflated score.

## Next build step

Create one fixture-first comparison spike: a local HTTP/1.1 endpoint, two tabs in the same browser context, an intentionally early-signing uploader and an admission-first uploader; prove failure/success from fixture-server timestamps and compare setup effort with a plain Playwright example. Add one queued-cancel and one tab-close case. Label all generated scenarios synthetic, keep production/cloud credentials out, and stop at an upstream example if that meets the need.

Tracked validation: `apps-cjp`. Daily research: `apps-06q`.

## Source access caveats

- The canonical Reddit helper fetched eight r/sysadmin posts through **RSS fallback after public JSON HTTP 403**. RSS score/comment-count zero fields are placeholders, not engagement measurements.
- The r/selfhosted helper returned **HTTP 429** without usable posts. No tight retries were made. Direct public HTML extraction subsequently returned its new-post listing and the photography thread. A direct r/webdev HTML listing and the upload thread also worked; this is HTML fallback, not restored JSON/RSS access. Relative ages on HTML were used as displayed, not converted into invented exact timestamps.
- The winner's original HTML included comments and reporter follow-ups. Those are not a representative sample or independent confirmation of every technical suggestion. Unrelated fresh sysadmin posts were not used to pad the winner's evidence.
- `xurl whoami` succeeded; a small search returned **HTTP 401 Unauthorized**, and no OAuth2 token was available for a fallback. No X evidence is claimed. A public X-constrained search also returned no results.
- Date-constrained and broader Reddit web searches, plus a specific competitor search, all returned empty result sets. That does not demonstrate an empty market. Direct original Uppy, Playwright, MDN, AWS, Microsoft and Darktable pages supplied the usable substitute checks.
- Read-only research only. No social writes, customer outreach, production uploads, cloud API changes or tests against third-party storage were performed.
