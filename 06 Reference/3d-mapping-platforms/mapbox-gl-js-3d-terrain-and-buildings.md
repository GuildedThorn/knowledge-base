---
summary: "Mapbox GL JS renders dynamic browser maps with vector styles, raster DEM terrain, hillshade, custom layers, and 3D building/polygon extrusions."
status: active
tags: [reference, geospatial, mapbox, webgl, 3d-terrain, 3d-buildings]
private: false
---

# Mapbox GL JS 3D Terrain and Buildings

## Purpose

Mapbox GL JS is a browser/WebGL mapping platform for dynamic client-side maps. It is strongest when the goal is custom styled web visualization with terrain, vector overlays, extrusions, and interaction.

## Core Model

- Maps render client-side from sources plus style layers.
- Supported source types include vector, raster, raster-dem, GeoJSON, image, and video.
- Product positioning: Mapbox GL JS is the web map renderer in the Mapbox platform; docs connect it to Mapbox maps, mobile SDKs, Studio, Static Maps, Tiling Service, Search, Navigation, and data products.
- 3D terrain uses a `raster-dem` source and `map.setTerrain`.
- Hillshade layers render DEM-based terrain shading client-side.
- 3D buildings and custom polygon prisms use `fill-extrusion` layers.
- Mapbox Standard style includes 3D buildings by default; older classic-style examples manually add building extrusions from vector tiles.

## Terrain Data

- Mapbox Terrain-DEM v1 is a Mapbox-provided global elevation raster tileset.
- It stores raw elevation values in PNG RGB channels.
- It underpins 3D terrain rendering in Mapbox GL JS and Mapbox mobile SDKs.
- Elevation decode formula from docs: `height = -10000 + ((R * 256 * 256 + G * 256 + B) * 0.1)`.
- Mapbox notes that elevation sources may use different vertical datums, so precise normalization to one datum can be inaccurate.

## Building / Extrusion Model

- `fill-extrusion` renders polygons/multipolygons as 3D prisms.
- Height/base/color/opacity can be data-driven from feature attributes.
- Useful for building visualization, indoor floorplans, choropleths extruded by value, and lightweight urban context.

## Strengths

- Fast browser-native 2D/3D vector-map rendering.
- Strong styling and data-driven visualization model.
- Easy overlay of GeoJSON/vector/raster sources.
- Broad developer surface: API docs, examples, style specification, GitHub source, quickstarts, Studio/design tooling, and Mapbox Tiling Service.
- Good for dashboards, interactive web products, and thematic 3D maps.

## Constraints

- Not a full photogrammetric 3D mesh platform like Google Photorealistic 3D Tiles.
- 3D buildings are mainly vector/extrusion/model-style visualizations, not continuous captured reality meshes.
- Terrain-DEM access is SDK-oriented and subject to Mapbox account/token/licensing.

## Sources

- Mapbox GL JS product page - https://www.mapbox.com/mapbox-gljs
- Mapbox Docs - https://docs.mapbox.com/
- Mapbox GL JS docs - https://docs.mapbox.com/mapbox-gl-js/
- Mapbox docs - Work with sources and layers - https://docs.mapbox.com/mapbox-gl-js/guides/styles/work-with-layers/
- Mapbox example - Display buildings in 3D - https://docs.mapbox.com/mapbox-gl-js/example/3d-buildings/
- Mapbox example - Extrude polygons for 3D indoor mapping - https://docs.mapbox.com/mapbox-gl-js/example/3d-extrusion-floorplan/
- Mapbox Terrain-DEM v1 tileset - https://docs.mapbox.com/data/tilesets/reference/mapbox-terrain-dem-v1/
- Mapbox Tiling Service docs - https://docs.mapbox.com/mapbox-tiling-service/

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
