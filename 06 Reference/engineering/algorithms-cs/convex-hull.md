---
summary: "Smallest convex polygon enclosing a point set, computed by Graham scan in O(n log n)."
status: active
tags: [reference, engineering, algorithms, geometry, hull]
private: false
---

# Convex Hull

## Purpose

Smallest convex polygon enclosing a point set, computed by Graham scan in O(n log n).

## Core Model

- The convex hull of a finite planar point set is the smallest convex polygon containing every point; every hull vertex is a point of the set.
- The primitive is the orientation (cross-product) test: three points turn left, right, or are collinear, letting the algorithm avoid floating-point angle computation.
- A left/right turn test drives most hull constructions by rejecting points that create a reflex (concave) vertex.

## How It Works

- Graham scan sorts points by polar angle about the lowest point, then walks the sorted list pushing points onto a stack and popping any that make a non-left turn; it runs in O(n log n), dominated by the sort.
- Gift-wrapping (Jarvis march) repeatedly picks the most counter-clockwise next hull point in O(nh), where `h` is the hull size, favoring small hulls.
- Andrew's monotone chain is a robust variant sorting by x-coordinate and building lower and upper hulls.

## Tradeoffs

- Comparison-based hull construction has an Omega(n log n) lower bound via reduction from sorting.
- Output-sensitive methods like Chan's algorithm achieve O(n log h), beating both when `h` is small.

## Sources

- Graham, An Efficient Algorithm for Determining the Convex Hull of a Finite Planar Set (1972) - https://doi.org/10.1016/0020-0190(72)90045-2
- de Berg et al., Computational Geometry: Algorithms and Applications - https://www.springer.com/gp/book/9783540779735

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
