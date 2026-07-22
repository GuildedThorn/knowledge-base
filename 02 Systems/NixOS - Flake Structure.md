## Purpose

Document what the `ThornixOS` flake defines and how it turns repo structure into buildable NixOS configurations.

## Scope

This reflects the current `flake.nix` at `~/Documents/ThornixOS`, which uses flake-parts + import-tree (see [[02 Systems/NixOS - Repository Layout|Repository Layout]]). The old `current-user.lock`/`current-host.lock` model is gone.

## Inputs

Notable flake inputs include:

- `nixpkgs` on `nixos-unstable`
- `home-manager`
- `flake-parts` and `import-tree` (drive the module auto-loading pattern itself)
- `hyprland` (pinned to a commit), `hyprland-plugins`, and `hyprland-scroll-overview`
- `spicetify-nix`
- `stylix` (fleet theming — currently the `catppuccin-mocha` base16 scheme, set in `modules/users/thorn.nix`)
- `comin` (GitOps deploy agent)
- `sops-nix`, `disko`, `lanzaboote`
- `proxmox-nixos`
- `nixvim`, `yazi`
- `awww` (spanning-wallpaper daemon used by the `wallpaper` Home Manager module)
- `nix-flatpak`
- `guildedthorn-com` — the [[GuildedThorn.com - Overview|GuildedThorn.com]] repo itself, providing the `services.guildedthorn` NixOS module used by the `websites` host

The `astal` and `ags` inputs were dropped along with the unused `programs/ags`/`programs/eww` widget trees.

## Outputs

`flake.nix` itself only declares inputs; `outputs = import-tree ./modules` does the rest. Every `.nix` file under `modules/` is loaded as a flake-parts module and can:

- register a named module fragment under `config.nixos.modules.<name>` (consumed by host files), or
- register a full host directly under `flake.nixosConfigurations.<name>`

There is no dynamic host enumeration or lock file anymore — each `modules/computers/<host>.nix` file explicitly defines its own `flake.nixosConfigurations.<host>` with an explicit module list. All hosts target `x86_64-linux`.

## How a Host File Composes

A typical `modules/computers/<host>.nix` (see actual examples in the repo) lists:

- `config.nixos.modules.thorn-core` (always first — base config bundle)
- desktop/processor/graphics named modules as needed
- service named modules as needed
- `hosts/<host>/hardware-configuration.nix`, `disko.nix`, and `networking.nix` as needed
- `hosts/<host>/secrets.nix` for hosts with sops secrets
- an inline `home-manager.users.thorn = import "${inputs.self}/hosts/<host>/home.nix";` block for hosts with a Home Manager overlay
- an inline anonymous module for host-specific one-off config (bootloader, package list, service tweaks) that doesn't warrant its own named module

## Practical Takeaway

The repo is a multi-host flake where each host is a fully explicit composition of named modules plus host-local data files — there is no implicit host discovery, and no separate deploy-time selection step. Which host builds is just which `modules/computers/*.nix` file you're looking at (or `.#<host>` on the flake). Getting a host running on real hardware is a one-time manual `nixos-rebuild switch --flake github:GuildedThorn/ThornixOS#<host>`; after that [[02 Systems/NixOS - Rebuild and Host Selection|comin]] keeps it in sync with `main`.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
