---
summary: "Reproducible builds and binary caches let teams verify, share, and deploy build outputs with stronger supply-chain confidence."
status: active
tags: [reference, engineering, nix, reproducible-builds]
private: false
---

# Reproducible Builds and Binary Caches

## Purpose

Reproducible builds and binary caches let teams verify, share, and deploy build outputs with stronger supply-chain confidence.

## Core Model

- A reproducible build produces the same output from the same inputs across environments.
- Nix binary caches serve prebuilt store paths signed by trusted keys.
- Cache substitution trades build time for trust in cache provenance and signatures.

## Engineering Notes

- Pin dependencies, avoid undeclared inputs, normalize timestamps, and capture build metadata.
- Trust cache keys deliberately; an untrusted cache is code execution at install time.
- Use CI to build and populate caches for slow packages and shared dev environments.

## Sources

- Reproducible Builds project - https://reproducible-builds.org/
- Nix store and binary caches - https://nix.dev/manual/nix/latest/package-management/binary-cache-substituter
- nix copy/store paths - https://nix.dev/manual/nix/latest/command-ref/new-cli/nix3-copy

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
