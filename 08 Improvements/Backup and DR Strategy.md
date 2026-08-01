---
summary: "Fleet backup and disaster-recovery posture: observability data is backed up, application state isn't, and the NAS is both primary storage and the only target."
status: in-progress
tags: [improvements, backup, disaster-recovery]
private: false
---

## Purpose

Capture what fleet state is actually protected today, what is exposed, and the open decisions for a real backup/DR strategy. Graduated out of the [[08 Improvements/Homelab Roadmap|Homelab Roadmap]] brainstorm now that there is production state to lose.

## Current State

### Protected today

- **Infrastructure config** — the entire fleet is reproducible from the `ThornixOS` git repo (host modules, `disko.nix`, service definitions), pushed to GitHub as the offsite copy. Rebuilds land via `comin` GitOps — see [[02 Systems/NixOS - Rebuild and Host Selection|Rebuild and Host Selection]]. Lowest-risk layer.
- **Secrets** — sops-encrypted ciphertext is committed per-host in the `ThornixOS` repo, so it rides the same GitHub offsite copy. The admin's YubiKey-backed GPG key is a permanent co-recipient on every file, so a host loss is never a lockout; `restic_password` is additionally held in a password manager. Host private keys are intentionally never backed up (regenerated on reinstall, then `sops updatekeys`). See [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]].
- **Prometheus TSDB** (`soc`) — 90 days retained on the VM disk plus a **daily `restic` backup** to a `prometheus-backup` bucket on the NAS, retention 7 daily / 4 weekly / 3 monthly. See [[02 Systems/NixOS - Host soc|Host soc]].
- **Loki logs** (`soc`) — written directly to a SeaweedFS S3 bucket on the NAS; durable only as far as the NAS is.

### Production state with no documented backup

- **GuildedThorn.com application data** on `websites` — the biggest hole:
  - **MongoDB** (accounts, guestbook, gallery metadata) — the connection is injected via the `guildedthorn_env` sops blob; where Mongo actually runs and whether it is dumped anywhere is **undocumented**. Resolve this first. *Lead (2026-08-01): a MongoDB app runs on the NAS with ~1.24G of data (`platter/ix-apps/app_mounts/mongodb`) — likely this instance; confirm against the `guildedthorn_env` connection string. See [[03 Devices/TrueNAS|TrueNAS]].*
  - **Gallery / upload `StateDirectory`** — the `services.guildedthorn` systemd `DynamicUser` persistent state (actual uploaded files) — no snapshot or copy documented.
  - **Owncast** state on `websites` (stream config, any recordings) — not captured.
  - RabbitMQ (guestbook publisher) is transient queue state — low value, no backup needed.
- **TrueNAS media** (CIFS `//…/media`, 447G) — primary copy only; confirmed 2026-08-01: **no snapshots, no snapshot tasks, no replication** on the NAS ([[12 Datasets/TrueNAS Storage Capture 2026-08-01|capture]]). Same applies to the 53.6G `malware` dataset and all app data (Gitea, MongoDB, SeaweedFS — the Loki bucket's durability floor).

### Single points of failure

- **The NAS is both primary storage and the only backup target.** Media lives on it, and the Prometheus `restic` repo + Loki logs back up *onto* it. If the NAS is lost, the media and every observability history and the restic repo are lost together — the backups share a failure domain with the primary. This is the core DR weakness.
- **No offsite for anything except the git-backed config/secrets.** The 3-2-1 rule (3 copies, 2 media, 1 offsite) is met only for `ThornixOS`.
- **No tested restore.** Nothing above has a documented restore drill; a `restic` repo whose password is only in a password manager is only as good as that recovery path.
- **Proxmox VM-level backup** (`vzdump` of `websites` / `soc` / guests) is not documented — ties to the deferred Proxmox management gap ([[08 Improvements/Homelab Roadmap|Homelab Roadmap]]).
- **pfSense config** backup/restore is still on that device's "to add" list — see [[03 Devices/pfSense Router|pfSense Router]].

## Target Strategy (to decide)

Not built — decisions to make, not current state:

- Pick a **second failure domain** so backups don't sit only on the NAS: either an offsite `restic`/`rsync.net`/Backblaze B2 target, or NAS ZFS replication (`syncoid`/`zrepl`) to a separate box.
- Decide whether the NAS should run **ZFS snapshot tasks** on the media/backup datasets — captured 2026-08-01: it currently runs **none** (no periodic snapshot tasks, no replication; the only scrub task is `platter` on Sundays 00:00 with a 35-day threshold). See [[03 Devices/TrueNAS|TrueNAS]] → Storage.
- Add a **MongoDB dump** (`mongodump`) job for GuildedThorn.com and a copy of the gallery `StateDirectory`, targeting the same offsite repo as Prometheus.
- Adopt **Proxmox `vzdump`** for the VMs, or accept config-only reproducibility and document that the app data path above is the sole thing needing separate backup.
- Verify the **restore path** for the existing `restic` Prometheus repo end-to-end at least once.

## Tasks

- [ ] Determine where GuildedThorn.com's MongoDB runs and whether it is backed up anywhere today
- [ ] Add a `mongodump` + gallery `StateDirectory` backup for `websites` to an offsite target
- [ ] Break the NAS-as-sole-target SPOF: choose offsite (restic/B2/rsync.net) or NAS→second-box ZFS replication
- [x] Capture the NAS's actual dataset / snapshot / scrub config (fills the [[03 Devices/TrueNAS|TrueNAS]] stub) — done 2026-08-01, evidence in [[12 Datasets/TrueNAS Storage Capture 2026-08-01|TrueNAS Storage Capture 2026-08-01]]: no snapshot tasks, no replication, scrub only on `platter` (Sun 00:00, 35-day threshold)
- [ ] Do one end-to-end restore test of the `restic` Prometheus repo and record the procedure
- [ ] Decide on Proxmox `vzdump` for `websites` / `soc` or document config-only DR explicitly
- [ ] Document pfSense config backup (AutoConfigBackup or scheduled XML export)

## Related

- [[08 Improvements/Homelab Roadmap|Homelab Roadmap]]
- [[08 Improvements/Improvements Tracker|Improvements Tracker]]
- [[02 Systems/NixOS - Host soc|Host soc]]
- [[02 Systems/NixOS - Host websites|Host websites]]
- [[02 Systems/NixOS - Secrets Strategy|Secrets Strategy]]
- [[03 Devices/TrueNAS|TrueNAS]]
- [[GuildedThorn.com - Deployment|GuildedThorn.com - Deployment]]
- [[06 Reference/engineering/databases-storage/backup-restore-and-pitr|Backup, Restore, and PITR]]
