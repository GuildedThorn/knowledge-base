## Purpose

Document the `vmware-test` host under `nixos/users/thorn/hosts/vmware-test`.

## Role

Minimal test environment for VMware-related or disposable desktop experiments.

## Composition

- networking from `hosts/vmware-test/networking.nix`
- `desktop/xfce+i3.nix`
- shared service modules for audio, ClamAV, and SSH

## Notable Host Behavior

- Hostname is `vmware-test`.
- NetworkManager is disabled.
- Uses DNS `1.1.1.1`.
- Opens only TCP and UDP port `22`.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
