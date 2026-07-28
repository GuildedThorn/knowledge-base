---
summary: "Brendan Gregg's method for analyzing resource health by checking Utilization, Saturation, and Errors for every system resource."
status: active
tags: [reference, engineering, sre, performance, methodology, resources]
private: false
---

# The USE Method

## Purpose

Brendan Gregg's methodology for analyzing resource health by checking Utilization, Saturation, and Errors for every system resource.

## Utilization, Saturation, Errors

- Utilization: the average time a resource was busy servicing work, as a percent over an interval; high utilization is a bottleneck indicator but not proof of a problem.
- Saturation: the degree of extra work that cannot be serviced and must queue or wait; any sustained saturation is a strong sign of a resource constraint.
- Errors: the count of error events for the resource, checked first because errors can degrade performance while being easy to overlook.
- Utilization and saturation are distinct: a resource can be under 100% utilized yet already saturated due to bursty demand and queueing.

## Per-Resource Checklist

- Apply the three metrics to every physical resource: CPUs, memory, network interfaces, storage devices, controllers, and interconnects.
- On Linux, tools map to each cell of the matrix (`vmstat`, `mpstat`, `iostat`, `sar`, `netstat`, `ss`, and PSI in `/proc/pressure`).
- Draw a functional block diagram of the system first, then walk each resource so nothing is missed.

## When to Apply It

- USE is resource-oriented and best for the bottom-up question "which resource is the bottleneck," complementing workload-oriented methods.
- It is fast triage: a short checklist surfaces the constrained resource before deeper drill-down.
- For request-driven services it pairs with the RED method or golden signals, which look at the workload rather than the resources.

## Sources

- The USE Method - https://www.brendangregg.com/usemethod.html
- USE Method Linux Checklist - https://www.brendangregg.com/USEmethod/use-linux.html

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
