---
title: "HTB: Bedsides — Campaign Index"
tags: [htb, pentest, rooted]
target: 10.129.66.223
status: rooted
started: 2026-07-23
completed: 2026-07-23
---

# HTB: Bedsides — 10.129.66.223 — ✅ ROOTED

Step-by-step log of an authorized Hack The Box engagement. Each step gets its own note, tagged:

- 🟢 **could go somewhere** — a live lead worth pushing on
- 🐇 **rabbit hole** — interesting but likely a distraction
- 🔴 **dead end** — confirmed no path here

## 🏁 Flags

- **User** (`developer`): `663aa6b35552c31ddba418f84dba7249`
- **Root**: `2d5540b9ce670f389a5e5759c2ef114f`

## Steps

1. [[htb-bedsides-01-nmap]] — full TCP scan: 22/80 open, 3000 filtered — 🟢
2. [[htb-bedsides-02-web-80]] — vhost discovery on :80 — 🟢
3. [[htb-bedsides-03-fuzzing]] — dir/vhost fuzzing — 🟢
4. [[htb-bedsides-04-research-vhost]] — `research.bedside.htb` upload portal, `X-Powered-By: pdfminer.six` — 🟢 HOT
5. [[htb-bedsides-05-upload-probe]] — uploads land at `/uploads/<name>`, served back by name — 🟢
6. [[htb-bedsides-06-zip-symlink]] — zip symlink read primitive — 🔴 (no sync extraction)
7. [[htb-bedsides-07-conversion]] — filename traversal + conversion probing — 🔴 (no observable output)
8. [[htb-bedsides-08-pdfminer-cve]] — foothold vuln = **CVE-2025-64512** pdfminer pickle RCE — 🟢 THE PATH
9. [[htb-bedsides-09-exploit-build]] — weaponised `shell.pickle.gz` + `trigger.pdf` — ✅ shell as `datawrangler@data-wrangler` (container)
10. [[htb-bedsides-10-root]] — root via **:3000 esm.sh/x LFI → developer SSH key → shared `/datastore` + MONAI torch pickle RCE** — ✅ root

## The full kill chain

1. **Foothold** — `research.bedside.htb` runs pdfminer.six (CVE-2025-64512). Upload `shell.pickle.gz` (`.gz` accepted despite the notice), then a `trigger.pdf` whose Type0 font `/Encoding` name decodes to the pickle's absolute path. pdfminer unpickles it → reverse shell as **`datawrangler`** inside the `data-wrangler` container (host networking).
2. **Pivot** — the parked **:3000** (filtered externally) is now reachable on `127.0.0.1`. It's an **esm.sh/x dev server** ("Bedside Clinic - Image Viewer") vulnerable to **path traversal / arbitrary file read** (`curl --path-as-is 'http://127.0.0.1:3000/../../../../../../etc/passwd'`).
3. **User** — LFI-read `/home/developer/.ssh/id_rsa` (ed25519, comment `developer@bedside`) and `user.txt`. `ssh -i` in as **developer** on the host `bedside`.
4. **Root** — `sudo -l`: `(ALL) NOPASSWD: /usr/bin/python3 /opt/trainer/bedside_trainer.py` (no wildcard). The trainer auto-resumes from the newest `*.pt` in `/datastore/checkpoints` via MONAI `CheckpointLoader` → **`torch.load(..., weights_only=False)`**. `/datastore` is a volume **shared with the container** and owned by `datawrangler` (us). From the container we drop a malicious `.pt` (pickle `__reduce__` → `os.system`) + one valid `.png` (so the trainer reaches the load), then run the sudo hook as developer → **code exec as root**.

## Loot / creds

- Attacker tun0: **10.10.14.136**.
- Foothold user: **`datawrangler`** (uid 988, gid 1001 `dataops`) in container `data-wrangler`; host networking.
- Host user: **`developer`** (uid 1000) — ed25519 private key at `/home/developer/.ssh/id_rsa` (recovered via :3000 LFI). Key saved on attacker as `~/htb/bedsides/dev_key`.
- Shared volume: **`/datastore`** (`drwxrwx--- datawrangler dataops`) — the bridge between container and host trainer.
- Root: SUID `/bin/bash` dropped (`bash -p` → euid 0). Root flag also copied to `/datastore/checkpoints/root_flag.txt`.

## Notes for cleanup / report

- Two chained insecure-deserialization bugs (pdfminer pickle → torch pickle) plus an LFI, bridged by a shared Docker volume and host networking.
- Vuln line confirmed in traceback: `monai/handlers/checkpoint_loader.py:125` → `torch.load(self.load_path, map_location=..., weights_only=False)`.
