---
summary: Godot's InputMap/Action system vs raw keycode checks, retrofit path, and keybind UX conventions for UI-heavy spatial tools like vr-brain.
status: active
tags: [reference, gamedev, godot, ui, input]
private: false
---

## Purpose

vr-brain's desktop keyboard handling is 100% raw hardcoded key checks (`Input.IsPhysicalKeyPressed(Key.W)` polling in `DesktopRig.cs`, a `switch (key.PhysicalKeycode)` in `Pointer.cs`) — Godot's InputMap/Action system is used nowhere on the desktop side, unlike the VR-controller side which already does the idiomatic named-action thing (see [VR Controller Input and OpenXR Action Maps](kb://06-reference-vr-controller-input-and-openxr-action-maps)). This note covers what InputMap actually buys, how to retrofit it, and keybind UX conventions for a reading/terminal/search-heavy spatial tool rather than a twitch action game. Compiled 2026-07-24.

## What InputMap Is and Why It's Idiomatic

`InputMap` is a project-level singleton mapping **named string actions** (`"dash"`, `"summon_terminal"`) to one or more `InputEvent`s (key, mouse, joypad). Editor-defined via Project Settings → Input Map (persisted in `project.godot`), or runtime-defined for a C#-driven project: `InputMap.AddAction("dash")` then `InputMap.ActionAddEvent("dash", new InputEventKey { PhysicalKeycode = Key.F })`, typically once from an autoload's `_Ready()`. Code then queries the action, never the key: `Input.IsActionPressed("dash")` (held), `Input.IsActionJustPressed("dash")` (edge-triggered — the correct replacement for a `switch` on `key.PhysicalKeycode`).

**Structural benefits raw keycode checks can't provide:**

1. **Rebindability.** A settings UI calls `InputMap.ActionEraseEvents(action)` then `ActionAddEvent(action, newEvent)` at runtime with zero changes to logic reading `IsActionPressed`. A hardcoded `case Key.F:` has no equivalent seam — rebinding means shipping new code.
2. **Multi-device binding without branching.** One action accepts multiple simultaneous events — keyboard `F` *and* a gamepad button *and* a joystick axis all bound to `"dash"` — so the same call site works everywhere with no per-device `if` chains.
3. **Single source of truth.** `InputMap.GetActions()` returns every registered action name, iterable by a settings/rebind screen or a cheat-sheet generator. This directly targets vr-brain's current risk: the `H`-bound cheat sheet is hand-authored text that has to be manually kept in sync with the `switch` statement's cases — any new shortcut added and forgotten in the cheat sheet silently goes stale. That staleness class disappears once the cheat sheet is generated from `InputMap.GetActions()` + `InputMap.ActionGetEvents()` instead of hand-typed.

## Retrofitting InputMap onto vr-brain's Existing Code

1. **Register actions** programmatically in an autoload's `_Ready()` (matches a C#-driven project better than editor authoring): one `AddAction`/`ActionAddEvent` pair per current hardcoded key — `move_forward` (W), `dash` (F), `summon_terminal` (T), `summon_browser` (B), `recenter` (C), `postcard` (P), `search` (Slash), `dismiss` (X), `resync` (R), `delete_item` (Delete), plus the Shift/Ctrl-tiered variants (`detach_browser` = Ctrl+Shift+W, `quit_browser` = Ctrl+Shift+Q, etc.).
2. **Swap call sites**: `Input.IsPhysicalKeyPressed(Key.W)` → `Input.IsActionPressed("move_forward")`; the `Pointer.cs` switch collapses into `if (@event.IsActionPressed("dash"))` checks (or a dictionary of action name → delegate).
3. **Build a minimal rebind UI**: a "waiting for input" state entered on a rebind-button click, captured via `_UnhandledKeyInput(InputEvent @event)`; on receipt, `InputMap.ActionEraseEvents(action)` then `ActionAddEvent(action, capturedEvent)`. For display strings, `InputEventKey.AsTextPhysicalKeycode()` (or `AsTextKeyLabel()` for a localized label) gives a human-readable string like `"Ctrl+Shift+T"` directly — no manual string-building.
4. **Persist manually — the one sharp edge.** InputMap changes are runtime-only; nothing writes them back to `project.godot`, and that's the wrong place for user prefs anyway. Standard pattern: a `ConfigFile` (`user://keybinds.cfg`) written on rebind, reloaded and applied as an override on top of the programmatic defaults before InputMap setup on next launch.
5. **Consider not hand-rolling it**: community plugins solve the full rebind-UI + profile + persistence problem — [Keychain (Orama-Interactive)](https://github.com/Orama-Interactive/Keychain) supports multi-event actions across keyboard/mouse/gamepad with profiles and save/load; [Maaack/Godot-Input-Remapping](https://github.com/Maaack/Godot-Input-Remapping) is a lighter remap-menu-plus-ConfigFile template.

No InputMap-breaking API changes across Godot 4.4–4.6 — `AddAction`/`ActionAddEvent`/`ActionEraseEvents`/`EraseAction`/`HasAction`/`GetActions`/`ActionGetEvents` are stable. One open bug worth checking against the target version: [godot#114223](https://github.com/godotengine/godot/issues/114223) — InputMap not always reloading correctly after `project.godot` changes at runtime in 4.5.x, which argues further for the ConfigFile-override pattern over relying on editor-file reloads.

## Keybind UX Conventions for a Reading/Terminal/Search-Heavy Tool

vr-brain's existing pattern — bare keys for high-frequency actions, Shift+key for a "summon" tier, Ctrl+Shift+key for session management — maps onto a real, named convention, not ad hoc choices:

- **Tiered modifier convention.** Microsoft's own HIG states it explicitly: bare/simple keys for frequent direct actions, Ctrl+key for large-scale/global effects, Shift+key for actions that extend or complement the base action — close to vr-brain's F=dash / Shift+T=summon-terminal split. Vim pushes bare keys over chords further for high-frequency tools; VS Code's chorded tier (`Ctrl+K Ctrl+C`-style) exists specifically for *rare* commands where collision-avoidance outweighs speed. vr-brain's three tiers (bare → Shift → Ctrl+Shift) is a legitimate scaling of this same idea.
- **Mnemonic consistency** (T=Terminal, B=Browser) traces back to the original Mac shortcut conventions (⌘O=Open) and is cited as the single strongest predictor of shortcut learnability/retention.
- **OS/compositor collision avoidance** is a live risk, not theoretical, for an app running under Hyprland (a Wayland compositor that binds global chords, generally `Super`-prefixed) alongside browsers/DEs that commonly claim `Ctrl+W`, `Ctrl+Shift+Esc`, `Alt+Tab`, `Ctrl+Shift+T` (reopen closed tab — worth checking against vr-brain's own Shift+T terminal-summon binding for conflict potential inside `BrowserPanel`'s embedded browser context). Never let an app-level binding shadow a well-known system chord. Practical audit once InputMap is adopted: `InputMap.GetActions()` diffed against Hyprland's active bind list and the embedded browser's default chords.
- **Command palette as the discoverability fallback.** vr-brain's `/`-bound search already follows the VS Code `Ctrl+Shift+P` pattern — a keyboard-first entry point with fuzzy matching over every available command, which is what makes memorizing the full shortcut set optional. Natural upgrade once InputMap is adopted: drive the palette's entry list from `InputMap.GetActions()` directly, rendering each entry's live current binding via `InputEventKey.AsTextPhysicalKeycode()` next to its label — self-updating, can never drift.
- **Cheat sheet / help overlay.** vr-brain's `H`-bound sheet matches the standard passive-discoverability convention (`?`/`H`/`F1` bound to a glanceable reference, vs the active-search palette). The staleness risk applies even more acutely here since it's prose, not search results — generate it from the InputMap action registry at display time, don't maintain it as static text.

## Toggle vs Momentary vs Chorded

- **Momentary** (held-while-active): movement, sprint/boost modifiers, anything that should stop the instant the key releases — check with `IsActionPressed` every frame/tick. vr-brain's WASD movement already does this in spirit, just via raw keys instead of actions.
- **Toggle** (single tap flips persistent state): pin/unpin, mute, mode switches — check with `IsActionJustPressed` and flip a bool, don't require holding. vr-brain's X (dismiss/unpin) is inherently toggle-shaped already.
- **Chorded** (modifier + key, single edge-triggered event): reserve for the second/third UX tier — rarer, higher-consequence, or disambiguating actions (session management, destructive actions like delete-with-confirmation). Should almost always be edge-triggered (`IsActionJustPressed`), not polled — a held chord repeating an action every frame is rarely correct.

## Related

- [VR Controller Input and OpenXR Action Maps](kb://06-reference-vr-controller-input-and-openxr-action-maps)
- [Godot UI Architecture and Control Nodes](kb://06-reference-godot-ui-architecture-and-control-nodes)
- [Godot Engine Architecture and Patterns](kb://06-reference-godot-engine-architecture-and-patterns)
- [vr-brain - Architecture](kb://07-projects-vr-brain-vr-brain-architecture)
- [Reference Map](kb://01-maps-reference-map)
