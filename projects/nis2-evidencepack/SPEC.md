# SPEC — NIS2 EvidencePack

## User story

As a small-company IT owner preparing for NIS2, I want to turn existing exports, screenshots, and policy files into a structured evidence pack, so that management, consultants, or auditors can see which requirements are covered without me manually building a binder from scratch.

## Core flow

1. User creates a local evidence project with a country/stack profile.
2. User drops files into `inbox/` or runs import commands for supported exports.
3. EvidencePack extracts safe metadata: filename, type, date, source system, detected control keywords, and freshness.
4. User reviews suggested mappings and assigns owners.
5. EvidencePack generates an evidence binder with a coverage matrix and missing-evidence report.

## Data model

```text
Control
- id
- framework: NIS2 / ENISA mapping
- title
- description
- evidence_examples[]
- required_owner_role

EvidenceArtifact
- id
- source_type: csv | json | pdf | screenshot | markdown | doc
- filename
- captured_at
- owner
- sha256
- summary
- mapped_controls[]
- confidence: low | medium | high
- freshness_days

EvidencePack
- profile
- organization_label
- controls[]
- artifacts[]
- gaps[]
- generated_at
```

## Technical approach

- Python CLI first; no SaaS backend.
- Local workspace with plain files and a small SQLite index.
- Deterministic importers for CSV/JSON plus best-effort text extraction for PDFs and Markdown.
- Control catalog stored as versioned YAML so legal/control interpretation is auditable.
- Optional local LLM summarization later, but v0.1 must work without model dependencies.
- Secret-safe by design: hash files and describe missing evidence; never request admin tokens.

## Validation plan

- Build a fixture pack with sample Microsoft 365, GitHub, policy, supplier, and incident-response artifacts.
- Verify that the CLI creates a binder without network access.
- Compare generated rows against the NISD2 evidence-upload/checklist workflow and the public NIS2 SME toolkit.
- Validate wedge with 5 target users: one-person IT owners, MSP consultants, or compliance freelancers serving EU SMEs.
- Kill the idea if users say manual checklist upload is already good enough, or if useful evidence mapping requires privileged cloud APIs before the MVP can prove value.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and spec.
- v0.1.0-alpha.1 — CLI skeleton, local project format, and static control catalog.
- v0.1.0-alpha.2 — fixture importers and binder export.
- v0.2.0-alpha.1 — user-tested NIS2 evidence mapping workflow.
