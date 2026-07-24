---
summary: Master plan for the vr-brain Earth rewrite — a from-scratch cube-sphere planet engine + a pluggable GeoLayer data framework for ADSB, weather, winds, heat, cyber threats, WiGLE, pins, and more, on desktop and VR.
status: active
tags: [project, vr-brain, godot, rendering, geospatial]
---

## Purpose

Rewrite the vr-brain Earth "from the bottom up" for the highest fidelity practical in Godot 4 C#, with a pluggable data-layer framework so any geospatial dataset can be added, usable on both desktop and VR. Decided 2026-07-24.

## Summary

Two parts, built together:
1. **Cube-sphere planet engine** — from-scratch, chosen over draped-slippy-tiles (poles) and 3D-Tiles/Cesium-ion (dependency/billing). Real orbit-to-surface, WGS84, real terrain relief.
2. **GeoLayer framework** — decouple data *Source* from render *Layer* (Cesium/deck.gl model). Every feature (ADSB, NWS, radar, winds, heat, cyber, WiGLE, pins, quakes, fires) is a `IGeoLayer` on the globe. This is the backbone that makes "much more" trivial.

**Decisions:** render core = cube-sphere from scratch. API keys = free-tier OK (WiGLE, abuse.ch Auth-Key, OpenWeatherMap, Mapbox — pasted into `vr-brain.cfg`). First data layers = all four groups (weather, cyber, winds+heat, natural events). Refs: [[High-Fidelity Planet Rendering (Godot)]], [[Globe Data Source APIs]].

## Architecture

