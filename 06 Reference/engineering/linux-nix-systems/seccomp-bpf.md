---
summary: "Kernel syscall filtering that restricts which system calls a process may make using classic BPF programs."
status: active
tags: [reference, engineering, linux, seccomp, syscall-filter, sandbox]
private: false
---

# seccomp and seccomp-BPF

## Purpose

Kernel syscall filtering that restricts which system calls a process may make using classic BPF programs.

## Modes

- **Strict mode** (`SECCOMP_SET_MODE_STRICT`): the process may only call `read`, `write`, `_exit`, and `sigreturn`; any other syscall kills it.
- **Filter mode** (`SECCOMP_SET_MODE_FILTER`): installs a classic-BPF program evaluated on every syscall.
- Filters are installed via `seccomp(2)` or the older `prctl(PR_SET_SECCOMP)`; setting `PR_SET_NO_NEW_PRIVS` first lets unprivileged processes install them.
- Filters are inherited across `fork`/`clone` and preserved across `execve`; multiple filters stack and the most restrictive action wins.

## Filter Programs and Actions

- The BPF program receives a `seccomp_data` struct: syscall number, architecture, instruction pointer, and up to six arguments.
- Return actions include `KILL_PROCESS`, `KILL_THREAD`, `TRAP` (SIGSYS), `ERRNO` (fake a return code), `USER_NOTIF` (delegate to a supervisor), `TRACE`, `LOG`, and `ALLOW`.
- Always match on `arch` first — syscall numbers differ per architecture and the x32 ABI ORs in a high bit.

## Pitfalls and Uses

- BPF cannot dereference pointer arguments, so it cannot inspect string paths or struct contents — only scalar/flag args.
- This exposes TOCTOU races; deep argument inspection needs `USER_NOTIF` or ptrace, not the filter alone.
- Used by container runtimes (Docker's default profile blocks ~44 syscalls), systemd `SystemCallFilter=`, and browser/renderer sandboxes.

## Sources

- Linux kernel docs - Seccomp BPF - https://docs.kernel.org/userspace-api/seccomp_filter.html
- man7 - seccomp(2) - https://man7.org/linux/man-pages/man2/seccomp.2.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
