---
summary: "Document which AI coding tools are actually in use across the fleet, since they show up scattered as package references with no home of their own."
status: active
tags: [software]
---

## Purpose

Document which AI coding tools are actually in use across the fleet, since they show up scattered as package references with no home of their own.

## Current State

- **Claude Code** (`claude-code`): installed on `scout`; this vault itself is maintained through it.
- **Codex** (OpenAI's CLI coding agent, `codex`): installed on both `nixos` and `scout`. Real config at `~/.codex/config.toml` confirms active use — `model = "gpt-5.5"`, `model_reasoning_effort = "xhigh"`, with trusted-project entries for `~/`, `~/Documents/SkyDestroyer`, and two **pre-rename paths**: `~/Downloads/nix-config` and `~/Downloads/GuildedThorn.com-main` — both stale now (the former is `ThornixOS` at `~/Documents/ThornixOS`, the latter is `GuildedThorn.com` at `~/Documents/GuildedThorn.com`), meaning Codex's own trust list hasn't been updated since those repos moved.
- **opencode** (`opencode`): installed on `nixos` only.
- **Wakatime**: genuinely configured, not just installed — `wakatime-cli` is a package on `nixos`, and [[04 Software/NixVim|NixVim]] has `wakatime.enable = true` as a real plugin, so coding time is actively tracked from the editor. This corrects the earlier assumption in [[08 Improvements/Ideas Backlog|Ideas Backlog]] that Wakatime had "no declared config" — it does, just from NixVim rather than a standalone module. It reports to **Wakapi** (`https://wakapi.dev/api`, the hosted instance of the open-source self-hostable WakaTime-server alternative) rather than the official wakatime.com service — the API key is a sops secret (`wakatime_api_key`) templated straight into `~/.wakatime.cfg`.

## Coding-Time Tracking Backend

Wakapi is worth calling out on its own: it's an open-source, self-hostable reimplementation of the WakaTime backend, API-compatible with the official `wakatime-cli`/editor plugins. Using the public `wakapi.dev` instance rather than wakatime.com means the data isn't tied to a WakaTime account — and self-hosting it later (there's precedent for that instinct across this fleet — see [[03 Devices/TrueNAS|TrueNAS]], SearXNG, Owncast) would be a natural, low-effort addition to [[08 Improvements/Homelab Roadmap|Homelab Roadmap]].

## Open Questions

- Should the stale Codex trusted-project paths be cleaned up to match the current `ThornixOS`/`GuildedThorn.com` locations?
- Is there a preference between Claude Code, Codex, and opencode for different kinds of work, or is it mostly ad hoc?

## Related

- [[01 Maps/Software Map|Software Map]]
- [[04 Software/NixVim|NixVim]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Host scout|Host scout]]
- [[08 Improvements/Ideas Backlog|Ideas Backlog]]
- [[08 Improvements/Homelab Roadmap|Homelab Roadmap]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
