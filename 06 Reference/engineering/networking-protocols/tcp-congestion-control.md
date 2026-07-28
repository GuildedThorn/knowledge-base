---
summary: "How TCP paces sending via slow start, congestion avoidance, fast recovery, and CUBIC loss-based window growth used by default in modern stacks."
status: active
tags: [reference, engineering, networking, tcp, congestion, cubic]
private: false
---

# TCP Congestion Control and CUBIC

## Purpose

How TCP paces sending via slow start, congestion avoidance, fast recovery, and the loss-based CUBIC window growth used by default in modern stacks.

## Core Algorithms

- A sender maintains a congestion window (cwnd) and slow-start threshold (ssthresh); the amount in flight is bounded by min(cwnd, receiver window).
- Slow start grows cwnd by roughly one MSS per ACK (exponential per RTT) while cwnd < ssthresh, probing for available bandwidth after a connection or timeout.
- Congestion avoidance takes over at cwnd >= ssthresh, growing cwnd by about one MSS per RTT (additive increase) for a cautious search near the operating point.
- A retransmission timeout (RTO) collapses cwnd to 1 MSS and re-enters slow start; loss detected via duplicate ACKs is handled more gently.

## Fast Retransmit and Recovery

- Three duplicate ACKs trigger fast retransmit of the presumed-lost segment without waiting for the RTO to expire.
- Fast recovery sets ssthresh to half of flight size, then continues transmitting new data inflated by the dup-ACK count, avoiding a full slow-start restart.

## CUBIC Window Function

- CUBIC replaces linear additive increase with a cubic function of time since the last loss, making growth independent of RTT and fairer across differing path latencies.
- The window plateaus near the pre-loss maximum (concave region) then probes upward (convex region), improving utilization on high bandwidth-delay-product links.
- CUBIC is the default congestion controller in Linux and other modern stacks.

## Sources

- RFC 5681 - TCP Congestion Control - https://www.rfc-editor.org/rfc/rfc5681
- RFC 9438 - CUBIC for Fast and Long-Distance Networks - https://www.rfc-editor.org/rfc/rfc9438

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
