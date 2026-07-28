# SPEC — OOBEGuard

## User story

As a Windows imaging admin, I want to run a local preflight check on a redacted deployment plan, so that I can catch setup-phase, OEM-key, and driver-staging traps before imaging a fleet.

## Core flow

1. User creates or copies `examples/win11-pro-oem.yml`.
2. User runs `oobeguard check examples/win11-pro-oem.yml`.
3. OOBEGuard loads static rules and evaluates the deployment plan.
4. CLI prints a Markdown report with blockers, warnings, safer alternatives, and source links.
5. User can paste the report into a rollout checklist, ticket, or public forum post without exposing private fleet details.

## Data model

Initial YAML fields:

```yaml
windows:
  version: "11"
  edition: "Pro"
  license_channel: "OEM"
imaging:
  tool: "FOG"
  post_install_hooks:
    - type: "SetupComplete.cmd"
      reboots: false
  driver_strategy:
    phase: "online-after-image"
    command: "dism"
    recurse: true
fallbacks_considered:
  - "RunOnce"
  - "FirstLogonCommands"
  - "pnputil"
```

Rule result shape:

```json
{
  "id": "windows.setupcomplete.oem.disabled",
  "severity": "blocker",
  "summary": "SetupComplete.cmd is disabled for OEM product keys except Enterprise/Server.",
  "evidence": ["https://learn.microsoft.com/..."],
  "fallbacks": ["RunOnce", "FirstLogonCommands", "unattend commands"]
}
```

## Technical approach

- Start as a small CLI with static fixtures and deterministic rules.
- Prefer a boring implementation: parse YAML, evaluate rule functions, render Markdown.
- Keep evidence links in rule metadata.
- Do not access devices, networks, activation state, registries, or private logs in the MVP.
- Make all examples fictional and public-safe.

## Initial rules

1. `windows.setupcomplete.oem.disabled`
   - If edition is non-Enterprise/non-Server and license channel is OEM and hook includes `SetupComplete.cmd`, emit blocker.
2. `windows.setupcomplete.reboot.bad_state`
   - If `SetupComplete.cmd` indicates reboot, emit blocker/warning based on certainty.
3. `drivers.dism.online.confusion`
   - If driver phase is online after image and command is DISM, emit warning to verify context and consider `pnputil`.
4. `drivers.dism.recurse.bloat`
   - If offline DISM uses recursive folders, emit warning about image bloat and duplicate payloads.
5. `fallbacks.missing`
   - If no fallback path is listed for a blocker, emit warning with RunOnce/FirstLogon/unattend options.

## Validation plan

- Unit-test every rule against synthetic YAML fixtures.
- Snapshot-test Markdown output.
- Validate source links are present for every blocker/warning.
- Compare output against the evidence table in the 100-days index brief.
- Validate the wedge: one report should clearly explain the OEM `SetupComplete.cmd` trap faster than reading scattered docs and forum threads.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — CLI reads one YAML fixture and renders one Markdown report.
- v0.1.0-alpha.2 — add rule tests and three more synthetic fixtures.
- v0.2.0-alpha.1 — usable demo with docs and copy/paste report examples.
