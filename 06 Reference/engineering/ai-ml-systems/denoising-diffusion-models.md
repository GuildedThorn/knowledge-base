---
summary: "Generative models that learn to reverse a gradual noising process to synthesize samples from noise."
status: active
tags: [reference, engineering, ai-ml, generative, diffusion]
private: false
---

# Denoising Diffusion Probabilistic Models

## Purpose

Generative models that learn to reverse a gradual noising process to synthesize samples from noise.

## Core Model

- A fixed forward (diffusion) process adds Gaussian noise to data over T steps until it becomes approximately pure noise.
- A learned reverse process, parameterized by a neural network, removes noise step by step to reconstruct a data sample.
- The closed-form forward marginal lets any noisy step be sampled directly from the clean input, enabling efficient training.
- DDPM reparameterizes the model to predict the added noise ε, giving a simple weighted mean-squared-error objective.

## Training and Sampling

- Training samples a random timestep, corrupts the input, and minimizes the error between predicted and true noise.
- The noise schedule (linear, cosine) controls how variance is added and strongly affects sample quality.
- Ancestral DDPM sampling requires many sequential denoising steps, making generation slow.
- DDIM defines a non-Markovian deterministic reverse process that produces comparable samples in far fewer steps.

## Sources

- Denoising Diffusion Probabilistic Models - https://arxiv.org/abs/2006.11239
- Denoising Diffusion Implicit Models - https://arxiv.org/abs/2010.02502

## Related

- [AI, ML, and Agent Systems - Index](kb://06-reference-engineering-ai-ml-systems-ai-ml-systems-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
