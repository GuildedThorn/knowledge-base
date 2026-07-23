---
summary: Track unfinished device and host documentation for the main workstation.
status: in-progress
tags: [improvements]
---

## Purpose

Track unfinished device and host documentation for the main workstation.

## Current State

- The `Main PC` note is standardized and linked to the `nixos` host note.
- The host docs already cover AMD graphics, Hyprland, Docker, VR, gaming, and a media CIFS mount.
- Podman/Waydroid/Technitium are no longer part of the config — this host now uses Docker and external DNS (`1.1.1.1`) with static `extraHosts` entries instead of a local resolver.
- Physical layout, recovery process, and peripheral inventory are still missing.

## Tasks

- [ ] Add storage layout beyond the primary drive note
- [ ] Add monitor and peripheral inventory
- [ ] Add container workflow notes for Docker
- [ ] Add media share mount expectations and failure/recovery notes for `/mnt/media`
- [ ] Add notes for DisplayLink usage and any dock-specific quirks
- [ ] Add notes for gaming and VR-specific hardware dependencies
- [ ] Add backup or recovery workflow for the workstation

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[03 Devices/Main PC|Main PC]]
- [[02 Systems/NixOS - Host nixos|NixOS - Host nixos]]
