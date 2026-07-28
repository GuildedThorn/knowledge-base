---
summary: "Dependency injection separates object construction from behavior; the composition root wires concrete implementations at application startup."
status: active
tags: [reference, engineering, architecture, dependency-injection]
private: false
---

# Dependency Injection and Composition Root

## Purpose

Dependency injection separates object construction from behavior; the composition root wires concrete implementations at application startup.

## Core Model

- Constructor injection makes dependencies explicit and testable.
- The composition root is the outermost place where concrete graphs are built.
- Service locator hides dependencies and moves failures from construction to runtime.

## Engineering Notes

- Keep DI containers at the edge; domain code should not know about the container.
- Prefer explicit lifetimes and watch captive dependencies such as singleton services holding scoped objects.
- Use factories for runtime parameters and expensive/on-demand object creation.

## Sources

- Martin Fowler - Inversion of Control Containers and DI - https://martinfowler.com/articles/injection.html
- Microsoft - Dependency injection in .NET - https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection
- ASP.NET Core dependency injection - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection

## Related

- [Software Architecture - Index](kb://06-reference-engineering-software-architecture-software-architecture-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
