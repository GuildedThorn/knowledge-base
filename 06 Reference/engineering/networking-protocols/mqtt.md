---
summary: "A lightweight broker-based publish/subscribe protocol for constrained IoT devices with tiered quality-of-service delivery guarantees."
status: active
tags: [reference, engineering, networking, mqtt, pubsub, iot]
private: false
---

# MQTT Publish/Subscribe Messaging

## Purpose

A lightweight broker-based publish/subscribe protocol for constrained IoT devices with tiered quality-of-service delivery guarantees.

## Broker and Topic Model

- Clients never talk directly; a central broker receives PUBLISH messages and routes them to clients that have SUBSCRIBEd to matching topics.
- Topics are hierarchical UTF-8 strings separated by slashes (e.g., home/livingroom/temp), supporting single-level (+) and multi-level (#) wildcards.
- The protocol runs over TCP with a compact fixed 2-byte minimum header, minimizing overhead for low-bandwidth, high-latency networks.
- MQTT 5.0 adds features such as user properties, reason codes, shared subscriptions, and message expiry intervals over the 3.1.1 baseline.

## QoS 0/1/2 Delivery

- QoS 0 (at most once) fires and forgets with no acknowledgement, so messages may be lost.
- QoS 1 (at least once) uses PUBACK acknowledgements and may deliver duplicates on retransmission.
- QoS 2 (exactly once) uses a four-part PUBREC/PUBREL/PUBCOMP handshake to guarantee single delivery at the cost of more round trips.

## Retained Messages, LWT, and Keepalive

- A retained message is stored by the broker per topic and delivered immediately to any new subscriber, conveying last-known state.
- The Last Will and Testament is a message the broker publishes on a client's behalf if it disconnects ungracefully.
- A keepalive interval and PINGREQ/PINGRESP exchange let the broker detect dead connections; persistent sessions retain subscriptions across reconnects.

## Sources

- MQTT Version 5.0 - OASIS - https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
