---
summary: BloodHound — collect AD data (SharpHound/bloodhound-python), map shortest path to Domain Admin.
status: active
tags: [security, tools, bloodhound, active-directory]
private: false
---

# BloodHound

Graphs AD relationships so escalation becomes "find a path" instead of guessing. Collect → import → query.

## Collect

```bash
# from Linux with any valid creds
bloodhound-python -d corp.local -u user -p pass -c all -ns $DC --zip
# from a domain-joined Windows host
SharpHound.exe -c All --zipfilename loot.zip
# nxc can collect too:
nxc ldap $DC -u user -p pass --bloodhound -c all
```

Collection methods: `Session`, `LoggedOn`, `ACL`, `Trusts`, `Group`, `LocalAdmin` (`-c All` for everything).

## Analyze

- Run the DB (Neo4j) + BloodHound GUI (CE or legacy); drag the `.zip` in.
- **Mark owned** nodes (right-click → Mark as Owned) — you as the foothold user.
- Pre-built queries: **Shortest Path to Domain Admins**, **from Owned Principals**, **Kerberoastable users**, **AS-REP roastable**, **Unconstrained Delegation**, **Dangerous ACLs**.

## Reading the edges (what each abuse means)

- `MemberOf` → group inheritance.
- `AdminTo` / `CanRDP` / `CanPSRemote` → direct access to a host.
- `GenericAll` / `GenericWrite` / `WriteDacl` / `WriteOwner` → ACL abuse: reset password, add SPN → Kerberoast, or grant yourself rights.
- `ForceChangePassword` → reset target's password.
- `HasSession` → creds of that user are on a box you can reach → dump them.
- `AllowedToDelegate` / `Owns` → delegation / ownership chains.

Each edge's **Help → Abuse Info** tab gives the exact commands.

## Related

- [BloodHound tool index](kb://11-security-tools-tools-index)
- [Active Directory](kb://11-security-playbook-active-directory)
- [impacket & netexec](kb://11-security-tools-impacket-netexec)
