## Purpose

Document the VR/XR tooling enabled on the `nixos` host.

## Current State (Real)

- The `services-vr` module enables WiVRn (a standalone OpenXR runtime for streaming VR to a headset over the network) and Monado, plus a custom AMD GPU kernel patch — see [[02 Systems/NixOS - Shared Modules|Shared Modules]].
- Packages: `openxr-loader`, `xrizer` (OpenVR-to-OpenXR compatibility, lets SteamVR-only titles run on the OpenXR/WiVRn stack), `wayvr` (Wayland desktop virtualized inside VR).
- Only enabled on `nixos` — not `scout` or `mac`.
- The main homegrown app on this stack is [[07 Projects/vr-brain/vr-brain - Overview|vr-brain]] (the knowledge-base-as-VR-constellation, Godot 4 + OpenXR), built from the `vr-base` template — both in `~/Documents`.

## Open Questions

- Which headset is actually in use? WiVRn's whole point is network-streamed VR (no cable to the host), so this strongly implies a standalone/Quest-style headset rather than a tethered one — worth confirming and naming once known.
- Is `xrizer` needed because of specific SteamVR-only titles being played — worth listing which ones once that's settled.
- Any interest in documenting the actual network path WiVRn streams over (same LAN segment as `nixos`? dedicated Wi-Fi?) — relevant given the fleet's broader network-segmentation questions in [[05 Network/VLANs|VLANs]].

## Related

- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
- [[07 Projects/vr-brain/vr-brain - Overview|vr-brain - Overview]]
