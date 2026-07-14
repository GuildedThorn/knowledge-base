## Purpose

Document emulation and retro-gaming tooling across the fleet, including its overlap with [[07 Projects/SkyDestroyer/SkyDestroyer - Overview|SkyDestroyer]].

## Current State (Real)

- `retroarch` plus `libretro.pcsx-rearmed` and `libretro.pcsx2` cores are installed on `nixos` (via the `services-retroarch` module); a curated libretro core set lives under `/etc/retroarch`.
- `clonehero` (rhythm game) is installed on both `nixos` and `scout`, and has its own packaging under `programs/clonehero/clonehero.nix` in `ThornixOS` — a standalone program tree rather than a plain package reference.
- `osu-lazer`/`osu-lazer-bin` is installed on `nixos`.
- `heroic` (Epic/GOG launcher) and `lutris` are installed on `nixos`.
- PCSX2 (a real PS2 emulator, separate from the RetroArch core) is a dev-shell dependency of [[07 Projects/SkyDestroyer/SkyDestroyer - Overview|SkyDestroyer]] specifically for rig-testing the server against a real *Tribes: Aerial Assault* client — screenshot/input-automation tooling (`xdotool`, `wtype`, `wlrctl`, `grim`, `slurp`) is bundled alongside it for that purpose.
- Sober/Vinegar (Roblox compatibility layers) are installed via Flatpak on `nixos`.

## Open Questions

- Beyond the SkyDestroyer testing use case, is PCSX2 also used for general PS2 game emulation, or is it purpose-built for that one project?
- Which RetroArch cores beyond PCSX/PCSX2 are actually configured under `/etc/retroarch` — worth documenting once that's settled.
- Any interest in a dedicated retro-gaming library/ROM management note, or is this purely ad hoc?

## Related

- [[07 Projects/SkyDestroyer/SkyDestroyer - Overview|SkyDestroyer - Overview]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
