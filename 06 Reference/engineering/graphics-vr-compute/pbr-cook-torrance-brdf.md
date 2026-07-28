---
summary: "The microfacet reflectance model with normal distribution, geometry, and Fresnel terms underlying modern PBR shading."
status: active
tags: [reference, engineering, graphics, brdf, microfacet]
private: false
---

# Physically Based Rendering and the Cook-Torrance BRDF

## Purpose

The microfacet reflectance model with normal distribution, geometry, and Fresnel terms underlying modern PBR shading.

## Core Model

- Cook-Torrance treats a surface as a field of microscopic mirror facets whose orientation distribution defines its roughness.
- The specular BRDF is `DGF / (4 (N·V)(N·L))`, combining a normal distribution D, geometry G, and Fresnel F term.
- D (e.g. GGX/Trowbridge-Reitz) gives the fraction of facets aligned with the halfway vector, controlling highlight shape.
- G models self-shadowing and masking of facets; F gives the angle-dependent fraction of light reflected versus refracted.

## Key Ideas

- The metallic-roughness workflow parameterizes materials by base color, metalness, and roughness rather than ad-hoc constants.
- Metals reflect specularly with tinted F0 and no diffuse; dielectrics have a low ~0.04 F0 plus a diffuse lobe.
- Energy conservation requires reflected diffuse plus specular energy never exceed incident energy, unlike legacy Phong shading.
- Fresnel is commonly approximated with Schlick's equation, cheaply interpolating reflectance toward 1.0 at grazing angles.

## Engineering Notes

- Consistent PBR inputs let assets look correct across lighting environments and image-based lighting probes.
- GGX is favored for its long, physically plausible highlight tails matching measured real-world materials.
- Roughness typically maps to the GGX alpha as roughness squared for perceptually linear artist control.

## Sources

- Cook & Torrance, A Reflectance Model for Computer Graphics (1982) - https://dl.acm.org/doi/10.1145/357290.357293
- LearnOpenGL: PBR Theory - https://learnopengl.com/PBR/Theory
- Google Filament PBR - https://google.github.io/filament/Filament.html

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
