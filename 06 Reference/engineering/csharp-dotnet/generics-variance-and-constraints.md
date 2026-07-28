---
summary: "C# generics provide type-safe reusable code; constraints and variance define what generic APIs can promise and safely substitute."
status: active
tags: [reference, engineering, csharp, generics]
private: false
---

# Generics, Variance, and Constraints

## Purpose

C# generics provide type-safe reusable code; constraints and variance define what generic APIs can promise and safely substitute.

## Core Model

- Generic type parameters are reified in the CLR, so runtime type identity includes generic arguments.
- Constraints such as class, struct, unmanaged, notnull, new(), base types, interfaces, and static abstract members shape valid operations.
- Variance is limited to interface/delegate positions: `out` for covariance, `in` for contravariance.

## Engineering Notes

- Push constraints into APIs when they remove casts or runtime checks, but keep public generic signatures understandable.
- Use generic math and static abstract interface members for reusable numeric algorithms in modern .NET.
- Be cautious with arrays: array covariance exists for legacy reasons and can fail at runtime.

## Sources

- Microsoft - Generics in .NET - https://learn.microsoft.com/en-us/dotnet/standard/generics/
- Microsoft - Constraints on type parameters - https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/constraints-on-type-parameters
- Microsoft - Variance in generic interfaces - https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/variance-in-generic-interfaces

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
