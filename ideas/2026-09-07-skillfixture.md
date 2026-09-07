# Day 074 — SkillFixture

Date: 2026-09-07
Status: idea-only

## One-line pitch

A local CLI that turns an agent-skill folder into a reproducible compatibility
receipt: validate its manifest and bundled files, run declared fixture commands
in an isolated temporary directory, and emit a shareable pass/fail report before
an author publishes the skill.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS fallback | https://www.reddit.com/r/SideProject/comments/1w9kzmm/i_launched_skill_grill_a_community_directory_for/ | A freshly launched directory explicitly asks users to judge whether agent skills actually work rather than relying on stars or install counts. This is one founder report, not evidence of broad demand, but it exposes a trust gap around shipped skill packages. |
| Anthropic documentation | https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview | Agent Skills are filesystem directories that may bundle YAML metadata, instructions, scripts, and reference materials. That package shape creates deterministic checks that are separate from judging an agent's semantic output. |
| Promptfoo documentation | https://www.promptfoo.dev/docs/intro/ | Promptfoo is an established CLI/library for LLM-app evaluation, automated scoring, red teaming, and CI. It is a strong broad substitute and sets a high bar for any testing claim. |
| OpenAI evaluation documentation | https://platform.openai.com/docs/guides/evals | OpenAI documents eval workflows for model/agent behavior and regression testing. This confirms that general evaluation already exists; SkillFixture must stay narrowly focused on portable skill-package contracts. |

## Problem

Agent-skill authors can publish a folder that looks complete while its frontmatter,
linked files, executable scripts, or declared setup assumptions fail on another
machine. Today a prospective user can inspect a README, star count, or a directory
listing, then manually install and try it. That makes failures costly in setup time
and makes a directory's reputation vote subjective rather than reproducible.

This run has only one fresh community report, so it does **not** establish a
high-frequency, ecosystem-wide pain. The status-quo test passes only for authors
and reviewers who repeatedly publish, evaluate, or curate skills: debugging a
broken install can consume well over 30 minutes and damages a public listing's
trust. For one-off authors, manual testing remains tolerable.

## Target user

Maintainers of filesystem-based agent skills who publish a skill directory or
review submissions for a curated collection and need a deterministic, local
pre-publication check without sending prompts, repositories, or credentials to a
third-party evaluation service.

## MVP scope

- Parse and validate `SKILL.md` frontmatter, referenced relative files, and
  declared fixture metadata.
- Create a temporary workspace containing only the tested package and fixture
  inputs; network access is disabled by default where the host supports it.
- Run explicitly declared deterministic smoke commands with time and output
  limits; never infer or execute arbitrary commands from prose.
- Check expected files and sanitized output snapshots, then emit Markdown and
  JSON receipts with the exact failed contract.
- Provide an opt-in adapter interface for a small set of filesystem skill
  layouts; report unsupported runtimes instead of claiming compatibility.
- No model calls, cloud dashboard, marketplace, automatic publishing, secret
  scanning, autonomous code repair, or semantic quality scoring in the MVP.

## Shortlist and wedge-first gate

1. **SkillFixture — selected.** Filesystem-skill maintainer or curator → manual
   install plus stars/directories, Promptfoo, and general eval platforms → these
   either do not prove package references and deterministic setup work or require
   an author to construct a bespoke app-eval harness → local, declarative
   skill-folder contract test and receipt → publishable GitHub Action plus exact
   searches for agent-skill templates, directory submissions, and broken-skill
   setup reports → skills are increasingly packaged as folders containing
   metadata, instructions, scripts, and assets, while a fresh directory launch
   asks for evidence that skills work. **Kill:** ten representative public skill
   repositories show that their current CI already catches missing references,
   unsupported setup, and fixture regressions with no meaningful extra work; or
   maintainers will not add fixtures before publishing.
2. **Directory reputation layer — rejected.** Prospective skill installer →
   Skill Grill-style community listings, GitHub stars, and comments → reputation
   is social and susceptible to sparse feedback, but a new directory requires a
   two-sided network before it can improve trust → verified-directory badge →
   directory-launch audiences → the fresh source is itself an early directory
   product and does not prove supply or demand for another directory. **Kill:**
   network-effect dependency without a controlled first-user channel.
3. **AI-written-code preflight — rejected.** Solo developer shipping AI-written
   code → local scanners, dependency tools, code review, and the OnePort launch
   in the fresh Reddit feed → the job is already a crowded generic security and
   autofix-wrapper category → no narrow workflow beyond an all-in-one verdict →
   generic launch/security audiences → explicit reject-by-default category and
   no differentiated first-user channel. **Kill:** crowded category.
