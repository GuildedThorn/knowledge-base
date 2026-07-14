## Purpose

Document the `vmware-guest` host, composed in `modules/computers/vmware-guest.nix`.

## Role

VMware guest profile for XFCE+i3 desktop testing with a Home Manager overlay.

## Composition

- `thorn-core` base bundle
- `desktop-xfce-i3` module
- service modules: audio, ClamAV, SSH, `vmware-guest`
- `hosts/vmware-guest/hardware-configuration.nix`, `networking.nix`
- host-specific Home Manager overlay (`hosts/vmware-guest/home.nix`), historically just `home.stateVersion`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[02 Systems/NixOS - Host vmware-test|Host vmware-test]]
