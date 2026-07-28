---
summary: Engineering record for the two-session vr-brain overhaul through 2026-07-26, covering the intelligence ledger, spatial workspace, Earth precision renderer, runtime diagnostics, debugging decisions, verification, and remaining work.
status: active
tags: [project, vr-brain, engineering-log, intelligence, geospatial, godot]
created: 2026-07-26
updated: 2026-07-26
---

# vr-brain Engineering Run Through 2026-07-26

## Purpose

Preserve the useful engineering context from the current and immediately
preceding Codex sessions so work can resume without rediscovering architecture,
failure modes, or validation results. This is an implementation and decision
record, not a transcript or private chain-of-thought dump.

The scope grew from Earth renderer controls into three connected systems:

1. a durable evidence and personal-intelligence layer joining the knowledge
   base to live events;
2. an in-world spatial desktop for terminals, browsers, arbitrary applications,
   operations, and agent workflows;
3. a building-scale WGS 84 Earth renderer that can display the resulting
   correlations at their real locations.

## Source State

- Repository: `~/Downloads/vr-brain`
- Branch: `main`
- HEAD while this note was written: `a76b23f`
  (`update README for the Earth geo-engine rewrite`)
- Runtime: Godot 4.7 Mono, .NET 8, Forward+, desktop fallback and OpenXR paths
- The implementation is saved in the working tree but is not consolidated into
  a new commit by this note.
- The tracked diff at capture time contained about 8,317 insertions and 1,287
  deletions across 47 existing files.
- New project implementation and tests total about 21,242 lines across the
  intelligence, Earth, application-window, workspace, and observability
  subsystems.
- Existing unrelated security artifacts such as `bedside_initial.txt`,
  `cjChk.txt`, `cjX.txt`, `cobblestone_full.nmap`, and the `nmap*.txt` files
  were not part of this work and must not be included in a vr-brain commit.
- No API keys, bearer tokens, environment values, or other secrets are copied
  into this note.

## Product Direction

The project is no longer only a 3D visualization of notes. The intended system
is a personal spatial intelligence environment:

- the knowledge base provides people, places, systems, projects, interests, and
  historical context;
- live feeds provide time-varying external observations;
- an LLM correlates both through inspectable tools rather than opaque prompts;
- generated conclusions retain evidence, time, confidence, conflicts, and KB
  influence;
- Earth is the spatial evidence surface, down to a building or roof when data
  allows;
- changes proposed by the agent enter a review inbox rather than silently
  rewriting the vault;
- terminals, browsers, desktop applications, dashboards, and agent sessions are
  persistent in-world work surfaces rather than external host windows.

The main query this architecture is intended to answer is:

> What changed in the real world, why does it matter to this knowledge base,
> what evidence supports that conclusion, and where exactly can it be inspected?

## Decision Record

### Evidence is data, never instruction

Feed bodies, event summaries, web text, and model-produced fields are treated as
untrusted evidence. They are normalized, length-bounded, credential-stripped,
hashed, and checked for prompt-injection patterns before entering retrieval.
This prevents a hostile feed item from becoming an executable instruction just
because an LLM later searches it.

### Events need durable identity and history

Rendering a fire, flight, quake, or alert directly from the latest API response
loses temporal state. All supported observations now normalize into stable
records with revisions. Authoritative snapshots resolve records that disappear;
non-authoritative observations can update or explicitly resolve/reopen without
erasing history.

### Retrieval must remain inspectable

Neural similarity is useful but insufficient on its own. Retrieval combines
embedding cosine score, lexical matching, wikilink graph degree, recency,
geography, severity, and source confidence. Score components and reasons remain
visible to callers so the relevance engine can explain why a result ranked.

### Synthesis cannot bypass human review

Dossiers, briefings, note links, and event-derived tasks are proposals. The
`KnowledgeReview` inbox is the write boundary. Approval applies a proposal
through `VaultSync`; rejection remains auditable. Background analysis and MCP
tools cannot silently mutate the vault.

### WGS 84 is the Earth contract

The geographic contract is WGS 84 geodetic latitude, longitude, and ellipsoidal
height (EPSG:4979), converted in doubles to WGS 84 geocentric ECEF
(EPSG:4978). Web Mercator is only a source-tile projection, not the planet
geometry. Orthometric DEM heights are converted through EGM96 before placement.

### ENU is a render frame, not a second coordinate system

Authoritative positions stay geodetic/ECEF. At high zoom they are transformed
into a camera-relative east/north/up frame and periodically rebased. This keeps
Godot float vertices near zero without corrupting stored coordinates or making
annotations dependent on a temporary origin.

### High zoom needs a protected focus path

