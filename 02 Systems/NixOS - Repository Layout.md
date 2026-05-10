## Purpose

Document how `/run/media/thorn/NIX_CONFIG/nix-config` is structured so it is easier to find shared modules, per-user config, and per-host overrides.

## Scope

This note reflects the repo rooted at `/run/media/thorn/NIX_CONFIG/nix-config`, with the active NixOS flake living under `nixos/`.

## Layout

- `Makefile` manages import, drift checks, backup, revert, and interactive or forced install into `/etc/nixos`.
- `bin/rebuild-deploy` writes `current-user.lock` and `current-host.lock` into `/etc/nixos`, then runs `sudo nixos-rebuild switch --flake /etc/nixos --upgrade`.
- `nixos/flake.nix` defines flake inputs and generates `nixosConfigurations` from discovered hosts.
- `nixos/configuration.nix` is the shared base system layer.
- `nixos/desktop` contains desktop environment modules such as `hyprland`, `gnome-x11`, and `xfce+i3`.
- `nixos/graphics` contains GPU-specific modules for `amd`, `intel`, and `nvidia`.
- `nixos/processor` contains CPU/platform-specific modules for `amd` and `intel`.
- `nixos/services` contains reusable service modules such as `audio`, `bluetooth`, `steam`, `ssh`, `ollama`, and `vmware`.
- `nixos/secrets` contains a planned `sops-nix` bootstrap, migration notes, and currently exposed credential material.
- `nixos/users/thorn` contains shared config for the `thorn` user plus host overlays for `scout`, `nixos`, `mitm`, `vmware-test`, and `vmware-guest`.

## How Composition Works

1. The flake reads the active username from `current-user.lock`.
2. It reads the active host from `current-host.lock` if present.
3. If no host lock exists, it enumerates host directories under `nixos/users/<user>/hosts`.
4. `nixos/configuration.nix` imports `./users/${username}/${username}.nix`.
5. Each user entrypoint imports `./hosts/${host}/configuration.nix` when that file exists.
6. Host config imports desktop, graphics, processor, service, and networking modules as needed.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
