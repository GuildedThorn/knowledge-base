---
summary: How Google Earth, Cesium/quantized-mesh, and ArcGIS/Esri solve crack-free multi-LOD terrain, DEM tile edge seams, and fast streaming — the techniques behind the vr-brain globe optimization.
status: active
tags: [reference, rendering, terrain, godot, vr-brain]
---

## Purpose

Primary-source techniques for optimizing a streamed, displaced-terrain globe (the [[Earth - Geo Engine Rewrite|vr-brain Earth]]). Answers the three problems: same-LOD tile grid, different-LOD blocky step, and streaming slowness. Compiled 2026-07-24 from Cesium source, the quantized-mesh + 3D Tiles specs, Mapzen/Mapbox DEM docs, and CDLOD.

## DEM tile edge convention (the grid seam)

- **Raster terrain tiles are area-registered ("pixel-is-area"): adjacent 256×256 tiles do NOT share an edge sample.** The 256 samples are pixel *centers*, inset half a pixel; neighbor tile x col 255 and tile x+1 col 0 are one pixel-spacing apart. **Empirically confirmed for AWS Terrarium:** adjacent tiles' shared columns differ ~40 m mean (never identical). So a per-tile mesh gets a different edge height on each side → a crease.
- **Why buffered tiles exist:** Mapzen ships 260/516 (2-px buffer) and Mapbox Terrain-DEM ships a 1-px buffer *specifically* to supply the neighbor's edge samples for meshing + normals. **But AWS `elevation-tiles-prod` only serves 256** (no buffer variant) — so you must stitch neighbor edges yourself.
- **Fix — 1-px apron:** when building a tile's DEM field, blit a 1-px border copied from the 4 neighbors' adjacent edge rows/cols → a 258×258 field; sample at `(globalPx − 0.5, globalPy − 0.5)` (area→center). Both tiles then interpolate the *same* physical pixels at the seam → identical height. Use **(N+1) vertices/side** so seam coords are integer ×256 (bit-identical positions). **Recompute normals from the apron'd field** — a normal discontinuity alone still shows a seam.
- Terrarium decode: `h = R*256 + G + B/256 − 32768` m. Stay on Terrarium PNG (Godot decodes natively); **LERC** (Esri's bounded-error float codec, `MaxZError=0.1 m` for Terrain 3D) needs a native P/Invoke lib — not worth it.

## LOD-boundary step (fine tile next to coarse tile)

- Fine and coarse tiles sample the DEM at different resolutions → genuinely different edge heights (a *step*, not just a crack). **Skirts hide sky-through-crack, NOT height disagreement.**
- **Cesium/Google use skirts** (need zero neighbor knowledge, tolerate async loading). Cesium skirt depth = `geometricError(level) × 5`, hung straight down from the edge-vertex lists, textured with the tile imagery, excluded from the bounding volume. Size skirts to the *actual* worst-case gap (a coarse cell or two), not a fixed large fraction, or they read as dark walls.
- **Kill the step at its source (better):** constrain a fine tile's edge vertices to the coarse parent's *interpolated* edge line (never sample independently at the boundary) — the CDLOD guarantee — and/or build a **consistent decimated pyramid** (coarse sample = fixed decimation of children) so parent edge == child even-index sample. Enforce a **balanced quadtree** (neighbors differ ≤1 level) so edge-stitch `step ∈ {1,2}`.
- **CDLOD geomorphing** (Strugar) — recommended for runtime-generated heightfield terrain (our case): one regular grid per node, vertex shader morphs high-LOD vertices toward parent positions over a transition band; edge vertices forced to full morph → no cracks, no popping, no skirts. Google Earth morphs (patent US9153011); Cesium hard-swaps + skirts.

## Screen-space error (LOD selection)

`SSE = geometricError · viewportHeight / (distance · 2·tan(fovY/2))`; refine to children when `SSE ≥ maxScreenSpaceError`. Cesium terrain default `maxSSE = 2` (apps raise to 16 for speed). `geometricError(z) = groundSampleDistance(z) × qualityFactor`, halving per level. Esri I3S uses the equivalent `maxScreenThreshold` (node MBS pixel diameter).

## Streaming / perceived speed (the big wins)

1. **Displace in the vertex shader from a per-tile height texture on ONE shared grid mesh.** New tile = a texture upload, not a mesh build. Removes the "heavy patch built before it appears" stall and most main-thread cost. *(Biggest Godot-side win — not yet applied in vr-brain.)*
2. **Decouple imagery from terrain** — draw imagery on the resident smooth sphere the instant it arrives; add displacement when the DEM lands. Allow imagery LOD ≠ terrain LOD.
3. **Parent-upsample "fill tiles"** — render every not-yet-loaded tile from upsampled ancestor data (imagery UVs + interpolated parent DEM) so the globe is never holed, only sharpens.
4. **Prioritize the request queue:** `priority = (1 − dot(dirToTile, viewDir)) · distance` (front-and-near first); 3 bands (blocking-refinement > visible > speculative preload); **cancel** off-frustum requests; **cap builds/uploads per frame** (time-budget). Cesium: 2–10× faster, 27–53% fewer tiles.
5. **Prefetch** a one-tile ring + keep ancestors resident.
6. **LRU tile cache** keyed by (z,x,y), sized by count/GPU-bytes, touched every frame, evict only tiles not in the current render set; + persistent disk cache of decoded tiles (Godot gets no free HTTP cache).

## Normals for lighting

Central difference of the height field: `n = normalize(vec3(hL−hR, 2·d, hD−hU))`, transformed into the sphere frame; `d` = world texel size (meters). Do it from the displacement height texture (per-pixel in fragment) for crisp lighting consistent with the geometry. Sobel (8-tap) is smoother at ~2× cost.

## Godot 4 C# threading

- Build vertex arrays (`Vector3[]`, UVs, indices, normals) on a worker thread — fine.
- **`SurfaceTool.Commit` / `ArrayMesh.AddSurfaceFromArrays` touch the RenderingServer — marshal to the main thread** (`CallDeferred`). Only that call is main-thread; the math already happened.
- Best: prebuild ONE grid mesh + index buffer per LOD, share it, displace/curve in the vertex shader from a per-tile height texture → almost no runtime `AddSurfaceFromArrays`. `MultiMesh` + a height-texture atlas collapses draw calls.

## Related

- [[Earth - Geo Engine Rewrite]] · [[High-Fidelity Planet Rendering (Godot)]] · [[Globe Data Source APIs]]
