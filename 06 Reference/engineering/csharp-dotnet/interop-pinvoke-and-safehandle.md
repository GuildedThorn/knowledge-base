---
summary: ".NET interop bridges managed code to native libraries; SafeHandle, marshaling, and lifetime ownership decide whether it stays reliable."
status: active
tags: [reference, engineering, dotnet, interop]
private: false
---

# Interop, P/Invoke, and SafeHandle

## Purpose

.NET interop bridges managed code to native libraries; SafeHandle, marshaling, and lifetime ownership decide whether it stays reliable.

## Core Model

- P/Invoke calls unmanaged exports through generated stubs that marshal managed types to native representations.
- SafeHandle wraps OS/native handles so release is reliable even under exceptions and finalization.
- String encoding, struct layout, calling convention, ownership, and buffer lifetime are common bug surfaces.

## Engineering Notes

- Prefer built-in libraries first; native interop should isolate unsafe code behind a small reviewed API.
- Use SafeHandle for handles and document who allocates/frees memory across the boundary.
- Write platform tests for Linux/macOS/Windows if the library has different ABIs or names.

## Sources

- Microsoft - Native interoperability - https://learn.microsoft.com/en-us/dotnet/standard/native-interop/
- Microsoft - P/Invoke - https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke
- Microsoft - SafeHandle - https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.safehandle

## Related

- [C# and .NET - Index](kb://06-reference-engineering-csharp-dotnet-csharp-dotnet-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
