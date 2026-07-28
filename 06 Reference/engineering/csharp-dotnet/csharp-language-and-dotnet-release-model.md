---
summary: "C# evolves with the .NET SDK; language features, runtime libraries, and deployment targets should be pinned together in project documentation."
status: active
tags: [reference, engineering, csharp, dotnet]
private: false
---

# C# Language and .NET Release Model

## Purpose

C# evolves with the .NET SDK; language features, runtime libraries, and deployment targets should be pinned together in project documentation.

## Core Model

- The C# compiler ships with the .NET SDK, so language availability follows the SDK selected by global.json, project TFM, and tooling.
- Target framework monikers control library/runtime compatibility; language version can be explicit but should usually track the target framework.
- .NET's annual release cadence alternates support windows; LTS choices matter for production platform planning.

## Engineering Notes

- Record SDK version, target framework, nullable mode, implicit usings, and LangVersion in repo setup notes.
- Avoid adopting preview language/runtime features in long-lived services unless the deployment platform is pinned.
- When upgrading, test analyzers, source generators, trimming, NativeAOT, and package compatibility together.

## Sources

- Microsoft - C# language versioning - https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/configure-language-version
- Microsoft - .NET release policies - https://learn.microsoft.com/en-us/dotnet/core/releases-and-support
- Microsoft - What's new in .NET - https://learn.microsoft.com/en-us/dotnet/core/whats-new/

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
