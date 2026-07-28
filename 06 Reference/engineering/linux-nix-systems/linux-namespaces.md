---
summary: "The seven kernel namespace types that virtualize global resources to give processes isolated views of the system."
status: active
tags: [reference, engineering, linux, namespaces, isolation, containers]
private: false
---

# Linux Namespaces

## Purpose

The seven kernel namespace types that virtualize global resources to give processes isolated views of the system.

## The Seven Types

- **Mount (`CLONE_NEWNS`)**: isolates the set of filesystem mount points a process sees.
- **UTS (`CLONE_NEWUTS`)**: isolates the hostname and NIS domain name.
- **IPC (`CLONE_NEWIPC`)**: isolates System V IPC objects and POSIX message queues.
- **PID (`CLONE_NEWPID`)**: gives an isolated process-ID number space, with a new PID 1 acting as init/reaper.
- **Network (`CLONE_NEWNET`)**: isolates network devices, IP addresses, routing tables, ports, and firewall rules.
- **User (`CLONE_NEWUSER`)**: isolates UID/GID mappings and capabilities; can be created unprivileged.
- **Cgroup (`CLONE_NEWCGROUP`)**: isolates the view of the cgroup filesystem root, plus Time (`CLONE_NEWTIME`) for clock offsets.

## Lifecycle

- `clone(2)` and `fork` create a child directly in new namespaces via `CLONE_NEW*` flags.
- `unshare(2)` moves the calling process into fresh namespaces without forking.
- `setns(2)` joins an existing namespace referenced by an fd (e.g. `/proc/<pid>/ns/*`).
- A namespace persists while any process is a member, an fd is open on it, or a bind mount pins it.

## How Containers Use Them

- Runtimes (runc, LXC, systemd-nspawn) combine all namespace types plus cgroups, capabilities, and seccomp.
- Namespaces provide the isolated *view*; cgroups provide resource *limits* — the two are orthogonal.
- User namespaces enable rootless containers by mapping an unprivileged host UID to root inside.

## Sources

- man7 - namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html
- LWN - Namespaces in operation - https://lwn.net/Articles/531114/

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
