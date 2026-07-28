---
summary: "Timeouts, retries, exponential backoff, and jitter prevent small distributed-system failures from becoming synchronized overload."
status: active
tags: [reference, engineering, sre, resilience, distributed-systems]
private: false
---

# Timeouts, Retries, Backoff, and Jitter

## Purpose

Timeouts, retries, backoff, and jitter are basic client-side resilience controls. Used correctly, they reduce user-visible failures. Used badly, they amplify overload.

## Core Model

- Timeouts bound how long a caller waits for a dependency.
- Retries give transient failures another chance.
- Backoff spaces retries out so a failing dependency is not hammered immediately.
- Jitter randomizes retry timing so many clients do not synchronize into retry storms.

## Design Rules

- Pick timeouts from latency distributions and false-timeout tolerance, not arbitrary round numbers.
- Budget retries across the whole call path; layered retries can multiply load explosively.
- Retry only operations that are safe or protected by idempotency tokens.
- Use capped exponential backoff with jitter for remote calls under partial failure.
- Prefer client libraries with well-tested retry behavior when they match the service semantics.

## Failure Modes

- Too-short timeouts create false failures and unnecessary retries.
- Too-long timeouts consume threads, sockets, memory, and user patience.
- Retrying non-idempotent writes can duplicate side effects.
- Synchronized retries can turn a small dependency problem into cascading failure.
- Backoff without a total deadline can preserve pressure long after the user request is no longer useful.

## Sources

- Amazon Builders Library - Timeouts, retries, and backoff with jitter - https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- AWS Architecture Blog - Exponential Backoff and Jitter - https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
- AWS Prescriptive Guidance - Retry with backoff pattern - https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [SLIs, SLOs, and Error Budgets](kb://06-reference-engineering-observability-sre-sli-slo-error-budgets)
- [Timeouts, Retries, and Idempotency](kb://06-reference-engineering-systems-distributed-timeouts-retries-and-idempotency)
