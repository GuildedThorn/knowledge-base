---
summary: "Idempotency keys make retrying mutating API requests safe by binding repeated attempts to one server-side operation result."
status: active
tags: [reference, engineering, distributed-systems, api, reliability]
private: false
---

# API Idempotency Keys

## Purpose

Idempotency keys let clients safely retry mutating requests after network failures, timeouts, or ambiguous responses without duplicating side effects.

## Core Model

- The client generates a high-entropy key for one logical operation.
- The server records the first operation result associated with that key.
- Retries with the same key return the same result or are rejected if parameters differ.
- Keys expire after a retention window.

## Design Rules

- Use idempotency keys for `POST`/mutation operations that may be retried.
- Compare request parameters to detect accidental key reuse for a different operation.
- Store the response after endpoint execution begins, not for validation failures that did not create side effects.
- Scope keys by account/tenant to avoid cross-tenant collision or leakage.
- Make the retention window longer than realistic retry windows.

## Failure Modes

- Key reuse can mask distinct business operations.
- Weak keys can collide.
- Storing only success responses leaves ambiguity for partially failed operations.
- Retrying without deadlines can preserve load after the user no longer cares.

## Sources

- Stripe API Reference - Idempotent requests - https://docs.stripe.com/api/idempotent_requests
- Stripe Engineering - Designing robust and predictable APIs with idempotency - https://stripe.com/blog/idempotency

## Related

- [Timeouts, Retries, and Idempotency](kb://06-reference-engineering-systems-distributed-timeouts-retries-and-idempotency)
- [Timeouts, Retries, Backoff, and Jitter](kb://06-reference-engineering-observability-sre-timeouts-retries-backoff-jitter)
- [REST API Design](kb://06-reference-engineering-software-architecture-rest-api-design)
