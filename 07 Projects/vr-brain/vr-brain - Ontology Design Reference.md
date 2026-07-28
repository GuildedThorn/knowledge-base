---
summary: "Palantir Foundry Ontology concepts to consider for a later, plugin-owned semantic operations layer in the vr-brain rewrite."
status: reference
tags: [projects, vr-brain, architecture, ontology, knowledge-graph]
source: https://www.palantir.com/docs/foundry/ontology/overview
reviewed: 2026-07-27
---

## Purpose

Keep Palantir Foundry's Ontology in consideration for a later phase of the
ground-up vr-brain rewrite. This is an architectural reference, not a decision
to add Palantir as a service, SDK, or runtime dependency.

Official reference:
[Ontology building overview](https://www.palantir.com/docs/foundry/ontology/overview).

## Useful model

The overview separates:

- **semantic elements** — object types, properties, links, and interfaces;
- **kinetic elements** — governed actions and functions;
- **application projections** — reusable views, search, graphs, maps, and
  workflows;
- **policy** — granular security, governance, and change management.

Possible vr-brain mapping:

| Ontology idea | Rewrite analogue |
|---|---|
| Object type/property | versioned typed projections from knowledge, evidence, ingestion, Earth, and integrations |
| Link type | explicit provenance, spatial, temporal, authorship, and dependency relations |
| Interface | shared read contract implemented by multiple domain object types |
| Action type | bounded command with validation, Touchstone consent when privileged, and an audit result |
| Function | deterministic plugin-owned query or transformation |
| Object view | workspace surface or spatial inspector that consumes contracts |
| Digital twin | rebuildable projection of evidence and current state, never the sole authority |

## Rewrite guardrails

- Keep the kernel schema-free; ontology behavior belongs in removable plugins.
- Preserve authoritative source records and provenance.
- Separate read projections from mutations.
- Treat remote text as evidence, never executable instruction.
- Route privileged actions through Touchstone with append-before-apply audit.
- Version object, link, interface, and action definitions before external
  plugins can depend on them.
- Enforce visibility at query time as well as ingestion time.

## Decision gate

Consider an optional `vrbrain.ontology` plugin family only after at least three
independent domains need the same typed relationship or governed-action
contract. A later slice could contain a schema registry, rebuildable projection
index, bounded query service, Touchstone-gated action registry, and spatial or
workspace views.

The repository version of this note is
`/home/thorn/Games/vr-brain-rewrite/docs/ONTOLOGY.md`.

## Related

- [[vr-brain - Ground-Up Plugin Rewrite 2026-07-27]]
- [[vr-brain - Architecture]]
- [[Earth - Geo Engine Rewrite]]
- [[vr-brain - Overview]]
