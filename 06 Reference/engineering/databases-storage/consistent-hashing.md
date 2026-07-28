---
summary: "A hashing scheme mapping keys and nodes onto a ring so that adding or removing nodes remaps only a small key fraction."
status: active
tags: [reference, engineering, databases, consistent-hashing, partitioning, distributed]
private: false
---

# Consistent Hashing

## Purpose

A hashing scheme mapping keys and nodes onto a ring so that adding or removing nodes remaps only a small key fraction.

## How It Works

- Both keys and nodes are hashed onto the same fixed circular space (the hash ring).
- A key is owned by the first node encountered when walking clockwise from the key's position on the ring.
- Adding or removing a node only remaps the keys between it and its ring neighbor, roughly K/N keys, not the whole dataset.
- Introduced by Karger et al. for distributed web caching to avoid the near-total remap that plain modulo hashing causes on resize.

## Engineering Notes

- Plain node placement gives uneven load; virtual nodes (many ring points per physical node) smooth the distribution and ease heterogeneity.
- Dynamo uses consistent hashing for partitioning and places replicas on the next N distinct nodes clockwise (preference list).
- Rebalancing cost is proportional to the keys owned by the changed node, bounding data movement during scale-out and failure.
- Jump consistent hash (Lamping & Veach) achieves minimal, balanced remapping with no per-node storage, but assumes numbered buckets without arbitrary removal.

## Sources

- Karger et al. - Consistent Hashing and Random Trees - https://dl.acm.org/doi/10.1145/258533.258660
- DeCandia et al. - Dynamo - https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Lamping & Veach - A Fast, Minimal Memory, Consistent Hash Algorithm (Jump) - https://arxiv.org/abs/1406.2294

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
