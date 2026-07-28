---
summary: "A path-based mandatory access control LSM that confines programs with per-executable security profiles."
status: active
tags: [reference, engineering, linux, apparmor, mac, lsm]
private: false
---

# AppArmor

## Purpose

A path-based mandatory access control LSM that confines programs with per-executable security profiles.

## Path-Based vs Label-Based

- AppArmor keys access decisions on filesystem **paths**, not on labels attached to inodes as SELinux does.
- This makes profiles easier to read and write, but means access can differ across hard links or bind mounts to the same inode.
- Profiles are per-executable and stored in `/etc/apparmor.d/`; unconfined programs run with normal DAC rules.
- Default on Ubuntu, SUSE, and Debian, where it is generally considered lower-effort to author than SELinux policy.

## Modes

- **Enforce mode**: operations outside the profile are blocked and logged.
- **Complain (learning) mode**: violations are permitted but logged, used to build a profile against real workload behavior.
- `aa-genprof` and `aa-logprof` generate and refine profiles from logged activity; `aa-enforce`/`aa-complain` switch modes; `aa-status` lists loaded profiles.

## Profile Language

- Rules grant file permissions (`r`, `w`, `x`, `m`, `k`, `l`) over path globs, plus capability, network, and mount rules.
- Reusable **abstractions** (e.g. `abstractions/base`, `abstractions/nameservice`) are included to cover common access patterns.
- Execute transitions control child confinement: `Px` (transition to child's profile), `Cx` (child profile), `ix` (inherit), `ux` (unconfined).

## Sources

- AppArmor Wiki - https://gitlab.com/apparmor/apparmor/-/wikis/home
- Ubuntu manpages - apparmor(7) - https://manpages.ubuntu.com/manpages/noble/man7/apparmor.7.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
