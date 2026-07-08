# Day 020 — DavSync Doctor

Date: 2026-07-08
Status: repo-created
Repo: https://github.com/halaprix/davsync-doctor

## One-line pitch

A local-first CardDAV/CalDAV diagnostic CLI that tells Radicale/Baïkal self-hosters why iOS or macOS Contacts is not syncing before they leak configs into support threads.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback | https://www.reddit.com/r/selfhosted/comments/1uqiwcw/apple_contacts_issue_with_radicale/ | Fresh r/selfhosted post: Apple Contacts only syncs 7-8 of 20 contacts to Radicale; user cannot tell whether edits, account setup, or server behavior is responsible. |
| GitHub issue | https://github.com/Kozea/Radicale/issues/1865 | Radicale user reports iOS 18.4+ CardDAV/CalDAV failure despite correct credentials, nearly five hours lost, username-encoding confusion, and failed workarounds. |
| Radicale docs | https://radicale.org/v3.html | Radicale is positioned as out-of-the-box CardDAV/CalDAV, but the docs also acknowledge protocol complexity and client-specific behavior. |
| CalConnect CardDAV guide | https://devguide.calconnect.org/carddav/building-a-client/ | CardDAV has a clear diagnostic chain: well-known discovery, principal, addressbook-home-set, address book listing, REPORT, PUT, and sync. |

## Source access caveats

- X/Twitter auth check worked (`whoami`), but X search returned `401 Unauthorized`; no X search evidence was used.
- Reddit public JSON was blocked with `HTTP 403 theme-beta`; r/selfhosted RSS fallback worked for listing posts.
- Reddit thread/comment JSON fetches for shortlisted posts were blocked with `HTTP 403`; the brief uses the RSS post summaries plus web-extracted public sources.
- Some subreddit RSS/JSON calls returned `HTTP 429`; I stopped retrying and used web search/extraction for competitor validation.

## Problem

Self-hosted DAV users can have a server that appears healthy while Apple Contacts silently leaves some contacts on-device, fails to show collections, or breaks after an iOS/macOS change. The debugging path is too manual: re-add the account, tweak usernames and URLs, try `curl` snippets, read Radicale logs, inspect GitHub issues, and ask Reddit with a half-redacted config.

This passes the status-quo pain test: failed contact/calendar sync risks data loss, blocks trust in self-hosted identity/contact workflows, and can burn multiple hours because the failure may sit across client discovery, auth encoding, proxy headers, collection permissions, vCard validity, or sync tokens.

## Target user

Self-hosters running Radicale, Baïkal, or a similar small CardDAV/CalDAV server who need native iOS/macOS Contacts or Calendar sync to work reliably.

## MVP scope

- `davsync-doctor check <url>` CLI with password prompt and no secret logging.
- Read-mostly CardDAV checks for:
  - `/.well-known/carddav` redirect behavior,
  - `current-user-principal`,
  - `addressbook-home-set`,
  - address book collection discovery,
  - OPTIONS capability,
  - sample `addressbook-query` REPORT,
  - ETag/sync-token visibility,
  - optional local vCard syntax validation.
- Detect common Apple-facing traps: username encoding, missing collection visibility, TLS/proxy redirect mismatch, read-only permissions, malformed vCards, and stale sync metadata.
- Emit a redacted Markdown/JSON report suitable for GitHub or Reddit support posts.

## Shortlist considered

