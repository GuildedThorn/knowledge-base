## Purpose

Track the remaining documentation and cleanup work for the pfSense router.

## Current State

- The router has a clean device note and a separate pfSense firewall note.
- The current documentation came from a status dashboard snapshot dated `April 28, 2026`.
- Firewall, NAT, DHCP, and VPN behavior are only partially captured.

## Tasks

- [ ] Record interface assignments with real switch ports and cable paths
- [ ] Record the real IP or purpose of `MGMT`
- [ ] Document firewall rules by interface
- [ ] Document which interfaces are allowed to reach the pfSense admin UI
- [ ] Document NAT and port forwarding
- [ ] Document outbound NAT mode
- [ ] Document DHCP scopes and static mappings per internal interface
- [ ] Document DNS resolver/forwarder behavior and any overrides
- [ ] Document OpenVPN access scope and client expectations
- [ ] Document what public services on `guildedthorn.com` depend on pfSense forwards versus downstream reverse proxies
- [ ] Add backup and restore procedure

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[Firewall - pfSense|Firewall - pfSense]]
