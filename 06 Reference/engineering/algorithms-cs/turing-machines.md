---
summary: "Abstract model of computation defining computability and grounding the Church-Turing thesis."
status: active
tags: [reference, engineering, algorithms, computability, models]
private: false
---

# Turing Machines

## Purpose

Abstract model of computation defining computability and grounding the Church-Turing thesis.

## Machine Definition and Configurations

- A Turing machine has a finite state control, an unbounded tape divided into cells, and a read/write head positioned over one cell.
- A transition function maps (current state, scanned symbol) to (new symbol, head move left/right, new state).
- A configuration captures the full instantaneous state: tape contents, head position, and control state.
- Computation proceeds as a sequence of configurations until the machine halts in an accepting or rejecting state, or runs forever.

## Universality

- A universal Turing machine takes an encoding of any machine plus its input and simulates that machine's behavior.
- Universality demonstrates that a single fixed machine can compute any computable function, prefiguring the stored-program computer.
- Variants (multi-tape, nondeterministic, multi-track) compute the same class of functions, differing only in efficiency, showing the model is robust.

## Church-Turing Thesis

- The thesis holds that any function "effectively calculable" by a mechanical procedure is computable by a Turing machine.
- It is a definitional claim linking the informal notion of algorithm to a precise formal model, not a provable theorem.
- Independent formalisms - lambda calculus, general recursive functions, register machines - all define the same class, strong evidence for the thesis.

## Sources

- Turing, On Computable Numbers, with an Application to the Entscheidungsproblem (1936) - https://doi.org/10.1112/plms/s2-42.1.230
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis - https://plato.stanford.edu/entries/church-turing/

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
