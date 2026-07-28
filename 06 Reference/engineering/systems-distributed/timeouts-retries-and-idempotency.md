---
summary: "Timeouts, retries, and idempotency keys turn transient failure handling from accidental duplicate work into a controlled protocol."
status: active
tags: [reference, engineering, distributed-systems, reliability]
private: false
---

# Timeouts, Retries, and Idempotency

## Purpose

Timeouts, retries, and idempotency keys turn transient failure handling from accidental duplicate work into a controlled protocol.

## Core Model

- Timeouts bound waiting; retries create additional load; backoff and jitter reduce synchronized retry storms.
- Idempotency means an operation can be safely repeated with the same effect or same result.
- At-least-once delivery requires consumers that tolerate duplicates.

## Engineering Notes

- Set deadlines from end-to-end latency budgets, not arbitrary per-hop defaults.
- Use idempotency keys for externally visible writes such as payments, job creation, and provisioning.
- Pair retries with circuit breakers, bulkheads, queues, and load shedding under overload.

## Sources

- Google SRE Book - Handling overload - https://sre.google/sre-book/handling-overload/
- AWS Builders Library - Timeouts, retries, and backoff - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Stripe - Idempotent requests - https://docs.stripe.com/api/idempotent_requests

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
