---
summary: "Physically based rendering models materials and light with energy-aware parameters such as base color, roughness, metallic, normals, and environment lighting."
status: active
tags: [reference, engineering, graphics, pbr]
private: false
---

# PBR Materials and Lighting

## Purpose

Physically based rendering models materials and light with energy-aware parameters such as base color, roughness, metallic, normals, and environment lighting.

## Core Model

- PBR separates material properties from lighting so assets respond consistently across environments.
- Common metallic/roughness workflows encode base color, metalness, roughness, normal, ambient occlusion, and emissive maps.
- Image-based lighting and tone mapping are major contributors to believable results.

## Engineering Notes

- Keep units, exposure, color space, and texture import settings consistent across the asset pipeline.
- Avoid painting lighting into albedo textures unless the style requires it.
- Validate materials under multiple lighting environments, not only the author's scene.

## Sources

- Filament PBR documentation - https://google.github.io/filament/Filament.html
- glTF 2.0 PBR material model - https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#materials
- Godot PBR materials - https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
