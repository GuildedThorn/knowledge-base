---
summary: "Document the `firewall` host, composed in `modules/computers/firewall.nix`."
status: active
tags: [systems, host]
---

## Purpose

Document the `firewall` host, composed in `modules/computers/firewall.nix`.

## Role

Dedicated, minimal firewall box.

## Composition

- `thorn-core` base bundle only
- `hosts/firewall/hardware-configuration.nix`, `networking.nix`

## Notable Host Behavior

- NetworkManager disabled; DNS `1.1.1.1`.
- Firewall opens only TCP/UDP port 22 (SSH) — no other modules or services are layered on.

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[01 Maps/Network Map|Network Map]]
- [[05 Network/Firewall - pfSense|Firewall - pfSense]]
