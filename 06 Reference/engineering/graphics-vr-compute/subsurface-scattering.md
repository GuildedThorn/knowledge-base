---
summary: "Modeling light that enters, scatters beneath, and re-exits translucent materials like skin using BSSRDF approximations."
status: active
tags: [reference, engineering, graphics, sss, bssrdf]
private: false
---

# Subsurface Scattering

## Purpose

Modeling light that enters, scatters beneath, and re-exits translucent materials like skin using BSSRDF approximations.

## Core Model

- A BSSRDF generalizes the BRDF: outgoing radiance depends on a different surface point than where light entered, capturing lateral light transport.
- Jensen et al. (2001) split transport into a single-scattering term and a dipole diffusion approximation for the dominant multiple-scattering component.
- Diffusion profiles describe how far light of each wavelength spreads; red spreads farthest in skin, giving the characteristic reddish translucency at edges and shadow boundaries.
- Absorption and reduced scattering coefficients parameterize the medium per wavelength.

## How It Works

- Texture-space diffusion renders irradiance into a UV-unwrapped light map, then convolves it with a sum-of-Gaussians approximation of the diffusion profile before lighting.
- Screen-space subsurface scattering blurs the diffuse lighting buffer in screen space, weighting by depth so blur radius tracks world-space distance; cheaper but view-dependent.
- Real skin is multi-layered (oil, epidermis, dermis); GPU Gems 3 models it with separately weighted Gaussians and a transmittance term for thin regions like ears and nostrils.

## Engineering Notes

- Separate diffuse (scattered) and specular (surface) responses; only diffuse is blurred so pores and specular highlights stay sharp.
- Blur must run in linear space, and the profile should be normalized to conserve energy.

## Sources

- Jensen et al., A Practical Model for Subsurface Light Transport (2001) - https://graphics.stanford.edu/papers/bssrdf/
- GPU Gems 3, Ch. 14: Real-Time Skin Rendering - https://developer.nvidia.com/gpugems/gpugems3/part-iii-rendering/chapter-14-advanced-techniques-realistic-real-time-skin

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
