---
summary: "Data dictionary for the autonomous-systems attack tables (autonomous vehicles, robotics) in the AI Agent Cybersecurity 2026 dataset."
status: active
tags: [datasets]
---

# Autonomous Systems Tables — AI Agent Cybersecurity 2026

The `data/autonomous_systems/` group: two curated catalogs of attacks on cyber-physical AI systems — autonomous vehicles and robotics. Reference tables of 10–12 rows. Part of [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|AI Agent Cybersecurity Dataset 2026]].

## autonomous_vehicle_attacks.csv — 12 rows

`data/autonomous_systems/autonomous_vehicle_attacks.csv` · one row = an attack on an AV system or sensor (e.g. adversarial stop-sign against object detection).

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. AV-001) |
| attack_name | Name |
| attack_type | Class |
| target_system | System/vendor (e.g. Tesla Autopilot, Waymo) |
| target_component | Component hit (e.g. camera object detector) |
| attack_method | How it is carried out |
| impact | Consequence |
| severity_score | 0–10 severity |
| risk_level | Critical/High/… |
| ai_model | Model targeted |
| attack_success_rate | ASR (0–1) |
| real_world_ref | Documented case |
| year | Year |
| mitigation | Defense |
| source | Citation |

## robotics_security.csv — 10 rows

`data/autonomous_systems/robotics_security.csv` · one row = a robotics/cyber-physical attack on a robot system or controller (e.g. ROS topic injection). Same shape as the AV table minus `ai_model`/`attack_success_rate`.

| Column | Description |
|---|---|
| attack_id | Stable ID (e.g. ROB-001) |
| attack_name | Name |
| attack_type | Class |
| target_system | System (e.g. ROS 1) |
| target_component | Component (e.g. ROS topic / message bus) |
| attack_method | Method |
| impact | Consequence |
| severity_score | 0–10 severity |
| risk_level | Critical/High/… |
| real_world_ref | Documented case |
| year | Year |
| mitigation | Defense |
| source | Citation |

## Related

- [[12 Datasets/AI Agent Cybersecurity 2026/Dataset Index|Dataset Index]]
- [[12 Datasets/AI Agent Cybersecurity 2026/Core Tables|Core Tables]]
