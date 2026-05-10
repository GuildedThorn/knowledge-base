## Purpose

Track how host-specific configuration is split across shared modules, user layers, and per-machine files.

## Layout Pattern

The repo uses a layered layout:

1. `nixos/configuration.nix` provides the base system layer.
2. `nixos/users/<user>/<user>.nix` provides shared config for a specific user.
3. `nixos/users/<user>/hosts/<host>/configuration.nix` provides host-specific system config.
4. `nixos/users/<user>/hosts/<host>/home.nix` provides host-specific Home Manager overrides when needed.
5. `nixos/users/<user>/hosts/<host>/networking.nix` isolates network and firewall settings per host.

## Current Host Trees

- `scout`
- `nixos`
- `mitm`
- `vmware-test`
- `vmware-guest`

## Why This Split Works

- shared user defaults stay centralized
- networking stays isolated per machine
- desktop, graphics, and services are reusable imports rather than copy-pasted blocks
- Home Manager stays mostly shared while still allowing per-host monitor and panel layouts for hosts that define a host `home.nix`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Repository Layout|Repository Layout]]
- [[02 Systems/NixOS - Hosts Overview|Hosts Overview]]
