---
summary: "Log analytics stack pairing Elasticsearch storage and search with Logstash/Beats ingestion and Kibana visualization."
status: active
tags: [reference, engineering, sre, logging, search, kibana]
private: false
---

# Elastic Stack (ELK)

## Purpose

Log analytics stack pairing Elasticsearch storage and search with Logstash/Beats ingestion and Kibana visualization.

## Ingestion

- Beats are lightweight per-host shippers: Filebeat for logs, Metricbeat for metrics, Packetbeat, Winlogbeat, and others.
- Logstash is the heavier ETL layer, using input/filter/output plugins (notably grok, mutate, and date) to parse and enrich events.
- Ingest pipelines inside Elasticsearch can perform many transforms without a separate Logstash tier.

## Storage and Search

- Elasticsearch stores documents in indices backed by Lucene inverted indexes, enabling fast full-text and term queries.
- Mappings define field types; text fields are analyzed and tokenized, while keyword fields are exact-match and aggregatable.
- Indices are sharded and replicated across nodes for horizontal scale and availability, with index lifecycle management aging data through hot/warm/cold/frozen tiers.

## Visualization

- Kibana provides discover search, dashboards, and Lens visualizations over Elasticsearch data.
- KQL and the query DSL drive filtering; aggregations power charts, histograms, and metric panels.

## Sources

- Elastic Stack Documentation - https://www.elastic.co/guide/index.html
- Elasticsearch Reference - https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

## Related

- [Observability and SRE - Index](kb://06-reference-engineering-observability-sre-observability-sre-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
