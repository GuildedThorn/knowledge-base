---
summary: "Nix flakes package inputs, outputs, and lockfiles into a reproducible interface for packages, apps, dev shells, and NixOS systems."
status: active
tags: [reference, engineering, nix, flakes]
private: false
---

# Flakes, Lockfiles, and Inputs

## Purpose

Nix flakes package inputs, outputs, and lockfiles into a reproducible interface for packages, apps, dev shells, and NixOS systems.

## Core Model

- flake.nix declares inputs and outputs; flake.lock pins resolved revisions and content hashes.
- Outputs commonly include packages, apps, devShells, checks, overlays, nixosModules, and nixosConfigurations.
- Lockfile updates are dependency updates and should be reviewed like any other dependency change.

## Engineering Notes

- Use `follows` to avoid duplicate nixpkgs inputs where practical.
- Keep host outputs and development outputs named consistently.
- Commit lockfile changes with the reason for upgrade when they affect production hosts.

## Sources

- Nix flakes manual - https://nix.dev/manual/nix/latest/command-ref/new-cli/nix3-flake
- NixOS wiki - Flakes - https://wiki.nixos.org/wiki/Flakes
- nix.dev flakes tutorial - https://nix.dev/tutorials/working-with-local-files.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
