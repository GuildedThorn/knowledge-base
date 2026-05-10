## Purpose

Document firewall policy, interface separation, NAT behavior, VPN exposure, and validation steps for the ThornCloud pfSense edge router.

## Scope

This note applies to [[03 Devices/pfSense Router|pfSense Router]] at `pfsense.guildedthorn.arpa`.

## Current Interface Inventory

- `WAN`: public-facing interface with `64.53.182.82`
- `LAN`: internal network gateway at `192.168.1.1`
- `OPT1`: internal network gateway at `172.16.25.1`
- `MGMT`: management-facing interface, present but no IP shown in the captured status view
- `OPT3`: internal network gateway at `10.0.8.1`

## Firewall Intent

- `WAN` should remain default-deny except for explicitly exposed services.
- `LAN`, `OPT1`, `MGMT`, and `OPT3` should be treated as separate trust zones with deliberate inter-zone rules.
- Broadcast and multicast noise should be evaluated per interface rather than broadly allowed.
- VPN traffic should be constrained to the internal networks and services that actually need remote access.

## Observed Status Snapshot

From the `Tuesday, April 28, 2026` status capture:

- blocked traffic was visible on `WAN`, `LAN`, and `MGMT`
- blocked `WAN` traffic included unsolicited external traffic
- blocked internal traffic included `mDNS` multicast and broadcast traffic
- state table usage was `213 / 1632000`
- OpenVPN listener shown was `UDP4:1194`

## Rules To Document Next

- default allow or deny posture per internal interface
- management-plane access rules for the pfSense web UI and SSH
- DNS policy for each subnet
- inter-VLAN routing rules
- outbound restrictions or egress filtering
- logging rules that are intentionally noisy versus actually actionable

## NAT and Port Forwarding

The current pasted status page does not show NAT details. This note should eventually track:

- outbound NAT mode
- inbound port forwards
- 1:1 NAT mappings if any
- reflection/hairpin behavior if enabled
- which internal services are intentionally exposed to `WAN`

## VPN

Current known details:

- OpenVPN service name: `ThornCloud Private Network`
- Transport: `UDP4`
- Port: `1194`
- Connected clients at capture time: `0`

Document next:

- tunnel subnet
- client access scope
- split-tunnel versus full-tunnel behavior
- certificate/auth method
- DNS behavior for VPN clients

## Validation

When changing firewall or NAT behavior, verify:

- management access still works from the intended network
- internal DNS resolution still works
- exposed public services are reachable only on intended ports
- VPN clients can reach only intended internal networks
- logs do not show unexpected new deny events after a change

## Change Log Cues

Record these each time rules change:

- date of change
- interface affected
- reason for change
- expected user-visible effect
- rollback path

## Related

- [[03 Devices/pfSense Router|pfSense Router]]
- [[01 Maps/Network Map|Network Map]]
