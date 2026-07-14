## Purpose

Track the phased rollout of the planned SIEM/SOC capability described in [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]].

## Current State

- Nothing in this plan is built yet — this is a fresh initiative, not a partially-done one.
- Depends on unresolved questions in [[05 Network/VLANs|VLANs]] before the network-visibility and purple-team phases can start for real.

## Tasks

### Phase 1 — Core Stand-Up

- [ ] Confirm the `proxmox` hypervisor ([[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]) has spare capacity, or plan resource reallocation
- [ ] Stand up the Kali Purple VM and bring up its Elastic/Wazuh manager stack
- [ ] Set up sops-nix scaffolding for any secrets this introduces (manager enrollment keys, Elastic credentials, TheHive/Cortex API keys)

### Phase 2 — Host Telemetry

- [ ] Package a Wazuh agent for NixOS (`modules/services/wazuh-agent.nix` or an overlay) since none exists upstream
- [ ] Onboard `nixos` as the first Wazuh agent
- [ ] Onboard `scout`, `mac`, `mitm`, `websites`, `proxmox-guest` one at a time

### Phase 3 — Network Visibility

- [ ] Resolve VLAN ID mapping and trunk/access port questions (blocks this phase — see [[05 Network/VLANs|VLANs]])
- [ ] Configure a SPAN/mirror port feeding the Kali Purple VM
- [ ] Bring up Suricata and Arkime against the mirrored traffic

### Phase 4 — Perimeter Logs

- [ ] Forward pfSense syslog to the SIEM
- [ ] Decide whether pfSense should also run its own Suricata/Snort package

### Phase 5 — Purple-Team Loop

- [ ] Carve out an isolated segment for attack-simulation targets, separate from `websites`/`nixos`/`mitm`
- [ ] Stand up a disposable target (reuse `proxmox-guest`/`vmware-test`/`vmware-guest` or build a dedicated vulnerable host)
- [ ] Run a first attack scenario end-to-end and confirm the expected SIEM detections fire

### Phase 6 — Case Management and Alerting

- [ ] Wire up TheHive/Cortex for triage workflow
- [ ] Decide on an alert fan-out target (email, [[07 Projects/ThornBot/ThornBot - Overview|ThornBot]] via Discord, something else)

## Related

- [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]]
- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[08 Improvements/Network Improvements|Network Improvements]]
- [[05 Network/VLANs|VLANs]]
