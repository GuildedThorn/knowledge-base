---
summary: Document the SDR/radio tooling installed across the fleet.
status: active
tags: [hobbies]
---

## Purpose

Document the SDR/radio tooling installed across the fleet.

## Current State (Real)

- `sdr.nix` (RTL-SDR + HackRF tooling) is enabled as a service module on `nixos` and `scout` — see [[02 Systems/NixOS - Shared Modules|Shared Modules]].
- `chirp` (radio programming software for amateur/GMRS/business-band handheld and mobile radios) is installed on both `nixos` and `scout`.

## Open Questions

- Is there an amateur radio license/callsign associated with this setup, or is the SDR side purely receive-only (scanning/monitoring) for now?
- Which specific hardware is on hand — an RTL-SDR dongle, a HackRF One, both? Worth recording once known, since it affects what's actually receivable (HF vs VHF/UHF only).
- Which radios does `chirp` currently manage? Worth a device-specific note once that's settled, similar to [[06 Reference/Commands Cheat Sheet|Commands Cheat Sheet]] but for radio programming templates.

## Related

- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
