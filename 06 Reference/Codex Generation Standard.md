## Purpose

Define a compact operating standard for generating new vault content with minimal token waste, clean discovery, and consistent formatting.

## Primary Goal

Turn rough input into stable notes with:

- minimal searching
- minimal repetition
- one topic per note
- consistent section structure
- correct folder placement
- useful links to existing maps and related notes

## Token Discipline

- Search narrow before reading broad.
- Read only the files directly relevant to the request.
- Prefer maps, existing related notes, and exact-path files before scanning whole folders.
- Do not restate the user’s text unless it needs cleanup or normalization.
- Do not generate long explanations when a direct note is enough.
- Avoid duplicate summaries across multiple notes.

## Search Workflow

1. Identify the target topic.
2. Check the most relevant map note first.
3. Search for an existing note with `rg --files`.
4. Read only the closest matching notes.
5. If the topic depends on config or source files, read only the files tied to that topic.
6. Generate or update the note.
7. Add or fix links in the relevant map note only if needed.

## Source Priority

Use sources in this order:

1. user-provided text in the current message
2. inbox note content
3. existing note in the vault
4. directly related config or project files
5. map notes for placement and linking

## Folder Placement Rules

- `00 Inbox`: raw capture only
- `02 Systems`: OS, configuration, auth, secrets, deployment workflow
- `03 Devices`: machine or hardware-specific notes
- `04 Software`: app-specific notes
- `05 Network`: firewall, DNS, routing, VPN, remote access, serial, recovery
- `06 Reference`: reusable standards, commands, templates, cheatsheets
- `07 Projects`: project architecture, implementation, deployment, operations
- `08 Improvements`: unfinished work, cleanup, follow-up

## Note Creation Rules

- One note per topic.
- Prefer updating an existing note over making a duplicate.
- Use a clear, searchable filename.
- Link to the most relevant map note.
- Add only sections that are justified by the content.
- Do not preserve messy phrasing if the meaning is clear.
- Separate current state from planned scope.

## Standard Note Shapes

### Device Note

- `## Purpose`
- `## Identity`
- `## Hardware Specs`
- `## NixOS-Specific Notes` or `## System Notes`
- `## Hosted Services` or `## Workload Notes` if relevant
- `## Related`

### System Note

- `## Purpose`
- `## Scope`
- `## Current State` or `## Layout`
- `## Workflow`, `## Operations`, or `## Composition`
- `## Related`

### Network Note

- `## Purpose`
- `## Current Known State`
- `## Tasks`, `## Questions To Resolve`, or `## Validation` as needed
- `## Related`

### Project Note

- `## Purpose`
- `## Summary`
- `## Architecture`, `## Stack`, or `## API`
- `## Deployment` or `## Runtime Dependencies`
- `## Related`

### Improvement Note

- `## Purpose`
- `## Current State`
- `## Tasks`
- `## Related`

## Inbox-to-Note Workflow

When generating from `00 Inbox`:

1. extract the actual topic
2. drop chatter, duplicates, and temporary phrasing
3. split multi-topic notes into separate destination notes if needed
4. convert action items into `08 Improvements` only if they are unresolved
5. move stable knowledge into its permanent folder

## User-Text-to-Note Workflow

When generating directly from user text:

1. infer the note type
2. normalize names, capitalization, and units
3. mark anything speculative as planned or unverified
4. do not invent missing facts
5. cross-reference existing notes when a host, device, or project already exists

## Style Rules

- Start directly with useful content.
- Use short sections.
- Use bullets for facts, not paragraphs of filler.
- Prefer exact hostnames, paths, ports, service names, and file paths.
- Keep prose plain and technical.

## Do Not

- create duplicate notes for the same topic
- leave placeholder links pretending a note exists
- mix current state with future ideas without labeling them
- expand scope beyond the user request unless the missing context is directly necessary
- scan unrelated folders just because they exist

## Success Condition

A generated note is correct when it is:

- in the right folder
- named clearly
- linked to the right map
- free of obvious duplication
- concise but useful
- based only on relevant source material

## Related

- [[00 Inbox/Inbox Processing|Inbox Processing]]
- [[90 Templates/Inbox Note Template|Inbox Note Template]]
- [[90 Templates/Setup Note Template|Setup Note Template]]
- [[01 Maps/Reference Map|Reference Map]]
