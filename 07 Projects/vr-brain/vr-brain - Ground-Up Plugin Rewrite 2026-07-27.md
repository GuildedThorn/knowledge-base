---
summary: Ground-up plugin-first rewrite of vr-brain from a fresh vr-base clone, including the WGS 84 Earth pipeline, spatial knowledge constellation, knowledge and intelligence cores, private agent gateway, and credited Touchstone and Intellio adapters.
created: 2026-07-27
updated: 2026-07-27
tags: [project, vr-brain, architecture, plugins, earth, knowledge, constellation, intelligence, touchstone, intellio]
---

# vr-brain - Ground-Up Plugin Rewrite 2026-07-27

## Outcome

The new implementation lives at:

`/home/thorn/Games/vr-brain-rewrite`

It began from a fresh clone of
`git@github.com:GuildedThorn/vr-base.git`. The former checkout at
`/home/thorn/Downloads/vr-brain` and this knowledge base were used as
requirements, experiments, and postmortems. The implementation is new source,
not a line-for-line reimplementation and not a compatibility wrapper around
the old `src/Brain` monolith.

The central design decision is that essentially all product behavior is a
plugin. `scenes/Main.tscn` contains only `RuntimeKernel`; the kernel owns
lifecycle, typed capabilities, events, config, admission policy, and scene
ownership. Earth, knowledge, intelligence, integrations, agent access,
diagnostics, input, and workspace surfaces are independently removable
plugins.

## Plugin kernel

The host validates the complete graph before product state changes:

- stable plugin IDs and manifests;
- explicit required and optional plugin dependencies;
- typed required, optional, and provided capabilities;
- one provider per capability;
- declared permission grants;
- deterministic topological startup;
- noncritical failure containment;
- critical rollback;
- owner-scoped event/capability revocation;
- reverse-order shutdown.

External packages are disabled by default. Loading requires an exact assembly
SHA-256 trust record, explicit enablement, an exact permission bitmask, package
path containment, manifest/implementation identity checks, and a collectible
assembly context. These permissions are admission/audit policy, not an OS
sandbox; admitted external code still runs in-process.

## Earth rebuilt from the math up

Earth is no longer one oversized class. Separate plugins own state, providers,
cache, streaming, overview rendering, precision rendering, buildings, and UI.

Foundation:

- WGS 84 geodetic ↔ ECEF conversion in double precision;
- local east/north/up frames;
- Vincenty geodesics with an antipodal fallback;
- Web Mercator tile identity, bounds, ancestry, children, and neighbors;
- focus-protected z18–z22 LOD and altitude-derived clipping;
- Terrarium height decode, bilinear samples, and neighbor aprons;
- building coverage and provenance models.

Runtime:

- ArcGIS World Imagery with ArcGIS Streets and OpenStreetMap fallback;
- private content-addressed tile cache;
- host allowlists, bounded payloads, request deduplication, cancellation,
  retries, negative caching, and circuit breaking;
- z3 overview atlas with corrected Web Mercator-to-sphere sampling;
- local ENU precision frame with one shared grid and GPU terrain displacement;
- bounded OpenStreetMap/Overpass footprint extrusion;
- visible active-source attribution.

The visual pass caught two errors that unit/headless tests could not: the first
overview shader sampled Web Mercator as linear latitude, and the old Euler
orientation sent a Chicago focus to its antipode. The final renderer performs
the correct projection and builds an explicit local east/north/outward basis,
placing North America at the selected focus with north upright. Polar no-data
pixels blend into a procedural cap instead of producing a dark artifact.

## Knowledge and intelligence

The knowledge plugin performs a read-only, bounded Obsidian scan. It skips
hidden/reparse paths, parses frontmatter, tags, wikilinks, and headings, and
provides explainable lexical/tag/link/recency ranking.

The intelligence plugin is a separate durable evidence domain. It normalizes
untrusted text, flags instruction/tool language, strips credentials from
source URIs, hashes evidence, records revisions, appends before applying
mutations, checkpoints to compressed snapshots, recovers from its journal, and
returns scored query reasons.

The spatial workspace is a provider registry. Knowledge, intelligence,
diagnostics, security, and integrations lease surfaces into one shell rather
than reaching through a giant root scene.

## Spatial knowledge constellation

The former star KB idea was re-engineered as its own
`vrbrain.knowledge.constellation` plugin rather than copied out of the old
`BrainGraph` monolith. It consumes the typed, read-only knowledge capability
and publishes a typed constellation capability; Earth remains a separate
mode and neither renderer reaches into the other.

The new graph is deterministic and bounded:

- a synthetic knowledge sun, folder planets, and note stars;
- hierarchy paths plus resolved, deduplicated wikilink paths;
- importance-aware note and edge caps that preserve connected material;
- non-overlapping golden-angle clusters laid out primarily in the screen
  plane, with shallow depth for spatial readability;
- multimesh rendering, distance LOD, local relationship emphasis, and a
  deterministic twinkling deep starfield;
- screen-space picking, selection rings, double-click/Enter focus, reader,
  explainable search, and Home reset;
- desktop orbit/zoom and OpenXR ray selection, focus, mode switching, and
  haptic confirmation.

On the real vault, the validated graph contained 453 indexed notes and 654
wikilinks, rendered as 512 bodies and 989 bounded paths. `G` switches between
Earth and the constellation, `K` opens the constellation directly, and the
Knowledge workspace also exposes an explicit **Open 3D constellation**
action. The implementation has no dependency on the legacy constellation
classes.

