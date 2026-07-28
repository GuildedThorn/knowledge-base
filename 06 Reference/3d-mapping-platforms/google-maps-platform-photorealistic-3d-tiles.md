---
summary: "Google Maps Platform Photorealistic 3D Tiles exposes Google's textured 3D real-world mesh through the Map Tiles API for compatible 3D Tiles renderers."
status: active
tags: [reference, geospatial, google-maps-platform, 3d-tiles, photogrammetry, 3d-mapping]
private: false
---

# Google Maps Platform Photorealistic 3D Tiles

## Purpose

Google Maps Platform Photorealistic 3D Tiles is the official documented way to access Google's high-fidelity 3D real-world mesh for custom immersive applications.

## Core Model

- Product: Google Maps Platform **Map Tiles API**.
- 3D product: **Photorealistic 3D Tiles**.
- Data: textured 3D mesh of real-world buildings, landmarks, terrain, and natural surroundings.
- Format/workflow: provide a root tileset URL to a compatible 3D Tiles renderer.
- Example renderer: CesiumJS.
- Authentication: Google Cloud project, billing, Map Tiles API enabled, API key.

## Access Pattern

- Root tileset URL pattern: `https://tile.googleapis.com/v1/3dtiles/root.json?key=YOUR_API_KEY`
- Renderer fetches subsequent tiles as the camera explores the scene.
- Google docs state a single root tileset request permits at least three hours of tile requests before a new root request is needed.
- Renderer must support copyright attribution display.

## Strengths

- Highest-fidelity off-the-shelf global urban mesh among these options.
- Official API avoids the ToS/stability risk of reverse-engineered `kh.google.com` Google Earth endpoints.
- Compatible with existing 3D Tiles renderers instead of requiring custom mesh protocol reverse engineering.
- Useful for urban planning, context visualization, digital twins, location storytelling, and immersive real-world scenes.

## Constraints

- Requires Google Cloud billing/API key.
- Licensing and Maps Platform policies govern usage, caching, attribution, and derivative works.
- Photorealistic coverage is broad but not universal; Google product pages currently describe 3D coverage across 49+ countries.
- It is a rendered/visualization mesh source, not an editable GIS system of record.

## Project Notes

- For `vr-brain`, this is the safer peer to the existing reverse-engineered `kh.google.com` note.
- If high-fidelity real-world mesh becomes a target, prototype against the official 3D Tiles endpoint first.
- Use CesiumJS or a 3D Tiles loader as a reference implementation before attempting Godot-native ingestion.

## Sources

- Google Developers - Map Tiles API overview - https://developers.google.com/maps/documentation/tile/overview
- Google Developers - Photorealistic 3D Tiles - https://developers.google.com/maps/documentation/tile/3d-tiles
- Google Maps Platform - Map Tiles product page - https://mapsplatform.google.com/maps-products/map-tiles/

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Google Earth 3D Photogrammetry API (kh.google.com)](kb://06-reference-google-earth-3d-photogrammetry-api-kh-google-com)
- [CesiumJS 3D Geospatial Visualization](kb://06-reference-3d-mapping-platforms-cesiumjs-3d-geospatial-visualization)
