---
summary: "Selection matrix for ArcGIS Pro, Google Photorealistic 3D Tiles, Mapbox GL JS, and CesiumJS."
status: active
tags: [reference, geospatial, 3d-mapping, comparison]
private: false
---

# 3D Mapping Platform Selection Matrix

## Purpose

Quick technical comparison for choosing between ArcGIS Pro, Google Maps Platform Photorealistic 3D Tiles, Mapbox GL JS, and CesiumJS.

## Matrix

| Platform | Best Fit | 3D / Geospatial Data Model | Runtime | Main Constraint |
|---|---|---|---|---|
| ArcGIS Pro | Enterprise GIS editing, analysis, publishing | I3S scene layers: 3D object, building, integrated mesh, point, point cloud, voxel | Desktop + ArcGIS Online/Enterprise ecosystem | Licensing/ecosystem weight |
| Google Photorealistic 3D Tiles | High-fidelity real-world urban mesh | OGC 3D Tiles-compatible textured photogrammetry mesh | Compatible 3D Tiles renderer, commonly CesiumJS | API key, billing, Google Maps policies |
| Mapbox GL JS | Dynamic styled web maps with terrain/building extrusions | Vector tiles, GeoJSON, raster, raster DEM, fill-extrusion | Browser/WebGL | Not full captured-reality mesh |
| CesiumJS | Open web globe and massive 3D geospatial streaming | 3D Tiles, terrain meshes, imagery layers, point clouds, photogrammetry | Browser/WebGL | Heavy scenes need careful LOD/memory management |
| Xweather MapsGL | Animated weather layers and forecast visualization | Weather layers, raster/vector/GeoJSON/encoded sources, particle/contour/grid/sample renderers | Browser/WebGL over Mapbox/MapLibre/Google/Leaflet | Subscription and weather-data licensing |
| Eagleview | Property-level aerial imagery and measurements | Orthogonal/oblique imagery, property attributes, reports, 3D models, APIs | Eagleview apps/APIs/integrations | Commercial access and derivative-use constraints |
| OpenEarth.Online | Offline 3D mesh/pano export for AI/CG/BIM/simulation | Fetched 3D tiles and panorama exports into GLTF/OBJ/FBX/STL/DAE/JPEG workflows | Web/service workflow plus DCC/game-engine import | Commercial/export licensing and provenance review |
| USGS TNM / EarthExplorer | Official U.S. elevation, imagery, lidar, topo, hydrography, and base layers | DEM, lidar, WMS/WMTS, WCS, WFS, ArcGIS REST, scene/scene-search workflows | Web apps, REST/OGC services, downloads | U.S.-focused; EarthExplorer downloads require account |

## Practical Recommendation

- For an authoritative GIS backend: **ArcGIS Pro**.
- For highest-fidelity city mesh: **Google Photorealistic 3D Tiles**, rendered through **CesiumJS** first.
- For product/dashboard maps: **Mapbox GL JS**.
- For open globe/digital-twin visualization: **CesiumJS**.
- For weather overlays: **Xweather MapsGL**.
- For parcel/property intelligence: **Eagleview**.
- For official U.S. terrain/base layers: **USGS The National Map / EarthExplorer**.
- For offline mesh fixtures/assets: **OpenEarth.Online** after terms review.
- For a Godot-native globe: use these platforms as source/architecture references, but expect custom streaming, LOD, attribution, and licensing work.

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
