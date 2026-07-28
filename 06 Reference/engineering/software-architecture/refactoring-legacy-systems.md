---
summary: "Legacy-system evolution is controlled change: characterization tests, seams, strangler patterns, and small reversible refactors."
status: active
tags: [reference, engineering, architecture, refactoring]
private: false
---

# Refactoring Legacy Systems

## Purpose

Legacy-system evolution is controlled change: characterization tests, seams, strangler patterns, and small reversible refactors.

## Core Model

- Legacy code is code without sufficient safety for change, not merely old code.
- Characterization tests capture current behavior before changing internals.
- Strangler patterns route new behavior around old systems while reducing risk incrementally.

## Engineering Notes

- Stabilize with tests and observability before large rewrites.
- Refactor toward clear boundaries around the change you need now.
- Keep migration states explicit: dual-write, shadow-read, backfill, cutover, rollback.

## Sources

- Martin Fowler - Strangler Fig Application - https://martinfowler.com/bliki/StranglerFigApplication.html
- Working Effectively with Legacy Code - https://www.oreilly.com/library/view/working-effectively-with/0131177052/
- Refactoring.com - https://refactoring.com/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
