## Purpose

Document the Ghostty terminal setup declared in `modules/home-manager/ghostty.nix`.

## Current State

- Enabled on all four desktop hosts — `nixos`, `scout`, `mac`, and `proxmox-guest` — via `thorn.programs.ghostty.enable = true`; systemd integration, Zsh integration, and Bat/Vim syntax files are all enabled.
- Font: GeistMono Nerd Font, Regular, size 14, with a 2% cell-height adjustment.
- Block cursor, 10px window padding on both axes, 80% background opacity, copy-on-select disabled.
- `mouse-hide-while-typing` enabled, URLs are clickable (`link-url = true`).
- Shell integration is set to `detect` with `ssh-env,ssh-terminfo` features — Ghostty's shell integration propagates over SSH sessions, not just locally.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
