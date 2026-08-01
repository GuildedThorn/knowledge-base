---
summary: "Raw capture of the TrueNAS box's pool / dataset / snapshot / scrub / replication state, taken 2026-08-01 over SSH. Evidence behind the TrueNAS device note's Storage section."
status: active
tags: [datasets, devices, evidence]
---

## Purpose

Raw command output captured from `truenas.guildedthorn.arpa` (172.16.25.4) on 2026-08-01, run as `thorn` over SSH. This is the evidence behind the `## Storage` section of [[03 Devices/TrueNAS|TrueNAS]] and closes the "capture the NAS's actual dataset / snapshot / scrub config" task in [[08 Improvements/Backup and DR Strategy|Backup and DR Strategy]]. Read-only session — nothing on the NAS was changed.

## Headline findings

- **No periodic snapshot tasks exist** (`pool.snapshottask.query` → `[]`). The only snapshots on the system are app-rollback snapshots (gitea, seaweedfs) and boot-environment `@pristine` markers. `platter/media`, `platter/malware`, `platter/files`, `platter/certs` have zero snapshots.
- **No replication** (`replication.query` → `[]`).
- **One scrub task**: pool `platter`, Sundays 00:00, 35-day threshold, enabled — so it effectively scrubs about every 5 weeks. Last platter scrub: Sun Jul 12 2026, 0B repaired. The boot-pool scrub (last: Sun Jul 26 2026) is driven by the separate boot-pool scrub interval, not a `pool.scrub` task.
- **Running version is 25.10.4** (`/etc/version`), with the previous `25.04.2.3` boot environment retained. The `@pristine` snapshots date the upgrade to ~Jul 13 2026.
- **MongoDB, Gitea, Jellyfin, and SeaweedFS run as TrueNAS apps** (`platter/ix-apps/app_mounts/*`).

## Pools

```
% zpool list -o name,size,alloc,free,health
NAME        SIZE  ALLOC   FREE    HEALTH
boot-pool   111G  12.2G  98.8G    ONLINE
platter    7.25T   540G  6.72T    ONLINE
```

## Scrub history

`zpool status` scan lines (pools in alphabetical order: boot-pool, then platter):

```
% zpool status | grep -A2 scan
  scan: scrub repaired 0B in 00:00:29 with 0 errors on Sun Jul 26 03:45:30 2026   <- boot-pool
--
  scan: scrub repaired 0B in 00:18:22 with 0 errors on Sun Jul 12 00:18:23 2026   <- platter
```

The platter scrub started at 00:00 on a Sunday, matching the scheduled task below.

## Datasets

```
% zfs list -o name,used,avail,mountpoint,com.sun:auto-snapshot -r
NAME                                                       USED  AVAIL  MOUNTPOINT                                      COM.SUN:AUTO-SNAPSHOT
boot-pool                                                 12.2G  95.4G  none                                            -
boot-pool/ROOT                                            12.1G  95.4G  none                                            -
boot-pool/ROOT/25.04.2.3                                  8.88G  95.4G  legacy                                          -
boot-pool/ROOT/25.10.4                                    3.27G  95.4G  legacy                                          -
boot-pool/grub                                            9.06M  95.4G  legacy                                          -
platter                                                    540G  6.60T  /mnt/platter                                    -
platter/.system                                           2.16G  6.60T  legacy                                          -
platter/certs                                               96K  6.60T  /mnt/platter/certs                              -
platter/files                                               96K  6.60T  /mnt/platter/files                              -
platter/ix-apps                                           16.8G  6.60T  /mnt/.ix-apps                                   -
platter/ix-apps/app_configs                               8.30M  6.60T  /mnt/.ix-apps/app_configs                       -
platter/ix-apps/app_mounts                                3.51G  6.60T  /mnt/.ix-apps/app_mounts                        -
platter/ix-apps/app_mounts/gitea                          20.1M  6.60T  /mnt/.ix-apps/app_mounts/gitea                  -
platter/ix-apps/app_mounts/gitea/config                    100K  6.60T  /mnt/.ix-apps/app_mounts/gitea/config           -
platter/ix-apps/app_mounts/gitea/data                      912K  6.60T  /mnt/.ix-apps/app_mounts/gitea/data             -
platter/ix-apps/app_mounts/gitea/postgres_data            19.0M  6.60T  /mnt/.ix-apps/app_mounts/gitea/postgres_data    -
platter/ix-apps/app_mounts/jellyfin                        377M  6.60T  /mnt/.ix-apps/app_mounts/jellyfin               -
platter/ix-apps/app_mounts/jellyfin/cache                 93.5M  6.60T  /mnt/.ix-apps/app_mounts/jellyfin/cache         -
platter/ix-apps/app_mounts/jellyfin/config                 283M  6.60T  /mnt/.ix-apps/app_mounts/jellyfin/config        -
platter/ix-apps/app_mounts/mongodb                        1.25G  6.60T  /mnt/.ix-apps/app_mounts/mongodb                -
platter/ix-apps/app_mounts/mongodb/data                   1.24G  6.60T  /mnt/.ix-apps/app_mounts/mongodb/data           -
platter/ix-apps/app_mounts/seaweedfs                      1.88G  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs              -
platter/ix-apps/app_mounts/seaweedfs/admin-data           6.84M  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs/admin-data   -
platter/ix-apps/app_mounts/seaweedfs/filer-data           3.62M  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs/filer-data   -
platter/ix-apps/app_mounts/seaweedfs/master-data           208K  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs/master-data  -
platter/ix-apps/app_mounts/seaweedfs/volume-data          1.87G  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs/volume-data  -
platter/ix-apps/app_mounts/seaweedfs/worker-data            96K  6.60T  /mnt/.ix-apps/app_mounts/seaweedfs/worker-data  -
platter/ix-apps/docker                                    13.0G  6.60T  /mnt/.ix-apps/docker                            -
platter/ix-apps/truenas_catalog                            362M  6.60T  /mnt/.ix-apps/truenas_catalog                   -
platter/malware                                           53.6G  6.60T  /mnt/platter/malware                            -
platter/media                                              447G  6.60T  /mnt/platter/media                              -
```

