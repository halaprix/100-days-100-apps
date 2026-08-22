# Day 058 — ForegroundProbe

Date: 2026-08-22
Status: repo-created
Repo: [`projects/foregroundprobe`](../projects/foregroundprobe)

## One-line pitch

ForegroundProbe turns a local Android manifest and target-SDK configuration into a reviewable Android 12–15 foreground-service readiness packet: declared-type/permission checks, background-start and boot risks, Android 15 timeout exposure, and the device tests that static analysis cannot replace.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1vv5762/we_just_submitted_botdroid_turn_an_android_phone/ | Fresh RSS-fallback post for an Android bot host treats foreground persistence, reboot recovery, and OEM battery killers as core product work rather than incidental implementation detail. |
| BotDroid | https://botdroid.app/ | The launched product explicitly relies on a foreground service, WakeLock, boot restore, restart backoff, and battery-exemption guidance to keep on-device bots running. |
| Android Developers | https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start | Android 12+ restricts background foreground-service starts and documents `ForegroundServiceStartNotAllowedException`. Updated 2026-08-14. |
| Android Developers | https://developer.android.com/develop/background-work/services/fgs/timeout | Android 15 gives background `dataSync` and `mediaProcessing` foreground services a six-hour-per-24-hour budget, requires timeout handling, and publishes test commands. Updated 2026-08-14. |
| Android Developers | https://developer.android.com/develop/background-work/background-tasks/optimize-battery | Android documents constraints, expedited-work trade-offs, and stop reasons for background tasks. Updated 2026-02-26. |
| Don't kill my app! | https://dontkillmyapp.com/ | The benchmark and vendor matrix show that power-management behavior remains materially device/OEM-specific. |

## Problem

For Android apps that need a durable foreground service—an on-device bot, sync client, tracker, companion, or agent—“it runs on my phone” is inadequate release evidence. Android 12 restricts background starts; Android 14 adds type/permission considerations; Android 15 limits certain background foreground-service categories; and OEM power management remains uneven.

The status quo is to read several platform pages, inspect Logcat after a failure, and repeat manual tests across a device matrix. That is reactive, hard to hand off, and can cost days after a release or beta test when a supposedly persistent feature stops. A static packet cannot certify runtime survival, but it can move known platform-rule mistakes and missing test cases into review before device testing.

## Target user

Android developers shipping a small on-device bot, AI agent, sync tool, tracker, or companion app whose user-visible value depends on a long-running foreground service.

## MVP scope

- Local parser for a selected `AndroidManifest.xml` and a minimal config containing target SDK and service-entry assumptions.
- Deterministic rules for declared foreground-service types, Android 14 type permissions, Android 12 background-start/boot-receiver risks, and Android 15 `dataSync`/`mediaProcessing` timeout exposure.
- Markdown packet with findings, confidence boundaries, documentation links, the relevant `adb` compatibility-test commands, and an OEM-device test matrix.
- Synthetic fixtures only. No telemetry, source rewrite, device control, Play Console connection, battery-optimization bypass, or runtime-survival claim.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Android Studio lint and Android background-work documentation | Lint and docs cover individual declarations and platform behavior, but do not make a project-specific lifecycle/readiness packet that combines target SDK, service type, boot/background assumptions, timeout exposure, and required test evidence. |
| Direct competitor | Don't kill my app! benchmark and vendor guides | Strong vendor/OEM reference and benchmark. It diagnoses device behavior and settings, not an Android-project static preflight for modern platform restrictions. |
| Direct competitor | dkma-monster toolkit | The public project advertises OEM battery-manager guidance across CLI/GUI/library surfaces. Its focus is mitigation/guidance; the proposed MVP is a repository-local Android 12–15 design review packet. Validate feature overlap before writing a plugin. |
| Indirect substitute | Manual manifest review, Android docs, Logcat, emulators, real phones, and issue search | Flexible but reactive; project-review evidence and test planning are recreated manually after each design change. |
| Status quo | Ship, then investigate a background-start, service-type, timeout, or OEM-kill failure | The failure can make a core feature unreliable and turn a short build into days of diagnosis and retesting. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ForegroundProbe | Android developers whose bot/sync/agent depends on a long-running foreground service → Android lint/docs, Don't kill my app!, and manual device testing → each covers a slice but none creates a local Android 12–15 lifecycle risk packet plus explicit remaining-test plan → manifest/target-SDK preflight for service type, start source, boot risk, timeout exposure, and OEM matrix → Android background-work searches, Android developer communities, and maintainers of on-device bot/agent projects → Android 15 timeout rules and a fresh bot-host launch make persistent-service design newly reviewable | Winner; painful status quo, specific artifact, and repeatable technical-search/community channel. |
| PocketBot Host | Indie bot makers → VPS, Termux, BotDroid, BotHost, and a spare computer → established products already provide phone-hosted bots with persistence and pricing → no defensible narrow wedge beyond generic hosting → maker and Telegram-bot communities → fresh BotDroid launch | Rejected; direct products already solve the job and distribution would be a feature comparison. |
| ClickSpec | Non-technical founders → Figma, v0/Lovable/Bolt and clickable prototypes → the category already supplies prototype generation, and the fresh discussion does not establish a narrower unserved workflow → executable-spec comments → founder communities → fresh r/startups discussion | Rejected; crowded AI-prototype category with no concrete first-user wedge. |
| ResumeLatex QA | CS graduates tailoring ATS resumes → Teal, Jobscan, Resume Worded, Rezi, templates, and manual editing → strong incumbents already cover keyword matching, resume building, and formatting checks → LaTeX-only QA is too narrow without proof of a channel → university career communities → fresh r/SideProject post | Rejected; job-application automation is reject-by-default and the incumbent set is strong. |
| MealHistory Planner | Families deciding dinner → meal planners, grocery apps, recipe sites, shared notes, and a rotating meal list → established meal planners already learn preferences and make lists → household-history angle lacks a concrete first-user channel → generic family/productivity audiences → fresh r/SideProject post | Rejected; tolerable manual workaround for many households and no sharp distribution wedge. |

