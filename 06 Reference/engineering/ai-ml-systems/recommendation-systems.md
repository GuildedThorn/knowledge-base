---
summary: "Recommendation systems rank items for users using signals, candidate generation, scoring, exploration, and feedback loops."
status: active
tags: [reference, engineering, ai, recommenders]
private: false
---

# Recommendation Systems

## Purpose

Recommendation systems rank items for users using signals, candidate generation, scoring, exploration, and feedback loops.

## Core Model

- Typical architecture separates candidate retrieval from ranking and re-ranking.
- Collaborative filtering, matrix factorization, embeddings, sequence models, and content features solve different cold-start and scale problems.
- Feedback loops can amplify popularity, bias, or stale behavior.

## Engineering Notes

- Measure business and user outcomes with offline and online metrics; click-through alone can degrade quality.
- Keep exploration, diversity, freshness, and safety constraints explicit.
- Audit training labels and negative sampling; implicit feedback is noisy.

## Sources

- Google Recommendations Systems guide - https://developers.google.com/machine-learning/recommendation
- Matrix factorization techniques for recommender systems - https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf
- Microsoft Recommenders repo - https://github.com/recommenders-team/recommenders

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
