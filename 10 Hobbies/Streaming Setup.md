## Purpose

Tie together the streaming-related pieces that already exist on both the infrastructure and client side.

## Current State (Real)

- **Server side**: the `websites` NixOS host runs Owncast (`services.owncast`, port 8090, RTMP 1935) for the live stream, and [[GuildedThorn.com - Overview|GuildedThorn.com]] has a dedicated `/stream` page (Twitch embed) plus a `StreamScheduleController`/`StreamEvent` model for schedule data.
- **Client/desktop side**: `obs` is enabled via the `services-obs` module on `nixos` (PipeWire capture, background-removal plugin, `v4l2loopback`) — the actual broadcast-encoding side.
- **Consumption side**: the [[04 Software/Glance|Glance]] dashboard follows Twitch streamer `s1ren_official` and a `twitch-top-games` widget, suggesting an interest in the wider Twitch ecosystem beyond just running the site's own stream.

## Open Questions

- Is the site's `/stream` page pointing at a Twitch channel, the self-hosted Owncast instance, or both depending on context?
- Has an actual stream gone out yet on the self-hosted Owncast path, or is that infrastructure built but not yet used in anger?
- Any interest in formalizing a stream schedule (the `StreamScheduleController` exists — is it populated with real data)?

## Related

- [[GuildedThorn.com - Overview|GuildedThorn.com]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
- [[02 Systems/NixOS - Host websites|Host websites]]
- [[04 Software/Glance|Glance]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
