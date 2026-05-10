## Purpose

Document the `vmware-guest` host under `nixos/users/thorn/hosts/vmware-guest`.

## Role

VMware guest profile for XFCE+i3 desktop testing with the shared `thorn` Home Manager layer.

## Composition

- networking from `hosts/vmware-guest/networking.nix`
- `desktop/xfce+i3.nix`
- shared service modules for audio, ClamAV, and SSH
- host-specific Home Manager overlay from `hosts/vmware-guest/home.nix`, currently only setting `home.stateVersion = "26.05"`

## Notable Host Behavior

- Hostname is `vmware-guest`.
- NetworkManager is disabled.
- Uses DNS `1.1.1.1`.
- Opens only TCP and UDP port `22`.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
