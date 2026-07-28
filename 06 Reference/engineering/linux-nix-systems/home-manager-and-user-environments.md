---
summary: "Home Manager manages user-level packages, dotfiles, services, and application config with Nix modules."
status: active
tags: [reference, engineering, nix, home-manager]
private: false
---

# Home Manager and User Environments

## Purpose

Home Manager manages user-level packages, dotfiles, services, and application config with Nix modules.

## Core Model

- Home Manager can run standalone or as a NixOS module.
- User services, programs, files, and xdg paths are modeled through options.
- It complements system configuration but should not hide host-level requirements that belong in NixOS.

## Engineering Notes

- Use Home Manager for per-user shell/editor/app config and NixOS modules for system services, hardware, and security policy.
- Keep secrets out of the Nix store unless intentionally public.
- Document compatibility boundaries between Linux desktop, macOS, and host-specific user config.

## Sources

- Home Manager manual - https://nix-community.github.io/home-manager/
- Home Manager options - https://nix-community.github.io/home-manager/options.xhtml
- NixOS manual - https://nixos.org/manual/nixos/stable/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
