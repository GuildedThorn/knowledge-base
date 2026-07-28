---
summary: "The actor model structures concurrent systems as isolated entities that communicate by asynchronous messages."
status: active
tags: [reference, engineering, distributed-systems, actors]
private: false
---

# Actor Model and Message Passing

## Purpose

The actor model structures concurrent systems as isolated entities that communicate by asynchronous messages.

## Core Model

- Actors encapsulate state and process one message at a time, avoiding shared mutable state inside the actor.
- Supervision trees model failure handling as part of system structure.
- Location transparency is attractive but distributed actors still face network partitions, serialization, and backpressure.

## Engineering Notes

- Use actors for stateful coordination, protocol handlers, devices, sessions, and simulations.
- Design mailbox bounds and backpressure; unbounded queues convert overload into memory failure.
- Keep message schemas versioned and explicit when actors cross process boundaries.

## Sources

- Hewitt actor model paper - https://dl.acm.org/doi/10.5555/1624775.1624804
- Akka documentation - https://doc.akka.io/docs/akka/current/typed/guide/actors-intro.html
- Orleans documentation - https://learn.microsoft.com/en-us/dotnet/orleans/overview

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
