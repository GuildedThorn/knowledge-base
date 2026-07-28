---
summary: "How user namespaces remap UIDs/GIDs so unprivileged processes hold capabilities inside an isolated namespace."
status: active
tags: [reference, engineering, linux, user-namespace, rootless, privilege]
private: false
---

# User Namespaces and Rootless Containers

## Purpose

How user namespaces remap UIDs/GIDs so unprivileged processes hold capabilities inside an isolated namespace.

## UID/GID Mapping

- A user namespace defines a mapping between IDs inside the namespace and IDs in the parent namespace.
- Maps are written once to `/proc/<pid>/uid_map` and `/proc/<pid>/gid_map`, each line: `inside_id  outside_id  length`.
- Writing `gid_map` unprivileged usually requires first writing `deny` to `/proc/<pid>/setgroups`.
- Ranges for unprivileged users are delegated via `/etc/subuid` and `/etc/subgid`, typically applied by `newuidmap`/`newgidmap` (setuid helpers with `CAP_SETUID`).

## Scoped Capabilities

- The process that creates a namespace gains a full capability set *within* it, but those capabilities apply only to objects owned by that namespace.
- An unprivileged user can therefore become root-inside the namespace while remaining unprivileged on the host.
- Operations on resources owned by an ancestor namespace (e.g. the real root filesystem) still require real host privilege.

## Rootless Security Model

- Rootless container runtimes (Podman, rootless Docker, Buildah) run wholly inside a user namespace, shrinking the attack surface of a compromised container.
- A container-root escape yields only the mapped unprivileged host UID, not host root.
- Historically user namespaces expanded kernel attack surface (unprivileged creation of other namespaces), so some distros gate them behind sysctls like `kernel.unprivileged_userns_clone`.

## Sources

- man7 - user_namespaces(7) - https://man7.org/linux/man-pages/man7/user_namespaces.7.html
- man7 - unshare(2) - https://man7.org/linux/man-pages/man2/unshare.2.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
