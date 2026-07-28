---
summary: "The netfilter framework and nftables packet-classification engine that replaces iptables for Linux firewalling."
status: active
tags: [reference, engineering, linux, nftables, firewall, netfilter]
private: false
---

# nftables and Netfilter

## Purpose

The netfilter framework and nftables packet-classification engine that replaces iptables for Linux firewalling.

## Core Model

- Netfilter is the in-kernel framework exposing packet-processing *hooks* along the network path: prerouting, input, forward, output, and postrouting.
- nftables is the modern userspace and kernel classifier that attaches base chains to those hooks; it supersedes iptables, ip6tables, arptables, and ebtables under one tool.
- The pipeline is tables (per address family: ip, ip6, inet, arp, bridge, netdev) containing chains containing ordered rules.

## How It Works

- A base chain declares its hook and an integer *priority* that orders it relative to other subsystems (e.g. conntrack, NAT); lower numbers run earlier.
- Rules combine expressions (matches) with a verdict such as `accept`, `drop`, `jump`, `goto`, or `continue`; regular chains without a hook act as reusable jump targets.
- Named *sets* and *maps* enable O(1) lookups and data-driven dispatch (e.g. verdict maps), replacing long linear rule chains from iptables.

## Operational Notes

- Connection tracking (conntrack) supplies stateful matching via `ct state` (new, established, related, invalid), the basis for stateful firewalls and NAT.
- One `nft` atomic transaction applies a whole ruleset or fails cleanly, avoiding the partial-apply races common with iptables scripting.

## Sources

- nftables wiki - https://wiki.nftables.org/wiki-nftables/index.php/Main_Page
- netfilter.org project - https://www.netfilter.org/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
