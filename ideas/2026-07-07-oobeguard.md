# Day 019 — OOBEGuard

Date: 2026-07-07
Status: repo-created

## One-line pitch

A preflight CLI for Windows imaging admins that catches OEM/OOBE automation traps before a FOG, MDT, or PXE rollout silently skips post-install scripts or driver steps.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1upm9at/til_windows_11_pro_oem_silently_blocks/ | Fresh sysadmin reports spending weeks debugging a zero-touch imaging pipeline for roughly 350 devices across 5 campuses because Windows 11 Pro OEM silently skipped `SetupComplete.cmd` and blocked an online DISM driver-add path; workaround used RunOnce plus `pnputil`. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-a-custom-script-to-windows-setup?view=windows-11 | Microsoft documents that `%WINDIR%\Setup\Scripts\SetupComplete.cmd` is disabled when using OEM product keys except on Enterprise editions and Windows Server, and points to unattend/OOBE alternatives. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-and-remove-drivers-to-an-offline-windows-image?view=windows-11 | Microsoft documents DISM driver servicing for offline images and warns that recursive driver injection can bloat images; this validates that driver staging rules are subtle and deployment-context-dependent. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/pnputil-command-syntax | `pnputil` is included in Windows and supports adding, installing, exporting, enumerating, and scanning drivers, matching the workaround path mentioned in the Reddit post. |
| FOG Project | https://fogproject.org/ | FOG is a free/open-source network computer cloning and management solution with a large forum community, validating a reachable audience for imaging pipeline diagnostics. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows/deployment/deploy-windows-mdt/get-started-with-the-microsoft-deployment-toolkit | MDT is a broad Windows deployment toolkit with task sequences, logging, monitoring, and driver selection profiles, but it is not a small preflight explanation layer for the specific OEM/OOBE traps shown in the Reddit evidence. |

## Source access caveats

- Reddit public JSON returned `HTTP 403 theme-beta`; the bundled Reddit tool used public RSS for the r/sysadmin post list and search result.
- Fetching the full Reddit thread via JSON was blocked, so the Reddit evidence is limited to the public RSS title/snippet/permalink.
- Several configured Reddit feeds/searches returned RSS `HTTP 429`; the run used successful RSS results plus direct web documentation for validation and competitor checks.
- X/Twitter `xurl search` returned `401 Unauthorized`; X was not used as evidence.
- The web-search backend returned empty result sets for targeted Windows deployment queries, so competitor/source validation used direct public documentation/product pages.

## Problem

Small IT teams still run pragmatic Windows imaging stacks: FOG, PXE, MDT-era scripts, offline driver folders, `SetupComplete.cmd`, unattend files, RunOnce registry keys, and manual forum knowledge. The dangerous failure mode is not a loud compile error. It is a deployment step that silently does nothing because the image, license channel, setup phase, or driver command is incompatible with the target device path.

That kind of miss wastes days or weeks, blocks campus/store/lab rollouts, and makes admins choose between buying broader endpoint tooling or shipping a fragile workaround they barely trust.

## Target user

Sysadmins and IT generalists managing Windows 10/11 imaging for schools, labs, clinics, small businesses, or multi-site organizations with FOG/PXE/MDT-style pipelines and mixed OEM hardware.

## MVP scope

- `oobeguard check examples/win11-pro-oem.yml` reads a public-safe YAML deployment plan.
- Inputs: Windows edition/channel, activation/licensing assumptions, imaging tool, post-install hook choices, driver staging method, OOBE/audit mode choices, and sample redacted log flags.
- Rules for the first high-value traps:
  - `SetupComplete.cmd` disabled under OEM product keys except Enterprise/Server.
  - No reboot inside `SetupComplete.cmd`.
  - Offline DISM vs online driver install confusion.
  - Dangerous recursive driver injection bloat.
  - When `pnputil /add-driver ... /install` is the safer post-boot pattern.
  - RunOnce/FirstLogon/unattend alternatives and their tradeoffs.
- Output: Markdown preflight report with blockers, warnings, safer fallback recipes, and links to original documentation.

## Shortlist and wedge-first gate

