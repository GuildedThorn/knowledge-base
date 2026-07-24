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

## Next Step

- [ ] Scope MCP socket auth (token handshake)
- [ ] Prototype local-embeddings swap for SemanticIndex (see [Local Embedding Models for Semantic Search](kb://06-reference-local-embedding-models-for-semantic-search))
- [ ] Move secrets out of plaintext cfg into sops-nix
- [ ] Verify the anisotropic-filter fix actually reduces UI text shimmer in-headset, then decide if the deeper mipmap-generation pipeline is worth it
- [ ] Move this into a proper folder (07 Projects/vr-brain) once triaged

## Related

- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [vr-brain - Overview](kb://07-projects-vr-brain-vr-brain-overview)
- [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design)
- [UI Rendering Performance in Godot](kb://06-reference-ui-rendering-performance-in-godot)
- [Inbox Processing](kb://00-inbox-inbox-processing)
