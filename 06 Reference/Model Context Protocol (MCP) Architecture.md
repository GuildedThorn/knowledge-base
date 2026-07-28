## Purpose

Reference for the protocol vr-brain's own [McpServer.cs](kb://07-projects-vr-brain-vr-brain-architecture) implements a custom subset of — the standard MCP is a much fuller spec than the raw-TCP JSON-RPC bridge vr-brain runs today. Compiled 2026-07-24, checked against the [2026-07-28 MCP spec release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/).

## Core model

- **Transport-agnostic JSON-RPC 2.0.** Every message is a standard JSON-RPC request/response/notification. Two official transports: **stdio** (spawn the server as a local subprocess, talk over its stdin/stdout — what the `claude` CLI expects) and **HTTP/SSE** (remote servers, same JSON-RPC payloads over HTTP POST + Server-Sent Events for server→client push). vr-brain's `McpServer.cs` uses neither directly — it opens a raw loopback `TcpListener` and the `claude` CLI reaches it through a `socat` stdio↔TCP bridge, which is a pragmatic way to get a long-lived, always-on server without re-spawning a subprocess per session, at the cost of not being a spec-compliant transport on its own.
- **Three primitives**, each independently negotiated via capabilities:
  - **Tools** — functions the model can invoke (vr-brain: `earth_pin`, `open_terminal`, `read_note`, etc. — see `RunTool` in `McpServer.cs`).
  - **Resources** — data the model can read without a tool call (file contents, DB rows). vr-brain doesn't expose resources today; every read goes through a tool (`read_note`, `read_terminal`) instead.
  - **Prompts** — reusable, server-defined prompt templates the client can surface (e.g. as slash commands). Also unused in vr-brain currently.
- **Lifecycle:** client sends `initialize` (protocol version + its capabilities) → server responds with its own capabilities (e.g. `{"tools": {}}`, matching what `McpServer.cs` returns) → client sends `initialized` notification → normal operation (`tools/list`, `tools/call`, etc.) begins. Capability negotiation means a client should never assume a primitive is available — check the `initialize` response.

## 2026 spec direction (release candidate, final 2026-07-28)

- **Stateless protocol core** — session state becomes optional/pluggable rather than assumed, easing horizontal scaling of remote servers.
- **Extensions framework** — a formal mechanism for vendor/experimental capabilities without forking the core spec (where features like elicitation and sampling started).
- **Tasks** — long-running operations get first-class status/cancellation instead of every tool call being assumed synchronous. Directly relevant to anything like vr-brain's `open_terminal`/long shell commands, which today just block the JSON-RPC call until done.
- **MCP Apps** — a UI-surfacing extension so a server can ship an interactive widget, not just text/JSON results.
- **Authorization hardening + a formal deprecation policy** — MCP originally shipped with minimal auth guidance; this closes that gap for remote (HTTP) servers. Not relevant to a loopback-only server like vr-brain's, but load-bearing if `McpServer.cs` ever listens on more than `127.0.0.1` (flagged as a real risk in [vr-brain Improvement Areas](kb://00-inbox-vr-brain-improvement-areas): "unauthenticated JSON-RPC over localhost TCP... one misbind exposes the whole agent + browser surface").

## Design implications for vr-brain

- The permission-gating pattern already in `McpServer.cs` (`GateDescription`, the `permission_prompt`/`ask_user` special-cased tool calls that pause for in-world approval) is doing by hand what the Tasks + auth-hardening work in the 2026 spec is trying to standardize — a tool call that shouldn't just fire-and-forget. Worth knowing if vr-brain ever migrates off the custom TCP bridge onto a spec-native transport, since some of that plumbing might become protocol-level instead of app-level.
- If exposing more of vr-brain over MCP (e.g. letting other clients besides the bundled `claude` CLI connect), Resources would be the natural fit for `read_note`/`read_terminal` today doing double duty as both discovery and fetch — a real MCP resource list would let a client browse without a tool round-trip per item.

## Related

- [vr-brain - Overview](kb://07-projects-vr-brain-vr-brain-overview)
- [vr-brain Improvement Areas](kb://00-inbox-vr-brain-improvement-areas)

Sources:
- [Architecture overview - Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)
- [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
- [Complete Guide to MCP in 2026 - DEV Community](https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11)
