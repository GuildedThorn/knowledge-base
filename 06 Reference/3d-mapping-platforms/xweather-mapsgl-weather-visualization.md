---
summary: "Xweather MapsGL is a WebGL weather mapping SDK for animated, client-rendered weather layers across Mapbox GL, MapLibre GL, Google Maps, and Leaflet."
status: active
tags: [reference, geospatial, weather, xweather, mapsgl, webgl, visualization]
private: false
---

# Xweather MapsGL Weather Visualization

## Purpose

Xweather MapsGL is a specialized weather visualization SDK. It is relevant when the map/globe needs animated radar, satellite, alerts, forecasts, particles, contours, grids, or other weather layers without building the full weather-rendering stack from scratch.

## Core Model

- MapsGL is a browser-side graphics library using WebGL.
- It integrates with third-party map libraries including MapLibre GL, Mapbox GL, Google Maps, and Leaflet.
- A map controller adapts MapsGL to the host map implementation.
- Data sources are loaded and cached separately from layers.
- Layers are styled renderings of data sources.
- Built-in weather layers can be added by layer code and customized client-side.

## Data Sources

- `raster`: static raster imagery such as satellite or aerial imagery.
- `vector`: vector tiles with points, lines, and polygons.
- `geojson`: feature collections with geometry and attributes.
- `encoded`: gridded binary/raster data encoded into one or more image color bands.

## Layer Render Types

- `raster`: static imagery.
- `fill`: vector polygons.
- `line`: vector polygon/polyline outlines.
- `circle`: vector point circles.
- `symbol`: point images, glyphs, or custom GLSL shaders.
- `sample`: sample encoded data and colorize by color scale.
- `grid`: render sampled gridded data as symbols.
- `contour`: render isolines from sampled encoded data.
- `particle`: render vector data such as wind or ocean currents as flow fields.
- `heatmap`: render point-density surfaces.

## Weather Layer Coverage

The product page describes 70+ weather layers, 360-degree globe view, 10+ rendering types, and historical/realtime/forecast horizons. Example layer families include alerts, lightning, convective outlooks, road weather, hail threats, wind particles, snow depth, and cyclones.

## Strengths

- Purpose-built weather rendering rather than generic map overlay rendering.
- Client-side animation and styling control.
- Works with existing web map stacks instead of forcing a single base-map provider.
- Useful reference model for `vr-brain` weather layers: encoded data, color scales, particles, contours, timeline, legends, and data inspection.

## Constraints

- Requires an active Xweather Weather API and Maps subscription.
- Best fit is web applications; a native Godot integration would use it as architecture/reference rather than a direct SDK.
- Weather data licensing, attribution, and caching rules need review before production use.

## Sources

- Xweather MapsGL product page - https://www.xweather.com/products/mapsgl
- Xweather MapsGL documentation - https://www.xweather.com/docs/mapsgl
- Xweather MapsGL weather layers documentation - https://www.xweather.com/docs/mapsgl/weather-layers
- Xweather MapsGL GitHub project - https://github.com/aerisweather/mapsgl

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Mapbox GL JS 3D Terrain and Buildings](kb://06-reference-3d-mapping-platforms-mapbox-gl-js-3d-terrain-and-buildings)
