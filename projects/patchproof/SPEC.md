# PatchProof SPEC

## User story

As a small-team sysadmin responsible for patch management, I want to turn static patch, scanner, ticket, and endpoint exports into a clear evidence packet, so I can explain vulnerability-score gaps without manually stitching screenshots and spreadsheets for every review.

## Feature list

### MVP

1. Import static evidence
   - Generic CSV/JSON import for patch status, scanner findings, endpoint inventory, and ticket/exception notes.
   - Sample adapter shapes for Intune, PDQ/Action1-style patch reports, and Qualys/Tenable/Rapid7-style scanner exports.
2. Asset reconciliation
   - YAML/CSV mapping file for scanner asset names, patch-tool device names, and pseudonymous report labels.
   - Warnings for unmatched assets and duplicate mappings.
3. Classification engine
   - States: patched, pending reboot, offline/stale, not applicable, rollback/breakage, exception needed, unknown.
   - Rules are deterministic and visible in the rendered appendix.
4. Evidence packet renderer
   - Markdown and HTML output.
   - Executive summary, stale endpoint list, real remediation gaps, deployed-awaiting-rescan items, rollback notes, and exception appendix.
5. Public-safe fixture suite
   - Synthetic assets only.
   - No real hostnames, IP addresses, usernames, ticket IDs, or vulnerability data.

### Later

- Live adapters for selected platforms after the static-export flow proves useful.
- PDF export.
- Signed report metadata and diff between review cycles.
- MSP multi-client workspace mode with strict local redaction rules.

## Data model

```json
{
  "report_id": "sample-patch-review",
  "generated_at": "2026-08-16T07:20:00Z",
  "assets": [
    {
      "asset_label": "asset-a",
      "last_seen_days": 2,
      "patch_status": "deployed",
      "scanner_status": "still-vulnerable",
      "ticket_status": "awaiting-rescan",
      "classification": "patched_pending_rescan",
      "evidence": ["patch-export", "scanner-export", "ticket-note"]
    }
  ]
}
```

## Build plan

1. Define fixture CSV schemas for patch status, scanner findings, endpoint last-seen, and exception notes.
2. Implement parser and normalization into a single in-memory asset/finding model.
3. Add deterministic classification rules and warnings for unknown/mismatched assets.
4. Render Markdown packet from the sample fixtures.
5. Add HTML export once the Markdown report is stable.

## Validation plan

- Unit-test fixture parsing and asset matching.
- Unit-test each classification state with synthetic assets.
- Golden-file test for Markdown output.
- Public-safety verifier that scans tracked docs/fixtures for token markers and private-infrastructure patterns.
- Manual demo: run the fixture pipeline and inspect the generated executive summary plus per-asset appendix.
