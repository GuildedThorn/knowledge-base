---
summary: "ArcGIS Pro is an enterprise 3D GIS authoring and analysis platform built around local/global scenes, scene layers, I3S, editing, geoprocessing, and ArcGIS publishing."
status: active
tags: [reference, geospatial, gis, esri, arcgis, 3d-mapping]
private: false
---

# Esri ArcGIS Pro 3D GIS

## Purpose

ArcGIS Pro is the enterprise-grade 3D GIS option: it is strongest when 3D visualization must remain connected to authoritative GIS data, editing, analysis, geoprocessing, and ArcGIS Online/Enterprise publishing.

## Core Model

- 3D work is organized as **scenes**.
- **Global scenes** are for earth-scale geographic context and WGS84/CGCS 2000-style global display.
- **Local scenes** are for smaller extents, projected coordinate systems, local measurement, editing, below-surface analysis, and engineering/site workflows.
- 3D data is published and consumed through **scene layers** optimized for large 3D datasets.
- Scene layers use Esri's **I3S** format and are cached with LODs for performance.

## 3D Layer Types

- 3D object scene layers: modeled objects such as buildings, often from multipatch/CAD-style sources.
- Building scene layers: BIM-derived buildings and subcomponents.
- Integrated mesh scene layers: continuous textured reality meshes from imagery/photogrammetry or sensor capture.
- Point scene layers: large symbolized point datasets.
- Point cloud scene layers: LiDAR or dense point-cloud visualization.
- Voxel layers: multidimensional volumetric data such as atmospheric, oceanic, or geological datasets.

## Integrated Mesh Notes

- Integrated mesh captures terrain, buildings, trees, cliffs, and other real-world features as a textured continuous mesh.
- It is generally used for citywide or area-scale reality mapping.
- It can supersede the ground and basemap in a scene.
- It is normally not restyled like vector/building layers; it is more like a captured reality surface.
- ArcGIS Pro supports modification workflows such as clip, mask, and replace for integrated mesh/3D Tiles layers.

## Strengths

- Authoritative enterprise GIS workflow.
- Strong desktop editing, analysis, measurement, and geoprocessing.
- Supports many 3D GIS data types, not just visualization meshes.
- Good fit for managed organizations with ArcGIS Online/Enterprise.

## Constraints

- Heavier platform and licensing model than web-only/open-source stacks.
- Best results assume ArcGIS ecosystem adoption.
- Less appropriate if the goal is only lightweight browser rendering or custom game-engine integration.

## Sources

- ArcGIS Pro docs - Scenes - https://doc.esri.com/en/arcgis-pro/latest/help/mapping/map-authoring/scenes.html
- ArcGIS Pro docs - What is a scene layer? - https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/what-is-a-scene-layer-.html
- ArcGIS Pro docs - Integrated mesh scene layer - https://doc.esri.com/en/arcgis-pro/latest/help/mapping/layer-properties/the-integrated-mesh-scene-layer-in-arcgis-pro.html
- Esri Developer - IntegratedMeshLayer web scene specification - https://developers.arcgis.com/web-scene-specification/objects/integratedMeshLayer/

## Related

- [3D Mapping Platforms - Index](kb://06-reference-3d-mapping-platforms-3d-mapping-platforms-index)
- [Globe Data Source APIs](kb://06-reference-globe-data-source-apis)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