- **`Geo`** — WGS84 constants; `Vector3d`; geodetic↔ECEF (Bowring); lat/lon↔unit-dir (keeps existing texture convention so pins align); cube→sphere COBE warp.
- **`CubeSphere`** — builds a per-face cube-sphere `ArrayMesh` (COBE-warped, equirect UVs, normals). Base for the LOD quadtree.
- **`GeoGlobe`** (replaces `Earth` internals; keeps its public API as a drop-in) — cube-sphere surface with per-face **chunked-LOD quadtree** driven by screen-space error `SSE = geomError·H/(dist·2tan(fovy/2))`; per-chunk streaming imagery (GIBS/EOX free); **floating-origin + rescaled units** for precision (Godot `precision=double` is unusable in C#); hull-sphere atmosphere scattering; UTC subsolar sun + day/night + night lights. Exposes `IGeoGlobe` (SurfaceRoot, LatLonToLocal, RadiusMeters, RequestGoto) + hosts `GeoLayerManager` + shared clock.
- **`IGeoLayer` / `GeoLayerManager`** — `OnAdd/OnRemove/Process/Pick`, visibility/z-order, data-driven styling. Sources fetch on worker threads → queue → main-thread apply (existing discipline), query by bbox+zoom+time.
- **Interaction** — one unified model for desktop mouse + VR controllers: hover→pick→act, trackball rotate, dive-zoom, god's-eye grab. Comfort: miniature god's-eye globe, teleport/snap-turn (godot-xr-tools).
- **MCP** — keep `earth_pin`/`earth_pins`; add `earth_goto`, `earth_layer` (toggle/list).

## Roadmap

- **Phase 0 — Foundation ✅:** `Geo.cs`, `Vector3d.cs`, `CubeSphere.cs`, `GeoLayer.cs` framework. Compiles; old Earth kept running.
- **Phase 1 — Cube-sphere renderer ✅ (core):** cube-sphere base mesh swapped in for the UV sphere (`CubeSphere.BuildGlobe`), pole-correct + uniform density; `earth.gdshader` now samples imagery per-fragment from surface direction (no seam, topology-independent); sun-aware scattering atmosphere (`atmosphere.gdshader`, blue lit-limb → orange terminator → faint night, fed world-space sun). Existing streaming imagery + layers unchanged and working. **Precision insight:** the globe is a *miniature* object in the constellation, not true-scale — so **floating origin is unnecessary** (absolute coords stay small, no jitter), and the chunked-LOD quadtree's payoff is terrain relief, so it moves to Phase 4.
- **Phase 2 — Framework wiring ✅ (core):** `Earth` implements `IGeoGlobe` + hosts `GeoLayerManager` (process/pick/toggle, `_ExitTree` cleanup). MCP tools `earth_goto` (fly-to, frames a place from outside + faces it via `XRRig.GotoLookAt`) and `earth_layer` (list/on/off) added. **Fixed:** cube-sphere back-face winding (terrain was invisible from outside — culled — while fine from inside); verified from orbit. Still TODO: port legacy pins/aircraft/threats onto the framework; unified pick→hover readout; settings-panel toggles.
- **Phase 3 — New layers:** Four archetypes proven & verified live from orbit — **polygons** (`WeatherAlertsLayer`, NWS ✅), **points** (`QuakesLayer`, USGS pulsing ✅), **rasters** (`RadarLayer`, NEXRAD WMS ✅), **arcs** (`CyberThreatLayer`, DShield top-attacker IPs → GeoLite2 → animated attack-map arcs, no key ✅). **Global flights ✅:** Flights got a `[flights] mode` — `global` (OpenSky `/states/all` worldwide, optional free OAuth2 creds `opensky_client_id/secret`, ~1500-cap) or `radius` (adsb.lol). Perf: global's 1500 contacts thrashed the GPU via per-plane trail meshes (→20 fps); fixed by auto-disabling trails in global mode + capping visible labels to 80 (→145 fps). **Future scale:** move darts to `MultiMesh` for thousands. Remaining: FIRMS fires (free MAP_KEY); abuse.ch Feodo/ThreatFox C2 (free Auth-Key); WiGLE wardriving (free key); Winds+heat (GFS particles — GRIB decode offline). Each is now a ~1-file layer on a template.
- **Phase 3 layers — COMPLETE (8 live, all verified from orbit):** weather_alerts, quakes, radar, cyber_threats (DShield + optional Feodo), fires (FIRMS, needs `[firms] map_key`), wigle (needs `[wigle] api_name/token`), wind (Open-Meteo global streaks ✅), heat (GIBS LST shell ✅, off by default — toggle via earth_layer). Key-gated layers self-disable cleanly ("layer idle") until keys are pasted. `heat.gdshader` added (direction-sampled shell). ~93 fps with everything on; per-layer toggles via `earth_layer` MCP tool.
- **Phase 4 — Fidelity + polish:** **Terrain relief ✅** — AWS Terrarium elevation (no key) displaced onto the detail tiles: `[earth] terrain_layer/terrain_exaggeration(=5, fixed)/terrain_max_zoom`. Fixed (zoom-independent) exaggeration so LOD neighbours agree on edge heights (per-zoom exaggeration tore black cracks). `earth_goto` arrives oblique so relief reads.
  - **DEM signal processing ✅** (`TerrainFilter.cs`): zero-phase **biquad notch** (destripe) + **windowed low-pass** (Hann/Hamming/Blackman/Lanczos) + **bilinear reconstruction** — replaced blocky nearest-neighbour. `[earth] terrain_window/terrain_smooth/terrain_notch*`.
  - **Hill-shading ✅** (`terrain_tile.gdshader` + per-vertex central-difference normals): terrain now catches light (was flat/unshaded); sun fed via a **global shader uniform** `earth_sun_obj`. Gentle contrast so per-tile normal seams stay faint.
  - **Caching/perf ✅:** raw tiles disk-cached (verified 0 re-downloads on revisit); **in-memory processed-DEM cache** (filter once, reuse across shared ancestors + rebuilds); patch subdivision 24→16; `DrainTiles` throttled to 4 builds/frame (no hitches); fetch concurrency 6→12.
  - **Researched but NOT yet applied** (see [[Terrain Rendering Optimization]]): 1-px **neighbour-apron edge stitching** (removes the faint tile grid at its source — the DEM 1-px mismatch); **vertex-shader displacement from a per-tile height texture on a shared grid mesh** (biggest streaming win — new tile = texture upload, not mesh build); **imagery/terrain decouple + parent-upsample fill-tiles** (never-holed, progressive sharpen); **request prioritisation** (`(1−dot)·dist`, cancel off-frustum, per-frame budget); **CDLOD geomorphing** (zero-pop LOD).
- **Non-terrain remaining (optional):** settings-panel toggle rows per layer (today via `earth_layer` MCP); port legacy pins/aircraft/threats onto the framework; `MultiMesh` darts (thousands); Hillaire scattering; MSAA/VRS-XR + xr-tools comfort; hover-to-read on layers.

## Config (planned `[earth.*]` / per-layer sections in vr-brain.cfg)

Free keys: `[wigle] api_name/api_token`, `[abuse_ch] auth_key`, `[owm] api_key`, `[mapbox] token`. Each layer: `enabled`, refresh, source-specific params. Center/home shared with `[flights]`/`[threat]`.

## Related

- [[High-Fidelity Planet Rendering (Godot)]]
- [[Globe Data Source APIs]]
- [[vr-brain - Overview]]
