---
summary: "A prompting paradigm interleaving chain-of-thought reasoning traces with tool-use actions and observations."
status: active
tags: [reference, engineering, ai-ml, agents, tool-use]
private: false
---

# ReAct Reasoning and Acting Agents

## Purpose

A prompting paradigm interleaving chain-of-thought reasoning traces with tool-use actions and observations.

## Core Model

- ReAct prompts a language model to emit interleaved reasoning traces (Thought) and task actions (Action) in one loop.
- Each action invokes an external tool or environment; the returned result is fed back as an Observation.
- Reasoning guides which action to take next, while observations ground reasoning in real external feedback.
- The pattern unifies pure chain-of-thought (reason only) and pure act-only agents into a single interleaved policy.

## How It Works

- The loop repeats Thought to Action to Observation until the model emits a final answer or a stopping condition triggers.
- Tools are typically search APIs, calculators, code execution, or knowledge lookups exposed via a fixed action vocabulary.
- Few-shot exemplars in the prompt teach the model the trace format and appropriate tool-selection behavior.
- Observations let the agent recover from mistakes, revise plans, and reduce hallucination versus reasoning in isolation.

## Engineering Notes

- Grounding reasoning in tool feedback improves factuality on knowledge tasks and success rates on interactive benchmarks.
- Failure modes include repetitive action loops and malformed tool calls, mitigated by output parsing and step limits.
- ReAct underpins many modern agent frameworks that orchestrate tools, memory, and multi-step planning.

## Sources

- ReAct: Synergizing Reasoning and Acting in Language Models - https://arxiv.org/abs/2210.03629

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
