---
summary: Godot's OpenXR action-map layer, controller-profile conventions across headsets, semantic button conventions, comfort/accessibility, and the menu-button reservation gotcha.
status: active
tags: [reference, gamedev, godot, vr, input]
private: false
---

## Purpose

vr-brain's VR controller side already does input the idiomatic Godot way — `XRController3D.GetVector2("primary")` and similar named-action calls, not raw button codes — unlike its desktop side (see [Godot Input Handling and Keybind Design](kb://06-reference-godot-input-handling-and-keybind-design)). This note covers the general OpenXR/Godot XR input conventions underneath that, as a design reference for extending or validating the existing scheme (right hand: laser + trigger grab/pin, grip unpin, A open, B close/recenter, menu resync; left hand: thumbstick fly-where-you-look, grip dash, X search, Y push-to-talk). Compiled 2026-07-24.

## How Godot's XR Input System Works

Input flows through a layered abstraction, not raw button IDs:

- **OpenXR interaction profiles** (defined by the platform runtime) map a physical controller's real buttons/axes to standardized OpenXR input paths — e.g. `/user/hand/right/input/trigger/value`, `/user/hand/left/input/squeeze/value`, `/user/hand/left/input/thumbstick`. Godot never sees "Quest button 3," it sees a semantic path; the runtime/driver does the physical-to-semantic mapping per device.
- **Godot's XR Action Map** (`OpenXRActionMap`, Project Settings → XR → OpenXR → Action Map, stored as `openxr_action_map.tres`) sits on top: **`XRActionSet`s** (groups enabled/disabled together, e.g. "gameplay" vs "menu," each with a conflict-resolution priority) contain actions of five types — Bool (buttons), Float (analog, trigger pull), Vector2 (thumbstick/trackpad), Pose (spatial tracking — aim/grip/palm), Haptic (output only). Each action binds, per interaction profile, to a concrete OpenXR path — this is what lets one action named `"primary"` bind to the Quest Touch thumbstick on one profile and the Index thumbstick on another with the same code.
- **`XRController3D`** exposes the current profile's bound actions via `get_float(name)` (trigger/grip pull), `get_vector2(name)` (thumbstick/trackpad), `get_input(name)` (generic), `is_button_pressed(name)`, plus signals `button_pressed`/`button_released(action_name)`, `input_float_changed`, `input_vector2_changed`, and `profile_changed(role)` (fires if the runtime swaps interaction profiles mid-session — e.g. the user switches controller type).

**No runtime rebinding of the OpenXR layer** — per Godot's own docs: *"Godot's input system allows changes to what inputs are bound to actions in runtime, OpenXR does not."* Action-map bindings are editor-time only, baked into the exported resource, unlike desktop `InputMap` which is freely rebindable at runtime. An in-app "rebind your controller buttons" feature isn't achievable by remapping the OpenXR action map itself — it needs an app-level indirection layer: read a fixed set of raw actions, decide in game logic what each does, let the user reassign the game-logic side, not the OpenXR-binding side. Some runtimes (SteamVR notably) let the *end user* remap bindings outside the app via their own binding UI, but that's runtime-level, not app-controlled.

## Controller Profile Conventions

**Common across virtually all profiles**: analog trigger, grip/squeeze, a thumbstick or trackpad with click, at least one or two face buttons, a menu/system button path, haptic output. The **Khronos Simple Controller profile** (`/interaction_profiles/khr/simple_controller`) is the deliberate lowest-common-denominator fallback — just select/click, menu/click, grip pose, aim pose, haptic, nothing analog — for unknown/future hardware.

**What varies — don't design around universal assumptions:**

- **Grip fidelity**: most controllers (Quest Touch, WMR/Reverb G2) expose grip only as a binary click or single analog value. **Valve Index "Knuckles"** is the outlier — capacitive proximity *and* a separate analog grip-force sensor — but Godot's default action map only exposes proximity, not force (a still-open engine limitation), so "analog grip strength" isn't available out of the box even on Index.
- **Finger sensing**: Index alone reports per-finger curl (index/middle/ring/little, 0–1) via capacitive touch — no other mainstream profile has this.
- **Face buttons**: Quest Touch and Index both expose two per hand (A/B, X/Y); WMR/Reverb G2 controllers historically have only a trackpad + thumbstick and a single "grasp" button, fewer or no dedicated face buttons depending on generation.
- **Menu/system button asymmetry**: on the Oculus/Meta Touch profile, only the **left** controller's `menu` input reaches the app by default — the **right** controller's equivalent is the OS-level Oculus/system button and is not delivered to the application at all. Concrete, hardware-specific gotcha worth checking against any binding scheme putting an app-facing menu action on the right controller.

