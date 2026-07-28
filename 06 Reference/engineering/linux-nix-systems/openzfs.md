---
summary: "The pooled-storage, copy-on-write filesystem and volume manager offering checksums, snapshots, and self-healing."
status: active
tags: [reference, engineering, linux, zfs, pooled-storage, checksums]
private: false
---

# OpenZFS on Linux

## Purpose

The pooled-storage, copy-on-write filesystem and volume manager offering checksums, snapshots, and self-healing.

## Core Model

- A pool (zpool) is built from one or more vdevs; datasets and zvols draw space from the shared pool.
- Vdevs define redundancy: mirror, RAID-Z1/2/3, or single disk; redundancy is a property of the vdev, not the pool.
- Copy-on-write never overwrites live blocks in place, which keeps on-disk state consistent without a separate fsck.
- Datasets are independently tunable (compression, recordsize, quotas) and share the pool's free space.
- Snapshots and clones are cheap, referencing unchanged blocks until they diverge.

## How It Works

- Every block carries a checksum stored in its parent, forming a Merkle tree validated on read.
- With redundant vdevs, a bad checksum triggers self-healing: ZFS reconstructs and rewrites the correct data.
- The ARC caches data in RAM; an optional L2ARC extends it to SSD; the ZIL/SLOG accelerates synchronous writes.
- Scrubs walk every allocated block to verify checksums and repair latent errors before they compound.

## Engineering Notes

- ARC sizing competes with application memory; tune it deliberately on memory-constrained hosts.
- recordsize should match workload access patterns (large for streaming, small for databases).
- A SLOG only helps sync-heavy workloads and must itself be reliable/power-loss protected.

## Sources

- OpenZFS documentation - https://openzfs.github.io/openzfs-docs/
- OpenZFS project - https://openzfs.org/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
