---
summary: Canonical multiplayer netcode patterns — client-server prediction/reconciliation, lag compensation, snapshot compression, rollback, tick rate, reliable UDP.
status: active
tags: [reference, gamedev, networking]
private: false
---

## Purpose

Generalized reference for multiplayer netcode patterns — the theory behind what [SkyDestroyer](kb://07-projects-skydestroyer-skydestroyer-overview)'s `BitStream`/`ConnectionManager`/`UpdateManager` already implement in practice, written down so future projects don't require re-deriving it from scratch. Compiled 2026-07-24.

## Client-Server Authoritative Model

The server is the sole source of truth (health, position, hit results) — clients send inputs/intents, never state, since a client-trusted model is trivially cheatable. At realistic latencies (50-100+ ms) a naive authoritative model makes local input feel laggy.

- **Client-side prediction**: the client immediately simulates its own input locally using the same movement/physics code the server runs, giving instant feedback instead of waiting a round-trip.
- **Server reconciliation**: the client buffers unacknowledged inputs with sequence numbers. When an authoritative snapshot arrives, the client snaps to the confirmed server state and **replays** every locally-buffered input newer than that snapshot on top of it. Divergence is usually smoothed with a small positional lerp rather than a hard snap.

Source: Gabriel Gambetta, *Client-Server Game Architecture* — https://www.gabrielgambetta.com/client-server-game-architecture.html

## Lag Compensation

The server **rewinds** other players' hitboxes to the point in time the shooter actually saw them (based on the shooter's reported latency + interpolation delay) before resolving a hitscan. Documented canonically for Source engine.

**Tradeoff — peeker's advantage**: rewinding favors the peeking/moving player. As they round a corner, their lag-compensated hitbox on the server is still positioned where the defender's screen showed them a moment ago, so the peeker can land shots the defender's client hasn't rendered as exposed yet — the mechanism behind "died behind cover." NVIDIA Research (2024) found the *defender's* latency affects peeker's advantage more than the peeker's own.

Source: Valve Developer Wiki, *Lag Compensation* — https://developer.valvesoftware.com/wiki/Lag_compensation

## Snapshot Interpolation vs Extrapolation

Remote entities render from a delayed, interpolated view, not snapped to the latest packet. Recommended buffer ≈ 3× the packet send interval under typical 2-5% loss (e.g. 300ms at 10 pkt/s + ~50ms jitter). Hermite interpolation (using velocity samples) beats plain linear — less visible jitter/rotation artifact. **Extrapolation** (predicting past the last snapshot to cut delay) is a fallback for missed packets only — it has no knowledge of the physics sim, so extrapolated objects can clip geometry before correction arrives.

Source: Glenn Fiedler, *Snapshot Interpolation* — https://gafferongames.com/post/snapshot_interpolation/

## Delta / Snapshot Compression

Encode each snapshot relative to a baseline the receiver has acknowledged (server tracks per-client acks, baselines roughly one RTT back) instead of resending full world state every tick. One "unchanged" bit per object dominates when few objects move; delta-encode indices for locality; adaptive-range value encoding (small deltas get fewer bits); quantized "smallest-three" quaternion encoding for orientation. Fiedler's worked example: a 901-object physics scene goes from 17.38 Mbps naive full-state @60Hz to ~256 Kbps combining these.

Source: Glenn Fiedler, *Snapshot Compression* — https://gafferongames.com/post/snapshot_compression/

## Rollback Netcode (GGPO-style)

