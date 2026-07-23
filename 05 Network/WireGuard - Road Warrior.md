---
summary: "Document the WireGuard road-warrior setup that lets `scout` (the roaming ThinkPad) reach home from anywhere — declared in `hosts/scout/wireguard.nix`, with pfS…"
status: active
tags: [network]
---

## Purpose

Document the WireGuard road-warrior setup that lets `scout` (the roaming ThinkPad) reach home from anywhere — declared in `hosts/scout/wireguard.nix`, with pfSense as the server side.

## Current State

Two `wg-quick` interfaces share one identity (same keys and tunnel IP `10.10.10.3/32`, so pfSense sees a single peer either way), listening against endpoint port `4501` on the WAN:

- `wg0` — **full tunnel**: `AllowedIPs 0.0.0.0/0`, all traffic routed home. LAN access plus protection on hostile networks, and it carries the SOC telemetry (scout's `observability-roaming` module remote-writes metrics to `soc` over this).
- `wg1` — **split tunnel**: only home subnets routed (`10.10.10.0/24` + `172.16.25.0/24`). Deliberately *not* `192.168.1.0/24` — hotspots use that range constantly and a tunnel route for it would fight whatever local network scout is actually on.

Only one can be up at a time — the systemd units `Conflict`, so starting one stops the other. Shell aliases: `vpn-full`, `vpn-split`, `vpn-off`, `vpn-status`.

## Design Decisions

- **On demand, not auto-started** (`autostart = false`): scout is sometimes physically on the home LAN, where an always-up tunnel would try to reach the WAN IP from inside the network — a hairpin pfSense won't do. The handshake fails but the routes are already installed, black-holing traffic.
- **MTU pinned to 1280** instead of wg-quick's default 1420: cellular hotspots drop full-size encapsulated packets (PMTUD black hole — TLS handshakes stall while pings pass). 1280 is the always-works floor for a laptop roaming arbitrary networks.
- **DNS `10.10.10.1`** (pfSense over the tunnel) in both modes, so `.arpa` names resolve — at the cost of all DNS queries riding the tunnel even in split mode.
- Keys are sops secrets on scout (`wg_private_key`, `wg_preshared_key`) — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]].

## Related

- [[01 Maps/Network Map|Network Map]]
- [[02 Systems/NixOS - Host scout|Host scout]]
- [[03 Devices/pfSense Router|pfSense Router]]
- [[08 Improvements/SIEM-SOC Rollout|SIEM-SOC Rollout]]