Screen-space-error refinement alone can spend the entire adaptive budget on
peripheral roots. The selected/`earth_goto` coordinate therefore receives a
minimum altitude-derived LOD and reserved leaf capacity. Peripheral detail
continues to obey normal SSE and adaptive budgets.

### 3D Tiles is an optional content path

The core globe does not depend on Cesium ion or a native plugin. A managed OGC
3D Tiles loader handles the explicit hierarchy and common payloads. Battle
Road/Cesium Native remains an optional capability for unsupported formats and
implicit tiling. Unsupported features are reported instead of silently
pretending to render them.

### In-world applications share one surface model

Terminals, browsers, arbitrary XDG applications, and remote RFB sessions expose
the same `IWorkspaceSurface` contract. Layout, focus, snapshots, context,
capture, performance governance, and MCP control are implemented once around
that contract.

### Runtime diagnostics must not own feature behavior

The flight computer observes and adjusts bounded quality controls, but Earth,
the constellation, surfaces, and agents remain functional if diagnostics are
disabled. Exported support bundles are credential-free and exclude note,
terminal, and browser content.

### Bursty input must select immediately and commit expensive work later

Renderer selection should feel immediate, while tile cancellation, tree
teardown, cache/source changes, and config writes should happen once after a
short quiet interval. `CoalescedTransition<T>` implements this pattern. The
same rule should be reused for future rebuild-heavy settings.

## Implemented: Intelligence Layer

### Durable event ledger

Added `src/Brain/Intelligence/`:

- `IntelligenceModels.cs` defines evidence, normalized events, revisions,
  batches, queries, relationships, KB chunks, insights, storylines, tracked
  locations, relevance profiles, deviations, proposals, and evaluation models.
- `IntelligenceSafety.cs` normalizes identifiers and fields, removes URI
  credentials, rejects invalid spatial values, computes SHA-256 content hashes,
  and flags instruction overrides and tool requests.
- `EventLedger.cs` is Godot-independent and persists:
  - current event state in `events.snapshot.json.gz`;
  - mutations between checkpoints in `events.journal.jsonl`;
  - bounded revision history;
  - source checkpoints and active IDs;
  - monotonically increasing sequence numbers.
- `EventStore.cs` is the Godot node and main-thread ingestion boundary. It
  processes bounded batches, checkpoints periodically, prunes to configured
  limits, and publishes change notifications.

Each event can retain:

- stable ID, kind, lifecycle status, revision, and content hash;
- source ID/name/URI and source trust;
- started, observed, updated, expiry, and ended timestamps;
- latitude, longitude, altitude, and affected radius;
- severity and confidence;
- entities, tags, structured facts, linked event IDs, and KB references;
- one or more evidence references with their own retrieval time, excerpt,
  trust, hash, and safety flags.

### Event ingestion

The following sources now publish normalized batches:

- `Flights`: OpenSky global or adsb.lol radius aircraft state;
- `FiresLayer`: FIRMS fire detections;
- `QuakesLayer`: USGS earthquakes;
- `WeatherAlertsLayer`: weather-alert geometry and lifecycle;
- `CyberThreatLayer` and `ThreatGlobe`: geolocated threat observations;
- `VaultSync` snapshots: feed items, current KB note state, note updates, and
  note deletions;
- MCP `earth_annotate`: durable LLM/KB/event spatial correlations.

Aircraft position churn is deliberately not journaled every poll. It is
interval-bounded while current position remains queryable. OpenSky HTTP 429 is
handled as rate limiting with `Retry-After` support and bounded exponential
backoff instead of dumping a full exception trace every 30 seconds.

### Embeddings and hybrid retrieval

- `EmbeddingService.cs` can start a private `llama-server` with
  `nomic-ai/nomic-embed-text-v1.5-GGUF:Q4_K_M`, or use a configured
  OpenAI-compatible embedding endpoint.
- Tokens for configured endpoints are read from an environment-variable name,
  not copied into config output or MCP status.
- `HybridRetrieval.cs` chunks notes at approximately 1,100 characters with
  180-character overlap.
- Embeddings are fingerprinted and cached in
  `user://intelligence/embeddings.bin`.
- Knowledge ranking combines neural, lexical, wikilink graph, and recency
  factors. Event ranking additionally considers geography, source confidence,
  severity, time, entities, and tags.
- Lexical fallback remains functional while the neural provider is unavailable
  or still indexing.

### Personal relevance, stories, and time

`IntelligenceEngine.cs`:

- scores live events against tracked terms, entities, locations, stories, and
  vault material;
- builds evolving storylines and source diversity;
- records why an event matters, not only a scalar score;
- reports contradictory facts and conflicting reports;
- computes temporal deviations and "what changed since" views from revisions;
- persists the personal relevance profile separately from the vault;
- never writes a note directly.

