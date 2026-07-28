---
summary: "Kafka models durable ordered streams as partitioned replicated logs, decoupling producers and consumers at scale."
status: active
tags: [reference, engineering, distributed-systems, kafka]
private: false
---

# Kafka Distributed Log

## Purpose

Kafka models durable ordered streams as partitioned replicated logs, decoupling producers and consumers at scale.

## Core Model

- Topics split into partitions; order is guaranteed within a partition, not across a whole topic.
- Consumers track offsets and can replay logs as long as retention keeps data.
- Replication, ISR, acks, and controller metadata decide durability and failover behavior.

## Engineering Notes

- Choose partition keys for ordering, scaling, and hotspot avoidance together.
- Treat exactly-once as a specific producer/consumer/transaction configuration, not a blanket guarantee.
- Monitor lag, broker disk, under-replicated partitions, controller health, and retention pressure.

## Sources

- Kafka original paper - https://notes.stephenholiday.com/Kafka.pdf
- Apache Kafka documentation - https://kafka.apache.org/documentation/
- Confluent - Kafka design - https://docs.confluent.io/kafka/design/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
