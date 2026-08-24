# AssistCutover

A local-only migration readiness scanner for OpenAI Assistants API applications.

## Problem

Teams with production code still calling the Assistants API face a hard sunset on
August 26, 2026. The official migration guide explains the target API, but it
cannot inventory a repository's raw endpoints, SDK calls, dynamic assistant
creation, persistent-thread assumptions, or tool/file dependencies. Under a
short deadline, a manual grep and generic coding agent leave migration risk
unowned and untestable.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Original platform announcement | https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666 | OpenAI says the Assistants API beta sunsets on August 26, 2026 and points users to the Responses API. |
| Official migration guide | https://developers.openai.com/api/docs/assistants/migration | The guide provides side-by-side API patterns, including a move from thread state to conversations. |
| Developer community report | https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666 | A developer reports that dynamically created assistants and prompt creation are not a one-to-one migration. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | OpenAI's Assistants migration guide | Strong target-state documentation, but it does not inspect a repository or emit a project-specific readiness packet. |
| Indirect substitute | IDE search, grep, code agents, and a hand-maintained checklist | Finds obvious SDK calls but misses semantic dependencies and produces no auditable migration inventory. |
| Status quo | Delay, then fix production breakage after the sunset | A service outage or emergency rewrite is materially worse than a local preflight. |

## Wedge

**Teams maintaining a JavaScript or Python Assistants API app → official docs plus grep → generic guidance cannot show which risky legacy patterns exist → local static inventory and ordered migration packet → OpenAI Developer Community and GitHub issue searches → the August 26, 2026 sunset creates an immediate cutover window.**

AssistCutover does not generate a blind rewrite or send source code to a service.
It answers the first operational question: *what exactly must this repository
prove before we can switch?*

## Target user

A small product or platform team that owns a JavaScript/TypeScript or Python
application using the OpenAI Assistants API.

## MVP

- Scan a local repository without network access or credentials.
- Detect SDK and raw HTTP uses of Assistants, Threads, Messages, Runs, file
  search/vector stores, Code Interpreter, function tools, and dynamic creation.
- Emit JSON plus a Markdown readiness packet with migration mappings, risk level,
  file locations, and verification steps.
- Include a `--fail-on high` CI mode.

## Non-goals

- No automatic source rewrites.
- No API calls, key discovery, upload, or migration of remotely stored data.
- No general-purpose API-deprecation platform.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only.
