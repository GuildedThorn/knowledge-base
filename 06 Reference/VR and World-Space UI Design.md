---
summary: Diegetic UI design for VR — SubViewport-to-quad pixel density, real PPD/legibility numbers, laser vs poke interaction, panel ergonomics, text-rendering gotchas specific to VR.
status: active
tags: [reference, gamedev, godot, ui, vr]
private: false
---

## Purpose

vr-brain already implements several world-space UI panels (`ReaderPanel`, `TerminalPanel`, `BrowserPanel`, `SearchPanel`, `SettingsPanel` — all SubViewport-rendered onto 3D quads, driven by a laser-pointer `Pointer` system) that grew organically with no documented design reference. This note is that reference — professional diegetic/VR UI principles with real citable numbers. Compiled 2026-07-24.

## Diegetic vs Non-Diegetic UI in VR

**Diegetic**: UI that exists as an object within the 3D world's own space — exactly the SubViewport-on-a-quad panels already built, behaving like physical screens the user can walk around, grab, reposition. **Non-diegetic**: rendered outside the world's diegesis, classically a camera-locked screen-space HUD. A third category, "spatial UI," floats and follows the player but isn't a world object.

**Why diegetic wins in VR**: camera-locked UI is a well-documented comfort hazard — it doesn't respect natural head parallax, reads as "smeared on the inside of the lens," and is a common vergence/fixed-focal-plane mismatch trigger. Unity's own VR guidance explicitly avoids Screen Space rendering paths for VR for this reason.

**Where non-diegetic is still legitimate**: brief system feedback without needed object permanence — loading spinners, transient toasts, and *minimal* persistent utility readouts (small, low-contrast, near the visual periphery, not demanding fixation). vr-brain's own architecture already validates this split correctly: `DesktopHud` (title/sync, clock/FPS, aim readout, cheat-sheet) is explicitly desktop-only, never instantiated in the XR rig — the right call per this guidance. `FpsHud` (a `Label3D` on the camera, shown in both rigs) is the one legitimate non-diegetic exception already present — a single small readout, not a full HUD, consistent with "minimal persistent overlay only."

## The SubViewport-to-Quad Technique

A `Control`-tree renders into a `SubViewport` at a fixed pixel resolution; the resulting `ViewportTexture` applies as an unshaded/albedo texture on a `MeshInstance3D` quad sized in world-space meters. **The ratio of SubViewport pixel resolution to quad world size is the effective pixel density.** Meta's Spatial SDK formalizes this exact tradeoff: panels sized by DP-per-meter (default **500 dp/m**, ~20% scaling headroom) or fixed DPI (default **288**) or literal pixel dimensions. Meta caps recommended texture resolution near Quest 3's own eye-buffer size (**2064×2208px**) — exceeding it wastes memory/fill-rate since headset optics can't resolve more than the eye buffer anyway. Unity XR community guidance for small world-space canvases: push dynamic pixel density up (100-300) rather than default settings, since desktop-density scaling under-resolves at typical VR panel sizes.

## Readable Text Size and Viewing Distance

