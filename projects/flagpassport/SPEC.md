# FlagPassport specification

## User story

As a Forge Marketplace partner, I want a local report of client-side feature
flag calls that could become anonymous-default paths, so I can review the
December 2026 change before a customer encounters altered UI behavior.

## Core flow

1. The user supplies one or more project paths explicitly.
2. FlagPassport reads supported TypeScript/JavaScript and Forge manifest files
   locally without executing them.
3. It detects `@forge/bridge` feature-flag client usage, initialization inputs,
   and default values used in checks.
4. It joins findings to relevant manifest-module access signals where possible;
   unprovable associations remain `manual-review`.
5. It emits a deterministic Markdown and JSON report with an authenticated and
   unauthenticated verification matrix.

## Feature list

### MVP

- Explicit-path local discovery for `manifest.yml`, TypeScript, and JavaScript.
- AST-based or conservative token-based detection of `FeatureFlags` client use.
- Source labels, import aliases, initialization evidence, and check defaults.
- `unlicensedAccess` and relevant manifest-module context when present.
- A packet with `affected`, `manual-review`, and `not-proven` classifications.
- Tests proving no source text, credentials, or identifiers are retained in output.

### Later

- GitHub Action for repository-managed Forge apps.
- Rule support for more frontend toolchains and generated code maps.
- User-approved remediation patch suggestions.
- Optional vendor documentation version pinning.

## Data model

```json
{
  "packet_version": 1,
  "deadline": "2026-12-01",
  "findings": [
    {
      "source_label": "frontend source",
      "client_sdk": "forge-bridge",
      "initialization": "account-id-not-proven",
      "default_behavior": "false",
      "module_access": "possible-unlicensed-access",
      "classification": "manual-review"
    }
  ],
  "summary": {"manual_review": 1, "affected": 0, "not_proven": 0}
}
```

## Technical approach

Start as an offline CLI with a YAML parser and a TypeScript parser. It accepts
only explicit inputs, never executes application code, and writes deterministic
reports to a user-selected directory. Unsupported expressions, wrappers, and
manifest shapes are reported as unknown rather than inferred as safe.

## Build plan

1. Create synthetic Forge fixtures covering authenticated client use,
   omitted-account initialization, aliased imports, unlicensed module settings,
   unrelated feature flags, and malformed manifests.
2. Implement the parser adapters and conservative finding model.
3. Render Markdown and JSON packets plus an authenticated/unauthenticated test
   matrix.
4. Add output-redaction, no-network, and no-execution tests.
5. Validate the wedge with five Forge Marketplace partners that use client flags.
6. Stop if each partner can complete the vendor-guided review in under 15 minutes
   or if an established Forge scanner adds the same client/manifest/default packet.

## Validation plan

- Unit-test classification and unknown handling with synthetic fixtures only.
- Assert report output contains no fixture source text or secret-shaped values.
- Assert the CLI opens no network connections and never invokes project commands.
- Demo a mixed app set becoming a concise, deadline-specific review packet.
- Compare with FSRT and the vendor documentation: FlagPassport must add only
  exposure correlation and test evidence, not claim general vulnerability coverage.

## Milestones

- `v0.1.0-alpha.0` — scaffold and specification.
- `v0.1.0-alpha.1` — fixture-driven, read-only scanner.
- `v0.2.0-alpha.1` — report renderer and partner validation spike.
