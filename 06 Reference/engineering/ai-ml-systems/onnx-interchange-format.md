---
summary: "An open standard graph representation for exchanging trained models across frameworks and inference runtimes."
status: active
tags: [reference, engineering, ai-ml, interoperability, serialization]
private: false
---

# ONNX Model Interchange Format

## Purpose

An open standard graph representation for exchanging trained models across frameworks and inference runtimes.

## Core Model

- Represents a model as a directed computation graph of nodes (operators), typed tensor inputs/outputs, initializers (weights), and metadata, serialized with protocol buffers.
- Standardizes behavior through versioned operator sets (opsets); each node references an operator whose semantics are fixed by the opset it targets.
- Covers both classic ML (via the ai.onnx.ml domain) and deep-learning tensor operators, with extension domains for custom ops.

## How It Works

- Frameworks such as PyTorch and TensorFlow export trained models to `.onnx`, decoupling the training stack from the deployment stack.
- ONNX Runtime loads the graph and executes it across hardware via pluggable execution providers (CPU, CUDA, TensorRT, DirectML, and others), applying graph optimizations.
- The portable format enables toolchain steps like quantization, shape inference, and cross-runtime deployment to mobile, edge, and server targets.

## Sources

- ONNX official site - https://onnx.ai/
- ONNX specification repo - https://github.com/onnx/onnx

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
