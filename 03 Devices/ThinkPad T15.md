## Purpose

Remote network management, software development, and personal finance.

## Identity

- Hostname: `scout`
- OS: `NixOS 26.06`
- Config path: `~/nix-config/nixos/users/thorn/hosts/scout`

## Hardware Specs

- CPU: `Intel Core i5-10210U`
- GPU: `Intel UHD Graphics`
- Memory: `16 GB DDR4 @ 2133 MHz`
- Storage: `1 TB Sabrent Rocket Pro NVMe`

## NixOS-Specific Notes

- Uses the `scout` host under the `thorn` user tree.
- Runs Hyprland with a host-specific single-monitor layout.
- Uses NetworkManager with Wi-Fi power saving enabled.
- Enables ThinkPad fan control with `thinkpad_acpi` and `thinkfan`.
- Enables laptop-oriented services including `howdy`, IR emitter support, `tlp`, `thermald`, and `upower`.

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host scout|NixOS - Host scout]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
