---
summary: Recon & enumeration cheat sheet — nmap sweeps, service enum, vhost/directory fuzzing.
status: active
tags: [security, playbook, recon, enumeration]
private: false
---

# Recon & Enumeration

First contact. Map ports → services → versions, then enumerate each service until something gives.

## Port scanning (nmap)

```bash
# fast full-TCP sweep, then targeted deep scan of what's open
nmap -p- --min-rate 5000 -T4 -oN ports.txt $IP
nmap -p 22,80,3000 -sCV -oN deep.txt $IP        # -sC scripts, -sV versions
nmap -sU --top-ports 50 -oN udp.txt $IP         # UDP (slow; 53,161,69,123)
```

- `filtered` ≠ closed — note it and revisit after a foothold (often reachable on `127.0.0.1` later; see the Bedsides :3000 pivot).
- Grep versions straight into CVE lookups (`searchsploit`, [crossview](kb://hub-11-security)).

## Web enum (the usual first target)

```bash
whatweb -a3 http://$IP                     # stack fingerprint
curl -sI http://$IP                        # headers: Server, X-Powered-By
gobuster dir -u http://$IP -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,txt,html
feroxbuster -u http://$IP --scan-limit 4   # recursive alt
```

### Virtual host / subdomain fuzzing

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
     -H "Host: FUZZ.$DOMAIN" -u http://$IP -fs <baseline-size>
```

Add discovered vhosts to `/etc/hosts`. This is exactly how `research.bedside.htb` surfaced.

## Service enum quick refs

- **SMB (445)**: `enum4linux-ng -A $IP`, `smbclient -L //$IP -N`, `nxc smb $IP -u '' -p ''`
- **FTP (21)**: try `anonymous:anonymous`, `ls -la`, check for writable dirs
- **DNS (53)**: `dig axfr @$IP $DOMAIN` (zone transfer)
- **SNMP (161)**: `snmpwalk -v2c -c public $IP`
- **NFS (2049)**: `showmount -e $IP`
- **RPC/LDAP (135/389)**: `rpcclient -U '' -N $IP`, `ldapsearch -x -H ldap://$IP -s base`

## Wordlists (SecLists)

- dirs: `raft-*-directories.txt`, `directory-list-2.3-medium.txt`
- vhosts: `subdomains-top1million-*.txt`
- creds: `rockyou.txt`, `xato-net-10-million-usernames.txt`

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Web Application Testing](kb://11-security-playbook-web-app-testing)
- [Password Attacks & Hash Cracking](kb://11-security-playbook-password-attacks)
