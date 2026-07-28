---
summary: "OpenEarth.Online is a commercial Earth/Pano Studio service for searching, fetching, and exporting 3D earth tiles and panoramas for AI, CG, BIM, simulation, and digital-twin workflows."
status: active
tags: [reference, geospatial, 3d-mapping, mesh, photogrammetry, openearth]
private: false
---

# OpenEarth.Online 3D Mesh Export

## Purpose

OpenEarth.Online is a commercial workflow for downloading and exporting 3D Earth mesh tiles and panorama data into common DCC/BIM/game formats. It is relevant as a practical asset-export path for AI training, robot simulation, CG, BIM, Unreal/Blender workflows, and digital-twin visualization.

## Core Model

- Product areas: **EarthStudio** for 3D tiles and **PanoStudio** for panoramic images.
- Workflow: register, define/search a target region, fetch tiles/panos, export into downstream formats.
- EarthStudio exports 3D tiles/meshes with original-resolution texture.
- PanoStudio exports panoramic images with metadata such as camera latitude, longitude, elevation, and Euler angles.
- The site markets use cases including machine learning, robot simulation, CG, BIM, and twin visualization.

## Export / Format Notes

- EarthStudio lists export support for `GLTF`, `OBJ`, `FBX`, `STL`, and `DAE`.
- PanoStudio lists JPEG export with original metadata.
- Pricing tiers constrain tile balance, search area size, merge/export capability, and street-view download counts.
- The FAQ states that users do not need a Google API token.

## Fit For vr-brain Earth

- Useful as an offline asset acquisition/prototyping source, not as the primary runtime streaming architecture.
- Candidate workflow: use exported city/area meshes as test fixtures for Godot import, LOD experiments, Nanite/Unreal comparison, or ML/simulation datasets.
- Treat licensing, source provenance, allowed derivative use, and redistribution as unresolved until reviewed.
- Do not conflate with official Google Maps Platform Photorealistic 3D Tiles; this is a separate commercial exporter-style service.

## Constraints / Risks

- Commercial account/subscription model.
- Coverage and regional restrictions may apply.
- Terms, licensing, caching, and data provenance require review before project integration.
- Not a documented open geospatial service endpoint for live application streaming.

## Sources

- OpenEarth.Online homepage - https://www.openearth.online/
- OpenEarth.Online EarthStudio - https://www.openearth.online/earthstudio
- OpenEarth.Online PanoStudio - https://www.openearth.online/panostudio

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Google Maps Platform Photorealistic 3D Tiles](kb://06-reference-3d-mapping-platforms-google-maps-platform-photorealistic-3d-tiles)
- [Google Earth 3D Photogrammetry API (kh.google.com)](kb://06-reference-google-earth-3d-photogrammetry-api-kh-google-com)
- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
