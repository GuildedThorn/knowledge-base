---
summary: "How network namespaces isolate the networking stack and veth pairs bridge packets between namespaces."
status: active
tags: [reference, engineering, linux, netns, veth, virtual-networking]
private: false
---

# Network Namespaces and veth Pairs

## Purpose

How network namespaces isolate the networking stack and veth pairs bridge packets between namespaces.

## Core Model

- A network namespace gives a process its own copy of the network stack: interfaces, routing table, firewall rules, /proc/net, port space, and sockets.
- A newly created namespace starts empty except for a loopback device, which is down by default.
- Physical and virtual interfaces belong to exactly one namespace at a time and can be moved between them.
- Namespaces are referenced by processes or by named entries under /var/run/netns (used by `ip netns`).

## How It Works

- A veth (virtual Ethernet) device is always created as a connected pair acting like a pipe: a frame sent on one end appears on the other.
- Placing each end in a different namespace forms a point-to-point tunnel, the standard way to connect an isolated namespace to a parent or a bridge.
- One veth end is typically moved into the container namespace while the peer stays in the host, often attached to a Linux bridge or subject to NAT.
- Assigning addresses and enabling both ends provides routable connectivity between the namespaces.

## Operational Notes

- Container runtimes build per-container networking from these primitives: a namespace plus a veth pair into a host bridge.
- Deleting either veth end destroys the pair; deleting a namespace releases its interfaces (virtual ones vanish, physical ones return to the default namespace).

## Sources

- man7 - network_namespaces(7) - https://man7.org/linux/man-pages/man7/network_namespaces.7.html
- man7 - veth(4) - https://man7.org/linux/man-pages/man4/veth.4.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
