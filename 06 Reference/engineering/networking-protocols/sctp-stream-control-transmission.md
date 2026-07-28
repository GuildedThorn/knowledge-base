---
summary: "A message-oriented transport offering multi-streaming, multi-homing, and a four-way handshake resistant to SYN flooding."
status: active
tags: [reference, engineering, networking, sctp, multihoming, multistreaming]
private: false
---

# Stream Control Transmission Protocol (SCTP)

## Purpose

A message-oriented transport offering multi-streaming, multi-homing, and a four-way handshake resistant to SYN flooding.

## Association Setup

- SCTP connections are called associations and are established with a four-way handshake (INIT, INIT-ACK, COOKIE-ECHO, COOKIE-ACK).
- The responder stays stateless until the cookie returns, so it allocates no resources for an unconfirmed peer, defeating SYN-flood-style resource exhaustion.
- Data is exchanged in variable-length chunks bundled into packets, and SCTP preserves message boundaries rather than presenting a byte stream.

## Multi-Streaming

- An association carries multiple independent streams, each with its own ordered delivery, so loss in one stream does not stall delivery in the others (no cross-stream head-of-line blocking).
- Applications may request unordered delivery per message when ordering is unnecessary.
- Reliability is connection-wide via a single transmission-sequence-number space, while ordering is tracked per stream.

## Multi-Homing and Failover

- Each endpoint can bind multiple IP addresses; one path is primary and the others are backups for the same association.
- Heartbeats monitor idle destination addresses, and on primary-path failure traffic fails over to an alternate address without re-establishing the association.
- Multi-homing gives network-level fault tolerance transparently to the application, which is why SCTP is used in telephony signaling (SIGTRAN) and WebRTC data channels (over DTLS).

## Sources

- RFC 9260 - Stream Control Transmission Protocol - https://www.rfc-editor.org/rfc/rfc9260

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
