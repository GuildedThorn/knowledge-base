---
summary: "The Nix language builds lazy attribute-set expressions that evaluate to derivations, which describe reproducible build actions."
status: active
tags: [reference, engineering, nix, derivations]
private: false
---

# Nix Language and Derivations

## Purpose

The Nix language builds lazy attribute-set expressions that evaluate to derivations, which describe reproducible build actions.

## Core Model

- Nix expressions are pure-ish functional values: attribute sets, lists, strings, functions, paths, and derivations.
- A derivation is a build recipe with inputs, builder, environment, outputs, and store paths.
- The Nix store names outputs by hashes of inputs and build instructions, enabling sharing and rollback.

## Engineering Notes

- Keep pure package logic separate from host-specific configuration.
- Use overlays and package overrides sparingly and document why they exist.
- When builds are not reproducible, inspect fixed-output derivations, network access, timestamps, and undeclared inputs.

## Sources

- Nix language manual - https://nix.dev/manual/nix/latest/language/
- Nix derivations - https://nix.dev/manual/nix/latest/language/derivations
- nixpkgs manual - https://nixos.org/manual/nixpkgs/stable/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
