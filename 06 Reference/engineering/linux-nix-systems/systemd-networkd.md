---
summary: "The systemd network configuration daemon that manages links, addresses, and routes from declarative .network files."
status: active
tags: [reference, engineering, linux, networkd, networking, systemd]
private: false
---

# systemd-networkd

## Purpose

The systemd network configuration daemon that manages links, addresses, and routes from declarative .network files.

## How It Works

- `systemd-networkd` is a system service that detects and configures network devices as they appear, reacting to link state through the kernel and rtnetlink.
- Configuration lives in `.network`, `.netdev`, and `.link` files under `/etc/systemd/network`, `/run/systemd/network`, and `/usr/lib/systemd/network`, applied in lexical order by filename.
- `.network` files match interfaces via a `[Match]` section (by name, MAC, driver, type) and set addressing, routes, and DNS in `[Network]`, `[Address]`, and `[Route]` sections.
- `.netdev` files create virtual devices (bridges, bonds, VLANs, tunnels, VXLAN, WireGuard); `.link` files configure low-level link properties and naming.
- The companion `systemd-resolved` and `systemd-networkd-wait-online` services handle name resolution and boot-time link readiness.

## Engineering Notes

- Static addressing uses `Address=` and `Gateway=`; DHCP is enabled with `DHCP=yes|ipv4|ipv6` in the `[Network]` section.
- Bridging attaches members by setting `Bridge=<name>` in each member's `.network` file, while the bridge itself is declared as a `.netdev`.
- Bonding works the same way via `Bond=`, with mode and options set in the bond `.netdev`.
- `networkctl status` and `networkctl list` inspect runtime state; `networkctl reload` re-reads configuration without restart.

## Sources

- systemd docs - systemd.network(5) - https://www.freedesktop.org/software/systemd/man/latest/systemd.network.html
- systemd docs - systemd-networkd.service(8) - https://www.freedesktop.org/software/systemd/man/latest/systemd-networkd.service.html

---
## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
---
