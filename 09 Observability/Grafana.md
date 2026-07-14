## Purpose

Document Grafana usage across ThornCloud for dashboards and (planned) SIEM visualization.

## Current State

- Grafana is defined (but currently `enable = false`) on the `proxmox-mitm` NixOS host — see [[02 Systems/NixOS - Host proxmox-mitm|Host proxmox-mitm]]. It's bound to `127.0.0.1:3000` there, intended to sit behind the same NGINX reverse proxy as the rest of that host's services, at `grafana.guildedthorn.arpa`.
- [[GuildedThorn.com - Overview|GuildedThorn.com]] ships application logs via Serilog to a Loki sink (`Loki:Uri` in config), but no Loki server is currently documented as deployed anywhere in `ThornixOS` — so this Grafana instance has no confirmed data source wired up yet.
- No dashboards, alert rules, or data sources are documented as configured.

## Planned Role

If the [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC plan]] moves forward, Grafana is the intended visualization layer for application logs (via Loki) kept deliberately separate from the Wazuh/Elastic security-telemetry path, cross-linked rather than merged.

## Related

- [[01 Maps/Observability Map|Observability Map]]
- [[02 Systems/NixOS - Host proxmox-mitm|Host proxmox-mitm]]
- [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
