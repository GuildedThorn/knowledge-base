## Purpose

Document the architecture, runtime dependencies, and current status of the `SkyDestroyer` project.

## Summary

SkyDestroyer is a byte-faithful C# rewrite of AADS (Aerial Assault Dedicated Server) and TAAML (Tribes Aerial Assault Master List), the original dedicated-server and master-list software for the PS2 game *Tribes: Aerial Assault*. It is built as:

- an ASP.NET / .NET 9 console server, cross-platform (Windows/Linux/macOS)
- a wire-faithful reimplementation of the original AADS network protocol, ported line-by-line from the original C++ rather than a clean-room rewrite
- a standalone C# reimplementation of the `taaml` master-list server
- GitHub org: [SkyDestroyerTAAS/SkyDestroyer](https://github.com/SkyDestroyerTAAS/SkyDestroyer), branch `development`

This corrects the previous version of this note, which understated the project's scope and incorrectly listed RabbitMQ/Loki/Serilog as dependencies — those are not used anywhere in this repo.

## Repo Layout

- `Program.cs`: entrypoint — loads `Config`, constructs the server, handles graceful shutdown.
- `SkyDestroyer.cs` (~2000 lines): main server class — login/ban/cull, `PacketShipLoop` (ticks stations, turrets, flipflops, pickups, vehicles, bots, flags, bounds), `LifecycleLoop` (drives the state machine and frame timer), map-vote/change-map orchestration.
- `MasterList/`: standalone reimplementation of `taaml`, byte-faithful to the reference source, own wire protocol (port 15101, 100-server cap, 300s timeout).
- `SyntheticClient/`: a synthetic test client for exercising the server without a real game client.
- `Tests/SkyDestroyer.Tests.csproj`: round-trip/unit test suite.
- `tools/CdfsExtract/`: extracts game assets from the original PS2 disc's `FILES.DAT` (a custom CDFS archive format) — used to pull real building-interior collision data.
- `Utils/` (~80 files): the bulk of the port —
  - networking/transport: `BitStream.cs`, `ConnectionManager.cs`, `UpdateManager.cs`, `MoveManager.cs`, `GameEventManager.cs`
  - player simulation: `ServerPlayer.cs`, `PlayerMoveInfo.cs`, `GhostPlayer.cs`
  - combat: `WeaponFire.cs`, `Projectiles.cs`, `LinearProjectile.cs`, `Pain.cs`
  - vehicles: `VehiclePhysics.cs`, `VehicleStation.cs`
  - assets/turrets/stations: `TurretRuntime.cs`, `TurretHost.cs`, `StationRuntime.cs`, `InventoryStation.cs`, `PickupHost.cs`, `DeployManager.cs`, `FlipFlopHost.cs`
  - game modes: `GameManager.cs` (CTF/Capture-and-Hold/Hunt logic, mission voting, team balance)
  - bot AI (ported from ~21k lines of original C++): `NavGraph.cs`, `BotObject.cs`, `MasterAI.cs`, `CtfMasterAI.cs`, `CnhMasterAI.cs`, `BotManager.cs`, `PathKeeper.cs`
  - world collision: `Terrain.cs`, `Collider.cs`, `BuildingInterior.cs`, `ServerInteriors.cs`, `ShapeFile.cs`, `AssetCollision.cs`
  - framework/admin: `ServerStateMachine.cs`, `FrameTimer.cs`, `ServerTick.cs`, `BanList.cs`, `TelnetClient.cs`/`TelnetManager.cs`
- `Resources/`: `config.json` (runtime config, auto-written with defaults), `Characters/*.txt` (real armor/physics data files from the original game), `Interiors/*.BIN` (Avalon building collision meshes extracted via `CdfsExtract`).
- `docs/`: `PORTING.md`, `PORTING-HISTORY.md`, `SYNC_PORT_SCOPE.md`, `INTERACTION_SCOPE.md` — an actively maintained porting ledger tracking fidelity status per subsystem.
- `flake.nix`: Nix dev shell with `dotnet-sdk_9` plus `pcsx2` and screenshot/input-automation tooling (`xdotool`, `wtype`, `wlrctl`, `grim`, `slurp`) for testing against a real PS2 emulator client.
- `config.live.json`: live deployment config (server identity/port, ban policy, connection tuning, master-list registration, LAN discovery, telnet admin, logging).

## Major Features

- Wire-faithful AADS protocol: login, mission, disconnect, reliable heartbeat/ack layer, LAN discovery, master-list registration — ported byte-for-byte from the original.
- Full gameplay simulation is live: real player physics, all weapons/projectiles/damage, vehicles (ground-effect and flight physics, multi-seat mount/dismount), turrets/stations/pickups/deployables.
- Three game modes implemented: CTF (real flag physics), Capture-and-Hold, Hunter/Escalade.
- Full bot AI: nav-graph pathing and per-game-mode bot brains.
- Map voting, kick voting, terrain/interior/asset collision.
- Telnet admin console: `status`, `players`, `stats`, `kick`, `banlist`, `clearbans`, `say`, `shutdown`.
- Temporary ban list (configurable slots/duration, kick-bans by system ID).
- As of the last porting-ledger update (2026-07-12), net/transport/player/weapons/vehicles/turrets/game-modes/bots are all marked tested and confirmed on a real PCSX2 rig. Remaining work is rig-testing coverage for Hunter/CnH/vehicles on non-Avalon maps and multi-client sync, plus a planned plugin API.

## Development Process

This is an unusually rigorous porting effort, not a from-scratch rewrite: `docs/PORTING.md` is a live-maintained fidelity ledger with hard rules ("always read the original C++ source before porting, never approximate") and a verify-before-commit policy requiring live-rig confirmation (a real PCSX2 client) before a feature is marked done.

## Runtime Dependencies

- .NET 9 SDK
- PCSX2 emulator + a real *Tribes: Aerial Assault* client/disc, for rig testing
- No RabbitMQ, Loki, or Serilog — this server has no external service dependencies at runtime

## Prior Art

SkyDestroyer is a rewrite grounded in three separate reference/lineage trees on disk (not separate vault projects, just source material):

- `~/Documents/aads`: the original TAA.xyz **AADS** (Aerial Assault Dedicated Server) C++ Windows source — the primary reference the porting ledger reads function-by-function.
- `~/Documents/AerialAssault`: a third-party upstream archive ([bisc67/AerialAssault](https://github.com/bisc67/AerialAssault)) of the client-side engine and AADS source, used as the other line-numbered reference throughout the porting docs.
- `~/Documents/PS2`: the original `TribesAerialAssault.iso` disc image plus its extracted `FILES.DAT` — raw game asset data (not code), used by `tools/CdfsExtract` to pull real mission/interior collision data.

## Related
