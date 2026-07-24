---
summary: VR-specific performance discipline — frame budget math, reprojection, foveated rendering, single-pass stereo, MSAA vs TAA, motion-to-photon latency, comfort tradeoffs.
status: active
tags: [reference, gamedev, godot, vr, performance]
private: false
---

## Purpose

VR-specific performance methodology that applies regardless of what's being rendered — complements [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization) and vr-brain's own rendering notes (already at MSAA 4x/no-TAA, teleport+snap-turn, comfort vignette, ~93-145fps desktop headroom). Compiled 2026-07-24.

## Why VR Frame Budgets Are Categorically Stricter

| Refresh rate | Frame budget |
|---|---|
| 90Hz (most WiVRn targets) | 11.1ms |
| 120Hz | 8.3ms |
| 144Hz | 6.9ms |

That's render budget only — compositor, scan-out, and (for a network-streamed setup like WiVRn) network transport all eat the same window on top. The failure mode differs qualitatively from flat-screen: a dropped VR frame means the image doesn't match where the vestibular system says the head just went — that mismatch, not mere visual quality, is a proximate cause of simulator sickness. Frame budget is a hard real-time constraint here, not a quality slider — headroom above the floor exists specifically to survive worst-case scenes without borrowing from it.

## Reprojection / (Asynchronous) Timewarp

When the app misses its deadline, the runtime re-projects the last successfully rendered frame using fresh head-tracking data instead of freezing.

- **Rotational reprojection (Timewarp/ATW)**: cheap 2D image warp for rotation only — no new geometry, no positional correction. Handles head-turn well; doesn't correct for translation (leaning) or moving objects, which stay stuck where they were rendered, producing visible swim.
- **Positional/Spacewarp-style reprojection**: extrapolates motion from the last two rendered frames (optionally aided by depth + motion vectors) to synthesize a new in-between frame, correcting for translation and animating objects too. Fundamentally extrapolation/guesswork — more artifact-prone (smearing, edge warping, misjudged occlusion on fast foreground motion). Godot 4.6 added frame-synthesis support (runtime consumes app-supplied depth + motion vectors).
- **Discipline point**: reprojection is a safety net against a hard freeze, not a substitute for hitting frame rate. It still looks/feels worse than a real frame, especially for content moving independently of the head (comets, orbiting bodies, crew — exactly the case it handles worst). Treat sustained reliance on it as a regression to fix, not a feature to lean on.

## Foveated Rendering

Exploits eye acuity falloff — sharp vision confined to the ~5° foveal cone, peripheral vision far lower-resolution.

- **Fixed Foveated Rendering (FFR)**: static pattern, full detail centered on the lens (no eye tracking needed), reduced resolution/shading rate toward the periphery. Works on any headset. Meta's own figures: ~15-25% GPU time saved at FFR level 2, 30%+ at level 4 — the safe default for headsets without eye tracking (Quest 3/3S have none).
- **Dynamic/eye-tracked (ETFR)**: moves the high-detail region to wherever the eye actually points, allowing far more aggressive peripheral reduction — needs eye-tracking hardware (Quest Pro, Varjo Aero, PSVR2) and low tracking-to-shading latency so the fovea doesn't outrun the high-detail patch. Exposed in OpenXR mainly via vendor extensions on `XR_FB_foveation`.
- **Godot 4.6/4.7**: added Vulkan Variable Rate Shading-based foveation on Android/mobile Vulkan (previously desktop-Vulkan/OpenGL-Android only) plus **Quad View rendering** (splitting each eye into an inner high-res + outer low-res viewport pair — the standard technique underlying foveation on tile-based mobile GPUs); 4.7 added Vulkan subsampled images to improve it further. Exposed as `Viewport.vrs_mode = VRS_XR` + an OpenXR foveation level. **Known interaction to check**: foveation combined with post effects (Glow/bloom, DOF) without MSAA/FXAA can visibly degrade to low-res-everywhere — worth validating directly against vr-brain's bloom-heavy cosmos visuals (corona, prominences, nebula) before assuming foveation and glow compose cleanly.

## Stereo Cost and Single-Pass/Multiview Rendering

