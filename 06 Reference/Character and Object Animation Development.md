---
summary: Skeletal animation, rigging, IK/FK, blend trees, and Godot 4's AnimationPlayer/AnimationTree system, including root motion and procedural animation.
status: active
tags: [reference, gamedev, godot, animation]
private: false
---

## Purpose

Character/object animation theory and Godot 4-specific implementation — skinning, rigging, blending, and the AnimationPlayer/AnimationTree split, plus procedural animation techniques relevant to terrain-heavy work. Compiled 2026-07-24.

## Skeletal Animation Fundamentals

A character mesh is deformed by a **skeleton** — a hierarchy of **bones** (parent-child transforms, e.g. `hip → spine → chest → shoulder → upper_arm → forearm → hand`). Each bone has a **rest pose** (bind pose), the default transform the mesh was skinned in; animation drives bones away from rest pose and the mesh follows.

**Skinning** binds each mesh vertex to one or more bones with weights (an elbow vertex might be 70% forearm, 30% upper-arm). At render time the GPU blends the vertex position through each influencing bone's current transform, weighted accordingly — **linear blend skinning**, the near-universal technique. Weight painting (done in Blender) is what prevents "candy-wrapper" twisting at joints.

**Why skeletal over shape-key (morph target) animation for characters**: shape keys store an explicit vertex-position delta per key — cost scales with mesh density and pose count, and arbitrary poses don't compose algebraically. Skeletal animation stores a handful of bone transforms per keyframe — orders of magnitude less data, reusable across meshes with the same rig (retargeting), and naturally composable (layering, blending, IK, procedural offsets all operate on bone transforms). Shape keys remain the right tool for what skeletons handle poorly — facial expressions, muscle bulge, cloth wrinkling — often used *together* with a skeleton (jaw bone for macro mouth movement, shape keys for fine detail).

## Rigging Basics: Deform Rig vs Control Rig

- **Deform rig**: the minimal bone set that actually influences vertices via skinning — kept lean for performance and clean weighting.
- **Control rig**: an animator-facing layer on top, relevant once hand-animating extensively (not required for procedural/mocap-driven work): IK handles/targets (draggable proxies that solve the deform chain), custom bone shapes/widgets for easier viewport selection, and constraints (copy rotation, limit rotation, stretch) that make the rig harder to pose wrong. Control-rig bones are typically **not** exported for game skinning — only deform bones are baked to the game engine.

Blender's **Rigify** add-on auto-generates a full control+deform rig pair — the standard shortcut. **Mixamo** remains the fastest path to a usable humanoid deform rig + mocap library if hand-rigging isn't the goal.

## IK vs FK

- **FK (Forward Kinematics)**: pose each joint down the chain in order (shoulder → elbow → wrist); the hand's position is a consequence of upstream rotations. Natural for arcing, expressive motion (arm swings, tail whips).
- **IK (Inverse Kinematics)**: place an end effector (hand/foot target); a solver computes the joint rotations to reach it. Preferred whenever a limb must satisfy a world-space constraint — feet planting on uneven terrain, hands gripping a ladder rung — since you specify the goal rather than fighting to hand-pose three joints to hit an exact point every frame.
- **IK/FK switching** is the standard advanced-rig feature — same deform chain, both controls, blended/switched per shot.
- **Godot 4 specifically**: `SkeletonIK3D` (CCDIK two-bone solver) is **deprecated as of 4.4**, replaced by a `SkeletonModifier3D` family — `LookAtModifier3D` (single-bone aim, 4.4), then in 4.5 `BoneConstraint3D` subclasses (`AimModifier3D`, `CopyTransformModifier3D`, `ConvertTransformModifier3D`) plus `SpringBoneSimulator3D` for secondary motion. General-purpose IK solving returns more completely in **4.6**. The community plugin **Twisted IK 2** fills gaps for anything beyond single-bone look-at/aim on earlier versions.

## Animation Blending & Blend Trees

Blending mixes clips based on a runtime parameter instead of hard-cutting: **1D** (walk↔run by speed scalar), **2D** (aim-up/down/left/right by a look vector, or 8-way movement by a velocity vector). Godot's `AnimationTree` implements this directly: `AnimationNodeBlendSpace1D` (one parameter axis) and `AnimationNodeBlendSpace2D` (two axes) interpolate weights between clips placed at points/regions in the parameter space. `AnimationNodeStateMachine` is the discrete-state counterpart (idle → jump → fall → land). `AnimationNodeAdd2`/`Add3` allow additive layering (a flinch or lean on top of a base locomotion blend).

