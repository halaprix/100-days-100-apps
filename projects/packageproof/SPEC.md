# PackageProof SPEC

## User story

As an Android publisher with direct or mixed distribution, I want a local packet
that connects an APK's package ID and signer fingerprint to an explicit release
route, so that I can complete the correct verification work before a release is
blocked or a package is removed.

## Feature list

### MVP

1. Accept a selected APK path and a local YAML/JSON inventory of intended
   distribution routes.
2. Extract package name and certificate SHA-256 fingerprint with local Android
   tooling; explain missing tooling rather than downloading or invoking a cloud
   service.
3. Compare artifact facts with route declarations and deterministic rules.
4. Render Markdown and JSON finding packets with source links and an explicit
   `unknown` state where console registration cannot be checked locally.
5. Include synthetic APK/metadata fixtures for an unknown route, missing
   fingerprint, duplicate package, and coherent package.

### Later

- A Gradle task wrapper and CI artifact attachment.
- An optional adapter for official delegated APIs after a separate credential and
  threat-model review.
- A human-entered registration receipt field, never a claim inferred from local
  metadata.

## Data model

```json
{
  "artifact": {
    "path": "demo-release.apk",
    "package_name": "example.demo",
    "certificate_sha256": "AA:BB:...",
    "source": "local-apk"
  },
  "routes": [
    {
      "package_name": "example.demo",
      "channel": "outside-play",
      "certificate_sha256": "AA:BB:..."
    }
  ],
  "findings": [
    {
      "code": "route_match",
      "severity": "info",
      "next_action": "Open the Android Developer Console registration guide."
    }
  ]
}
```

## Build plan

1. Define synthetic fixture metadata and golden packet expectations.
2. Implement an artifact-adapter boundary around local `apksigner` output.
3. Parse a minimal explicit route inventory; do not inspect keystores or secrets.
4. Add reconciliation rules and Markdown/JSON renderers.
5. Demonstrate one coherent and three failing fixture packets.
6. Validate the wedge with five affected Android publishers; stop if the native
   console/API already creates the same preflight or manual reconciliation is
   not a material release cost.

## Validation plan

- Unit-test every finding against synthetic fixture data.
- Verify the tool makes no network connection and never reads a keystore.
- Demo a route/fingerprint mismatch and show the official native-console action,
  without claiming the app is registered.
- Compare the output with the Android Developer Console and Play Console guides
  to keep next-action wording current.
- Reject/narrow if five target users report less than 30 minutes per release
  cycle and no release/delivery risk from manual reconciliation.
