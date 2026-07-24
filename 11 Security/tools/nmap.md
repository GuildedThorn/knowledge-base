---
summary: nmap reference — scan types, timing, service/version detection, NSE scripting.
status: active
tags: [security, tools, nmap, recon]
private: false
---

# nmap

Port and service discovery. Two-pass workflow: find open ports fast, then deep-scan only those.

## Core flags

- `-p-` all 65535 TCP · `-p 22,80` specific · `--top-ports 100`
- `-sS` SYN (default as root) · `-sT` connect (through proxychains) · `-sU` UDP · `-sn` ping sweep
- `-sV` version detection · `-sC` default NSE scripts · `-A` aggressive (`-sC -sV -O --traceroute`)
- `-O` OS detect · `-Pn` skip host discovery (host "down" but is up) · `-n` no DNS
- `-T4` timing · `--min-rate 5000` force pace · `-oA base` all output formats

## Two-pass workflow

```bash
nmap -p- --min-rate 5000 -T4 -Pn -oN ports.txt $IP
nmap -p 22,80,3000 -sCV -oN deep.txt $IP
nmap -sU --top-ports 50 -oN udp.txt $IP
```

## NSE scripting

```bash
nmap --script vuln $IP                     # known-vuln checks
nmap --script "smb-enum-*" -p445 $IP
nmap --script http-enum,http-title -p80 $IP
ls /usr/share/nmap/scripts/ | grep <svc>   # discover scripts
```

## Through a pivot

`-sT -Pn` only (no raw sockets over proxychains): `proxychains nmap -sT -Pn -p 445,3389 10.10.20.5`.

## Related

- [nmap tool index](kb://11-security-tools-tools-index)
- [Recon & Enumeration](kb://11-security-playbook-recon-enumeration)
