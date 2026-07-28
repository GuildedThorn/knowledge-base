---
summary: "The union filesystem that stacks a writable upper layer over read-only lower layers using copy-up semantics."
status: active
tags: [reference, engineering, linux, overlayfs, union-fs, containers]
private: false
---

# OverlayFS

## Purpose

The union filesystem that stacks a writable upper layer over read-only lower layers using copy-up semantics.

## Core Model

- An overlay mount combines a lowerdir (one or more read-only layers), an upperdir (the writable layer), and a workdir (private scratch space for atomic operations).
- Reads resolve top-down: the upper layer shadows the lower, and multiple lower layers are searched in order.
- The merged mount presents a single unified directory tree to userspace.
- Both upperdir and workdir must reside on the same underlying filesystem.

## How It Works

- Copy-up: modifying a file that exists only in a lower layer first copies it into the upper layer, after which changes are confined there.
- Whiteouts: deleting a lower-layer file creates a whiteout marker in the upper layer that hides it from the merged view.
- Opaque directories mask an entire lower directory when it has been replaced in the upper layer.
- Metadata-only copy-up can defer copying file data until the contents are actually written.

## Operational Notes

- Container engines map image layers to stacked lowerdirs and give each container its own upperdir, so image data is shared read-only and per-container writes stay isolated.
- Because copy-up duplicates whole files on first write, workloads that rewrite large lower-layer files incur upfront copy cost.

## Sources

- Linux kernel docs - Overlay Filesystem - https://docs.kernel.org/filesystems/overlayfs.html
- man8 - mount(8) - https://man7.org/linux/man-pages/man8/mount.8.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
