# DavSync Doctor

A local-first CardDAV/CalDAV diagnostic CLI for self-hosters whose iOS or macOS contacts stop syncing with Radicale, Baïkal, or similar DAV servers.

## Problem

Self-hosters can have a CardDAV server that works in a browser, Thunderbird, or Android client while Apple Contacts silently leaves records on-device or fails to show collections. The current debugging loop is slow: re-add the account, tweak usernames and reverse-proxy paths, inspect server logs, search GitHub issues, then post a partial configuration dump publicly.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit | https://www.reddit.com/r/selfhosted/comments/1uqiwcw/apple_contacts_issue_with_radicale/ | Fresh self-hosted user reports Apple Contacts only syncing 7-8 of 20 contacts to Radicale and cannot tell why. |
| GitHub issue | https://github.com/Kozea/Radicale/issues/1865 | Radicale user says iOS 18.4+ CardDAV/CalDAV failure cost nearly five hours and involved username-encoding confusion and failed workarounds. |
| Radicale docs | https://radicale.org/v3.html | Radicale positions itself as out-of-the-box CardDAV/CalDAV, but its docs also note protocol complexity and client-specific behavior. |
| CalConnect guide | https://devguide.calconnect.org/carddav/building-a-client/ | The CardDAV discovery path has clear steps that can be automated: well-known URL, principal, addressbook home set, address book listing, REPORT, PUT, sync. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Apple ccs-caldavclientlibrary; generic DAV test tools | Powerful but aimed at protocol implementers, not self-hosters trying to produce a safe, redacted, Apple-client-focused diagnosis. |
| Indirect substitute | `curl` PROPFIND snippets, Radicale logs, browser login checks, server docs | These expose pieces of the problem but do not connect discovery, auth encoding, collection visibility, vCard validity, and safe report generation. |
| Status quo | Re-add the iOS account, edit usernames/URLs, search issues, ask Reddit/GitHub | Wastes hours and risks leaking private URLs, contacts, or credentials in support threads. |

## Wedge

DavSync Doctor is deliberately narrow: Radicale/Baïkal-style self-hosted CardDAV plus Apple Contacts failure reports. It will not be a full DAV client. The initial win is a one-command, read-mostly diagnostic that maps each Apple-visible sync prerequisite to pass/fail output and produces a redacted support bundle.

## Target user

Self-hosters running Radicale, Baïkal, or another small CardDAV server who need contacts and calendars to sync reliably with iPhone, iPad, or macOS native apps.

## MVP

- `davsync-doctor check <url>` runs CardDAV discovery checks against a configured account without printing secrets.
- Verify `/.well-known/carddav`, `current-user-principal`, `addressbook-home-set`, address book discovery, ETag visibility, and a dry-run/sample vCard validation path.
- Detect common iOS/macOS traps: username encoding, missing collection visibility, redirect/TLS/header mismatch, read-only permissions, malformed vCards, stale sync-token behavior.
- Emit a redacted Markdown/JSON report suitable for a GitHub issue or Reddit support post.

## Non-goals

- Not a full contacts manager.
- Not an Apple device automation tool.
- Not a hosted sync service.
- Not storing address books or credentials.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