The desktop/XR `IntelligencePanel` provides overview, story, event, and review
views. It exposes evidence, source freshness, confidence, safety flags,
relationships, KB passages, and proposal state rather than presenting an
unsupported generated paragraph.

### Closed-loop knowledge

`KnowledgeReview.cs` creates and persists reviewable:

- dossiers;
- briefings;
- event-derived tasks;
- note/link proposals.

Applying or rejecting a proposal is explicit and remains in the inbox history.
Daily briefing generation now follows this evidence-first proposal path rather
than bypassing review.

### Evaluation

`IntelligenceEvaluationRunner.cs` and
`tests/intelligence-evaluation.json` maintain retrieval, citation/evidence,
personal relevance, and hostile-prompt cases. The standalone
`tests/IntelligenceTests` suite covers stable IDs, safety normalization,
credential stripping, content hashes, invalid coordinates, add/update/resolve/
reopen lifecycle, compressed checkpoint recovery, append-journal recovery, and
WGS 84 distance.

### Intelligence MCP tools

Added:

- `semantic_search`
- `search_events`
- `related_events`
- `explain_relevance`
- `list_stories`
- `track_story`
- `track_interest`
- `what_changed`
- `create_dossier`
- `create_briefing`
- `create_event_task`
- `review_inbox`
- `review_proposal`
- `intelligence_status`
- `run_intelligence_evaluation`

## Implemented: Earth System

### Full geodetic foundation

- The globe surface is a WGS 84 ellipsoid using semi-major axis 6,378,137 m
  and the WGS 84 flattening/polar radius, not a mean-radius sphere.
- CPU placement uses double-precision geodetic-to-ECEF and ECEF-to-geodetic
  conversion.
- `CrsTransform.cs` supports OGC:CRS84/EPSG:4326/4979, EPSG:4978 ECEF, and
  EPSG:3857 Web Mercator.
- `assets/egm96_15.gtx` is the NGA EGM96 15-minute geoid grid distributed by
  OSGeo/PROJ. `Egm96Geoid.cs` reads its big-endian GTX values and bilinearly
  converts orthometric height using `h = H + N`.
- The source and SHA-256 are recorded in `assets/egm96_15.README.md`.
- `SolarEphemeris.cs` provides date-aware subsolar latitude/longitude and
  equation-of-time values for lighting.

### Precision and LOD

- Close tiles use a camera-relative ENU root derived from WGS 84 ECEF doubles.
- The frame rebases when drift exceeds the configured threshold, default 2 km.
- Imagery can refine through z22 where the provider has data.
- `EarthLodPolicy` enforces a protected focus target:
  - about z18 at a 1.5 km building-scale approach;
  - z22 at roughly 100 m;
  - never below the existing coarse frontier or configured max zoom.
- Precision selection reserves focus-leaf capacity before peripheral roots.
- The adaptive governor keeps at least 32 tile slots in precision mode after a
  low-FPS collapse, avoiding the earlier root-only starvation at 500 m.
- `EarthCameraClipPolicy` derives a local-horizon far plane and a stable
  near/far ratio. It is applied synchronously on `earth_goto`, preventing the
  temporary invalid frustum seen when near changed before far.

### Tile streaming and terrain

- `EarthTileKey.cs`: normalized Web Mercator z/x/y identity, ancestry, bounds,
  and ground resolution.
- `EarthTileCache.cs`: bounded downloads and reads, signature validation,
  checksums, atomic writes, retries, negative caching, host circuit breakers,
  and background pruning.
- Defaults are 96 leaves, six requests, four uploads, 1 GiB, and 8,192 files;
  adaptive effective budgets shrink and recover with frame pressure.
- Requests are cancellable and prioritized by focus and on-screen error.
- Parent imagery and terrain remain as placeholders and crossfade when sharper
  content arrives, preventing holes during LOD replacement.
- A shared grid mesh and vertex-shader displacement replace per-tile CPU mesh
  generation.
- Terrain samples AWS Terrarium ancestors toward z15 where available, filters
  the DEM once, converts EGM96 orthometric heights, and caches processed
  heightfields/textures.
- `terrain_tile.gdshader` handles ellipsoidal displacement, parent/detail
  blending, skirts, and normal reconstruction.

### Renderer modes and Earth-only input

`I` now cycles four explicit modes while Earth is active:

1. satellite plus terrain;
2. street map plus terrain;
3. satellite flat;
4. street map flat.

`Shift+I` reverses. Selection updates the overview texture immediately.
`CoalescedTransition<RenderMode>` waits 180 ms before one expensive tile-tree
commit and config write. Cycling back to the already-applied mode cancels the
pending rebuild entirely.

