---
summary: "The default journaling Linux filesystem built on extents, delayed allocation, and htree directory indexing."
status: active
tags: [reference, engineering, linux, ext4, journaling, extents]
private: false
---

# ext4

## Purpose

The default journaling Linux filesystem built on extents, delayed allocation, and htree directory indexing.

## Core Model

- ext4 maps file data with extents: ranges of contiguous blocks described by a start and length, replacing ext3's indirect block maps.
- Extents cut metadata overhead and fragmentation for large files and speed up truncation and deletion.
- Files are stored in block groups, each with its own inode and block bitmaps to keep related metadata local.
- Directories can be indexed with htree (a hashed B-tree) so lookups in large directories stay fast instead of scanning linearly.

## Journaling and Allocation

- The jbd2 layer journals filesystem changes so a crash can be recovered to a consistent state on the next mount.
- Three journaling modes trade safety for speed: journal (data and metadata journaled), ordered (default: metadata journaled, data written before commit), and writeback (metadata only).
- Delayed allocation defers assigning physical blocks until writeback, letting the allocator place more data contiguously.
- Multiblock allocation grabs many blocks at once, further reducing fragmentation.

## Engineering Notes

- ext4 is backward compatible enough to mount many ext3 filesystems and supports larger volumes and files than its predecessors.
- Delayed allocation can widen the window for data loss on crashes without proper fsync, a known application-behavior consideration.

## Sources

- Linux kernel docs - ext4 - https://docs.kernel.org/filesystems/ext4/index.html
- Linux kernel docs - ext4 admin guide - https://docs.kernel.org/admin-guide/ext4.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
