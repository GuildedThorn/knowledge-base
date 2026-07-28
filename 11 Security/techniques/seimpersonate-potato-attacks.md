---
summary: "Escalating from a service account with SeImpersonatePrivilege to SYSTEM by coercing and relaying a privileged token."
status: active
tags: [security, techniques, potato, privilege-escalation, token]
private: false
---

# SeImpersonate Potato Attacks

## Purpose

Escalating from a service account with SeImpersonatePrivilege to SYSTEM by coercing and relaying a privileged token.

## Core Model

- Service accounts (IIS `IIS APPPOOL`, MSSQL, `NETWORK SERVICE`) commonly hold `SeImpersonatePrivilege`, which lets a thread act under any token it receives.
- Potato attacks coerce a privileged Windows component to authenticate to a listener the attacker controls, capture the resulting SYSTEM token, then use it to launch a process as SYSTEM.
- The privilege turns a low-integrity service foothold into full local compromise without any kernel exploit.

## How It Works

- Classic JuicyPotato abuses DCOM/OXID resolution to make a SYSTEM COM server authenticate to a local RPC endpoint, capturing its token via `ImpersonateNamedPipeClient` or COM impersonation.
- RoguePotato and later variants redirect the OXID resolver to a remote listener to survive patches that disabled the local port 135 trick.
- PrintSpoofer coerces the Print Spooler service over a named pipe; RottenPotato/SweetPotato bundle multiple coercion paths.

## Operational Notes

- Mitigate by stripping `SeImpersonatePrivilege` from accounts that do not need it, disabling the Print Spooler where unused, and patching coercion surfaces.
- Detect via named-pipe impersonation from service accounts, unexpected SYSTEM child processes of web/db services, and spooler-triggered auth.

## Sources

- MITRE ATT&CK T1134.001 - https://attack.mitre.org/techniques/T1134/001/
- JuicyPotato - https://github.com/ohpe/juicy-potato
- Microsoft Impersonate a Client Privilege - https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/impersonate-a-client-after-authentication

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
