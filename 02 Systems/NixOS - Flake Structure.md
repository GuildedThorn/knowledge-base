## Purpose

Document what the active flake defines and how it turns repo structure into buildable NixOS configurations.

## Inputs

The flake currently pulls in:

- `nixpkgs` on `nixos-unstable`
- `home-manager`
- `stylix`
- `hyprland` pinned to `v0.54.3`
- `hyprland-plugins`
- `spicetify-nix`
- `astal` and `ags`
- `comin`
- `proxmox-nixos`
- `nixvim`

## Outputs

The flake generates `nixosConfigurations` dynamically.

- the system target is `x86_64-linux`
- the username comes from `current-user.lock`; evaluation throws if it is missing
- the active host comes from `current-host.lock` when present
- if no host lock exists, the flake enumerates all host directories for that user

## Shared Modules Included for Every Host

Each generated host imports:

- the shared base `./configuration.nix`
- the Home Manager NixOS module
- the Stylix NixOS module
- the Hyprland NixOS module
- the Proxmox VE NixOS module
- the `comin` NixOS module

## Special Arguments

The flake passes these into modules as `specialArgs`:

- `inputs`
- `system`
- `username`
- `host`
- selected upstream inputs such as `hyprland`, `comin`, `spicetify-nix`, `proxmox-nixos`, and `nixvim`

## Practical Takeaway

The repo is not a flat single-host flake. It is a multi-host flake that selects the active `thorn` host through small lock files and then composes shared, user, and host layers underneath the shared base system.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