`Pointer.HandleEarthKey` uses the persistent `Keybinds.Matches` registry rather
than raw action strings. Earth controls no longer fire in the constellation and
continue to work after rebinding:

- `G`: enter Earth; `Shift+G`: return to the constellation;
- `Z`: zoom; `Shift+Z`: reverse;
- `I`: renderer; `Shift+I`: reverse;
- `F3`: place/event search;
- `F4`: distance/area measurement;
- `N`: north-up;
- `0`: home;
- `U`: Earth HUD;
- `1` through `9`: data-layer toggles.

Settings now include a destructive but explicit "remove all pins" action.
`Earth.ClearPins()` removes persistent user pins, ends pin naming, frees pin
nodes, and saves the empty pin file without touching live feed markers.

### Earth explorer and interoperability

`EarthExplorer.cs` adds:

- coordinate, local KB place, event, and remote Nominatim search;
- attributed result candidates and bounded disk cache;
- back/forward travel history;
- current WGS 84 and terrain/LOD diagnostics;
- north-up and home;
- geodesic distance and area measurement reconstructed after ENU rebases.

`GeoJsonLayer.cs` loads watched local RFC 7946 files and OGC API Features
responses. It supports point, line, polygon, multi-geometry, and geometry
collection data plus SimpleStyle colors/opacity.

`NationalMapLayer.cs` renders USGS 3DEP visualization modes and now validates
HTTP status, content type context, and the PNG signature before asking Godot to
decode. This removes the earlier cascade of "Not a PNG file" engine errors when
the service returned text/JSON.

`UsgsElevation.cs` exposes official EPQS point elevation. MCP adds
`earth_transform` and `earth_elevation`.

### Building and 3D content

`OsmBuildingsLayer.cs`:

- queries Overpass only at close camera heights;
- rate-limits globally and caches responses;
- retains authoritative WGS 84 footprints;
- extrudes buildings and building parts in the active ENU frame;
- rebuilds after a rebase;
- resolves a coordinate to a loaded footprint/roof with OSM feature ID,
  address/name, and source provenance.

`Ogc3dTilesLayer.cs`:

- traverses explicit OGC 3D Tiles 1.0/1.1 trees using geometric error/SSE;
- supports region, box, and sphere bounds;
- supports `ADD` and `REPLACE` refinement;
- loads embedded GLB, B3DM including `RTC_CENTER`, PNTS point clouds, and
  external tilesets;
- maps content transforms from ECEF doubles into the current ENU frame;
- bounds tileset/content/point sizes, retries failures, caches content, applies
  request/build/resident budgets, and exposes diagnostics;
- reads tokens only from the configured environment variable;
- detects Battle Road/Cesium Native classes for optional capabilities;
- reports implicit tiling and unsupported I3DM/CMPT rather than claiming them.

### Spatial event workflow

`IntelligenceMapLayer.cs` clusters located ledger events at overview scale and
refines toward individual evidence-bearing markers. At close range an
annotation can retain both the original observation and a building surface
anchor.

The intended MCP workflow is:

1. `earth_geocode` resolves an address or place.
2. `search_events`, `related_events`, and `explain_relevance` correlate it.
3. `earth_annotate` records title, summary, event IDs, KB refs, confidence,
   source URI, radius, and optional building feature.
4. `earth_jump_event` moves to it.
5. `earth_surface` reports loaded building/terrain context.
6. `earth_nearby` inspects surrounding evidence.
7. `earth_annotation_state` resolves or reopens it without deleting history.

KB notes join the map automatically from frontmatter using scalar
`latitude`/`longitude`, `location: [lat, lon]`, `geo: [lat, lon]`, or GeoJSON
`coordinates: [lon, lat]`, plus optional altitude and radius.

## Implemented: Spatial Workspace and Applications

### Arbitrary desktop applications

`DesktopApps.cs`, `DesktopAppWindows.cs`, and `DesktopAppProfiles.cs`:

- discover XDG desktop entries with desktop-file precedence;
- parse executable fields without shell interpolation;
- route `Terminal=true` applications into native terminal panels;
- launch graphical applications in private headless sway/XWayland sessions;
- provide private D-Bus and localhost-only wayvnc;
- do not pass the host display into the application;
- support per-app resolution, FPS, clipboard, audio, network, vault access,
  keep-alive, and isolation profiles;
- offer display isolation by default and optional bubblewrap sandboxing;
- keep sessions alive across vr-brain restarts and reattach them;
- show native secondary windows/dialogs through the same application surface;
- rank applications using favorites and recency.

