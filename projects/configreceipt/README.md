# ConfigReceipt

A local-first receipt generator for manually exported appliance configuration
files: capture what was exported, redact the shareable copy, compare revisions,
and produce a restore checklist without connecting to the appliance.

## Problem

Small self-hosters often export a router, switch, NAS, or application
configuration manually and put the file in a generic folder. The public signal
for this bet asks for export date and purpose metadata, calls a Bitwarden note
clunky, and describes NetBox as daunting for a small lab. A personal Git
repository can retain history, but it does not make a binary or vendor-specific
export safe to share or explain why it exists.

## Target user

A self-hoster with manually downloaded appliance/configuration exports who wants
a credible, offline recovery record without giving the tool device credentials
or running a network-management platform.

## MVP

- Import a user-selected export file and an explicit device/purpose form.
- Store a content hash, acquisition timestamp, device label, firmware/version
  note, and recovery-location reminder in a local manifest.
- Create a redacted copy using reviewable user-confirmed rules; preserve the
  original only at its chosen local path.
- Compare two text exports, distinguish an opaque/binary file, and render a
  Markdown receipt with a restore checklist and `unknown` fields.
- Never connect to devices, discover a network, retain credentials, or claim an
  exported file is a valid restore point.

## Non-goals

- Not a RANCID/Oxidized replacement or a device polling service.
- Not a NetBox/DCIM/topology manager.
- Not a secrets vault, credential scanner, cloud backup service, or automatic
  restore tool.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit direct page | https://www.reddit.com/r/selfhosted/comments/1w8g2ur/solution_suggestions_for_config_backup_and/ | A fresh self-hoster says router exports are dumped in a config folder and asks for export date, purpose metadata, and a paperless-style system. Comments suggest Git plus dated exports, Obsidian, or NetBox, while calling NetBox daunting for a small lab. |
| RANCID | https://shrubbery.net/rancid/ | RANCID logs into network devices, collects and normalizes output, emails diffs, and commits history to version control; it is a strong substitute for reachable, supported network gear. |
| Oxidized | https://github.com/ytti/oxidized | Oxidized is a RANCID replacement for network-device configuration backup with scheduled retrieval, version/diff APIs, and support for many operating-system types. |
| NetBox | https://netbox.readthedocs.io/ | NetBox is a full network source of truth covering devices, cabling, IPAM, and extensions; it is the viable topology substitute but deliberately much broader than a manual-export receipt. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | RANCID | Captures and versions configurations by logging in to supported devices. It wins where device access and supported command models exist. |
| Direct competitor | Oxidized | Mature, extensible automated backup/diff tool. It wins for managed network fleets and should not be displaced. |
| Indirect substitute | Git plus dated export folders, Obsidian, or a Bitwarden note | Cheap, private, and recommended in the source thread, but metadata/redaction/recovery context are inconsistent and binary exports do not diff cleanly. |
| Indirect substitute | NetBox | Handles topology and equipment documentation, but has a broad operational model that the source thread describes as daunting for a small lab. |
| Status quo | Save an export wherever convenient and rediscover its device, date, and purpose at recovery time | A tolerable one-off habit becomes expensive during a restore or when an export must be safely shared for support. |

## Wedge

ConfigReceipt is not another configuration collector. Its narrow job begins
*after* a person manually exports a file: create an offline, redacted,
reviewable receipt around a file that RANCID/Oxidized cannot retrieve and a
full NetBox deployment does not justify. The first channel is concrete:
self-hosted configuration-backup searches and small-lab documentation content
that compares Git-only history with an export receipt.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. No remote is
configured.
