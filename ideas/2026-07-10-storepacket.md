# Day 022 — StorePacket

Date: 2026-07-10
Status: repo-created

## One-line pitch

StorePacket is a local-first release packet builder that helps solo mobile SaaS founders assemble App Store submission metadata, screenshots, privacy answers, subscriptions, and reviewer notes before losing days inside App Store Connect.

## Source access caveat

Reddit public JSON returned the known `theme-beta` HTTP 403 block for thread fetches, so this run used the reddit-readonly RSS fallback for usable Reddit signals. Several subreddits also hit RSS HTTP 429 and were treated as unavailable rather than retried in a loop. X authentication worked for `whoami`, but X search returned HTTP 401 Unauthorized, so X did not contribute usable search evidence.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SaaS | https://www.reddit.com/r/SaaS/comments/1usgdcq/to_the_man_who_told_me_apple_would_be_an_easy/ | Fresh solo founder reports 72 hours and 50+ hours spent preparing App Store release work: TestFlight, App Store Connect, subscriptions, tax forms, banking, privacy disclosures, screenshots, legal agreements, and review information. |
| Apple App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy | App privacy answers are required public product-page disclosures, not optional copy. |
| Apple App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/upload-app-previews-and-screenshots | Screenshots and app previews are separate App Store Connect assets that must be managed per platform/status. |
| fastlane `deliver` | https://docs.fastlane.tools/actions/deliver/ | Existing automation can upload screenshots, metadata, previews, and binaries, which validates the artifact-management pain but assumes the packet is already organized. |
| Expo EAS Metadata | https://docs.expo.dev/eas/metadata/ | Expo documents that app-store presence requires “a lot of information” before users can use the app, validating the multi-field release-prep burden. |
| AppConsul checklist | https://appconsul.com/tools/app-store-submission-checklist/ | Interactive submission checklists already exist, so the wedge cannot be “a checklist”; it must be a local packet/report that works before credentials or upload automation. |
| PreFlight | https://preflight.build/ | AI-powered App Store compliance scanners exist, so StorePacket must stay narrower: prep and inventory, not broad approval prediction. |

## Problem

First-time App Store submission is a launch blocker for web-first and SaaS-first founders. The work spans metadata, screenshots, privacy details, subscriptions, build readiness, TestFlight, reviewer notes, legal/tax/banking setup, and public URLs. The status quo is a pile of browser tabs, folders, spreadsheets, and repeated App Store Connect attempts.

The pain clears the status-quo test because it can burn multiple days, block a launch, and create preventable rejection risk from incomplete metadata or weak reviewer notes.

## Target user

Solo SaaS founders and small teams shipping their first iOS companion app, especially React Native/Expo or web-first builders who do not operate inside App Store Connect every week.

## Shortlist gate

| Candidate | Wedge-first line | Decision |
|---|---|---|
| StorePacket | Solo mobile SaaS founder preparing a first App Store release → Apple docs/App Store Connect/Fastlane/Expo/checklists → existing tools upload or list requirements but do not create one repo-local missing-asset packet before credentials and submission → no-credentials manifest checker plus Markdown/JSON handoff packet → App Store submission SEO, r/SaaS, r/iOSProgramming, Expo/React Native launch-post replies → fresh post reports 72 hours and 50+ hours of release-prep pain now. | Winner; clears repo gate. |
| TwilioPayload Tutor | Student building a WhatsApp bot → Twilio docs, Twilio Console, Postman, webhook testers → broad docs scatter payload shape, webhook signatures, media examples, and sandbox flow → WhatsApp-sandbox-only payload replay recipes and explainer CLI → webdev/student Twilio queries → fresh r/webdev confusion about unclear Twilio docs. | Idea-only; useful but smaller pain and several webhook simulators already cover much of the job. |
| NoAI Gallery Starter | Photographer wanting a simple portfolio that discourages AI scraping → WordPress/SmugMug/robots.txt/Cloudflare/Glaze/ArtShield → defenses are partial and easy to overpromise → transparent static-site starter with best-effort crawler headers, metadata, watermarking, and plain-language caveats → webdev plus photographer communities → fresh post asks for cheap site while keeping AI scrapers out. | Idea-only; trust/claims are risky and anti-scraping guarantees are weak. |
| HARLetter | Customer debugging a broken warranty portal → DevTools, HAR export guides, Google HAR Analyzer, vendor support tickets → nontechnical users cannot safely redact and explain network evidence → local HAR sanitizer plus vendor-ready bug report letter → support/community troubleshooting replies → fresh webdev post shows user manually reverse-engineering a broken portal. | Idea-only; privacy/liability edge needs sharper validation. |
| RFP Answer Agent for MSPs | MSP/security team answering RFPs and security questionnaires → Conveyor/Vanta/Loopio/Responsive/SafeBase/trust centers → funded incumbents already target the exact job → only possible wedge would be tiny MSP offline docs, but that is not proven → MSP communities/search → fresh r/SaaS founder asks if the pain is real. | Rejected; crowded security-questionnaire category with strong incumbents. |

