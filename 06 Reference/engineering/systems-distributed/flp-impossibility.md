---
summary: "FLP proves deterministic consensus is impossible in an asynchronous system with even a single crash failure."
status: active
tags: [reference, engineering, distributed-systems, consensus, impossibility]
private: false
---

# FLP Impossibility Result

## Purpose

FLP proves deterministic consensus is impossible in an asynchronous system with even a single crash failure.

## Model Assumptions

- Fully asynchronous message passing: no bound on message delay or relative process speed, and no clocks.
- Reliable network that eventually delivers every message, but in arbitrary order and after arbitrary delay.
- At most one process may crash (fail-stop); the rest are correct. Consensus requires agreement, validity, and termination.

## The Bivalence Argument

- Fischer, Lynch, and Paterson show every protocol has an initial bivalent configuration whose eventual decision is not yet determined.
- From any bivalent state an adversarial scheduler can always delay one message to reach another bivalent state, keeping the outcome undecided forever.
- The core obstacle: a process cannot distinguish a crashed peer from an arbitrarily slow one, so it can never safely decide.

## Circumventions

- Randomization: probabilistic protocols (Ben-Or, and later BFT designs) terminate with probability 1, sidestepping the deterministic-termination requirement.
- Partial synchrony: assuming eventual message-delay bounds (Dwork-Lynch-Stockmeyer) restores solvability and underlies Paxos and Raft.
- Failure detectors: an eventually-accurate oracle (Chandra-Toueg's ◇W) supplies the weakest information sufficient to solve consensus.

## Sources

- Impossibility of Distributed Consensus with One Faulty Process (Fischer, Lynch, Paterson) - https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
