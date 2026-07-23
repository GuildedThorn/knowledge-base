---
summary: Document the maker/fabrication tooling installed across the fleet.
status: active
tags: [hobbies]
---

## Purpose

Document the maker/fabrication tooling installed across the fleet.

## Current State (Real)

- `orca-slicer` (3D-printer slicer) is installed on `nixos` and `scout`.
- `fritzing` (circuit/breadboard design) is installed on both.
- `plasticity` (parametric CAD/3D modeling) is installed on both.
- `arduino` and `arduino-ide` are installed on `nixos`; an `~/Arduino` sketch directory and `.arduino15`/`.arduinoIDE` config exist on disk, confirming active use rather than just an installed-but-unused package.
- `blender` and `krita` (3D/2D art) are installed on both hosts too, and could feed into fabrication work (modeling for print, textures/decals) as much as pure digital art.

## Open Questions

- Which 3D printer(s) does Orca Slicer actually target — worth a device-specific profile note once known (bed size, filament types, known-good settings).
- What's in `~/Arduino` currently — worth a project-by-project breakdown once there's something concrete to point at (this note is intentionally light until then, to avoid inventing project names).
- Any interest in tracking print/build history (what's been printed, what worked, what didn't) the way [[08 Improvements/Improvements Tracker|Improvements Tracker]] tracks other unfinished work?

## Related

- [[01 Maps/Hobbies Map|Hobbies Map]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
