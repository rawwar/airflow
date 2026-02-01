# 90 Metrics

## Overview

Airflow metrics provide deep visibility into scheduler, executor, DAG, and task performance. Airflow 3.x exposes metrics via StatsD and OpenTelemetry, enabling integration with Prometheus, Grafana, Datadog, and other observability platforms.

## Airflow 3.x Notes
- OpenTelemetry support enhanced
- StatsD remains primary metrics backend
- New metrics for triggerer component
- Asset-related metrics added
- Improved executor metrics

---

# 90.1 Metrics Fundamentals

## Overview
Understanding Airflow's metrics system and configuration.

## Tasks

### - [ ] 90.1.1 Metrics Architecture Overview
Filename: `90_01_01_metrics_architecture.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand how Airflow emits metrics

- [ ] StatsD protocol basics
- [ ] Metrics types: counters, gauges, timers
- [ ] Airflow components that emit metrics
- [ ] Metrics naming conventions

**Expected Behavior**: Clear understanding of metrics flow

---

### - [ ] 90.1.2 Enabling StatsD Metrics
Filename: `90_01_02_enabling_statsd.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure StatsD metrics export

- [ ] statsd_on configuration
- [ ] statsd_host and statsd_port settings
- [ ] statsd_prefix configuration
- [ ] Verify metrics emission

**Expected Behavior**: Metrics sent to StatsD

---

### - [ ] 90.1.3 OpenTelemetry Metrics Setup
Filename: `90_01_03_opentelemetry_setup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure OpenTelemetry metrics

- [ ] otel_on configuration
- [ ] OTEL exporter setup
- [ ] Resource attributes
- [ ] Service name configuration

**Expected Behavior**: Metrics exported via OTEL

---

### - [ ] 90.1.4 Custom Metrics Prefix
Filename: `90_01_04_custom_metrics_prefix.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Customize metrics naming

- [ ] statsd_prefix for namespacing
- [ ] Environment-specific prefixes
- [ ] Multi-cluster metrics isolation
- [ ] Metrics aggregation patterns

**Expected Behavior**: Organized metrics namespace

---

### - [ ] 90.1.5 Metrics Sampling and Performance
Filename: `90_01_05_metrics_sampling.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Optimize metrics collection overhead

- [ ] Sample rate configuration
- [ ] High-volume metrics optimization
- [ ] Metrics buffering
- [ ] Performance impact analysis

**Expected Behavior**: Efficient metrics collection

---

# 90.2 Scheduler Metrics

## Overview
Metrics specific to the Airflow scheduler component.

## Tasks

### - [ ] 90.2.1 Scheduler Heartbeat Metrics
Filename: `90_02_01_scheduler_heartbeat.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Monitor scheduler health via heartbeat

- [ ] scheduler_heartbeat gauge
- [ ] Heartbeat interval monitoring
- [ ] Detecting scheduler failures
- [ ] Multi-scheduler environments

**Expected Behavior**: Scheduler health visible

---

### - [ ] 90.2.2 DAG Parsing Metrics
Filename: `90_02_02_dag_parsing_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track DAG file parsing performance

- [ ] dag_processing.total_parse_time
- [ ] dag_processing.import_errors
- [ ] Per-file parsing duration
- [ ] Identifying slow DAG files

**Expected Behavior**: Parsing bottlenecks identified

---

### - [ ] 90.2.3 Task Scheduling Latency
Filename: `90_02_03_task_scheduling_latency.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Measure time from scheduled to queued

- [ ] scheduler.tasks.scheduled counter
- [ ] Queuing delay metrics
- [ ] Priority queue analysis
- [ ] Scheduling throughput

**Expected Behavior**: Scheduling performance measured

---

### - [ ] 90.2.4 Pool and Slot Metrics
Filename: `90_02_04_pool_slot_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor pool utilization

- [ ] pool.open_slots gauge
- [ ] pool.used_slots gauge
- [ ] Pool saturation detection
- [ ] Capacity planning data

**Expected Behavior**: Pool usage visible

---

### - [ ] 90.2.5 Zombie Task Metrics
Filename: `90_02_05_zombie_task_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track zombie task detection

- [ ] scheduler.zombie_tasks.killed counter
- [ ] Zombie detection frequency
- [ ] Root cause correlation
- [ ] Infrastructure health indicators

**Expected Behavior**: Zombie issues tracked

---

# 90.3 Executor Metrics

## Overview
Metrics for various executor implementations.

## Tasks

