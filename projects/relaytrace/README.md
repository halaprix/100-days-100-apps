# RelayTrace

A local-first SMTP forwarding and catch-all envelope probe for self-hosted mail admins.

## Problem

Self-hosted mail users often put an ISP, VPS, or filtering relay in front of a
home mail server. That relay may accept every address for a domain, scan the
message, then forward it onward with the original envelope recipient hidden in a
custom header such as `X-Envelope`, `X-Original-To`, or `Delivered-To`.

The setup works until it does not: catch-all routing, alias extraction, spam
tracing, and per-recipient rules can silently fail if the relay rewrites the
recipient, strips the header, or delivers test mail through a different path.
The usual debug loop is manual: send messages, inspect raw headers, read Postfix
or mail-stack docs, then paste sanitized snippets into forums.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vgtyki/smtp_forwarding/ | Fresh self-hosted mail user describes ISP SMTP forwarding with an `X-Envelope` header and asks for a replacement that preserves catch-all recipient processing while shielding the home server. |
| Swaks | https://www.jetmore.org/john/code/swaks/ | Mature SMTP test tool confirms SMTP probing is scriptable, but it is a generic transaction tool rather than a catch-all relay verdict packet. |
| MXToolbox SMTP Diagnostics | https://mxtoolbox.com/diagnostic.aspx | Online diagnostics test server connectivity, open relay behavior, PTR, and response time, not private relay envelope/header preservation. |
| MXToolbox Email Header Analyzer | https://mxtoolbox.com/EmailHeaders.aspx | Header parsing is a known diagnostic workflow, but users still interpret forwarding-specific recipient headers manually. |
| Postfix Address Rewriting docs | https://www.postfix.org/ADDRESS_REWRITING_README.html | Postfix documents address rewriting, aliasing, local catch-all behavior, and debugging, but not an app-shaped probe packet for front-relay handoffs. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Swaks | Excellent generic SMTP transaction tool. It can send probes but does not encode the self-hosted catch-all relay workflow or produce pass/fail evidence packets. |
| Direct competitor | MXToolbox SMTP Diagnostics / Email Header Analyzer | Good hosted diagnostics for public mail server health and readable headers; not local-first and not aimed at validating custom envelope-recipient preservation across a private forwarding relay. |
| Direct competitor | mailcow, docker-mailserver, Mailu, maddy docs/admin UIs | Full mail stacks solve hosting and alias management, but admins still need to verify how an upstream relay rewrites or preserves recipient evidence. |
| Indirect substitute | Manual test messages, raw header inspection, Postfix maps, forum advice | Works for experts but burns time and produces inconsistent evidence when aliases, catch-all addresses, and provider headers differ. |
| Status quo | Keep the ISP relay, hope the custom header is stable, and debug only after a message lands in the wrong rule or disappears | Risks lost mail, broken spam-source tracing, and hours of fragile troubleshooting. |

## Wedge

RelayTrace is not a mail server and not another deliverability dashboard. The
narrow wedge is a public-safe probe packet for one painful handoff: "did my
front SMTP relay preserve enough recipient evidence for my self-hosted catch-all
processor to route this message correctly?"

It can be useful before any live integration by accepting a probe plan and saved
RFC822 messages, then reporting whether expected unique recipients appear in
allowed headers, whether multiple aliases collapse into one value, and which
relay assumptions are unproven.

## Target user

- Self-hosted mail admins using an ISP/VPS/filtering relay in front of a home or
  small-team server.
- Users of Postfix, mailcow, docker-mailserver, Mailu, or maddy who rely on
  catch-all aliases and recipient-tag processing.
- Small operators who need a sanitized packet to discuss with a provider or
  community before changing MX records.

## MVP

- `relaytrace check --plan examples/catchall-relay.yaml --inbox examples/messages/`.
- YAML plan with expected recipient aliases and accepted envelope header names.
- RFC822 parser that scans raw messages for `X-Envelope`, `X-Original-To`,
  `Delivered-To`, `Original-Recipient`, and configured custom headers.
- Markdown and JSON verdicts: preserved, missing, ambiguous, overwritten, or
  untested.
- Public-safe sample messages only; no real credentials or live SMTP sending in v0.

## Non-goals

- No hosted email deliverability scoring.
- No replacement for Postfix/mailcow/docker-mailserver/Mailu/maddy.
- No storage of real email bodies beyond user-provided local fixtures.
- No DNS or MX mutation.
- No live SMTP authentication in the scaffold release.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
