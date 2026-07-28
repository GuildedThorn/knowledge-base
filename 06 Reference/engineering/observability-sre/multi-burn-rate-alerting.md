---
summary: "SLO-based alerting that combines fast and slow burn-rate windows to page on real budget consumption with low false positives."
status: active
tags: [reference, engineering, sre, alerting, slo, burn-rate]
private: false
---

# Multi-Window Multi-Burn-Rate Alerting

## Purpose

SLO-based alerting that combines fast and slow burn-rate windows to page on real budget consumption with low false positives.

## Burn Rate Math

- Burn rate is how fast an incident consumes the error budget relative to nominal: a burn rate of 1 exhausts the whole budget exactly over the SLO window; a burn rate of 14.4 exhausts it in 1/14.4 of the window.
- For a 30-day window, a 2% budget spend in 1 hour corresponds to a burn rate of about 14.4; alerting on that catches fast-burning outages quickly.
- Choosing an alert threshold means picking a budget fraction to spend and a detection window; longer windows detect slow burns, shorter windows detect fast ones.

## Window Pairing

- A single long window reacts too slowly to sharp outages; a single short window is noisy and fires on transient blips.
- The Google SRE Workbook recommends pairing a long window (for significance) with a short window (for a fast reset), and requiring both to breach before paging.
- Typical multi-tier setup: 2%-budget/1h (short 5m) as a page, 5%-budget/6h as a page, 10%-budget/3d as a ticket — escalating severity by burn speed.
- The short "reset" window ensures the alert clears promptly once error rates recover, avoiding lingering pages.

## Tradeoffs

- Multi-burn-rate improves precision (fewer false pages) and recall (catches both fast and slow burns) versus static threshold alerting.
- Complexity is higher: multiple recording rules and thresholds per SLO must be maintained.
- Precision vs recall is tuned by the budget-fraction and window choices for each tier.

## Sources

- SRE Workbook: Alerting on SLOs - https://sre.google/workbook/alerting-on-slos/

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
