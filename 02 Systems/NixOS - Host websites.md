## Purpose

Document the `websites` host, composed in `modules/computers/websites.nix` — the production home of [[GuildedThorn.com - Overview|GuildedThorn.com]].

## Role

Proxmox VM that serves the live GuildedThorn.com site plus its live-stream and guestbook infrastructure.

## Composition

- `thorn-core` base bundle
- service modules: ClamAV, SSH
- `inputs.guildedthorn-com.nixosModules.default` — the site's own NixOS module, entering the flake as a dedicated input rather than being hand-written here
- `qemu-guest.nix` profile (Proxmox VM)
- `hosts/websites/hardware-configuration.nix`, `disko.nix`, `networking.nix`, `secrets.nix` (one of only two hosts with sops secrets — see [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]])

## Notable Host Behavior

- `services.guildedthorn` runs the site on port 8080, reading its environment from a sops-managed secrets file.
- `services.owncast` runs the live stream (port 8090, RTMP 1935), bound to loopback.
- `services.rabbitmq` runs locally for the guestbook publisher; `epmd` is pinned to listen on `127.0.0.1` only since IPv6 is disabled on this host.
- A `cloudflared` systemd unit runs the Cloudflare Tunnel outbound-only — only SSH is exposed on the public interface; the firewall additionally opens the Owncast/RTMP ports to RFC1918 ranges only (not the public internet).
- BIOS boot via GRUB (forced to a single device to avoid a disko/GRUB duplicate-entry assert), predictable interface naming disabled so the NIC stays `eth0`.
- Static networking: private IP off `172.16.25.0/24`, with a local `/etc/hosts`-style override so the internal `.arpa` name for the TrueNAS host resolves without depending on internal DNS (needed for S3-endpoint TLS to match its cert).

## Deploying Updates

Shipping a new site build is a `flake.lock` bump for the `guildedthorn-com` input, not a change to this host's own config — see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]].

## Related

- [[01 Maps/NixOS Map|NixOS Map]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