The launcher is `F1`; `Ctrl+D` toggles a favorite. The agent receives
`list_applications` and `open_application`.

### Unified workspace

`IWorkspaceSurface` is implemented by terminal, browser, application, and
remote surfaces. `SpatialWorkspace` adds:

- live overview and bottom dock;
- wall, arc, and focus layouts;
- left/right snapping;
- complete workspace snapshots and restore;
- unclean-session recovery journal;
- note and WGS 84 context attachment;
- focused-surface capture into `VR Brain/Captures/`;
- optional Tesseract OCR;
- dropped-file import and XDG opening inside the world;
- remote `vnc://host:port` surfaces;
- camera-following tablet mode;
- notification history;
- foreground/background surface FPS governance;
- basic automation rules.

`WorkspaceCommands` provides a shared command registry for the UI and palette.
MCP receives `list_surfaces` and `workspace`.

### Unified palette and keybindings

`SearchPanel` is now a desktop/XR command palette with modes for knowledge,
commands, applications, sessions, and web. Prefixes select modes, while normal
queries merge ranked results. It uses `KnowledgeIndex` for title/body/tag/link
search and recent-note ranking.

`Keybinds.cs` is the single metadata-rich desktop binding registry. Overrides
persist in `user://keybinds.cfg`; Settings can capture, replace, reset one, or
reset all bindings. The control/help surfaces are generated from this registry
instead of relying on duplicated hard-coded labels.

## Implemented: Agent, MCP, and Operations

### Claude and Codex

`ClaudeAgent` now supports either locally authenticated CLI through the same
visual panel and embedded MCP boundary:

- Claude runs with read-only native tools and an in-world permission prompt;
- Codex runs in read-only sandbox mode and receives only the ephemeral vr-brain
  MCP override, preserving the user's normal `CODEX_HOME` and authentication;
- resumed runs receive the current MCP port instead of retaining a stale port;
- both can visibly open notes, terminals, browsers, and applications;
- stderr is captured and shown for failed runs rather than discarded;
- Codex JSONL events are parsed for thread, agent message, tool, usage, and
  error state.

The embedded server is newline-delimited JSON-RPC on an ephemeral localhost TCP
port. `socat` provides stdio transport. The separate `codex_apps` startup error
was not a failure of this server.

The user-level Codex Godot MCP registration was also saved and validated:

- command: `npx -y @coding-solo/godot-mcp`;
- `GODOT_PATH` points to the actual Nix Godot 4.7 binary;
- the package successfully started on stdio.

For running-world state, the embedded vr-brain MCP remained more direct than
an editor-oriented MCP because it can inspect application-specific Earth,
event, workspace, and renderer state.

### Flight computer and Grafana

`RuntimeTelemetry.cs`, `FlightComputer.cs`, and `MissionControlPanel.cs` add:

- bounded FPS/frame-time metrics and percentiles;
- draw, primitive, object, memory, resource, and orphan counters;
- subsystem health matrix;
- rotating JSONL black box and five-second heartbeat;
- clean/unclean shutdown detection;
- foreground/background exception capture;
- hysteretic five-stage adaptive quality with slow recovery;
- sanitized `runtime_status`, `adaptive_quality`, and `export_diagnostics`
  MCP tools;
- redacted diagnostic ZIPs that exclude vault, terminal, browser, token, and
  environment content.

`GrafanaSoc.cs` adds an in-world status surface and browser-based sign-in.
Optional service-account telemetry reads its token from an environment variable
and exposes only credential-free status through MCP.

## Critical Debugging Record

### Repeated `I` made the application impossible to close

Observed symptom:

- rapidly pressing `I` appeared to crash vr-brain;
- the Godot process stayed in a running/high-CPU state and could not be closed
  normally.

Root cause:

```csharp
while (_stack.GetChildCount() > 5)
    _stack.GetChild(0).QueueFree();
```

Godot defers `QueueFree()` until the end of the frame. The child remained
attached, so `GetChildCount()` never changed and the sixth toast entered an
infinite loop on the main thread.

Fix:

- detach the oldest child with `RemoveChild(oldest)` before `QueueFree()`;
- coalesce notification-history writes for 250 ms instead of rewriting JSON on
  every keypress;
- flush dirty notification history during `_ExitTree`;
- coalesce renderer commits for 180 ms;
- use `Keybinds.Matches` for the actual Earth input path.

Verification:

- the stuck process was terminated with SIGTERM;
- the app was relaunched;
- 30 immediate renderer MCP transitions completed;
- 40 compositor shortcuts were sent as an additional burst;
- 12 paced real `I` shortcuts traversed the exact Pointer -> Toasts -> Earth
  path, exceeding the old six-toast failure point;
