# Day 073 — ConfigReceipt

Date: 2026-09-06
Status: repo-created

## One-line pitch

A local-first receipt generator for manually exported appliance configuration
files: capture what was exported, redact the shareable copy, compare revisions,
and generate a restore checklist without connecting to the appliance.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS fallback/direct page | https://www.reddit.com/r/selfhosted/comments/1w8g2ur/solution_suggestions_for_config_backup_and/ | A fresh self-hoster says router exports are dumped in a config folder and asks for export date, purpose metadata, and a paperless-style system. Public replies suggest Git plus dated exports, Obsidian, or NetBox, while describing NetBox as daunting for a small lab. |
| RANCID | https://shrubbery.net/rancid/ | RANCID logs into network devices, collects and normalizes output, emails diffs, and commits configuration history to version control. It establishes a mature automated substitute for reachable, supported gear. |
| Oxidized | https://github.com/ytti/oxidized | Oxidized is a RANCID replacement with scheduled retrieval, version/diff APIs, and support for many device operating systems. It is a strong substitute for ongoing automated backups. |
| NetBox documentation | https://netbox.readthedocs.io/ | NetBox models devices, cabling, connections, and other infrastructure as a network source of truth. It is the viable topology substitute, but it is materially broader than a manual-export receipt. |

## Problem

For a small self-hoster, a manually downloaded router, NAS, switch, or
application export often becomes an opaque file in a generic folder. At the
next firmware change, support request, or recovery attempt, the operator may
not know which device it came from, whether it predates the relevant change,
what it contains, or whether it is safe to share.

The source demonstrates a real workflow gap but only one fresh public account.
It does not prove that every manual export is a recurring weekly pain. The
status-quo harm is most credible at a recovery/support moment: lost time,
unsafe sharing, or a failed restore decision. The MVP must earn its place by
showing that it prevents a material omission that Git folders and notes leave
behind.

## Target user

A self-hoster who manually downloads appliance/configuration exports and wants
an offline recovery/support record without giving a new tool credentials or
running a network-management platform.

## MVP scope

- Import a user-selected export file and explicit context: device label,
  purpose, export method, claimed firmware/version, and recovery-location
  reminder.
- Calculate a local content hash; classify the file as text or opaque/binary.
- Produce a user-reviewed redacted derivative and record the applied rules;
  never claim that a derivative is secret-free.
- Diff two supported text exports; report opaque files as unsupported rather
  than inventing a diff.
- Render deterministic Markdown and JSON receipts with unknown fields and a
  manual restore checklist.
- No device connections, network scanning, credential collection, cloud backup,
  topology discovery, or restore action.

## Shortlist and wedge-first gate

1. **ConfigReceipt — selected.** Self-hoster with manually exported appliance
   files → RANCID/Oxidized, Git folders, Obsidian, Bitwarden notes, and NetBox →
   automated tools require reachable/supported devices while generic folders
   and notes do not make an opaque export's purpose, revision, redaction, and
   recovery context reviewable → offline receipt around a user-selected export
   only → exact self-hosted configuration-backup and router-export searches,
   plus practical Git-versus-receipt content for small labs → the fresh request
   and replies explicitly expose the manual-export/metadata trade-off.
   **Kill:** five target users show their Git/note workflow takes under 30
   minutes per month and leaves no recovery or support ambiguity; or a mature
   tool already produces the same local, no-credential receipt for arbitrary
   manual exports.
2. **UpdateEcho — rejected.** Container operator receiving duplicate update
   alerts → DIUN, WhatUpDocker, Watchtower, and manual image checks → existing
   update tooling already owns image detection and application, while the fresh
   report may be a configuration-specific duplicate rather than an unmet
   category need → notification deduplication overlay → update-notification
   searches and the fresh r/selfhosted report → no evidence that a separate
   layer beats diagnosing DIUN or using an existing updater. **Kill:** crowded
   container-update category and only one configuration report.
3. **AlertRoute — rejected.** Small IT team considering Discord for Icinga
   alerts → Icinga webhooks, email/SMS, Teams, Discord, and Apprise → Apprise
   already documents Discord delivery, templating, retries, attachments, and
   routing knobs → alert-channel policy helper → r/sysadmin monitoring-alert
   searches → no credible 1–3 day wedge beyond configuration advice. **Kill:**
   mature notification transport already solves the requested integration.
