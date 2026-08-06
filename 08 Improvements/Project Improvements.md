---
summary: Track unfinished work across applications and websites documented in the vault.
status: in-progress
tags: [improvements]
---

## Purpose

Track unfinished work across applications and websites documented in the vault.

## Current State

- `GuildedThorn.com` moved from `~/Downloads/GuildedThorn.com-main` to `~/Documents/GuildedThorn.com`, upgraded to .NET 10, and grew substantially: WebAuthn/passkey auth, S3-backed gallery/radio storage, a knowledge-base sync engine (this vault is mirrored into the live site), Web Push, donations, contact, and a fully-built-out radio feature. All five project notes were rewritten to match.
- `SkyDestroyer`, `Tribes-Website`, `ThornBot`, `CI4k`, and `surround-panner` now have project notes under `07 Projects`.
- `ThornixOS` (the NixOS config repo) moved to a flake-parts/import-tree "dendritic" layout with `comin` GitOps deployment and live sops-nix secrets — documented under `02 Systems`.

## Tasks

- [x] Create `04 Software/VS Code.md` or remove the placeholder link from `Software Map` — resolved: editor is neovim ([[04 Software/NixVim|NixVim]]), VS Code not in use, placeholder removed
- [x] Create `04 Software/Syncthing.md` or remove the placeholder link from `Software Map` — resolved: Syncthing is not in use, placeholder removed
- [x] Set the real network identity for the `mac` NixOS host — resolved: Mac is deployed as the OPT1 Proxmox hypervisor; see [[05 Network/Host & IP Inventory|Host & IP Inventory]]
- [ ] Decide whether `Tribes-Website` stays a generic starter template or gets built out with the staged `wwwroot/tribes-assets` into an actual Tribes community site
- [ ] Track `SkyDestroyer`'s remaining rig-test queue (Hunter/CnH/vehicle sync on non-Avalon maps, multi-client sync) and its still-unimplemented plugin API
- [ ] Confirm whether `surround-panner` has had its first real 7.1-speaker listening session yet (README marks this as the explicit next step, not yet done as of the last read)
- [ ] Record which projects are actually deployed versus just local/in-progress across the full project list (currently: GuildedThorn.com and SkyDestroyer are live/active; ThornBot and CI4k are personal-use tools; Tribes-Website and surround-panner are early-stage)

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/Projects Map|Projects Map]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[08 Improvements/GuildedThorn.com Follow-Up|GuildedThorn.com Follow-Up]]
