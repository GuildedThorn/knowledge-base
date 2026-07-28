---
summary: "Distributed locks need leases, fencing tokens, and failure-aware design because clients can pause, partition, or continue after losing ownership."
status: active
tags: [reference, engineering, distributed-systems, locks]
private: false
---

# Distributed Locks, Leases, and Fencing

## Purpose

Distributed locks need leases, fencing tokens, and failure-aware design because clients can pause, partition, or continue after losing ownership.

## Core Model

- A lock service can grant mutual exclusion only under specific timing and failure assumptions.
- Leases expire; a paused client may resume after another client has acquired the same lease.
- Fencing tokens let downstream systems reject stale actors even if they wake up late.

## Engineering Notes

- Prefer idempotent operations and single-writer ownership over distributed locks when possible.
- When locks are necessary, require fencing at the protected resource, not only at the lock service.
- Document clock, TTL, renewal, and failover assumptions; leases are a protocol, not a mutex.

## Sources

- Martin Kleppmann - How to do distributed locking - https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
- Google Chubby paper - https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/
- Redis Redlock documentation - https://redis.io/docs/latest/develop/use/patterns/distributed-locks/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
