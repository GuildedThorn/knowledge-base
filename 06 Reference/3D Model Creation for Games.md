---
summary: Blender-to-Godot 4 game asset pipeline — topology, UV unwrapping, PBR texturing/channel packing, LOD generation, glTF export.
status: active
tags: [reference, gamedev, blender, godot]
private: false
---

## Purpose

The practical asset-creation pipeline for Blender (installed and in active use) → Godot 4 game-ready models — topology, texturing, and export mechanics not previously documented in the vault. Compiled 2026-07-24.

## Topology Fundamentals

- **Quads vs triangles vs n-gons**: quads subdivide predictably and deform evenly (four edges to distribute stress) — standard for anything rigged/animated. Triangles in deforming areas cause unpredictable pinching; n-gons risk shading artifacts since auto-triangulation at export can pick a bad diagonal, interpolating normals poorly. Everything triangulates at export regardless (glTF and every real-time renderer only consume triangles) — modeling in quads is a modeling-time discipline for predictable edge loops and deformation, not an export requirement.
- **Edge flow / loop cuts**: loops must run perpendicular to the bend axis at every joint (elbows, knees, shoulders, fingers; 8–12 loops around eyes/mouth for expressive faces). Poles (vertices with ≠4 edges) are unavoidable at loop terminations but belong in low-deformation areas, never on a joint or sharp corner.
- **Poly count budgets** (rough real-world triangle ranges): mobile/background prop ~500–1,000; mobile/VR hero prop or mid-importance character ~5,000–15,000 (VR needs more *modeled* geometry, not less — normal-map trickery reads poorly at HMD viewing distance, so detail that would be faked with normals on flat-screen often needs to be actual geometry); background PC/console prop ~1,000–5,000; mid-tier PC/console character ~10,000–30,000; AAA console hero character tens of thousands up to ~100,000+. Set per-project in pre-production, hero assets budgeted explicitly higher than background fill.

## UV Unwrapping

- **Seam placement**: natural silhouette breaks (under a collar, inside a sleeve) and hard feature edges (panel lines) so seams are hidden or already read as an edge. More seams (smaller islands) reduces stretching at the cost of more visible seam lines to manage.
- **Minimize stretch**: unwrap, check with a checkerboard test texture at target resolution — uniform squares = good, skewed = re-seam or use Minimize Stretch.
- **Islands and padding**: consistent texel density across islands of the same asset/atlas; 2–4px padding at target resolution between islands to prevent mip-level color bleed. >85% UV space utilization on hero assets.
- **Why it matters for streaming/mipmapping**: islands packed too close bleed neighboring pixel data once mips generate, producing seam artifacts at distance; inconsistent texel density across an asset/atlas means some parts look blurry/oversharp relative to others at the same viewing distance.

## PBR Texturing Workflow

**Standard channel set**: Albedo/Base Color, Normal (tangent-space), Roughness, Metallic, Ambient Occlusion, optionally Height/Displacement and Emissive.

**High-to-low bake**: sculpt/model detail on a high-poly, retopologize a clean low-poly game mesh over it, bake the high-poly's surface detail onto the low-poly's normal map via Cycles bake (Selected to Active) — the standard route to high-fidelity surface detail at game-ready poly counts.

**Naming convention**: `AssetName_ChannelSuffix`, e.g. `Prop_Crate_BaseColor.png`, `Prop_Crate_Normal.png`, `Prop_Crate_ORM.png` — consistent suffixes let shader auto-binding infer channel purpose from filename.

**Channel packing (ORM)**: pack Occlusion/Roughness/Metallic (each naturally single-channel grayscale) into R/G/B of one texture instead of three — cuts texture memory and reduces fetches per pixel from 3 samples to 1, meaningfully helping fill-rate-bound mobile/VR rendering. **glTF 2.0's spec uses R=Occlusion, G=Roughness, B=Metallic** — convenient since Godot imports glTF natively, so packing to glTF's ORM order round-trips correctly. Free packing tools exist, or do it manually in Krita by copying each grayscale map into its target channel.

## LOD Generation

- **Decimation**: Blender's Decimate modifier (Collapse/ratio mode — 0.5/0.25/0.1 for successive tiers) or Limited Dissolve for hard-surface objects. Mark important edges Sharp and enable Lock Boundaries before decimating, to prevent UV seams and silhouette creases from collapsing.
- **Typical tier count**: 3–4 LOD levels — LOD0 full → LOD1 ~50% → LOD2 ~25% → LOD3/billboard at far distance.
- **Screen-size-based switching**: engines swap LOD meshes by the asset's projected screen-space size (same underlying concept as the terrain screen-space-error LOD already documented in [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization), applied per-object instead of to a continuous heightfield). Godot exposes this via `MeshInstance3D`'s `visibility_range_begin/end`.
- **Automation**: Blender add-ons like LODGen and Game Asset Optimizer now semi-automate multi-tier LOD generation with export presets for Godot/Unity/Unreal.

## Blender → Godot 4 Export

**glTF 2.0 is Godot's recommended/native format** — binary `.glb` (single file, easiest to drop in) or text `.gltf`+`.bin`+loose textures (better for version-control diffing). Collada (`.dae`) is legacy; FBX import in Godot 4.3+ uses the improved `ufbx` library.

**What glTF preserves**: PBR materials (maps directly onto Blender's Principled BSDF metallic/roughness workflow — custom node shaders are the main cause of materials breaking on export), animations (actions/NLA), full skeletons/armatures with skinning weights.

**Exporter settings that matter**: Embed Images (for `.glb`); stick to Principled BSDF; enable NLA Strips as the animation source, disable "Export all animation actions" to avoid exporting unused test actions; **apply all modifiers and Apply Scale (Ctrl+A) before export** — the single most common cause of tiny/huge/distorted imports.

**Godot's native `.blend` import** (Editor Settings → Filesystem → Import → Blender Path): Godot calls a local Blender install to convert `.blend` → glTF behind the scenes on every reimport. Fast local iteration (save in Blender, alt-tab to Godot) at the cost of requiring Blender on every teammate's machine at a known path, no Android/web editor support, and no stable baked asset in version control. Best treated as a fast local convenience, with glTF as the shipped source of truth.

## Common Beginner Mistakes

- **Non-manifold geometry**: edges shared by 3+ faces, flipped normals, duplicate faces/verts. Breaks baking, physics, and export/shading. Fix via Mesh → Clean Up and manual normal-orientation checks.
- **Non-uniform scale unapplied**: distorts normals and breaks lighting on export — always Ctrl+A → Apply → Scale (and Rotation) before export.
- **Un-triangulated n-gons**: auto-triangulation at export/render can pick a bad diagonal → pinching/dark shading, especially on curved surfaces.
- **Not applying transforms before export**: the single most common "why is my model tiny/huge/rotated in Godot" cause.

## Related

- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [Character and Object Animation Development](kb://06-reference-character-and-object-animation-development)
- [Terrain Rendering Optimization](kb://06-reference-terrain-rendering-optimization)
- [Reference Map](kb://01-maps-reference-map)
