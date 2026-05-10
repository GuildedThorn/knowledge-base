## Purpose

Provide a single summary of the host inventory represented in `~/nix-config`.

## Thorn Hosts

- `scout`: Intel-based laptop with Hyprland, ThinkPad-specific thermal and power tuning, Wi-Fi via NetworkManager, and a desktop-heavy daily-driver software stack.
- `nixos`: AMD-based main workstation with Hyprland, local DNS pointing at `127.0.0.1`, CIFS media mount, Podman, Waydroid, VMware host support, gaming, SDR, and VR tooling.
- `mitm`:  Intel-based minipc service-oriented host with NGINX reverse proxying, Technitium DNS, MongoDB, Grafana, and a partially defined SearXNG setup.
- `vmware-test`: lighter XFCE+i3 test VM with audio, ClamAV, and SSH enabled.
- `vmware-guest`: XFCE+i3 VMware guest profile with audio, ClamAV, SSH, and a host-specific Home Manager overlay.

## Shared Patterns

- IPv6 is disabled on all inspected hosts.
- Host networking is split into separate `networking.nix` files.
- Host configs import reusable desktop, graphics, and service modules rather than duplicating large option blocks.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[02 Systems/NixOS - Host scout|Host scout]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Host mitm|Host mitm]]
- [[02 Systems/NixOS - Host vmware-test|Host vmware-test]]
- [[02 Systems/NixOS - Host vmware-guest|Host vmware-guest]]
