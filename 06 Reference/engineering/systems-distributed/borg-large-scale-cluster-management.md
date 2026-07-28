---
summary: "Borg is Google's large-scale cluster manager for scheduling service and batch workloads across shared machine pools."
status: active
tags: [reference, engineering, distributed-systems, cluster-management, scheduling]
private: false
---

# Borg Large-Scale Cluster Management

## Purpose

Borg is Google's internal cluster manager described in the 2015 EuroSys paper. It schedules long-running services and batch jobs across shared clusters while enforcing priority, quota, failure recovery, and resource isolation.

## Core Model

- Users submit jobs made of tasks.
- Machines run agents that execute tasks and report state to replicated cluster masters.
- Workloads have priorities, constraints, resource requests, and restart behavior.
- Production services and lower-priority batch workloads share capacity, improving utilization.
- The control plane stores cluster state consistently and continuously reconciles desired state with observed state.

## Design Lessons

- Cluster scheduling is an economic system: priority, quota, preemption, and admission control matter as much as placement algorithms.
- Sharing production and batch workloads improves utilization but requires strong isolation and predictable preemption behavior.
- Declarative job specs and a reconciliation loop are more scalable than one-off operational scripts.
- Observability and developer-facing UIs are core scheduler features, not add-ons.

## Sources

- Google Research - Large-scale cluster management at Google with Borg - https://research.google/pubs/pub43438/
- MIT 6.824 mirror of Borg paper - https://pdos.csail.mit.edu/6.824/papers/borg.pdf

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Containers, Namespaces, and cgroups](kb://06-reference-engineering-linux-nix-systems-containers-namespaces-and-cgroups)
- [Kubernetes Pod Security Standards](kb://06-reference-engineering-linux-nix-systems-kubernetes-pod-security-standards)
