## Purpose

Track cleanup work inside the knowledge base itself so maps and notes do not drift into placeholder soup.

## Current State

- `Projects Map` now exists and covers GuildedThorn.com, SkyDestroyer, Tribes-Website, ThornBot, CI4k, and surround-panner.
- `02 Systems/NixOS - *` notes were fully rewritten to match the current `ThornixOS` repo (flake-parts/import-tree, `comin` GitOps, sops-nix live, 10 hosts) — the old `nix-config`/Makefile/lock-file description was replaced, not patched.
- `Devices Map` was missing a link to `HP Mini PC.md`, which already existed as a note — fixed.
- Several previously-tracked dead links have since been resolved by real notes landing (`Firefox`, `GhostTTY`, `DNS`, `VLANs`, `Routing`, `SSH Access`, `Remote Recovery`, `Docks and Displays`) — removed from the dead-link list below.
- `07 Projects/GuildedThorn.com/GuildedThorn.com - Backend.md` had a block of unrelated, garbled pasted text partway through the file — removed during the rewrite.

## Tasks

- [ ] Decide whether map notes should prefer bare wiki-links like `[[ThinkPad T15]]` or explicit paths like `[[03 Devices/ThinkPad T15]]`, then standardize (both styles are still mixed across maps)
- [ ] Review stub notes and either expand or archive them

## Dead Links Still Open

- `03 Devices/Homelab Laptop`
- `03 Devices/Keyboard Firmware`
- `04 Software/VS Code`
- `04 Software/Syncthing`
- `05 Network/WireGuard`
- `05 Network/Tailscale`

## Other Open Question

- `05 Network/VLANs.md` referenced a NixOS host note that was never created and doesn't correspond to any host in the current `ThornixOS` repo (its `systemd-networkd` VLANs and `vmbr0`/`vmbr1` bridges point at a Proxmox hypervisor box, not one of the 10 NixOS guest/host configs) — removed the dead link rather than guess at a note. Worth confirming whether this is the bare-metal `proxmox` host itself ([[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]) and documenting it for real.

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/Devices Map|Devices Map]]
- [[01 Maps/Software Map|Software Map]]
- [[01 Maps/Network Map|Network Map]]
- [[01 Maps/Projects Map|Projects Map]]
