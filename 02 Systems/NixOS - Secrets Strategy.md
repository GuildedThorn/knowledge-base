## Purpose

Capture the current secret-management direction in the repo without copying sensitive values into the knowledge base.

## Current State

- `nixos/secrets/default.nix` exists and describes the intended `sops-nix` setup.
- The active `nixos/flake.nix` does not currently include a `sops-nix` input or import the secrets module globally.
- The repo still contains exposed material that the repo itself identifies as migration targets rather than finalized secret handling.

## Documented Migration Targets

According to `nixos/secrets/README.md`, the first migration targets are:

- the CIFS credentials file used by the media share mount
- the committed VPN profile under `nixos/users/thorn/certs/vpn/pfproxmox.ovpn`
- service configs that currently embed password or API values, including Glance and Pi-hole module examples
- the inline Intelephense license key in `nixos/users/thorn/programs/nixvim/main.nix`

## Intended Layout

The repo’s own plan points toward:

- host or common encrypted YAML files under `nixos/secrets/hosts`
- binary secrets such as VPN profiles stored as encrypted files
- service configs reading secrets from `config.sops.secrets.*.path` after `sops-nix` is wired into the flake

## Operational Notes

- `sops-nix` decrypts during activation, not evaluation, once enabled.
- Host SSH keys must exist on the target system for decryption to work with the current approach.
- This knowledge base should document where secrets are consumed, but not store literal secret values or raw secret files.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
