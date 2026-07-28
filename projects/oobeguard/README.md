# OOBEGuard

A preflight CLI for Windows imaging admins that catches OEM/OOBE automation traps before a FOG, MDT, or PXE rollout silently skips post-install scripts or driver steps.

## Problem

Small IT teams still run pragmatic Windows imaging stacks: FOG, PXE, MDT-era scripts, offline driver folders, `SetupComplete.cmd`, unattend files, RunOnce registry keys, and manual forum knowledge. The dangerous failure mode is not a loud error. It is a deployment step that silently does nothing because the image, license channel, setup phase, or driver command is incompatible with the target device path.

OOBEGuard starts as a local, public-safe checker for redacted deployment plans and log snippets. It does not touch production devices.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1upm9at/til_windows_11_pro_oem_silently_blocks/ | Fresh sysadmin reports weeks lost debugging a zero-touch Windows 11 Pro OEM imaging pipeline across hundreds of devices because `SetupComplete.cmd` and an online DISM driver path did not behave as expected. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/add-a-custom-script-to-windows-setup?view=windows-11 | Microsoft documents that `SetupComplete.cmd` is disabled with OEM product keys except Enterprise editions and Windows Server. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/pnputil-command-syntax | `pnputil` is built into Windows and supports adding, installing, enumerating, and scanning driver packages. |
| FOG Project | https://fogproject.org/ | FOG validates a reachable community around open-source computer cloning and management. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Intune / Windows Autopilot | Strong for cloud-first endpoint management, but heavy for teams keeping a FOG/PXE/MDT-style imaging stack. |
| Direct competitor | MDT / Configuration Manager task sequences | Powerful deployment tooling; OOBEGuard is a small preflight explanation layer, not a replacement. |
| Direct competitor | SmartDeploy / PDQ deployment products | Commercial lifecycle tools. OOBEGuard focuses on local compatibility checks for existing scripts and docs. |
| Indirect substitute | FOG forums and r/sysadmin threads | Useful but slow; admins must already know what setup-phase/licensing trap to ask about. |
| Indirect substitute | Microsoft Learn pages and scattered scripts | Authoritative but fragmented; important rules are easy to miss until a rollout fails. |
| Status quo | Trial-and-error imaging runs | Silent skips are discovered only after devices are imaged. |

## Wedge

OOBEGuard is deliberately narrow: turn a redacted Windows imaging plan into a Markdown report that flags documented OEM/OOBE/script/driver traps and suggests safer fallback recipes. It wins if it prevents one bad rollout or gives an admin a clear public-safe report to paste into a forum/ticket before reimaging devices.

## Target user

Sysadmins and IT generalists managing Windows 10/11 imaging for schools, labs, clinics, small businesses, or multi-site organizations with FOG/PXE/MDT-style pipelines and mixed OEM hardware.

## MVP

- `oobeguard check examples/win11-pro-oem.yml` reads a fixture deployment plan.
- Detect the first high-value blockers and warnings:
  - `SetupComplete.cmd` disabled under OEM product keys except Enterprise/Server.
  - No reboot inside `SetupComplete.cmd`.
  - Offline DISM vs online driver install confusion.
  - Risky recursive driver injection bloat.
  - When `pnputil /add-driver ... /install` is a safer post-boot pattern.
- Print a Markdown report with severity, explanation, source links, and fallback recipes.

## Non-goals

- Not a full endpoint-management suite.
- Not a device inventory scanner.
- Not a licensing, activation, or circumvention tool.
- Not collecting private fleet data or production logs.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
