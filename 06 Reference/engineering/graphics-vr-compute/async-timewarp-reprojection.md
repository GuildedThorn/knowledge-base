---
summary: "Re-projecting the last rendered frame to the latest head pose so VR keeps hitting display refresh despite frame drops."
status: active
tags: [reference, engineering, graphics, timewarp, reprojection]
private: false
---

# Asynchronous Timewarp and Reprojection

## Purpose

Re-projecting the last rendered frame to the latest head pose so VR keeps hitting display refresh despite frame drops.

## Core Model

- Timewarp resamples an already-rendered eye buffer using a newer head-pose reading taken just before scanout.
- Orientation-only warp applies a rotational homography, correcting yaw/pitch/roll with negligible cost and no depth data.
- Positional (space) warp additionally shifts pixels by translation using a depth buffer, correcting for head movement.
- The goal is to shrink motion-to-photon latency independently of the application's render rate.

## How It Works

- Synchronous timewarp runs after the app finishes a frame; asynchronous timewarp runs on a separate high-priority GPU context.
- When the app misses its frame budget, async timewarp re-projects the previous frame to a fresh pose, sustaining display refresh (e.g. 90 Hz).
- Warping is done per-scanline or in tiles to account for rolling-shutter and beam-racing timing on the panel.

## Engineering Notes

- Disocclusion holes appear where positional warp exposes surfaces the original frame never rendered; edges are stretched or inpainted.
- Positional data (moving objects, animation) is not corrected by orientation-only warp, producing judder on in-world motion.
- Async timewarp masks dropped frames but is a safety net, not a substitute for hitting native frame rate.

## Sources

- Meta: Asynchronous Timewarp Examined - https://developers.meta.com/horizon/blog/asynchronous-timewarp-examined/
- van Waveren, The Asynchronous Time Warp for VR on Consumer Hardware (2016) - https://dl.acm.org/doi/10.1145/2993369.2993375

## Related

- [Graphics, VR, and GPU Compute - Index](kb://06-reference-engineering-graphics-vr-compute-graphics-vr-compute-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
