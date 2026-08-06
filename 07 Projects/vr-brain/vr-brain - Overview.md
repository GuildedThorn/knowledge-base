---
summary: "Track Celestial, the plugin-first successor to `vr-brain`, and its path to a verified desktop/OpenXR release."
status: active
tags: [projects, vr-brain, celestial]
---

## Purpose

Track the architecture, current state, and release work for **Celestial** (`vr-brain-rewrite`), while preserving the original `vr-brain` history as implementation evidence.

## Summary

The original vr-brain turns the Obsidian knowledge-base — and the GuildedThorn online presence — into a walkable VR solar system. Built on the [[10 Hobbies/VR Setup|vr-base]] template (Godot 4 + C# / .NET 8 + OpenXR), it runs on the WiVRn/Monado stack from the `services-vr` module on host `nixos`, and also has a desktop (non-headset) rig. Its ground-up plugin-first successor is **Celestial**.

- Current rewrite: [GuildedThorn/Celestial](https://github.com/GuildedThorn/Celestial), local checkout at `/home/thorn/Games/vr-brain-rewrite`
- Legacy repo: [GuildedThorn/vr-brain](https://github.com/GuildedThorn/vr-brain), local checkout at `~/Downloads/vr-brain` (moved from `~/Documents/vr-brain` on 2026-07-23)
- Template it grew from: [GuildedThorn/vr-base](https://github.com/GuildedThorn/vr-base) at `~/Documents/vr-base`

## Celestial rewrite status (2026-08-01)

The rewrite is substantially ahead of the 2026-07-27 snapshot in [[vr-brain - Ground-Up Plugin Rewrite 2026-07-27]]. Repository evidence shows that MCP, the in-world agent panel, cosmic ambience, semantic and orbital constellation behavior, Typst documents, settings, and later Earth/OSINT work are already implemented. `docs/CARRY_FORWARD.md` now treats every legacy idea in its tracked port list as represented by a removable plugin or a documented later-architecture reference.

The remaining work is therefore release convergence, not a blanket port of the old monolith:

- The GitHub repository is named **Celestial**, while the Godot application, assembly/namespace, configuration and user-data paths, plugin IDs, MCP/socket names, environment variables, docs, and Discord presence still use VR Brain naming. This needs an explicit compatibility plan before identifiers are changed.
- `celestial/main` was last observed at merge commit `95cb345` (2026-07-29). The checkout was still on `feature/typst-documents` at its parent `42a1214`, and local `main` was older. A clean integration baseline has not been recorded in this vault.
- The authenticated JSON-RPC/MCP gateway supports bounded `knowledge.search` and `knowledge.read`, but those calls still do not publish typed activity that can pulse, highlight, or focus constellation notes. The removable agent-activity plugin specified in the rewrite note remains unimplemented.
- No repository CI workflow, Godot export preset, tagged release, or repeatable release checklist was found. The earlier desktop pass was recorded, but physical OpenXR/headset validation remains outstanding.
- Task comets were deliberately cut from the decorative cosmos plugin. Restoring them is a product-scope decision, not an assumed rewrite defect; active browsers and persistent terminals likewise need an explicit security/product decision because Celestial currently provides deliberately constrained replacements.

## The constellation

- The graph is a solar system: the identity hub is the sun, each top-level vault folder and presence source is a ringed planet, notes/repos are moons, subfolders are smaller moon-hubs, and leaf content stays folded under its source until focused. Orbits are deterministic with a slow drift; planets are grouped into per-category spiral-arms (by their dominant child kind), ordered by population, and spaced by each folder's moon-disk footprint so nothing overlaps (reorganized 2026-07-23). Constellation link-lines are kept local (same cluster) so the sky isn't a web; the floor grid was removed so the system floats in open space.
- `[[wikilinks]]` draw as constellation lines; `private: true` notes are ringed in red; grabbing a body pins it in place, unpinning glides it back.
- Online presence hangs off the same identity hub, fetched live with no auth: GitHub repos (sized by stars), gists, and starred projects, plus web/blog pages.
- An astronaut idles by the sun and flies to any note that changes on disk (Obsidian edit, git push, or Claude writing the vault), showing edits live.

## Terminals, browsers, station

- Real terminals float in-world, backed by dtach sessions (`term-socks/term-N`) that detach on quit and reattach on relaunch. Fleet SSH consoles use session ids 920+.
- Real Firefox browsers run in-world with per-session persistent profiles under `browser-sessions/`.
- A space station rides a high orbit as the ops deck: a SOC console (auto-runs the security dashboard, survives restarts), an admin console, and a persistent docked browser.

## Claude voice agent

- Push-to-talk with voice engine `claude`: the local whisper transcript is handed to a headless `claude` run rooted in the vault, wired into the world through an embedded MCP server. The agent can search/read/write notes, focus orbs, open terminals and type into them, and open in-world browsers; a floating panel streams its output.
- Mutations (note writes, terminal commands) pause on an in-world approve prompt — Y runs, N declines. Claude's own file tools are read-only; edits funnel through `write_note`. Toggle via `[voice] agent_approval`.
- The panel has a prompt line for typed follow-ups in the same conversation; a fresh voice push starts a new one.
- The agent also writes into the vault itself: daily notes under `Briefings/` and VR screenshots + captions under `Postcards/`.

## Key bindings (highlights)

- **H** — cheat sheet; **C** — recenter; **Esc** — release panel focus; **X** — dismiss/stop the agent panel.
- **Shift+T** — summon terminals to you; **Shift+B** — summon browsers; **Ctrl+Shift+W** — detach a browser session; **Ctrl+Shift+Q** — quit a browser session (profile survives).
- **Shift+C** (added 2026-07-22) — flies *you* to the next terminal with a live `claude` process and focuses it, one hop per press; panels stay where placed, free-floating ones turn to face you, station consoles untouched. Detection: `Terminals.SessionsRunningClaude()` scans `/proc` for `claude` processes and walks parent chains to the dtach session master to recover the session id. Runs only on keypress. Limits: fleet SSH consoles (ids 920+) can't be detected (remote claude is invisible to local `/proc`); plain **C** remains recenter. Code: `src/Brain/Terminals.cs` (`VisitNextClaude`), `src/Brain/Pointer.cs`, `src/DesktopRig.cs`.

## Comets (tasks)

- Every unchecked `- [ ]` task in the vault becomes an icy comet on a deterministic eccentric, inclined orbit crossing the system. Each has a glowing **coma**, a ribbon **trail threaded back along the path it actually travelled**, and ion/dust particles streaming out behind its motion; it flares brighter near perihelion and dims out at the cold far end. Overdue tasks turn red. Aim + Enter (or RMB) opens the source note; checking the task off melts the comet on the next sync. Toggle: `[display] comets`. Code: `src/Brain/Comets.cs`.

## Cosmic environment (added 2026-07-23)

The ambient/visual layer, all additive + bloomed and holding ~140 fps on desktop:

- **Living sun** — the identity sun breathes and flickers via a stacked additive **corona** and erupts plasma **prominences** (magnetic loops arcing off the surface); sized to dwarf Earth. `src/Brain/SolarCorona.cs`, `SolarProminences.cs`.
- **Nebula** — a procedural FBM-noise nebula (no assets) wraps the system in a tilted galactic band of gas clouds. `src/Brain/Nebula.cs`.
- **Spiral galaxies** wheel in the deep background (log-spiral star-motes in one MultiMesh each). `src/Brain/Galaxies.cs`.
- **Asteroid belt** — a tilted ring of ~1600 tumbling rocks in a single MultiMesh. `src/Brain/AsteroidBelt.cs`.
- **Meteor shower** — occasional shooting stars streak the far sky. `src/Brain/Meteors.cs`.
- **Twinkling starfield** — the background stars shimmer on detuned sines. `src/Brain/Starfield.cs`.
- Inner bodies (planets, comet perihelia, the crew dock) were pushed out so nothing sits inside the enlarged sun's corona.

## Search palette

- **/** (desktop) or left **X** (VR) opens a fuzzy finder over *everything*: notes — matched on title **and** full body text — and presence orbs, plus the live floating terminals, browser panels, and task comets. Select a result to focus it and dash there. `src/Brain/SearchPanel.cs`, `FuzzySearch.cs`.

## Related

- [[vr-brain - Engineering Run Through 2026-07-26]] — two-session implementation, decision, validation, and resume record
- [[vr-brain - Architecture]] — full subsystem map + config schema
- [[Earth - Geo Engine Rewrite]] — the cube-sphere globe + data layers + terrain
- [[Terrain Rendering Optimization]] · [[High-Fidelity Planet Rendering (Godot)]] · [[Globe Data Source APIs]]
- [[10 Hobbies/VR Setup|VR Setup]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[01 Maps/Projects Map|Projects Map]]

## Ephemeris Plan

<!-- ephemeris:plan:start -->
## Goals

- Deliver a verified desktop/OpenXR release of **Celestial** while retaining its plugin-first architecture, compatibility boundaries, privacy controls, and existing release-convergence intent [E1] [E4] [W5].
  - **Objective:** Establish the authoritative rewrite baseline, verify it, record desktop/OpenXR acceptance evidence, reconcile project documentation, and evaluate the ranked user-facing feature candidates below without treating them as approved scope [W1] [W2] [W5] [W6] [W7] [W8] [W9].
  - **Definition of done:** The authoritative commit is recorded; automated verification results and per-suite totals are recorded; desktop and OpenXR acceptance evidence exists; naming compatibility and privacy boundaries are documented; the project brief is reconciled; and each proposed feature is either accepted into separately scoped work or explicitly deferred [E1] [W5] [W6] [W7] [W8] [W9].
  - **Uncertainty:** The supplied evidence does not contain a current clean verification result, exact assertion totals, or recorded desktop/OpenXR acceptance results [E1] [W2] [W7].

## Milestones

- [ ] Reconcile the project note with recent repository evidence [E1]. [W1]
- [ ] Confirm the current test baseline [E1]. [W2]
- [ ] Reconcile the project note with recent repository evidence [E1]. [W1] [W3]
- [ ] Confirm the current test baseline [E1]. [W2] [W4]
- [ ] Release **Celestial** from the plugin-first rewrite with a coherent identity, visible and privacy-bounded agent activity, green automated verification, and recorded desktop/OpenXR acceptance evidence. [W1] [W3] [W5]
- [ ] Move the working baseline to `celestial/main` (or create a clean tracking branch/worktree), record the exact commit, and stop treating the older local `main` as authoritative. [W7] [W4] [W6]
- [ ] Run `./scripts/verify.sh` from that clean integration tree and record the build result plus per-suite assertion totals in the rewrite note. [W8] [W5] [W7]
- [ ] Record the decision and evidence for the completed slice. [W8]
- [ ] Re-run Ephemeris reconciliation and update the project brief. [W9]

## Tasks

- [ ] **Rank 1 — Propose a first-run privacy and capability tour**
  - **Inference:** Celestial’s external packages require explicit trust, enablement, and permissions, while agent access and integrations are removable plugins; a user-facing first-run tour could make those boundaries understandable without changing the security model [E4].
  - **User value:** A user can see what data and capabilities each enabled plugin or agent can access before entering the spatial environment [E4].
  - **Smallest testable slice:** On a fresh profile, show one desktop-compatible screen listing enabled plugins, requested permissions, external-package trust state, and agent visibility; require confirmation before continuing.
  - **Dependencies:** Complete the naming/identifier compatibility decision and use the authoritative verified baseline so the tour presents stable product and plugin identities [E1] [W6] [W7].
  - **Material risks:** Permission descriptions may imply OS-level isolation even though admitted external code runs in-process; the copy must distinguish admission policy from sandboxing [E4].
  - **Acceptance criteria:** A fresh-profile test displays every enabled plugin and its declared grants; untrusted external packages are identified as disabled; proceeding records the user’s confirmation; desktop and OpenXR reviewers can read and complete the flow without configuration-file editing.
  - **Evidence gap:** The supplied evidence does not establish whether an onboarding flow already exists; repository confirmation is required before accepting this candidate [E1].

- [ ] **Rank 2 — Propose portable comfort and control profiles**
  - **Inference:** The product supports both OpenXR and a desktop fallback, but the supplied evidence documents fixed locomotion/control behavior rather than user-selectable comfort profiles [E8].
  - **User value:** Users could switch among seated, standing, reduced-motion, and desktop control presets without manually tuning individual settings.
  - **Smallest testable slice:** Add one reduced-motion profile that disables pitch-following flight, lowers travel speed, and replaces continuous turning with configurable snap turning while preserving the existing default.
  - **Dependencies:** Verified desktop and OpenXR input baselines, stable settings persistence, and acceptance runs on both rigs [E1] [E8] [W7].
  - **Material risks:** Divergent desktop/OpenXR behavior could complicate testing; forced camera motion can still cause discomfort if shared travel helpers bypass the profile [E8].
  - **Acceptance criteria:** A user can select and persist the reduced-motion profile; all shared travel paths honor it; returning to the default restores existing controls; desktop and OpenXR acceptance evidence covers both profiles.
  - **Evidence gap:** Settings are reported as implemented, but their exact control and accessibility coverage is not supplied [E1].

- [ ] **Rank 3 — Propose spatial bookmarks with resumable sessions**
  - **Inference:** Celestial provides navigable celestial, Earth, workspace, and application surfaces, creating value in restoring a user’s location and working context; no supplied evidence confirms a user-facing bookmark or session-resume feature [E1] [E4] [E6].
  - **User value:** A user can leave a complex investigation or workspace and return directly to the same viewpoint and selected context.
  - **Smallest testable slice:** Save and restore one local bookmark containing rig mode, viewpoint, selected object identifier, and active workspace surface—without storing terminal contents, agent transcripts, or secrets.
  - **Dependencies:** Stable object/plugin identifiers, the naming compatibility plan, settings or user-data persistence, and shared desktop/OpenXR navigation contracts [E1] [E8].
  - **Material risks:** Renamed or removed plugins can invalidate bookmarks; persisted workspace state could leak sensitive context; restoring an XR pose could be disorienting.
  - **Acceptance criteria:** A bookmark survives restart; a missing object produces a safe fallback; private content is excluded by schema and test; restoration works in desktop mode and requires explicit confirmation before XR movement.
  - **Evidence gap:** Persistence formats and stable spatial-object identifiers are not described in sufficient detail to estimate implementation effort [E1] [E4].

- [ ] **Rank 4 — Propose an in-world provenance trail for inspected claims**
  - **Inference:** The architecture emphasizes authoritative records, provenance, typed projections, and treating remote text as evidence; a compact user-facing provenance trail would expose those guarantees during exploration [E3] [E6].
  - **User value:** When inspecting a note, live observation, correlation, or Earth object, a user can distinguish source evidence from derived or agent-generated interpretation [E3] [E6].
  - **Smallest testable slice:** For one knowledge-derived object type, display its authoritative source, observation time when available, transformation/plugin owner, and whether the displayed statement is source material or inference.
  - **Dependencies:** Existing knowledge/evidence contracts, plugin ownership metadata, visibility enforcement, and a privacy review for source identifiers [E3] [E4].
  - **Material risks:** Incomplete metadata could create false confidence; source paths or authorship may reveal private information; heterogeneous plugins may not expose equivalent provenance [E3].
  - **Acceptance criteria:** Every object in the pilot type shows its source and derivation state; missing fields are labeled unknown rather than fabricated; visibility rules apply when provenance is queried; tests cover authoritative, derived, inaccessible, and missing-source cases.
  - **Evidence gap:** The evidence establishes provenance as an architectural guardrail but does not confirm that all runtime objects currently expose the metadata required by this feature [E3].

- [ ] Sequence feature decisions after baseline verification: check each candidate against the authoritative tree for duplication, then record accept/defer/reject decisions without altering the existing release milestones [W6] [W7] [W8].
- [ ] Treat Rank 1 as the preferred post-baseline discovery spike because it directly supports the existing privacy-bounded release intent; this ranking is a proposal, not an approved reprioritization [W5].
- [ ] Keep Ranks 2–4 outside the release critical path unless baseline evidence shows they are required for desktop/OpenXR acceptance [W5] [W7].

## Tasks — Feature candidates

- [ ] **Rank 1 — Add an in-world plugin control center**
  - **User value:** Let users inspect installed plugins, dependency relationships, permissions, health, and startup failures without editing configuration files. This builds on Celestial’s plugin-first architecture and failure-containment model [E4].
  - **Smallest testable slice:** A read-only panel listing each plugin’s status, declared capabilities, dependencies, and permission grants; enablement changes remain out of scope.
  - **Dependencies:** Authoritative rewrite baseline and verified plugin lifecycle behavior [W10] [W11].
  - **Material risks:** Exposing enable/disable controls prematurely could create invalid dependency graphs or obscure the distinction between admission policy and an OS sandbox [E4].
  - **Acceptance criteria:** On desktop and OpenXR, the user can open the panel, inspect every discovered plugin, identify a deliberately failed noncritical plugin, and see its dependency and permission information without destabilizing other plugins [E4] [W9].
  - **Inference/uncertainty:** The evidence documents plugin mechanics and settings, but does not establish that a user-facing lifecycle inspector already exists [E1] [E4]; duplication must be checked against the authoritative tree before acceptance [W18].

- [ ] **Rank 2 — Add a spatial “focus lens” for dense knowledge scenes**
  - **User value:** Temporarily reduce unrelated bodies, links, and live overlays around a selected object so users can understand one neighborhood without permanently changing the underlying knowledge graph.
  - **Smallest testable slice:** Selecting one celestial object reveals only its first-degree relationships, with a single action to restore the full scene.
  - **Dependencies:** Stable selection behavior and existing semantic/orbital constellation capabilities [E1].
  - **Material risks:** Hidden context could mislead users; the interface must clearly indicate that the scene is filtered rather than complete.
  - **Acceptance criteria:** In both desktop and OpenXR, selecting a test object activates the lens, preserves the selected object and all first-degree links, visibly marks the filtered state, and restores the identical pre-lens view on exit [W1] [W9].
  - **Inference/uncertainty:** Semantic and orbital constellation behavior is reported as implemented, but the supplied evidence does not confirm a reversible local decluttering workflow [E1].

- [ ] **Rank 3 — Add guided spatial routes through knowledge and Earth content**
  - **User value:** Allow a user to arrange several notes, locations, or observations into a step-by-step narrated route for presentations, investigations, or learning.
  - **Smallest testable slice:** Create a three-stop route from existing selectable objects, move forward and backward between stops, and display a short caption at each stop.
  - **Dependencies:** Shared travel controls across desktop and OpenXR, plus stable object identifiers [E8] [E4].
  - **Material risks:** Automated movement may cause VR discomfort, and plugin-owned objects may disappear between sessions.
  - **Acceptance criteria:** A three-stop route can be created and replayed in both modes; each transition supports immediate cancellation, missing stops produce a recoverable warning, and route data stores references rather than duplicating authoritative content [E3] [E8].
  - **Inference/uncertainty:** Existing travel primitives can likely support route playback, but route authoring and persistence are not evidenced [E8].

- [ ] **Rank 4 — Add a time-scrubber for live geospatial observations**
  - **User value:** Let users compare how weather, cyber, natural-event, or other Earth layers changed over a bounded period instead of seeing only the latest state.
  - **Smallest testable slice:** One timestamped point layer with play, pause, and scrub controls over a fixed local sample dataset.
  - **Dependencies:** GeoLayer source/render separation and timestamp-preserving ingestion contracts [E5].
  - **Material risks:** Feeds may have incompatible retention, timestamps, or licensing; replayed observations could be mistaken for current data.
  - **Acceptance criteria:** The sample layer renders the correct snapshot at three known timestamps, clearly labels replay mode and observation time, and returns to live state without mixing historical and current records [E3] [E5].
  - **Inference/uncertainty:** The evidence describes time-varying observations and pluggable layers, but does not establish historical retention or replay support [E5] [E6].
<!-- ephemeris:plan:end -->