1. **OOBEGuard** — Windows imaging admins with FOG/PXE/MDT-style stacks → Microsoft docs, forum archaeology, MDT/Intune/Autopilot, SmartDeploy/PDQ, trial-and-error scripts → broad tools automate deployments but do not give a tiny preflight report for OEM/OOBE/script/driver traps before a rollout → local YAML/log-snippet checker focused on Windows setup phase compatibility and fallback recipes → r/sysadmin, FOG forums, MDT/Windows deployment search queries, and pasteable public-safe reports → fresh Reddit post shows weeks lost today on a documented-but-easy-to-miss OEM restriction.
2. **ManualSnap** — web developers making client user manuals → Scribe, Tango, Guidde, Supademo, screenshots plus Word/Photoshop → existing tools already capture step-by-step flows well; user pain is real but crowded and browser-extension-like → could narrow to static admin-panel manuals with exportable editable screenshots → r/webdev and SEO around user manual generation → fresh r/webdev post asks for automating flow screenshots. Held: crowded category and weak wedge against polished incumbents.
3. **AgentWorkflowRealityCheck** — non-technical ops teams trying no-code AI agents for HR onboarding → Zapier, Make, n8n, Gumloop, Lindy, no-code agent builders, consultants → demo agents fail when real integrations/webhooks are required, but the market is crowded and trust-heavy → checklist/simulator that grades whether a workflow is actually no-code before trial signup → selfhosted/no-code communities and comparison SEO → fresh Reddit post reports a wasted Friday on toy demos. Held: crowded AI/no-code category and distribution would blur into generic agent-tool content.
4. **MicroSaaS StackFit** — first-time solo founders choosing between Base44, Lovable, Supabase, Stripe, Vercel, and custom code → YouTube tutorials, boilerplates, founder communities, consultants → advice is abundant but confusing; the status quo is tolerable unless the user is already blocked by a concrete build → budget-aware stack decision report → r/SaaS/r/SideProject search/reply content → fresh selfhosted post shows confusion. Rejected: audience is broad, advice-market wedge is weak, and pain is not specific enough.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Intune / Windows Autopilot | Modern cloud-first endpoint management and provisioning. Strong for organizations already buying into Microsoft 365/Entra/Intune; too heavy for a small FOG/PXE script preflight and not a focused diagnostic report for legacy imaging traps. |
| Direct competitor | MDT / Configuration Manager task sequences | Powerful deployment tooling with logging, driver selection profiles, and task sequence extensibility. The wedge is not replacing MDT; it is checking brittle assumptions before a small team ships a task sequence or post-image script. |
| Direct competitor | SmartDeploy / PDQ deployment products | Commercial imaging, app deployment, and endpoint management products. They solve more of the lifecycle but require product adoption; OOBEGuard would be a small local checker for teams staying with existing tooling. |
| Indirect substitute | FOG Project forums and r/sysadmin threads | Useful human support, but slow and repetitive; the admin must know which setup phase, license channel, and driver method to ask about. |
| Indirect substitute | Microsoft Learn pages and scattered scripts | Authoritative but fragmented. The specific rule that `SetupComplete.cmd` is disabled with OEM product keys is easy to miss until a rollout fails. |
| Status quo | Trial-and-error imaging runs | Admins discover silent skips after devices are imaged, then rebuild scripts under pressure or buy broader management tools. |

## Wedge

OOBEGuard is not another deployment system. It is a narrow preflight and explanation layer for one recurring sysadmin failure mode: “my Windows image worked in the guide, but this setup phase/license/driver path silently does not run on my fleet.” A 1-3 day MVP can win by encoding a small set of documented traps into a local, public-safe report that admins can paste into tickets, forum posts, or rollout checklists before touching production devices.

## Kill condition

Reject or narrow if admins only want full endpoint-management suites, if Microsoft/FOG/MDT tooling already surfaces these exact blockers clearly before deployment, or if the MVP requires collecting private fleet inventory/logs instead of using redacted YAML/log snippets. Also reject any roadmap that starts making licensing circumvention or activation advice; the product must stay on safe compatibility diagnostics.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The status quo can waste weeks and block hundreds of devices; the Reddit evidence is concrete and Microsoft docs validate the trap. |
| Feasibility | 4/5 | A rules-backed CLI with YAML fixtures, redacted log snippets, and Markdown output is buildable quickly without privileged APIs. |
| Demo potential | 4/5 | A failing Win11 Pro OEM fixture can produce an obvious before/after preflight report with links and fallback recipes. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin troubleshooting, FOG forums, MDT/Windows deployment searches, and pasteable reports for manual replies. |
| Competitive wedge / timing | 3/5 | Broad deployment suites and docs exist; the wedge is the narrow, local preflight layer for mixed legacy/OEM imaging stacks. |
| Total | 19/25 | Clears repo threshold and both gates. |

## Decision

Create a dedicated repo: `halaprix/oobeguard`.

Reason: the score clears 18/25, distribution is 4/5, and competitive wedge/timing is 3/5. The weakest dimension is competitive wedge/timing because Microsoft and commercial endpoint-management products already cover adjacent deployment jobs; the MVP must stay sharply focused on setup-phase compatibility checks.

## Next build step

Implement `oobeguard check examples/win11-pro-oem.yml` with a fixture-backed rules engine that prints a Markdown report flagging the OEM `SetupComplete.cmd` blocker, driver-injection risks, and safer RunOnce/unattend/`pnputil` alternatives.
