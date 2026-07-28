---
summary: "The socket-based kernel-to-userspace messaging protocol used to configure and query the networking stack."
status: active
tags: [reference, engineering, linux, netlink, rtnetlink, ipc]
private: false
---

# Netlink Sockets

## Purpose

The socket-based kernel-to-userspace messaging protocol used to configure and query the networking stack.

## Core Model

- Netlink is a datagram-oriented address family (`AF_NETLINK`) opened with `socket(AF_NETLINK, SOCK_RAW|SOCK_DGRAM, protocol)`, where the protocol selects a subsystem family.
- Families include `NETLINK_ROUTE` (rtnetlink), `NETLINK_NETFILTER`, `NETLINK_KOBJECT_UEVENT`, and the extensible `NETLINK_GENERIC`.
- Messages carry a fixed `nlmsghdr` (length, type, flags, sequence, pid) followed by a family-specific payload, and can be batched into a single send.

## How It Works

- Payloads use nested TLV attributes (`rtattr` / `nlattr`), giving forward- and backward-compatible extensibility without breaking older parsers.
- rtnetlink manages links, addresses, routes, neighbors, and traffic control; tools like `ip` (iproute2) speak it instead of legacy ioctls.
- Multicast groups let the kernel push asynchronous notifications (e.g. link up/down, route changes) to subscribed listeners; generic netlink multiplexes new subsystems over one protocol number.

## Engineering Notes

- Requests set `NLM_F_REQUEST`; dumps add `NLM_F_DUMP`, and the kernel replies with a sequence terminated by `NLMSG_DONE`, with errors delivered as `NLMSG_ERROR`.
- Reliability is app-managed via sequence numbers; delivery is best-effort and can drop (`ENOBUFS`) under buffer pressure.

## Sources

- man7 - netlink(7) - https://man7.org/linux/man-pages/man7/netlink.7.html
- RFC 3549 - Linux Netlink as an IP Services Protocol - https://www.rfc-editor.org/rfc/rfc3549

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
