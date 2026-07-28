---
summary: "AI evaluations measure model behavior on task-specific datasets, rubrics, adversarial cases, and regression suites."
status: active
tags: [reference, engineering, ai, evals]
private: false
---

# Evals and Benchmarks

## Purpose

AI evaluations measure model behavior on task-specific datasets, rubrics, adversarial cases, and regression suites.

## Core Model

- Benchmarks compare models but rarely capture local product risk by themselves.
- Task evals need input distribution, expected behavior, scoring rubric, and failure taxonomy.
- Human review, model grading, unit tests, and production telemetry all catch different failures.

## Engineering Notes

- Create golden sets from real workflows and update them when the workflow changes.
- Track regressions across model, prompt, retrieval, tool, and infrastructure changes.
- Include refusal, hallucination, citation, safety, latency, and cost in deployment gates where relevant.

## Sources

- HELM benchmark - https://crfm.stanford.edu/helm/
- EleutherAI LM Evaluation Harness - https://github.com/EleutherAI/lm-evaluation-harness
- MLCommons AI Safety benchmark - https://mlcommons.org/working-groups/ai-safety/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
