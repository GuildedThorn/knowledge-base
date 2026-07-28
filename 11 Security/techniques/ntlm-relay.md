---
summary: "Relaying captured NTLM authentication to a third-party service to authenticate as the victim without knowing any secret."
status: active
tags: [security, techniques, ntlm, relay, mitm]
private: false
---

# NTLM Relay Attacks

## Purpose

Relaying captured NTLM authentication to a third-party service to authenticate as the victim without knowing any secret.

## How It Works

- NTLM is a challenge-response protocol with no channel binding by default, so the authenticating client is not tied to a specific destination.
- The attacker positions between a victim and a service, forwarding each NTLM message unchanged to a different target that accepts it.
- The target completes the handshake believing the attacker is the victim, granting an authenticated session.
- Unlike pass-the-hash, no hash is captured; the live authentication itself is proxied.

## Coercion and Targets

- Victims are lured with LLMNR/NBT-NS/mDNS poisoning or coercion methods like PetitPotam and PrinterBug.
- Common relay targets are SMB (for code execution), LDAP (to grant rights or add machine accounts), and AD CS web enrollment for certificate theft.
- Impacket `ntlmrelayx.py` with Responder is the standard toolchain.

## Defensive Use

- Enforce SMB signing and LDAP signing/channel binding to reject relayed sessions.
- Enable Extended Protection for Authentication (EPA) on HTTP endpoints, including AD CS enrollment.
- Disable LLMNR and NBT-NS to remove the name-poisoning foothold.
- Patch and restrict the coercion RPC interfaces (MS-EFSRPC, MS-RPRN).

## Sources

- MITRE ATT&CK T1557.001 - https://attack.mitre.org/techniques/T1557/001/
- Impacket ntlmrelayx - https://github.com/fortra/impacket
- Microsoft NTLM Overview - https://learn.microsoft.com/en-us/windows-server/security/kerberos/ntlm-overview

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