Naive two-eye rendering means two full render passes: two full scene-graph traversals, two full draw-call sets, double CPU submission overhead. Fragment cost genuinely scales ~2x (both eyes' pixels shaded), but CPU overhead doesn't have to. **Single-pass instanced/multiview**: the engine or GPU driver issues each draw call once and instances it to both eye viewpoints in the same pass, using a per-instance view index for the correct matrix in the vertex stage — roughly halves CPU-side draw-call submission and traversal cost. Multiview (Vulkan `VK_KHR_multiview`, used by Godot's Forward+/Mobile renderers) is the driver-level variant, needing less engine-side bookkeeping than hand-rolled single-pass-instanced.

**Shader-authoring consequence** (already reflected in vr-brain's rendering note): shaders must be multiview-safe — indexed off `VIEW_INDEX`/per-view `EYE_OFFSET`, not a single assumed camera. Screen-space techniques and camera-facing billboards that ignore per-eye projection break or mismatch between eyes if not handled per-view.

## MSAA vs TAA in VR

Confirms the existing rendering note's stance, with the mechanism: **TAA** accumulates samples *across frames*, reprojecting previous frames via motion vectors — works well on flat screens where camera motion between frames is small and predictable. VR head rotation is fast and far less predictable frame-to-frame (300+ deg/s is real), across two independent frustums simultaneously — TAA's motion-vector estimate breaks down, producing ghosting/smearing exactly where the motion-sensitive periphery would catch it. **MSAA** samples multiple sub-pixel positions *within* a single frame — no temporal history, no motion-vector dependency to get wrong. Costs more GPU memory/bandwidth per frame, but quality doesn't degrade with head-motion speed, which is the property VR needs. Standard reason essentially all VR engine guidance defaults to MSAA and treats TAA as flat-screen-only.

## Motion-to-Photon Latency

The real perceptual metric — time from a physical head movement to the corresponding photons landing on the display, not raw fps. Comfort threshold (John Carmack's 2013 Oculus latency work): **under ~20ms** end-to-end for the mismatch to become largely imperceptible; above ~50ms reads as sluggish; beyond ~60ms is a recognized sickness driver. Pipeline contributors: sensor/tracking sampling → app render time (the frame-budget math above — the piece the engine directly controls) → compositor/runtime overhead → display scan-out → **network transport**.

The last is specific to a network-streamed setup like WiVRn/Monado, unlike a wired headset: WiVRn compresses (typically H.265, with 10-bit and foveated-encoding options) and streams the rendered frame over Wi-Fi, then streams tracking data back. H.265 encode alone adds roughly 3ms; Wi-Fi introduces variable jitter/contention a tethered link doesn't have. Network conditions directly compete with render-time budget for the same 20ms envelope — a perfectly-timed 8ms render on a congested Wi-Fi channel can still blow the comfort threshold. Practical levers: WiVRn's stream-resolution/foveated-encoding defaults (50% stream resolution by default in recent versions, tunable), bitrate ceiling (up to ~200Mbit/s on clean Wi-Fi), keeping the streaming link on uncontended 5/6GHz.

## Comfort-Driven Design Decisions

Some "performance" choices are really comfort decisions that happen to also be cheap:

- **Locomotion model**: continuous smooth locomotion couples directly to frame-time stability — any dip or reprojection event during continuous self-motion is one of the strongest known nausea triggers (visual motion the vestibular system doesn't corroborate, worsened by stutter). **Teleport + snap-turn** (the actual choice here, 30-45° increments) sidesteps the problem structurally — no continuous visual motion to desync from vestibular input, so a frame drop during a teleport/snap is far less provocative than one during smooth flight. This is why teleport/snap-turn is the industry-wide default comfort recommendation, not a stylistic choice — it moves the problem out of the performance-sensitive path entirely.
- **Comfort vignette on smooth motion**: narrowing effective FOV during motion reduces peripheral optical-flow stimulation, the main driver of vection-induced discomfort — a cheap shader-side mitigation that buys tolerance for the smooth-motion fly-where-you-look path used alongside teleport.
- **General principle**: given a frame-budget miss is inevitable occasionally even in a well-optimized app, *what's on screen* during that miss matters — a reprojection glitch during a static/teleported view is nearly unnoticeable; the same glitch during continuous smooth self-motion or fast independent object motion (the case reprojection handles worst) is the exact worst-case comfort scenario. Choose locomotion and effects with this asymmetry in mind, not raw fps targets alone.

## Related

- [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization)
- [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling)
- [High-Fidelity Planet Rendering (Godot)](kb://06-reference-high-fidelity-planet-rendering-godot)
- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [VR Setup](kb://10-hobbies-vr-setup)
- [Reference Map](kb://01-maps-reference-map)
