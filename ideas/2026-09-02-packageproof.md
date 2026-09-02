# Day 069 — PackageProof

Date: 2026-09-02
Status: repo-created

## One-line pitch

A local Android release preflight that turns package IDs, signing-certificate
fingerprints, distribution routes, and verification requirements into a
reviewable packet before the September 30 Android developer-verification milestone.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Android Developers — developer verification | https://developer.android.com/developer-verification | Original platform documentation says enforcement begins September 30, 2026 for installs from participating stores in Brazil, Indonesia, Singapore, and Thailand on certified Android 7+ devices, with global expansion in 2027. |
| Android Developers — Android Developer Console guide | https://developer.android.com/developer-verification/guides/android-developer-console | Off-Play distributors must register package names, provide a SHA-256 signing-certificate fingerprint, and sometimes prove ownership by uploading a signed APK. The guide also names APIs for verification and package registration. |
| Android Developers — Google Play Console guide | https://developer.android.com/developer-verification/guides/google-play-console | Play developers must check and register any remaining package names by September 30, 2026 to avoid global removal from Google Play and disruption to installation. |

## Problem

A small Android publisher can have several application IDs, product flavors, old
signing keys, and a mix of Play and direct distribution. The new verification
flow makes the package name and the signing-certificate fingerprint operational
release data: a wrong pairing or an unregistered residual package can block a
launch or removal-free distribution path.

The native consoles perform registration, but a developer still has to reconcile
what the built artifact is signed with, which package each distribution route
uses, and which console action is needed. That is a release-blocking task rather
than a generic compliance dashboard. This run has strong first-party deadline
and workflow evidence, but no fresh buyer thread measuring weekly time loss.

## Target user

An Android developer or small mobile release team that ships one or more apps
outside Google Play, or maintains Play apps with legacy/direct-distribution
package IDs and signing keys.

## MVP scope

- Read user-selected APK metadata and an explicit local route file; never read a
  keystore or call a console.
- Extract package name and signing-certificate SHA-256 fingerprint using local
  Android build tooling, then compare them with the supplied route inventory.
- Render a Markdown/JSON packet that labels each package as Play-only,
  direct-distribution, unknown, or conflict; lists the required native-console
  action; and links to the relevant official guide.
- Flag duplicate package IDs, missing fingerprints, debug-signed release
  artifacts, and route declarations that cannot be reconciled.
- Ship synthetic fixtures only. No identity verification, APK upload, signing,
  console automation, credential handling, or claim of registration success.

## Shortlist and wedge-first gate

1. **PackageProof — selected.** Android publisher with legacy/direct-distribution
   packages → Android Developer Console, Play Console, `apksigner`, build notes,
   and a spreadsheet → native surfaces register packages but do not reconcile a
   shipped artifact, route inventory, and required verification action into one
   preflight → local, read-only package-to-certificate release packet → Android
   verification deadline searches, Android developer communities, Gradle/CI
   examples, and fixture-led release-check content → September 30 enforcement
   begins in four countries and the platform documents global expansion in 2027.
   **Kill:** Google’s native console/API or a maintained plugin already generates
   the same artifact-to-route packet, or five affected developers report that
   manual reconciliation is under 30 minutes per release cycle.
2. **SharedSleepPacket — rejected.** Intune administrator debugging one shared
   Windows desktop that powers off after sleep → Intune, Event Viewer, power
   reports, OEM support, and a manual case log → the workflow is frustrating but
   the fresh r/sysadmin RSS report is a single device-specific incident; a generic
   diagnostic wrapper has no demonstrated wedge → a support-ready evidence packet
   → Intune/Windows support searches → one fresh report. **Kill:** the thin,
   non-repeatable evidence and existing native diagnostics do not support a
   buildable differentiated product.
3. **SeniorMap — rejected.** Engineer choosing interview-study topics → curated
   roadmaps, bookmarks, and the author’s 573-topic knowledge base → those
   substitutes already organize content, while the fresh post describes a maker’s
   finished resource rather than a painful, repeated buyer workflow → role-specific
   gap map → engineering-career content → no evidence of a >30-minute weekly
   status-quo cost. **Kill:** this is a crowded learning-content category without
   a concrete first-user path.
