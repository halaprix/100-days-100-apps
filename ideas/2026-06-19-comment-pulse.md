# Day 001 — CommentPulse

Date: 2026-06-19
Status: blocked

## One-line pitch

A creator research dashboard that turns comments into traceable audience pain points and weekly content ideas.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1ua8uk2/i_built_an_automation_that_tells_a_youtube/ | Builder found repeated audience questions buried in YouTube comments; the useful differentiator was linking every AI insight back to original comment IDs. |
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1ua9ayc/built_a_financial_dashboard_for_creators_selling/ | Creator operators want cross-platform truth, not isolated vanity metrics; public creator-tooling validation is active but distribution is hard. |
| Reddit / r/productivity | https://www.reddit.com/r/productivity/comments/1ua79pm/how_do_i_stop_getting_distracted_online_and/ | A fresh thread shows people explaining specific work-distraction pains in comments; communities already contain content-topic demand if mined carefully. |
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1ua8jy6/built_a_lightweight_logging_dashboard_go_htmx/ | Adjacent signal: indie builders value lightweight dashboards with alerts over heavyweight enterprise tooling. |

## Problem

Creators receive the best product/content research in comments, replies, and community posts, but those signals are noisy and hard to review consistently. Existing analytics tools prioritize views, CTR, watch time, and revenue; they rarely answer “what are people repeatedly struggling with, and which exact comments prove it?”

## Target user

Small YouTube, newsletter, course, and community creators who have enough comments to miss patterns but not enough budget for a researcher or community analyst.

## MVP scope

- CSV comment import first; public video URL import second.
- Cluster comments into repeated pains, questions, objections, praise, and urgent-support flags.
- Show representative comments for every generated insight.
- Export a weekly Markdown/PDF brief with content ideas and original evidence references.
- No posting, replying, scraping behind auth, or audience engagement automation.

## Shortlist considered

| Idea | Source signal | Score | Notes |
|---|---|---:|---|
| CommentPulse | Creator comment pain mining with traceable evidence | 20/25 | Best mix of clear pain, simple MVP, demo value, and creator distribution. |
| FocusFetch | Distraction-safe web research mode for editors/writers | 19/25 | Strong pain from r/productivity; likely crowded with blockers/focus apps. |
| SiteSnap Safety | Construction photos to compliance-ready safety reports | 18/25 | High-value B2B pain, but domain/compliance risk is heavier for day-one build. |
| Loglet Lite | Tiny log dashboard for side projects with webhook alerts | 17/25 | Very feasible; crowded observability market lowers novelty. |
| BrickBin | Loose LEGO inventory and missing-piece matcher | 16/25 | Concrete hobby pain, but narrower distribution and data complexity. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Clear repeated pain: comments contain actionable research but creators miss patterns. |
| Feasibility | 4/5 | CSV import, clustering, SQLite, and Markdown export are small enough for an MVP. |
| Demo potential | 5/5 | A before/after demo from raw comments to a weekly brief is immediately understandable. |
| Distribution | 4/5 | Creators, indie hackers, and marketing operators are reachable through public channels. |
| Novelty/timing | 3/5 | Comment analytics exists, but traceable AI evidence and weekly content briefs are timely. |
| Total | 20/25 | Clears the 18/25 repo-creation threshold. |

## Decision

Create a dedicated repo: [`halaprix/comment-pulse`](https://github.com/halaprix/comment-pulse).

The GitHub repo was created via the API, but the initial scaffold push failed with `403`. The scaffold commit exists locally and is ready to push once GitHub contents write access is fixed. The product should stay narrow: import comments, cluster pains, preserve evidence links, export a weekly brief.

## Next build step

Implement the CSV-import MVP: parse a comment export, store comments in SQLite, generate deterministic theme stubs, and export a Markdown brief with comment IDs preserved.

## Research access note

Reddit public JSON returned 403 from this environment, so the run used public Reddit RSS/web pages plus web extraction. X search returned 401 despite account lookup working, so X was treated as unavailable for this run and not used as evidence.
