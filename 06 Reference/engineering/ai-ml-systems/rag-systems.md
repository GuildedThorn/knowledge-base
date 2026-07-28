---
summary: "RAG grounds model responses in retrieved external context, combining indexing, retrieval, ranking, prompting, generation, and citation checks."
status: active
tags: [reference, engineering, ai, rag]
private: false
---

# Retrieval-Augmented Generation

## Purpose

RAG grounds model responses in retrieved external context, combining indexing, retrieval, ranking, prompting, generation, and citation checks.

## Core Model

- The pipeline usually includes ingestion, chunking, embedding/indexing, query rewriting, retrieval, reranking, context assembly, and answer generation.
- Retrieval failure and generation failure are separate; good prompts cannot fix missing evidence.
- Grounding requires source metadata and answer validation, not merely stuffing chunks into context.

## Engineering Notes

- Build eval sets with real questions, expected sources, and unacceptable answers.
- Track retrieval metrics such as recall@k and generation metrics such as groundedness and refusal behavior.
- Use hybrid lexical/vector retrieval for technical corpora where exact symbols matter.

## Sources

- Lewis et al. - Retrieval-Augmented Generation - https://arxiv.org/abs/2005.11401
- Haystack RAG docs - https://docs.haystack.deepset.ai/docs/rag
- LangChain RAG concepts - https://python.langchain.com/docs/concepts/rag/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