| Candidate | Wedge-first gate | Outcome |
|---|---|---|
| DavSync Doctor | Radicale/Baïkal self-hosters with Apple Contacts failures → `curl`, Radicale logs, docs, generic DAV tools → substitutes do not map Apple-visible sync prerequisites into a safe report → narrow CardDAV diagnostic and redacted issue bundle → r/selfhosted, Radicale issues, CardDAV/iOS search traffic → fresh r/selfhosted complaint plus iOS 18.4+ issue history. | Winner. |
| DockerRaw Doctor | Docker Desktop/self-hosted users with growing Docker.raw/VM disk → `docker system df`, prune docs, Docker Disk Usage extension → substitutes either delete too broadly or focus on Docker Desktop GUI → dry-run reclaim plan that explains volumes/cache/sparse VM growth → r/selfhosted and Stack Overflow answers → fresh post about Docker storage growing until services fail. | Rejected/narrowed: Docker already has official prune docs and a 1M+ Disk Usage extension; wedge is weaker unless focused on non-Desktop servers. |
| FirstWatch Ping | Plex/Tautulli users who forget to log movies → Tautulli webhooks, iOS Shortcuts, Trakt/Letterboxd scripts → setup is fiddly, but the pain is mostly convenience → first-watch-only notification bridge → r/Plex/r/Tautulli content and media-server communities → fresh r/selfhosted request. | Idea-only/rejected: status-quo pain is below the bar; existing webhook/script paths are acceptable for many users. |
| VPS Fit Sheet | Small self-hosted app owners choosing VPS/PaaS/home lab → VPS calculators and provider comparisons → calculators compare specs but not exposure/backups/deployment burden → workload-specific placement checklist → r/selfhosted content/search → fresh post asks about pricing, public IP exposure, backups, deployment ease. | Rejected: crowded calculator/comparison space and overlaps prior LabFit; distribution/wedge too vague. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Apple `ccs-caldavclientlibrary`, generic WebDAV check tools, `davcli` | Useful for developers/protocol implementers, but not packaged as a self-hoster-safe Apple Contacts diagnostic with plain-language checks and redacted report output. |
| Direct competitor | Radicale documentation/issues and Baïkal/sabre docs | Good reference material, but users still have to infer which discovery/auth/collection step failed. |
| Indirect substitute | `curl` PROPFIND/REPORT snippets, server logs, browser login checks | Can identify pieces of the problem, but is slow, easy to mis-run, and risky to paste publicly. |
| Indirect substitute | Android DAVx5-style client testing | Helps prove the server works for another client, but does not explain native iOS/macOS failure modes. |
| Status quo | Re-add the Apple account, edit usernames/URLs, try random workarounds, ask Reddit/GitHub | Wastes hours and risks leaking private hostnames, usernames, contacts, or headers. |

## Wedge

DavSync Doctor is narrow by design: Radicale/Baïkal-style CardDAV plus native Apple client sync failure. The wedge is not “yet another DAV client”; it is a diagnostic checklist and redacted support bundle that follows the exact discovery chain Apple depends on and explains what each failure means.

Distribution is concrete: reply manually with the tool/report format in Radicale GitHub issues, r/selfhosted CardDAV/iOS threads, and search-targeted docs for “Radicale iOS contacts not syncing” and “CardDAV account verification failed”.

## Kill condition

Reject or narrow if the first implementation cannot identify at least three real failure classes beyond “credentials wrong”, or if existing DAV test tools already produce an Apple-client-focused redacted report with better UX.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Broken contacts/calendar sync creates real trust and data-loss anxiety, and public evidence shows multi-hour debugging loops. |
| Feasibility | 4/5 | CardDAV discovery and REPORT checks can be implemented with HTTP/XML in a 1-3 day CLI MVP; Apple device internals are out of scope. |
| Demo potential | 4/5 | A local Radicale fixture can show pass/fail checks and a redacted Markdown report clearly in a terminal/GIF. |
| Distribution | 4/5 | Specific channels exist: r/selfhosted, Radicale issues/discussions, Baïkal/sabre communities, and search docs around iOS CardDAV failures. |
| Competitive wedge / timing | 3/5 | Wedge is credible but narrow; incumbents are mostly generic protocol tools/docs, not Apple-focused self-hoster diagnostics. |
| Total | 19/25 | Clears repo threshold and dimension gates. |

## Decision

Create the repo. The score is 19/25 with distribution 4/5 and competitive wedge/timing 3/5, so it clears the repo creation gates. Status: `repo-created` after scaffold push and tag verification.

Weakest dimension: competitive wedge/timing at 3/5. The MVP must prove it diagnoses Apple-visible sync failures better than generic DAV tooling.

## Next build step

Implement `davsync-doctor check` against a local Radicale container fixture with redaction tests for URLs, usernames, Authorization headers, and contact fields.
