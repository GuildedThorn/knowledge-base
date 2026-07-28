---
summary: "Sagas coordinate long-running distributed business transactions through local commits and compensating actions."
status: active
tags: [reference, engineering, distributed-systems, sagas]
private: false
---

# Sagas and Workflow Orchestration

## Purpose

Sagas coordinate long-running distributed business transactions through local commits and compensating actions.

## Core Model

- A saga decomposes a distributed transaction into steps, each with a compensating operation.
- Choreography distributes control through events; orchestration centralizes workflow state in a coordinator.
- Compensation is business logic, not a database rollback.

## Engineering Notes

- Use sagas when cross-service work cannot or should not hold a distributed ACID transaction.
- Make steps idempotent and durable; workflow state must survive process crashes.
- Design manual repair paths for compensation failure and partially completed workflows.

## Sources

- Garcia-Molina and Salem - Sagas - https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- Temporal documentation - https://docs.temporal.io/
- Microsoft - Saga distributed transactions - https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