4. **Travel-recommendation extractor — rejected.** Traveler planning a city trip
   → Reddit search, maps, guidebooks, and travel-planning apps → extracted
   sentiment is hard to verify, freshness and context are weak, and travel apps
   already own discovery → travel-subreddit citation layer → generic travel
   searches → no demonstrated status-quo harm above a tolerable planning task.
   **Kill:** vague distribution and weak repeated pain evidence.
5. **Movie-soundtrack resolver API — rejected.** Movie-site developer needing
   official soundtrack links → manual Spotify search, music metadata services,
   and the fresh SoundtrackDB launch → the claimed API gap may involve unstable
   catalog matching and music-service terms, not a simple software wedge → title
   resolver API → generic entertainment-developer distribution → a single
   founder claim is insufficient and data-rights risk blocks a 1–3 day MVP.
   **Kill:** unresolved data provenance or platform-policy constraints.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Promptfoo | Mature local/open-source evaluation and red-team tool with CI support. It can test an agent application, but it is broader than a no-model skill-package contract runner. |
| Direct competitor | OpenAI Evals | General model and agent-evaluation workflows can cover behavior/regressions, but they require the author to define an evaluation around an application rather than validating a portable skill folder's declared assets and fixtures. |
| Direct competitor | Skill Grill | A newly launched community directory for discovering and rating agent skills. It addresses discovery and subjective reputation, not reproducible pre-publication package checks. |
| Indirect substitute | Manual installation, README review, GitHub stars, and ad-hoc shell testing | Cheap for one skill, but a reviewer must recreate assumptions and cannot compare a reproducible pass/fail receipt across submissions. |
| Status quo | Publish first; users report broken references or setup afterward | The direct cost is repeated setup/debugging and a public trust hit. This matters only when a maintainer or directory curator handles enough submissions for the repetition to exceed a tolerable one-off check. |

## Wedge

SkillFixture should not compete with general LLM evaluation, agent observability,
or security scanning. It wins only if it can transform a skill folder plus a small
fixture declaration into a deterministic local compatibility receipt in one
command, while broad eval platforms require a model/application harness and
community directories can only collect subjective reports after publication.

The distribution path is specific but not yet repeatable: a GitHub Action,
portable skill template, and targeted content/search/reply work around public
skill repositories and directories. That reaches an identifiable audience, but
this run has not proved a channel with reliable conversion, so Distribution stays
at 3/5.

## Kill condition

Reject or narrow SkillFixture if a sample of ten public skill repositories shows
that existing CI already catches package-reference, fixture, and setup failures
without meaningful extra configuration; or if five skill maintainers decline to
maintain even a small deterministic fixture. Also stop if the intended runtime
cannot safely isolate declared smoke commands without broad host access.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | Broken published skills can waste meaningful setup/review time, but this run has one fresh founder report rather than repeated independent pain. |
| Feasibility | 5/5 | Frontmatter/file checks, declared fixture execution, snapshots, and deterministic reports are a credible 1–3 day local CLI MVP. |
| Demo potential | 4/5 | A missing referenced file or failing smoke command turning into a concise receipt is easy to show with synthetic skill folders. |
| Distribution | 3/5 | Skill authors and curators are identifiable, but the GitHub Action/template path is not yet a proven repeatable acquisition channel. |
| Competitive wedge / timing | 3/5 | The package-contract boundary is narrower than Promptfoo/OpenAI-style behavior evals and aligns with folder-based skills, but existing broad evaluation tools are strong substitutes. |
| Total | 18/25 | Clears the numeric threshold but fails the Distribution gate. |

## Decision

**idea-only.** SkillFixture scores 18/25, but Distribution is 3/5 rather than
the required 4/5 for a dedicated project. No repo was created. The score should
not be upgraded until direct maintainer validation demonstrates that the fixture
receipt solves a repeated review/publishing failure and the GitHub Action or
another first-user route produces adoption.

## Next build step

Run a no-publish validation spike against ten public skill repositories: inventory
whether each has frontmatter, linked assets/scripts, existing CI, and a
reproducible smoke fixture; then ask five maintainers whether they would add a
small fixture to prevent post-publication breakage before scaffolding a project.

## Source access caveats

Reddit public JSON was blocked with the documented `403` theme-beta response.
The read-only tool successfully used public RSS for r/SideProject, which supplied
the selected fresh source; RSS does not expose reliable score or comment metadata,
so this brief makes no engagement or consensus claim. Subsequent small r/SaaS and
r/webdev RSS probes returned `429` and were not retried. Broader Reddit fallback
queries returned no results.

`xurl` could read account identity but reported no default OAuth 2 token; its
read-only X search probe returned `401 Unauthorized`. No X signal is used.
Direct extraction of Anthropic, Promptfoo, and OpenAI documentation succeeded;
the web-search backend returned no results for the tested discovery queries.
