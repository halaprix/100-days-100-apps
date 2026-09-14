# Day 080 — ReceiptHandoff

Date: 2026-09-14
Status: idea-only

## One-line pitch

A local, accountant-ready handoff builder for tiny businesses that already keep a spreadsheet: turn a month's phone receipts, invoices, and mixed image files into a normalized, reviewable delivery folder without adopting a full accounting system.

## Evidence

| Source | Link | Signal |
|---|---|---|
| r/SideProject public post, 2026-09-14 (RSS fallback) | [After years of fighting with Excel, I finally built our own bookkeeping tool](https://www.reddit.com/r/SideProject/comments/1wfw2pm/after_years_of_fighting_with_excel_i_finally) | A small-business owner described moving receipt photos from phone to laptop, renaming files one by one, sending a transfer link to an accountant, and losing nearly a day to the batch; iPhone HEIC files also caused an accountant access problem.[1] |
| Dext product documentation | [Receipt Bank is now Dext](https://dext.com/uk/receipt-bank/) | Dext extracts receipt data, categorizes costs, connects to accounting software, and targets accountants, bookkeepers, and businesses.[2] |
| Hubdoc product documentation | [Document & Data Capture Software](https://www.hubdoc.com/?lang=en) | Hubdoc captures documents by mobile, email, scan, or upload, extracts fields, and creates transactions in Xero and QuickBooks Online.[3] |
| Moneybird product documentation | [Processing purchase invoices](https://www.moneybird.com/features/purchase-invoices/) | Moneybird supports receipt/invoice upload, email intake, mobile scanning, OCR, and bookkeeping workflows.[4] |

The fresh public report is one concrete incident, not proof of category-wide demand. The incumbent pages establish the substitute bar rather than validate the proposed wedge.

## Problem

A very small business can be too invested in an existing spreadsheet-and-accountant workflow to adopt a full accounting platform, yet still accumulate a painful monthly pile: phone photos, HEIC images, PDFs, emailed invoices, ambiguous filenames, and an accountant who needs a usable, complete set.

The status quo is manual transfer, conversion, renaming, spreadsheet updates, and a large email or file-transfer link. The cited report describes this taking almost a full day and creating an extra accounting cost.[1] That clears the status-quo pain test when it recurs monthly; it does not justify replacing bookkeeping software.

## Target user

A 1–5 person service or trades business that already gives a monthly receipt bundle to an external accountant, tracks totals in a spreadsheet, and does not want to migrate its books merely to make one handoff less error-prone.

## MVP scope

A local desktop app or CLI that processes a selected monthly folder and produces a new delivery folder:

1. accepts PDFs, JPEGs, PNGs, and HEIC images without uploading source documents;
2. converts unsupported image formats to accountant-friendly PDF/JPEG copies while preserving originals and recording file hashes;
3. proposes deterministic filenames from local OCR where confidence is sufficient, otherwise creates a review queue rather than guessing;
4. creates a manifest with original filename, normalized filename, file type, checksum, and review status; and
5. exports a ZIP plus a spreadsheet-friendly CSV for the accountant handoff.

Non-goals: bookkeeping, tax categorization, payment initiation, bank connections, accounting-system sync, tax advice, or replacing Dext, Hubdoc, Moneybird, or an accountant.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Outcome before scoring |
|---|---|---|
| **ReceiptHandoff** | Tiny business owner already using Excel plus an external accountant → Dext/Hubdoc/Moneybird or manual folders → full accounting capture products require an account and workflow change, while folders fail on mixed formats and handoff completeness → local, one-month handoff packet with conversion, manifest, and review queue → accountant-facing “how to send receipts” guides, bookkeeping communities, and search around HEIC/accountant receipt handoffs → a fresh public report shows the exact manual batch and cross-device format failure. | Narrow enough to score, but demand evidence is a single report and distribution is not yet repeatable. |
| Proxmox backup planner | Self-hoster with LXC/VM backups → Proxmox Backup Server, Borg/Restic, and existing scripts → setup advice is fragmented → generated migration plan → self-hosted community guides → a fresh backup-storage question. | Rejected: established backup products already cover the job; no evidence of a distinct, painful planning gap. |
| Performance-marketing matcher | Solo SaaS maker → agencies, affiliates, and cold outreach → upfront marketing cost feels risky → pay-on-performance matchmaker → founder communities → a fresh request for such a service. | Rejected: a two-sided marketplace needs supply and demand; the only clear acquisition path would be spammy outreach. |
| Offline authenticator | Privacy-sensitive phone user → 2FAS, Ente Auth, Aegis, and platform authenticators → cloud sync is unwanted → offline-only vault → privacy communities → a fresh side-project launch. | Rejected: crowded credential category, mature substitutes, and no credible distribution wedge. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | [Dext](https://dext.com/uk/receipt-bank/) | Strong incumbent: extraction, categorization, storage, and accounting-software integration. ReceiptHandoff must not compete on OCR accuracy or bookkeeping automation.[2] |
| Direct competitor | [Hubdoc](https://www.hubdoc.com/?lang=en) | Strong document-capture workflow with data extraction and Xero/QuickBooks transaction creation.[3] |
| Direct competitor | [Moneybird](https://www.moneybird.com/features/purchase-invoices/) | Especially relevant for the cited Dutch user: receipt upload, email, mobile scan/recognize, and bookkeeping are already available.[4] |
| Indirect substitute | Finder folders, Preview/image conversion, spreadsheet, email/transfer link | Cheap and familiar, but completion is not auditable and each batch requires manual conversion, naming, and checking. |
| Status quo | Deliver a raw, mixed-format monthly folder to the accountant | Tolerable for a tiny/simple batch; becomes costly when uploads, formats, and missing-file review cause a late or unusable handoff. |

## Wedge

ReceiptHandoff is not receipt capture software. Its narrow job is a local *end-of-month delivery compiler* for businesses deliberately staying outside a cloud accounting workflow: preserve originals, make usable copies, surface ambiguity, and give both sides the same manifest.

The wedge survives only if people value that low-commitment, accountant-facing handoff more than a broader capture subscription. The practical first-user route is a short, downloadable “accountant handoff folder” example aimed at accountants who already publish client document-submission instructions, followed by validation with three such firms. This is specific but unproven, so it earns Distribution 3/5 rather than a repository-creation score.

## Kill condition

Reject the idea if three accountants say a shared folder plus their existing Dext/Hubdoc/Moneybird intake handles this in under five minutes per month, or if three spreadsheet-first businesses would rather adopt an incumbent than pay for a one-time/monthly handoff tool. Also reject if reliable HEIC conversion and local OCR make the MVP materially harder than a three-day spike without creating differentiated value.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | The reported workflow can consume almost a day and create accountant cost, but it is one fresh public incident rather than repeated validation.[1] |
| Feasibility | 5/5 | Local file processing, image conversion, checksums, manifest generation, and a conservative review queue fit a 1–3 day spike. |
| Demo potential | 4/5 | A messy phone-export folder becoming a clean delivery packet with one review warning is easy to show. |
| Distribution | 3/5 | Accountants and spreadsheet-first microbusinesses are identifiable, but an owned or repeatable channel is not yet proven. |
| Competitive wedge / timing | 3/5 | The wedge is deliberately outside full bookkeeping software, but incumbent capture products are strong and timing is a fresh incident rather than a platform deadline. |
| Total | 18/25 | Clears the numeric threshold but fails the required Distribution gate (minimum 4/5). |

## Decision

**Idea-only.** Do not create a dedicated repository. ReceiptHandoff reaches 18/25 but Distribution is 3/5, below the repository-creation gate. The right next move is to test whether accountants endorse a standardized delivery packet before building another receipt tool.

## Next build step

Create one synthetic mixed-format monthly-receipts fixture and a local prototype that emits a ZIP plus manifest; ask three accountants whether the output would save real review time compared with their existing intake route.

## Source access caveats

Reddit public JSON was blocked. The r/SideProject result above came from the public RSS fallback, so score and comment-count data were unavailable and no consensus is claimed. RSS fallback also returned recent r/SaaS and r/selfhosted entries, but r/webdev and r/sysadmin failed at HTTP 429; later r/Entrepreneur and r/productivity probes also returned HTTP 429. X authentication status showed no usable OAuth 2 token and the read-only search endpoint returned HTTP 401, so no X signal is claimed. Web search produced no usable Reddit fallback results; the competitor claims above rely on directly fetched vendor pages.

## Sources

[1] https://www.reddit.com/r/SideProject/comments/1wfw2pm/after_years_of_fighting_with_excel_i_finally
[2] https://dext.com/uk/receipt-bank
[3] https://www.hubdoc.com/?lang=en
[4] https://www.moneybird.com/features/purchase-invoices
