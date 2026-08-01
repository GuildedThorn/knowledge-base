---
summary: Evidence-backed Pulse execution log for vr-brain.
status: active
tags: [projects, ephemeris, pulse]
---

# vr-brain - Pulse Log

## 2026-08-01 01:58 — Capture the NAS's actual dataset / snapshot / scrub config (fills the [[03 Devices/TrueNAS|TrueNAS]] stub)

- **Outcome:** Completed
- **Focus:** 18 minutes (Medium energy, Balanced mode)
- **Objective:** Capture the NAS's actual dataset / snapshot / scrub config (fills the [[03 Devices/TrueNAS|TrueNAS]] stub)
- **Summary:** What the capture found:
- No periodic snapshot tasks exist (pool.snapshottask.query → []) and no replication — the only snapshots anywhere are app-rollback points (gitea, seaweedfs) and boot-environment @pristine markers. The 447G media and 53.6G malware datasets have zero point-in-time protection.
- One scrub task: platter, Sundays 00:00 with a 35-day threshold — so it really scrubs ~every 5 weeks (last: Jul 12, clean). Boot-pool scrubs separately (last: Jul 26, clean).
- The NAS is running 25.10.4, not 25.04.2.3 — the device note's "upgrade in progress" guess was stale; the @pristine snapshots date the upgrade to ~Jul 13.
- Bonus lead: MongoDB runs as a TrueNAS app with 1.24G of data — likely the "where does GuildedThorn.com's Mongo actually run" unknown from the DR doc (task 50 stays open until you confirm the connection string), and relevant to Tuesday's MongoDB-probing SIEM alert.

Files: raw evidence in 12 Datasets/TrueNAS Storage Capture 2026-08-01.md; new ## Storage section + corrected OS line + apps list in 03 Devices/TrueNAS.md; DR strategy got its checkbox checked, the "currently unknown" resolved, and the media/Mongo bullets updated with evidence; both indexes updated.
- **Session:** `ephemeris://pulse/sessions/96bba992a78840798aab73bfe6bcb10e`

### Flight recorder

- **Progress · 01:57:** Wrote evidence to 12 Datasets/TrueNAS Storage Capture 2026-08-01.md;
- **Evidence · 01:57:** NAS is running 25.10.4, not 25.04.2.3 — the device note's "upgrade in progress" guess was stale
- **Progress · 01:58:** What the capture found:
- No periodic snapshot tasks exist (pool.snapshottask.query → []) and no replication — the only snapshots anywhere are app-rollback points (gitea, seaweedfs) and boot-environment @pristine markers. The 447G media and 53.6G malware datasets have zero point-in-time protection.
- One scrub task: platter, Sundays 00:00 with a 35-day threshold — so it really scrubs ~every 5 weeks (last: Jul 12, clean). Boot-pool scrubs separately (last: Jul 26, clean).
- The NAS is running 25.10.4, not 25.04.2.3 — the device note's "upgrade in progress" guess was stale; the @pristine snapshots date the upgrade to ~Jul 13.
- Bonus lead: MongoDB runs as a TrueNAS app with 1.24G of data — likely the "where does GuildedThorn.com's Mongo actually run" unknown from the DR doc (task 50 stays open until you confirm the connection string), and relevant to Tuesday's MongoDB-probing SIEM alert.

Files: raw evidence in 12 Datasets/TrueNAS Storage Capture 2026-08-01.md; new ## Storage section + corrected OS line + apps list in 03 Devices/TrueNAS.md; DR strategy got its checkbox checked, the "currently unknown" resolved, and the media/Mongo bullets updated with evidence; both indexes updated.
