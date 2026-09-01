# Day 068 — ReviewDelta

Date: 2026-09-01
Status: idea-only

## One-line pitch

A local, read-only CLI that records a reviewer checkpoint for a GitHub pull
request and later produces a compact “what changed since I last looked” packet:
new commits and files, changed CI state, unresolved threads, and a safe link
back to the live review.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit community report (RSS fallback) | https://www.reddit.com/r/SideProject/comments/1w44eha/i_built_a_readonly_pr_inbox_for_mac_because_code/ | A fresh builder describes code review as “tab archaeology”: moving heads, unresolved conversations, and scattered AI suggestions made it hard to regain context. This is one RSS-only report, not consensus or a competitor endorsement. |
| GitHub Changelog | https://github.blog/changelog/2026-07-09-new-pull-requests-dashboard-is-now-generally-available/ | GitHub made its refreshed pull-request dashboard generally available in July, with an inbox for review requests, CI failures, new comments, and saved views. This validates the workflow importance but materially raises the substitute bar. |
| GitHub product documentation | https://github.com/features/code-review | GitHub positions pull-request review around the diff, conversation, checks, history, an inbox, and Copilot review. It establishes the native workflow that any narrow tool must complement rather than replace. |
| Graphite documentation | https://graphite.com/docs/review-pull-requests | Graphite offers a review queue, comments, timeline, file tree, and navigation across stacked pull requests. It is a strong direct competitor for a broad review-inbox proposition. |

## Problem

When an engineer returns to a pull request after another task, they often need to
reconstruct whether the author pushed a material revision, which conversations
remain unresolved, and whether the CI state changed. The current workaround is
to reopen GitHub tabs, compare the branch by eye, scan the timeline, and revisit
comment threads. For maintainers reviewing several active pull requests, that
can repeat across a week; however, this run has only one direct community report
and does not quantify the time cost.

The product must not be another pull-request dashboard or AI reviewer. Its narrow
job is reviewer re-entry: turn a known prior review checkpoint into an auditable,
read-only delta packet.

## Target user

A maintainer or senior engineer who reviews pull requests across several GitHub
repositories, leaves a review part-way through, and later needs to resume without
reconstructing the full timeline.

## MVP scope

- `reviewdelta mark <pr-url>` records the reviewed head SHA and timestamp in a
  local state file controlled by the user.
- `reviewdelta resume <pr-url>` uses GitHub’s existing API/CLI session to render
  Markdown and terminal output for commits/files after that SHA, current check
  status, unresolved review threads, and links to the relevant GitHub views.
- Label unavailable or permission-limited data as `unknown`; never infer that a
  thread was read, resolved, or safe to merge.
- Keep the tool local and read-only. No review comments, approvals, merges,
  repository writes, AI-generated code review, or central hosted inbox.

## Shortlist and wedge-first gate

1. **ReviewDelta — selected, but held.** Maintainer resuming an interrupted
   GitHub review → GitHub pull-request dashboard, browser tabs, timeline, and
   Graphite → they show current work and broad review state but a reviewer can
   still need to reconstruct the change from their own last checkpoint → local,
   explicit checkpoint-to-delta packet only → GitHub CLI/Marketplace discovery
   plus content targeting “resume PR review,” stale-diff, and unresolved-thread
   searches → GitHub’s new inbox increases review flow but makes a narrowly
   complementary re-entry tool more important and much harder to differentiate.
   **Kill:** GitHub or Graphite already offers the same per-reviewer checkpoint
   delta in a practical workflow, or five maintainers say reopening the native
   timeline takes under five minutes per week.
2. **AnswerThread — rejected.** B2B SaaS founder finding unanswered category
   questions → F5Bot, Syften, Octolens, and manual Reddit searches → broad alerts
   can be noisy, but verified unanswered-thread discovery is still a
   social-listening/lead-mining workflow → manual proof bundle for one public
   question → category-search content → a fresh r/SaaS post about unanswered
   Reddit threads. **Kill:** this is explicitly a crowded, spam-adjacent category;
   established monitoring products already cover the alerting job and there is no
   evidence of a safe first-user channel beyond outreach.
3. **CloseoutInvoice — rejected.** Trade contractor completing field work →
   Jobber, Housecall Pro, QuickBooks, and paper notes → field-to-invoice handoff
   can lag, but mobile field-service suites already create, send, and collect
   invoices on site → photo-to-invoice completeness prompt → trade groups and
   local service-business content → a fresh r/SideProject contractor-backoffice
   report. **Kill:** Jobber’s public mobile invoicing documentation already covers
   the core job; the proposed wedge is too generic without interviews showing a
   specific missing handoff.