## Wedge

ForegroundProbe does not compete to keep a process alive and does not promise to defeat OEM power management. It produces the missing review artifact before the runtime test: a deterministic mapping from what this Android project declares to the known Android 12–15 foreground-service constraints, plus the device tests still needed. That is narrower than generic lint, safer than an auto-fix wrapper, and complementary to OEM guidance rather than a replacement for it.

## Kill condition

Reject or narrow if Android Studio’s built-in checks plus Don't kill my app! already produce an equivalent project-level background-start/type-permission/timeout review and device-test plan in under 30 minutes, or if three target developers say their foreground-service incidents are rare or the packet would not change a release decision. Do not add a runtime agent if the static packet cannot demonstrate a distinct review benefit.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A persistent feature failure is visible to users and can cost days of diagnosis, though it affects a technical niche rather than all Android apps. |
| Feasibility | 4/5 | A manifest/config parser, deterministic rules, fixtures, and Markdown packet fit a 1–3 day MVP; cross-device runtime verification is explicitly deferred. |
| Demo potential | 4/5 | A synthetic manifest can visibly become a finding list, timeout warning, and device-test matrix. |
| Distribution | 4/5 | Concrete search intent and repeatable channels exist: Android foreground-service/background-start/timeout searches, Android communities, and projects building on-device bots or agents. |
| Competitive wedge / timing | 3/5 | Android docs and OEM guides are strong, but the local review-packet boundary is distinct and Android 15’s documented limits create timely review work. |
| Total | 19/25 | Clears the 18-point threshold and both gates; competitive wedge/timing is the weakest dimension. |

## Decision

Create repo. ForegroundProbe scored 19/25 with distribution 4/5 and competitive wedge/timing 3/5. The local dedicated repository and its public-safe snapshot were created; no dedicated GitHub remote is configured.

## Next build step

Implement one synthetic Android 15 `dataSync` fixture: parse its manifest and target SDK, flag timeout and boot/background-start concerns, then render a golden readiness packet with the required manual test matrix.

## Source access caveats

Reddit public JSON was blocked with `theme-beta`; the multi-subreddit collection used RSS fallback for r/SideProject and r/startups, while several configured subreddits hit RSS `HTTP 429`. The fresh Reddit evidence is a permalink from RSS fallback, so no score or comment-count claim is made. X account lookup worked, but the permitted read-only `xurl search` returned `401 Unauthorized`; no X posts were used and no social writes were attempted. Competitor and platform validation used public Android documentation, product pages, search results, and Don't kill my app!.
