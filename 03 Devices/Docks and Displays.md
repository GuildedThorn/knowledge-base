## Purpose

Document DisplayLink dock/monitor handling across the fleet.

## Current State

- `modules/services/displaylink.nix` (the `services-displaylink` module, enabled on [[02 Systems/NixOS - Host nixos|Host nixos]]) loads the `evdi` kernel module and runs a `displaylink-server` systemd service wrapping `DisplayLinkManager`, restarting on failure.
- The module has both a Wayland comment (referencing a Synaptics DisplayLink driver download URL as a `nix-prefetch-url` example) and a commented-out X11 fallback (`services.xserver.videoDrivers = [ "displaylink" "modesetting" ]`) — Wayland is the active path given `nixos` runs Hyprland.
- `nwg-displays` and `nwg-look` are installed on `nixos` alongside this, suggesting manual per-monitor layout management on top of DisplayLink rather than a fully declarative monitor config.

## Open Questions

- Which specific dock hardware is in use?
- How many external displays does this typically drive, and at what resolution/refresh rate?
- Any known DisplayLink reliability issues (reconnect-on-wake, driver version drift) worth recording?

## Related

- [[01 Maps/Devices Map|Devices Map]]
- [[02 Systems/NixOS - Host nixos|Host nixos]]
- [[02 Systems/NixOS - Shared Modules|Shared Modules]]
