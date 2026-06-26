# Day 008 — AgentLedger

Date: 2026-06-26
Status: idea-only

## One-line pitch

A local-first task ledger and proof-of-done dashboard for self-hosted personal agents, so the chat agent, background worker, and “waiting on me” list all derive from one auditable source of truth instead of drifting in separate memories and chat threads.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ufz6kp/247_agent_to_manage_media_server_and_personal/ | Fresh self-hosted user runs a 24/7 “life-ops” agent and reports vanishing projects, repeated waiting-list items, false “done” reports, desynced task lists, timid background work, and context loss. They identify the root cause directly: no single source of truth. |
| Reddit / r/selfhosted comments | https://www.reddit.com/r/selfhosted/comments/1ufz6kp/247_agent_to_manage_media_server_and_personal/ | Community advice pushes against one endless 24/7 context and recommends task-scoped sessions, watchdogs, and explicit proposed-solution loops, reinforcing that durable state should live outside a long chat transcript. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ufx5wg/help_with_nzbdav_its_downloading_the_entire_files/ | Adjacent fresh self-hosted pain: a media-stack configuration caused full files to download locally and consume roughly 1.3 TB. This is not an agent problem, but it shows the same audience values state/config checks that prevent expensive background automation mistakes. |
| Hermes Agent docs | https://hermes-agent.nousresearch.com/docs | Hermes supports messaging channels, persistent memory, skills, cron, subagents, and MCP. It is a capable runtime, but the public docs position it as an agent platform rather than a tiny external task ledger with proof requirements. |
| OpenClaw docs | https://docs.openclaw.ai/ | OpenClaw is a self-hosted multi-channel gateway for AI agents with sessions, memory, routing, and a control UI. This is a direct runtime/platform substitute, not a focused proof-of-done ledger. |
| LangGraph docs | https://docs.langchain.com/oss/python/langgraph/persistence | LangGraph has checkpointers and stores for persistence, human-in-the-loop workflows, time travel, and fault tolerance. Strong building block, but too low-level for a self-hoster who wants a ready task board and invariant checker. |
| n8n blog | https://blog.n8n.io/human-in-the-loop-automation/ | n8n’s human-in-the-loop guidance emphasizes approve/reject checkpoints, audit logs, and routing only risky cases to humans, validating the “automation needs explicit proof and escalation states” pattern. |
| Reddit / r/SaaS | https://www.reddit.com/r/SaaS/comments/1ufy2an/how_much_time_does_your_team_waste_translating/ | Adjacent startup signal: teams waste 3–5 hours/week translating technical progress upward when progress lives in people’s heads. A top comment says the practical fix was a plain-English line at ship time. This informed the “proof line” part of AgentLedger but was not the winning segment. |

Research note: Reddit public JSON was blocked by `HTTP 403 theme-beta`; collection used the reddit-readonly RSS fallback for listing posts and public page extraction for the most relevant threads. Several subreddit RSS requests returned `HTTP 429`, so the run stopped retrying. X read auth worked (`whoami`), but X search returned `401 Unauthorized`, so X was not used as evidence.

## Problem

Self-hosted power users are starting to run personal agents as always-on background operators across media stacks, home automation, research, notifications, and admin chores. The fragile part is not only model quality; it is state discipline.

In the source thread, the same underlying task can appear in a project list, a waiting-for-user list, a chat transcript, and a background worker queue. Once those drift, the agent can lose active projects, resurrect completed requests, claim work is done without proof, or ask for decisions that were already made. The user then has to audit the agent instead of delegating to it.

The status-quo pain clears the threshold: it wastes repeated troubleshooting time, can cause expensive automation mistakes, and destroys trust in background agents. The problem is narrow enough for a 1–3 day MVP if AgentLedger stays a sidecar ledger rather than trying to become a full agent runtime.

## Target user

Self-hosted agent operators and technical hobbyists who:

- already run or want to run an agent through Discord, Telegram, Slack, CLI, or a web UI,
- delegate multi-step personal automation or homelab tasks,
- need a persistent “waiting on me” lane,
- want “done” to require evidence instead of model confidence,
- are comfortable running a small local SQLite-backed service.

## MVP scope

- SQLite task ledger with immutable-ish event log: `created`, `claimed`, `blocked`, `waiting_on_user`, `proof_submitted`, `verified_done`, `reopened`.
- Derived views: project list, active background work, “waiting on me,” stale tasks, and tasks whose proof is missing.
- Simple HTTP API and MCP tool surface: create task, update state, attach proof, ask for next actionable task, list waiting items.
- Tiny web dashboard with drift warnings: “listed as done but no proof,” “waiting item has no source task,” “task stale for N hours.”
- Proof templates: command output, URL, file diff summary, screenshot hash, checklist, or human approval note.
- Optional webhook/CLI adapters for agent platforms; no attempt to replace Hermes, OpenClaw, LangGraph, n8n, or Home Assistant.

Non-goals for v0.1: autonomous execution, general project management, full memory replacement, cloud sync, mobile app, or handling secrets.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Hermes Agent / OpenClaw | They provide agent runtime, channels, memory, skills, sessions, and routing. AgentLedger’s wedge is being a runtime-agnostic state/proof sidecar, not another agent shell. |
| Direct competitor | LangGraph persistence / LangSmith | Strong for engineers building custom agents with checkpointing, stores, and observability. Too low-level for a self-hoster who wants a ready board, “waiting on me” lane, and proof invariants. |
| Direct competitor | n8n / Node-RED / workflow automation tools | Good for deterministic workflows and human approval checkpoints. Less suited to a shared task ledger used by multiple chat agents, watchdogs, and background workers. |
| Direct competitor | Taskade / Notion AI / general AI workspaces | Provide task/project surfaces and agents, but push users into their workspace model instead of sitting beside a self-hosted agent stack. |
| Indirect substitute | Markdown, SQLite, Beads, Linear, GitHub Issues, Todoist, Notion | Any tracker can be the source of truth if the user is disciplined. The gap is automatic proof requirements and drift checks designed for agents, not humans. |
| Indirect substitute | Chat history and memory | Lowest-friction, but this is exactly what produced drift, false done states, and repeated waiting-list items in the source thread. |
| Status quo | Manually audit the agent, rebuild prompts, restart sessions, and reconcile lists by hand | Works for experiments, but collapses as soon as the agent runs background work across several domains. |