## Local agent boundary

Agents connect through authenticated newline-delimited JSON-RPC 2.0 on a
private Unix-domain socket:

- a random 256-bit per-process token;
- `0600` descriptor and socket and a `0700` runtime directory;
- fixed-time token comparison;
- strict JSON fields, depth, frame, and response sizes;
- bounded clients, auth failures, rate, and main-thread work;
- no request parameters or tokens in logs;
- stale-instance cleanup with validated process, path, and instance identity.

The allowlist covers bounded knowledge reads, intelligence queries, Earth
navigation, workspace state, Touchstone requests, and Intellio validation.
There is no arbitrary shell, raw filesystem access, vault write, or invisible
Intellio report generation.

## Visible agent use of the knowledge constellation

Agents retain the knowledge base as a primary context source. The private
gateway exposes bounded, read-only `knowledge.search` and `knowledge.read`
methods over the indexed vault instead of granting agents raw filesystem
access.

The committed rewrite does not yet project those tool calls onto the 3D
constellation. Searches and reads work, but they do not currently pulse,
highlight, or focus stars. Restoring the old system's visible-agent behavior
is an explicit port requirement.

A removable `vrbrain.knowledge.agent-activity` plugin should consume typed
knowledge-activity events; the gateway must not call the constellation
renderer directly. The intended behavior is:

- searching pulses the bounded top-result stars;
- reading highlights the selected note and draws a temporary agent-to-note
  trail;
- explicit `knowledge.open` or `knowledge.focus` requests may move the camera
  and open the reader;
- background searches and reads never steal camera focus;
- each agent/session receives a stable visible color and independently fading
  activity trail;
- only bounded operation metadata and note IDs are exposed to the visualizer;
  tokens, full note content, and sensitive query text are not persisted.

The future MCP bridge should map its knowledge tools onto the authenticated
gateway and publish the same typed activity events. It must not restore the
legacy raw TCP authority, arbitrary shell execution, or direct vault writes.
The constellation remains fully functional when the activity plugin is
disabled.

## Touchstone integration and credit

**Touchstone by kalanik0a**  
<https://github.com/kalanik0a/touchstone>

Touchstone supplies hardware-bound privilege consent for AI coding agents. VR
Brain contains an adapter, not a replacement:

- detects `ts-run`, `ts-sudo`, `ts-ssh`, `ts-scp`, and `ts-sftp`;
- invokes one exact wrapper with a bounded argument list and no shell
  interpolation;
- permits one active consent request and captures bounded output;
- never bypasses Touchstone review, policy, PAM, signed audit, or
  FIDO2/YubiKey.

The inspected Touchstone repository is MIT licensed; no Touchstone source was
vendored. The app surface prominently displays “Touchstone by kalanik0a,” its
upstream URL, its independent-project status, and the trust boundary. On this
machine the tools were not installed, so the tested surface correctly showed
an explicit idle state.

## Intellio integration and credit

**Intellio by kalanik0a**  
<https://github.com/kalanik0a/Intellio>

The adapter was engineered against the local repository at
`/home/thorn/Documents/Intellio` and its public HTTP boundary:

- `GET /api/health`;
- `POST /api/validate`;
- `POST /api/report`.

No Intellio source was copied or vendored. The inspected checkout contained no
license file, so the separation is deliberate. Cleartext HTTP is accepted only
for a literal loopback IP; remote origins require HTTPS. Redirects are off,
responses are bounded JSON, credentials in cited source URLs are removed, and
an optional bearer comes only from `INTELLIO_BEARER_TOKEN`.

The app surface prominently displays “Intellio by kalanik0a” and the upstream
URL. Visible “Generate + ledger” creates a normalized evidence record.
Agent access is limited to status and subject validation, so a costly report
cannot be generated invisibly. Intellio was not running during the visual
pass; the feature correctly showed offline without affecting the other 24
plugins.

## Verification

The final serial solution build has zero warnings and zero errors. Automated
coverage totals 362 assertions:

- kernel: 16;
- Earth: 209;
- knowledge and constellation layout: 52;
- intelligence: 48;
- agent/integration security: 37.

Live gateway testing additionally verified invalid-token rejection, `0600`
descriptor/socket permissions, strict JSON-RPC, status/read/query methods,
Earth navigation, workspace focus, Touchstone state, Intellio state, and stale
socket cleanup.

Desktop rendering was inspected on the RX 6700 XT. The z3 atlas loaded 64/64
tiles, active attribution was visible, North America centered correctly for
the Chicago focus, both credited integration surfaces were opened through the
real gateway, and the full-vault constellation was inspected in the running
Godot application. OpenXR could not initialize in this desktop validation
environment because its runtime library dependency was unavailable, so the
documented desktop fallback was exercised; headset validation remains a
separate physical-device check.

## Carry-forward direction

Former features such as feeds, browsers, terminals,
weather/radar/fire/flight/cyber layers, voice, fleet actions, briefings, and
National Map tools now have explicit plugin seams. They should be ported as
independent data, view, workspace, or Touchstone-gated action plugins—not
folded back into `RuntimeKernel`.

Related:

- [[vr-brain - Overview]]
- [[vr-brain - Architecture]]
- [[vr-brain - Engineering Run Through 2026-07-26]]
- [[Earth - Geo Engine Rewrite]]
- [[Earth - National Map Viewer Target]]