**Angular resolution (PPD) of 2025-2026 headsets**: Quest 3 ≈ **25 PPD** (up from Quest 2's 20); Pico 4 Ultra ≈ **22 PPD**; Apple Vision Pro ≈ **34 PPD**; Varjo XR-4 ≈ **51 PPD** (enterprise outlier). A desktop monitor at normal viewing distance is typically **50-60+ PPD** — consumer VR is roughly **2-3x lower angular resolution**, so text needs proportionally more angular size for equal legibility.

**Concrete numbers**: minimum readable font angular size ≈ **1.33°** (≈2.32cm character height at 1m — equivalent to a 16px phone font scaled to that angle); comfortable/recommended size ≈ **3.45°** (≈6.04cm at 1m). Academic work on flat vs curved canvases found mean comfortable character sizes of **~20.6-23.8dmm** depending on device/curvature. Don't place informational content closer than **0.5m** or farther than **~20m**.

**Practical implication**: a desktop-density UI (12-14px body text designed for ~60cm monitor viewing) shrunk onto a small VR quad falls well under the 1.33° legibility floor unless the panel is physically large or placed close. Target roughly **20-40 characters per line** in VR panels — shorter than typical desktop wrap widths — to keep character angular size comfortable without oversized panels.

## Interaction Models

**Ray/laser** (already built) is Meta's standard technique for **far-field** targets — controller-friendly, distance-independent, no hand-tracking dependency. Meta ships `OVRHand.PointerPose` as the canonical ray origin/direction so pointing stays consistent across apps.

**Poke/direct-touch**: reserved for **near-field** targets within arm's reach; Meta's guidance is index-finger-contact-only for the least ambiguous gesture. Feels embodied but constrains placement to arm's-reach distances and needs hand tracking or precise controller-collision volumes.

**Hybrid pattern (recommended)**: raycast for targeting at a distance, pinch/trigger for selection; reserve poke for panels deliberately placed within reach (a settings panel pulled close). Since VR pointing lacks a desktop mouse's pixel precision, **clear hover/highlight feedback is mandatory** — buttons need a visibly distinct hover state (glow/scale/color) triggered well before the exact click boundary, since users can't fine-tune aim like nudging a mouse.

## Panel Placement and Ergonomics

Concrete numbers converge across sources: primary UI at **~0.75m minimum** (avoids eye-strain from excessive convergence) up to ~10m for strongest stereo depth cueing (usable to ~20m for less critical content); practical everyday sweet spot **0.5-1.5m**, arm's length. Vertically, center panels **slightly below true eye level** — natural gaze rests slightly downward. Keep important interactive UI inside a forward-facing cone of roughly **±30° from horizontal**, within a **~40-60° comfortable no-head-turn arc**, to avoid repeated large head/neck rotations.

**Flat vs curved**: a flat quad viewed off-axis suffers keystone/perspective distortion at its edges, worse as panel width grows relative to viewing distance. Curving toward the viewer (cylindrical wrap) mitigates this — standard for wide panels (a wide BrowserPanel or multi-pane layout). For the existing single-purpose panels (ReaderPanel, TerminalPanel), staying narrow enough that edge distortion stays negligible is simpler than adding curvature; curving only pays off once panel width exceeds a comfortable single-glance arc.

## Text Rendering Gotchas for SubViewport UI in VR

**MSAA is the wrong tool for UI text** — it only smooths geometric edge coverage, not font glyph rasterization (Godot's own docs note MSAA does not affect font antialiasing; that's a separate concern — font hinting/subpixel AA, or SDF/MSDF font rendering via `FontFile`'s `multichannel_signed_distance_field`). Godot 4.2+ has/had a known bug where setting `msaa_2d` on a `SubViewport` to anything but disabled **corrupts or freezes the rendered contents** — so the existing "MSAA 4x, never TAA" 3D-scene guidance should **not** be blindly applied inside UI SubViewports. 2D MSAA is a distinct project setting from 3D MSAA; for SubViewport-driven quads it's generally safer left off, relying on font AA/SDF and quad-texture filtering instead.

**Mipmaps on the quad texture**: `ViewportTexture` does **not** generate mipmaps by default (a documented, still-open gap) — quads viewed at distance or a shallow angle alias/shimmer badly, and this is *worse in VR* because head movement constantly re-triggers the shimmer rather than it being static. Workarounds: force mipmap regeneration on texture update (`Image.generate_mipmaps()`), or supersample the SubViewport and let trilinear filtering smooth it (simpler, costs fill-rate — matters since VR already renders ~2x for stereo). Apply `TEXTURE_FILTER_LINEAR_WITH_MIPMAPS` or anisotropic filtering to the quad's material once mipmaps exist — the standard fix for shallow-angle shimmer.

## Related

- [Godot UI Architecture and Control Nodes](kb://06-reference-godot-ui-architecture-and-control-nodes)
- [UI Rendering Performance in Godot](kb://06-reference-ui-rendering-performance-in-godot)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Reference Map](kb://01-maps-reference-map)
