---
summary: "MapReduce popularized large-scale batch processing by decomposing jobs into map, shuffle/sort, and reduce phases over distributed storage."
status: active
tags: [reference, engineering, distributed-systems, batch-processing]
private: false
---

# MapReduce Dataflow Model

## Purpose

MapReduce popularized large-scale batch processing by decomposing jobs into map, shuffle/sort, and reduce phases over distributed storage.

## Core Model

- Map tasks process input splits independently and emit intermediate key/value pairs.
- Shuffle groups values by key and moves data across the cluster.
- Reduce tasks aggregate grouped values and write output back to distributed storage.

## Engineering Notes

- MapReduce is a durable batch model, not a low-latency stream processor.
- Shuffle is usually the expensive phase; key skew can dominate job runtime.
- Modern systems such as Spark and Flink generalize the model but still face data locality, shuffle, and fault-recovery tradeoffs.

## Sources

- Google MapReduce paper - https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/
- Apache Hadoop MapReduce - https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
- Apache Spark documentation - https://spark.apache.org/docs/latest/

## Related

- [Systems and Distributed Computing - Index](kb://06-reference-engineering-systems-distributed-systems-distributed-index)
- [Engineering Research Library](kb://06-reference-engineering-research-library)
- [Reference Map](kb://01-maps-reference-map)
- [06-reference](kb://hub-06-reference)
