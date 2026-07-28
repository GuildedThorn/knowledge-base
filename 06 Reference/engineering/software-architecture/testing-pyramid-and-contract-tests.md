---
summary: "A healthy test strategy layers fast unit tests, focused integration tests, contract tests, and a smaller number of end-to-end workflows."
status: active
tags: [reference, engineering, architecture, testing]
private: false
---

# Testing Pyramid and Contract Tests

## Purpose

A healthy test strategy layers fast unit tests, focused integration tests, contract tests, and a smaller number of end-to-end workflows.

## Core Model

- The testing pyramid favors many cheap deterministic tests and fewer broad slow tests.
- Contract tests verify that services agree on request/response/event contracts without requiring full environment orchestration.
- End-to-end tests cover user-critical paths but are slow, flaky, and expensive when overused.

## Engineering Notes

- Place tests at the lowest layer that catches the failure with confidence.
- Use contract tests for service boundaries and generated clients.
- Track flakiness as technical debt; unreliable tests stop protecting the system.

## Sources

- Martin Fowler - Test Pyramid - https://martinfowler.com/bliki/TestPyramid.html
- Pact contract testing - https://docs.pact.io/
- Google Testing Blog - https://testing.googleblog.com/

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
