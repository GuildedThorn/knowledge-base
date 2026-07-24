---
summary: Windows privilege escalation — services, tokens, AlwaysInstallElevated, unquoted paths, creds.
status: active
tags: [security, playbook, privesc, windows]
private: false
---

# Windows Privilege Escalation

Enumerate, find one misconfig, escalate to `NT AUTHORITY\SYSTEM`.

## Automate the sweep

```
winPEAS.exe / winPEASany.exe        # broad
PowerUp.ps1  -> Invoke-AllChecks    # PowerShell, service/registry focus
Seatbelt.exe -group=all
```

## Manual checks

```
whoami /priv        # SeImpersonate/SeAssignPrimaryToken -> Potato
whoami /groups
systeminfo          # OS build -> missing-patch KB lookup
cmdkey /list        # saved creds -> runas /savecred
```

## The big categories

- **Token impersonation**: `SeImpersonatePrivilege` (common on service accounts / web shells) → **PrintSpoofer**, **GodPotato**, RoguePotato → SYSTEM. Highest-yield modern path.
- **Service misconfigs**: unquoted service paths (`C:\Program Files\...` with spaces + writable dir), weak service binary/registry perms (`accesschk.exe -uwcqv user *`), writable `binPath` → `sc config svc binPath= ...` → restart.
- **AlwaysInstallElevated**: both HKLM+HKCU registry keys = 1 → install a malicious MSI as SYSTEM (`msfvenom -f msi`).
- **Scheduled tasks**: writable task binary run by a privileged user.
- **DLL hijacking**: writable dir in a privileged process's search path.
- **Registry autoruns / startup** with weak perms.
- **Kernel / patch gap**: `systeminfo` → Watson / WES-NG maps missing KBs to exploits.

## Credential hunting

- `C:\Users\*\`, `Desktop`, `Documents`, unattended installs (`Unattend.xml`, `sysprep.xml`), `web.config`, PowerShell history (`ConsoleHost_history.txt`), `cmdkey`/Credential Manager, registry (`reg query HKLM /f password /t REG_SZ /s`).
- **Dump hashes** once elevated: `mimikatz sekurlsa::logonpasswords`, `reg save hklm\sam` + `system` → `secretsdump.py`.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Active Directory](kb://11-security-playbook-active-directory)
- [Linux Privilege Escalation](kb://11-security-playbook-linux-privesc)
