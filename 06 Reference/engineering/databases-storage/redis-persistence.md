---
summary: "Redis's two durability mechanisms: point-in-time RDB snapshots and the append-only log of write commands."
status: active
tags: [reference, engineering, databases, redis, persistence, durability]
private: false
---

# Redis Persistence (RDB and AOF)

## Purpose

Redis's two durability mechanisms: point-in-time RDB snapshots and the append-only log of write commands.

## Core Model

- RDB produces a compact point-in-time binary dump of the whole dataset, triggered by `SAVE`/`BGSAVE` or `save` interval rules.
- `BGSAVE` calls `fork()`; the child writes the snapshot using copy-on-write pages while the parent keeps serving traffic.
- AOF logs every write command to a file that is replayed on restart to reconstruct state, giving finer-grained recovery than RDB.
- AOF grows unbounded, so a rewrite periodically rebuilds a minimal command set; modern Redis uses an RDB preamble plus AOF tail (hybrid).

## Engineering Notes

- `appendfsync` controls durability vs throughput: `always` (per write, safest, slowest), `everysec` (default, ~1s worst-case loss), `no` (OS-flushed).
- RDB is faster to load and better for backups; AOF loses less data but restores more slowly and yields larger files.
- Fork-based snapshots can cause latency spikes and memory pressure on write-heavy, large datasets due to copy-on-write duplication.
- Replicas typically bootstrap from an RDB transfer, then follow the master's replication stream; persistence and replication are independent concerns.

## Sources

- Redis Documentation - Persistence - https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/
- Redis Documentation - Replication - https://redis.io/docs/latest/operate/oss_and_stack/management/replication/
- Redis Documentation - Data Types - https://redis.io/docs/latest/develop/data-types/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