- all 12 renderer transitions committed;
- MCP remained responsive afterward;
- the original `satellite flat` setting was restored;
- the window then closed normally;
- no Godot or `socat` process remained.

### Precision tile budget starvation

At about 500 m the adaptive tile budget fell to 16. Coarse roots consumed every
slot, so the protected focus path never reached z18+.

Fix:

- precision mode has a bounded 32-tile effective floor;
- LOD selection reserves `3 * forcedFocusLevels` leaf capacity before accepting
  peripheral roots.

Live result:

- z20/z21 at approximately 500 m;
- z18 at 1.5 km;
- ENU drift around 0.03 m;
- no failed requests in the inspected run.

### Close-goto frustum errors

`earth_goto` lowered the camera near plane while the far plane remained at the
interplanetary default for several frames. Godot logged
`create_frustum_points` failures.

Fix:

- derive near and far together from camera altitude and the local geometric
  horizon;
- apply synchronously in `RequestGoto` and normal tile updates.

The rerun produced no frustum errors.

### National Map non-PNG response

The 3DEP endpoint sometimes returned an error document while the caller
unconditionally called `LoadPngFromBuffer`, causing multiple engine-level PNG
errors.

Fix:

- validate HTTP success and PNG magic bytes first;
- log a bounded response summary instead of invoking the decoder.

### OpenSky anonymous rate limiting

Anonymous worldwide polling returned HTTP 429 every refresh. The poll loop now
honors `Retry-After` when supplied and otherwise uses bounded exponential
backoff up to 30 minutes. This is expected source degradation, not an
application crash.

## Live Earth Validation

At the Willis Tower location:

- Overpass produced the configured cap of 3,000 footprints and about 84,000
  triangles;
- `earth_surface` snapped to OSM way `137162297` at an approximately 355 m
  roof height and returned provider provenance;
- a temporary evidence-bearing roof annotation was created;
- `earth_nearby` returned it;
- diagnostics reported one building anchor;
- the annotation was then resolved with an audit reason so no active test marker
  was left behind.

The run demonstrated end-to-end:

`WGS 84 coordinate -> geocoder/building -> durable event -> map marker ->
building roof -> nearby evidence -> lifecycle resolution`.

## Verification Summary

Commands:

```sh
dotnet build VrBrain.sln --no-restore
dotnet run --project tests/EarthFoundationTests/EarthFoundationTests.csproj --no-restore
dotnet run --project tests/IntelligenceTests/IntelligenceTests.csproj --no-restore
```

Results at capture time:

- build succeeded with 0 warnings and 0 errors;
- Earth foundation tests passed: 132 assertions;
- intelligence tests passed: 20 assertions;
- total: 152 assertions;
- `git diff --check` passed;
- exact repeated-`I` runtime regression passed;
- the app was intentionally left stopped after validation.

Earth tests cover tile bounds/ancestry, z18-z22 focus policy, transition
coalescing, close-camera clipping, geocoder provenance, adaptive streaming
hysteresis/floors, solar plausibility, WGS 84 vault frontmatter, and coordinate
order. Intelligence tests cover durable identity, safety, lifecycle, recovery,
and geographic distance.

## Known Issues and Risks

### Satellite detail source is currently wrong when an ArcGIS key is present

`Earth.TileUrl()` still chooses:

```text
/arcgis/imagery/labels/static/tile/{z}/{y}/{x}
```

for keyed satellite detail. ArcGIS describes this as a transparent reference
label layer intended to be overlaid on imagery. Cached samples were identical,
2,127-byte, fully transparent 512x512 PNGs. This explains close-detail frames
that appeared white/blank and the historical case where the notification said
the renderer changed but Earth did not visibly change.

Next fix:

- use keyed static `arcgis/streets` only for street detail (512 px);
- use classic `World_Imagery/MapServer/tile` for satellite detail (256 px);
- derive ground-resolution math from the selected provider's actual tile size,
  not merely whether an API key exists;
- reject a fully transparent payload when it is being used as a required
  basemap;
- rerun side-by-side satellite/street screenshots at orbit, 1.5 km, and 500 m.

Do not clear the whole cache preemptively. A corrected URL naturally receives a
different cache key.

### Close-view atmosphere/decor needs another visual pass

An attempted precision-mode atmosphere/title visibility guard did not explain
the entire white close frame. Add explicit `earth_status` fields for atmosphere
visibility, title visibility, and inside-shell state before changing more
rendering code. Fix the transparent imagery source first because it is a
confirmed defect.

### OSM building hierarchy can overlap

Overpass returns both parent building footprints and `building:part` geometry.
Rendering both can overlap and produce z-fighting. Prefer parts when a parent is
fully represented, while retaining the parent as provenance.

