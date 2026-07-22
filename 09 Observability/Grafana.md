## Purpose

Document Grafana usage across ThornCloud for dashboards and SIEM visualization.

## Current State

- Grafana is **live on the dedicated `soc` VM** at `https://soc.guildedthorn.arpa:3000`, TLS via a ThornCloud_CA-signed cert (the fleet trusts that CA; the private key stays in sops). Admin password, secret key, and the Discord alert webhook are all sops-managed and injected via `$__file{}`, never touching the Nix store.
- Fully provisioned from the `ThornixOS` repo (`modules/computers/soc.nix` + `hosts/soc/dashboards/`) — datasources, dashboards, contact points, notification policies, and alert rules are all Nix-declared. UI edits are allowed but survive only until the next `comin` deploy; the repo JSON is the source of truth.
- Datasources: **Loki** (`127.0.0.1:3100`, journal + Suricata EVE + pfSense syslog from the whole fleet) and **Prometheus** (`127.0.0.1:9090`, node/comin/Loki metrics — the default).
- Five dashboards in a SIEM folder: SOC Overview, Fleet Health, Fleet Deploys, Endpoint Activity, Pipeline Health.
- Alerting: a `siem` rule group (host down, SSH brute force, Suricata/CrowdSec hits, comin deploy failures, log-silence and detection-canary rules) delivers to Discord, with a severity-split policy — critical pages at 10s/1m and re-notifies hourly, warnings batch at 30s/5m/4h.
- The earlier disabled Grafana definition on `proxmox-mitm` is superseded by this instance.
- [[GuildedThorn.com - Overview|GuildedThorn.com]] ships application logs via Serilog to a Loki sink; with Loki live on `soc`, application logs and security telemetry share one query surface.

## Related

- [[01 Maps/Observability Map|Observability Map]]
- [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]
- [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]]
- [[GuildedThorn.com - Overview|GuildedThorn.com]]
