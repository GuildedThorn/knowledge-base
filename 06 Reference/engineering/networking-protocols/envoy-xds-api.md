---
summary: "The discovery-service protocol (LDS/RDS/CDS/EDS) that dynamically pushes listeners, routes, clusters, and endpoints to Envoy proxies."
status: active
tags: [reference, engineering, networking, envoy, xds, servicemesh]
private: false
---

# Envoy xDS Configuration APIs

## Purpose

The discovery-service protocol (LDS/RDS/CDS/EDS) that dynamically pushes listeners, routes, clusters, and endpoints to Envoy proxies.

## xDS Resource Types

- LDS (Listener Discovery Service) supplies listeners, the sockets Envoy binds to accept traffic.
- RDS (Route Discovery Service) supplies HTTP route tables referenced by listeners.
- CDS (Cluster Discovery Service) supplies clusters, the logical groups of upstream services.
- EDS (Endpoint Discovery Service) supplies the concrete endpoint addresses within each cluster.
- Together these let a control plane reconfigure a running proxy without restarts or config-file reloads.

## Delivery and Consistency

- State-of-the-World (SotW) delivery sends the full set of resources on every update for a resource type.
- Incremental (Delta) xDS sends only added or removed resources, reducing bandwidth for large fleets.
- Aggregated Discovery Service (ADS) multiplexes all resource types over a single gRPC stream to enforce a deterministic update ordering.
- xDS provides eventual consistency; ADS ordering avoids transient traffic drops from applying, for example, a cluster before its endpoints.

## Sources

- Envoy xDS Protocol - https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol
- Envoy Documentation - https://www.envoyproxy.io/docs/envoy/latest/

## Related

- [Networking and Protocols - Index](kb://06-reference-engineering-networking-protocols-networking-protocols-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
