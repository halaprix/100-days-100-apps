# PackageProof

PackageProof is a local Android release preflight that turns package IDs,
signing-certificate fingerprints, distribution routes, and verification
requirements into a reviewable packet before Android developer-verification
enforcement begins on September 30, 2026.

## Problem

Android developer verification makes package-name registration and the signing
certificate's SHA-256 fingerprint operational release data. Small publishers
with legacy package names, product flavors, or direct distribution need to
reconcile those details before release rather than discovering an unresolved
package at the console.

PackageProof is deliberately not a console client. It checks the local artifact
and an explicit route inventory, then states the official next action.

## Target user

Android developers and small release teams with an app distributed outside
Google Play, or Play apps with residual/legacy direct-distribution package IDs.

## MVP

- Inspect a user-selected APK and local route file.
- Read its package ID and signing-certificate SHA-256 fingerprint.
- Report missing or conflicting fingerprints, duplicate package IDs, unknown
  routes, and the matching Android Developer Console or Play Console action.
- Produce deterministic Markdown and JSON with official documentation links.

## Non-goals

- No Google, Play, or Android Developer Console login, API call, or automation.
- No keystore read, signing action, APK upload, identity verification, or
  registration submission.
- No claim that a local preflight proves an app is registered or installable.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Android Developers | https://developer.android.com/developer-verification | Enforcement starts September 30, 2026 for participating stores in Brazil, Indonesia, Singapore, and Thailand; expansion is planned globally in 2027. |
| Android Developer Console guide | https://developer.android.com/developer-verification/guides/android-developer-console | Off-Play registration requires package name and SHA-256 certificate fingerprint, with APK ownership proof for existing names in some cases. |
| Google Play Console guide | https://developer.android.com/developer-verification/guides/google-play-console | Developers must register remaining packages by September 30, 2026 to avoid removal/disrupted installation. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Android Developer Console | Required official registration surface for off-Play apps. PackageProof prepares data; it never replaces registration. |
| Direct competitor | Google Play Console | Required official Play registration surface; automatically covers most apps. |
| Indirect substitute | `apksigner`, Gradle, spreadsheets, release notes | Supply fragments but not a reconciled artifact-to-route packet. |
| Status quo | Manually compare artifact metadata and console tabs at release time | Risks discovering mismatched package/fingerprint data during a deadline-bound release. |

## Wedge

A credential-free, artifact-first packet for a narrow decision: whether a local
release artifact and its declared distribution route have the data needed for
the correct native-console verification path. It complements the official
consoles instead of cloning them.

## Status

`v0.1.0-alpha.0` — scaffold and specification only. No remote is configured.
