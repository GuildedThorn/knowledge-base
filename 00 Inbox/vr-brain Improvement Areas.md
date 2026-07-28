## Summary

Where vr-brain has the most room to improve, from a review of the [Architecture](kb://07-projects-vr-brain-vr-brain-architecture) doc on 2026-07-24.

## Context

- Source: Claude review (in-world agent)
- Machine: nixos
- Project: [vr-brain](kb://07-projects-vr-brain-vr-brain-overview)
- Date: 2026-07-24

## Notes

**Security (highest value)**

- Secrets (arcgis_api_key, miniflux token, FIRMS map_key, wigle token, opensky creds, abuse.ch auth_key) sit in plaintext `vr-brain.cfg`. Move to a secrets store / sops-nix, or at least lock file perms + gitignore discipline.
- `wayvnc` runs RFB **security None** and `McpServer` is unauthenticated JSON-RPC over localhost TCP. Localhost-only today, but one misbind exposes the whole agent + browser surface. Add a token handshake on the MCP socket.

**Intelligence**

- `SemanticIndex` is still TF-IDF + cosine — the arch doc itself calls it a "drop-in for real embeddings." Swapping to a local embedding model is the single biggest relevance upgrade. Research on how to actually do this now exists: [Local Embedding Models for Semantic Search](kb://06-reference-local-embedding-models-for-semantic-search) (ONNX Runtime in-process, BGE-small/nomic-embed model choice, incremental re-embedding keyed to VaultSync content hashes, brute-force cosine at this vault's scale).

**Scale & reliability**

- One `Main.tscn` with every subsystem as an always-loaded child, and `VaultSync` does a full hard-reset **reparse per snapshot**. Both degrade as the vault grows — incremental reparse + lazy subsystem loading would help.
- No automated tests are documented. Even a headless smoke test of `VaultParser` / `MarkdownBbcode` / `McpServer` would catch regressions.

**Known gaps**

- Fleet SSH consoles (ids 920+) can't detect a remote `claude` via local `/proc` — remote sessions are invisible to Shift+C.
- Still no Proxmox/TrueNAS telemetry (see [deferred migration](kb://02-systems-nixos-host-nixos)). An interim syslog / node_exporter feed into ThreatGlobe or Fleet would close it.

## Code Audit — UI Panel Rendering (2026-07-24)

Triggered by writing [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design) and [UI Rendering Performance in Godot](kb://06-reference-ui-rendering-performance-in-godot) — went back and checked the actual `~/Downloads/vr-brain` source against the general Godot caveats surfaced by that research. Repo had ~20 files of unrelated uncommitted WIP at the time; changes below were scoped narrowly and `dotnet build` confirmed clean (0 warnings, 0 errors) before and after.

**Fixed**: none of the five SubViewport-backed quad panels (`ReaderPanel`, `TerminalPanel`, `BrowserPanel`, `SearchPanel`, `SettingsPanel`) set an explicit `TextureFilter` on their quad's `StandardMaterial3D` — all five were relying on the implicit default rather than mip-aware anisotropic sampling. Added `TextureFilter = BaseMaterial3D.TextureFilterEnum.LinearWithMipmapsAnisotropic` to all five (same one-line change, same spot: right after `AlbedoTexture = _viewport.GetTexture()`).

**Checked, not a bug** (correcting an assumption from the UI research before verifying against real code):

- Feared: `SubViewport` 2D MSAA corrupting/freezing content (a real, documented Godot bug). Checked — nothing in the codebase sets `msaa_2d` anywhere. Never triggered. No fix needed.
- Feared: `TerminalPanel` rebuilding its `RichTextLabel.Text` wholesale every update instead of using `append_text()`, per generic "avoid re-parsing a big RichTextLabel" advice. Checked — `TerminalPanel` implements a real terminal-grid model (cursor addressing, in-place redraw anywhere on screen, needed for vim/htop-style full-screen apps), which **cannot** be append-only by nature — `append_text()` would be actively wrong here, not an optimization. It already throttles full-buffer re-renders to a fixed interval (`RenderInterval = 0.05`, comment: "throttle full-buffer re-parse") — already correctly optimized for what it actually needs to do.
- SubViewport update modes across all five panels were already well-chosen before this audit: `Always` on `BrowserPanel`/`ClaudeAgent`/`Fleet`/`TerminalPanel` (genuinely continuous content), `WhenVisible` on `ReaderPanel`/`SearchPanel`/`SettingsPanel`/`VrKeyboard` (event-ish content). Matches the guidance in [UI Rendering Performance in Godot](kb://06-reference-ui-rendering-performance-in-godot) already — no change made.

**Real gap, not fixed — needs the Godot editor open to verify visually**: `ViewportTexture` doesn't generate mipmaps by default in Godot (a still-open upstream limitation) — the `TextureFilter` change above makes the materials mip-*ready* but doesn't create mip data itself, so panel text may still alias/shimmer at distance or a shallow viewing angle in VR until that's addressed. A real fix needs a periodic `Image` snapshot + `generate_mipmaps()` + `ImageTexture` swap per panel (or supersampling the SubViewport as a cheaper partial workaround) — didn't attempt it blind since this session has no way to visually confirm the render actually looks right.

## Code Fix — ClaudeAgent Silent Error (2026-07-24)

The recurring "the run ended with an error" message in the voice/agent panel had no diagnostic info because `ClaudeAgent.cs` read the headless `claude` process's stderr and discarded it (`ReadToEnd()` into nothing). Fixed: stderr is now captured progressively into a locked buffer, cleared at the start of each run, and folded into the fallback error message along with the stream-json result's `subtype` (`error_max_turns`, `error_during_execution`, etc.) whenever a run ends without usable `result` text. `dotnet build` clean. Next time it fails, the panel will show the real cause instead of the opaque generic line — revisit once that surfaces what's actually recurring.

## Code Retrofit — Desktop Keyboard InputMap (2026-07-24)

Triggered by writing [Godot Input Handling and Keybind Design](kb://06-reference-godot-input-handling-and-keybind-design) and [VR Controller Input and OpenXR Action Maps](kb://06-reference-vr-controller-input-and-openxr-action-maps) — checked the real code and found the desktop side had **zero** InputMap usage: every binding was a raw `Input.IsPhysicalKeyPressed(Key.X)` or `switch (key.PhysicalKeycode)` check across `DesktopRig.cs` (movement/look/recenter/mouselook) and `Pointer.cs` (reader scroll + the whole interaction switch — dash, summon terminal/browser, search, dismiss, resync, postcard, delete). The VR-controller side already did this correctly via named OpenXR actions (`XRController3D.GetVector2("primary")`, etc.) — only desktop needed the retrofit.

**Applied**: added `src/Brain/Keybinds.cs`, a static registry (`Keybinds.RegisterDefaults()`, called once as the first line of `XRBootstrap._Ready()`) that binds one InputMap action per physical key — `move_forward`/`strafe_left`/`rise`/`sprint`/`look_up`/`recenter`/`toggle_mouselook`/etc. for `DesktopRig.cs`, `reader_line_down`/`reader_page_up`/etc. for the reader scroll, and `interact`/`search`/`dash`/`dismiss`/`resync`/`terminal_key`/`browser_key`/`goto_next_claude`/`postcard`/`delete_key` for `Pointer.cs`'s interaction switch (converted to an `if`/`else if` chain on `key.IsActionPressed(...)`). Every call site swapped 1:1 — same keys, same behavior, `dotnet build` clean before and after.

**Deliberately preserved as explicit code, not baked into the bound event**: all modifier disambiguation (Shift+T vs plain T vs Ctrl+T, Shift+B, Shift+C vs plain C, Ctrl+Alt+Delete). Godot's `IsActionPressed` ignores extra modifiers by default (`exact_match` defaults to `false`), so binding "Ctrl+T" as the event itself would risk the base `terminal_key` action firing right alongside it instead of staying mutually exclusive — each site still checks `key.CtrlPressed`/`ShiftPressed`/`AltPressed` itself, exactly as before.

**What this buys, not yet built**: `InputMap.GetActions()` is now a real, complete registry of every desktop keybind — the natural next steps (not attempted this pass, both are real UI work needing visual iteration) are (1) a rebind settings screen (`InputMap.ActionEraseEvents`/`ActionAddEvent` at runtime + a `user://keybinds.cfg` persistence layer, per the reference note), and (2) generating the `H` cheat sheet from the registry instead of hand-maintaining it — it can silently drift from the actual bindings today, and this retrofit doesn't fix that on its own, only makes it fixable cheaply.

## Code Fix — H Key Conflict: Cheat Sheet vs Reader Paging (2026-07-24)

Went looking for real keybind conflicts across the whole codebase (not just the two files touched in the InputMap retrofit above) after being told UI-navigation fixes were welcome, not just mechanism swaps. `VoiceInput.cs`'s push-to-talk `V` poll turned out to already be correctly guarded against every panel's typing-capture state (`SearchPanel.Capturing` etc.) — not a bug, verified before assuming otherwise.

**Real conflict found and fixed**: `DesktopHud.cs`'s `H`-toggles-cheat-sheet handler guarded against `SearchPanel`/`TerminalPanel`/`BrowserPanel`/`ClaudeAgent` all `.Capturing`, but not against the reader panel being open — and `Pointer.HandleReaderKeys()` polls `H` for page-up whenever `_reader.Visible` is true, completely independently. Pressing H to page up in an open note also flashed the cheat-sheet overlay open/closed every time — two unrelated things reacting to one keypress. Fixed by giving `DesktopHud` a `_reader` reference (`GetNode<ReaderPanel>("../ReaderPanel")`, same pattern it already uses for `VaultSync`/`BrainGraph`) and adding `&& !_reader.Visible` to the toggle's guard. `dotnet build` clean.

## Code Rewrite — Earth Tile LOD: shared mesh + GPU displacement (2026-07-24)

Reported by voice as "fix the Earth's red" — meant the renderer, specifically the pop/holes visible moving toward or away from the globe. Root cause in `Earth.cs`: the streamed detail-tile LOD evicted a tile the instant it fell out of the `needed` set, but its replacement was fetched over the network and mesh-built at only 4/frame — so zooming showed a visible hole where the old tile vanished before the new one was ready. Confirmed against [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization) and [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot), several of whose fixes were flagged "researched but not yet applied" in [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite). Chose the full rewrite over a small eviction-timing patch (per research, the "biggest win"). `dotnet build` clean (0 warnings, 0 errors) after all four changes below.

**Applied**:
- `Geo.CubeSphere.BuildTileGrid(seg)` — one shared unit-patch grid + baked skirt ring (COLOR.r flag), built once (lazily, static field on `Earth`), reused by every streamed tile at every LOD instead of a per-tile `SurfaceTool` build.
- `TerrainFilter.ToHeightTexture` — packs the already-filtered metre height field into a single-channel `Format.Rf` `Image` for GPU upload.
- `terrain_tile.gdshader` rewritten: vertex shader does the lat/lon→direction→displacement math that used to run per-vertex on the CPU in `BuildTilePatch`, sampling a per-tile `heightmap` texture. Fragment shader computes the shading normal via central difference of the *displaced position* (not a flat tangent-plane approximation), sampled at full heightmap resolution rather than the tile's coarse mesh. A `morph` uniform blends the height sample toward a coarser mip as a tile nears its refine threshold (0.12 screen-space error) — a practical CDLOD-style analogue for a texture-displaced grid, not a literal port of Strugar's fixed-grid vertex morph (which assumes concentric clipmap rings; ours are lat/lon quads of varying size).
- `Earth.cs`: `BuildTilePatch` is now a thin get-or-create (shared mesh + `ShaderMaterial`) plus a texture/uniform push via the new shared `ApplyTileUniforms` helper — reused for both a fresh tile and upgrading a placeholder to real data in place. `DrainTiles`'s per-frame build budget raised 4 → 16 tiles now that building is a texture upload, not a mesh rebuild. **The actual hole/pop fix**: `CreatePlaceholderTile` — when a tile is newly needed, it walks up to the nearest resident ancestor already in `_tiles` and points the new tile's material at that ancestor's *already-uploaded* textures with a cropped UV sub-rect (new `img_frac`/`img_span`/`elev_frac`/`elev_span` shader uniforms, the same trick the code already used for elevation-ancestor reuse, now extended to imagery and composed across placeholder chains). The new tile renders instantly — blurrier, upsampled from the parent — so the old coarser tile can be evicted the *same frame* with nothing left blank; when the tile's own fetch lands, `BuildTilePatch` swaps the same `MeshInstance3D`'s material over to sharp data in place (no node recreate).
- **Correctness fix caught before it shipped**: `BuildTileGrid`'s raw vertex data is a tiny (0,0,0)-(1,1,0) box, but the vertex shader moves `VERTEX` far from that to the actual sphere surface — Godot's automatic frustum-cull AABB is computed from the raw mesh, not the shader output, so every tile now gets an explicit `CustomAabb` (a generous sphere-radius box, `static readonly Aabb TileAabb`) or tiles would risk being wrongly culled while still on-screen.

**Deliberately out of scope this pass** (per the plan, to avoid stacking risk in one change): the 1-px DEM neighbour-apron edge stitch (the true ~40 m height-mismatch fix at tile seams — skirts still visually hide it as before) and reweighting the fetch-priority formula (current screen-space-error priority queue already refines nearest/largest-on-screen first; no evidence it was part of the reported symptom).

**Not yet done — needs the headset**: this is a live-rendering change with no headless test coverage. Build is clean; fly toward/away from the globe and confirm the pop/hole is actually gone and imagery/terrain still align (no black cracks, no wrongly-culled tiles) before treating this as fully done.

## Next Step

- [ ] In-headset confirmation of the Earth tile LOD rewrite (see entry above) — fly toward/away from the globe, check for holes/pops/cracks/culling glitches
- [ ] Scope MCP socket auth (token handshake)
- [ ] Prototype local-embeddings swap for SemanticIndex (see [Local Embedding Models for Semantic Search](kb://06-reference-local-embedding-models-for-semantic-search))
- [ ] Move secrets out of plaintext cfg into sops-nix
- [ ] Verify the anisotropic-filter fix actually reduces UI text shimmer in-headset, then decide if the deeper mipmap-generation pipeline is worth it
- [ ] Watch for the next ClaudeAgent failure to see what the real recurring error actually is, now that stderr surfaces
- [ ] Generate the `H` cheat sheet from `InputMap.GetActions()` instead of hand-maintained text (also closes the class of conflict just fixed, structurally)
- [ ] Build a rebind UI in SettingsPanel now that InputMap.GetActions() is a real registry
- [ ] 1-px DEM neighbour-apron edge stitching (deferred from the Earth tile LOD rewrite above)
- [ ] Move this into a proper folder (07 Projects/vr-brain) once triaged

## Related

- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [vr-brain - Overview](kb://07-projects-vr-brain-vr-brain-overview)
- [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design)
- [UI Rendering Performance in Godot](kb://06-reference-ui-rendering-performance-in-godot)
- [Godot Input Handling and Keybind Design](kb://06-reference-godot-input-handling-and-keybind-design)
- [VR Controller Input and OpenXR Action Maps](kb://06-reference-vr-controller-input-and-openxr-action-maps)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot)
- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
- [Inbox Processing](kb://00-inbox-inbox-processing)
