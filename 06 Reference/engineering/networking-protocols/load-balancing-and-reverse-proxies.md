---
summary: "Load balancers and reverse proxies route traffic, terminate TLS, enforce policy, perform health checks, and shape failure behavior."
status: active
tags: [reference, engineering, networking, load-balancing]
private: false
---

# Load Balancing and Reverse Proxies

## Purpose

Load balancers and reverse proxies route traffic, terminate TLS, enforce policy, perform health checks, and shape failure behavior.

## Core Model

- Layer 4 balancing routes connections; Layer 7 proxies inspect application protocol semantics.
- Algorithms include round-robin, least-connections, EWMA/latency, consistent hashing, and locality-aware routing.
- Health checks define whether traffic is sent to an instance; bad checks cause outages or black holes.

## Engineering Notes

- Separate readiness, liveness, and dependency health; do not route traffic to instances that cannot serve it.
- Preserve client IP and request IDs deliberately through X-Forwarded-For/Forwarded headers and trusted proxy settings.
- Tune timeouts across client, proxy, upstream, and app so failures are bounded and explainable.

## Sources

- NGINX reverse proxy docs - https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
- Envoy architecture overview - https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/arch_overview
- HAProxy documentation - https://docs.haproxy.org/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
