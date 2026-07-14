## Purpose

Document the `vmware-test` host, composed in `modules/computers/vmware-test.nix`.

## Role

Minimal, no Home Manager overlay test environment for VMware-related or disposable desktop experiments.

## Composition

- `thorn-core` base bundle
- `desktop-xfce-i3` module
- service modules: audio, ClamAV, SSH, `vmware-guest`
- `hosts/vmware-test/hardware-configuration.nix`, `networking.nix`

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[02 Systems/NixOS - Host vmware-guest|Host vmware-guest]]