### - [ ] 90.3.1 Executor Queue Metrics
Filename: `90_03_01_executor_queue_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor executor queue depth

- [ ] executor.queued_tasks gauge
- [ ] executor.running_tasks gauge
- [ ] Queue growth trends
- [ ] Executor capacity analysis

**Expected Behavior**: Queue visibility achieved

---

### - [ ] 90.3.2 Celery Executor Metrics
Filename: `90_03_02_celery_executor_metrics.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Celery-specific metrics

- [ ] celery.task_timeout_error counter
- [ ] Worker pool metrics
- [ ] Broker connection metrics
- [ ] Task routing metrics

**Expected Behavior**: Celery health monitored

---

### - [ ] 90.3.3 Kubernetes Executor Metrics
Filename: `90_03_03_kubernetes_executor_metrics.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: K8s executor pod metrics

- [ ] Pod launch latency
- [ ] Pod success/failure rates
- [ ] Resource request metrics
- [ ] Namespace utilization

**Expected Behavior**: K8s executor visible

---

### - [ ] 90.3.4 Local Executor Metrics
Filename: `90_03_04_local_executor_metrics.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Local executor process metrics

- [ ] Process pool utilization
- [ ] Parallelism usage
- [ ] Memory consumption
- [ ] Task throughput

**Expected Behavior**: Local executor monitored

---

### - [ ] 90.3.5 Triggerer Metrics
Filename: `90_03_05_triggerer_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Monitor triggerer component

- [ ] triggerer.triggers.running gauge
- [ ] Trigger completion rate
- [ ] Async loop performance
- [ ] Deferred task metrics

**Expected Behavior**: Triggerer health visible

---

# 90.4 Task and DAG Metrics

## Overview
Metrics at the task and DAG level.

## Tasks

### - [ ] 90.4.1 Task Duration Metrics
Filename: `90_04_01_task_duration_metrics.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Track task execution times

- [ ] ti.duration timer
- [ ] Per-task type duration
- [ ] Duration trends over time
- [ ] Outlier detection

**Expected Behavior**: Task duration tracked

---

### - [ ] 90.4.2 Task State Metrics
Filename: `90_04_02_task_state_metrics.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Track task state transitions

- [ ] ti.successes counter
- [ ] ti.failures counter
- [ ] State transition counts
- [ ] Success rate calculation

**Expected Behavior**: Task states counted

---

### - [ ] 90.4.3 DAG Run Duration Metrics
Filename: `90_04_03_dagrun_duration_metrics.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Track DAG run execution time

- [ ] dagrun.duration timer
- [ ] Critical path analysis
- [ ] SLA adherence metrics
- [ ] Duration by run_type

**Expected Behavior**: DAG run timing visible

---

### - [ ] 90.4.4 Custom Task Metrics
Filename: `90_04_04_custom_task_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Emit custom metrics from tasks

- [ ] StatsD client in tasks
- [ ] Business metrics emission
- [ ] Metric naming conventions
- [ ] Context-aware metrics

**Expected Behavior**: Custom metrics emitted

---

### - [ ] 90.4.5 Asset Metrics
Filename: `90_04_05_asset_metrics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track Asset (Dataset) operations

- [ ] Asset update events
- [ ] Consumer trigger metrics
- [ ] Asset freshness metrics
- [ ] Cross-DAG asset tracking

**Expected Behavior**: Asset flow visible

---

# 90.5 Metrics Integration

## Overview
Integrating Airflow metrics with external systems.

## Tasks

### - [ ] 90.5.1 Prometheus Integration
Filename: `90_05_01_prometheus_integration.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Export metrics to Prometheus

- [ ] StatsD exporter for Prometheus
- [ ] Metric type mapping
- [ ] Recording rules
- [ ] Prometheus query examples

**Expected Behavior**: Metrics in Prometheus

---

### - [ ] 90.5.2 Datadog Integration
Filename: `90_05_02_datadog_integration.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Send metrics to Datadog

- [ ] DogStatsD configuration
- [ ] Custom tags
- [ ] Datadog dashboard templates
- [ ] APM correlation

**Expected Behavior**: Metrics in Datadog

---

### - [ ] 90.5.3 CloudWatch Metrics
Filename: `90_05_03_cloudwatch_metrics.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Export to AWS CloudWatch

- [ ] CloudWatch agent setup
- [ ] Custom dimensions
- [ ] Metric filters
- [ ] Alarm integration

**Expected Behavior**: Metrics in CloudWatch

---

### - [ ] 90.5.4 InfluxDB Integration
Filename: `90_05_04_influxdb_integration.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Store metrics in InfluxDB

