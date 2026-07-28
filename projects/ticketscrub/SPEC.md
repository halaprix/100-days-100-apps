# TicketScrub Specification

## User story

As a Jira admin or security lead, I want users warned about obvious PII and secrets before they create or update a ticket, so sensitive data does not enter Jira unless there is a conscious exception.

## Feature list

### v0 prototype

1. Local fixture that mimics Jira issue create/comment fields.
2. Browser extension content script that discovers configured text fields.
3. Rule engine for:
   - credit card-like numbers with Luhn check,
   - SSN-like identifiers,
   - IBAN-like identifiers,
   - API tokens and private keys,
   - passwords in pasted email threads,
   - over-broad forwarded email dumps.
4. Inline warning panel with severity, category, matched snippet preview, and redaction suggestion.
5. Submit interception with `submit anyway` reason capture in local demo mode.
6. Admin policy JSON with enabled detectors and custom regexes.
7. Markdown report export for the demo run.

### Later

- Jira Cloud content-script hardening.
- Forge UI Modifications proof-of-concept.
- Attachment and screenshot OCR spike.
- Per-project policy packs.
- Admin allowlist/false-positive workflow.

## Data model

```text
Policy
- version
- detectors[]
- custom_patterns[]
- allowlist[]
- severity_overrides{}

Finding
- id
- detector
- severity
- field
- start/end offsets
- preview
- suggestion

Decision
- finding_ids[]
- action: block | redact | submit_anyway
- reason
- timestamp
```

## Build plan

1. Create fixture HTML form with Jira-like issue fields.
2. Implement detector library in TypeScript.
3. Add content script that scans on input and before submit.
4. Render inline warnings and redaction suggestions.
5. Export policy JSON and Markdown demo report.
6. Add tests for detectors and submit-blocking behavior.

## Validation plan

- Unit tests for each detector.
- Fixture browser test that pastes a risky email thread and confirms submit is blocked.
- Fixture browser test that redacted content submits.
- Manual review for false positives on benign ticket text.
- Public-safety scan before publishing examples.
