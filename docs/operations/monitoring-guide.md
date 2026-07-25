# Monitoring Guide

There is no daemon, service endpoint, metrics exporter, structured event stream, or hosted runtime to monitor. Operational feedback is currently terminal output, process exit code, filesystem results, and the optional JSONL operation log.

For real executions, retain the log with the source data and inspect for `ERROR` output and destination collisions. Do not treat a zero process exit code as proof that every operation succeeded; `Executor.run` reports counts in output and catches per-operation errors.

Future observability should define structured output and a machine-checkable summary (`OPS-002`).
