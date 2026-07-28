---
summary: "Triangulation maximizing minimum angles and dual to the Voronoi diagram, built by sweepline methods."
status: active
tags: [reference, engineering, algorithms, geometry, triangulation]
private: false
---

# Delaunay Triangulation

## Purpose

Triangulation maximizing minimum angles and dual to the Voronoi diagram, built by sweepline methods.

## Core Model

- The Delaunay triangulation of a point set is the triangulation in which no point lies inside the circumcircle of any triangle (the empty-circumcircle property).
- Among all triangulations it maximizes the minimum interior angle, avoiding thin slivers and making it preferred for mesh generation and interpolation.
- It is the straight-line dual of the Voronoi diagram: an edge joins two points exactly when their Voronoi cells share a boundary.

## How It Works

- Fortune's sweepline moves a horizontal line down the plane, tracking a "beach line" of parabolic arcs; site events add arcs and circle events emit Voronoi vertices, yielding O(n log n) construction.
- The Delaunay edges are recovered as the dual of the computed Voronoi diagram.
- Incremental insertion with edge flips restores the empty-circumcircle property locally after each point is added; randomized incremental construction gives expected O(n log n).

## Tradeoffs

- The InCircle predicate is degeneracy-prone; robust implementations use exact or adaptive-precision arithmetic to avoid inconsistent flips.
- Any planar Delaunay triangulation has O(n) triangles, but the 3D generalization can be quadratic in the worst case.

## Sources

- Fortune, A Sweepline Algorithm for Voronoi Diagrams (1987) - https://doi.org/10.1007/BF01840357
- de Berg et al., Computational Geometry: Algorithms and Applications - https://www.springer.com/gp/book/9783540779735

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
