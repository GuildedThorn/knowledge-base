---
summary: "NixOS modules merge option declarations and definitions into a system configuration evaluated into activation and service artifacts."
status: active
tags: [reference, engineering, nixos, modules]
private: false
---

# NixOS Modules, Options, and Evaluation

## Purpose

NixOS modules merge option declarations and definitions into a system configuration evaluated into activation and service artifacts.

## Core Model

- Options declare type, default, description, example, and merge behavior.
- Modules define config fragments that merge structurally rather than by text.
- mkIf, mkMerge, mkDefault, mkForce, and priorities control conditional and override behavior.

## Engineering Notes

- Create options for reusable policy, not for one-off values that can remain local.
- Keep host modules small enough that option source can be traced quickly.
- Use `nixos-option`, `nix repl`, and evaluation traces to debug unexpected merged config.

## Sources

- NixOS manual - Writing modules - https://nixos.org/manual/nixos/stable/#sec-writing-modules
- NixOS options search - https://search.nixos.org/options
- NixOS module system docs - https://nix.dev/tutorials/module-system/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
