---
summary: Typst markup-based typesetting system and its typst.app web editor — a candidate tool, not yet declared in ThornixOS.
status: planned
tags: [software]
---

## Purpose

Track Typst — a markup-based typesetting system — as a candidate writing tool
for the fleet. Documents what it is and what installing it would involve, since
nothing document-authoring (LaTeX, pandoc, Typst) is declared in ThornixOS yet.

## Current State

- **Not installed or declared.** `typst` is not on `PATH` on this host and no
  `modules/` file references it as of 2026-07-28.
- Typst is a modern LaTeX alternative: plain-text markup compiled to PDF, written
  in Rust, with fast incremental compilation and a scripting language for styles.
- <https://typst.app/> is the hosted collaborative editor (Overleaf-style, live
  preview, project sharing). It runs in the browser and needs an account.
- The same engine is available offline as the `typst` CLI (nixpkgs package
  `typst`); `tinymist` is the current Typst language server for editor
  integration (supersedes the old `typst-lsp`).

## Tasks

- Decide hosted (typst.app account) vs. local CLI — likely local to match the
  declarative, offline-first setup.
- If local: add `typst` to `home.packages` in
  `modules/home-manager/base.nix`, or give it a dedicated
  `modules/home-manager/typst.nix` following the per-app module pattern.
- For editing in [[04 Software/NixVim|NixVim]], add the `tinymist` LSP and a
  Typst filetype/treesitter grammar.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[06 Reference/Typst Examples|Typst Examples]]
- [[04 Software/NixVim|NixVim]]
- [[08 Improvements/Ideas Backlog|Ideas Backlog]]
