---
summary: hashcat & john — offline cracking modes, rules, *2john extractors, mask attacks.
status: active
tags: [security, tools, cracking, passwords]
private: false
---

# hashcat & john

Offline hash cracking. hashcat = GPU speed + attack modes; john = great `*2john` extractors and auto-detection.

## Identify first

```bash
hashid '<hash>'          # or name-that-hash / hash-identifier
```

## hashcat

```bash
hashcat -m <mode> -a <attack> hashes.txt <wordlist|mask> [-r rule]
```

- Attack modes `-a`: `0` straight (wordlist) · `3` mask (brute) · `6` wordlist+mask · `1` combinator.
- Common `-m`: `0` MD5 · `100` SHA1 · `1400` SHA256 · `1800` sha512crypt `$6$` · `500` md5crypt `$1$` · `3200` bcrypt `$2*$` · `1000` NTLM · `5600` NetNTLMv2 · `13100` Kerberoast · `18200` AS-REP · `22000` WPA.
- Rules: `-r /usr/share/hashcat/rules/best64.rule` (or `rockyou-30000.rule`, `dive.rule`).
- Mask: `?l?l?l?l?d?d` (lower×4 + digit×2); charsets `?l ?u ?d ?s ?a`.
- `--show` print cracked · `--username` hashes have `user:hash` · `-O` optimized · `-w 3` workload.

## john

```bash
john --wordlist=rockyou.txt --rules=Jumbo hash
john --format=<fmt> hash
john --show hash
# extractors -> crackable hash file:
ssh2john id_rsa > h; zip2john f.zip > h; keepass2john db.kdbx > h
unshadow /etc/passwd /etc/shadow > h        # combine for cracking
```

## Related

- [hashcat tool index](kb://11-security-tools-tools-index)
- [Password Attacks & Hash Cracking](kb://11-security-playbook-password-attacks)