### Normal shutdown still reports Godot resource leaks

The final graceful test exit completed, but Godot reported leaked CanvasItem,
Texture, shaped-text/font RIDs, and ObjectDB instances. They did not block exit,
but ownership should be audited, especially dynamically created UI, textures,
and long-lived surface sessions.

### External-source limitations

- OpenSky anonymous worldwide access remains quota-limited even with correct
  backoff.
- Heat and other public layers can time out independently.
- OSM Overpass is not a bulk production building service; cache and request
  discipline remain mandatory.
- 3D Tiles implicit tiling, I3DM, CMPT, Draco, and some external glTF resources
  still need the optional native backend or additional managed support.
- A real `[tiles3d] url` was not configured during the final runtime.
- Local neural retrieval needs `llama-server` and the model download before it
  can become neural-ready; lexical fallback remains available.

### Validation gaps

- No headset/OpenXR visual acceptance pass was completed for the final combined
  system.
- No production photogrammetry tileset was streamed end-to-end.
- High-zoom imagery still needs validation after the ArcGIS source correction.
- Godot shutdown leak diagnostics need a focused verbose run.
- The large working tree should be committed in coherent, reviewable groups
  after separating unrelated files.

## Recommended Resume Order

1. Correct the keyed ArcGIS satellite detail URL and provider-specific tile
   pixel size.
2. Add transparent-basemap rejection and source/visibility diagnostics.
3. Relaunch through the embedded MCP and capture satellite versus street at
   three altitudes.
4. Audit shutdown RID/ObjectDB leaks with a minimal Earth test, then the full
   spatial workspace.
5. Suppress duplicate parent OSM footprints when building parts are present.
6. Configure one legal OGC 3D Tiles test endpoint and validate transforms,
   refinement, cache recovery, and building-level event anchoring.
7. Run the full live intelligence evaluation after embeddings are neural-ready.
8. Perform an OpenXR acceptance pass for input scope, readable UI, comfort,
   frame pacing, and precision Earth transitions.
9. Split and commit the project work by subsystem: intelligence, spatial
   workspace/apps, observability, Earth foundation, Earth 3D content, and input/
   crash fixes.

## File Inventory

### Core integration and documentation

- `README.md`
- `VrBrain.csproj`
- `flake.nix`
- `scenes/Main.tscn`
- `assets/earth.gdshader`
- `assets/terrain_tile.gdshader`
- `assets/egm96_15.gtx`
- `assets/egm96_15.README.md`

### Intelligence

- `src/Brain/Intelligence/EmbeddingService.cs`
- `src/Brain/Intelligence/EventLedger.cs`
- `src/Brain/Intelligence/EventStore.cs`
- `src/Brain/Intelligence/HybridRetrieval.cs`
- `src/Brain/Intelligence/IntelligenceEngine.cs`
- `src/Brain/Intelligence/IntelligenceEvaluationRunner.cs`
- `src/Brain/Intelligence/IntelligenceModels.cs`
- `src/Brain/Intelligence/IntelligenceSafety.cs`
- `src/Brain/Intelligence/KnowledgeReview.cs`
- `src/Brain/IntelligencePanel.cs`
- `tests/IntelligenceTests/`
- `tests/intelligence-evaluation.json`

### Earth and geospatial

- `src/Brain/Earth.cs`
- `src/Brain/EarthExplorer.cs`
- `src/Brain/Geo/CoalescedTransition.cs`
- `src/Brain/Geo/CrsTransform.cs`
- `src/Brain/Geo/CubeSphere.cs`
- `src/Brain/Geo/EarthCameraClipPolicy.cs`
- `src/Brain/Geo/EarthLodPolicy.cs`
- `src/Brain/Geo/EarthStreamingGovernor.cs`
- `src/Brain/Geo/EarthTileCache.cs`
- `src/Brain/Geo/EarthTileKey.cs`
- `src/Brain/Geo/Egm96Geoid.cs`
- `src/Brain/Geo/Geo.cs`
- `src/Brain/Geo/GeoLayer.cs`
- `src/Brain/Geo/GeoLocationResolver.cs`
- `src/Brain/Geo/SolarEphemeris.cs`
- `src/Brain/Geo/TerrainFilter.cs`
- `src/Brain/Geo/UsgsElevation.cs`
- `src/Brain/Geo/Layers/GeoJsonLayer.cs`
- `src/Brain/Geo/Layers/IntelligenceMapLayer.cs`
- `src/Brain/Geo/Layers/NationalMapLayer.cs`
- `src/Brain/Geo/Layers/Ogc3dTilesLayer.cs`
- `src/Brain/Geo/Layers/OsmBuildingsLayer.cs`
- the modified weather, quake, radar, cyber, fire, WiGLE, wind, and heat layers
- `scenes/EarthTest.tscn`
- `src/Tools/EarthTestMain.cs`
- `src/Tools/FreeFlyCam.cs`
- `tests/EarthFoundationTests/`

