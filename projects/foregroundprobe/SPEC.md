# ForegroundProbe SPEC

## User story

As an Android developer building a long-running foreground service, I want a local readiness packet from my manifest and target SDK, so that I can catch platform-rule gaps and plan device testing before an on-device bot or sync feature fails in the background.

## Feature list

### MVP

1. Read an `AndroidManifest.xml` and a small explicit config containing target SDK and service entry points.
2. Identify foreground-service declarations, service types, related permissions, boot receivers, and launch assumptions.
3. Apply deterministic checks for Android 12 background-start restrictions, Android 14 type/permission alignment, and Android 15 timeout-sensitive types.
4. Render Markdown with findings, confidence/limitations, relevant Android-documentation links, and a manual test matrix.
5. Ship only synthetic fixtures and no network client.

### Later

- Gradle plugin and custom Android lint integration.
- Optional local ADB collector for an explicitly selected attached test device.
- Versioned OEM test results imported from a public-safe fixture.
- CI annotation output.

## Data model

```json
{
  "project": {
    "target_sdk": 35,
    "services": [
      {
        "name": "SyncService",
        "foreground_service_type": ["dataSync"],
        "started_from": "boot_receiver"
      }
    ],
    "permissions": ["FOREGROUND_SERVICE", "FOREGROUND_SERVICE_DATA_SYNC"]
  }
}
```

## Build plan

1. Add a small parser for manifest service, permission, and receiver declarations.
2. Map findings to documented platform-version rules.
3. Add a renderer and synthetic Android 15 data-sync fixture.
4. Add golden packet tests and a public-safety check.
5. Ask three Android developers with long-running services whether the packet changes a release/test decision; stop if it does not save meaningful diagnosis time.

## Validation plan

- Unit-test each platform finding against synthetic manifests.
- Produce a demo packet showing a missing type permission, boot-start risk, Android 15 timeout exposure, and non-actionable limitations.
- Verify no network connection, device mutation, manifest rewrite, or battery-optimization request occurs.
- Reject/narrow the bet if target users say Android Studio lint plus Don't kill my app! guidance already covers their PR review and device-test planning in under 30 minutes.