## Godot 4: AnimationPlayer vs AnimationTree

- **`AnimationPlayer`**: the base primitive — holds named `Animation` resources (keyframe tracks over any animatable property). Plays one clip at a time. Use for cutscenes, UI animation, simple one-shot object animation, **or** as the underlying data source an `AnimationTree` reads from — AnimationTree holds no animation data itself, it re-blends/re-sequences an AnimationPlayer's library via `anim_player`.
- **`AnimationTree`**: a graph built from `AnimationNodeBlendTree`, `AnimationNodeStateMachine`, blend spaces, etc. Use whenever runtime blending, layered/additive composition, or state-driven transitions are needed — essentially all locomotion/gameplay character animation. Both derive from the shared `AnimationMixer` base, where root-motion and blend-mode properties live.
- **State machine transitions**: each `AnimationNodeStateMachineTransition` has an Advance Mode (`Disabled`/`Enabled`/`Auto`) and, under Auto, an Advance Condition (a boolean parameter set at runtime via `tree.set("parameters/conditions/<name>", true)` or `travel()`), plus a configurable Xfade Time (linear cross-fade duration) and optional Xfade Curve for non-linear blending.

## Root Motion

The root bone's translation/rotation is baked into the animation itself — a walk cycle displaces the root forward the correct distance per step — instead of playing in place while a script drives `CharacterBody3D.velocity` separately. `AnimationMixer` exposes `root_motion_track`; `AnimationTree` computes accumulated delta per frame (`get_root_motion_position()`/`_rotation()`/`_transform()`), fed manually into `move_and_slide()`.

**Tradeoff**: foot-perfect, physically-grounded movement (no foot sliding, turning arcs match the actual weight shift), essential for precise climbing/mantling/attack-lunges — at the cost of control: gameplay-critical movement (responsive strafing, instant direction changes, networked prediction) is harder since velocity is locked to whatever the clip encodes, and blending root-motion clips requires blending their motion deltas too. Most action games use root motion selectively (attacks, traversal) and script-driven velocity for core locomotion.

## Animation Compression & Keyframe Reduction

Raw mocap is captured at 30–120+ Hz per bone-channel with no redundancy removal — tens of thousands of keyframes across a 20+ bone rig is normal. Two costs: memory and runtime decode. Mitigations: **keyframe reduction/curve fitting** (Blender's Decimate modifier on F-curves, or the Simplify curve operator, collapses near-linear segments to their endpoints within an error tolerance); **quantization** (compressed quaternions instead of full 32-bit floats per channel); resample mocap down to a sane import framerate (e.g. 120fps capture → 30fps) rather than importing every raw frame as a keyframe; use `AnimationLibrary` resources so shared clips (idle, common locomotion) aren't duplicated per character.

## Procedural Animation

Given terrain/procedural-heavy work elsewhere in this vault, this is the highest-leverage supplement to hand-authored clips:

- **Procedural IK foot placement**: raycast from each foot to terrain each frame, feed the hit point as an IK target so feet plant correctly on slopes/stairs without a hand-authored clip per terrain angle — blend the procedural IK offset on top of the base locomotion animation, not as a replacement.
- **Procedural look-at/aim offsets**: `LookAtModifier3D` (4.4+) aims a head/spine/weapon bone at a target point, layered additively on top of base animation — solves the aim-up/aim-down case without a full pre-authored blend-space.
- **Secondary motion**: `SpringBoneSimulator3D` (4.5+) does physically-simulated jiggle/follow-through for hair, cloth, tails, antennae — a lightweight alternative to full cloth sim or hand-keyed secondary motion.
- General pattern: procedural techniques trade some hand-crafted "feel" for infinite adaptability to runtime state (arbitrary terrain, arbitrary aim targets) and much lower authoring cost — layer procedural adjustments on top of a hand-authored/mocap base rather than choosing one exclusively.

## Godot Animation System — Version Notes

Mid-migration from monolithic single-purpose nodes to a composable `SkeletonModifier3D` stack: **4.4** introduced `SkeletonModifier3D`, deprecated `SkeletonIK3D`, added `LookAtModifier3D`/`RetargetModifier3D`; **4.5** added `SpringBoneSimulator3D` and the `BoneConstraint3D` family; **4.6** brings general-purpose IK solving back more completely. Check target Godot version before relying on specific IK API surface — it has shifted release-to-release.

## Related

- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [3D Model Creation for Games](kb://06-reference-3d-model-creation-for-games)
- [Reference Map](kb://01-maps-reference-map)
