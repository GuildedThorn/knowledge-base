---
summary: General/advanced networking concepts beyond ThornCloud's own home-lab setup — routing protocols, VLANs, QoS, overlays, SDN, segmentation, TCP tuning.
status: active
tags: [reference, networking]
private: false
---

## Purpose

ThornCloud's own network is documented in [Network Map](kb://01-maps-network-map) (flat /24s on pfSense, no VLANs, static routing, WireGuard road-warrior). This note is the general/advanced reference layer for concepts *not* currently in use there — useful for understanding larger networks (enterprise, cloud, ISP-scale) or as a reference if the home-lab ever grows into them. Compiled 2026-07-24.

## Dynamic Routing: OSPF vs BGP

**OSPF** — link-state interior gateway protocol (IGP), single autonomous system. Every router floods Link State Advertisements to build an identical topology map, then runs Dijkstra locally. **Areas** scale it: Area 0 (backbone) is mandatory, all other areas connect through it; stub/NSSA areas limit external-route flooding. Cost is cumulative from interface bandwidth (`reference-bandwidth / interface-bandwidth`; often bumped above the 100 Mbps default on modern gear). Sub-second to few-second convergence. Use when you control every hop and want automatic failover between redundant internal paths — static routing can't do that.

**BGP** — path-vector exterior gateway protocol (EGP), the internet's own routing protocol. Each AS has an ASN (16-bit 1–65535, or 32-bit up to ~4.29B since the legacy space exhausted; private: 64512–65534 / 4200000000–4294967294). Routers exchange full AS-paths, not costs — a route with your own ASN already in its path is rejected (native loop prevention). Incremental UPDATE/WITHDRAW messages, not periodic refresh, which is why route flaps ripple across the internet within seconds. The **default-free zone (DFZ)** — Tier-1 backbones carrying the full ~1M+ prefix table with no default route — sits above everyone else, who either peer (settlement-free) or buy transit via IXPs. Use BGP the moment you're multihomed (2+ upstreams) or originate your own prefixes; a single-uplink network has no BGP use case.

