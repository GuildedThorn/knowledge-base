---
summary: "Unreliable failure detectors abstract crash detection, characterizing the weakest oracle needed to solve consensus asynchronously."
status: active
tags: [reference, engineering, distributed-systems, fault-tolerance, consensus]
private: false
---

# Failure Detectors

## Purpose

Unreliable failure detectors abstract crash detection, characterizing the weakest oracle needed to solve consensus asynchronously.

## Core Model

- A failure detector is a distributed oracle giving each process a possibly-inaccurate list of processes it suspects have crashed.
- Detectors are classified by two axes: completeness (crashed processes are eventually suspected) and accuracy (correct processes are not wrongly suspected).
- Accuracy comes in strong, weak, eventually strong, and eventually weak forms; eventual variants allow arbitrary early mistakes that must stop after some unknown time.
- Chandra and Toueg show consensus is solvable with detectors as weak as eventually weak (denoted diamond-W), sidestepping the FLP impossibility result in pure asynchrony.

## Key Results

- Detectors form a lattice under reduction: one detector reduces to another if its output can be transformed to emulate the other's.
- Omega outputs a single trusted leader that all correct processes eventually agree on; it is equivalent in power to eventually-weak accuracy with completeness.
- Chandra, Hadzilacos, and Toueg prove Omega is the weakest failure detector for solving consensus, so any detector that solves consensus can implement Omega.
- In practice these are approximated with timeouts and heartbeats, since true asynchronous detection is impossible; leader-based protocols like Paxos and Raft embody the Omega abstraction.

## Sources

- Unreliable Failure Detectors for Reliable Distributed Systems (Chandra, Toueg) - https://www.cs.utexas.edu/~lorenzo/corsi/cs380d/papers/p225-chandra.pdf
- The Weakest Failure Detector for Solving Consensus - https://dl.acm.org/doi/10.1145/234533.234549

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
