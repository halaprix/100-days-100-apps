# Day 062 — CachePath

Date: 2026-08-26
Status: idea-only

## One-line pitch

A Gradle check and emulator test recipe that catches user-created Android media
stored in purgeable cache paths before a release turns a low-storage cleanup into
permanent data loss.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report (Reddit RSS fallback) | https://www.reddit.com/r/SideProject/comments/1vyp8iw/i_built_an_ai_fitness_trainer_app_solo_heres_what/ | On August 26, an Android fitness-app builder reported that progress photos must survive Android cache clearing or users lose their history. This is one fresh report, not a measure of prevalence. |
| Original platform documentation | https://developer.android.com/training/data-storage/app-specific | Android separates persistent app-specific files from cache directories and documents storage-management flows that can clear cache files. The page was updated August 14, 2026. |
| Original platform documentation | https://developer.android.com/training/data-storage/ | Android's storage overview distinguishes app-specific, shared, preference, and database storage; choosing the wrong class for irreplaceable media is a product-data risk. |
| Original platform tooling documentation | https://developer.android.com/topic/performance/inspecting-overview | Android provides inspection and performance tooling, but this is a broad toolbox rather than a release gate for user-generated-media durability. |

## Source access caveats

- Reddit's public JSON endpoint was blocked. The read-only tool used public RSS
  fallback for `r/SideProject` and `r/SaaS`; scores and comment counts are
  unavailable. `r/sysadmin` and `r/selfhosted` then returned `429` from RSS and
  were not retried.
- `xurl whoami` succeeded, but `xurl search` returned `401 Unauthorized`; X
  search was unavailable and no X signal is claimed.
- The opportunity is grounded in one fresh community report plus Android's
  storage documentation. It is not yet evidence that the problem is common.

## Problem

An Android app that saves progress photos, recordings, scans, or drafts under a
cache directory may appear to work until a storage cleanup removes them. The
failure is unusually costly: the user loses irreplaceable history, support has
no recovery path, and a normal happy-path UI test is unlikely to expose it.

This passes the status-quo pain test for apps that own user-created media. The
workaround is a manual code review plus ad-hoc emulator/low-storage testing;
missing it can cause permanent user-data loss and public trust damage, rather
than merely wasting a few minutes.

## Target user

A Kotlin/Android developer at a small app team whose app captures or generates
user-created photos, audio, scans, or drafts and keeps some files locally before
syncing them.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Outcome |
|---|---|---|
| CachePath | Android developers storing user-created media → Android Studio inspection, generic mobile tests, and manual reviews → they do not connect media-origin code paths to purgeable storage or force a reviewable persistence check → Gradle lint plus a focused emulator test recipe for user media → Kotlin/Android storage-error searches, a free Gradle Plugin Portal check, and Android developer communities → a fresh builder report exposes the exact failure mode | **Selected**; narrow loss-of-history failure with a small, demonstrable MVP. |
| Fallback Contract | Indie apps using free LLM providers → provider SDK retries and generic observability → a model/provider fallback contract tool is an LLM operations wrapper in a crowded category → provider-specific output fixtures → LLM builder communities → one builder reported deprecations | Rejected before scoring: generic LLM spend/availability tooling is crowded, and the evidence does not establish a defensible first-user channel. |
| Handoff Owner | SaaS founders coordinating freelancers → Linear/Jira/Notion/agencies → ownership ambiguity is real but established project tools and process changes already cover it → feature handoff receipt → founder communities → a fresh founder post | Rejected before scoring: no sharp software wedge over existing project-management systems. |
| Linked Dev Tools | Developers decoding tokens and timestamps → individual web utilities or scripts → copy/paste is mildly annoying, not a material loss → connected utility tray → developer-tool directories → a fresh utility launch | Rejected before scoring: the status quo is tolerable and the idea does not clear the pain test. |

## MVP scope

- Ship a Kotlin/Gradle plugin that flags writes of named user-media types to
  `cacheDir`, `externalCacheDir`, and known cache subpaths.
- Allow explicit annotations or config for genuinely regenerable assets so the
  output does not claim every cache write is a bug.
- Generate a Markdown release check listing suspected media paths, persistence
  class, and the source locations to review.
- Include an `adb`/emulator recipe that creates a fixture asset, clears the app
  cache, relaunches, and asserts the asset or its durable record remains.
- Stay local-only: no device data upload, Play Console access, or automatic code
  rewrite.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Android Studio inspections and Android Lint | They catch many static correctness issues, but no identified standard inspection frames user-created media in cache as a release-blocking durability check with a test packet. Verify this before implementation rather than assuming a gap. |
| Direct competitor | Mobile automation stacks such as Appium, Maestro, and Firebase Test Lab | They can run bespoke UI tests, but require teams to author and maintain the storage-loss scenario themselves; they are not a focused source-to-path audit. |
| Indirect substitute | Manual storage review, `adb shell pm clear`, and a custom instrumentation test | Powerful but easy to skip, difficult to standardize in release review, and often written only after a loss incident. |
| Status quo | Treat the app's cache as a persistence area until a device cleanup reveals the mistake | The resulting loss can be permanent and erodes trust in apps holding user history. |

## Wedge

CachePath is not another no-code mobile-test platform or generic static analyzer.
It is a deliberately narrow local release gate: find likely user-owned media in
purgeable paths, explain why the path is unsafe, and hand the team a minimal
reproduction command. Its value is a reviewable proof that a history-bearing
feature survives cache cleanup, without requiring a device cloud or credentials.

## Kill condition

Reject or narrow if Android Lint already ships a maintained inspection that
flags user-created media in cache directories with equivalent actionable output,
or if five Android developers who maintain media-bearing apps report that a
manual cache-clear test takes under five minutes and would not be used in CI or
release review. Also reject if the first five code samples show false positives
outnumber actionable findings after explicit regenerable-asset exclusions.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | User-created history disappearing is a trust and support incident, but the affected feature class is specific. |
| Feasibility | 5/5 | Kotlin PSI/Android Lint rules plus a fixture emulator recipe and Markdown report fit a 1–3 day prototype. |
| Demo potential | 5/5 | A fixture can show a photo surviving before the fix, disappearing after cache clear, then the lint/test gate blocking the unsafe path. |
| Distribution | 3/5 | Android storage-error searches, Android developer communities, and the Gradle Plugin Portal are specific channels, but a repeatable acquisition path is not yet validated. |
| Competitive wedge / timing | 3/5 | The loss mode is concrete and the audit is narrower than generic test stacks, but standard Lint coverage must be disproven before a build bet. |
| Total | 20/25 | Clears the total threshold but fails the distribution gate. |

## Decision

**Idea-only; no dedicated repo created.** CachePath scores 20/25, but the
Distribution score is 3/5, below the required 4/5 gate. The weakest dimension is
distribution: a specific Android audience exists, but this run has not proven a
repeatable way to reach developers maintaining media-bearing apps. The second
blocker is validation of the claimed Android Lint gap.

## Next build step

Run a five-repository spike against open-source Android apps with user-created
media: check whether existing Android Lint reports the cache-path pattern, then
contact no one yet—publish the findings as a reproducible sample only if the
false-positive rate is acceptable.
