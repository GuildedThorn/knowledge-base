---
summary: "Remote network management, software development, and personal finance."
status: active
tags: [devices]
---

## Purpose

Remote network management, software development, and personal finance.

## Identity

- Hostname: `scout`
- OS: `NixOS 26.06`
- Config path: `~/Documents/ThornixOS` (`modules/computers/scout.nix` + `hosts/scout/`)

## Hardware Specs

- CPU: `Intel Core i5-10210U`
- GPU: `Intel UHD Graphics`
- Memory: `16 GB DDR4 @ 2133 MHz`
- Storage: `1 TB Sabrent Rocket Pro NVMe`

## NixOS-Specific Notes

- Uses the `scout` host under the `thorn` user tree.
- Runs Hyprland with a host-specific two-monitor layout (`eDP-1` internal panel + `HDMI-A-2` external, likely via the dock — see [[03 Devices/Docks and Displays|Docks and Displays]]).
- Uses NetworkManager with Wi-Fi power saving enabled.
- Enables ThinkPad fan control with `thinkpad_acpi` and `thinkfan` (custom aggressive fan curve).
- Enables laptop-oriented services including `howdy`, IR emitter support, `tlp` (with battery charge thresholds), `thermald`, and `upower`.
- Secure boot via `lanzaboote`; U2F required for `sddm`/`sudo` login.

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host scout|NixOS - Host scout]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