(Boot-environment sub-datasets under `boot-pool/ROOT/25.04.2.3/*` and `boot-pool/ROOT/25.10.4/*` — the usual `/etc`, `/usr`, `/var`, … split — and `platter/.system/*` service datasets omitted here for brevity; nothing in them is snapshot- or backup-relevant beyond what's summarized. `com.sun:auto-snapshot` is unset (`-`) on every dataset.)

## Snapshots (newest 20)

```
% zfs list -t snapshot -o name,creation -s creation | tail -20
boot-pool/ROOT/25.10.4/etc@pristine                         Mon Jul 13  0:57 2026
boot-pool/ROOT/25.10.4/opt@pristine                         Mon Jul 13  0:57 2026
boot-pool/ROOT/25.10.4@pristine                             Mon Jul 13  0:57 2026
boot-pool/ROOT/25.10.4/usr@pristine                         Mon Jul 13  0:57 2026
boot-pool/ROOT/25.10.4/var@pristine                         Mon Jul 13  0:57 2026
boot-pool/ROOT/25.10.4/var/lib@pristine                     Mon Jul 13  0:57 2026
platter/ix-apps/app_mounts/gitea@1.6.19                     Mon Jul 13  1:01 2026
platter/ix-apps/app_mounts/gitea/config@1.6.19              Mon Jul 13  1:01 2026
platter/ix-apps/app_mounts/gitea/data@1.6.19                Mon Jul 13  1:01 2026
platter/ix-apps/app_mounts/gitea/postgres_data@1.6.19       Mon Jul 13  1:01 2026
platter/ix-apps/app_mounts/seaweedfs@1.2.29                 Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/seaweedfs/admin-data@1.2.29      Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/seaweedfs/filer-data@1.2.29      Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/seaweedfs/master-data@1.2.29     Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/seaweedfs/volume-data@1.2.29     Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/seaweedfs/worker-data@1.2.29     Tue Jul 14 23:30 2026
platter/ix-apps/app_mounts/gitea@1.6.21                     Sat Jul 18 11:53 2026
platter/ix-apps/app_mounts/gitea/config@1.6.21              Sat Jul 18 11:53 2026
platter/ix-apps/app_mounts/gitea/data@1.6.21                Sat Jul 18 11:53 2026
platter/ix-apps/app_mounts/gitea/postgres_data@1.6.21       Sat Jul 18 11:53 2026
```

All snapshots on the system are app-upgrade rollback points or boot-environment `@pristine` markers — none are periodic, none cover user data.

## Scheduled tasks and replication (middleware queries)

```
% midclt call pool.snapshottask.query
[]

% midclt call pool.scrub.query | python3 -m json.tool
[
    {
        "pool": 1,
        "threshold": 35,
        "description": "",
        "schedule": {
            "minute": "00",
            "hour": "00",
            "dom": "*",
            "month": "*",
            "dow": "7"
        },
        "enabled": true,
        "id": 1,
        "pool_name": "platter"
    }
]

% midclt call replication.query
[]
```

## Version

```
% cat /etc/version
25.10.4
```

## Related

- [[03 Devices/TrueNAS|TrueNAS]]
- [[08 Improvements/Backup and DR Strategy|Backup and DR Strategy]]
- [[01 Maps/Datasets Map|Datasets Map]]
