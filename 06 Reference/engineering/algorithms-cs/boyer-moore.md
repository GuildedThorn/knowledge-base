---
summary: "String search scanning the pattern right-to-left with bad-character and good-suffix rules for sublinear skips."
status: active
tags: [reference, engineering, algorithms, string-matching, heuristics]
private: false
---

# Boyer-Moore Algorithm

## Purpose

String search scanning the pattern right-to-left with bad-character and good-suffix rules for sublinear skips.

## Right-to-Left Scan

- Boyer-Moore aligns the pattern against the text and compares characters from the pattern's right end toward its left.
- On a mismatch or full match, it shifts the pattern right by the maximum jump allowed by two precomputed heuristics.
- Scanning from the right lets long skips occur early, since a mismatch near the pattern's end can rule out many alignments at once.

## Bad-Character Rule

- When a text character causes a mismatch, the bad-character rule shifts the pattern so its rightmost occurrence of that character aligns with the mismatched text position.
- If the character does not appear in the pattern, the pattern can skip entirely past that text position.
- This rule is most effective on large alphabets where mismatched characters are often absent from the pattern.

## Good-Suffix Rule and Performance

- The good-suffix rule uses the already-matched suffix: it shifts to the next pattern occurrence of that suffix, or a matching prefix, avoiding known-bad alignments.
- The algorithm takes the larger of the two rule shifts at each step.
- Average-case behavior is sublinear - fewer than n comparisons for text length n - and preprocessing is O(m + alphabet); the classic worst case is O(nm) but variants like Galil's give linear worst-case time.

## Sources

- Boyer & Moore, A Fast String Searching Algorithm (1977) - https://doi.org/10.1145/359842.359859

## Related

- [Algorithms and CS - Index](kb://06-reference-engineering-algorithms-cs-algorithms-cs-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
