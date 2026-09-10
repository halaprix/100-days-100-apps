# Day 077 — FlagPassport

Date: 2026-09-10
Status: repo-created

## One-line pitch

A local, read-only CLI that turns Forge client feature-flag calls, possible
unauthenticated module exposure, and default values into a December 1, 2026
review packet before an anonymous visitor silently receives fallback UI.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Atlassian developer changelog | [Anonymous Forge client-SDK evaluation removal](https://developer.atlassian.com/changelog/) | Atlassian announced on September 2 that `FeatureFlags` in `@forge/bridge` will stop evaluating for unauthenticated users on December 1; calls without an `accountId` will fall back to defaults.[1] |
| Atlassian SDK guidance | [Client SDK vs server-side SDK](https://developer.atlassian.com/platform/forge/feature-flags/client-vs-server-sdk/) | The client SDK runs in Forge UI and sets the current user at initialization; server-side evaluation is a separate architecture with different semantics.[2] |
| Atlassian developer community | [Forge feature-flag docs mismatch](https://community.developer.atlassian.com/t/forge-feature-flag-docs-incorrect/100007) | A Marketplace partner reported a feature-flag documentation/code mismatch that Atlassian acknowledged and corrected, supporting conservative evidence rather than a blind search-and-replace.[3] |
| Atlassian Labs FSRT | [Forge Security Requirements Tester](https://github.com/atlassian-labs/FSRT) | An existing Forge static analyzer is a credible adjacent substitute; its published scope is common vulnerabilities, not a deadline-specific anonymous client-SDK exposure report.[4] |

## Problem

After December 1, 2026, a Forge UI app that initializes the client Feature Flags
SDK without an authenticated `accountId` no longer receives evaluated values; it
gets each flag's default. A partner has to find the relevant frontend calls,
check whether a module can render for an unauthenticated visitor, understand what
each default means in the UI, and document the test outcome. Documentation alone
does not join those facts across multiple apps.

The status quo passes the pain test for a Marketplace partner with public,
unlicensed, onboarding, or recovery routes: the default can silently alter a
customer-facing path, creating support load or blocking a sale. The job is not
worth a separate tool for an app with no client SDK use or no possible
unauthenticated route.

## Target user

A Jira or Confluence Marketplace partner whose Forge apps use `FeatureFlags`
from `@forge/bridge`, especially where a module may set `unlicensedAccess` or
otherwise render before an Atlassian account is available.

## MVP scope

- Read only explicit, user-supplied Forge project paths; do not discover
  accounts, scan a machine, execute project code, or call remote APIs.
- Detect `@forge/bridge` Feature Flags imports, initialization, and check
  defaults in TypeScript/JavaScript.
- Correlate candidates with manifest access settings; unsupported or ambiguous
  cases remain `manual-review` rather than safe.
- Emit redacted Markdown and JSON packets: source labels, possible exposure,
  default behavior, and authenticated/unauthenticated test matrix.
- Never copy source text, credentials, tenant IDs, or personal paths into output.

## Shortlist and wedge-first gate

1. **FlagPassport — selected.** Forge Marketplace partner using client
   `FeatureFlags` → Atlassian's change notice/docs, FSRT, Semgrep/custom rules,
   grep, and a manifest spreadsheet → none correlates client initialization,
   possible unauthenticated module exposure, flag default, and the required test
   in one local artifact → deadline-specific exposure packet → September
   changelog/search traffic, Forge developer community threads, and
   Marketplace-partner migration content → anonymous evaluation ends December 1,
   2026. **Kill:** five affected partners can complete the official-doc review in
   under 15 minutes, or FSRT/an established Forge tool releases the same
   client/manifest/default report.
2. **Connect EOS customer-notice copy checker — rejected.** Connect-to-Forge
   vendor preparing admin migration URLs → Atlassian's customer-notice guidance,
   migration consultancies, and manual copy review → a notice checker cannot
   prove the wider technical migration is safe → narrow content completeness
   lint → vendor migration documentation searches → current rollout is timely,
   but the buyer already has authoritative templates and the status-quo pain is
   not proven. **Kill:** no evidence of recurring notice-copy errors beyond
   normal editorial review.
3. **Indie-product catalogue rail — rejected.** Maker with several launched
   products → product-recommendation widgets, custom footer links, analytics,
   and manual cross-promotion → existing widgets already surface related products
   and the new tool would need behavioral data to outperform them → maker-owned
   lightweight product rail → one SideProject post and generic maker channels →
   the post reports lost cross-product discovery, but no defensible narrow
   distribution or substitute failure was verified. **Kill:** generic
   recommendation widgets and a static link list are good enough.
4. **Agent home-screen card contract checker — rejected.** Personal-agent
   builder with iOS widgets → Glance and generic agent dashboards → a fresh
   SideProject launch already demonstrates an actively shipping direct solution;
   no interoperability demand was shown → widget-schema validator → generic
   agent-builder audience → no concrete wedge or repeatable acquisition path.
   **Kill:** direct product already serves the stated workflow and the evidence
   is a launch, not a request for validation tooling.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Atlassian feature-flags documentation and change notice | Authoritative on the deadline and implementation choices, but it does not inventory client calls, manifest exposure, defaults, and manual test evidence across a project.[1][2] |
| Direct competitor | FSRT | A Forge static analyzer for common vulnerabilities. It can scan a project but its published scope is security requirements, not this dated client-SDK behavior change.[4] |
| Indirect substitute | Semgrep/custom AST rule, grep, manifest review, and spreadsheet | Can find an import, but the client/manifest/default correlation and a reviewable test record are recreated manually. |
| Status quo | Wait for a logged-out route to receive fallback defaults, then inspect the path under customer or support pressure | A default can quietly hide or expose the wrong UI route rather than generate an obvious deployment failure. |

## Wedge

FlagPassport is deliberately not a generic static-analysis wrapper. It produces
one evidence-bearing decision: where a dated vendor change meets client SDK
usage, possible unauthenticated module exposure, and each default's UI effect.
It remains local and input-scoped, lowering trust friction for Marketplace
partners. The first-user channel is concrete: deadline-specific Atlassian
changelog/search content and focused Forge developer-community and
Marketplace-partner discussions.

## Kill condition

Stop or narrow FlagPassport if five affected Marketplace partners can complete a
reliable, reviewable vendor-guided check in under 15 minutes, or if FSRT,
Semgrep's Forge ecosystem, or another established scanner ships the same
client/manifest/default packet. Also stop if real projects require credentialed
remote inventory before the local report is useful.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A silent fallback can alter a public/unlicensed/onboarding path and create sales or support harm; the exposed population is narrow. |
| Feasibility | 5/5 | Explicit-path parsing of manifests and JS/TS plus deterministic Markdown/JSON output is a small local CLI MVP. |
| Demo potential | 5/5 | A mixed Forge fixture set becoming an exposure packet and test matrix is immediately legible. |
| Distribution | 4/5 | Specific Forge Marketplace partners can be reached through deadline searches, Atlassian developer-community threads, and targeted migration content. |
| Competitive wedge / timing | 4/5 | The December 1 change gives a fixed reason now; vendor docs and FSRT are strong alternatives, but neither is this narrow correlation/reporting job. |
| Total | 22/25 | Clears the repository threshold and both dimension gates. |

## Decision

**repo-created.** FlagPassport scores 22/25 with Distribution at 4/5 and
Competitive wedge/timing at 4/5. A local dedicated scaffold and public-safe
snapshot were created at [`projects/flagpassport`](../projects/flagpassport).
No dedicated GitHub remote was created or claimed.

## Next build step

Implement fixture-driven detection for `@forge/bridge` client initialization and
manifest `unlicensedAccess`, then prove that anonymous-account absence results in
a `manual-review` packet rather than an automatic-safe verdict.

## Source access caveats

Reddit JSON returned the documented `403` theme-beta response. The read-only tool
used RSS fallback for the r/SideProject probe and retrieved fresh posts; earlier
query filtering found no candidate. Follow-up r/SaaS, r/sysadmin, r/selfhosted,
and r/webdev feed probes returned `429` and were not retried. The fresh
SideProject posts informed rejected alternatives only; this selected Forge bet
does not claim Reddit validation.

The `xurl` identity probe succeeded, but the default profile had no OAuth2 token
and the read-only search probe returned `401 Unauthorized`; no X signal is used.
The selected evidence is public Atlassian documentation, community discussion,
and the public FSRT repository retrieved directly from the web.

## Sources

[1] https://developer.atlassian.com/changelog/ — Atlassian developer changelog

[2] https://developer.atlassian.com/platform/forge/feature-flags/client-vs-server-sdk/ — Client SDK vs server-side SDK

[3] https://community.developer.atlassian.com/t/forge-feature-flag-docs-incorrect/100007 — Forge Feature Flag Docs Incorrect?

[4] https://github.com/atlassian-labs/FSRT — Forge Security Requirements Tester
