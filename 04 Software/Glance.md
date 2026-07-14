## Purpose

Document the Glance dashboard setup, managed by `modules/users/thorn-glance.nix` in `ThornixOS`.

## Current State

- Enabled on `nixos` and `scout` (both import the `thorn-glance` module); listens on `0.0.0.0:8080`.
- Five pages configured: Home, Feeds, Videos, Gaming, Services.

## Pages

- **Home**: clock (12h), weather for Alsip (imperial units), a small stock-ticker widget (SPY/S&P 500, PTLO/Portillo's, NVDA/NVIDIA, all linking to TradingView charts), a DuckDuckGo search bar with custom bangs (`!yt` YouTube, `!steam` Steam store, `!amazon` Amazon, `!rd` Reddit, `!fa` FlightAware), and an r/selfhosted feed.
- **Feeds**: an RSS widget pulling Hacker News and The Verge.
- **Videos**: a YouTube channels widget (two channel IDs, not yet identified by name) and a Twitch-channels widget following `s1ren_official`.
- **Gaming**: Twitch top-games widget, a grouped r/pcgaming + r/games reddit feed, a grid-cards video widget following gameranx, Skill Up, GameLinked, and Digi, and an r/gamingnews feed.
- **Services**: a `monitor` widget tracking [[03 Devices/TrueNAS|TrueNAS]]'s Jellyfin instance (`https://truenas.guildedthorn.arpa:8920`), `pfsense.guildedthorn.arpa`, `truenas.guildedthorn.arpa` itself, and SearXNG (`https://mitm.guildedthorn.arpa/searxng/stats`) — plus a `repository` widget tracking PRs/issues/commits on `GuildedThorn/ThornixOS`.

## Open Discrepancy

The Services page monitors SearXNG as if it's live, but both [[02 Systems/NixOS - Host mitm|Host mitm]] and [[02 Systems/NixOS - Host proxmox-mitm|Host proxmox-mitm]] currently have `services.searx.enable = false`. Either this monitor entry is stale, or SearXNG was live at some point and got disabled without updating the dashboard — worth reconciling.

## Related

- [[01 Maps/Observability Map|Observability Map]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
- [[03 Devices/TrueNAS|TrueNAS]]
- [[02 Systems/NixOS - Host mitm|Host mitm]]