## MVP scope

- `storepacket init` creates a local `storepacket.yaml` manifest for app metadata, privacy answers, screenshot slots, subscription/review evidence, build notes, and reviewer contact details.
- `storepacket check` validates required fields and assets against a small offline ruleset and outputs a missing-asset matrix with doc links.
- `storepacket packet` exports a Markdown and JSON submission packet with copy-paste fields, screenshot inventory, privacy checklist, subscription review notes, and reviewer-note draft.
- Include complete and incomplete fixtures so the demo can show a before/after packet without needing App Store Connect credentials.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | AppConsul App Store Submission Checklist | Covers the checklist angle, but it is a generic web checklist rather than a repo-local manifest, missing-asset report, and exportable submission packet. |
| Direct competitor | PreFlight | Targets AI-powered App Store compliance/rejection risk; stronger and broader, but higher-trust and later-stage than a no-credentials packet prep tool. |
| Direct competitor | fastlane `deliver`, Expo EAS Metadata | Automate upload/metadata management for teams ready to wire credentials and store config; they do not primarily help first-time founders discover and assemble the packet before submission. |
| Indirect substitute | Apple docs, App Store Connect forms, screenshot generators, spreadsheets, Notion checklists | Works if the founder already knows every required artifact; weak when the blocker is cross-form completeness and handoff clarity. |
| Status quo | Keep tabs open, fill App Store Connect manually, export screenshots repeatedly, write reviewer notes at the end | Can waste days and block release. Incomplete privacy answers, screenshots, review notes, or subscription evidence can delay launch. |

## Wedge

StorePacket is deliberately not an App Store uploader and not an approval predictor. The wedge is the pre-submission packet: a local, no-credentials manifest checker that turns scattered release prep into a missing-asset report and copy-paste submission handoff before the founder opens App Store Connect.

## Kill condition

Kill or narrow the idea if first-time mobile founders say AppConsul-style checklists plus Expo/Fastlane already save the painful part, or if Apple/Expo tooling exposes a simple official export/check command that produces the same cross-field missing-asset packet. Also kill any scope that requires storing App Store Connect credentials in the MVP.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | The source signal claims 50+ hours and a blocked submission path; the problem can delay revenue and launch timing. |
| Feasibility | 4/5 | A deterministic manifest checker and Markdown/JSON exporter is buildable in 1–3 days; keeping rules current is the hard part. |
| Demo potential | 4/5 | Missing-asset matrix and generated submission packet are screenshot/GIF-friendly. |
| Distribution | 4/5 | Concrete first-user path: App Store submission SEO, r/SaaS launch-post replies, iOS/Expo/React Native communities, and “first iOS app submission” content. |
| Competitive wedge / timing | 3/5 | Existing checklists, compliance tools, and upload automation are real; the narrower no-credentials packet-prep wedge is credible but not huge. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create the dedicated repo because StorePacket scored 20/25, Distribution is 4/5, and Competitive wedge / timing is 3/5.

Repo: https://github.com/halaprix/storepacket

## Next build step

Implement `storepacket check` with two fixtures: one complete first-submission packet and one incomplete packet that flags missing privacy, screenshot, subscription review, and reviewer-note fields.
