---
summary: Wireshark & tcpdump — capture and dissect traffic, display filters, follow streams, extract creds/files.
status: active
tags: [security, tools, wireshark, network, dfir]
private: false
---

# Wireshark & tcpdump

Packet capture and analysis — for malware C2, cleartext creds, and understanding a protocol on the wire.

## Capture

```bash
tcpdump -i eth0 -w cap.pcap                    # headless capture -> open in Wireshark
tcpdump -i eth0 'port 80 or port 445' -w cap.pcap
tshark -i eth0 -f "tcp port 443" -w cap.pcap   # CLI Wireshark
```

`-f` = BPF **capture** filter (kernel-level, limits what's saved). Different syntax from display filters.

## Display filters (in the GUI / tshark -Y)

```
ip.addr == 10.10.10.5
tcp.port == 445 && smb2
http.request.method == "POST"
dns.qry.name contains "evil"
tcp.flags.syn == 1 && tcp.flags.ack == 0     # connection attempts
frame contains "password"
tcp.stream eq 3
```

## Analyst workflow

- **Statistics → Conversations / Protocol Hierarchy** — who talks to whom, what protocols.
- Right-click a packet → **Follow → TCP/HTTP Stream** — reassemble a session (see full HTTP/creds/commands).
- **File → Export Objects → HTTP/SMB** — pull transferred files out of the capture.
- **Cleartext creds**: filter `http.authorization`, `ftp`, `telnet`, `pop`, `imap` — grab plaintext logins.
- **tshark extraction**: `tshark -r cap.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri`.

## Malware / C2 triage

Pair with INetSim/FakeNet (see [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)) — capture beacons, C2 domains, and exfil while the sample runs sandboxed.

## Related

- [Wireshark tool index](kb://11-security-tools-tools-index)
- [Malware Analysis Workflow](kb://11-security-malware-analysis-malware-analysis-workflow)
- [Pivoting & Tunneling](kb://11-security-playbook-pivoting-tunneling)