- [ ] Telegraf StatsD input
- [ ] InfluxDB bucket setup
- [ ] Retention policies
- [ ] Flux queries

**Expected Behavior**: Time series stored

---

### - [ ] 90.5.5 Metrics Aggregation and Rollup
Filename: `90_05_05_metrics_aggregation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Aggregate metrics for analysis

- [ ] Pre-aggregation strategies
- [ ] Rollup configurations
- [ ] High-cardinality handling
- [ ] Cross-environment metrics

**Expected Behavior**: Scalable metrics pipeline

---

# 90.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding metrics implementation pitfalls.

## Tasks

### - [ ] 90.6.1 High Cardinality Metrics
Filename: `90_06_01_high_cardinality.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Manage metric cardinality

- [ ] Too many label values
- [ ] Memory issues
- [ ] Cost explosion
- [ ] Cardinality limits

**Expected Behavior**: Cardinality controlled

---

### - [ ] 90.6.2 Missing Critical Metrics
Filename: `90_06_02_missing_critical.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Capture essential metrics

- [ ] Blind spots
- [ ] No alerting data
- [ ] Troubleshooting gaps
- [ ] Required metrics list

**Expected Behavior**: Critical metrics present

---

### - [ ] 90.6.3 Metrics Without Context
Filename: `90_06_03_metrics_without_context.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Add meaningful labels

- [ ] Unlabeled metrics
- [ ] Hard to filter
- [ ] Missing dimensions
- [ ] Label strategy

**Expected Behavior**: Metrics contextualized

---

### - [ ] 90.6.4 Ignoring Metric Retention
Filename: `90_06_04_ignoring_retention.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Plan metric retention

- [ ] Unlimited storage
- [ ] Cost growth
- [ ] Query performance
- [ ] Retention policies

**Expected Behavior**: Retention configured

---

### - [ ] 90.6.5 Metrics as Only Observability
Filename: `90_06_05_metrics_only.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Complete observability

- [ ] Missing logs
- [ ] No traces
- [ ] Correlation gaps
- [ ] Three pillars approach

**Expected Behavior**: Full observability

---

# 90.7 Testing Metrics

## Overview
Testing metrics implementations.

## Tasks

### - [ ] 90.7.1 Metric Emission Testing
Filename: `90_07_01_emission_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify metrics emitted

- [ ] Capture emitted metrics
- [ ] Validate metric names
- [ ] Check label values
- [ ] Value assertions

**Expected Behavior**: Metrics emission verified

---

### - [ ] 90.7.2 StatsD Mock Testing
Filename: `90_07_02_statsd_mock.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test without real backend

- [ ] Mock StatsD server
- [ ] Capture sent metrics
- [ ] Validate protocol
- [ ] Unit test integration

**Expected Behavior**: StatsD mocked

---

### - [ ] 90.7.3 Metric Accuracy Testing
Filename: `90_07_03_accuracy_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate metric values

- [ ] Known scenarios
- [ ] Expected values
- [ ] Counter accuracy
- [ ] Timer precision

**Expected Behavior**: Metrics accurate

---

### - [ ] 90.7.4 Dashboard Query Testing
Filename: `90_07_04_dashboard_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test dashboard queries

- [ ] PromQL validation
- [ ] Query performance
- [ ] Result accuracy
- [ ] Alert rules testing

**Expected Behavior**: Queries tested

---

### - [ ] 90.7.5 Metrics Pipeline Testing
Filename: `90_07_05_pipeline_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test full pipeline

- [ ] End-to-end flow
- [ ] Latency measurement
- [ ] Data completeness
- [ ] Integration testing

**Expected Behavior**: Pipeline verified

---

# 90.8 Performance Optimization

## Overview
Optimizing metrics collection and storage.

## Tasks

### - [ ] 90.8.1 Metric Sampling Strategies
Filename: `90_08_01_sampling_strategies.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Sample high-volume metrics

- [ ] Sample rate tuning
- [ ] Statistical accuracy
- [ ] Volume reduction
- [ ] Important metrics exemption

**Expected Behavior**: Sampling optimized

---

### - [ ] 90.8.2 Metric Aggregation
Filename: `90_08_02_metric_aggregation.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Pre-aggregate metrics

- [ ] Client-side aggregation
- [ ] Reduce network traffic
- [ ] Histogram buckets
- [ ] Summary percentiles

**Expected Behavior**: Aggregation efficient

---

### - [ ] 90.8.3 Storage Optimization
Filename: `90_08_03_storage_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize metric storage

