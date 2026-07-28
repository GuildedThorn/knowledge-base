---
summary: "Eagleview provides high-resolution aerial imagery, property measurements, AI-derived attributes, reports, APIs, and 3D/property intelligence workflows."
status: active
tags: [reference, geospatial, aerial-imagery, property-data, eagleview, photogrammetry]
private: false
---

# Eagleview Aerial Imagery and Property Intelligence

## Purpose

Eagleview is a geospatial/property-intelligence provider rather than a generic web-map renderer. It is relevant when the need is high-resolution aerial imagery, property measurements, roof/building reports, post-disaster imagery, government GIS support, insurance workflows, solar planning, or property-data APIs.

## Core Model

- Imagery products include high-resolution orthogonal and oblique aerial imagery.
- Eagleview markets 1-inch GSD imagery for high-detail property and infrastructure analysis.
- Property intelligence combines imagery, measurements, AI-derived attributes, reports, and software/API delivery.
- Developer resources expose APIs for report ordering, proposals/materials lists, visualizations, property evaluation, claims, imagery viewing, and map updates.

## Data / Product Areas

- Imagery: 1-inch GSD imagery, Reveal, Vault.
- Data and insights: Eagleview Data and Eagleview AI.
- 3D models and measurements: residential/commercial reports and measurement products.
- Software/delivery: Eagleview One, Cloud Connect, Explorer, MyEagleview, integrations, and developer APIs.

## Technical Concepts

- **GSD**: Ground Sample Distance, the ground area represented by one image pixel; lower GSD means higher spatial detail.
- **Orthogonal imagery**: top-down imagery useful for maps, measurements, and basemaps.
- **Oblique imagery**: side-angle imagery useful for roof faces, facades, and context not visible from straight down.
- **Property data API**: structured access to measurements, imagery, and property attributes in machine-readable formats such as JSON/XML.
- **Photogrammetry / 3D models**: high-resolution imagery can be processed into measurable 3D renderings/models.

## Strengths

- Strong property-level resolution and measurement workflow.
- Useful for roof, insurance, solar, government assessment, emergency management, utilities, and asset-management workflows.
- Developer/API surface exists for custom integrations.
- More appropriate for property intelligence than general basemap rendering.

## Constraints

- Commercial platform; access generally requires account, contract, or product purchase.
- Not a drop-in replacement for Cesium/Mapbox-style interactive map rendering.
- Coverage, recency, API permissions, caching, and derivative-use rights need contract review.

## Project Notes

- For `vr-brain`, Eagleview is more likely a property-detail/imagery data source than a global terrain renderer.
- Best candidates: property inspection mode, high-resolution urban/property overlays, damage-assessment layers, roof/solar analysis, or government GIS workflows.
- Treat as a paid/proprietary data source with licensing review before implementation.

## Sources

- Eagleview homepage - https://www.eagleview.com/
- Eagleview Developer - https://developer.eagleview.com/
- Eagleview 1-Inch Imagery - https://www.eagleview.com/product/1-inch-imagery/
- Eagleview Government solutions - https://www.eagleview.com/industry/government/
- Eagleview blog - Property Data API - https://www.eagleview.com/blog/eagleview/property-data-api/
- Eagleview blog - Aerial Mapping - https://www.eagleview.com/blog/aerial-mapping/

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Esri ArcGIS Pro 3D GIS](kb://06-reference-3d-mapping-platforms-esri-arcgis-pro-3d-gis)
