# SPEC — StorePacket

## User story

As a solo mobile SaaS founder preparing a first App Store release, I want a local release packet that shows every missing submission artifact before I open App Store Connect, so that I can avoid days of scattered checklist work and avoid preventable metadata/review delays.

## Core flow

1. Run `storepacket init` in the app repo.
2. Fill `storepacket.yaml` with product metadata, support URLs, privacy answers, screenshot inventory, build notes, subscription details, and reviewer notes.
3. Run `storepacket check` to get a missing-asset matrix with severity and links to authoritative docs.
4. Run `storepacket packet` to export a Markdown/JSON handoff packet for App Store Connect.

## Data model

```yaml
app:
  name: string
  bundle_id: string
  sku: string
  category: string
  description: string
  keywords: [string]
  support_url: string
  marketing_url: string
  privacy_policy_url: string
privacy:
  collects_data: boolean
  data_types: [string]
  tracking: boolean
screenshots:
  locales:
    en-US:
      iphone_6_9: [path]
      iphone_6_5: [path]
      ipad_13: [path]
subscriptions:
  products:
    - id: string
      display_name: string
      review_screenshot: path
review:
  demo_account: string
  notes: string
  contact: string
build:
  version: string
  testflight_checked: boolean
```

## Technical approach

- Start as a small Python CLI using `argparse` and `PyYAML`.
- Keep all checks offline and deterministic.
- Store rule definitions in versioned YAML/JSON so Apple-doc-derived rules can evolve.
- Output Markdown for humans and JSON for automated tests.
- Include fixtures for a complete packet and an intentionally incomplete packet.

## Validation plan

- Fixture tests: incomplete packet must produce deterministic missing items.
- Snapshot tests: generated Markdown packet is stable and redactable.
- Manual validation: compare the checklist against Apple App Store Connect Help pages for privacy and screenshots, fastlane deliver, and Expo EAS Metadata.
- Wedge validation: ask first-time iOS SaaS builders whether the generated packet would have saved more than 30 minutes before their first submission.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — runnable CLI with manifest parsing and basic checks.
- v0.2.0-alpha.1 — complete sample packet, docs links, and demo GIF.
