---
summary: "Nullable reference types make nullability part of the C# type flow analysis so APIs can express and check null contracts."
status: active
tags: [reference, engineering, csharp, nullable]
private: false
---

# Nullable Reference Types

## Purpose

Nullable reference types make nullability part of the C# type flow analysis so APIs can express and check null contracts.

## Core Model

- NRT is a compile-time analysis feature; it does not change CLR reference semantics.
- `string` means expected non-null and `string?` means may be null when nullable annotations are enabled.
- Attributes such as NotNullWhen, MaybeNull, MemberNotNull, and DoesNotReturn refine flow analysis for real APIs.

## Engineering Notes

- Enable nullable in new projects and migrate older projects per assembly or folder to avoid warning floods.
- Treat nullability warnings as API design feedback, not merely compiler noise.
- Use guard clauses and attributes for framework/lifecycle code where the compiler cannot infer initialization.

## Sources

- Microsoft - Nullable reference types - https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references
- Microsoft - Nullable static analysis attributes - https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/attributes/nullable-analysis
- Microsoft - Nullable warnings - https://learn.microsoft.com/en-us/dotnet/csharp/nullable-warnings

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
