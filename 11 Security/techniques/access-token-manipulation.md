---
summary: "Duplicating, impersonating, or stealing security tokens to run code in another user's security context."
status: active
tags: [security, techniques, token, impersonation, privilege-escalation]
private: false
---

# Access Token Manipulation

## Purpose

Duplicating, impersonating, or stealing security tokens to run code in another user's security context.

## Core Model

- Every Windows process and thread carries an access token describing the user identity, group memberships, and privileges used for all access checks.
- Primary tokens are assigned to processes; impersonation tokens are attached to individual threads so a thread can act as another identity.
- Impersonation levels (Anonymous, Identification, Impersonation, Delegation) bound how far a captured token can be reused, especially across the network.

## How It Works

- `OpenProcessToken` retrieves a target's token; `DuplicateTokenEx` copies it into a new primary or impersonation token.
- `ImpersonateLoggedOnUser` or `SetThreadToken` applies an impersonation token to the current thread; `CreateProcessWithTokenS`/`CreateProcessAsUser` spawns a new process under a stolen token.
- Duplicating another process's token and creating a process typically requires `SeDebugPrivilege` and `SeImpersonatePrivilege`/`SeAssignPrimaryTokenPrivilege`, so it is usually a lateral or same-privilege move, not a raw escalation.

## Security Notes

- Detection focuses on token-manipulation API sequences, unusual `CreateProcessWithToken` calls, and processes whose token user mismatches their parent.
- Restrict `SeDebugPrivilege` and impersonation privileges to service accounts that truly need them; audit privilege-use events (4673/4674).

## Sources

- MITRE ATT&CK T1134 - https://attack.mitre.org/techniques/T1134/
- Microsoft Access Tokens - https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
