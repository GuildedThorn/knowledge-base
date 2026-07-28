---
summary: "ADRs capture important design decisions, context, options, consequences, and status in a durable lightweight format."
status: active
tags: [reference, engineering, architecture, adr]
private: false
---

# Architecture Decision Records

## Purpose

ADRs capture important design decisions, context, options, consequences, and status in a durable lightweight format.

## Core Model

- An ADR records one decision and the reasoning at the time it was made.
- Statuses such as proposed, accepted, superseded, and deprecated make architecture history navigable.
- ADRs are useful because future engineers inherit context, not just outcome.

## Engineering Notes

- Write ADRs for decisions that are expensive to reverse or likely to be questioned.
- Keep them short and link to experiments, benchmarks, incidents, or source material.
- Supersede old ADRs instead of editing away history.

## Sources

- Michael Nygard - Documenting Architecture Decisions - https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- ADR GitHub organization - https://adr.github.io/
- Thoughtworks Technology Radar - Lightweight Architecture Decision Records - https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
