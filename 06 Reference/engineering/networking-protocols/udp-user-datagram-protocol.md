---
summary: "The connectionless, unreliable datagram transport adding only ports and a checksum atop IP, forming the base for DNS, QUIC, and real-time media."
status: active
tags: [reference, engineering, networking, udp, datagram, transport]
private: false
---

# User Datagram Protocol (UDP)

## Purpose

The connectionless, unreliable datagram transport that adds only ports and a checksum atop IP, forming the base for DNS, QUIC, and real-time media.

## Header and Checksum

- The UDP header is a fixed 8 bytes: 16-bit source port, 16-bit destination port, 16-bit length, and 16-bit checksum.
- The checksum covers the header, the data, and a pseudo-header drawn from the IP layer (addresses and protocol), catching misdelivery as well as corruption.
- Over IPv4 the checksum is optional and a value of zero signals "not computed"; over IPv6 the checksum is mandatory.
- Length counts the header plus data, bounding a datagram to what fits in a single IP packet.

## Connectionless Semantics

- UDP has no handshake, sequence numbers, acknowledgements, or retransmission; datagrams may be lost, duplicated, or reordered with no notification.
- Each sendto delivers one self-contained message with preserved boundaries, unlike TCP's byte stream.
- It suits DNS queries, real-time audio/video, and tunneling/transport substrates such as QUIC where the application supplies its own reliability.

## Usage Guidelines

- Applications must implement their own congestion control (or use a tuned library), since UDP itself does nothing to avoid overwhelming a path.
- Senders should keep datagrams within the path MTU to avoid IP fragmentation, and should rate-limit and back off to coexist with responsive traffic.

## Sources

- RFC 768 - User Datagram Protocol - https://www.rfc-editor.org/rfc/rfc768
- RFC 8085 - UDP Usage Guidelines - https://www.rfc-editor.org/rfc/rfc8085

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
