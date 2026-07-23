---
summary: "Document the shared shell/CLI tooling declared in `modules/home-manager/base.nix`, previously only mentioned in passing from other notes."
status: active
tags: [software]
---

## Purpose

Document the shared shell/CLI tooling declared in `modules/home-manager/base.nix`, previously only mentioned in passing from other notes.

## Current State

- `zsh` with Oh My Zsh, completion, and syntax highlighting; one custom alias, `nix-rebuild = "sudo nixos-rebuild switch --flake /etc/nixos --upgrade"`. This alias is stale — `ThornixOS` no longer deploys by rebuilding against `/etc/nixos` at all; it's `comin` GitOps now (see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]). Worth fixing or removing.
- `atuin` (shell history sync/search): `auto_sync = true`, `sync_frequency = "10m"`, `style = "compact"`, `search_mode = "fuzzy"`. No self-hosted sync server is configured anywhere in `ThornixOS`, so this is presumably syncing against the default `atuin.sh` hosted service.
- `intelli-shell`: enabled with Zsh integration (command-snippet/bookmark tool).
- `zoxide`: enabled with Zsh integration (smarter `cd`).
- `fastfetch`: enabled (system-info banner).
- `feh`: enabled (lightweight image viewer — matches the `.fehbg` wallpaper-restore script seen on disk).
- `playerctld`: enabled as a user service (MPRIS media-key daemon).
- GPG: enabled with custom `scdaemonSettings` (`disable-ccid = true`, `pcsc-shared = true`) for smartcard/YubiKey sharing.
- `nix.settings.experimental-features = [ "nix-command" "flakes" ]` and `nixpkgs.config.allowUnfree = true` are also set here.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[04 Software/Yazi|Yazi]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
