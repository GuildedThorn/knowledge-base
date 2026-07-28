---
summary: "Using the Task Scheduler to run attacker payloads on triggers, at logon, or on a recurring schedule."
status: active
tags: [security, techniques, scheduled-task, persistence, execution]
private: false
---

# Windows Scheduled Task Persistence

## Purpose

Using the Task Scheduler to run attacker payloads on triggers, at logon, or on a recurring schedule.

## How It Works

- Tasks are created via the `schtasks.exe` CLI, PowerShell `ScheduledTasks` cmdlets, or directly through the Task Scheduler COM interface (`ITaskService`).
- Trigger types include at logon, at startup, on a time interval, on idle, and on specific event-log events, giving flexible re-execution.
- A task can be registered to run as `SYSTEM` or as a specific user, and admin rights allow creating tasks in the all-users store.
- Task definitions live as XML under `C:\Windows\System32\Tasks` with matching entries in the registry `TaskCache` tree.
- Hidden tasks can be crafted by manipulating the `SD` (security descriptor) registry value so they do not list in the GUI.

## Detection Notes

- Enable and monitor the Microsoft-Windows-TaskScheduler/Operational log; Event ID 106 (registered), 140 (updated), 200/201 (action run).
- Security Event ID 4698 records new scheduled-task creation with the task XML.
- Compare on-disk `Tasks` files against registry `TaskCache` to spot GUI-hidden tasks.
- Flag tasks that launch scripting hosts, LOLBins, or binaries from user-writable paths.

## Sources

- MITRE ATT&CK T1053.005 - https://attack.mitre.org/techniques/T1053/005/
- Microsoft Task Scheduler - https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page

## Related

- [Techniques - Index](kb://11-security-techniques-techniques-index)
- [Research Library](kb://11-security-research-library)
- [Security Map](kb://01-maps-security-map)
- [11-security](kb://hub-11-security)
