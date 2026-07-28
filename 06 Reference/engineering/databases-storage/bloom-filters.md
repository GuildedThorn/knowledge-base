---
summary: "A space-efficient probabilistic structure answering set membership with no false negatives and tunable false positives."
status: active
tags: [reference, engineering, databases, bloom-filter, probabilistic, membership]
private: false
---

# Bloom Filters

## Purpose

A space-efficient probabilistic structure answering set membership with no false negatives and tunable false positives.

## How It Works

- Backed by a bit array of m bits and k independent hash functions, all initially zero.
- Insert sets the k bits given by hashing the element; a query tests whether all k of an element's bits are set.
- If any bit is unset the element is definitely absent, so false negatives are impossible.
- If all k bits are set the element is probably present; collisions from other inserts cause false positives.
- Standard filters support insert and query but not deletion (counting variants add it).

## Sizing Math

- False-positive rate is approximately (1 - e^(-kn/m))^k for n inserted elements.
- The optimal hash count is k = (m/n) ln 2, which minimizes the false-positive probability.
- At optimal k, roughly 9.6 bits per element gives about 1% false positives; each added bit-per-element cuts it further.

## Defensive and Systems Use

- LSM-tree engines attach a Bloom filter per SSTable to skip disk reads for keys not present, cutting read amplification.
- RocksDB and LevelDB use them on the read path to avoid probing files that cannot contain a key.
- Also used for cache admission, duplicate suppression, and network-membership queries.

## Sources

- Bloom - Space/Time Trade-offs in Hash Coding with Allowable Errors - https://dl.acm.org/doi/10.1145/362686.362692
- Broder & Mitzenmacher - Network Applications of Bloom Filters: A Survey - https://www.eecs.harvard.edu/~michaelm/postscripts/im2005b.pdf
- RocksDB Wiki - Bloom Filter - https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter

## Related

- [Databases and Storage - Index](kb://06-reference-engineering-databases-storage-databases-storage-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
