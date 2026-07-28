---
summary: "A copy-on-write Linux filesystem providing snapshots, subvolumes, checksums, and integrated multi-device support."
status: active
tags: [reference, engineering, linux, btrfs, copy-on-write, snapshots]
private: false
---

# Btrfs

## Purpose

A copy-on-write Linux filesystem providing snapshots, subvolumes, checksums, and integrated multi-device support.

## Core Model

- Btrfs stores metadata and data in copy-on-write B-trees, so modifications write to new blocks rather than overwriting in place.
- Subvolumes are independently mountable directory trees within one filesystem, each acting as its own snapshot boundary.
- Because writes never overwrite live data, the on-disk state stays consistent without a traditional journal.
- Data and metadata blocks carry checksums, letting the filesystem detect silent corruption on read.

## Snapshots and Send/Receive

- A snapshot is a copy-on-write clone of a subvolume that shares blocks until either side is modified, making creation near-instant and space-efficient.
- Snapshots can be read-only or writable and are commonly used for rollbacks and backups.
- `btrfs send` serializes the difference between two snapshots into a stream that `btrfs receive` replays elsewhere for incremental backups.

## Engineering Notes

- Btrfs manages multiple devices natively with configurable RAID profiles (RAID0/1/10, and single/dup) selectable per data and metadata.
- `scrub` reads all blocks, verifies checksums, and repairs from a good copy when redundancy is present.
- Parity RAID (RAID5/6) has historically carried stability caveats and is used with caution.

## Sources

- Btrfs documentation - https://btrfs.readthedocs.io/en/latest/
- Linux kernel docs - Btrfs - https://docs.kernel.org/filesystems/btrfs.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