- [ ] Compression settings
- [ ] Retention tiering
- [ ] Downsampling
- [ ] Cost management

**Expected Behavior**: Storage optimized

---

### - [ ] 90.8.4 Query Optimization
Filename: `90_08_04_query_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Fast metric queries

- [ ] Recording rules
- [ ] Query caching
- [ ] Time range limits
- [ ] Efficient PromQL

**Expected Behavior**: Queries fast

---

### - [ ] 90.8.5 Collection Overhead Reduction
Filename: `90_08_05_overhead_reduction.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Minimize collection impact

- [ ] Async emission
- [ ] Batching
- [ ] Buffer sizing
- [ ] CPU/memory impact

**Expected Behavior**: Overhead minimal

---

# 90.9 Debugging Metrics Issues

## Overview
Troubleshooting metrics problems.

## Tasks

### - [ ] 90.9.1 Missing Metrics Debugging
Filename: `90_09_01_missing_metrics.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Find missing metrics

- [ ] Configuration check
- [ ] Network issues
- [ ] Backend problems
- [ ] Filter verification

**Expected Behavior**: Metrics appearing

---

### - [ ] 90.9.2 Incorrect Values Debugging
Filename: `90_09_02_incorrect_values.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug wrong metric values

- [ ] Counter resets
- [ ] Rate calculation
- [ ] Aggregation issues
- [ ] Timestamp problems

**Expected Behavior**: Values correct

---

### - [ ] 90.9.3 Backend Connection Issues
Filename: `90_09_03_backend_connection.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug backend connectivity

- [ ] StatsD connection
- [ ] Network firewall
- [ ] Port configuration
- [ ] Protocol issues

**Expected Behavior**: Backend connected

---

### - [ ] 90.9.4 Cardinality Explosion Diagnosis
Filename: `90_09_04_cardinality_explosion.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug cardinality issues

- [ ] Identify high cardinality
- [ ] Label analysis
- [ ] Memory impact
- [ ] Remediation

**Expected Behavior**: Cardinality controlled

---

### - [ ] 90.9.5 Metric Lag Debugging
Filename: `90_09_05_metric_lag.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug delayed metrics

- [ ] Collection lag
- [ ] Network latency
- [ ] Processing delay
- [ ] Timestamp skew

**Expected Behavior**: Metrics timely

---

# 90.10 Real-World Examples

## Overview
Production metrics implementations.

## Tasks

### - [ ] 90.10.1 Complete Prometheus Setup
Filename: `90_10_01_prometheus_setup.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Full Prometheus integration

- [ ] StatsD exporter
- [ ] Recording rules
- [ ] Alert rules
- [ ] Grafana dashboards

**Expected Behavior**: Prometheus complete

---

### - [ ] 90.10.2 Datadog Full Integration
Filename: `90_10_02_datadog_integration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Complete Datadog setup

- [ ] DogStatsD config
- [ ] Custom metrics
- [ ] Dashboards
- [ ] APM integration

**Expected Behavior**: Datadog integrated

---

### - [ ] 90.10.3 SLA Monitoring Dashboard
Filename: `90_10_03_sla_monitoring.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: SLA tracking metrics

- [ ] SLA metrics definition
- [ ] Compliance tracking
- [ ] Violation alerting
- [ ] Reporting dashboards

**Expected Behavior**: SLA monitored

---

### - [ ] 90.10.4 Cost Attribution Metrics
Filename: `90_10_04_cost_attribution.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Track resource costs

- [ ] Resource usage metrics
- [ ] Team attribution
- [ ] Cost calculation
- [ ] Budget alerting

**Expected Behavior**: Costs tracked

---

### - [ ] 90.10.5 Custom Business Metrics
Filename: `90_10_05_business_metrics.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Business-level metrics

- [ ] Pipeline success rates
- [ ] Data freshness
- [ ] Processing volumes
- [ ] Business KPIs

**Expected Behavior**: Business metrics tracked

---

# Summary

## Topic Completion Checklist
- [ ] Metrics fundamentals explained
- [ ] Scheduler metrics covered
- [ ] Executor metrics documented
- [ ] Task/DAG metrics included
- [ ] Integration patterns provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 19: Logging Monitoring (logging complement)
- Section 91: Alerting (metrics-based alerts)
- Section 92: Dashboards (visualization)

## Notes for Implementation
- Test with StatsD receiver
- Show OpenTelemetry alternative
- Include metric naming best practices
- Demonstrate cardinality management