Fundamentally different from server-authoritative prediction/reconciliation: **peer-to-peer, fully deterministic simulation**, no authoritative server. Every peer simulates each frame immediately using local input plus a **prediction of the remote input** (GGPO's default: assume the opponent keeps pressing whatever they pressed last frame). When the real remote input arrives and doesn't match, the peer **rolls back** to the last confirmed state and **resimulates** every frame since with the corrected input.

Requires bit-exact determinism across machines (same inputs → same outputs, always) — the same constraint as deterministic lockstep. Suits 1v1/small-N fighting games specifically because: rollback cost scales with player count (must resimulate everyone's logic per rollback) and prediction-window length, and a fighting game's small deterministic state is cheap to resimulate many times a frame — impractical for a large sim with physics/vehicles/many bots (SkyDestroyer's domain), which is exactly why it uses the authoritative-server model instead.

Sources: GGPO SDK — https://www.ggpo.net/ · SnapNet, *Netcode Architectures Part 2: Rollback* — https://www.snapnet.dev/blog/netcode-architectures-part-2-rollback/

## Interest Management / Area-of-Interest

Only send a client entity state relevant to it (nearby/in-zone), not full world state — without this, per-player cost grows with total entity count and roughly quadratically with concurrent nearby players. Standard implementations: **spatial grid** (cheap, but coarse cells overload dense areas) or **quadtree** (adapts to density, more complex, has to handle entities entering/leaving interest). Directly relevant to bot AI + vehicle sim at scale: AOI is what keeps per-client snapshot/delta cost bounded as entity count grows, independent of tick rate or compression scheme.

Sources: Dynetis Games, *Interest management for multiplayer online games* — https://www.dynetisgames.com/2017/04/05/interest-management-mog/ · ACM Computing Surveys, *Interest management for distributed virtual environments: A survey* — https://dl.acm.org/doi/10.1145/2535417

## Tick Rate

Fixed timestep for determinism and stable physics independent of frame-rate variance. Tick rate trades directly against bandwidth and CPU — doubling it roughly doubles both. Reference points: CS:GO/CS2 and Valorant up to 128 tick (7.8ms); Overwatch ~60 tick; older console CoD titles as low as 12-22 tick; MMORPGs typically 15-30 Hz combat, occasionally 60 Hz in bounded-entity instanced arenas. CS2 has moved toward "sub-tick" input timestamping to decouple hit-registration precision from raw tick rate.

**Deterministic lockstep** (classic RTS — early Age of Empires/StarCraft) is the alternative to snapshot sync: peers exchange only input commands, every peer simulates the full game identically. Bandwidth is essentially independent of entity count, but demands bit-exact determinism (same RNG seeds, no cross-platform/compiler float divergence) and a frame typically can't advance until all peers' inputs are confirmed — handled with playout-delay buffers and redundant input transmission over UDP, not TCP retransmission, to avoid stalling the whole sim on one slow peer.

Source: Glenn Fiedler, *Deterministic Lockstep* — https://gafferongames.com/post/deterministic_lockstep/

## UDP vs TCP for Games

UDP + a custom reliability layer beats TCP for latency-sensitive gameplay because TCP's guarantees actively hurt it: **head-of-line blocking** stalls newer, more relevant packets behind a retransmit of an old lost one, and TCP has no "this is stale, drop it" concept — exactly wrong when the newest position update supersedes an old one. Games build only the reliability they need on top of raw UDP:

- **Sequence numbers** on every packet, monotonically increasing, never reused.
- **Ack + ack-bitfield header**: each packet header carries the latest received remote sequence number plus a bitfield covering the prior N — Fiedler's reference design acks each packet 32 times over so a few lost acks don't cause false "lost" classification.
- **Reliable-ordered messages** layered selectively on top only for state that must arrive (item pickups) — fast-changing state (movement) stays unreliable since a stale update is simply superseded.

Maps directly onto a `BitStream` (wire format) / `ConnectionManager` (sequence/ack/ack-bitfield handshake, loss/RTT tracking) / `UpdateManager` (reliable vs unreliable channel per message) split — exactly SkyDestroyer's architecture.

Sources: Glenn Fiedler, *Reliability, Ordering and Congestion Avoidance over UDP* — https://gafferongames.com/post/reliability_ordering_and_congestion_avoidance_over_udp/ · *Reliable Ordered Messages* — https://gafferongames.com/post/reliable_ordered_messages/ · *What Every Programmer Needs To Know About Game Networking* — https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/

## Related

- [SkyDestroyer - Overview](kb://07-projects-skydestroyer-skydestroyer-overview)
- [Reference Map](kb://01-maps-reference-map)
- [Projects Map](kb://01-maps-projects-map)
