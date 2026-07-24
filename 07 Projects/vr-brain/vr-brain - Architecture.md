---
summary: Complete subsystem architecture of vr-brain — the bootstrap/rig, knowledge-graph constellation, cosmos visuals, in-world tools, interaction/UI, agent/MCP integration, geo engine, and the full vr-brain.cfg schema.
status: active
tags: [project, vr-brain, godot, architecture]
---

## Purpose

Full technical map of every vr-brain subsystem (companion to the experiential [[vr-brain - Overview]] and the geo-specific [[Earth - Geo Engine Rewrite]]). Godot 4.7, C#/.NET 8, OpenXR (WiVRn/Monado) with a desktop fallback rig. Compiled from source 2026-07-24.

## Summary

One `scenes/Main.tscn` (root `Node3D`, script `XRBootstrap`); every subsystem is a direct child node. `XRBootstrap` starts an OpenXR session or, if none, activates the desktop rig — so it's always controllable. The vault (an Obsidian knowledge base) is parsed into a walkable solar system; presence sources, tasks, homelab, and live geodata are woven in as celestial + globe objects. Real terminals, browsers, and a Claude agent run *inside* the world. All visuals are code-generated (no 3D assets), additive + bloomed, mostly one MultiMesh/draw-call per body.

## Bootstrap & rig

- **`XRBootstrap`** (`src/XRBootstrap.cs`) — Main root; `_Ready` tries OpenXR, else desktop fallback. `[Export] RigPath`.
- **`XRRig`** (`src/XRRig.cs`, `XROrigin3D` from `scenes/XRRig.tscn`) — fly-where-you-look locomotion (left stick, pitch included), left-trigger boost, right-stick snap-turn; no collision/gravity. Hosts the shared glide `TravelToNode`/`RecenterHead`/`GotoLookAt` used by dash + recenter + `earth_goto` in both modes.
- **`DesktopRig`** (`src/DesktopRig.cs`) — WASD/QE fly-cam driving the same origin/camera; visible cursor for point-drag, `M` = captured mouselook; yaw→origin, pitch→camera.
- **`DesktopMouse`** (`src/Brain/DesktopMouse.cs`, static) — shared cursor policy; no-op in XR.

## Knowledge graph & notes

- **`VaultSync`** (`src/Brain/VaultSync.cs`) — keeps the vault synced, publishes parsed snapshots. `[vault] mode`: **git** (clone → `user://kb-repo`, poll, hard-reset+reparse only when `origin/HEAD` moves; shells to git CLI) or **local** (watch an existing checkout, read-only). Feeds status to HUD/Discord.
- **`VaultParser`** (static) — Obsidian parsing (slugs, wikilinks, frontmatter); thread-safe, runs on the sync worker.
- **`VaultNote`** — data model; `enum NodeKind {Note, Identity, Repo, …}` (Note = vault note; others = presence nodes).
- **`BrainGraph`** (`src/Brain/BrainGraph.cs`, ~44k) — the solar-system builder: identity hub = sun; folders + presence sources = planets; notes/repos/socials/pages = moons; leaf posts = star specks. Draws wikilink + semantic lines; persists user pins to `user://layout.json`; rebuilds each snapshot. The hub other subsystems query.
- **`NoteCard`** — one celestial body (code-built billboard label + Area3D hit target), spawned per node.
- **`OrbitLayout`** — deterministic orbital layout (radius/phase/inclination from hierarchy), damped toward targets; pinned bodies hold absolute position + carry children.
- **`SemanticIndex`** — local TF-IDF + cosine relatedness (boosted by shared tags/links) → top-K relatives drawn as "semantic" constellation lines; drop-in for real embeddings later.
- **`Presence`** (`src/Brain/Presence.cs`, ~31k) + `PresenceConfig` — online presence with no auth: GitHub repos (sized by stars), gists, starred, website/blog pages, YouTube, feeds. Reads `[sources]`, `[social]`.
- **`ReaderPanel`** — world-space markdown reader (SubViewport → RichTextLabel quad); `kb://` links re-focus the graph. **`MarkdownBbcode`** (static) = injection-safe Markdown→BBCode.
- **`TimeMachine`** — scrub git history; each step `git archive`s a commit → reparse → snapshot (real repo untouched), watching the constellation grow.

## Cosmos / ambient visuals

