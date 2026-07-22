## Purpose

A single brainstorm of things this vault will likely grow into, based on everything documented so far — a starting point to accept, reject, or reprioritize, not a commitment. Bigger items here should graduate to their own note (or their own Improvement tracker) once there's real work behind them; this note should stay a map of possibility, not accumulate stale detail itself.

## Why This Exists

The vault currently documents a lot of *built* things (GuildedThorn.com, SkyDestroyer, ThornixOS) reasonably well, but several real threads only show up as scattered installed packages or one-line mentions with no home. This is an attempt to name those threads out loud.

## Security

- [[09 Observability/SIEM and SOC - Planned Architecture|SIEM and SOC - Planned Architecture]] and its [[08 Improvements/SIEM-SOC Rollout|rollout tracker]]
- Track CTF platform activity (HackTheBox, TryHackMe, or similar) if that's of interest — a simple running log of boxes/challenges completed and techniques learned

## Infrastructure

- [[08 Improvements/Homelab Roadmap|Homelab Roadmap]] — Home Assistant, VPN, backup/DR, alerting, SearXNG
- A dedicated [[03 Devices/TrueNAS|TrueNAS]] deep-dive once its actual dataset/snapshot/replication config is known (this note is currently just what's inferable from other hosts referencing it)
- Formal documentation of the `proxmox` hypervisor's own guest inventory — right now individual guests (`websites`, `soc`, `proxmox-guest`) are documented from the `ThornixOS` side, but there's no single "what's actually running on this box" view from the Proxmox side itself

## Hobbies and Maker Work

- [[01 Maps/Hobbies Map|Hobbies Map]] and everything under it — most of these notes end in open questions (which printer, which headset, which vehicle) that only the person actually doing the hobby can answer
- A project-outcome log for 3D printing / Arduino work, once there's something concrete to log

## Software Coverage Gaps

Installed and clearly in active use, but with no config declared anywhere beyond the package reference — so no real note exists yet without inventing content:

- VS Code (already tracked in [[08 Improvements/Vault Cleanup|Vault Cleanup]])
- Syncthing (already tracked in [[08 Improvements/Vault Cleanup|Vault Cleanup]])
- Postman, MongoDB Compass, `wakatime-cli`, Anki (`anki-bin`), JetBrains Rider — all installed on one or more hosts, none documented; low priority individually, but worth a combined "Developer Tooling" note if they ever get real configuration behind them (dotfiles, Wakatime project tags, Anki deck subjects) rather than staying bare package references
- `Neomutt` — already flagged in [[04 Software/Matcha|Matcha]] as the second, parallel email stack with no note of its own yet

## Meta

- Consider whether `06 Reference/Codex Generation Standard` and `AGENT.md` need a line about this backlog's existence/lifecycle, so future passes know to prune graduated items rather than let this note grow without bound

## Related

- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[08 Improvements/Homelab Roadmap|Homelab Roadmap]]
- [[01 Maps/Hobbies Map|Hobbies Map]]
