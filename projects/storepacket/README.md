# StorePacket

StorePacket is a local-first release packet builder for solo mobile SaaS founders preparing a first App Store submission.

## Problem

First-time App Store submission is not one checklist. It crosses App Store Connect metadata, screenshots for required devices, privacy details, TestFlight/build readiness, subscriptions, tax/banking/legal setup, and review notes. Solo SaaS founders often discover those dependencies only after they are already trying to submit.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SaaS | https://www.reddit.com/r/SaaS/comments/1usgdcq/to_the_man_who_told_me_apple_would_be_an_easy/ | Fresh solo founder reports 72 hours and 50+ hours spent preparing App Store release details before being able to submit. |
| Apple App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy | App privacy answers affect the public product page and must be completed accurately. |
| Apple App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/upload-app-previews-and-screenshots | Screenshots and previews are separate required assets managed in App Store Connect. |
| fastlane deliver | https://docs.fastlane.tools/actions/deliver/ | Automation exists for uploading binaries, metadata, screenshots, and previews, but assumes the release packet is already organized. |
| Expo EAS Metadata | https://docs.expo.dev/eas/metadata/ | App-store presence automation exists, validating the pain of maintaining many store fields. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | AppConsul App Store Submission Checklist | Interactive checklist coverage is useful, but it is a generic web checklist rather than a repo-local packet with generated evidence, missing-asset report, and review-note drafts. |
| Direct competitor | PreFlight | AI compliance scanning targets rejection risk; StorePacket is narrower and earlier: assemble the first submission packet without uploading credentials or scanning private code. |
| Indirect substitute | Apple docs, App Store Connect, fastlane `deliver`, Expo EAS Metadata, screenshot generators | Strong once the founder knows every required artifact; weak at telling a first-time founder what is missing across metadata, privacy, screenshots, subscriptions, and review notes. |
| Status quo | Browser tabs, spreadsheet checklist, screenshots in folders, repeated App Store Connect form attempts | Wastes days, blocks launch, and increases risk of incomplete metadata or rejected review notes. |

## Wedge

StorePacket avoids the crowded "submit to the App Store" lane. It wins as a local, no-credentials release packet generator: one manifest in the repo, one missing-asset matrix, one Markdown/JSON handoff packet for App Store Connect and reviewer notes.

## Target user

Solo SaaS builders and small teams shipping their first iOS companion app, especially React Native/Expo or web-first founders who do not live in App Store Connect every week.

## MVP

- `storepacket init` creates a release manifest for app metadata, privacy answers, screenshot slots, subscriptions, build/test notes, and reviewer notes.
- `storepacket check` validates the manifest against a small ruleset and reports missing fields/assets.
- `storepacket packet` exports a Markdown/JSON submission packet with copy-paste App Store Connect fields, screenshot inventory, privacy answer checklist, and review-note draft.

## Non-goals

- Not submitting builds or metadata to Apple.
- Not storing App Store Connect API keys.
- Not promising App Review approval.
- Not replacing fastlane, Expo EAS, or App Store Connect.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
