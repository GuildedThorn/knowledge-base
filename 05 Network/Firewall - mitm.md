## Purpose

Document firewall policy, interface separation, NAT behavior, VPN exposure, and validation steps for the ThornCloud pfSense edge router.

## Scope

This note applies to [[HP Mini PC]] at `mitm.guildedthorn.arpa`.

## Current Interface Inventory

- `LAN`: sits in internal network on [[pfSense Router]] at `172.16.25.2`

## Firewall Intent

- Blocks all traffic coming in `80` and `443` unless it is coming in from cloudflare proxy from this automated script [here](https://github.com/GuildedThorn/Automization/blob/main/scripts/Universal-Linux/Cloudflare-UFW.sh)
## Validation

When changing firewall or NAT behavior, verify:

- management access still works from the intended network
- internal DNS resolution still works

## Change Log Cues

Record these each time rules change:

- date of change
- interface affected
- reason for change
- expected user-visible effect
- rollback path

## Related

- [[01 Maps/Network Map|Network Map]]
