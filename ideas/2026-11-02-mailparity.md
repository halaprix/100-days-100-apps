# Day 097 — MailParity

Date: 2026-11-02
Status: idea-only

## One-line pitch

An offline CLI that compares two independently produced mail-export trees and flags message or attachment discrepancies before a PST-to-Thunderbird migration is accepted.

## Research brief

- **Decision:** retain a narrowly scoped validation bet, not build another PST converter.
- **Target customer:** small IT teams retiring Outlook archives into Thunderbird Local Folders; initially an operator already able to produce two exports.
- **Geography:** English-language Windows/Linux mail-migration workflows, not a jurisdiction-specific compliance product.
- **Category / substitutes:** Outbird validation, Aid4Mail conversion/logs, readpst, a short MIME/hash script and manual mailbox sampling.
- **Time horizon:** a one-to-three-day comparison prototype only after the validation gate below.
- **Must-answer question:** does reusable cross-export comparison catch meaningful exceptions that existing validation plus a prepared script misses or makes expensive to triage?
- **Evidence bar:** primary product documentation plus complete community context; require real operator validation before treating this as demonstrated demand. No defensible market-size estimate or willingness-to-pay evidence yet.
- **Creative constraint:** “Nothing new except glue” — compare existing outputs; do not implement a PST parser or a migration engine.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public builder report, 2026-11-02; discovered via Reddit RSS fallback, full post retrieved | [Portable PST-to-mbox/Thunderbird converter](https://www.reddit.com/r/sysadmin/comments/1xlqv2h/portable_scriptable_pst_mboxthunderbird_converter/) | Author reports recurring archive-access tickets and a real test comparing 293 messages across 22 folders with readpst, including attachment hashes. Reports four attached mails lost by a libpff-based route. These are author claims, not independently reproduced results. Strong counterevidence: the author already built a converter and performed detailed validation. No comments were visible when retrieved. |
| Original substitute documentation, retrieved this run | [Outbird documentation](https://github.com/namshubs/hypersuite/blob/main/docs/outbird.md) and [CLI](https://github.com/namshubs/hypersuite/blob/main/docs/command-line.md) | Already reads PST directly, exports a standalone mbox tree, validates folders/message counts, writes a conversion report and backs up a profile before installation. A folder-count wrapper is not a wedge. Documentation does not establish the absence of further checks in the implementation. |
| Historical public user report, 2021; full post and visible replies retrieved | [Imported mail searchable but attachments inaccessible](https://www.reddit.com/r/Thunderbird/comments/oa475r/importing_mbox_file_in_thunderbird_does_not/) | Author could extract attachments separately with readpst but could not access them after an mbox import. A later commenter reports success loading at least one attachment by a different import path. Supports distinguishing extracted payload from client usability, not a proven converter defect or fresh market trend. |
| Original utility documentation | [Debian readpst manual](https://manpages.debian.org/testing/pst-utils/readpst.1.en.html) | Existing free extraction supports recursive mbox, separate messages with attachments, and separate attachment files. `-S`, `-M` and `-e` produce different layouts; output selection and mbox quoting matter. Establishes a strong native baseline. |
| Original commercial product documentation | [Aid4Mail Converter](https://www.aid4mail.com/editions/aid4mail-converter) | Already advertises direct PST reading without Outlook, mbox/EML output, detailed audit/per-message logs, metadata retention, MIH/MIH+ IDs and an included viewer. These are vendor claims, not our tested results; existing professional tooling materially weakens the opportunity. |

**Evidence confidence:** medium for the existence of archive-migration and validation work; low for an unmet standalone-product need. There is one fresh, commercially interested builder report and an old user report, not several independent fresh buyers. Existing behavior includes both building a working tool and writing comparison checks. Do not turn either into proof of demand for this app.

## Shortlist: competitor and wedge-first gate before scoring

All three candidates are software bets. Checks below preceded the winner's scoring; rejected candidates receive no numeric score.

### 1. MailParity — narrowed and retained

**Wedge-first line:** IT operator retiring a PST archive into Thunderbird Local Folders → Outbird's built-in validation, Aid4Mail logs/viewer, readpst plus a prepared MIME/hash script → folder/count equality alone cannot establish attachment payload agreement, while repeatable cross-export triage may require custom scripting; the actual incremental burden remains unmeasured → an offline, converter-neutral discrepancy list over two supplied export trees, with ambiguous matches and unsupported content explicit → Thunderbird migration-help search content and an openly reusable fixture/comparison recipe, with community participation only where permitted → a fresh portable converter makes a new two-route comparison workflow timely, but there is no verified external deadline.

- **Direct / near-direct competitors:** Outbird's built-in checks and the author's already-completed cross-parser test; Aid4Mail integrity features, message IDs, logs and viewer.
- **Indirect substitutes:** readpst plus Python's MIME/mailbox tooling; a folder-mapping worksheet; manual attachment sampling.
- **Status quo:** keep original PSTs, use existing reports, sample messages and investigate discrepancies manually. Extra acquisition may outweigh any saved triage time.
- **Gate result:** reject a new PST converter or generic migration report. Retain only the independent-output comparison hypothesis. Cross-export comparison is not a proven source-completeness check.
- **Kill condition:** a short script plus a prepared worksheet provides equivalent exception triage, existing tools already supply the required comparison, or operators do not repeatedly need a second export.

### 2. CohortFit — rejected before scoring

**Wedge-first line:** solo Android study-app publisher evaluating a closed beta → paid acquaintances, an intake form and Lyssna screeners → the fresh author reports testers misunderstanding the intended study workflow, but has not shown that screening software rather than clearer onboarding is missing → candidate was a cohort-tagged feedback intake separating intended-use fit from Play testing participation → a specific study-app beta-onboarding guide, not generic startup promotion → a fresh beta retrospective exposes the mismatch, not a new platform requirement.

- **Signal:** [Paid Beta Testers Really Surprised Me](https://www.reddit.com/r/Entrepreneur/comments/1xlesbo/paid_beta_testers_really_surprised_me/), 2026-11-01; full post and visible comments retrieved. Author clarifies there were about 30 testers, mostly organic; only a few received $20. Do not repeat the commenter's assumption that all twelve were paid.
- **Direct competitor:** [Lyssna screeners](https://help.lyssna.com/en/articles/9189892-using-screeners-to-qualify-participants) already qualify self-recruited participants, support filtering and include answers in CSV exports; own-audience screening is documented as free.
- **Indirect substitute / status quo:** an intake form and separate cohort column, plus an improved tutorial. The post does not demonstrate costly recurring analysis work.
- **Wedge and kill:** native screening plus a simple form already covers the proposed wedge. Reject; neither unmet tooling need nor a repeatable channel advantage is demonstrated. No tester marketplace, policy-evasion promise or claimed Play approval guarantee.

### 3. ConsentRoute — rejected before scoring

**Wedge-first line:** small MSP reviewing a client's Claude-to-M365 connector rollout → Entra consent settings, Graph exports and an implementation checklist → fragmented decisions may burden handoff, but missing native controls have not been demonstrated → candidate was a passive consent-review worksheet generated from supplied exports, not a security scanner → a connector-specific MSP deployment guide and implementation partners, with no verified partner access → a fresh implementer's rollout account, not independently confirmed broad demand.

- **Signal:** [Clients asking for Claude?](https://www.reddit.com/r/sysadmin/comments/1xljvhp/clients_asking_for_claude_a_few_things_i_learned/), 2026-11-02; full post and visible comments retrieved. It is an implementer exploring demand for services, not a buyer requesting an app. Its connector scope and CSP/licensing assertions were not independently verified here.
- **Direct functional substitute:** [Entra user-consent configuration](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent) already documents portal, Graph and PowerShell paths and the admin-consent workflow. The native consent-review workflow competes with the proposed app even though it is not a separate startup.
- **Indirect substitute / status quo:** current permissions export plus an MSP review checklist and a SharePoint permissions assessment.
- **Wedge and kill:** no specific workflow gap beyond existing administrative tooling; reject this generic security-review wrapper. Native documentation also says changing user-consent settings affects future consent, not existing grants. Do not imply disabling consent revokes prior access or proves all personal-account connections blocked.

## Problem

A converted archive can have plausible folder/message counts without every expected attachment being usable. Conversely, an attachment may exist in a standalone export while Thunderbird does not display it through a particular import path. Operators need these failure classes kept separate.

The fresh author already solved substantial parts of this job: safe conversion, folder/count validation and a cross-parser comparison on a test archive. The remaining hypothesis is that other operators need reusable discrepancy triage over their own independently generated exports. We have not established that they do.

**Status-quo pain test:** missing archive content can cause business data loss or block acceptance of a migration. That potential consequence clears the seriousness test; the research does **not** quantify weekly labor, show a current customer losing money, or prove that two-export review is necessary on every migration. Keeping the PST and using existing tools is a legitimate fallback.

## Target user

A small-team IT administrator who must retain access to an old mail archive after Outlook retirement, already uses Thunderbird Local Folders, and can legally obtain two export routes. Not every Thunderbird user, an eDiscovery investigator, or a user simply seeking a free converter.

Outbird's current source-available license permits internal business use but restricts offering it commercially to others. Do not assume an MSP can bundle or run a paid conversion service using it. A comparator should accept operator-supplied exports without redistributing or silently invoking that tool.

## MVP scope

A proposed local Python CLI, not implemented in this research run:

1. Accept two supplied, explicitly mapped mbox/EML trees and record tool/version/options supplied by the operator. No mailbox login, network call, PST mutation or live Thunderbird-profile write.
2. Index folders, message multiplicities and MIME-part inventories. Preserve duplicate and missing Message-ID cases; never deduplicate solely on Message-ID or subject.
3. Compare decoded attachment payload hashes and clearly scoped message/header fields. Separate exact payload equality, normalized metadata agreement, missing candidates, ambiguous matches and parse errors. Do not equate whole-message byte inequality with lost content.
4. Preserve nested `message/rfc822`, inline parts, encoding differences and mbox-quoting uncertainty. Treat encrypted/signed content as unsupported or opaque unless a separately validated comparison exists; do not claim signature verification.
5. Produce local JSON and an escaped HTML exception report with opaque local record references by default. Do not upload mail, include subject/address/body data in public fixtures, or call hashes anonymization.
6. Include explicit scope and error counts. “Two exports agree” is not “the PST is complete”: shared parser bugs, skipped items or identical acquisition filters can affect both routes. Rendering and real Thunderbird search/attachment access need a separate operator check.

**Non-goals:** converter replacement; repair, deletion or automatic acceptance; contacts/calendar migration; legal admissibility; recovery of missing PST content; proof that every source item or signed/encrypted attachment survived. A full PST fidelity engine is not a one-to-three-day MVP.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | Outbird validation and `conversion-report.json` | Already supplies folder/count validation, safe standalone export and guarded profile migration. The author already performed independent message/attachment comparison. Do not sell these as missing features. |
| Near-direct commercial competitor | Aid4Mail Converter | Existing direct PST access, exports, logs, MIH/MIH+ IDs and viewer. Lack of a confirmed cross-export comparator on the retrieved page is not proof it cannot perform the job. Test the actual workflow before claiming differentiation. |
| Indirect substitute | readpst plus a prepared MIME/hash script | Strong free baseline; explicit output modes already provide messages and attachment payloads. A second parser is an additional acquisition step, not a shortcut supplied by the proposed comparator. |
| Indirect substitute | ImportExportTools NG / direct Local Folders workflow and manual sampling | Historical replies suggest an alternate import path can change attachment visibility. The comparator cannot diagnose a client problem from export bytes alone. |
| Status quo | Retain PST, use converter reports and manually open representative attachments | May already be adequate. No evidence warrants forcing dual exports or authorizing source deletion. |

## Wedge

A possible advantage is a reusable, converter-neutral exception workflow rather than another converter, count report or checksum manifest. It must save triage effort across independent export routes, handle ambiguous identities honestly, and preserve the distinction between payload agreement and client usability.

This is a **hypothesis**, not a validated gap. The strongest fresh source already did detailed comparison, and a short script might be the better deliverable. Prefer a fixture recipe or an existing-tool improvement if that meets the need.

## Kill condition

Reject the standalone app if any of the following holds:

- Existing Outbird/Aid4Mail workflows or a short MIME/hash script with a prepared folder map provide equivalent triage at equal or lower total effort, including obtaining the second export.
- Three relevant operators cannot supply recurring acceptance-review examples or do not want to produce independent exports.
- A representative fixture set cannot distinguish missing payloads from duplicate IDs, legitimate MIME normalization, nested messages, unsupported encryption or parser failures without excessive false positives.
- The only useful result requires unrestricted PST parsing, cloud access, private mail upload, client automation or commercial use of a substitute outside its license.

## Scoring

Scores assigned only after narrowing and the competitor gate above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Archive content loss or blocked acceptance matters; frequency and incremental review burden are still unmeasured. |
| Feasibility | 4/5 | A bounded offline two-export comparator is plausible in one to three days. Full PST completeness and all MIME fidelity are explicitly outside scope. |
| Demo potential | 4/5 | A controlled fixture with unchanged message counts but one altered attachment can demonstrate the proposed exception view, not prove real-world converter behavior. |
| Distribution | 3/5 | Specific Thunderbird/migration communities and search queries exist. No validated repeatable acquisition path, maintainer endorsement or MSP partner access. |
| Competitive wedge / timing | 2/5 | Fresh converter activity is useful timing, but built-in checks, professional products and the author's existing comparison are substantial counterevidence. |
| Total | 17/25 | Below the 18/25 threshold; both dimension gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** MailParity is the best retained hypothesis from this shortlist, not a build recommendation. Distribution is 3/5 versus the required 4/5; competitive wedge/timing is the weakest dimension at 2/5 versus the required 3/5. Do not inflate scores to create another scaffold.

The evidence supports checking archive conversion rather than trusting counts. It does not yet support a standalone paid product, market size, or a claim that current converters fail on a representative corpus.

## Next build step

One validation-sized commit, only when this bet is taken forward: add a public-safe, handcrafted mbox/EML fixture recipe and a prepared short-script/worksheet baseline for unchanged-count attachment loss, duplicate/missing Message-ID, nested messages, quoting and an import-visibility case. Mark deliberately altered fixtures as synthetic; they are not measured converter defects. Time the complete comparison workflow, including second-export acquisition, with three relevant operators before implementing an app. No outreach or external participation was performed this run.

Follow-up is tracked in Beads, not as a Markdown task list.

## Source access caveats

- Canonical `reddit-readonly` probes for r/sysadmin and r/Entrepreneur hit public-JSON HTTP 403 and successfully used public RSS. RSS scores/comment counts are unavailable; zero placeholders are not engagement measurements.
- Probes for r/selfhosted, r/webdev and r/androidapps ended in HTTP 429; no tight retries. HTML extraction subsequently recovered r/selfhosted and r/webdev new-post listings. No recovered r/androidapps feed is claimed.
- Full selected Reddit posts and visible comments were retrieved through web extraction; collapsed replies were not exhaustively fetched. Reddit-constrained web search supplied the historical Thunderbird thread, subsequently read in full with visible replies.
- `xurl whoami` succeeded, but the configured read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured; no interactive login was attempted. Web search constrained to X returned only vendor conversion promotions, not independent customer validation, so those results are excluded from the winner's evidence.
- A general search for fresh spreadsheet pain and a cross-export comparison query returned no results; this is not evidence that the problems or competitors do not exist. Vendor docs and the Debian manual were fetched directly. The first readpst manual host failed extraction; the Debian manual provided a working alternative.
- A recovered webdev post used an “as of 3 November 2026” claim while this run is dated November 2. It was not used as verified regulatory timing evidence or included in the shortlist.
- No private mailbox, customer archive or paid API was accessed. All product behavior above is documentation or attributed public reporting, not an executed conversion benchmark.
