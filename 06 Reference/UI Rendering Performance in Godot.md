---
summary: SubViewport render cost and update-mode discipline, Control layout/redraw cost, RichTextLabel/terminal-stream performance patterns — for multi-panel world-space UI apps.
status: active
tags: [reference, gamedev, godot, ui, performance]
private: false
---

## Purpose

Performance discipline for Control/SubViewport-based UI, directly relevant to running multiple simultaneous world-space panels (ReaderPanel, TerminalPanel(s), BrowserPanel(s), SearchPanel, SettingsPanel) in a VR app. Complements [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling) and [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization) rather than repeating them. Compiled 2026-07-24.

## SubViewport Rendering Cost Fundamentals

Each `SubViewport` is a fully separate render target — Godot re-renders its entire subtree (own culling, draw-call submission, fragment shading) independently of the main view, with none of the main view's stereo-instancing optimizations. Cost scales with what's inside the viewport, not the SubViewport node itself, but driver/GPU overhead per extra render target is real and platform-sensitive — web exports have reported severe degradation with multiple simultaneously-rendering 3D SubViewports even when editor/native performance was fine.

**Disproportionately expensive in VR**: the main 3D view already renders twice per frame (stereo). Every active SubViewport panel is a *third, fourth, fifth* "scene" rendered on top of that. Five simultaneously `UPDATE_ALWAYS` UI panels next to a stereo 3D world is closer to "7 renders per frame" than "1."

## SubViewport Update Modes — The Primary Lever

`SubViewport.render_target_update_mode`: `UPDATE_DISABLED`, `UPDATE_ONCE` (renders next frame then reverts to disabled), `UPDATE_WHEN_VISIBLE` (default — renders only while its `ViewportTexture` is actually being drawn on-screen), `UPDATE_WHEN_PARENT_VISIBLE`, `UPDATE_ALWAYS`. Reserve `UPDATE_ALWAYS`/`UPDATE_WHEN_VISIBLE` for genuinely continuous content (a live minimap); drive everything else via `UPDATE_ONCE` triggered from your own "content changed" event — the recommended pattern for a markdown ReaderPanel (re-render only on navigation) vs a live TerminalPanel (re-render only when new output batches in).

**Caveat**: `UPDATE_WHEN_VISIBLE` has a known regression history — non-functional in early 4.0 (a regression from 3.5, where it worked). If a panel silently stops updating when off-quad-visible-but-technically-in-tree, test actual behavior on the target Godot version rather than trusting the mode blindly; driving updates manually via `UPDATE_ONCE` is more predictable.

## Resolution vs Fill-Rate

SubViewport pixel resolution (not the quad's world-space size) drives fragment shading cost — text shaping, glyph rendering, and any shader work inside the viewport all execute per SubViewport-pixel. A panel with a large quad but a small/distant apparent VR footprint should use a correspondingly modest SubViewport resolution; oversizing burns fill-rate for zero visible legibility gain (see [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design) for the pixel-density-vs-legibility side of this tradeoff), compounding the stereo-doubling cost above.

## Control Layout and Redraw Cost

Godot's layout system is notification-driven: changing anchors/size/margins or adding/removing children triggers `queue_sort()` on the parent Container (`NOTIFICATION_SORT_CHILDREN`), which can cascade up nested Container trees — deep nesting or hundreds-to-thousands of children in one container incurs real recalculation cost during resizing. Batch UI mutations (set all properties, then trigger one layout pass) rather than one property change at a time.

Separately, `CanvasItem`/Control drawing is redraw-on-demand, not per-frame: `queue_redraw()` schedules a single `NOTIFICATION_DRAW`/`_draw()` call at idle time, coalesced even across multiple calls in one frame — canvas items don't redraw every frame by default. A static Control (SettingsPanel that only changes on user interaction) costs nothing extra just for existing, as long as nothing calls `queue_redraw()` unnecessarily.

## RichTextLabel Cost (ReaderPanel)

Real measured regressions exist across Godot versions: clearing/resetting `.text` every frame is roughly **5x slower** than it should be (`Clear()` grows more expensive with more tags present), and enabling **Fit Content** costs ~5x more to add to the tree (~3000µs vs ~560µs). Practical rules: never re-set `.text` wholesale on every minor update — only when displayed content actually changes (document navigation); avoid `fit_content` on large/dynamic labels if avoidable; enable the `threaded` property so parsing/shaping happens off the main thread (prevents stutter, doesn't reduce total cost — official docs recommend this explicitly for large text).

## Terminal Panel (ANSI/SGR → BBCode) Specifics

Two concrete, sourced patterns directly relevant:

- **Use `append_text()`, not `text +=`**: `append_text()` only parses the newly appended BBCode chunk rather than re-parsing the full accumulated buffer — critical for a panel receiving continuous process output. Note its limitation: a BBCode tag opened in one `append_text()` call can't be closed in a later call, so structure ANSI→BBCode conversion to be self-closing per batch.
- **Batch incoming lines**: coalesce multiple lines arriving in one poll/tick into a single `append_text()` call instead of one call per line — each call has fixed overhead (BBCode parse setup, layout invalidation) independent of content size, so N small calls cost more than 1 large call.
- **Cap rendered scrollback**: trim/discard old buffer content rather than letting the internal item list grow unbounded — layout costs scale with total tag/line count, a confirmed real bottleneck for console logs spanning thousands of lines.

## Multiple Simultaneous SubViewports — Budget Guidance

No official hard number, but the actionable principle: **most panels should be idle (`UPDATE_DISABLED`/`UPDATE_ONCE`-driven) most of the time; only the panel(s) actively being looked at, or with genuinely fresh streaming content (a live TerminalPanel with an active process), should run `UPDATE_ALWAYS`/`UPDATE_WHEN_VISIBLE`.** For a panel set like ReaderPanel/TerminalPanel(s)/BrowserPanel(s)/SearchPanel/SettingsPanel, a reasonable default: one "focused" panel at full update rate, all others event-driven/`UPDATE_ONCE`. Given VR's stereo doubling, treat each concurrently-`UPDATE_ALWAYS` SubViewport as roughly comparable in frame-budget weight to a full extra eye-render of a moderately complex scene — **2-3 concurrently "hot" panels is a reasonable soft ceiling** before it becomes a real budget line item.

## VR-Specific Note: Composition Layers

For world-space UI in OpenXR specifically, sampling a SubViewport onto a 3D quad in the normal scene incurs lens-distortion resampling that degrades UI text legibility. `OpenXRCompositionLayerQuad` offloads presentation of the SubViewport directly to the XR runtime where supported, improving quality and — since the runtime handles compositing rather than the app's render loop — potentially reducing app-side compositing cost. Worth evaluating for whichever panel is always-visible/focused.

## Related

- [Game CPU Performance and Profiling](kb://06-reference-game-cpu-performance-and-profiling)
- [GPU and Rendering Optimization](kb://06-reference-gpu-and-rendering-optimization)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [Godot UI Architecture and Control Nodes](kb://06-reference-godot-ui-architecture-and-control-nodes)
- [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Reference Map](kb://01-maps-reference-map)
