## Purpose

Document the Vesktop (Discord client) setup declared in `modules/home-manager/vesktop.nix`.

## Current State

- Enabled on `nixos` and `scout` only (not `mac` or `proxmox-guest`).
- Was briefly dropped in favor of Dorion (a lighter Discord client; `modules/home-manager/dorion.nix`), then re-enabled — the Dorion module still exists but nothing currently enables it.
- Tracks the Discord **canary** branch.
- Settings: arRPC (local Rich Presence bridge) enabled, hardware acceleration on, minimize-to-tray on, tray icon on, update checks on.
- Vencord auto-update is on, with update notifications suppressed.

## Vencord Plugins Enabled

`MessageLogger` (ignoring the user's own messages), `FixSpotifyEmbeds`, `SpotifyControls`, `SpotifyCrack`, `SilentTyping`, `USRGB`, `ValidUser`, `YutubeAdBlock`, `ShowHiddenChannels`, `PlatformIndicators`, `Translate`, `FakeNitro`.

## Related

- [[01 Maps/Software Map|Software Map]]
- [[02 Systems/NixOS - Home Manager Layout|Home Manager Layout]]
- [[07 Projects/ThornBot/ThornBot - Overview|ThornBot - Overview]]