## Wedge

**Wedge-first line:** self-hosted personal-agent operators running background “life-ops” workflows → Hermes/OpenClaw memory, LangGraph persistence, n8n workflows, Notion/tasks, and chat history → substitutes either own the whole runtime, require custom engineering, or rely on human discipline, so “done,” “waiting,” and “active” drift across surfaces → a tiny runtime-agnostic SQLite ledger with proof-of-done invariants and derived waiting/task views → r/selfhosted, agent-platform docs/issues, and search content around “agent task state drift,” “AI agent proof of done,” and “waiting on me agent list” → always-on personal agents are moving from demos to real unattended automation.

The wedge is the invariant layer: AgentLedger does not make the agent smarter. It makes the agent unable to silently lose, duplicate, or complete work without a record.

## Kill condition

Reject or narrow if self-hosted agent users say they already trust their runtime’s built-in task/memory model, or if the MVP cannot integrate with at least one common agent surface through simple HTTP/MCP without becoming a platform-specific plugin. Also reject if users want a full project-management app; that turns the wedge into a crowded productivity category.

## Shortlist notes

| Candidate | Wedge-first gate result | Score | Decision |
|---|---|---:|---|
| AgentLedger | Self-hosted personal-agent operators → Hermes/OpenClaw/LangGraph/n8n/chat memory → substitutes do not provide a small runtime-agnostic proof ledger and derived waiting list → SQLite sidecar with proof invariants and drift checks → r/selfhosted plus agent-platform issue/search content → always-on personal agents are becoming real enough to fail painfully. | 18/25 | Winner, idea-only. Clears total and wedge gate, but distribution is still only 3/5, so no repo today. |
| ProgressLine | Early-stage startup founders/COOs translating engineering progress → Linear/Jira/Slack/standup bots/manual calls → updates live in heads and need business-language rewriting → PR/issue “did X, unblocks Y, risk Z” habit collector → r/SaaS founder/operator content → fresh thread reports 3–5h/week wasted. | 17/25 | Held. Strong pain, but Linear, Slack AI, Range, Geekbot, Standuply, and Steady already crowd the coordination/update space. |
| FunnelStitch | Bootstrapped SaaS founders wanting website→signup→paid→churn insight under $100/mo → PostHog/Metabase/Looker/Mixpanel/manual LLM prompts → cheap tools do funnels but not reliable experiment suggestions → export-to-LLM playbook plus connector templates → r/SaaS analytics questions/search → fresh post asks for this exact stack. | 15/25 | Rejected/held. Analytics + AI insights is explicitly crowded; wedge is not sharp enough. |
| SpinwheelScope | Fintech/debt-payoff app founders evaluating debt APIs → vendor calls/docs/peer anecdotes → integration reliability and pricing are hard to verify before commitment → checklist plus sandbox smoke-test harness → startup fintech API searches → fresh r/startups post asks for Spinwheel alternatives and integration feedback. | 14/25 | Held. Potentially useful, but depends on private API access and a narrow paid vendor ecosystem. |
| SafeOSS Triage | Self-hosters anxious about fast-moving open-source apps → GitHub stars/README/community trust/manual audit → visible popularity misses governance red flags → local repo risk report focused on contributor velocity, signatures, releases, and sandbox tips → r/selfhosted security posts/search → fresh post worries about a 25-day-old high-commit project. | 14/25 | Rejected for now. Security scanner category is reject-by-default; needs a sharper non-generic wedge. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The source pain includes lost tasks, false done states, repeated waiting items, and costly background-automation risk. This is more than convenience. |
| Feasibility | 4/5 | A SQLite service, dashboard, HTTP API, and MCP tools are buildable quickly. The hard part is staying runtime-agnostic and not expanding into a full agent platform. |
| Demo potential | 4/5 | Easy demo: show a chat agent marking a task done without proof, AgentLedger flags it, then a verified proof line moves it to done and updates “waiting on me.” |
| Distribution | 3/5 | Specific communities exist (`r/selfhosted`, agent platform users, homelab blogs), but repeatable access is not proven and the user base is still technical/niche. |
| Competitive wedge / timing | 3/5 | Strong timing around always-on agents, but major runtimes and workflow tools can absorb parts of this. The wedge must stay focused on proof/state invariants. |
| Total | 18/25 | Save as idea-only because the distribution gate fails: 3/5 is below the required 4/5 for repo creation. |

## Decision

Save AgentLedger as `idea-only`; do not create a dedicated repo today. It clears the 18/25 total threshold and the competitive-wedge gate, but it fails the distribution gate. The next validation should prove that self-hosted agent operators actively search for and adopt a sidecar ledger, rather than expecting their agent runtime to solve this internally.

## Next build step

Run a 90-minute validation spike: write a public mini-spec and mock dashboard for the exact failure modes from the r/selfhosted thread, then collect reactions from self-hosted/agent communities. If at least three operators say they would wire an HTTP/MCP sidecar into their current agent stack, create the project repo and build the SQLite ledger MVP.
