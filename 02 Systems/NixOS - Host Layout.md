## Purpose

Track how host-specific configuration is split across shared modules, per-host data, and one composition file per host.

## Layout Pattern

1. `modules/core/thorn-core.nix` (via `config.nixos.modules.thorn-core`) provides the base system layer every host imports first.
2. `modules/computers/<host>.nix` is the single composition file for that host — it lists which named modules (desktop, graphics, processor, service) the host wants, plus its `hosts/<host>/` data files, plus any host-specific inline config, and registers the result as `flake.nixosConfigurations.<host>`.
3. `hosts/<host>/hardware-configuration.nix` and, where used, `disko.nix` describe the machine's hardware/disk layout.
4. `hosts/<host>/networking.nix` isolates network, DNS, and firewall settings per host.
5. `hosts/<host>/home.nix` provides that host's Home Manager overlay, where a host has one.
6. `hosts/<host>/secrets.nix` + `secrets.yaml` provide that host's sops secrets, where a host has any.

This is a flatter version of the old `nixos/users/<user>/hosts/<host>/` nesting — there's no per-user layer anymore; hosts compose directly from `modules/computers/<host>.nix`.

## Current Host Trees

`nixos`, `scout`, `mac`, `websites`, `soc`, `firewall`, `mitm`, `proxmox-guest`, `vmware-guest`, `vmware-test` — see [[02 Systems/NixOS - Hosts Overview|Hosts Overview]] for what each one is. (`proxmox-mitm` was removed from the repo.)

## Why This Split Works

- Every host's full composition is readable from a single `modules/computers/<host>.nix` file rather than scattered across a per-user tree.
- Networking, disk layout, secrets, and Home Manager overlays stay isolated per machine as flat sibling files under `hosts/<host>/`.
- Desktop, graphics, processor, and service modules are reusable named imports rather than copy-pasted blocks.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Hosts Overview|Hosts Overview]]
