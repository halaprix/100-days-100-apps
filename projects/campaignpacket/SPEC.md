# SPEC — CampaignPacket

## User story

As a small-business Microsoft Teams Phone admin, I want a local preflight report for my Teams SMS / 10DLC campaign fields, so that I can fix missing CTA, privacy, terms, HELP/STOP, and sample-message details before resubmitting a rejected campaign.

## Core flow

1. User runs `campaignpacket check --fixture rejected-cta` for a demo or `campaignpacket check campaign.yaml` for a local campaign packet.
2. The CLI parses campaign description, target audience, opt-in method, CTA copy, privacy-policy URL notes, terms URL notes, sample messages, HELP response, STOP response, and declared content attributes.
3. It applies documented Teams SMS / 10DLC rules for required disclosures, voluntary opt-in, message type, message frequency, brand consistency, HELP/STOP instructions, privacy-policy language, and UCaaS low-volume limitations.
4. It emits a Markdown report and JSON findings with severity, missing evidence, suggested rewrite prompts, and resubmission checklist items.
5. It redacts phone numbers, addresses, client names, and private business details when producing a support-safe report.

## Data model

```text
CampaignPacket
- brand_name: string
- use_case: string
- target_audience: string
- campaign_description: string
- opt_in_method: web_form | text_keyword | verbal | paper | other
- call_to_action: string
- privacy_policy_url: optional string
- privacy_policy_notes: optional string
- terms_url: optional string
- terms_notes: optional string
- sample_messages: list<string>
- help_message: string
- stop_message: string
- content_attributes: ContentAttributes

ContentAttributes
- links: bool
- phone_numbers: bool
- marketing: bool
- automated_alerts: bool
- age_gated: bool

Finding
- severity: info | warning | blocker
- code: string
- field: string
- message: string
- evidence: string
- recommendation: string

Report
- generated_at: string
- packet_summary: object
- findings: list<Finding>
- resubmission_checklist: list<string>
- redactions: list<string>
```

## Technical approach

- Start as a tiny Python CLI using only the standard library.
- Use YAML if available, but support JSON fixtures without dependencies for the first alpha.
- Keep rule definitions explicit and versioned so compliance assumptions are reviewable.
- Never call Microsoft, carrier, or SMS-provider APIs in the MVP.
- Generate deterministic Markdown and JSON for easy screenshots, PR review, and search-indexable examples.
- Treat output as a preparation aid, not legal advice or approval guarantee.

## Validation plan

- Unit-test fixture scans for missing CTA disclosures, bundled consent, missing privacy/terms links, malformed HELP/STOP responses, sample-message/brand mismatch, and unsupported Teams SMS use cases.
- Test redaction against phone numbers, street addresses, email addresses, client names, and private business examples.
- Run `python3 scripts/verify_scaffold.py` in CI until the CLI exists; then replace/add a fixture smoke test.
- Validate wedge by answering public support/search queries with a synthetic packet example and checking whether admins can map the report to their rejected campaign.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and specification.
- v0.1.0-alpha.1 — fixture-driven CLI with Markdown/JSON output.
- v0.2.0-alpha.1 — local campaign file parser with rule coverage and redaction tests.
- v0.3.0-alpha.1 — report templates for Teams Admin Center resubmission packets.
