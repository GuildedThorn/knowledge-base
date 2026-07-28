---
summary: "The Linux Audit subsystem records syscalls, file access, and security events via kernel rules for host forensics."
status: active
tags: [security, dfir, auditd, linux, logging]
private: false
---

# Linux Audit Framework (auditd)

## Purpose

The Linux Audit subsystem records syscalls, file access, and security events via kernel rules for host forensics.

## Rule Syntax

- Watches (`-w`) monitor a path with permission filters (`-p rwxa`) and a key label, e.g. `-w /etc/passwd -p wa -k identity`.
- Syscall rules (`-a`) match on an action/list pair such as `always,exit` plus filters on syscall name, arch, uid, and success.
- Control rules set buffer size (`-b`), failure mode (`-f`), and immutability (`-e 2`), which locks rules until reboot.
- Rules load from `/etc/audit/rules.d/*.rules` and are compiled by augenrules into the running kernel policy.

## Record Types and Keys

- Kernel audit events flow through auditd to `/var/log/audit/audit.log`; a single action often spans multiple linked records sharing an event ID.
- Common record types include SYSCALL, PATH, EXECVE, CWD, USER_AUTH, and PROCTITLE.
- The `-k` key attaches a searchable tag so analysts can correlate rules to detections (e.g. a MITRE technique).

## ausearch and aureport Analysis

- `ausearch` queries the log by key, uid, syscall, time range, or event ID and reassembles multi-record events.
- `aureport` produces summaries (auth failures, executed commands, anomalies) across the audit trail.
- `auditctl -l` lists loaded rules and `-s` reports subsystem status including lost events and backlog.

## Sources

- auditd Man Page - https://man7.org/linux/man-pages/man8/auditd.8.html
- audit.rules Man Page - https://man7.org/linux/man-pages/man7/audit.rules.7.html
- Red Hat Auditing Guide - https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/auditing-the-system_security-hardening

## Related

- [DFIR & Detection - Index](kb://11-security-dfir-detection-dfir-detection-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
