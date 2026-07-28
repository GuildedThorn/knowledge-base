---
summary: "Minimal, opinionated VPN using Curve25519 keys and the Noise handshake to build fast, stateless-feeling encrypted tunnels."
status: active
tags: [reference, engineering, networking, wireguard, vpn, noise]
private: false
---

# WireGuard VPN Tunnel

## Purpose

A minimal, opinionated VPN using Curve25519 keys and the Noise handshake to build fast, stateless-feeling encrypted tunnels.

## Cryptokey Routing

- Each peer is identified solely by its Curve25519 public key; a peer's allowed-IPs list maps source/destination addresses to that key.
- Outbound packets are routed to the peer whose allowed-IPs contain the destination; inbound packets are only accepted if their source falls in the sending peer's allowed-IPs.
- The cipher suite is fixed and unnegotiated: ChaCha20-Poly1305 for data, Curve25519 for key exchange, BLAKE2s for hashing, avoiding downgrade attacks.

## Noise-Based Handshake

- The 1-RTT handshake is an instantiation of the Noise IK pattern, giving mutual authentication and forward secrecy from ephemeral keys.
- New session keys are derived roughly every two minutes of active traffic, bounding the exposure of any single key.
- A cookie mechanism mitigates handshake-flood denial of service by binding requests to the sender's address under load.

## Roaming and Stateless Design

- WireGuard is connectionless over UDP; the endpoint address of a peer is updated automatically from the source of authenticated packets, enabling seamless roaming across networks.
- Silence is silent: with no traffic there is no keepalive chatter by default, and the interface behaves like a stateless routing table rather than a session daemon.
- The small codebase (a few thousand lines) is a deliberate goal for auditability, and it runs in the Linux kernel for performance.

## Sources

- WireGuard: Next Generation Kernel Network Tunnel - https://www.wireguard.com/papers/wireguard.pdf
- WireGuard - https://www.wireguard.com/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
