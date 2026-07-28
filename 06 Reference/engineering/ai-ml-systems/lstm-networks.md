---
summary: "A gated recurrent architecture that mitigates vanishing gradients to model long-range sequence dependencies."
status: active
tags: [reference, engineering, ai-ml, recurrent, gating]
private: false
---

# Long Short-Term Memory Networks

## Purpose

A gated recurrent architecture that mitigates vanishing gradients to model long-range sequence dependencies.

## Core Model

- A cell state runs through each timestep as a memory conveyor, edited only by additive and multiplicative gate operations.
- The forget gate scales what the cell retains; the input gate controls new candidate values written; the output gate filters what the hidden state exposes.
- Gates are sigmoid-squashed linear layers over the previous hidden state and current input; candidate values use tanh.
- The hidden state feeds the next step and any output head, decoupling stored memory from emitted representation.

## How It Works

- The additive cell-state path forms a "constant error carousel," letting gradients flow across many timesteps without repeated multiplicative shrinkage.
- This preserves error signal where plain RNNs suffer vanishing (or exploding) gradients through backpropagation through time.
- Variants like the GRU merge gates for fewer parameters; peephole connections let gates read the cell state directly.

## Engineering Notes

- Still useful for streaming or low-latency sequence tasks where full attention is costly, though transformers dominate large-scale modeling.
- Gradient clipping and careful gate-bias initialization (e.g. forget-gate bias near 1) stabilize training.

## Sources

- Long Short-Term Memory (Hochreiter & Schmidhuber) - https://www.bioinf.jku.at/publications/older/2604.pdf
- Understanding LSTM Networks (colah) - https://colah.github.io/posts/2015-08-Understanding-LSTMs/

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
