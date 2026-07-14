## Purpose

Track unfinished work around host config, secrets, deployment flow, and documentation for `ThornixOS`.

## Current State

- The vault now has host notes for all 10 current hosts: `nixos`, `scout`, `mac`, `websites`, `firewall`, `mitm`, `proxmox-mitm`, `proxmox-guest`, `vmware-test`, and `vmware-guest`.
- The old `bin/rebuild-deploy` / `current-user.lock` / `current-host.lock` / Makefile workflow is gone — deployment is now GitOps via `comin` (see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]), so those tasks are resolved rather than open.
- `sops-nix` is fully wired in and live (not just planned) — but only `nixos` and `websites` are onboarded so far (see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]).
- Documentation is now current on architecture; day-two operational procedures are still thin.

## Tasks

- [ ] Onboard `mitm` (and/or its `proxmox-mitm` variant) to sops-nix so the SearXNG secret key can be wired up for real, since SearXNG is currently disabled on both partly because of this
- [ ] Set the real LAN IP for the `mac` host — it's still a `TODO` placeholder in `modules/computers/mac.nix`
- [ ] Decide whether `mitm` or `proxmox-mitm` is the one meant to actually run in production, since both currently have the same reverse-proxy config staged but disabled/partial
- [ ] Add host-specific operational notes for `mitm`/`proxmox-mitm`, especially NGINX, SearXNG, and (on `proxmox-mitm`) Grafana bring-up
- [ ] Add host-specific operational notes for `nixos`, especially Docker, local DNS, VR, and CIFS media mount behavior
- [ ] Add host-specific operational notes for `scout`, especially power, thermals, secure boot (`lanzaboote`), and travel usage
- [ ] Create a dedicated note for Home Manager UX customizations (`ags`, `eww`, `matcha`, `desktop-rice`) if they keep growing
- [ ] Decide whether NixVim should standardize on `nixfmt`, `nixpkgs-fmt`, or `alejandra`
- [ ] Fix the `nix-rebuild` shell alias in `modules/home-manager/base.nix` — it still runs `sudo nixos-rebuild switch --flake /etc/nixos --upgrade`, a leftover from the pre-`comin` deploy model (see [[04 Software/Shell Environment|Shell Environment]])
- [ ] Clean up the two stale pre-rename trusted-project paths in `~/.codex/config.toml` (`~/Downloads/nix-config`, `~/Downloads/GuildedThorn.com-main`) — see [[04 Software/AI Coding Tools|AI Coding Tools]]

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|NixOS - Secrets Strategy]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
