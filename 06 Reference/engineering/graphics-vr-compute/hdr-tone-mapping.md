---
summary: "Compressing high-dynamic-range linear radiance into displayable range with photographic and filmic operators."
status: active
tags: [reference, engineering, graphics, hdr, tonemap]
private: false
---

# HDR Tone Mapping

## Purpose

Compressing high-dynamic-range linear radiance into displayable range with photographic and filmic operators.

## Core Model

- Rendering computes linear radiance over an unbounded range; a tone-mapping operator maps it into the [0,1] displayable range before encoding.
- Exposure scales scene luminance first, emulating a camera aperture/shutter; auto-exposure derives the scale from average or log-average scene luminance.
- Eye adaptation smooths the exposure scale over time toward the current scene key, avoiding abrupt brightness jumps.
- Operators split into global (one curve for the whole frame) and local (spatially varying) forms; real-time engines favor global for cost.

## Operator Families

- Reinhard: `L/(1+L)` maps all values into [0,1); the extended variant preserves a chosen white point to avoid over-desaturating highlights.
- Filmic (Hable/Uncharted 2) uses a shoulder-and-toe curve giving photographic contrast and gentle highlight rolloff.
- ACES filmic approximations are a de facto standard, matching film-stock response and neutral color under saturation.
- After tone mapping, apply the display transfer function: sRGB gamma (~2.2) or the PQ/HLG curve for HDR displays.

## Sources

- Reinhard et al., Photographic Tone Reproduction (2002) - https://dl.acm.org/doi/10.1145/566654.566575
- LearnOpenGL: HDR - https://learnopengl.com/Advanced-Lighting/HDR
- Hable, Filmic Tonemapping Operators - http://filmicworlds.com/blog/filmic-tonemapping-operators/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
