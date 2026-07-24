---
summary: Techniques for a Google-Earth-VR-quality planet in Godot 4 C# — cube-sphere chunked LOD, screen-space error, WGS84 math, floating-origin precision, atmosphere scattering, VR specifics, and existing open-source projects.
status: active
tags: [reference, godot, rendering, vr, vr-brain]
---

## Purpose

Rendering research for the [[vr-brain - Overview|vr-brain]] Earth rewrite ([[Earth - Geo Engine Rewrite]]). Target: high-fidelity globe, orbit-to-surface, flat-screen + OpenXR VR, Vulkan Forward+, AMD. Compiled 2026-07-24.

## Geometry & LOD

- **Two topologies:** (a) **cube-sphere / quad-sphere** — 6 faces, each a chunked-LOD quadtree; uniform triangle density (with warp), reaches poles, clean 3D-distance LOD; needs cube→sphere area correction + Web-Mercator reprojection for imagery. (b) **draped slippy tiles** (z/x/y on curved patches) — consumes the whole map/terrain tile ecosystem free, but Web Mercator clips at ±85.05° so **cannot cover poles** + polar slivers. **Verdict: cube-sphere for a real planet; draped tiles only as a fast imagery path.** (Cesium terrain uses geographic EPSG:4326 two-root quadtree to reach poles.)
- **Screen-space error (refinement driver):** each tile has `geometricError` (m). `SSE = geometricError·viewportHeight / (distance·2·tan(fovy/2))`. Refine to children when `SSE > maxScreenSpaceError` (default ~16; VR wants slightly higher for perf; lower = sharper/slower). `distance` = to closest point on tile bounding volume.
- **Cube→sphere warp:** naive `p/|p|` distorts; tangent warp `u'=tan(u·π/4)`; **COBE analytic** (keeps unit length): `x'=x·√(1−y²/2−z²/2+y²z²/3)` (and cyclic).
- **Chunked-LOD literature:** Ulrich Chunked LOD (SIGGRAPH 2002); Losasso/Hoppe Geometry Clipmaps; **Strugar CDLOD** (quadtree + vertex-shader geomorphing, `github.com/fstrugar/CDLOD`) — geomorphing + skirts hide LOD cracks.

## WGS84 ellipsoid

Needed for **data alignment** (all GNSS/GIS is WGS84; draping on a sphere → tens-of-km error mid-latitude), even if the mesh looks near-spherical. Constants: `a=6378137.0`, `b=6356752.3142`, `f=1/298.257223563`, `e²≈0.00669438`.
- **Geodetic→ECEF:** `N=a/√(1−e²sin²φ)`; `X=(N+h)cosφcosλ`, `Y=(N+h)cosφsinλ`, `Z=(N(1−e²)+h)sinφ`.
- **ECEF→Geodetic (Bowring):** `p=√(X²+Y²)`, `θ=atan2(Za,pb)`; `λ=atan2(Y,X)`; `φ=atan2(Z+e'²b·sin³θ, p−e²a·cos³θ)`; `h=p/cosφ−N`.

## Precision (the load-bearing constraint for C#)

- float32 ULP at Earth radius ≈ 0.5 m → jitter for objects meters above surface. Godot single-precision degrades past ~32k-65k units.
- **`precision=double` Godot build is effectively unsupported with C#/.NET** (GodotSharp `Vector3` stays float; compile/runtime errors). Do NOT rely on it.
- **Strategy (recommended):** keep authoritative state in C# `double` (`Vector3d`/lat-lon-alt) *outside* the scene graph; **rescale units** (1 unit = 1 km → radius ≈ 6370 units); **floating origin** (keep camera near 0; when it drifts past a threshold, subtract offset in double from root nodes, accumulate into a running double origin); compute each node's `Transform3D` camera-relative (`float = double_world − double_origin`). This is Cesium's RTE model done app-side.

## Atmosphere & lighting

- Ground sky-dome models (Preetham/Hosek) don't give a space-viewed limb. Use: **O'Neil single-scatter** (GPU Gems 2, cheap baseline) or **Hillaire 2020** (small LUTs, PBR multiscatter) — as a spatial shader on a **slightly-larger transparent hull sphere** (render back faces, blend additively), NOT the `sky` shader. Maintained: `github.com/Zylann/godot_atmosphere_shader` (Godot 4.3+).
- **Sun direction:** compute subsolar point from UTC (NOAA General Solar Position, ±arc-min). Day/night: `smoothstep(-0.05,0.05, dot(normal,sun))` blend; night-lights as emission masked by `(1−dayFactor)`.

## VR (Godot 4 OpenXR)

- **MSAA 4x, never TAA** (TAA ghosts under head motion). `rendering/anti_aliasing/quality/msaa_3d`.
- **Foveation:** `Viewport.vrs_mode = VRS_XR` + OpenXR foveation level. **Disabled when glow/bloom/DOF active** — budget accordingly.
- **Renderer:** Mobile recommended for new XR (subsampled foveation); Forward+ fine on desktop PCVR where quality matters.
- **Stereo-safe shaders:** multiview single-pass; use `VIEW_INDEX`/`EYE_OFFSET`; avoid screen-space tricks + camera-facing billboards that ignore per-eye projection.
- **Overlays:** batch markers with `MultiMesh`. **Comfort:** a **god's-eye miniature globe** you orbit is far more comfortable than 1:1 flight; teleport + snap-turn (30-45°); comfort vignette on smooth motion. Use `github.com/GodotVR/godot-xr-tools`.

## Data sources (see [[Globe Data Source APIs]] for full list)

- **Imagery (free):** NASA GIBS MODIS TrueColor / Blue Marble; EOX Sentinel-2 cloudless (10 m, CC-BY attribution); GIBS VIIRS Black Marble (night). Avoid Esri (ToS) & Bing (retired). Mapbox (token, 750k/mo) for higher res.
- **Elevation:** **AWS Terrarium** (no account) `s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png`, decode `h=(R*256+G+B/256)−32768`. Mapbox Terrain-DEM (token) `h=−10000+(R*65536+G*256+B)*0.1`. **Formulas are not interchangeable.**

## Existing Godot projects

- **cuberact/godot-cuberact-planet-chunked-lod** — MIT, Godot 4.6, active: full Earth-radius spherified-cube quadtree LOD, GPU displacement, atmosphere, horizon culling, **origin shifting**, orbit-to-surface. Best skeleton to study.
- **Battle-Road-Labs/3D-Tiles-For-Godot** — Apache-2.0, C++ GDExtension, active: streams 3D Tiles / Cesium ion / Google Photorealistic. The only turnkey real-Earth photoreal path (callable from C#; adds Cesium ion dependency).
- **Zylann/godot_atmosphere_shader**; **ivoyager** (astronomy-accurate solar system); **Terrain3D** (flat surface detail).
- Gap: no mature "slippy-map-on-a-globe" GIS globe exists — custom work, or 3D Tiles.

## Recommended approach

Cube-sphere + per-face chunked-LOD quadtree (COBE warp, CDLOD geomorph, skirts) driven by the SSE formula; WGS84 math in C# doubles; **floating-origin + rescaled units** for precision; Terrarium elevation + GIBS/EOX imagery; hull-sphere scattering shader + UTC subsolar sun; VR = Forward+/MSAA/VRS + god's-eye globe + xr-tools. Shortcut: 3D-Tiles-For-Godot + Cesium ion for instant photoreal at the cost of a dependency.

## Related

- [[Globe Data Source APIs]]
- [[Earth - Geo Engine Rewrite]]
- [[vr-brain - Overview]]
