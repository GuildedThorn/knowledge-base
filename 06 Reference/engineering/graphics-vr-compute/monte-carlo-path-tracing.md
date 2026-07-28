---
summary: "Solving the rendering equation by stochastically sampling light-transport paths with importance sampling."
status: active
tags: [reference, engineering, graphics, path-tracing, monte-carlo]
private: false
---

# Monte Carlo Path Tracing

## Purpose

Solving the rendering equation by stochastically sampling light-transport paths with importance sampling.

## Core Model

- The rendering equation expresses outgoing radiance at a point as emission plus an integral of incoming radiance weighted by the BRDF over the hemisphere.
- The integral is recursive and high-dimensional; Monte Carlo integration estimates it by averaging random path samples, converging as more samples accumulate.
- Path tracing traces rays from the camera, bouncing off surfaces by sampling the BRDF, and terminates paths via Russian roulette to keep the estimator unbiased.
- The estimate is unbiased: its expected value equals the true integral, so error appears as noise rather than systematic bias.

## Variance Reduction

- Importance sampling draws directions proportional to the BRDF or incoming light, concentrating samples where they contribute most.
- Multiple importance sampling (MIS) combines BSDF and light sampling with balance/power heuristics, robust across glossy and diffuse surfaces.
- Error falls as O(1/sqrt(N)) samples, so halving noise costs 4x samples; this drives long render times for clean images.
- Modern renderers pair few samples with learned or spatiotemporal denoisers (e.g. temporal accumulation, NN denoisers) for real-time use.

## Sources

- Kajiya, The Rendering Equation (1986) - https://dl.acm.org/doi/10.1145/15922.15902
- Physically Based Rendering (book, online) - https://www.pbr-book.org/
- Ray Tracing in One Weekend - https://raytracing.github.io/

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
