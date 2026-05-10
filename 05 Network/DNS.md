## Purpose

Document DNS design, upstream resolvers, local DNS services, and host-specific resolution behavior across ThornCloud.

## Current Known State

- `pfSense Router` is configured with `1.1.1.1` as a DNS server in the captured `April 28, 2026` status snapshot.
- The `nixos` workstation host uses `127.0.0.1` as its resolver and enables `services.technitium-dns-server`.
- The `scout` laptop uses `1.1.1.1` directly and also defines extra local host entries for internal systems.
- The `mitm` host also enables `services.technitium-dns-server`.

## Known DNS Consumers

- `pfSense Router`
- `nixos` workstation
- `mitm`
- `scout`

## Questions To Resolve

- Is pfSense acting only as a gateway, or also as a DNS forwarder/resolver for clients?
- Which host is authoritative for internal `guildedthorn.arpa` names?
- Are `Technitium` instances on `nixos` and `mitm` production DNS services, testing, or parallel experiments?
- Which systems should use local DNS versus public upstream DNS directly?

## Tasks

- [ ] Document whether pfSense provides DNS forwarding or DHCP-advertised DNS to clients
- [ ] Document which host owns internal zone data
- [ ] Document DNS behavior for VPN clients
- [ ] Document split between public DNS, internal DNS, and static host overrides

## Related

- [[01 Maps/Network Map|Network Map]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[02 Systems/NixOS - Host nixos|NixOS - Host nixos]]
- [[02 Systems/NixOS - Host mitm|NixOS - Host mitm]]
- [[02 Systems/NixOS - Host scout|NixOS - Host scout]]
