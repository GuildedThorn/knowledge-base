---
summary: "Document the architecture and current state of `vr-brain`, the VR knowledge-constellation app that renders this vault in a headset."
status: active
tags: [projects, vr-brain]
---

## Purpose

Document the architecture and current state of `vr-brain`, the VR knowledge-constellation app that renders this vault in a headset.

## Summary

vr-brain turns the Obsidian knowledge-base — and the GuildedThorn online presence — into a walkable VR solar system. Built on the [[10 Hobbies/VR Setup|vr-base]] template (Godot 4 + C# / .NET 8 + OpenXR), it runs on the WiVRn/Monado stack from the `services-vr` module on host `nixos`, and also has a desktop (non-headset) rig.

- Repo: [GuildedThorn/vr-brain](https://github.com/GuildedThorn/vr-brain), local checkout at `~/Documents/vr-brain`
- Template it grew from: [GuildedThorn/vr-base](https://github.com/GuildedThorn/vr-base) at `~/Documents/vr-base`

## The constellation

- The graph is a solar system: the identity hub is the sun, each top-level vault folder and presence source is a ringed planet, notes/repos are moons, subfolders are smaller moon-hubs, and leaf content stays folded under its source until focused. Orbits are deterministic with a slow drift; planets are grouped into per-category spiral-arms (by their dominant child kind), ordered by population, and spaced by each folder's moon-disk footprint so nothing overlaps (reorganized 2026-07-23). Constellation link-lines are kept local (same cluster) so the sky isn't a web; the floor grid was removed so the system floats in open space.
- `[[wikilinks]]` draw as constellation lines; `private: true` notes are ringed in red; grabbing a body pins it in place, unpinning glides it back.
- Online presence hangs off the same identity hub, fetched live with no auth: GitHub repos (sized by stars), gists, and starred projects, plus web/blog pages.
- An astronaut idles by the sun and flies to any note that changes on disk (Obsidian edit, git push, or Claude writing the vault), showing edits live.

## Terminals, browsers, station

- Real terminals float in-world, backed by dtach sessions (`term-socks/term-N`) that detach on quit and reattach on relaunch. Fleet SSH consoles use session ids 920+.
- Real Firefox browsers run in-world with per-session persistent profiles under `browser-sessions/`.
- A space station rides a high orbit as the ops deck: a SOC console (auto-runs the security dashboard, survives restarts), an admin console, and a persistent docked browser.

## Claude voice agent

- Push-to-talk with voice engine `claude`: the local whisper transcript is handed to a headless `claude` run rooted in the vault, wired into the world through an embedded MCP server. The agent can search/read/write notes, focus orbs, open terminals and type into them, and open in-world browsers; a floating panel streams its output.
- Mutations (note writes, terminal commands) pause on an in-world approve prompt — Y runs, N declines. Claude's own file tools are read-only; edits funnel through `write_note`. Toggle via `[voice] agent_approval`.
- The panel has a prompt line for typed follow-ups in the same conversation; a fresh voice push starts a new one.
- The agent also writes into the vault itself: daily notes under `Briefings/` and VR screenshots + captions under `Postcards/`.

## Key bindings (highlights)

- **H** — cheat sheet; **C** — recenter; **Esc** — release panel focus; **X** — dismiss/stop the agent panel.
- **Shift+T** — summon terminals to you; **Shift+B** — summon browsers; **Ctrl+Shift+W** — detach a browser session; **Ctrl+Shift+Q** — quit a browser session (profile survives).
- **Shift+C** (added 2026-07-22) — flies *you* to the next terminal with a live `claude` process and focuses it, one hop per press; panels stay where placed, free-floating ones turn to face you, station consoles untouched. Detection: `Terminals.SessionsRunningClaude()` scans `/proc` for `claude` processes and walks parent chains to the dtach session master to recover the session id. Runs only on keypress. Limits: fleet SSH consoles (ids 920+) can't be detected (remote claude is invisible to local `/proc`); plain **C** remains recenter. Code: `src/Brain/Terminals.cs` (`VisitNextClaude`), `src/Brain/Pointer.cs`, `src/DesktopRig.cs`.

## Comets (tasks)

- Every unchecked `- [ ]` task in the vault becomes an icy comet on a deterministic eccentric, inclined orbit crossing the system. Each has a glowing **coma**, a ribbon **trail threaded back along the path it actually travelled**, and ion/dust particles streaming out behind its motion; it flares brighter near perihelion and dims out at the cold far end. Overdue tasks turn red. Aim + Enter (or RMB) opens the source note; checking the task off melts the comet on the next sync. Toggle: `[display] comets`. Code: `src/Brain/Comets.cs`.

## Cosmic environment (added 2026-07-23)

The ambient/visual layer, all additive + bloomed and holding ~140 fps on desktop:

- **Living sun** — the identity sun breathes and flickers via a stacked additive **corona** and erupts plasma **prominences** (magnetic loops arcing off the surface); sized to dwarf Earth. `src/Brain/SolarCorona.cs`, `SolarProminences.cs`.
- **Nebula** — a procedural FBM-noise nebula (no assets) wraps the system in a tilted galactic band of gas clouds. `src/Brain/Nebula.cs`.
- **Spiral galaxies** wheel in the deep background (log-spiral star-motes in one MultiMesh each). `src/Brain/Galaxies.cs`.
- **Asteroid belt** — a tilted ring of ~1600 tumbling rocks in a single MultiMesh. `src/Brain/AsteroidBelt.cs`.
- **Meteor shower** — occasional shooting stars streak the far sky. `src/Brain/Meteors.cs`.
- **Twinkling starfield** — the background stars shimmer on detuned sines. `src/Brain/Starfield.cs`.
- Inner bodies (planets, comet perihelia, the crew dock) were pushed out so nothing sits inside the enlarged sun's corona.

## Search palette

- **/** (desktop) or left **X** (VR) opens a fuzzy finder over *everything*: notes — matched on title **and** full body text — and presence orbs, plus the live floating terminals, browser panels, and task comets. Select a result to focus it and dash there. `src/Brain/SearchPanel.cs`, `FuzzySearch.cs`.

## Related

- [[10 Hobbies/VR Setup|VR Setup]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[01 Maps/Projects Map|Projects Map]]
