---
summary: "Distributed systems papers and design notes: consensus, clocks, replication, logs, storage systems, and failure handling."
status: active
tags: [reference, engineering, distributed-systems, systems, index]
private: false
---

# Systems and Distributed Computing - Index

## Purpose

Distributed systems papers and design notes: consensus, clocks, replication, logs, storage systems, and failure handling.

## Notes

- [API Idempotency Keys](kb://06-reference-engineering-systems-distributed-api-idempotency-keys) - Idempotency keys make retrying mutating API requests safe by binding repeated attempts to one server-side operation result.
- [Actor Model and Message Passing](kb://06-reference-engineering-systems-distributed-actor-model-message-passing) - The actor model structures concurrent systems as isolated entities that communicate by asynchronous messages.
- [Bigtable Wide-Column Storage](kb://06-reference-engineering-systems-distributed-bigtable-wide-column-storage) - Bigtable stores sparse distributed sorted maps over rows, columns, and timestamps, influencing HBase, Cassandra, and many cloud databases.
- [Borg Large-Scale Cluster Management](kb://06-reference-engineering-systems-distributed-borg-large-scale-cluster-management) - Borg is Google's large-scale cluster manager for scheduling service and batch workloads across shared machine pools.
- [CAP, PACELC, and Consistency Models](kb://06-reference-engineering-systems-distributed-cap-pacelc-consistency) - CAP and PACELC describe tradeoffs between consistency, availability, latency, and partition tolerance in replicated systems.
- [Consensus: Paxos](kb://06-reference-engineering-systems-distributed-consensus-paxos) - Paxos is a family of consensus algorithms for agreeing on a value despite crash failures and asynchronous communication.
- [Consensus: Raft](kb://06-reference-engineering-systems-distributed-consensus-raft) - Raft is a consensus algorithm designed for understandability, using leader election, log replication, and safety rules.
- [Distributed Locks, Leases, and Fencing](kb://06-reference-engineering-systems-distributed-distributed-locks-leases-and-fencing) - Distributed locks need leases, fencing tokens, and failure-aware design because clients can pause, partition, or continue after losing ownership.
- [Distributed Systems Principles](kb://06-reference-engineering-systems-distributed-distributed-systems-principles) - Distributed systems coordinate multiple computers under partial failure, latency, concurrency, and independent clocks.
- [Dynamo and Eventual Consistency](kb://06-reference-engineering-systems-distributed-dynamo-eventual-consistency) - Dynamo is Amazon's highly available key-value design using consistent hashing, quorums, vector clocks, sloppy quorum, and hinted handoff.
- [Google File System](kb://06-reference-engineering-systems-distributed-google-file-system) - GFS is a distributed file system designed for large files, sequential workloads, chunk replication, and commodity-machine failure.
- [Kafka Distributed Log](kb://06-reference-engineering-systems-distributed-kafka-distributed-log) - Kafka models durable ordered streams as partitioned replicated logs, decoupling producers and consumers at scale.
- [Logical Clocks and Vector Clocks](kb://06-reference-engineering-systems-distributed-logical-clocks-and-vector-clocks) - Logical clocks capture ordering without relying on synchronized wall clocks; vector clocks detect causality and concurrency.
- [MapReduce Dataflow Model](kb://06-reference-engineering-systems-distributed-mapreduce-dataflow-model) - MapReduce popularized large-scale batch processing by decomposing jobs into map, shuffle/sort, and reduce phases over distributed storage.
- [Replication, Quorums, and Conflict Resolution](kb://06-reference-engineering-systems-distributed-replication-quorums-and-conflict-resolution) - Replication improves availability and durability but introduces quorum, lag, conflict, and failover tradeoffs.
- [Sagas and Workflow Orchestration](kb://06-reference-engineering-systems-distributed-sagas-and-workflow-orchestration) - Sagas coordinate long-running distributed business transactions through local commits and compensating actions.
- [Spanner and TrueTime](kb://06-reference-engineering-systems-distributed-spanner-and-truetime) - Spanner combines replication, transactions, SQL, and TrueTime uncertainty bounds to provide externally consistent distributed transactions.
- [Timeouts, Retries, and Idempotency](kb://06-reference-engineering-systems-distributed-timeouts-retries-and-idempotency) - Timeouts, retries, and idempotency keys turn transient failure handling from accidental duplicate work into a controlled protocol.

## Related

- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Engineering Source Corpus](kb://06-reference-engineering-engineering-source-corpus)
- [Reference Map](kb://01-maps-reference-map)
