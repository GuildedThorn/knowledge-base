## Purpose

Track unfinished work around host config, secrets, deployment flow, and documentation.

## Current State

- The vault now has host notes for `scout`, `nixos`, `mitm`, `vmware-test`, and `vmware-guest`.
- The repo has a `sops-nix` plan under `nixos/secrets`, but the active flake does not currently include the `sops-nix` input or import the secrets module.
- Some documentation is still architecture-level and does not yet capture day-two operational procedures.

## Tasks

- [ ] Document the exact `make install` plus `bin/rebuild-deploy <user> <host>` workflow as actually used in practice
- [ ] Record where `current-user.lock` and `current-host.lock` are normally managed from
- [ ] Wire `sops-nix` into the active flake or revise the secrets plan to match the chosen secret manager
- [ ] Convert the secrets plan into a real secret inventory with owners, source files, and migration status
- [ ] Record which hosts currently consume `credentials.env`, VPN material, or service secrets
- [ ] Move the inline Intelephense license key out of `nixos/users/thorn/programs/nixvim/main.nix`
- [ ] Decide whether NixVim should standardize on `nixfmt`, `nixpkgs-fmt`, or `alejandra`
- [ ] Add host-specific operational notes for `mitm`, especially NGINX, Grafana, Technitium DNS, and SearXNG
- [ ] Add host-specific operational notes for `nixos`, especially Podman, Waydroid, local DNS, VR, and CIFS media mount behavior
- [ ] Add host-specific operational notes for `scout`, especially power, thermals, docking, and travel usage
- [ ] Create a dedicated note for Home Manager UX customizations if `ags`, `eww`, `hyprpanel`, and monitor layout tuning keep growing
- [ ] Fix stale `users/guildedthorn/...` references in `nixos/secrets/README.md` so they point at `users/thorn/...`

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Secrets Strategy|NixOS - Secrets Strategy]]
