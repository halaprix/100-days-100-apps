# ConfigReceipt specification

## User story

As a self-hoster with a manually exported appliance configuration, I want a
local receipt that records what the file is for, safely prepares a shareable
copy, and compares revisions, so that I can recover or ask for help without
blindly opening the appliance or leaking configuration details.

## Core flow

1. Select an export file; ConfigReceipt reads it locally and calculates a
   content hash.
2. Enter only explicit context: friendly device label, export purpose, export
   method, claimed firmware/version, and recovery-location reminder.
3. Choose or review redaction rules. The tool emits a redacted derivative and
   records rules applied; it never silently declares a file secret-free.
4. Optionally select a prior receipt. ConfigReceipt renders a text diff or
   identifies the file as opaque/binary.
5. Export deterministic Markdown and JSON receipts with unresolved fields,
   comparison findings, and a manual restore checklist.

## Feature list

### MVP

- Single-file local import with SHA-256 hash and file classification.
- A compact, explicit receipt manifest.
- User-visible redaction rules and a no-redaction option.
- Unified diff for supported text files; clear `opaque` result otherwise.
- Markdown/JSON receipt output and synthetic fixtures.
- A no-network integration test or guard.

### Later

- Vendor parser plugins that identify non-sensitive configuration sections.
- A local Git repository adapter.
- An optional encrypted local archive after separate threat-model work.
- Import adapters for RANCID/Oxidized output, without credentials or polling.

## Data model

```json
{
  "receipt_version": 1,
  "source": {
    "filename": "router-export.cfg",
    "sha256": "<computed locally>",
    "classification": "text",
    "captured_at": "2026-09-06T00:00:00Z"
  },
  "context": {
    "device_label": "edge router",
    "purpose": "before firmware update",
    "claimed_firmware": "unknown",
    "recovery_location": "offline backup"
  },
  "redaction": {
    "state": "review-required",
    "rules": ["user-confirmed rule names"]
  },
  "comparison": {
    "prior_receipt": null,
    "state": "not-run"
  },
  "findings": [
    {"code": "missing_firmware", "severity": "warning"}
  ]
}
```

## Technical approach

A small local CLI is the first build. It takes input paths only from the user,
uses standard local parsers/hashing, writes output to an explicit directory,
and has no HTTP client dependency. Vendor-specific parsing remains opt-in; an
unknown format stays unknown instead of being guessed.

## Build plan

1. Define fixture exports and golden receipts for text, binary, and missing
   metadata cases.
2. Implement manifest validation and deterministic hashing/classification.
3. Add reviewed redaction transforms and receipt renderers.
4. Add two-file comparison with explicit unsupported-format behavior.
5. Add no-network and no-credential test guards.
6. Validate the wedge with five self-hosters who manually export configs. Stop
   if their existing Git/Obsidian workflow remains under 30 minutes per month
   and does not create restore/support risk.

## Validation plan

- Unit-test hashes, required metadata, redaction rule recording, diff output,
  and opaque-file behavior using synthetic files only.
- Verify the process opens no sockets and does not invoke device CLIs.
- Demo a dated export folder becoming a receipt, a redacted support copy, and a
  missing-firmware warning.
- Test the competitive claim with five target users: promote only if at least
  three have an unannotated or unsafe export that existing Git/notes do not
  make ready for recovery or support.