All additive/bloomed, deterministic seeds, single-draw-call MultiMeshes; children of Main.
- **`SolarCorona`** (3 halo layers) · **`SolarProminences`** (7 plasma loops) — ride the identity sun.
- **`Nebula`** (FBM gas band) · **`Galaxies`** (spirals, 2200 motes each) · **`AsteroidBelt`** (1600 rocks) · **`Meteors`** (pool of 6 streaks) · **`Starfield`** (550 specks on r=34 shell).
- **`BlackHole`** — where deleted notes go: core + accretion disk + photon ring + lensing; a real delete spirals the orb in. `[display] black_hole`.
- **`StreakStar`** — companion star tracking your git commit **streak** (from author-dates). `[display] streak_star`.
- **`WarpEffect`** (child of camera) — jump-warp streaks + desktop FOV punch during any rig glide, scaled by travel speed.
- **`Comets`** — each unchecked `- [ ]` task → an icy comet on an eccentric orbit (coma/trail/ion), red when overdue. `[display] comets`.
- **Crew:** **`Astronaut`** (manager) + **`Crewmate`** (Docked/Fly/Work/Return state machine) — crew launch to changed note bodies, work in sparks, return. `[display] astronaut_crew`. **`SpaceStation`** — high-orbit ISS from primitives; docks two real terminals (SOC auto-runs `[station] soc_command`, admin) + a persistent browser. `[station]`.

## In-world tools

- **`Terminals`** + **`TerminalPanel`** (~31k) — real shells on quads: `$SHELL` under util-linux `script` (pty), ANSI/SGR→BBCode; close **detaches** (dtach sockets under `user://term-socks`, respawn on startup). `Shift+T` summon, `Shift+C` fly to next terminal running `claude` (scans `/proc`). Station consoles reserved via `StationIdBase`.
- **`Browsers`** + **`BrowserPanel`** (~19k each) + **`RfbClient`** — real native **Firefox** in a per-session headless **sway**, streamed by **wayvnc** over localhost RFB 3.8 (security None, Raw+CopyRect); private `XDG_RUNTIME_DIR`; setsid-daemonized so close detaches, respawn on startup. `[browser] command`.
- **`ClaudeAgent`** (`src/Brain/ClaudeAgent.cs`, ~36k) — in-world voice Claude panel: on the `claude` engine, transcript runs headless `claude` (cwd = vault) wired to the in-world MCP tools via an ephemeral `--mcp-config` pointing at `socat STDIO TCP:127.0.0.1:{McpServer.Port}` (`--strict-mcp-config`, `MCP_TIMEOUT=300000`); streams tool calls + markdown answer. `[voice]`.
- **`VoiceInput`** — push-to-talk (`pw-record` 16 kHz → offline `whisper.cpp` on release → palette or ClaudeAgent by engine). Desktop `V`, VR left `Y`. `[voice]`.
- **`Tts`** — agent voice via offline **piper** (`pw-play`), strips markdown; new-run/dismiss cuts speech. `[voice] tts*`.
- **`VrKeyboard`** — world keyboard appearing whenever XR text capture is active (terminal/browser/prompt/pin/search); synthesizes real `InputEventKey` via `Input.ParseInputEvent` so every surface types through the desktop path.

## Interaction & UI

- **`Pointer`** (~31k) — picking/grabbing both modes. XR right hand: laser, trigger=grab/pin, grip=unpin, A=open, B=close/recenter, menu=resync; left = fly + grip dash. Desktop crosshair: LMB grab (wheel=distance), RMB/Enter select, F dash, C recenter, X unpin, R resync, Ctrl+Alt+Del delete→black hole, wheel/vim scroll. Feeds DesktopHud the aim target. Metadata-picking via `Area3D.SetMeta` (`earth`, `earth_pin`, `terminal_panel`, `comet_slug`, `fleet_index`, …).
- **`SearchPanel`** (~17k) + **`FuzzySearch`** (static) — command palette over everything (orbs, presence, terminals, browsers, comets) + app actions (new terminal/browser, recenter, back, settings, sync); `?…` asks Claude. Desktop `/`, VR left `X`, voice.
- **`SettingsPanel`** (~38k) — edits `user://vr-brain.cfg` in place (orbit speed live; vault/presence changes re-sync). Desktop overlay / VR panel; tabs display · graphics · vault · agent · actions · keys. Owns `[graphics]`.
- **`DesktopHud`** (CanvasLayer, desktop-only) — title+sync (TL), clock+FPS (TR), aim readout (center), cheat-sheet (`H`, BL). **`Toasts`** — transient stack, top-center. **`FpsHud`** (Label3D on camera) — in-world FPS (works in both rigs).
- **`Postcard`** — `P` grabs the viewport → `Postcards/<ts>.png` in the vault, asks Claude (socat/MCP) for a captioned note beside it → new moon. Pre-approved writes.
- **`DailyBriefing`** — once/day past `[briefing] hour`: headless claude surveys what's new via MCP → `Briefings/<date>.md`; astronaut flies to it.