4. **LabelBridge — rejected.** Legacy-reporting operator sending PDFs to Zebra
   printers → driver pipelines, Labelary, and browser PDF-to-ZPL converters →
   existing products render and convert ZPL while at least one public converter
   already operates locally in a browser → printer-preflight wrapper → thermal
   label/PDF-to-ZPL searches → the direct job is already well served and the
   source is a single niche implementation report. **Kill:** no differentiated
   workflow beyond an existing converter.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | RANCID | Captures and versions configurations by logging in to supported devices. It wins where device access and supported command models exist. |
| Direct competitor | Oxidized | Mature, extensible automated backup/diff tool. It wins for managed network fleets and should not be displaced. |
| Indirect substitute | Git plus dated export folders, Obsidian, or a Bitwarden note | These are the public thread's suggested workarounds. They are cheap and private, but metadata, redaction, and recovery context are inconsistent, especially for opaque exports. |
| Indirect substitute | NetBox | Handles topology and equipment documentation, but has a broad operational model that the thread describes as daunting for a small lab. |
| Status quo | Save an export wherever convenient and rediscover its device, date, and purpose at recovery time | The cost is tolerable until a recovery or support task requires the missing context, at which point time loss and unsafe sharing become plausible. |

## Wedge

ConfigReceipt must not compete as another collector, inventory system, or
configuration manager. Its smallest credible job begins *after* a person has
manually exported a file: attach explicit recovery context, produce a reviewed
redacted support copy, and state whether comparison is actually possible.

RANCID and Oxidized solve the ongoing, reachable-device backup job well. NetBox
solves broader infrastructure documentation. Git folders solve storage. The
narrow gap is a credential-free, arbitrary-export receipt for people who will
not deploy a polling platform. Its distribution path is specific but modest:
searches for configuration-export backup/metadata and educational small-lab
content comparing an unannotated Git folder with a recovery receipt.

## Kill condition

Reject or narrow ConfigReceipt if five target users can demonstrate that their
existing Git/note workflow takes under 30 minutes per month and leaves no
ambiguity in a recovery or support scenario. Also reject if a mature existing
tool produces the same local-only, arbitrary-file receipt with explicit
redaction review and restore context without device access.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | The recovery/support failure mode can matter, but this run has one fresh public account rather than repeated evidence of a weekly burden. |
| Feasibility | 5/5 | A local CLI for hashing, explicit metadata, reviewed transforms, text diffs, and deterministic reports is a 1–3 day MVP. |
| Demo potential | 4/5 | A generic export folder becoming a dated receipt, redacted support copy, and missing-firmware warning is easy to demonstrate with synthetic fixtures. |
| Distribution | 4/5 | The first-user path is concrete: exact configuration-backup/export searches and focused r/selfhosted content contrasting Git-only storage with a receipt. It is not a built-in viral channel. |
| Competitive wedge / timing | 3/5 | Automated incumbents are strong, but the manual-export, no-credential boundary is distinct and directly reflected in the source thread. It still needs user validation. |
| Total | 19/25 | Clears the 18-point threshold and both creation gates. |

## Decision

**repo-created.** ConfigReceipt scores 19/25, with Distribution at 4/5 and
Competitive wedge / timing at 3/5. A dedicated local project scaffold and a
public-safe snapshot were created. No dedicated GitHub remote was created or
claimed.

## Next build step

Implement the local receipt schema with three synthetic fixtures: a text router
export, an opaque appliance backup, and an export missing firmware/purpose.
Show deterministic receipts, reviewed redaction state, and no-network execution;
then validate the artifact with five self-hosters before expanding into vendor
parsers or storage integrations.

## Source access caveats

Reddit public JSON returned the documented `HTTP 403` theme-beta response. The
read-only tool successfully fell back to public RSS for r/selfhosted and
r/sysadmin; a later r/webdev RSS request returned `HTTP 429` and was not
retried. The selected r/selfhosted direct page was accessible and supplied the
quoted workaround detail. RSS fallback does not provide reliable score/comment
metadata, so this brief makes no engagement, volume, or consensus claim.

`xurl` reported no default OAuth 2 token and the read-only X search probe
returned `401 Unauthorized`; no X signal is used. Direct web extraction of the
selected Reddit page and competitor documentation succeeded. Web search did not
return fresh Reddit fallback results for the broad queries.
