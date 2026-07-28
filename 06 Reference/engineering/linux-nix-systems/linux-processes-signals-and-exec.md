---
summary: "Linux process control centers on fork/clone, exec, wait, signals, file descriptors, and exit status."
status: active
tags: [reference, engineering, linux, processes]
private: false
---

# Linux Processes, Signals, and exec

## Purpose

Linux process control centers on fork/clone, exec, wait, signals, file descriptors, and exit status.

## Core Model

- A process has virtual memory, file descriptors, credentials, namespaces, signal handlers, and scheduling state.
- exec replaces the program image while preserving selected process attributes such as PID and open file descriptors.
- Signals deliver asynchronous notifications with default actions, handlers, masks, and race-prone semantics.

## Engineering Notes

- Close or mark file descriptors close-on-exec when spawning child processes.
- Handle SIGTERM for graceful shutdown and reserve SIGKILL for last-resort termination.
- Use process groups/sessions for terminal jobs and service supervisors that need to stop trees.

## Sources

- Linux man-pages project - https://www.kernel.org/doc/man-pages/
- man7 signal - https://man7.org/linux/man-pages/man7/signal.7.html
- man2 execve - https://man7.org/linux/man-pages/man2/execve.2.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
