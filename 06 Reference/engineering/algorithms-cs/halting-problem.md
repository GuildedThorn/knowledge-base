---
summary: "Canonical undecidable problem proving no algorithm can decide whether an arbitrary program halts."
status: active
tags: [reference, engineering, algorithms, undecidability, computability]
private: false
---

# The Halting Problem

## Purpose

Canonical undecidable problem proving no algorithm can decide whether an arbitrary program halts.

## Diagonalization Proof

- The halting problem asks for a general procedure that, given a program and input, decides whether the program eventually halts.
- Turing (1936) proved no such procedure exists via a diagonalization argument.
- Assume a decider H exists; construct a program D that halts exactly when H reports its input does not halt, then run D on itself.
- D halting implies it should not halt and vice versa, a contradiction, so H cannot exist.

## Reductions to Other Problems

- Once halting is known undecidable, other problems are shown undecidable by reducing halting to them.
- Classic reductions establish undecidability of the totality problem, program equivalence, and the Post correspondence problem.
- A reduction converts a halting instance into an instance of the target problem so that a solver for the target would solve halting, which is impossible.

## Rice's Theorem Context

- Rice's theorem generalizes the result: every non-trivial semantic property of the function a program computes is undecidable.
- "Non-trivial" means the property holds for some but not all computable functions; "semantic" means it depends on behavior, not syntax.
- Consequences include the impossibility of a perfect general analyzer for properties like "always terminates" or "computes the zero function."

## Sources

- Turing, On Computable Numbers (1936) - https://doi.org/10.1112/plms/s2-42.1.230
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis - https://plato.stanford.edu/entries/church-turing/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
