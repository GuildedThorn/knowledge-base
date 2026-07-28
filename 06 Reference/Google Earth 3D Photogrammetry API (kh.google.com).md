## Purpose

Scoping reference for a possible high-fidelity terrain/building-mesh source for the [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite), from [retroplasma/earth-reverse-engineering](https://github.com/retroplasma/earth-reverse-engineering) (archived 2022, read-only, MIT-style license). It decodes Google Earth's undocumented 3D satellite-mode API — actual textured photogrammetry meshes (terrain **and** buildings), not a heightmap-displaced grid like the current AWS Terrarium pipeline. Live-checked 2026-07-24: `kh.google.com/rt/earth/PlanetoidMetadata` still returns a real `application/x-protobuffer` response, so the endpoint is alive despite the client repo being unmaintained for ~4 years.

## Protocol

- **Base:** `https://kh.google.com/rt/{planet}/{resource}` (`planet` = `earth`, `mars`, etc.)
- **`PlanetoidMetadata`** — root call, returns the initial epoch/version to seed the octree walk.
- **`BulkMetadata/pb=!1m2!1s{octant_path}!2u{epoch}`** — metadata for a batch of octree nodes (child existence, versioning) under `octant_path`.
- **`NodeData/pb=!1m2!1s{octant_path}!2u{epoch}!2e{texture_format}(!3u{imagery_epoch})!4b0`** — the actual mesh + texture payload for one octree node. `texture_format` selects JPG vs CRN-DXT1 (exact codes are in the repo's `rocktree_decoder.h`, not restated in the README — read the source before implementing).
- Everything is protobuf (schema: `rocktree.proto` in the repo) wrapped in an octree: `PlanetoidMetadata` → `BulkMetadata` (per octant) → `NodeData` (per leaf). No documented rate limits, headers, or auth — it's the same endpoint the Google Earth web/app client calls, unversioned and unofficial.

## Payload format

- **Mesh:** packed XYZ (quantized, octant-local), UV, per-vertex octant mask (which child octant a vertex belongs to, for seamless LOD stitching), normals. Reference decode logic: `rocktree_decoder.h` + `rocktree.proto` in the repo (C++, also compiled to WASM there).
- **Textures:** JPG (trivial — Godot decodes natively) or CRN-DXT1 (Crunch-compressed DXT1 — no native Godot/.NET decoder; would need a ported/bound Crunch decompressor, or just always request the JPG texture format to sidestep it entirely).
- **LOD:** octree depth, not a slippy `{z}/{x}/{y}` grid — conceptually parallel to this project's own chunked-LOD quadtree (see [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite) Phase 4), but the *leaf payload is real mesh geometry* (so it can resolve overhangs, building facades, bridges — a heightfield structurally cannot).

## Integration sketch, if pursued

1. Hand-parse the small protobuf wire format needed (varint/tag) — or add the `Google.Protobuf` NuGet — to decode `PlanetoidMetadata`/`BulkMetadata`/`NodeData`; port field layout from `rocktree.proto`.
2. New parallel tile system (not a drop-in to `TerrainFilter`/the height-displaced `terrain_tile.gdshader` grid): each resident node builds its own `ArrayMesh` from the decoded vertices/UVs/normals, textured from the JPG payload — closer to `BuildTilePatch`'s job today, but building real geometry per node instead of uploading a heightmap onto a shared grid.
3. Request JPG-only texture format to avoid writing a CRN-DXT1 decoder for a first pass.
4. Gate behind its own `[earth] mesh_terrain` config flag, off by default, so it doesn't touch the working AWS Terrarium path.
5. Rough effort: multi-session project, not a quick layer — new protobuf decode, new mesh-tile streaming/eviction path parallel to the existing one, new octant↔lat/lon math (the octree isn't lat/lon-aligned like the existing quadtree).

## The actual blocker: not effort, ToS/stability

Every other data source this project uses is a **documented, public, free-tier (or free-key) API** (ArcGIS World Imagery, AWS Terrarium, NASA GIBS/FIRMS, USGS, NWS, DShield, WiGLE) — the [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite) decisions log explicitly chose the from-scratch cube-sphere over Cesium-ion partly to dodge exactly this kind of dependency/ToS risk. `kh.google.com/rt/` is neither documented nor issued a key for — it's the private endpoint the real Google Earth clients call, reverse-engineered with no Google involvement. Risks: could be blocked/changed without notice (no deprecation notice, unlike a real API), and using a reverse-engineered private endpoint outside the Google Earth client is a materially greyer ToS position than every other source in this project. **Recommendation:** worth a small offline prototype (fetch + decode one node, confirm the mesh looks right) before committing real engineering time, and keep it behind an opt-in flag / clearly labeled as experimental if it ever lands — don't treat it as a peer of the documented sources above.

## Prototype status — `~/Documents/EarthRt` (started 2026-07-24)

Built the recommended offline prototype, deliberately **outside vr-brain**: spawned from [vr-base](kb://07-projects-vr-brain-vr-brain-overview)'s own `new-project.sh` template (`~/Documents/vr-base/new-project.sh EarthRt`), so it's a standalone git repo with the standard vr-base desktop/XR rig, not a vr-brain module. Ground-truth source pulled into `EarthRt/reference/` (not hand-waved from the README): `rocktree.proto`, the JS exporter (`decode-resource.js`, `decode-texture.js`, `get-url.js`, `convert-lat-long-to-octant.js`, `utils.js`, `dump_obj.js`), and the C++ client's `rocktree_decoder.h`/`rocktree_types.h` from the actual retroplasma repo.

**Implementation** (`EarthRt/src/Rocktree/`):
- `Wire.cs` — minimal hand-rolled proto2 wire-format reader (varint/tag/length-delimited/fixed32), not a full protobuf library.
- `RocktreeTypes.cs` — `NodeKey`/`NodeMetadata`/`BulkMetadata`/`PlanetoidMetadata`/`RtTexture`/`RtMesh`/`RtNodeData`, parsed directly against `rocktree.proto`'s field numbers.
- `MeshDecode.cs` — ports of `unpackVertices`/`unpackTexCoords`/`unpackIndices` from `rocktree_decoder.h` (delta-coded byte planes for position/UV, a varint-delta-coded generalized triangle strip for indices). Known simplification: skips the octant-mask/layer-bounds filtering and the oct-encoded normals decode that the real client does — renders every non-degenerate triangle in the strip, flat-shaded.
- `RocktreeClient.cs` — fetches `PlanetoidMetadata` → walks `BulkMetadata` looking for the first data-bearing node (`NODATA` flag bit 8 clear), descending into child bulks via flag bit 4 (named `LEAF` in the .proto, but per the JS reference's `hasBulkMetadataAtIndex` it actually means "this entry points at a deeper `BulkMetadata` to fetch" — the opposite of the intuitive reading, verified against `utils.js`).
- `EarthRtMain.cs` — orchestrates the fetch, builds a Godot `ArrayMesh` (position via `matrix_globe_from_mesh` applied exactly as `dump_obj.js`'s `writeMeshOBJ` does, re-centered on the mesh's own centroid since raw coords are ECEF-scale meters and would blow float precision), applies the JPG texture, adds it to the scene.

Wired into `EarthRt/scenes/Main.tscn` as a sibling node to the template's `XRRig`, so `F5`/`godot --path . scenes/Main.tscn` runs it directly — desktop fallback (WASD+mouse) works with no headset, matching the vr-base template's own defaults.

**Where it's at:** builds clean (0 errors). `PlanetoidMetadata` fetches and parses correctly — **hand-verified byte-for-byte**: response is 13 bytes (`0a 06 10 f4 07 28 f4 07 15 84 6d c2 4a`), decodes to `root_node_metadata{epoch:1012, bulk_metadata_epoch:1012}` + `radius≈6.37e6` (real Earth radius in meters, confirms the float decode is correct). Root `BulkMetadata` (path `""`, epoch 1012, fetched via `BulkMetadata/pb=!1m2!1s!2u1012`) is 3780 bytes; the first node entry (path `2051`) hand-decodes to a genuinely valid, data-bearing node (`NODATA` bit clear) — confirming the walk logic *should* find real data immediately. But the original `BulkMetadata.Parse` tried to fully drain the whole 3780-byte buffer before returning (as a correct generic protobuf parser must), and hit an `IndexOutOfRangeException` partway through — some later node entry doesn't match the assumed field layout and desyncs the byte offset. Made the parser resilient (wrapped the field loop in try/catch, stops cleanly and keeps every entry parsed before the failure point instead of throwing the whole response away) rather than root-causing the exact desync byte, since the first entry already has the data needed. Rebuilt clean; relaunched to confirm live, but the actual decoded mesh has **not yet been visually confirmed on screen** — that's the next thing to check.

**To resume:** `cd ~/Documents/EarthRt && nix develop -c godot --path . scenes/Main.tscn`, watch the console for `EarthRt:` log lines (or check `/tmp/earthrt2.log` if re-run with the same redirect pattern used during development). If a mesh still doesn't appear: check whether `RocktreeClient.FindDataNode` actually returns now that `BulkMetadata.Parse` degrades gracefully, then check whether `EarthRtMain.BuildMeshNode` builds a non-empty triangle list (it logs vertex/triangle counts either way). If the geometry looks wrong (inside-out, exploded, wrong scale) once something renders, the likely culprits are the skipped octant/layer-bounds filtering or a transpose/column-order mistake in the `matrix_globe_from_mesh` application (currently ported verbatim from `dump_obj.js`, unverified against real coordinates).

## Related

- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