4. **AdSpendSignal — rejected.** Early SaaS founder checking whether ad clicks
   are humans → Google Ads, analytics, bot filtering, and manual referrer checks
   → campaign traffic can look misleading, but mainstream analytics already
   filters bots and supports traffic analysis → campaign-quality dashboard →
   founder communities → a fresh r/SaaS paid-ads report. **Kill:** this is a
   reject-by-default analytics dashboard, and Plausible documents automatic bot
   and spam filtering; no narrow workflow wedge was established.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GitHub pull-request dashboard | GitHub’s generally available inbox surfaces review requests, CI failures, comments, ready-to-merge work, filters, and saved views. It is the default substitute and rules out building a generic inbox. |
| Direct competitor | Graphite review queue | Graphite provides a review queue, timeline, comments, file tree, and stacked-PR navigation. Its broad review experience makes a hosted review UI an untenable wedge. |
| Direct competitor | PRamatic | The fresh community post itself describes a read-only macOS PR inbox with contextual agent reviews. It is evidence that a read-only review-inbox product is already being built, not proof of demand for ReviewDelta. |
| Indirect substitute | GitHub tabs, comparison views, timeline, notifications, and `gh pr view` | These are authoritative and free, but require the reviewer to remember or reconstruct their prior checkpoint and manually join revisions, checks, and threads. |
| Status quo | Reopen a pull request and scan it again | Tolerable for a few changes, but repetitive reorientation can delay reviews and make unresolved feedback easier to miss. The size of that cost remains unvalidated. |

## Wedge

The only credible wedge is deliberately small: do not compete with a review
inbox, code-review service, or GitHub UI. Record an explicit reviewer checkpoint
locally and produce a deterministic resume packet only for the delta after that
checkpoint. That is easier to demonstrate than a dashboard and avoids storing
repository data centrally.

This is still an unproven wedge. The current public evidence shows that GitHub
and Graphite cover much of the surrounding workflow, and the fresh post is from
a builder of a neighbouring product rather than a buyer asking for this exact
capability. The distribution path is specific but not yet repeatable enough for
a project repo: publish a fixture-backed GitHub CLI example and test it against
maintainers who search for stale-diff, review-context, and unresolved-thread
problems.

## Kill condition

Reject the bet if a short research spike finds that GitHub’s dashboard, Graphite,
or another established review tool can already save and compare a reviewer’s own
checkpoint with subsequent commits and unresolved threads. Also reject if fewer
than three of five maintainers report that review re-entry causes more than 30
minutes of weekly waste or missed feedback, or if they prefer native GitHub
saved views once shown a resume-packet prototype.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | Review re-entry is credible, but the fresh evidence is one builder report and does not establish a repeated >30-minute weekly cost. |
| Feasibility | 5/5 | A local checkpoint file plus GitHub CLI/API reads and a Markdown renderer fit a 1–3 day CLI spike. |
| Demo potential | 5/5 | A before/after fixture can visibly turn a remembered SHA into commits, changed files, checks, and unresolved threads. |
| Distribution | 3/5 | GitHub maintainers have concrete search terms and the Marketplace/CLI ecosystem, but this run has no validated repeatable first-user path. |
| Competitive wedge / timing | 2/5 | GitHub’s new dashboard and Graphite are strong, current substitutes. The per-reviewer checkpoint is plausible but not yet demonstrated as absent or valuable enough. |
| Total | 18/25 | Clears the numerical threshold but fails both required dimension gates. |

## Decision

**idea-only.** No dedicated repo was created. Although the prototype is feasible
and demoable, Distribution is 3/5 (minimum 4) and Competitive wedge / timing is
2/5 (minimum 3). A repo would create a generic review-tool duplicate before the
only differentiator is validated.

## Next build step

Run five maintainer interviews or a fixture-only CLI spike that compares native
GitHub/Graphite workflows with an explicit checkpoint-resume packet; create a
repo only if at least three users report a recurring re-entry cost and no direct
competitor already performs the same per-reviewer delta.

## Source access caveats

Reddit public JSON was blocked by the documented `theme-beta` response. RSS
fallback returned fresh entries for r/SideProject, r/SaaS, and r/sysadmin; the
selected post is an RSS summary, so no score, comment, or engagement claim is
made. RSS fallback for r/startups, r/selfhosted, and r/webdev then returned HTTP
429, and direct thread retrieval was blocked with the same Reddit response.

X authentication could read the account profile through `xurl whoami`, but X
search returned `401 Unauthorized`; no X evidence is claimed. Web evidence comes
from public GitHub and Graphite documentation, with public competitor
information used to test rather than inflate the wedge.
