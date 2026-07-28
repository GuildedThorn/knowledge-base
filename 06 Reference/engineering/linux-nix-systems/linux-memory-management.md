---
summary: "Linux memory management combines virtual memory, page tables, demand paging, reclaim, swapping, NUMA, huge pages, and cgroup limits."
status: active
tags: [reference, engineering, linux, memory]
private: false
---

# Linux Memory Management

## Purpose

Linux memory management combines virtual memory, page tables, demand paging, reclaim, swapping, NUMA, huge pages, and cgroup limits.

## Core Model

- Processes see virtual address spaces backed by physical pages, files, anonymous memory, or shared mappings.
- The kernel reclaims page cache and anonymous memory under pressure using LRU-like mechanisms.
- OOM behavior depends on global memory, cgroups, overcommit policy, and reclaim success.

## Engineering Notes

- Read RSS, PSS, page cache, swap, cgroup memory, and OOM logs together; one number rarely explains memory pressure.
- Use mmap, huge pages, and pinned memory deliberately because they change reclaim and fragmentation behavior.
- Set service memory limits with headroom for runtime, allocator, page cache, and burst behavior.

## Sources

- Linux kernel memory management docs - https://docs.kernel.org/mm/
- man5 procfs memory fields - https://man7.org/linux/man-pages/man5/proc.5.html
- cgroup v2 memory controller - https://docs.kernel.org/admin-guide/cgroup-v2.html#memory

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
