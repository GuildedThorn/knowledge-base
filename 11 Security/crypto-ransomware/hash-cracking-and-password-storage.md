---
summary: "Password security depends on slow, salted password hashing, strong user choices, MFA, and rapid credential rotation after exposure."
status: active
tags: [security, passwords, hashing, credential-access]
private: false
---

# Hash Cracking and Password Storage

## Purpose

Password security depends on slow, salted password hashing, strong user choices, MFA, and rapid credential rotation after exposure.

## Key Ideas

- Password hashes are not encryption; defenders choose storage schemes to slow offline guessing if the database leaks.
- Use dedicated password hashing functions with salts and work factors: Argon2id, bcrypt, scrypt, or PBKDF2 when constrained by platform requirements.
- Credential stuffing and reuse mean password storage must pair with MFA, breach monitoring, and rate-limited authentication.

## Defensive Use

- Store no plaintext passwords, tune work factors periodically, protect reset flows, and rotate exposed secrets after an incident.
- For investigations, treat cracked passwords as compromised everywhere users may have reused them.

## Sources

- OWASP Password Storage Cheat Sheet - https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- NIST SP 800-63B - https://pages.nist.gov/800-63-4/sp800-63b.html
- hashcat project - https://hashcat.net/hashcat/

## Related

- [Crypto & Ransomware - Index](kb://11-security-crypto-ransomware-crypto-ransomware-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
