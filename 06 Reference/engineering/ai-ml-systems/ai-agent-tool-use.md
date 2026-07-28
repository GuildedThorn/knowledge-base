---
summary: "Agent systems let models call tools, read state, write artifacts, and iterate, so reliability depends on permissions, state, planning, and verification."
status: active
tags: [reference, engineering, ai, agents]
private: false
---

# AI Agent Tool Use

## Purpose

Agent systems let models call tools, read state, write artifacts, and iterate, so reliability depends on permissions, state, planning, and verification.

## Core Model

- A tool call is an external side effect or observation, not just text generation.
- Agents need state boundaries: what they can read, what they can mutate, and what requires approval.
- Plans help coordinate long work but do not replace verification.

## Engineering Notes

- Give tools narrow schemas, clear descriptions, and safe defaults.
- Require approvals for irreversible writes, shell commands, credentials, purchases, and external communications.
- Log tool calls and final state so failures are debuggable.

## Sources

- Model Context Protocol specification - https://modelcontextprotocol.io/specification/
- Anthropic - Building effective agents - https://www.anthropic.com/research/building-effective-agents
- LangGraph documentation - https://langchain-ai.github.io/langgraph/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
