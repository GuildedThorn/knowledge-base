---
summary: "The kernel device-mapper framework and LVM abstraction for flexible logical volumes over physical storage."
status: active
tags: [reference, engineering, linux, lvm, device-mapper, volumes]
private: false
---

# LVM and the Device Mapper

## Purpose

The kernel device-mapper framework and LVM abstraction for flexible logical volumes over physical storage.

## Core Model

- Physical volumes (PVs) label whole disks or partitions for LVM use.
- One or more PVs aggregate into a volume group (VG), a shared pool of extents.
- Logical volumes (LVs) are carved from a VG and appear as block devices under `/dev/mapper`.
- Allocation is in fixed-size physical/logical extents, decoupling logical layout from physical placement.
- LVs can be grown, shrunk, and moved between PVs while the VG stays online.

## How It Works

- LVM is a userspace layer built on the kernel's device-mapper, which stacks virtual block devices from targets.
- The linear target maps LV extents to underlying PV regions; striping spreads them across devices.
- The snapshot target uses copy-on-write to preserve original blocks as the origin changes.
- The thin target provisions from a shared thin pool, allocating backing store only on write.

## Engineering Notes

- Thin provisioning can overcommit a VG; monitor pool data/metadata usage to avoid running the pool full.
- Snapshots consume space as the origin diverges; an undersized snapshot can become invalid.
- Filesystem resize must accompany LV resize (grow FS after growing LV, shrink FS before shrinking LV).

## Sources

- man8 - lvm(8) - https://man7.org/linux/man-pages/man8/lvm.8.html
- Linux kernel docs - Device Mapper - https://docs.kernel.org/admin-guide/device-mapper/index.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
