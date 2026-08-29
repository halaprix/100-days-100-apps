# Day 065 — SwapCheck

Date: 2026-08-29
Status: repo-created

## One-line pitch

A local, read-only CLI that turns a GitHub Copilot model-policy export and
repository references into a dated migration packet before model retirement or
policy changes interrupt agent and review workflows.

## Evidence

| Source | Link | Signal |
|---|---|---|
| GitHub changelog | https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot/ | GitHub says Gemini 3.1 Pro, several Claude models, and Raptor Mini retire across Copilot experiences on September 1, 2026; organizations may need to enable alternatives through model policy. |
| GitHub changelog | https://github.blog/changelog/2026-08-26-global-model-policy-generally-available/ | Enforcement of the global model policy rolls out through September 1. Newly unconfigured models can inherit its state, so availability is not just a model-name replacement. |
| GitHub changelog | https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing/ | GitHub also announced August 28 policy changes affecting the unified Copilot experience and review defaults, creating an immediate administrator review window. |
| Reddit community report (RSS fallback) | https://www.reddit.com/r/SideProject/comments/1w1eng5/hackeroom_isnt_claude_codeonly_anymore_mix_claude/ | A fresh builder post describes mixing models in one agent workflow, a public example that model choice and shared guardrails are operational concerns rather than cosmetic settings. |

## Problem

A Copilot admin facing a retirement or policy rollout must reconcile four moving
pieces: named models in agent instructions and runbooks, GitHub's retirement
mapping, per-model or inherited policy state, and client availability. GitHub
provides the setting UI and documentation, but a manual review produces no
portable record of which workflow depends on a model, what replacement is
allowed, or which behavior-sensitive task needs a deliberate retest. The
workaround is repository search plus a spreadsheet and settings screenshots;
it can consume hours during a deadline and can leave an agent/review workflow
silently behaving differently after a default changes.

## Target user

A GitHub Copilot Business or Enterprise administrator and platform engineer
responsible for named-model policy and agent/review workflows across a small
set of repositories.

## MVP scope

- Read a local JSON/YAML model-policy export and an allowlisted repository path.
- Find named model references only in selected text configuration files.
- Join references to a versioned, public migration manifest containing retirement
  dates, suggested alternatives, and policy/client caveats.
- Emit a Markdown/JSON approval packet with affected paths, policy state,
  replacement, and required human retest; fail CI for retired or disabled models.
- Remain local and read-only: no GitHub API access, policy edits, prompt upload,
  model execution, or automatic text replacement.

## Shortlist and wedge-first gate

1. **SwapCheck — selected.** Copilot organization admin → GitHub settings,
   changelog, spreadsheet, and manual repository search → settings configure
   access but do not join source references, retirement dates, inherited policy,
   and retest ownership → local migration packet for named models only → GitHub
   Copilot admin docs/changelog, GitHub Community, and platform-engineering
   change-control content → September 1 retirements and simultaneous policy
   rollout create a dated review window.
2. **TillShield — rejected.** Independent retailer with a bespoke web POS →
   Windows kiosk/MDM tools and a security consultant → those configure endpoints
   but do not understand every custom business workflow → deployment checklist
   for browser POS terminals → retail-tech consultants and bespoke-POS builders
   → a fresh r/webdev operator is adding locations. **Kill:** KioWare/Codeproof
   and a competent security consultant already cover too much of the job; one
   thread does not prove a repeatable first-user channel.
3. **ShortcutTrace — rejected.** Front-end developer with one broken browser
   key → DevTools, framework docs, and manual event logging → repetitive but
   workable for an isolated bug → event-propagation recorder → framework issue
   searches and webdev content → a fresh r/webdev report. **Kill:** pain is
   sporadic and usually below the 30-minutes-per-week threshold.
4. **MetricGuard — rejected.** IT support lead asked for defensible KPIs → JSM,
   ServiceNow, marketplace dashboards, and a spreadsheet → reporting tools
   already compute the proposed metrics → incentive-risk annotation for a
   handpicked report → ITSM communities → a fresh r/sysadmin question. **Kill:**
   it is a crowded analytics dashboard problem, and direct products already
   cover reporting well.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GitHub Copilot settings and model-policy UI | The authoritative place to configure model access, but it does not produce a local migration manifest, scan repository model references, or assign retests. |
| Direct competitor | General prompt/model evaluation platforms | They can benchmark prompts, but require model execution and address a broader job; the MVP is a deterministic policy-and-reference packet with no prompt data or API credentials. |
| Indirect substitute | GitHub changelog + manual repository search + spreadsheet | Common and flexible, but reconciliation of policy inheritance, client availability, retirement mapping, and owners is manual and difficult to audit later. |
| Status quo | Let model retirement or a default-policy shift expose the gap | A named model can disappear or a workflow can change behavior during a production review/agent task; recovery happens under deadline pressure. |

## Wedge

SwapCheck is narrowly scoped change control, not another LLM dashboard or a
policy editor. It remains credential-free and deterministic: an administrator
supplies an export, gets a small review artifact, and decides whether a
replacement needs a retest. GitHub's August 26 policy rollout and September 1
model retirements make the first use case unusually time-bound. The first-user
channel is concrete: publish a public migration-manifest example and CLI output
in GitHub Copilot administrator/community discussions and platform-engineering
change-review content, then invite affected organizations to run it against a
sanitized fixture before their policy review.

## Kill condition

Reject or narrow after five administrator/platform-engineer interviews if fewer
than three would use a local packet in a model-change review, or if GitHub ships
a first-party export plus a repository-reference migration report that covers
policy inheritance and retest ownership. Also stop if target users only want
full prompt benchmarking; that is a different, crowded product category.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A deadline-bound admin failure can interrupt multiple workflows; the pain is acute but limited to organizations with named-model governance. |
| Feasibility | 5/5 | A local parser, versioned public manifest, allowlisted text scan, and Markdown/JSON renderer fit a 1–3 day CLI MVP. |
| Demo potential | 4/5 | Before/after packet showing a retired model, policy state, replacement, and retest is easy to show without sensitive inputs. |
| Distribution | 4/5 | Affected Copilot administrators have specific GitHub changelog, Community, and policy-review channels; fixture-based content gives a repeatable entry point. |
| Competitive wedge / timing | 4/5 | Settings UI handles configuration and generic eval tools handle testing; the narrow policy-plus-reference packet is distinct, and the September 1 deadline/policy rollout is immediate. |
| Total | 21/25 | Clears the repo threshold and both dimension gates. |

## Decision

**repo-created.** The local dedicated scaffold is at
[`projects/swapcheck`](../projects/swapcheck) and its public-safe snapshot is
consolidated at the same master-index path. It has no dedicated GitHub remote;
this does not claim a new remote repository exists.

## Next build step

Implement `swapcheck inventory` against fixture repositories, then validate the
packet with five Copilot administrators or platform engineers before extending
into policy matching.

## Source access caveats

Reddit public JSON was blocked with the documented `theme-beta` response. The
RSS fallback returned fresh entries for r/SideProject, r/Entrepreneur,
r/sysadmin, and r/webdev; r/SaaS, r/startups, r/selfhosted, r/LocalLLaMA, and
r/androidapps hit RSS `429` during this run, so no engagement counts are
claimed. The selected Reddit evidence is an RSS-fallback permalink, not a
validated consensus signal. X `xurl` authentication/status was checked, but
search returned `401 Unauthorized`; no X evidence is claimed. Web evidence is
from public GitHub changelog/docs pages.
