---
summary: "The Linux Security Module implementing mandatory access control via type enforcement and security contexts."
status: active
tags: [reference, engineering, linux, selinux, mac, lsm]
private: false
---

# SELinux

## Purpose

The Linux Security Module implementing mandatory access control via type enforcement and security contexts.

## Type Enforcement and Labels

- Every subject and object carries a security context `user:role:type:level` (e.g. `system_u:object_r:httpd_sys_content_t:s0`).
- **Type Enforcement (TE)** is the primary model: policy `allow` rules state which source types may perform which operations on which target types.
- Absent an explicit allow rule, access is denied by default — MAC overrides discretionary (DAC) permissions.
- Optional MLS/MCS levels add multi-level or category-based separation on top of type enforcement.

## Policy, Modules, and Booleans

- The active policy (commonly the targeted policy on RHEL/Fedora) is compiled from modules and loaded into the kernel.
- **Booleans** toggle predefined policy behavior at runtime without recompiling (e.g. `httpd_can_network_connect`), via `setsebool`.
- File contexts are assigned from rules and can be reset with `restorecon`; `semanage fcontext` persists custom label mappings.

## Modes and Troubleshooting

- Three modes: **enforcing** (deny + log), **permissive** (allow but log would-be denials), and **disabled**.
- Denials are recorded as **AVC** (Access Vector Cache) messages in the audit log; `ausearch`, `audit2allow`, and `sealert` help diagnose them.
- Common fixes are relabeling files or flipping a boolean rather than writing new policy; custom modules are generated with `audit2allow -M`.

## Sources

- SELinux Project Wiki - https://selinuxproject.org/page/Main_Page
- The SELinux Notebook - https://github.com/SELinuxProject/selinux-notebook

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
