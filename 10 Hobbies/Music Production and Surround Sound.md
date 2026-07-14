## Purpose

Tie together the music-production and surround-sound threads scattered across the fleet and projects into one place.

## Current State (Real)

- `mixxx` (DJ software) and `hydrogen` (drum machine) are installed on both `nixos` and `scout`; `musescore` (notation) is installed on both as well.
- Mixxx is genuinely, regularly used, not just installed: `~/.mixxx` has a real library database (`mixxxdb.sqlite`), configured `controllers/`, `effects.xml`, `broadcast_profiles/`, and 10+ rotated log files (`mixxx.log` through `mixxx.log.10`), indicating many real sessions rather than a one-off test.
- [[07 Projects/surround-panner/surround-panner - Overview|surround-panner]] is a working, tested, dependency-free VBAP 7.1 spatial-audio engine — offline, algorithm-verified, but not yet played on real 7.1 speakers.
- `~/Downloads/mixxx-surround-fork` is a separate, much earlier-stage effort: a plan (no code yet) to add live discrete-channel multichannel DJ mixing to Mixxx itself, distinct from surround-panner's offline VBAP approach.

## Idea: Close the Loop Into an Actual Studio Setup

Nothing here is built yet, but the pieces line up toward an obvious next project: a real 7.1 (or 5.1) monitoring setup fed by `surround-panner`'s output, to finally do the "first listening session" its own README calls out as the next step. Once that's validated, the Mixxx fork's live-mixing idea has a real target rig to build toward instead of being purely theoretical.

## Open Questions

- Is there an actual multichannel audio interface/speaker set on hand, or does this depend on future hardware?
- Does `nixos`'s audio module (PipeWire) already support routing to more than stereo out, or does that need explicit multichannel PipeWire config?
- Any interest in physical DJ controller hardware for the Mixxx side, or is this purely software-based for now?

## Related

- [[07 Projects/surround-panner/surround-panner - Overview|surround-panner - Overview]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
