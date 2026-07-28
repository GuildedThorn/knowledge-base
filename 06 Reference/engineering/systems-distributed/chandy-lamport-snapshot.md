---
summary: "The Chandy-Lamport algorithm records a consistent global snapshot of a distributed system using marker messages over channels."
status: active
tags: [reference, engineering, distributed-systems, snapshot, global-state]
private: false
---

# Chandy-Lamport Snapshot Algorithm

## Purpose

The Chandy-Lamport algorithm records a consistent global snapshot of a distributed system using marker messages over channels.

## How It Works

- The system is modeled as processes connected by reliable, FIFO, unidirectional channels.
- Any process initiates by recording its own state, then sending a marker on every outgoing channel before any further messages.
- On first receiving a marker, a process records its state, marks the channel it arrived on as empty, and forwards markers on all its outgoing channels.
- For channels where a marker has already been seen, the process records all messages received between its state capture and that channel's marker as the channel's in-flight state.
- The algorithm terminates once every process has received a marker on every incoming channel.

## Key Ideas

- The result is a consistent cut: a global state that could have occurred, even though no single instant is observed and processes never stop.
- Recorded channel state captures messages that were in transit, so the snapshot preserves both node and network state.
- Snapshots support stable-property detection such as deadlock, termination, and distributed garbage collection.
- The captured state is not necessarily one the system actually passed through, but it is reachable and causally consistent for evaluating stable predicates.

## Sources

- Distributed Snapshots: Determining Global States (Chandy, Lamport) - https://lamport.azurewebsites.net/pubs/chandy.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
