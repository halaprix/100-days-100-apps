# BayTrace

A local-first CLI that helps Proxmox and homelab builders trace unreliable SATA bays, controllers, cables, and power timing before trusting a new storage setup.

## Problem

Homelab users often build storage from recycled PCs, external drive cages, PCIe SATA cards, and mixed disks. When only some drives appear, formats seem to disappear, or boot hangs at udev, the debugging loop becomes unsafe guesswork: reboot, move cables, read `dmesg`, run `smartctl`, ask Reddit, and hope the next pool import is not destructive.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit | https://www.reddit.com/r/selfhosted/comments/1ur6fo1/pcie_sata_card_with_proxmox/ | Fresh self-hosted user reports 10 HDDs on a PCIe SATA card where random disks are missing and boot sometimes stalls waiting for udev. |
| Reddit | https://www.reddit.com/r/selfhosted/comments/1ur34yw/which_toolsolutions_do_i_need_for_my_project/ | Solo developer launching on a VM asks for one practical tool to understand hardware/backend health instead of stitching multiple observability products. |
| smartmontools | https://github.com/smartmontools/smartmontools | Mature low-level disk health tooling exists, but it does not produce a homelab bay/controller/cabling diagnosis by itself. |
| Hard Disk Sentinel | https://www.hdsentinel.com/hard_disk_sentinel_linux.php | Disk health monitors exist; BayTrace focuses on preflight correlation and redacted support reports for flaky homelab storage wiring. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Hard Disk Sentinel, smartmontools, Proxmox UI storage views | Strong at disk health or inventory; weak at correlating drive bay presence, controller identity, udev timeouts, power sequencing, and cabling evidence into one shareable diagnosis. |
| Indirect substitute | `dmesg`, `lspci`, `lsblk`, `smartctl`, forum checklists, manual cable swaps | Works for experts, but beginners paste partial logs and repeat risky reboots without a stable test plan. |
| Status quo | Reboot, swap cables, move disks, ask Reddit, then import/create storage anyway | Wastes hours and can lead to data-loss-prone decisions if the controller or power path is unstable. |

## Wedge

BayTrace is not another storage monitor. The wedge is a read-only, homelab-specific preflight that maps physical bays to Linux devices across repeated scans, highlights unstable disappearance patterns, summarizes controller/chipset risk, and emits a redacted Markdown report for Proxmox/selfhosted support threads.

## Target user

Self-hosters and small-lab operators building Proxmox, Debian, or Ubuntu storage nodes with consumer PCIe SATA cards, recycled desktops, external drive cages, or mixed HDD/SSD pools.

## MVP

- `baytrace scan` captures `lsblk`, `lspci`, selected `dmesg` storage events, udev settle status, and SMART availability without changing disks.
- `baytrace compare` runs two or more scans and flags bays/devices that appear, disappear, rename, or lose SMART visibility.
- `baytrace report` writes a redacted Markdown/JSON bundle with controller, kernel, drive, cabling, and power-sequencing clues.
- Plain-language checks for common traps: cheap SATA multiplier cards, controller reset spam, udev settle timeouts, missing serials, unstable device names, insufficient power sequencing, and non-HBA RAID modes.

## Non-goals

- Not a ZFS/pool repair tool.
- Not a destructive disk tester or benchmark in the MVP.
- Not a replacement for SMART monitoring.
- Not a hardware compatibility certification database.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