## Agent & integrations

- **`McpServer`** (~28k) — MCP server embedded in the world; newline JSON-RPC over localhost **TCP (ephemeral Port)**; claude reaches it via socat. Tools: `search_notes`, `list_notes`, `read_note`, `recent_feeds`, `write_note`, `open_note`, `open_browser`, `open_terminal`, `list_terminals`, `run_in_terminal`, `read_terminal`, `earth_pin`, `earth_pins`, `earth_goto`, `earth_layer`, `ask_user`. Mutations hit the in-world approval hook (`[voice] agent_approval`); `Briefings/`+`Postcards/` pre-approved. Session ids: SOC 900, admin 901, fleet 920+.
- **`DiscordRpc`** — Rich Presence over the Discord IPC Unix socket directly (no native lib): SET_ACTIVITY with note count / activity + elapsed. `[discord]`. Icons under `assets/discord/`.
- **`Fleet`** (~15k) — homelab as ships flying off the station truss; green/red/blink by ping; Aim+Enter docks a real **SSH console** (dtach, ids 920+, reattach on restart). `[fleet]` + `[fleet_hosts]`.
- **`ThreatGlobe`** — SIEM/attack arcs on the Earth globe from `[threat] log_command` or a geo endpoint → GeoIp → arcs to home. `[threat]`, `[geoip]`.

## Geo engine

The Earth globe + pluggable data layers — see [[Earth - Geo Engine Rewrite]] and [[Globe Data Source APIs]]. Core: `Earth.cs` (cube-sphere, imagery/detail tiles, terrain, pins, goto), `Geo/` (GeoLayer framework, CubeSphere, TerrainFilter, Vector3d), `Geo/Layers/` (weather, radar, quakes, fires, cyber, wigle, wind, heat), plus `Flights` (ADS-B), `FeedGeo`, `GeoIp`.

## Branding & infra

- **`Brand`** (static) — Catppuccin Mocha as deep space; runtime fonts Geist / GeistMono (`LoadDynamicFont`, no import step).
- **`flake.nix`** — Nix dev shell: `godot-mono`(→`godot`), `dotnet-sdk_8`, `git`, `whisper-cpp`+`pipewire`+`curl` (voice), `dtach`+`script` (terminals), `sway`+`wayvnc` (browsers), `socat` (MCP), `piper-tts` (TTS), `wtype` (UI automation).
- **`project.godot`** — Forward+, physics 90 tps, msaa_3d=2, OpenXR enabled. `openxr_action_map.tres` = XR bindings. Shaders in `assets/*.gdshader` (earth, atmosphere, terrain_tile, heat, planet, grid).

## Config schema (`~/.local/share/godot/app_userdata/vr-brain/vr-brain.cfg`)

Key names only (⚠ several sections hold **secrets** — arcgis_api_key, miniflux token, abuse_ch auth_key, firms map_key, wigle token, opensky creds — kept in the cfg, not here):

`[vault]` mode/repo_url/branch/poll_seconds/local_path/include_private · `[sources]` github/website/feeds/youtube/gists/starred/refresh · `[feeds]` named URLs · `[miniflux]` url/token/limits · `[social]` Mastodon/Bluesky/LinkedIn/YouTube · `[display]` orbit_speed/volumetrics/black_hole/streak_star/astronaut_crew/note_gravity/comets/note_aging · `[voice]` agent_approval/engine/whisper*/tts* · `[station]` name/soc_command/browser* · `[earth]` imagery+detail+terrain(+DSP) keys · `[geoip]` mmdb_path · `[fleet]`+`[fleet_hosts]` · `[briefing]` enabled/hour · `[threat]` log_command/home/geo_url · `[discord]` app_id · `[graphics]` preset/render_scale/msaa/glow/shadows · geo layers: `[flights]`/`[aircraft]`, `[weather]`, `[quakes]`, `[radar]`, `[cyber]`+`[abuse_ch]`, `[firms]`, `[wigle]`, `[wind]`, `[heat]`.

## Related

- [[vr-brain - Overview]] · [[Earth - Geo Engine Rewrite]] · [[Terrain Rendering Optimization]] · [[High-Fidelity Planet Rendering (Godot)]] · [[Globe Data Source APIs]]
