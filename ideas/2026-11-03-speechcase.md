# Day 098 — SpeechCase

Date: 2026-11-03
Status: idea-only

## One-line pitch

A local-first disclosure-component retest app that keeps the exact markup variant, keyboard steps, environment versions and human-observed screen-reader announcements together across browser updates.

## Research brief

- **Decision:** retain a narrow manual-retest hypothesis, not build another accessibility scanner or screen-reader automation platform.
- **Target customer:** a small design-system team that already includes Windows Narrator in its release matrix and maintains disclosure buttons in several components.
- **Geography:** initially English-language web-component maintenance; no jurisdiction-specific compliance certification.
- **Category / substitutes:** ARIA-AT test plans and generated review pages, Assistiv Labs, Guidepup, a minimal HTML reproduction and a prepared issue template.
- **Time horizon:** a one-to-three-day local app only after a baseline comparison and maintainer validation.
- **Must-answer question:** does keeping component-specific variants and versioned observations together materially reduce repeated reproduction/retest work beyond existing test harnesses and an issue template?
- **Evidence bar:** a complete fresh community report plus original pattern and substitute documentation. No independent reproduction, buyer interviews, willingness-to-pay evidence or defensible market-size estimate yet.
- **Creative constraint:** “Subtract” — one interaction pattern and human observations, without a crawler, hosted testing fleet, AI diagnosis or automatic remediation.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public maintainer report; HTML retrieved 2026-11-03, displayed as less than one hour old | [Web Accessibility — Narrator bug logged](https://www.reddit.com/r/webdev/comments/1xmmxrq/web_accessibility_narrator_bug_logged/) | Author reports that a disclosure button using `aria-expanded` with `aria-controls` sometimes fails to announce expanded/collapsed state with Narrator in Edge/Chrome, while Firefox behaves differently. Reports filing Feedback Hub and Chromium issues but supplies no issue identifiers or versioned minimal reproduction in the visible post. This is an attributed observation, not a confirmed platform regression. |
| Same author's visible follow-up, not an independent customer | [Three affected components](https://www.reddit.com/r/webdev/comments/1xmmxrq/comment/19s2hyd3it42o/) | Author says the behavior had been treated as a quirk for some time, was present in three components, and has now been addressed by removing the attribute. Supports repeated component exposure but also supplies counterevidence: the author already has a workable change. It does not establish recurring paid-tool demand. |
| Original pattern guidance, recovered from the W3C-maintained source repository | [APG disclosure pattern source](https://raw.githubusercontent.com/w3c/aria-practices/main/content/patterns/disclosure/disclosure-pattern.html) | Specifies a button, accurate `aria-expanded` state and Enter/Space activation. `aria-controls` is optional for this disclosure pattern. That supports testing a minimal variant; it does not justify removing the attribute from every ARIA pattern or prove any browser is defective. |
| Original existing-harness documentation | [ARIA-AT](https://github.com/w3c-cg/aria-at) and [local development](https://github.com/w3c-cg/aria-at/blob/master/docs/LOCAL_DEVELOPMENT.md) | Already supplies manual assertions about screen-reader behavior, test plans, generated HTML/JSON and local review pages. Strong counterevidence to a generic “portable AT test case” product. The retrieved [support configuration](https://raw.githubusercontent.com/w3c-cg/aria-at/master/tests/support.json) lists JAWS, NVDA and VoiceOver for macOS; this file alone is not proof Narrator cannot be tested through another route. |
| Original commercial substitute documentation | [Assistiv Labs plans](https://www.assistivlabs.com/pricing) and [Narrator overview](https://www.assistivlabs.com/assistive-tech/screen-readers/narrator) | Already offers real Narrator access and AT/browser combinations; local-site testing is supported. Its pricing page visibly lists a $19/month Freelancer plan with 120 testing minutes, although the extracted billing toggle does not establish which billing cadence is selected. Existing access is not the missing feature; no subscription was purchased or product trial run. |
| Original automation-library documentation | [Guidepup README](https://github.com/guidepup/guidepup) | Advertises real screen-reader automation, spoken-phrase logs and Playwright integration; currently names NVDA, Orca and VoiceOver. This undermines a generic spoken-output recorder. It does not establish Narrator support or validate a Narrator result using a different reader. |

**Evidence confidence:** medium that real interaction-level compatibility work exists; low that a standalone retest app is needed. One fresh author, including their own follow-up, is not multiple independent buyers. Vendor capabilities are documentation claims, not tested comparisons. We have not measured weekly maintenance time or reproduced the reported behavior.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked before assigning any numeric score. Rejected candidates are not scored.

### 1. SpeechCase — narrowed and retained

**Wedge-first line:** design-system maintainer already testing Narrator across disclosure components → ARIA-AT review pages, Assistiv Labs sessions and a prepared reproduction issue → real AT access and assertions already exist, but carrying a particular component variant, exact steps and environment-tagged observations into later retests may still be awkward; that burden is unmeasured → a local disclosure-only variant/retest app, with human-entered speech observations rather than simulated speech → a concrete disclosure-reproduction recipe and reusable artifact for component-maintainer issue discussions where invited, followed by a maintainer-owned test-template integration if validated → a fresh report describes the same ambiguity across three components, with no verified new browser release or external deadline.

- **Direct / near-direct competitors:** ARIA-AT manual harness and review pages; Assistiv Labs real AT/browser testing and debugging environment.
- **Indirect substitutes:** Guidepup on supported readers; a minimal HTML page, issue template, version columns and screen recording where appropriate.
- **Status quo:** apply the author's already-working narrow workaround, document it in the component issue and manually retest. This may be entirely sufficient.
- **Gate result:** reject broad accessibility auditing, generic AT automation and a new remote browser fleet. Retain only the bounded, component-specific retest-continuity hypothesis; the advantage remains unvalidated.
- **Kill condition:** an ARIA-AT contribution or prepared issue template provides equivalent retest continuity with no material extra labor. Prefer that contribution over a new app.

### 2. SharedFactor — rejected before scoring

**Wedge-first line:** small IT team with an unavoidable SaaS owner account outside SSO → 1Password shared vault plus built-in one-time passwords → the fresh team has not yet adopted a password manager, rather than demonstrated a failure in existing shared-TOTP tooling → candidate was an owner-account MFA handoff app, but no unmet product wedge survives the check → a specific SaaS owner-account setup guide for IT teams, not a generic security launch → fresh confusion about the existing feature, not a new technical requirement.

- **Signal:** [How does everyone handle shared MFA for multiple users?](https://www.reddit.com/r/sysadmin/comments/1xmjrg9/how_does_everyone_handle_shared_mfa_for_multiple/), discovered via RSS and retrieved with visible comments. Author explicitly asks whether 1Password can do this; replies name existing password managers and discuss shared-account risks.
- **Direct competitor:** 1Password's [authenticator support](https://support.1password.com/one-time-passwords/) and [organization vault sharing](https://support.1password.com/create-share-vaults-teams/) already cover the proposed core mechanics.
- **Indirect substitute / status quo:** individually delegated accounts and MFA where the SaaS supports them; otherwise an approved vault/recovery procedure. Sharing a TOTP does not add individual attribution to the downstream SaaS account, and storing both factors in one vault changes the threat model.
- **Wedge and kill:** feature-discovery/onboarding problem, not evidence for another credential-holding service. Existing product solves the requested job. Reject; collect no secrets and build no TOTP relay.

### 3. SppCohort — rejected before scoring

**Wedge-first line:** operator updating a small HPE ESXi cluster → SPP process, vSphere Lifecycle Manager and OEM hardware support managers → one node reportedly lost iSCSI connectivity after an update, but reinstall/reboot reportedly restored it and no missing inventory capability is demonstrated → candidate was a before/after firmware/driver cohort review, not a firmware updater → a specific HPE/ESXi maintenance comparison guide for virtualization operators, with no established recurring acquisition route → a fresh maintenance incident, not a verified widespread SPP defect or new deadline.

- **Signal:** [HPE Servers, how often are you doing SPP updates?](https://www.reddit.com/r/sysadmin/comments/1xmm2u0/hpe_servers_how_often_are_you_doing_spp_updates/), discovered via RSS; full short post and visible replies retrieved. Author asks about cadence for five nodes and reports recovery, not a request for a new app.
- **Direct functional substitute:** Broadcom's [hardware support manager documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle/using-images-to-install-and-update-esxi-hosts-and-clusters/firmware-updates/hardware-support-managers.html) describes OEM integration, including HPE OneView for VMware vCenter, for firmware add-ons. Its lifecycle documentation also links image compliance, remediation prechecks and hardware compatibility checks. These do not promise that every vendor incident is prevented.
- **Indirect substitute / status quo:** a prepared maintenance worksheet, change record, native inventory and vendor support; retain the established maintenance procedure and investigate an isolated failure.
- **Wedge and kill:** a second firmware inventory/report wrapper has no demonstrated advantage. Reject absent repeatable operator evidence that native reports miss a consequential cross-node comparison. Do not label an SPP release unsafe, recommend a patch cadence, or infer root cause from recovery after several simultaneous actions.

## Problem

A component can expose the expected markup while a real screen-reader/browser combination announces something unexpected. A useful bug report or later retest needs the exact variant, focus/activation steps and environment, not just “works in Firefox.” When several components share the pattern, the same uncertainty can spread.

The source author has already made a change and reported the behavior. The remaining hypothesis is **repeated retest preparation and comparison**, not lack of knowledge about the optional attribute. We have not established that an issue template and a small fixture are insufficient.

**Status-quo pain test:** inaccessible state announcements can impede interaction and create release-quality or public accessibility risk. That consequence justifies investigating; no evidence here establishes a legal violation, a blocked sale, lost revenue or more than 30 minutes of weekly work. If the workaround and an issue record are tolerable, reject the app even though its UI is easy to build.

## Target user

A component-library maintainer responsible for several disclosure implementations who already performs real Windows Narrator checks before releases. Not a general website owner, an automated WCAG scanner buyer, or someone needing a replacement screen reader.

Start with one maintainer's own sanitized fixture. Do not assume ownership of arbitrary customer pages, access to private issue attachments or permission to record a user's screen-reader session.

## MVP scope

Proposed software, **not implemented or behavior-tested in this research run**:

1. A static local web app with a small, handwritten disclosure fixture: equivalent button/content variants with and without the optional `aria-controls`, plus explicit initial-state and Enter/Space steps. No remote script/CDN dependency or production-site modification.
2. A case manifest identifying component revision, fixture revision and intended semantic state transitions. Keep the variant itself separate from the observation UI so the recorder does not change focus or announcements during the test.
3. A manual result form recording Windows build, AT identity/version as available, browser version, locale, voice/verbosity, scan/focus mode, input steps and what the tester actually heard. Unknown values stay unknown; no automatic AT detection or speech extraction promise.
4. Per-step semantic outcomes: observed, not observed, unexpected, not tested and inconclusive. Store actual words separately; language, verbosity and settings make exact transcript equality a poor universal oracle. Distinguish initial focus announcement from announcement after activation.
5. Compare case revisions and observation runs without merging different environments into a single pass. Render escaped text and export local JSON plus a human-reviewed Markdown issue draft. Do not import or execute arbitrary HTML/JavaScript from a result bundle.
6. An accessible keyboard-operated recorder with labels and deliberate focus behavior; public fixtures contain only synthetic content. No telemetry, upload, automatic issue submission or account requirement.

**Non-goals:** automatic Narrator control; a speech recorder or transcription engine; browser-fleet provisioning; general WCAG certification; a claim that valid DOM/accessibility-tree output proves audible behavior; remediation advice across unrelated ARIA patterns. A virtual reader or another AT cannot reproduce a Narrator observation by proxy. Browser/AT causation needs a controlled actual-environment comparison.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | ARIA-AT test suite and generated review pages | Already models commands, settings and expected AT responses and can run locally. Benchmark an existing or minimally adapted plan before crediting a case-packaging wedge. Retrieved support configuration is scoped evidence, not an exhaustive platform-support audit. |
| Near-direct commercial competitor | Assistiv Labs | Already offers Narrator, AT/browser combinations, local-site access and debugging. A cloud-free case record is only potentially useful beyond these capabilities; do not claim remote Narrator testing is unavailable. |
| Indirect automation substitute | Guidepup | Real reader automation and spoken output logs for named supported readers. A different reader's passing test is not proof that Narrator works. |
| Indirect substitute | Minimal fixture plus prepared issue template | Strong free baseline: component revision, exact steps, environment, actual/expected behavior and rerun rows. May meet the entire need without another app. |
| Status quo | Apply the source author's narrow change and retain the issue/fixture | Author already removed `aria-controls` in three components. We must measure any continuing retest burden instead of treating a resolved workaround as unmet demand. |

## Wedge

A possible wedge is a deliberately small **component-variant and retest workflow** for teams that already have real AT access: it preserves enough context to compare later observations without implying that DOM assertions or an AI-generated transcript equal what a user hears.

This is a falsifiable product hypothesis, not a confirmed missing feature. The native/free baseline already has test assertions and local review pages; a simple issue template may be better. The source author's workable change weakens replacement demand. No evidence warrants another general accessibility platform.

## Kill condition

Reject the standalone app if any condition holds:

- An ARIA-AT plan/review-page contribution or a prepared fixture and issue template handles the same two-run comparison at equal or lower total effort.
- Three relevant maintainers cannot provide recurring retest cases, or fewer than two find a meaningful workflow improvement. Use a provisional benchmark of at least 30% less preparation-plus-retest-documentation time without dropping environment/step detail; this is a validation target, not a measured result.
- Observations cannot be reliably separated by mode, locale, versions and input sequence, or the UI interferes with the interaction being observed.
- Useful differentiation requires automatic Narrator speech capture, a hosted browser fleet, private-page uploads or generalized compliance judgments outside the bounded MVP.
- The only demand is for a one-off explanation of the optional attribute; publish a reproduction recipe instead.

## Scoring

Scores assigned after the competitor and narrowing gates above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Inaccessible state feedback matters, and the author reports three affected components. Recurring retest burden and actual user impact remain unmeasured. |
| Feasibility | 4/5 | A disclosure-only local form, manifest and comparison view is plausible in one to three days. Real environment testing remains manual; automation and broad fidelity guarantees are excluded. |
| Demo potential | 4/5 | Two fixture variants and environment-tagged observations can show the workflow clearly. Any simulated result must be labeled synthetic, not a reproduction of the source's report. |
| Distribution | 3/5 | Component-maintainer issue threads and a concrete disclosure test recipe identify a narrow audience. No proven template adoption, recurring maintainer access or repeatable first-user channel yet. |
| Competitive wedge / timing | 2/5 | Fresh report is timely, but ARIA-AT, Assistiv Labs, Guidepup and a prepared issue template are strong substitutes; the author already has a workaround. |
| Total | 17/25 | Below 18/25; both dimension gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** SpeechCase is the best retained validation hypothesis of this shortlist, not a recommendation to build a paid platform. Competitive wedge/timing is weakest at 2/5 versus the required 3/5; Distribution is 3/5 versus the required 4/5.

The evidence supports real-reader testing with explicit context rather than assuming markup is sufficient. It does not yet support a standalone app, market-size claim, universal attribute-removal advice or a confirmed Narrator/Chromium bug. Prefer contributing a reproducible test to an existing project if that solves the job.

## Next build step

One validation-sized commit, if this idea is taken forward: prepare a sanitized two-variant disclosure fixture and a versioned observation template, alongside the equivalent ARIA-AT/local-review or prepared-issue baseline. Ask three relevant component maintainers to perform an initial run and later rerun in their real environments; time preparation and documentation, and require two to meet the improvement target before app implementation. Record unknown outcomes explicitly. Do not invent reported browser/OS versions or vendor issue IDs. No outreach, actual AT trial or behavioral reproduction was performed this run.

Follow-up is tracked in Beads (`apps-cx3`), not as a Markdown task list.

## Source access caveats

- Canonical `reddit-readonly find` requested five new posts each from r/sysadmin, r/selfhosted and r/webdev, restricted to 48 hours. r/sysadmin public JSON returned HTTP 403 with a theme-beta body, and public RSS supplied five posts. RSS score/comment zeroes are unavailable-metadata placeholders, not engagement measurements.
- The same probe reported r/selfhosted and r/webdev JSON/RSS unavailable with HTTP 429; no tight retries. Subsequent HTML extraction recovered both new-post listings. The winner was discovered through recovered r/webdev HTML, not RSS or successful JSON.
- Full selected posts and visible comments were retrieved with HTML extraction. Collapsed replies were not exhaustively read. The winner's short post and author follow-ups were visible; there was no independently retrieved vendor issue to establish affected versions or root cause.
- `xurl whoami` succeeded; the read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured and no interactive authentication was attempted. An X-constrained web search returned no results; no X evidence is claimed.
- Multiple web searches, including known vendor/tool queries and Reddit-constrained queries, returned empty results. Treat search as degraded, not proof that competition or additional demand is absent. Original product documentation and public repository files were retrieved directly instead.
- W3C's rendered APG disclosure page hit an antibot extraction failure; its current maintained repository source supplied the pattern text. The ARIA-AT app returned no readable body; its repository, support configuration and local-development instructions were readable. A Guidepup introduction link returned a not-found page; its homepage and repository README supplied the cited capabilities.
- HPE's Smart Update landing page hit an antibot failure; the SPP candidate uses the complete public incident report and Broadcom's retrieved OEM integration documentation, not an inferred HPE feature gap. Two exploratory Microsoft printing-document paths returned 404 and were discarded; an inspected printer thread was not promoted into the shortlist or the winner's evidence.
- All research was public and read-only. No private component code, credentials, SaaS accounts, paid testing session or actual screen-reader output was accessed. Pricing and product capabilities above are retrieved documentation, not executed product tests.
