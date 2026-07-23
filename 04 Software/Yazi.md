---
summary: Document the Yazi (terminal file manager) setup declared in `modules/home-manager/base.nix`.
status: active
tags: [software]
---

## Purpose

Document the Yazi (terminal file manager) setup declared in `modules/home-manager/base.nix`.

## Current State

- Enabled with Zsh integration, using the flake's own `yazi` package input (`inputs.yazi.packages.<system>.default`) rather than the nixpkgs version — implies wanting a newer/pinned build than nixpkgs ships.
- The `mount` plugin (`pkgs.yaziPlugins.mount`) is enabled.
- Stylix theming is explicitly targeted at Yazi (`stylix.targets.yazi.enable = true`).

## Configuration Detail

- Hidden files and symlinks are shown by default; sort is natural, case-sensitive, directories-first, with no extra line-mode annotation.
- Pane ratio is `[1, 4, 3]` (narrow parent / wide current / preview column).
- Image preview uses Lanczos3 filtering at 90% quality, capped at 600×900, via ueberzug.
- Task queue: 5 micro workers, 10 macro workers, 5 retries on failure ("bizarre_retry").

## Related

- [[01 Maps/Software Map|Software Map]]
- [[04 Software/Shell Environment|Shell Environment]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
