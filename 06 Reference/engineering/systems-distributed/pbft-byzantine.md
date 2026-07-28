---
summary: "Practical Byzantine Fault Tolerance tolerates arbitrary faults among 3f+1 replicas using a three-phase agreement protocol."
status: active
tags: [reference, engineering, distributed-systems, byzantine, replication]
private: false
---

# Byzantine Fault Tolerance and PBFT

## Purpose

Practical Byzantine Fault Tolerance tolerates arbitrary faults among 3f+1 replicas using a three-phase agreement protocol.

## The 3f+1 Bound

- Byzantine faults are arbitrary: a faulty replica may lie, equivocate, or collude, not merely crash.
- To tolerate f Byzantine replicas the system needs at least 3f+1 total, so that f+1 correct replicas form an intersecting quorum despite f faulty and f slow.
- Lamport's Byzantine Generals framing established that with only oral messages agreement requires more than two-thirds honest participants.

## Three-Phase Agreement

- A designated primary orders a client request and broadcasts pre-prepare; backups accept it for the current view and sequence number.
- In prepare, replicas multicast agreement on the ordering; collecting 2f matching prepares plus the pre-prepare guarantees a consistent order within the view.
- In commit, replicas multicast commit and wait for 2f+1 matching commits before executing and replying; the client accepts an answer on f+1 matching replies.

## View Changes and Liveness

- If the primary is suspected faulty (timeouts on progress), backups run a view-change protocol to elect a new primary and preserve prepared requests.
- Safety holds under full asynchrony; liveness requires eventual synchrony, consistent with the FLP result.
- Message authentication (later MACs rather than public-key signatures) makes the protocol practical for real service replication.

## Sources

- Practical Byzantine Fault Tolerance (Castro, Liskov) - https://pmg.csail.mit.edu/papers/osdi99.pdf
- The Byzantine Generals Problem (Lamport et al.) - https://lamport.azurewebsites.net/pubs/byz.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
