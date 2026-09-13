# Day 079 — HsProjectProof

Date: 2026-09-13
Status: idea-only

## One-line pitch

A local, redaction-first CLI that turns a HubSpot app migration into a reviewable receipt: what moved to `src/`, what was archived, and which serverless environment-variable names still require explicit secret migration.

## Evidence

| Source | Link | Signal |
|---|---|---|
| HubSpot developer documentation, updated 2026-09-08 | [Migrate an existing app to developer platform 2026.09](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/migrate-an-app/migrate-to-the-latest-platform-version) | The new `2026.09` migration path changes project source layout; `hs app migrate` creates and deploys a project, downloads source, and can move old `src/` into `archive/`. Crucially, `serverless.json` environment entries are not automatically migrated and must be redefined as secrets. |
| HubSpot developer documentation, same source | [Migration prerequisites and paths](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/migrate-an-app/migrate-to-the-latest-platform-version#determine-your-migration-path) | Maintainers have materially different paths for 2025.2 projects, older projects, and legacy non-project public apps. That makes a post-migration receipt more useful than a generic checklist. |

## Problem

A HubSpot developer-platform migration can produce a deployable project while leaving a security-sensitive manual follow-up: legacy serverless environment configuration is not automatically converted to secrets. The maintainer must also understand whether the old project moved into `archive/`, whether the intended feature configuration now exists in `src/`, and which migration path was taken.

The status quo is reading the migration guide, accepting CLI prompts, manually inspecting generated folders, and copying secret *names* into a separate checklist. Missing one runtime setting can break a production feature after cutover; sharing a raw migration folder for review risks exposing configuration details. This is a potentially costly incident, but the current public evidence is documentation-led rather than repeated user reports, so the bet remains idea-only.

## Target user

A developer or small platform team maintaining a legacy public HubSpot app, especially one with serverless functions, migrating it to the `2026.09` project model.

## MVP scope

A local CLI, run after `hs project migrate` or `hs app migrate`, that:

1. reads a selected migration directory without uploading it;
2. identifies the project version, `archive/` and `src/` layout, and manifest/configuration deltas;
3. detects legacy `serverless.json` environment **key names only** and emits explicit `hs secret add <name>` checklist items without reading or printing values;
4. produces a Markdown/HTML migration receipt with pass, warn, and manual-review sections; and
5. optionally compares the receipt against a committed, redacted baseline in CI.

Non-goals: executing migrations, writing secrets, calling HubSpot APIs, certifying runtime parity, or replacing HubSpot's CLI.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Outcome before scoring |
|---|---|---|
| **HsProjectProof** | HubSpot legacy-app maintainers → `hs app migrate` plus manual folder/secret review → the CLI migrates project structure but documentation says legacy serverless environment entries are not automatically migrated → local post-migration receipt with key-name-only secret checklist and layout diff → HubSpot developer community, migration-doc search, and a copy-paste CI example → the `2026.09` guide was updated September 8 and creates a concrete migration window. | Narrow enough to score; public evidence shows a real manual gap, but demand validation is still thin. |
| RationaleCheck | Maintainers inheriting undocumented edge-case code → `git blame`, ticket search, and Copilot explanations → history is fragmented and AI explanations are not a durable reason → PR-local rationale receipt linked to tests and incident IDs → GitHub Action marketplace plus maintainer write-ups → a fresh r/webdev post asks what to do when code has an undocumented reason. | Rejected: GitHub/Copilot and code-health tools are strong substitutes; one fresh post is insufficient proof of a distinct wedge. |
| AssetShelf API | Small photographer-web developers → Cloudinary, a headless CMS, or S3 metadata → setup and pricing can be disproportionate for small client sites → self-hosted image-plus-metadata API starter → photography-webdev templates and agency tutorials → a fresh r/webdev post asks for image storage with API metadata. | Rejected: crowded DAM/CMS/storage category; status quo is tolerable for most small sites and first-user access is vague. |
| Connect-notice preflight | Atlassian Connect partners → Forge CLI and migration docs → customer-facing Connect EOS messaging needs a public guide URL and correct intent → local notice-packet verifier → Atlassian developer community and changelog search → current Connect EOS rollout messaging. | Rejected as duplicate research: the closely related candidate was already rejected in the Day 077 FlagPassport brief for insufficient incremental pain proof. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | [HubSpot CLI migration commands](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/migrate-an-app/migrate-to-the-latest-platform-version) | `hs project migrate` and `hs app migrate` perform the migration; they are not replaced. The proposed tool only reviews their output and makes the documented manual secret follow-up auditable. |
| Direct competitor | CI scripts and custom migration checklists | A team can write a repository-specific diff/check script. They usually do not preserve a standard, redacted receipt across app types or foreground the documented serverless-environment exception. |
| Indirect substitute | `git diff`, file-tree inspection, PR review, and a spreadsheet | Works, but relies on a reviewer knowing which generated paths and secret-name follow-ups matter; it is easy to omit the exception that values must not be copied into a report. |
| Status quo | Follow the HubSpot guide and accept the CLI's prompts | This is adequate for a simple app. It becomes risky when several legacy features and serverless settings must be checked before a customer-facing cutover. |

## Wedge

HsProjectProof is deliberately not another migration engine or generic secret scanner. Its narrow job is to create a portable, secret-safe *after-action receipt* for the exact artifacts HubSpot's migration produces: source relocation, app/project shape, and the documented environment-to-secret handoff. It can run entirely locally and emit names and presence checks, never values.

The first distribution path is a worked example attached to searches for `hs app migrate serverless.json environment`, a HubSpot developer-community validation post, and a GitHub Action template for partners that already use project repositories. This is concrete but not yet a proven repeatable acquisition channel, so Distribution remains 3/5.

## Kill condition

Reject the idea if three redacted real-world migration fixtures show that HubSpot's current CLI already emits an equally clear post-migration report and every required secret handoff, or if maintainers report that checking the generated layout and environment names takes under five minutes and has caused no release risk. Also reject if supporting more than the documented project shapes requires HubSpot API access or credentials before a useful local MVP exists.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | A missed runtime setting can break a customer-facing app, but demand evidence is presently documentation-led rather than repeated public reports. |
| Feasibility | 5/5 | Local filesystem parsing, YAML/JSON inspection, redaction rules, and Markdown output fit a 1–3 day CLI spike. |
| Demo potential | 4/5 | A before/after migration folder and a redacted green/yellow receipt make a clear terminal and HTML demo. |
| Distribution | 3/5 | HubSpot developers are identifiable through the migration docs and developer community, but no repeatable owned channel is proven. |
| Competitive wedge / timing | 3/5 | The September 2026 migration guide supplies timely, specific behavior; HubSpot's CLI remains a strong incumbent, so the wedge is intentionally limited to review evidence. |
| Total | 18/25 | Clears the numerical threshold but fails the required Distribution gate (minimum 4/5). |

## Decision

**Idea-only.** Do not create a dedicated repository. The score reaches 18/25, but Distribution is 3/5, below the repo-creation gate. The correct next move is validation, not scaffolding another migration tool.

## Next build step

Create three synthetic, redacted fixtures representing the migration paths in HubSpot's documentation and test whether a small local parser can produce a useful receipt without ever reading a secret value; then seek three HubSpot-maintainer reviews of that receipt.

## Source access caveats

Reddit public JSON was blocked. The r/webdev RSS fallback returned fresh posts, including an unrelated undocumented-code discussion; its comment thread could not be fetched because Reddit returned HTTP 403. r/SideProject hit HTTP 429, and the broader RSS probes for r/SaaS, r/sysadmin, and r/selfhosted were unavailable/rate-limited, so this winner does **not** claim Reddit validation. X authentication reached `whoami`, but X search returned HTTP 401; no X search signal is claimed. Web evidence above is from HubSpot's public documentation fetched directly.
