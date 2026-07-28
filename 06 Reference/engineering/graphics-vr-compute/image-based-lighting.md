---
summary: "Using pre-filtered environment maps to light PBR surfaces with realistic diffuse irradiance and specular reflections."
status: active
tags: [reference, engineering, graphics, ibl, environment-map]
private: false
---

# Image-Based Lighting and Environment Mapping

## Purpose

Using pre-filtered environment maps to light PBR surfaces with realistic diffuse irradiance and specular reflections.

## Core Model

- IBL treats a captured environment (typically an HDR cubemap or equirectangular panorama) as an area light surrounding the scene.
- The rendering integral is split into diffuse and specular parts, each precomputed so real-time shading is a few texture lookups.
- Diffuse irradiance is precomputed by convolving the environment over the cosine-weighted hemisphere, yielding an irradiance map sampled by surface normal.
- Specular uses Karis's split-sum approximation: a roughness-mipmapped pre-filtered environment map times a precomputed BRDF integration lookup (scale and bias).

## Engineering Notes

- Higher roughness maps to higher, more blurred prefilter mip levels, approximating the widening specular lobe.
- The BRDF LUT is indexed by view angle (N dot V) and roughness and is independent of the environment, so it can be reused across scenes.
- Low-order spherical harmonics compactly store diffuse irradiance (typically 9 coefficients), cheaper than an irradiance cubemap.
- Cubemaps favor sharp specular reflections; SH favors low-frequency diffuse and light probe interpolation.

## Sources

- LearnOpenGL: IBL Diffuse Irradiance - https://learnopengl.com/PBR/IBL/Diffuse-irradiance
- Karis, Real Shading in Unreal Engine 4 (2013) - https://blog.selfshadow.com/publications/s2013-shading-course/
- Debevec, Image-Based Lighting - https://www.pauldebevec.com/Research/IBL/

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
