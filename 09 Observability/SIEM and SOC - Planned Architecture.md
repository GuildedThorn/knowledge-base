## Purpose

Plan how a SIEM/SOC capability could be added to ThornCloud using Kali Purple, without inventing claims about anything that exists today. Nothing in this note is built yet — see [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]] for the task-level tracker.

## Current State (Why This Doesn't Exist Yet)

- There is no central log aggregation live today: `09 Observability/Grafana.md` documents Grafana as present but disabled (on `proxmox-mitm`), and Loki is only referenced as a log-sink URI in [[GuildedThorn.com - Overview|GuildedThorn.com]]'s config — no Loki server is documented as deployed.
- No host-based EDR/telemetry agents, no network IDS, and no case-management tooling exist on any host today.
- `pfSense Router` is the only perimeter device; VLAN segmentation is still an open question (see [[05 Network/VLANs|VLANs]]).

## What Kali Purple Actually Is

Kali Purple is a Kali Linux variant aimed at purple-team work: it bundles the standard offensive Kali toolset with a defensive/SOC stack — Elastic Stack (SIEM indexing and dashboards), Suricata (network IDS), Arkime (full packet capture and session hunting), TheHive + Cortex (case management and automated enrichment), and optionally Zeek and MISP — pre-integrated as something close to a SOC-in-a-box, guided by a NIST CSF-aligned workflow. It is a Debian-based appliance, not something that fits the Nix module pattern directly.

## Placement

The physical [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]] is the strongest fit to host this: it's the box already running the `proxmox` hypervisor underneath `websites`, `proxmox-guest`, and `proxmox-mitm`, and at 128 GB RAM / dual Xeon X5690 it has far more headroom than anything else in the fleet — relevant because Elastic + Suricata + Arkime are memory- and disk-hungry (indices and PCAP retention both grow fast). Proposed: a new Kali Purple VM alongside the existing Proxmox guests there, sized around 8–16 GB RAM / 4 vCPU / 200+ GB disk to start.

## Two Ways to Get the Defensive Stack, and Which One Fits Better

- **Run Kali Purple as-is** (single appliance VM): fastest to stand up, gets the pre-integrated Elastic + Wazuh + Suricata + Arkime + TheHive/Cortex stack in one place, and keeps the offensive Kali tooling on the same box for purple-team exercises. Downside: it's an unmanaged Debian appliance sitting outside the `ThornixOS` flake — no `comin` GitOps, no sops-nix, config drift has to be tracked by hand.
- **Build the same capability natively in `ThornixOS`** (separate `modules/services/*.nix` for an Elastic/OpenSearch stack, Suricata, Wazuh manager): fits the dendritic pattern, gets sops-managed secrets and `comin` deploys like everything else, but is considerably more work since none of these exist as ready-made NixOS service modules the way `services.grafana` does — each would need real packaging/config effort.

Recommendation: start with the Kali Purple appliance for the SIEM/SOC core (fast, proven, integrated), and treat the "native NixOS module" path as a later optimization once the workflow is validated — not a blocker to getting started.

## Architecture Sketch

1. **Kali Purple VM** on the `proxmox` hypervisor (Mac Pro 5,1), on the same internal segment as `websites`/`proxmox-guest`/`proxmox-mitm`.
2. **Network visibility**: a SPAN/mirror port on the switch feeding pfSense's internal interfaces (the `OPT1` `172.16.25.1` segment where `websites` and `mitm` live) forwards a copy of traffic to Suricata/Arkime on the Kali Purple VM for passive NIDS and packet capture. This depends on resolving the still-open VLAN mapping questions in [[05 Network/VLANs|VLANs]].
3. **Host telemetry**: Wazuh agents on the real NixOS fleet (`nixos`, `scout`, `mac`, `mitm`, `websites`, `proxmox-guest`) reporting to the Wazuh manager bundled in Kali Purple. There's no existing NixOS packaging for the Wazuh agent, so this needs a new `modules/services/wazuh-agent.nix` in `ThornixOS` (or an overlay pulling the upstream `.deb`/tarball agent) before any host can be onboarded.
4. **Log centralization**: keep Loki/Grafana as the application-log path (already the intended sink for [[GuildedThorn.com - Overview|GuildedThorn.com]]) separate from the SIEM's security-telemetry path (Wazuh/Elastic), rather than trying to merge the two — cross-link dashboards in Grafana once both are live instead of collapsing them into one pipeline.
5. **Perimeter logs**: forward pfSense syslog (and Suricata/Snort alerts if pfSense ends up running its own IDS package) into the SIEM.
6. **Secrets**: Wazuh manager enrollment keys, Elastic credentials, and TheHive/Cortex API keys should go through sops-nix the same way `nixos` and `websites` already do — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]].

## Purple-Team Loop

Since this is explicitly Kali Purple and not just Kali, the point isn't only passive monitoring — it's closing the loop: run the offensive tooling from the same box (or a dedicated attack VM) against disposable targets (`proxmox-guest`, `vmware-test`, `vmware-guest`, or a new purpose-built vulnerable target host) and confirm the SIEM actually fires the expected detections. This should run on an isolated segment so red-team traffic never touches `websites`, `nixos`, or `mitm` — another reason to resolve the VLAN questions first.

## Open Questions

- Does the `proxmox` hypervisor (Mac Pro 5,1) have spare capacity for this alongside its current guests, or does it need a resource audit first?
- Should pfSense itself run a Suricata/Snort package for perimeter-level detection, or should all NIDS work happen passively from the SPAN port into Kali Purple?
- Is there an isolated VLAN/segment available today for purple-team exercise targets, or does one need to be carved out?
- What's the alerting fan-out target (email, Discord via [[07 Projects/ThornBot/ThornBot - Overview|ThornBot]], something else) — no notification channel is currently documented for this.

## Related

- [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]
- [[01 Maps/Observability Map|Observability Map]]
- [[09 Observability/Grafana|Grafana]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[05 Network/VLANs|VLANs]]
- [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]]
- [[03 Devices/pfSense Router|pfSense Router]]
