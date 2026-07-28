---
summary: "io_uring is Linux's shared-ring asynchronous I/O interface for submitting operations and receiving completions with fewer syscall transitions."
status: active
tags: [reference, engineering, linux, io, performance]
private: false
---

# io_uring Linux Async I/O

## Purpose

io_uring is a Linux-specific asynchronous I/O API built around submission and completion ring buffers shared between userspace and the kernel.

## Core Model

- Applications create a ring with `io_uring_setup`.
- Submission queue entries describe requested operations.
- The kernel processes submissions asynchronously.
- Completion queue entries report operation results.
- Shared rings reduce syscall and copy overhead compared with older I/O patterns.

## Engineering Notes

- Queue depth is a design parameter; depth one is easy to understand but leaves throughput on the table.
- io_uring can cover file I/O, networking, polling, timeouts, accept/connect, splice-like operations, and more depending on kernel version.
- Not every operation is truly non-blocking internally; understand when work may be punted to worker threads.
- Kernel version, liburing version, and security restrictions materially affect behavior.

## Sources

- man7 - io_uring(7) - https://www.man7.org/linux/man-pages/man7/io_uring.7.html
- Linux UAPI header - io_uring.h - https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git/+/master/include/uapi/linux/io_uring.h
- Linux kernel docs - io_uring zero-copy Rx - https://www.kernel.org/doc/html/next/networking/iou-zcrx.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Linux Processes, Signals, and exec](kb://06-reference-engineering-linux-nix-systems-linux-processes-signals-and-exec)
- [Linux Filesystems, VFS, and Permissions](kb://06-reference-engineering-linux-nix-systems-linux-filesystems-vfs-and-permissions)
