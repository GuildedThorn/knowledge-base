---
summary: "Design target for making vr-brain Earth behave like an immersive National Map-style viewer: searchable layers, elevation inspection, measurement, terrain profiles, and official USGS data sources."
status: active
tags: [project, vr-brain, earth, geospatial, usgs, national-map]
private: false
---

# Earth - National Map Viewer Target

## Purpose

Make `vr-brain` Earth feel like a VR/desktop-native version of The National Map viewer: official terrain/base layers, layer toggles, query/inspect, elevation profiles, measurement, and user-added geospatial data.

## Reference Behavior

The National Map viewer/help surfaces a useful product pattern:

- Widget panel for map tools.
- Basemap gallery.
- Layer list.
- Legend.
- Add Data by search or URL.
- Share/embed.
- Query operational layers.
- Measurement for area, line length, and point coordinates.
- Elevation profile for selected features or drawn lines.
- Spot elevation.
- Print/export.
- Draw/select tools.

## vr-brain Translation

- **Layer List:** expose `GeoLayerManager` layers in a real UI, not only MCP `earth_layer`.
- **Legend:** each `IGeoLayer` should optionally publish legend metadata: color ramp, symbols, units, thresholds, attribution.
- **Add Data:** support URL-backed layers for GeoJSON, WMS/WMTS, WCS, ArcGIS REST MapServer/ImageServer, and local files later.
- **Query:** clicking/pointing at a layer should return feature attributes or sampled raster/elevation values.
- **Measurement:** add great-circle distance, polyline length, polygon area, and coordinate readout.
- **Elevation Profile:** sample 3DEP/terrain provider along a drawn line and render a chart/popup.
- **Spot Elevation:** use local resident DEM first; fall back to USGS EPQS for U.S. official point elevation.
- **Basemap Gallery:** switch imagery/topo/hillshade/night/terrain styles without changing layer logic.

## Data Source Candidates

- 3DEP DEM via WCS/staged products for official U.S. terrain.
- 3DEP ImageServer/WMS for hillshade, slope, aspect, contours, tinted hillshade.
- EPQS for spot elevation validation and UI readouts.
- TNM services for hydrography, boundaries, structures, transportation, land cover, topo availability, and NAIP imagery index.
- EarthExplorer for manual/bulk imagery-scene acquisition.

## Implementation Notes

- Keep the current cube-sphere + GeoLayer framework. The National Map pattern is a UX/data-source target, not a renderer replacement.
- Add `IGeoLayer.Query(point/ray/bbox)` and `IGeoLayer.GetLegend()`.
- Add `IElevationProvider.Sample(lat, lon)` and `SampleLine(points, spacingMeters)`.
- Preserve offline/cache behavior for DEM and imagery tiles.
- Distinguish visual overlays from numeric datasets: WMS is fine for display; WCS/DEM products are needed for real terrain/profile values.
- Add attribution metadata per layer/source.

## Applied 2026-07-25

- Added `NationalMapLayer` to `vr-brain` as a first USGS/TNM runtime layer.
- Layer id: `national_map`.
- Data source: USGS 3DEP ImageServer `exportImage`.
- Default mode: `tinted_hillshade`; config can switch to `hillshade`, `slope`, or `aspect`.
- Default extent: CONUS bbox (`lat_s=24`, `lat_n=50`, `lon_w=-126`, `lon_e=-66`).
- Added layer legend metadata to `IGeoLayer` and `earth_layer list`.
- Added `UsgsElevation` EPQS client for official point elevation.
- Added MCP tool `earth_elevation(lat, lon)` returning USGS EPQS elevation in metres.
- Build verified with `nix develop -c dotnet build VrBrain.csproj`.

## Related

- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
- [USGS EarthExplorer and The National Map Data](kb://06-reference-geospatial-usgs-earthexplorer-and-national-map-data)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
