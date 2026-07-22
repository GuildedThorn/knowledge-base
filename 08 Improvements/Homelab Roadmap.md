## Purpose

Collect planned homelab infrastructure work that doesn't yet warrant its own dedicated note — bigger items graduate out of here once there's real config to document.

## Current State

None of the items below are built. This is a brainstorm/backlog, not a status report.

## Ideas

### Home Automation

- [ ] Home Assistant, previously flagged as future/planned scope for the `mitm` role — still nothing on disk or in `ThornixOS` today. Worth deciding whether it runs on `mitm` or its own new host (`proxmox-mitm` is no longer an option — removed from the repo).
- [ ] BLE integration specifically was the originally-floated angle (presence detection, sensors) — worth deciding what hardware this would actually integrate before building the NixOS side.

### Remote Access

- [ ] `05 Network/WireGuard` and `05 Network/Tailscale` are both still tracked as coverage gaps in [[08 Improvements/Vault Cleanup|Vault Cleanup]] — decide whether either is actually in use and document whichever wins. Note: an older pass of this vault referenced a committed OpenVPN profile (`pfproxmox.ovpn`) from the pre-rewrite `nix-config` layout; that path doesn't exist in the current `ThornixOS` repo, so confirm whether OpenVPN is still the intended approach at all before assuming it carries forward.

### Backup and Disaster Recovery

- [ ] No backup/DR strategy is documented anywhere for the fleet, despite there now being real production state to lose: `websites` (GuildedThorn.com + gallery/radio state), [[03 Devices/TrueNAS|TrueNAS]] (media + presumably other data), sops-managed secrets, and the `ThornixOS` repo itself (already git-backed, lower risk).
- [ ] TrueNAS is the obvious backup target for the rest of the fleet given it already exists — worth deciding what snapshots/replication it's actually configured to do today versus what's aspirational.

### Alerting

- [ ] Grafana exists (disabled) but there's no alerting pipeline anywhere — once the [[09 Observability/SIEM and SOC - Planned Architecture|SIEM/SOC]] or general observability work moves forward, decide on a notification target (email, [[07 Projects/ThornBot/ThornBot - Overview|ThornBot]] via Discord, something else). This is the same open question already flagged in the SIEM rollout tracker.

### SearXNG

- [ ] Reconcile the discrepancy flagged in [[04 Software/Glance|Glance]] — it's monitored as if live but currently `enable = false` on `mitm`.

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[08 Improvements/Ideas Backlog|Ideas Backlog]]
- [[08 Improvements/NixOS Improvements|NixOS Improvements]]
- [[03 Devices/TrueNAS|TrueNAS]]
