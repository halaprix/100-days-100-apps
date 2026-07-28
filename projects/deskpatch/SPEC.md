# SPEC — DeskPatch

## User story

As a small IT operator responsible for locked-down Windows analyst machines, I want users to run only approved desktop-tool updates without local admin rights, so that I do not touch hundreds of machines or put admin credentials into scripts.

## Core flow

1. Admin installs the DeskPatch service once on a workstation image or individual device.
2. Admin generates an update manifest for Power BI Desktop:
   - app id,
   - version,
   - installer URL,
   - installer SHA-256,
   - silent install command,
   - expiry,
   - approver,
   - signature.
3. User opens the DeskPatch client and sees that an approved Power BI Desktop update is available.
4. Client sends the manifest to the local service.
5. Service verifies the manifest signature, expiry, app allowlist, installer hash, and command template.
6. Service executes the approved installer under the service account/elevated context.
7. Service writes an audit event with requester, manifest hash, installer hash, timestamp, exit code, and result.

## Data model

### Manifest

```json
{
  "schema": "deskpatch.manifest.v1",
  "app_id": "power-bi-desktop",
  "display_name": "Power BI Desktop",
  "version": "2.155.756.0",
  "installer_url": "https://download.microsoft.com/.../PBIDesktopSetup_x64.exe",
  "installer_sha256": "<hex>",
  "command_template": "PBIDesktopSetup_x64.exe -quiet -norestart ACCEPT_EULA=1",
  "expires_at": "2026-07-24T00:00:00Z",
  "approved_by": "it-admin",
  "signature": "<detached-signature>"
}
```

### Audit event

```json
{
  "schema": "deskpatch.audit.v1",
  "timestamp": "2026-06-24T09:00:00Z",
  "device_id": "local-device-id-placeholder",
  "user": "local-user",
  "app_id": "power-bi-desktop",
  "manifest_sha256": "<hex>",
  "installer_sha256": "<hex>",
  "action": "install",
  "exit_code": 0,
  "result": "success"
}
```

## Technical approach

- Language: start with Go or Rust for a single static Windows service binary.
- Trust model: service has a built-in public key; manifests are signed offline by the admin-side tool.
- Allowlist: command execution is template-based per app id, not arbitrary shell execution.
- Verification:
  - manifest schema validation,
  - signature verification,
  - expiry check,
  - installer SHA-256 verification after download,
  - path and argument normalization before execution.
- Client: CLI first; tray app later if the CLI proves useful.
- Distribution: release unsigned dev builds initially; production story must include code signing before real use.

## Validation plan

1. Reproduce the source workflow with a fake installer first: non-admin user requests update, service verifies manifest, writes audit log.
2. Add a dry-run Power BI Desktop manifest generator that fetches public installer metadata but does not install by default.
3. Test competitor/substitute fit with five target users:
   - Do they lack Intune/PDQ/Admin By Request?
   - How many endpoints need Power BI Desktop updates?
   - How often do they touch machines manually?
   - Would a one-time service install be acceptable?
   - Is local audit log enough, or do they need central reporting immediately?
4. Kill the project if users mainly need generic patch management, arbitrary elevation, or cloud fleet control.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — manifest schema, signer/verifier, and fake installer demo.
- v0.1.0-alpha.2 — Windows service skeleton with local CLI.
- v0.2.0-alpha.1 — Power BI Desktop dry-run recipe and audit log viewer.
