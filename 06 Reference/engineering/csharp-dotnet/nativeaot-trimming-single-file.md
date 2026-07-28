---
summary: "Modern .NET deployment can publish trimmed, single-file, or NativeAOT binaries, but dynamic features must be designed for static analysis."
status: active
tags: [reference, engineering, dotnet, deployment]
private: false
---

# NativeAOT, Trimming, and Single-File Deployment

## Purpose

Modern .NET deployment can publish trimmed, single-file, or NativeAOT binaries, but dynamic features must be designed for static analysis.

## Core Model

- Trimming removes code the linker believes is unused; reflection-heavy code needs annotations or source-generated alternatives.
- Single-file bundling packages app artifacts into one executable with extraction and compatibility tradeoffs.
- NativeAOT compiles ahead of time to native code, reducing startup and deployment dependencies while limiting some dynamic runtime features.

## Engineering Notes

- Test published artifacts, not just debug builds; trim/AOT failures often appear only after publish.
- Prefer source-generated serializers and DI patterns when trimming or AOT is a requirement.
- Document runtime identifiers, self-contained mode, invariant globalization, and platform-specific native dependencies.

## Sources

- Microsoft - Native AOT deployment - https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/
- Microsoft - Trim self-contained deployments - https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trim-self-contained
- Microsoft - Single-file deployment - https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/overview

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
