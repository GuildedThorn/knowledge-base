---
summary: "Linux filesystems expose persistent and virtual resources through VFS objects, permissions, ownership, mounts, and special file types."
status: active
tags: [reference, engineering, linux, filesystems]
private: false
---

# Linux Filesystems, VFS, and Permissions

## Purpose

Linux filesystems expose persistent and virtual resources through VFS objects, permissions, ownership, mounts, and special file types.

## Core Model

- VFS normalizes operations across ext4, btrfs, tmpfs, procfs, sysfs, overlayfs, and network filesystems.
- Unix permissions combine owner/group/other bits with setuid, setgid, sticky bits, ACLs, capabilities, and mount options.
- Inodes, dentries, file descriptors, hard links, symlinks, and mount namespaces have distinct identities and lifetimes.

## Engineering Notes

- Debug permission problems by checking path traversal permissions, mount options, ACLs, LSM labels, and process credentials.
- Use atomic rename for safe replacement of files.
- Understand overlayfs semantics before relying on container filesystem behavior.

## Sources

- Linux kernel VFS docs - https://docs.kernel.org/filesystems/vfs.html
- man7 path_resolution - https://man7.org/linux/man-pages/man7/path_resolution.7.html
- man7 capabilities - https://man7.org/linux/man-pages/man7/capabilities.7.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