**RPKI / route-origin validation (2025–2026 state):** adoption is partial — [NIST's monitor](https://rpki-monitor.antd.nist.gov/) shows ~35% of routes RPKI-valid, ~63% still unsigned, but ~70% of *traffic volume* rides valid routes (large networks signed first). Only ~6.5% of internet users sit behind an AS that actually filters on ROV. Real incidents keep illustrating the gap: a May 2025 leak from AS22773 leaked 4,651 routes, 4,644 of which ROV would have rejected; a January 2026 Cloudflare IPv6 leak came from an overly-permissive iBGP-to-eBGP export policy, independent of RPKI entirely. Route leaks remain a live risk even where RPKI is deployed.

## VLANs and Trunking

Not used anywhere in ThornCloud today (see [VLANs](kb://05-network-vlans)) — reference for if/when that changes.

- **802.1Q tagging**: 4-byte tag, 12-bit VLAN ID (1–4094 usable, 4095 reserved), inserted between source MAC and EtherType.
- **Access port**: one VLAN, untagged — what an end host connects to.
- **Trunk port**: multiple VLANs tagged over one link, between switches or to a router doing inter-VLAN routing. A "native" VLAN can ride untagged on a trunk — the classic VLAN-hopping attack (double-tagging) exploits exactly this.
- **Inter-VLAN routing**: *router-on-a-stick* (one trunked interface, subinterfaces per VLAN e.g. `eth0.10`) is simple but bottlenecks all inter-VLAN traffic through one link/engine; an **L3 switch (SVI)** routes in ASIC hardware at line rate and is the standard enterprise/campus pattern.

## QoS and Traffic Shaping

- **DSCP**: 6 bits in the IP header (64 markings). `EF` (46) for voice, `AF` (4 classes × 3 drop precedences, e.g. AF41) for video/business traffic, `CS` legacy, `BE`/0 default.
- Marking alone does nothing — needs queuing/scheduling (priority queuing, WFQ, LLQ) configured at every congested hop.
- **Shaping vs policing**: policing drops/re-marks traffic over a rate immediately, no buffer — bursty and lossy. Shaping buffers and releases smoothed to the rate — adds latency, avoids drops. Shape on your own egress where you control the queue; police at trust boundaries (ISP enforcing a subscribed rate).
- Matters most for VoIP/gaming/video-conferencing: latency/jitter-sensitive (VoIP wants <150ms one-way, <30ms jitter, <1% loss) but low-bandwidth — the goal is a reserved priority slice ahead of bulk transfers, not raw bandwidth.

## Overlay Networking

- **VXLAN**: encapsulates L2 Ethernet in UDP/IP (port 4789), 24-bit VNI (~16M segments) — solves 802.1Q's 4094-VLAN ceiling, a real constraint at multi-tenant cloud/datacenter scale. VTEPs (top-of-rack switches or hypervisors) do encap/decap, stretching L2 domains over a routed L3 underlay (spine-leaf fabrics). Underpins most modern datacenter fabrics and cloud provider virtual networks.
- **GRE**: simpler, protocol-agnostic IP-in-IP tunneling, no native encryption — paired with IPsec for site-to-site VPNs, or MPLS-over-GRE / multicast tunneling.
- Overlays are what SDN controllers program dynamically — instead of hand-configuring VTEPs/VNIs per switch, a controller (VMware NSX, Cisco ACI) pushes overlay policy centrally, keeping the underlay "dumb."

## Software-Defined Networking (SDN)

Separates the **control plane** (routing/policy decisions) from the **data plane** (packet forwarding in ASIC hardware), centralizing control in software. **OpenFlow** was the original southbound protocol (controller programs switch flow tables: match-on-headers → forward/drop/rewrite/send-to-controller); in practice adoption has shifted to vendor/controller-specific APIs and overlay-based SDN rather than pure OpenFlow, but the control/data-plane split it introduced is now standard. Cloud providers use it to orchestrate policy across tens of thousands of switches/hypervisors via API (tied into Kubernetes/OpenStack) instead of per-device CLI config.

## Segmentation at Scale: Zero Trust / Microsegmentation

- **Perimeter model** (what VLAN segmentation implements): binary trust — inside the boundary is trusted, lateral movement inside a segment is largely unchecked.
- **Zero trust**: "never trust, always verify" — every flow, even same-subnet, authenticated/authorized individually (identity, device posture, workload identity), not IP/subnet-based.
- **Microsegmentation**: zero trust applied at the network layer — enforcement per-workload (host firewalls, hypervisor policy, service-mesh sidecars) rather than per-VLAN, so a compromised host can't laterally reach neighbors on the same segment without explicit policy. Materially finer than VLAN segmentation, which only stops *inter*-VLAN traffic. Adoption is still early (~5–20% of enterprises deployed vs ~90% who call it important); ransomware lateral-movement containment is the main driver. Platforms: Illumio, Cisco Secure Workload, VMware NSX.

## TCP Performance Tuning

- **Window scaling** (RFC 7323): the original 16-bit window field caps at 65,535 bytes, too small for high-bandwidth-delay-product links. The scale option multiplies by 2^N (N≤14) to reach ~1GB windows — needed to saturate fast, high-RTT links.
- **Congestion control — BBR vs CUBIC**: CUBIC (Linux long-time default) is loss-based — probes by increasing rate until packet loss, tends to fill buffers first (bufferbloat). BBR (Google, now BBRv3) is model-based — estimates actual bottleneck bandwidth + RTT and paces to match rather than waiting for loss; generally higher throughput on lossy/shallow-buffer links (wireless/cellular) and lower queuing delay on deep-buffer links. No universal consensus yet on replacing CUBIC as default (2025 research still debating); Google/YouTube/Spotify use BBR at scale, most distros still default CUBIC.
- **MTU/MSS and PMTUD**: standard Ethernet MTU 1500, MSS ≈ MTU−40. Tunnel overhead (WireGuard, VXLAN, GRE, IPsec) eats into effective MTU — directly the cause of the "MTU black hole" already documented in [WireGuard - Road Warrior](kb://05-network-wireguard-road-warrior): PMTUD relies on ICMP "Fragmentation Needed"/"Packet Too Big" messages, and cellular carriers/middleboxes often silently drop those, so senders never learn to shrink packets and connections hang. Mitigations: MSS clamping at the tunnel endpoint, or **PLPMTUD** (RFC 8899), which probes via real data packets/timeouts instead of depending on ICMP.

## Anycast, Unicast, Multicast

- **Unicast**: one sender, one receiver — default for nearly all traffic.
- **Multicast**: one sender, a subscribed group (224.0.0.0/4), IGMP for membership + PIM for routing. IPTV, market-data feeds, some IGP traffic (OSPF itself uses 224.0.0.5/6 for neighbor discovery) — rarely enabled inter-domain on the public internet.
- **Anycast**: one IP advertised via BGP from multiple geographically distributed sites; normal BGP best-path selection routes each client to the topologically nearest instance. DNS root servers are all anycast (1,900+ physical instances behind the "13 servers"), which is what makes root DNS resilient to regional failure/DDoS. CDNs anycast edge IP space so clients hit the nearest PoP with no client-side logic — also a natural DDoS mitigation since attack traffic distributes across every site.

## Related

- [Network Map](kb://01-maps-network-map)
- [VLANs](kb://05-network-vlans)
- [Routing](kb://05-network-routing)
- [WireGuard - Road Warrior](kb://05-network-wireguard-road-warrior)
- [Firewall - pfSense](kb://05-network-firewall-pfsense)
- [Reference Map](kb://01-maps-reference-map)