### Spatial desktop and user interface

- `src/Brain/DesktopAppProfiles.cs`
- `src/Brain/DesktopAppWindows.cs`
- `src/Brain/DesktopApps.cs`
- `src/Brain/Keybinds.cs`
- `src/Brain/KnowledgeIndex.cs`
- `src/Brain/SpatialWorkspace.cs`
- `src/Brain/SpatialWorkspaceUi.cs`
- `src/Brain/WorkspaceCommands.cs`
- `src/Brain/WorkspaceSurface.cs`
- `src/Brain/WorldLevelController.cs`
- modified browser, terminal, reader, search, settings, HUD, pointer, RFB,
  postcard, and voice integration files

### Operations and agents

- `src/Brain/FlightComputer.cs`
- `src/Brain/GrafanaSoc.cs`
- `src/Brain/MissionControlPanel.cs`
- `src/Brain/RuntimeTelemetry.cs`
- `scenes/FlightComputerTest.tscn`
- `src/Tools/FlightComputerTestMain.cs`
- modified `ClaudeAgent`, `ClaudeModels`, `McpServer`, `DailyBriefing`,
  `Flights`, `Fleet`, `ThreatGlobe`, `VaultParser`, `VaultNote`, and
  `VaultSync`

## Runtime State Paths

Important durable state added or expanded:

- `user://intelligence/ledger/events.snapshot.json.gz`
- `user://intelligence/ledger/events.journal.jsonl`
- `user://intelligence/embeddings.bin`
- `user://intelligence/profile.json`
- `user://intelligence/review-inbox.json`
- `user://earth/history.json`
- `user://earth/search/`
- `user://earth-overlays/`
- `user://spatial-workspace.json`
- `user://desktop-apps.json`
- `user://desktop-app-windows.json`
- `user://desktop-app-profiles.json`
- `user://desktop-app-sessions/`
- `user://notifications.json`
- `user://keybinds.cfg`
- `user://flight-session.json`
- `user://flight-recorder.jsonl`
- `user://diagnostics/`

## External References Used

- [OSGeo](https://www.osgeo.org/)
- [PROJ data](https://github.com/OSGeo/PROJ-data)
- [NGA EGM96 GTX distributed by OSGeo](https://download.osgeo.org/proj/vdatum/egm96_15/egm96_15.gtx)
- [Battle Road 3D Tiles for Godot](https://github.com/Battle-Road-Labs/3D-Tiles-For-Godot)
- [Cesium: Getting Started with 3D Tiles for Godot](https://cesium.com/blog/2025/05/01/getting-started-with-3d-tiles-for-godot/)
- [Cesium: Introducing 3D Tiles for Godot by Battle Road](https://cesium.com/blog/2025/05/01/introducing-3d-tiles-for-godot-by-battle-road/)
- [Godot discussion: building a Google Earth-like application](https://www.reddit.com/r/godot/comments/10j8pn4/can_godot_help_me_build_another_google_earth/)
- [ArcGIS Static Basemap Tiles](https://developers.arcgis.com/documentation/mapping-and-location-services/mapping/basemaps/introduction-static-basemap-tiles-service/)
- [ArcGIS imagery labels tile endpoint](https://developers.arcgis.com/rest/static-basemap-tiles/arcgis-imagery-labels-tile-get/)

## Related

- [[01 Maps/Projects Map|Projects Map]]
- [[07 Projects/vr-brain/vr-brain - Overview|vr-brain - Overview]]
- [[07 Projects/vr-brain/vr-brain - Architecture|vr-brain - Architecture]]
- [[07 Projects/vr-brain/Earth - Geo Engine Rewrite|Earth - Geo Engine Rewrite]]
- [[07 Projects/vr-brain/Earth - National Map Viewer Target|Earth - National Map Viewer Target]]
- [[06 Reference/Globe Data Source APIs|Globe Data Source APIs]]
- [[06 Reference/Terrain Rendering Optimization|Terrain Rendering Optimization]]
- [[06 Reference/High-Fidelity Planet Rendering (Godot)|High-Fidelity Planet Rendering (Godot)]]
- [[06 Reference/Model Context Protocol (MCP) Architecture|Model Context Protocol (MCP) Architecture]]
- [[06 Reference/Local Embedding Models for Semantic Search|Local Embedding Models for Semantic Search]]
