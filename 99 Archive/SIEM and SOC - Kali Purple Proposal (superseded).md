---
summary: "Plan how a SIEM/SOC capability could be added to ThornCloud using Kali Purple, without inventing claims about anything that existed at the time."
status: superseded
tags: [archive]
---

> [!warning] Archived — superseded, does not reflect reality
> This was an early proposal to build the SIEM/SOC around a **Kali Purple appliance** (Elastic / Wazuh / Suricata / Arkime / TheHive-Cortex). It was **not** the path taken — the capability was built natively in the `ThornixOS` flake instead. Kept only as a record of the plan that was rejected. For the real design see [[09 Observability/SIEM and SOC - Architecture|SIEM and SOC - Architecture]]; for status see [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]].

## Purpose (as originally written)

Plan how a SIEM/SOC capability could be added to ThornCloud using Kali Purple, without inventing claims about anything that existed at the time.

## What Kali Purple Is

Kali Purple is a Kali Linux variant aimed at purple-team work: it bundles the standard offensive Kali toolset with a defensive/SOC stack — Elastic Stack (SIEM indexing and dashboards), Suricata (network IDS), Arkime (full packet capture and session hunting), TheHive + Cortex (case management and automated enrichment), and optionally Zeek and MISP — pre-integrated as something close to a SOC-in-a-box, guided by a NIST CSF-aligned workflow. It is a Debian-based appliance, not something that fits the Nix module pattern directly.

## Proposed Placement

The physical [[03 Devices/Mac Pro 5,1|Mac Pro 5,1]] was the strongest fit to host it: the box already running the `proxmox` hypervisor underneath `websites`, `proxmox-guest`, and `proxmox-mitm`, with 128 GB RAM / dual Xeon X5690 for the memory- and disk-hungry Elastic + Suricata + Arkime. Proposed: a new Kali Purple VM alongside the existing Proxmox guests, ~8–16 GB RAM / 4 vCPU / 200+ GB disk to start.

## The Two Options Considered

- **Run Kali Purple as-is** (single appliance VM): fastest to stand up, pre-integrated stack in one place, offensive tooling on the same box for purple-team exercises. Downside: an unmanaged Debian appliance outside the `ThornixOS` flake — no `comin` GitOps, no sops-nix, drift tracked by hand.
- **Build the same capability natively in `ThornixOS`** (`modules/services/*.nix` for Elastic/OpenSearch, Suricata, Wazuh manager): fits the dendritic pattern, sops-managed secrets, `comin` deploys — but considerably more packaging work.

Original recommendation was to start with the appliance and treat native as a later optimization.

## Why It Was Dropped

The native path was taken instead — and taken *lighter* than either option here. Grafana + Loki + Prometheus (already the app-log stack) cover indexing/dashboards/alerting; auditd + journal shipping cover host telemetry; Suricata + CrowdSec + a detection canary cover detection; Discord covers alert fan-out. Elastic, Wazuh, TheHive/Cortex, and Arkime were all judged unnecessary weight for a one-person SOC. See [[09 Observability/SIEM and SOC - Architecture|the current architecture]].
