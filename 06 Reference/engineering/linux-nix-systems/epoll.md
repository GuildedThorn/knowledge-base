---
summary: "Linux's scalable I/O event notification interface for monitoring many file descriptors in O(1) readiness."
status: active
tags: [reference, engineering, linux, epoll, event-loop, io-multiplexing]
private: false
---

# epoll

## Purpose

Linux's scalable I/O event notification interface for monitoring many file descriptors in O(1) readiness.

## Core Model

- An epoll instance is a kernel object holding an *interest list* of watched fds and a *ready list* of fds with pending events.
- Unlike `select`/`poll`, which rescan the full fd set each call at O(n), epoll returns only ready fds so cost scales with active connections, not total watched.
- `epoll_create1` creates the instance and returns a fd; the fd itself can be nested inside another epoll instance.

## How It Works

- `epoll_ctl` mutates the interest list with `EPOLL_CTL_ADD`, `MOD`, or `DEL`, associating an `epoll_event` (event mask plus user data) with each fd.
- `epoll_wait` blocks until one or more fds are ready or a timeout elapses, filling a caller-supplied array of ready events.
- Level-triggered (default) re-reports an fd while it stays ready; edge-triggered (`EPOLLET`) reports only on transitions, requiring the app to drain the fd until `EAGAIN`.

## Engineering Notes

- Edge-triggered mode pairs with non-blocking fds and is common in high-performance servers to minimize wakeups.
- Underpins the event loops of nginx, libevent, libuv, and most async runtimes on Linux; `EPOLLONESHOT` helps distribute fds across worker threads safely.

## Sources

- man7 - epoll(7) - https://man7.org/linux/man-pages/man7/epoll.7.html
- man7 - epoll_ctl(2) - https://man7.org/linux/man-pages/man2/epoll_ctl.2.html

## Related

- [Linux, Nix, and Systems - Index](kb://06-reference-engineering-linux-nix-systems-linux-nix-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
