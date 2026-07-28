---
summary: "USGS EarthExplorer and The National Map provide search, visualization, web services, and downloads for imagery, elevation, lidar, hydrography, topo maps, and national geospatial base layers."
status: active
tags: [reference, geospatial, usgs, earthexplorer, national-map, 3dep, elevation, lidar]
private: false
---

# USGS EarthExplorer and The National Map Data

## Purpose

USGS EarthExplorer and The National Map are primary U.S. public geospatial data sources. They matter for `vr-brain` Earth because they provide official elevation, imagery, lidar, hydrography, structures, transportation, boundaries, land cover, and topo-map layers.

## EarthExplorer

EarthExplorer is the USGS EROS search/download application for current and historical remote-sensing scenes and related datasets.

Key workflow:

- Define search criteria by place/address, coordinates, polygon, circle, predefined area, uploaded GeoJSON/KML/Shapefile, WRS path/row, date range, and cloud cover.
- Select datasets.
- Apply dataset-specific additional criteria.
- Inspect results, browse/footprints, compare browse imagery, export results, add to bulk download/order, and download/order scenes.
- Login is required for downloads/orders.

Useful for:

- Landsat and other historical imagery searches.
- NAIP download routing where TNM points users to EarthExplorer.
- Scene-level metadata, footprints, browse imagery, and bulk workflows.

## The National Map

The National Map is a collection of free, nationally consistent U.S. geospatial datasets. USGS describes it as including elevation from 3DEP, surface water from NHD, place names from GNIS, and continuously updated datasets for trails, roads, boundaries, structures, land cover, and imagery.

Important apps/services:

- The National Map Viewer: base-layer GIS visualization and web-map creation.
- TNM Download Client: data and map downloads.
- LidarExplorer: search/download/visualize 3DEP lidar and DEM data.
- 3DEP Elevation Viewer: visualization for DEM renderings such as hillshade, slope, aspect, contours, and tinted hillshade.
- TNM Services list: REST, WMS/WMTS, WCS, WFS, and staged product access.
- EPQS: point elevation query service returning elevation for a lat/lon in feet or meters.

## 3DEP Elevation Services

- 3DEP is the elevation component of The National Map.
- 3DEP products include lidar point clouds and DEMs at multiple horizontal resolutions.
- USGS states 3DEP products are free of charge and without use restrictions.
- The 3DEP Bare Earth DEM Dynamic service is an ArcGIS ImageServer backed by multi-resolution USGS DEM data.
- Dynamic visualization functions include hillshade, aspect, stretched hillshade, multi-directional hillshade, slope map, elevation tinted hillshade, and contours.
- WMS and WCS interfaces are enabled for interoperability.
- EPQS returns point elevation from the USGS elevation service using longitude, latitude, units, and JSON/XML output.

## Implementation Notes For vr-brain

- Use TNM/3DEP as an official elevation source candidate alongside AWS Terrarium.
- Prefer WCS or staged DEM products for numeric terrain ingestion; WMS/WMTS is better for visual overlays.
- Use EPQS for spot elevation readouts, measurement widgets, hover/click inspection, or validation.
- Add TNM layers as a source family in the GeoLayer framework: elevation, contours, hydrography, roads, boundaries, structures, land cover, topo maps, and imagery.
- Keep EarthExplorer as a manual/data-acquisition path for bulk imagery scenes rather than a realtime tile source.

## Sources

- USGS EarthExplorer - https://earthexplorer.usgs.gov/
- USGS The National Map Viewer - https://www.usgs.gov/tools/national-map-viewer
- The National Map app hub - https://apps.nationalmap.gov/
- The National Map services - https://apps.nationalmap.gov/services/
- USGS The National Map Data Delivery - https://www.usgs.gov/the-national-map-data-delivery
- USGS 3D Elevation Program - https://www.usgs.gov/3d-elevation-program
- USGS About 3DEP Products & Services - https://www.usgs.gov/3d-elevation-program/about-3dep-products-services
- 3DEP Elevation ImageServer - https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer
- EPQS - https://apps.nationalmap.gov/epqs/
- TNM 3D Viewer help - https://apps.nationalmap.gov/help/

## Related

- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Earth - Geo Engine Rewrite](kb://07-projects-vr-brain-earth-geo-engine-rewrite)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
