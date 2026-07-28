---
summary: "Gossip protocols disseminate information and detect membership by randomized periodic peer-to-peer exchange resembling epidemic spread."
status: active
tags: [reference, engineering, distributed-systems, dissemination, membership]
private: false
---

# Gossip and Epidemic Protocols

## Purpose

Gossip protocols disseminate information and detect membership by randomized periodic peer-to-peer exchange resembling epidemic spread.

## How It Works

- Each node periodically picks a random peer and exchanges state, so updates spread like an epidemic infecting the population.
- Anti-entropy repeatedly reconciles full state between pairs, guaranteeing eventual convergence but at higher bandwidth cost.
- Rumor mongering spreads a "hot" update actively and stops forwarding it once too many contacted peers already know it, trading completeness for efficiency.
- Push, pull, and push-pull variants differ in who sends state; push-pull converges fastest, needing O(log N) rounds to reach all nodes.

## Properties and Membership

- Gossip is scalable and robust: load per node stays bounded, and there is no single point of failure since any peer can carry an update.
- The tradeoff is eventual (not immediate) consistency and redundant message delivery.
- SWIM separates dissemination from failure detection: nodes probe a random peer each period, using indirect pings through k relays to avoid false positives from a single dropped packet.
- SWIM piggybacks membership changes (joins, failures) on its probe traffic, giving detection time and message load that stay roughly constant as the cluster grows.

## Sources

- Epidemic Algorithms for Replicated Database Maintenance (Demers et al.) - https://dl.acm.org/doi/10.1145/41840.41841
- SWIM: Scalable Weakly-consistent Infection-style Membership - https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
