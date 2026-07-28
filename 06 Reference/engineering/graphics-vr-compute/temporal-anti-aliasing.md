---
summary: "Jittering samples across frames and reprojecting history to accumulate supersampling over time."
status: active
tags: [reference, engineering, graphics, antialiasing, temporal]
private: false
---

# Temporal Anti-Aliasing (TAA)

## Purpose

Jittering samples across frames and reprojecting history to accumulate supersampling over time.

## How It Works

- Each frame offsets the projection by a subpixel jitter (often a Halton sequence) so successive frames sample different positions within a pixel.
- Motion vectors reproject the previous frame's accumulated color into the current frame, aligning history despite camera and object motion.
- The current sample is blended with the reprojected history (an exponential moving average), effectively accumulating many samples per pixel over time.
- Under static conditions this converges toward high-quality supersampling at roughly one sample per pixel per frame.

## Engineering Notes

- Stale or wrong history causes ghosting and trails; neighborhood color clamping/clipping rejects history that falls outside the current pixel's local color range.
- Disocclusions, transparency, and shading that changes without motion vectors are common failure sources requiring per-case handling.
- The blend weight trades stability against responsiveness: heavier history is smoother but blurs and lags; lighter history flickers.
- A sharpening pass often compensates for the softening TAA introduces.

## Sources

- Karis, High Quality Temporal Supersampling (SIGGRAPH 2014) - https://advances.realtimerendering.com/s2014/
- Yang et al., A Survey of Temporal Antialiasing Techniques - https://onlinelibrary.wiley.com/doi/10.1111/cgf.13973

---
## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