## De Facto Semantic Conventions

- **Trigger = primary select/interact** (Meta's own guidance: firing/primary selection, also the UI "click" when pointer-aiming at a widget).
- **Grip = grab/hold physical objects** (Meta explicitly recommends grip, not trigger, for picking up in-world objects, matching real hand-closing intuition — trigger stays reserved for throwing/firing even while grip holds the object).
- **Thumbstick = locomotion or menu nav**, conventionally split across hands (one stick moves, the other snap-turns) — traces to early Oculus/SteamVR locomotion templates, now genre-standard.
- **Bottom face button (A/X) = confirm/interact; top face button (B/Y) = back/cancel/secondary** — mirrors gamepad convention (Xbox A/B) carried into VR via Touch controller labeling.
- **Menu button = pause/system menu** — but see below: largely reserved by the platform, not freely available to the app on most runtimes.

This set originates from Meta's own published button-mapping research (large-scale survey of per-button, per-genre player expectations) and OpenXR's suggested-bindings tables, themselves seeded by earlier Oculus/SteamVR conventions.

## Menu/System Button Reservation — Confirmed

The platform menu/system button is generally **not interceptable by apps**, across runtimes: on SteamVR/OpenXR, menu click is reserved system-wide; on Meta/Oculus, the right controller's system button always goes to the OS-level menu, only the left controller's menu input reaches the app (and even that can be intercepted by the platform in some configs); on HP Reverb G2/WMR, the system button routes to the Windows Mixed Reality portal. **Practical implication**: any in-app menu system needs its own dedicated action (a face button, grip-hold gesture, or UI element) — it cannot rely on the platform menu button. This is why binding "menu button = resync/utility" (an app-level action on an actually-available input, not the OS-reserved one) is the right pattern rather than an oversight.

## Comfort and Ergonomics

- **Hold-fatigue**: sustained trigger/button holds beyond a few seconds cause hand fatigue — industry practice favors toggle-on-tap over hold-to-sustain for anything long-duration (recording, voice, continuous scanning). Directly relevant if push-to-talk voice (currently Y = hold) is ever reconsidered — hold works for short utterances, but a toggle mode (tap to start/stop) is the more accessible default for longer sessions.
- **Thumbstick dead zones**: small mechanical drift/creep on cheap or worn sticks can register as unintended input (accidental turning/movement) if the dead zone is too tight — tune it, ideally expose as a setting, rather than hardcoding a near-zero threshold.
- **Avoid mandatory bimanual precision actions**: requiring two hands to simultaneously perform fine-motor input for a *common* action excludes one-handed users — reserve two-handed requirements for genuinely optional/advanced interactions, not core-loop actions.

## Accessibility

Only ~2 of 39 surveyed free VR titles offered a one-handed mode (2024 data), despite ~25% of adaptive/disabled players needing one-handed play per AbleGamers Foundation reporting — a real, underserved gap. **Alternate input paths**: gaze/head-direction + dwell-select is a documented fallback for users who can't operate physical triggers, though slower and prone to the "Midas touch" problem (unintended activation from natural looking) — needs an explicit dwell-timer and visual confirmation affordance, not silent activation. Voice commands are used by over 60% of VR users with mobility challenges per XR Association's 2024 report — reinforces voice (already load-bearing here via push-to-talk) as a legitimate accessibility channel, not just convenience. Godot supports hand tracking as a parallel input source (`XRHandModifier3D`, OpenXR hand-tracking extension) — the architectural basis for "support hand-tracking AND controllers," though combining them well (fallback/preference logic) is still application-level work. No standard runtime remapping exists for the OpenXR layer itself (see above) — any accessibility remap UI must be the same app-level indirection layer, not an OpenXR binding change.

## Current Developments (2025–2026)

**Godot 4.5** (Sept 2025): DirectX 12 + OpenXR combined on Windows for better performance; foveated rendering now works under Vulkan on Android; the OpenXR render-models extension is now supported (dynamically load the correct 3D controller model for whatever hardware is connected — relevant to laser-pointer/hand-model visualization); support for a universal OpenXR APK running across any OpenXR-compliant standalone Android headset without per-vendor builds. **Godot 4.6**: OpenXR 1.1 and the OpenXR spatial entities extension (persistent spatial anchors/world-locking) — not input-specific. No major input-binding-model changes for 2025–2026; the action-map/interaction-profile architecture above remains current.

## Related

- [Godot Input Handling and Keybind Design](kb://06-reference-godot-input-handling-and-keybind-design)
- [VR and World-Space UI Design](kb://06-reference-vr-and-world-space-ui-design)
- [VR Performance Optimization](kb://06-reference-vr-performance-optimization)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Reference Map](kb://01-maps-reference-map)
