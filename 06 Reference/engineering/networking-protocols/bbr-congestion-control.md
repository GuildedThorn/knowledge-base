---
summary: "Google's model-based congestion control that estimates bottleneck bandwidth and round-trip propagation time instead of reacting to packet loss."
status: active
tags: [reference, engineering, networking, bbr, congestion, bandwidth]
private: false
---

# BBR Congestion Control

## Purpose

Google's model-based congestion control that estimates bottleneck bandwidth and round-trip propagation time instead of reacting to packet loss.

## Core Model

- BBR builds a model of the path from two measured quantities: bottleneck bandwidth (BtlBw), the max delivery rate observed, and round-trip propagation time (RTprop), the min RTT observed.
- The bandwidth-delay product (BtlBw x RTprop) sets the amount of data needed to fill the pipe; BBR paces sending near this point rather than at the onset of loss.
- Sending rate is governed by a pacing rate derived from BtlBw, and inflight is capped by a cwnd_gain multiple of the BDP.
- Because it targets the actual bottleneck rate, BBR avoids filling deep buffers (bufferbloat) that loss-based controllers tend to keep full.

## Control States

- STARTUP grows the rate exponentially to discover BtlBw, similar to slow start, exiting when bandwidth stops rising.
- DRAIN empties the queue built during STARTUP by temporarily lowering the pacing gain.
- PROBE_BW cycles the pacing gain around 1.0 (a gain-cycling loop) to periodically probe for more bandwidth and yield it back.
- PROBE_RTT briefly reduces inflight to re-measure RTprop, preventing a stale minimum from persisting.

## Tradeoffs

- BBR can be unfair to loss-based flows (e.g. CUBIC) sharing a bottleneck, sometimes claiming a disproportionate share; BBRv2/v3 add loss and ECN response to improve coexistence.
- It performs well on lossy, high-BDP paths where loss-based control underutilizes capacity.

## Sources

- BBR: Congestion-Based Congestion Control - ACM Queue - https://queue.acm.org/detail.cfm?id=3022184
- BBR Congestion Control - IETF datatracker - https://datatracker.ietf.org/doc/draft-cardwell-iccrg-bbr-congestion-control/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