4. **TripBudgetGuard — rejected.** Traveler checking itinerary affordability →
   booking sites, spreadsheets, and AI planners → itinerary/budget tools are
   crowded and the fresh SideProject post is another builder launch, not proof of
   a narrow unmet workflow → deterministic transit-buffer budget check → travel
   communities → no evidence that a new entrant can beat established planners.
   **Kill:** reject-by-default crowded AI travel-planning category with no concrete
   distribution wedge.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Android Developer Console | The official surface verifies identities and registers off-Play package names, fingerprints, and ownership challenges. It is mandatory infrastructure, not something the MVP replaces. |
| Direct competitor | Google Play Console | The official Play path automatically registers most apps and lets developers check/register remaining package names. It is the default for Play distribution. |
| Direct competitor | Android Developer Console / Developer ID Status APIs | Google documents APIs for eligibility, package registration, and key management. A credentialed CI integration could absorb parts of the workflow, so PackageProof must remain useful before console/API access. No maintained standalone artifact-to-route preflight was found in the public web scan; absence is not proof it does not exist. |
| Indirect substitute | `apksigner`, Android Studio/Gradle output, spreadsheets, release notes | These expose pieces of the truth but leave the developer to join package, certificate, distribution route, deadline, and console action manually. |
| Status quo | Open console tabs and reconcile artifact metadata by hand at release time | Tolerable for one new Play app, but risky for legacy/direct packages: the deadline and potential removal/install disruption turn a missed pairing into a blocked release or public failure. |

## Wedge

PackageProof does not compete with identity verification, registration, or an app
store. It sits before them: a deterministic, credential-free proof that the
artifact about to ship, its signer fingerprint, and its intended distribution
route are coherent and have an explicit native-console next step. The narrow
artifact-to-route output is reviewable in a release PR and feasible without
asking a developer to grant a third party access to their console or keys.

The wedge is time-bound and only credible while teams are reconciling package
inventories ahead of enforcement. Google’s documented APIs are the main risk:
if they offer the same local-ready packet, this should become a small plugin or
be rejected rather than expanded into a console clone.

## Kill condition

Reject or narrow the bet if a documented Google console/API flow or maintained
Gradle plugin already accepts a local APK plus route inventory and renders the
same package/fingerprint/action matrix. Also reject if five direct-distribution
or multi-package Android publishers say manual reconciliation takes less than 30
minutes per release cycle and has not caused a delayed release, distribution
failure, or signing-key confusion.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The consequence is a blocked launch, removal, or installation disruption; the timing is first-party documented, though direct buyer-frequency evidence is still thin. |
| Feasibility | 5/5 | APK inspection, explicit local route data, deterministic checks, and Markdown output fit a 1–3 day local CLI MVP. |
| Demo potential | 5/5 | A synthetic release artifact can visibly change from a missing fingerprint/route conflict to a release packet with clear next actions. |
| Distribution | 4/5 | Specific Android developers are actively navigating the named verification paths; release-check examples can target deadline, package-registration, signing-fingerprint, and direct-distribution searches plus Android developer communities. |
| Competitive wedge / timing | 3/5 | The September 30 milestone is concrete and the credential-free preflight is narrower than native consoles, but Google’s APIs and console may reduce the wedge. |
| Total | 21/25 | Clears the 18/25 threshold and both dimension gates. |

## Decision

**repo-created.** PackageProof clears the threshold (21/25), Distribution (4/5),
and Competitive wedge / timing (3/5). A local dedicated repository and a
public-safe master-index snapshot were created. The project has no dedicated
remote; the master index is the public record for this scaffold.

## Next build step

Implement `packageproof inspect` against a synthetic APK fixture and explicit
route YAML, then test that it emits actionable findings for a missing certificate
fingerprint, a duplicate package ID, and an unknown distribution route.

## Source access caveats

Reddit public JSON was blocked; RSS fallback returned fresh entries only for
r/SideProject and r/sysadmin, while r/SaaS and r/webdev reached HTTP 429. Those
entries did not substantiate the selected Android-verification workflow, so no
Reddit source is used as winner evidence. The `selfhosted` and `Entrepreneur`
probe also returned HTTP 429 and was not retried.

X `xurl` authentication status showed no OAuth 2 token. A read-only search probe
returned `401 Unauthorized`, so no X evidence is claimed. The winner rests on
current first-party Android documentation, not inferred social engagement.
