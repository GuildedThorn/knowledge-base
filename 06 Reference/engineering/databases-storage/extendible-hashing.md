---
summary: "Dynamic hashing schemes that grow the hash table incrementally to avoid full rehashing under insertion load."
status: active
tags: [reference, engineering, databases, hashing, dynamic, access-methods]
private: false
---

# Extendible and Linear Hashing

## Purpose

Dynamic hashing schemes that grow the hash table incrementally to avoid full rehashing under insertion load.

## Core Model

- Extendible hashing uses a directory indexed by the top `global depth` bits of a key's hash; each directory slot points to a bucket carrying its own `local depth`.
- On bucket overflow, only that bucket splits; if its local depth equals the global depth, the directory doubles, otherwise the directory is untouched.
- Buckets can be shared by multiple directory entries when local depth is below global depth, so directory doubling is cheap pointer duplication, not data movement.
- Reads cost one directory lookup plus one bucket access, giving predictable worst-case access even as the table grows.

## Linear Hashing vs Extendible

- Linear hashing (Litwin) avoids a directory entirely, splitting buckets in a fixed round-robin order tracked by a split pointer rather than where overflow occurred.
- A split is triggered by a load-factor threshold, not by the overflowing bucket, so the bucket that overflows uses an overflow chain until its turn to split arrives.
- Extendible growth is data-driven and directory-based; linear growth is uniform and pointer-free but tolerates temporary overflow chains and uneven bucket occupancy.
- Both bound amortized rehash cost to a single bucket versus rebuilding the whole table on resize.

## Sources

- Fagin et al. - Extendible Hashing - https://dl.acm.org/doi/10.1145/320083.320092
- Litwin - Linear Hashing - https://dl.acm.org/doi/10.5555/1286711.1286726
- CMU 15-445 Hash Tables - https://15445.courses.cs.cmu.edu/

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
