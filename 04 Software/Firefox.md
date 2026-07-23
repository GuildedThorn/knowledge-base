---
summary: Document the Firefox setup declared in `modules/home-manager/firefox.nix`.
status: active
tags: [software]
---

## Purpose

Document the Firefox setup declared in `modules/home-manager/firefox.nix`.

## Current State

- Enabled on all four desktop hosts — `nixos`, `scout`, `mac`, and `proxmox-guest`.
- Homepage is `http://localhost:8080` — matches the [[04 Software/Glance|Glance]] dashboard's listen port, so Firefox opens straight to the local dashboard.
- Default and private search engine is DuckDuckGo, with search forced (`search.force = true`, can't be changed via the UI).
- Three custom NixOS-flavored search engines with aliases: `@np` (Nix Packages, `search.nixos.org/packages`), `@no` (Nix Options, `search.nixos.org/options`), `@nw` (NixOS Wiki).
- Policies: Pocket, telemetry, form history, and password reveal all disabled.
- Force-installed extensions (can't be removed by the user): uBlock Origin, Vimium, Dark Reader, and Spirited Away (all also enabled in private browsing except Spirited Away, which additionally has updates disabled).
- Stylix theming targets the `default` profile.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[04 Software/Glance|Glance]]
