# ForegroundProbe

ForegroundProbe is a local Android-project preflight that turns manifest and Gradle metadata into a reviewable foreground-service readiness packet for Android 12–15.

## Problem

A long-running Android worker can appear reliable in local testing yet fail after screen-off, reboot, background launch, or an OEM power-management decision. The rules are fragmented: Android 12 restricts background starts, Android 14 checks service-type permissions, and Android 15 imposes time budgets on `dataSync` and `mediaProcessing` foreground services.

Developers typically combine Android documentation, Logcat, an emulator, and manual device tests after an incident. That can burn days and still leaves reviewers without a clear statement of what was checked. ForegroundProbe is deliberately a static preflight and test-plan generator, not a promise of universal OEM survival.

## Target user

Android developers shipping a small on-device bot, agent, sync tool, tracker, or companion app that relies on a long-running foreground service.

## MVP

- Read a local `AndroidManifest.xml` plus minimal Gradle/target-SDK metadata.
- Flag declared foreground-service types, missing type permissions, background-start assumptions, boot-receiver risk, and Android 15 `dataSync`/`mediaProcessing` timeout exposure.
- Generate a Markdown packet with evidence, limits, required manual tests, relevant `adb` compatibility-test commands, and an OEM-device test matrix.
- Use deterministic rules and synthetic fixtures only; no device data leaves the machine.

## Non-goals

- No runtime monitoring, OEM-setting automation, Play Console upload, or production crash analytics.
- No claim that a static scan can prove background reliability on every manufacturer/device combination.
- No source-code rewriting, manifest mutation, or battery-exemption bypass.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1vv5762/we_just_submitted_botdroid_turn_an_android_phone/ | A fresh Android bot-host launch explicitly markets foreground-service persistence, reboot recovery, and resilience to OEM battery killers. |
| Android Developers | https://developer.android.com/develop/background-work/services/fgs/timeout | Android 15 limits background `dataSync` and `mediaProcessing` foreground services to six hours per 24 hours and documents a test switch. |
| Android Developers | https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start | Android 12+ background foreground-service starts are restricted and may throw `ForegroundServiceStartNotAllowedException`. |
| Don't kill my app! | https://dontkillmyapp.com/ | Device vendors apply different power-management behavior; the site provides a benchmark and vendor-specific guidance. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Android Studio lint and Android documentation | Catch some manifest/platform requirements and explain the APIs, but do not produce an opinionated service-lifecycle readiness packet or OEM test plan for a specific project. |
| Direct competitor | Don't kill my app! and its benchmark | Provides device/vendor behavior knowledge and a benchmark, not a repository-local Android 12–15 static preflight. |
| Indirect substitute | Manual manifest review, Logcat, emulator/phone testing, issue search | Flexible but reactive and hard to make repeatable in a pull request or handoff. |
| Status quo | Discover a background-start, type-permission, timeout, or OEM failure after release | Can consume days of diagnosis and makes an on-device bot/sync feature look unreliable. |

## Wedge

ForegroundProbe sits before runtime testing: it converts the local manifest and target SDK into a narrow, reviewable Android 12–15 risk packet plus the exact device tests still required. Existing vendor guides diagnose a device class; generic lint catches individual declarations. Neither turns a background-service design into a shareable preflight artifact.

## Current status

v0.1.0-alpha.0 — scaffold and specification only. The local repository has no remote configured.
