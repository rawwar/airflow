# 59 Data Intervals

## Overview
Deep understanding of Airflow's data interval model, replacing the older execution_date paradigm.

---

# 59.1 Data Interval Concepts

### - [ ] 59.1.1 What are Data Intervals
Filename: `59_01_01_data_interval_basics.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] data_interval_start, data_interval_end
- [ ] Represents period DAG run covers
- [ ] vs execution_date model
- [ ] Benefits of interval model

### - [ ] 59.1.2 logical_date vs execution_date
Filename: `59_01_02_logical_vs_execution.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] logical_date is new standard
- [ ] execution_date deprecated
- [ ] Migration path
- [ ] Compatibility considerations

### - [ ] 59.1.3 Interval Boundaries
Filename: `59_01_03_interval_boundaries.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Start inclusive, end exclusive
- [ ] No gaps between intervals
- [ ] Adjacent intervals
- [ ] Edge cases

### - [ ] 59.1.4 Accessing Data Intervals
Filename: `59_01_04_accessing_intervals.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] context['data_interval_start']
- [ ] context['data_interval_end']
- [ ] Template variables
- [ ] Jinja macros

### - [ ] 59.1.5 Data Interval Timing
Filename: `59_01_05_interval_timing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Run after interval ends
- [ ] Processing historical data
- [ ] Real-time considerations
- [ ] Schedule alignment

---

# 59.2 Working with Intervals

### - [ ] 59.2.1 Filtering Data by Interval
Filename: `59_02_01_filtering_data.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] SQL WHERE clauses
- [ ] API parameters
- [ ] File path patterns
- [ ] Partition selection

### - [ ] 59.2.2 Incremental Processing
Filename: `59_02_02_incremental_processing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Process only new data
- [ ] Use interval for delta
- [ ] Checkpoint patterns
- [ ] Recovery scenarios

### - [ ] 59.2.3 Templating with Intervals
Filename: `59_02_03_templating_intervals.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] {{ data_interval_start }}
- [ ] {{ data_interval_end }}
- [ ] Format conversions
- [ ] Common patterns

### - [ ] 59.2.4 Interval Arithmetic
Filename: `59_02_04_interval_arithmetic.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Add/subtract from intervals
- [ ] Previous/next intervals
- [ ] Duration calculations
- [ ] Timezone handling

### - [ ] 59.2.5 Custom Interval Logic
Filename: `59_02_05_custom_interval_logic.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Non-standard intervals
- [ ] Business logic intervals
- [ ] Fiscal periods
- [ ] Event-based intervals

---

# 59.3 Interval Patterns

### - [ ] 59.3.1 Daily Data Processing
Filename: `59_03_01_daily_processing.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Standard daily pattern
- [ ] Midnight boundaries
- [ ] Timezone considerations
- [ ] Late data handling

### - [ ] 59.3.2 Hourly Data Processing
Filename: `59_03_02_hourly_processing.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Hour boundaries
- [ ] Rolling windows
- [ ] Aggregation patterns
- [ ] High-frequency data

### - [ ] 59.3.3 Monthly/Yearly Intervals
Filename: `59_03_03_monthly_yearly.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Variable length months
- [ ] End-of-month logic
- [ ] Fiscal year alignment
- [ ] Quarter boundaries

### - [ ] 59.3.4 Overlapping Intervals
Filename: `59_03_04_overlapping.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Sliding windows
- [ ] Rolling averages
- [ ] Look-back processing
- [ ] Deduplication

### - [ ] 59.3.5 Non-Contiguous Intervals
Filename: `59_03_05_non_contiguous.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Skip certain periods
- [ ] Business hours only
- [ ] Market hours
- [ ] Custom schedules

---

# 59.4 Backfill and Catchup

### - [ ] 59.4.1 Catchup with Intervals
Filename: `59_04_01_catchup_intervals.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] catchup=True behavior
- [ ] Historical interval runs
- [ ] Order of execution
- [ ] Resource considerations

### - [ ] 59.4.2 Backfill Command
Filename: `59_04_02_backfill_command.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] airflow dags backfill
- [ ] Date range specification
- [ ] Interval alignment
- [ ] Reprocessing data

### - [ ] 59.4.3 Partial Backfills
Filename: `59_04_03_partial_backfill.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Specific intervals only
- [ ] Skip existing runs
- [ ] Clear and rerun
- [ ] Selective processing

### - [ ] 59.4.4 Backfill Performance
Filename: `59_04_04_backfill_performance.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Parallel backfills
- [ ] Resource management
- [ ] Progress monitoring
- [ ] Optimization

### - [ ] 59.4.5 Backfill Pitfalls
Filename: `59_04_05_backfill_pitfalls.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Data availability issues
- [ ] External dependency changes
- [ ] Schema evolution
- [ ] Idempotency requirements

---

# 59.5 Advanced Interval Topics

### - [ ] 59.5.1 External Trigger Intervals
Filename: `59_05_01_external_trigger.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Manual trigger intervals
- [ ] API trigger intervals
- [ ] Default vs explicit
- [ ] Custom interval for triggers

### - [ ] 59.5.2 Cross-DAG Interval Alignment
Filename: `59_05_02_cross_dag_alignment.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Same intervals across DAGs
- [ ] Different schedule coordination
- [ ] Asset-based alignment
- [ ] Sensor-based alignment

### - [ ] 59.5.3 Interval Metadata
Filename: `59_05_03_interval_metadata.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Store interval info
- [ ] Audit trail
- [ ] Data lineage
- [ ] Processing records

### - [ ] 59.5.4 Interval Debugging
Filename: `59_05_04_interval_debugging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Verify correct intervals
- [ ] Log interval values
- [ ] Test with specific intervals
- [ ] Troubleshooting

### - [ ] 59.5.5 Migration from execution_date
Filename: `59_05_05_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Update template variables
- [ ] Code migration
- [ ] Testing migration
- [ ] Compatibility layer

---

# 59.6 Advanced Interval Patterns

## Overview
Complex data interval handling patterns.

## Tasks

### - [ ] 59.6.1 Multi-Source Interval Alignment
Filename: `59_06_01_multi_source.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Different source schedules
- [ ] Alignment strategies
- [ ] Gap handling
- [ ] Consistency

### - [ ] 59.6.2 Interval-Based Partitioning
Filename: `59_06_02_partitioning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Partition by interval
- [ ] Storage optimization
- [ ] Query patterns
- [ ] Retention policies

### - [ ] 59.6.3 Late Data Handling
Filename: `59_06_03_late_data.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Data arriving after interval
- [ ] Reprocessing triggers
- [ ] Delta handling
- [ ] Alerting

### - [ ] 59.6.4 Interval Metadata Tracking
Filename: `59_06_04_metadata_tracking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Track processed intervals
- [ ] Audit logging
- [ ] Recovery support
- [ ] Lineage integration

### - [ ] 59.6.5 Custom Interval Logic
Filename: `59_06_05_custom_logic.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Business-specific intervals
- [ ] Complex calculations
- [ ] External calendar
- [ ] Implementation

---

# 59.7 Testing Data Intervals

## Overview
Testing data interval handling.

## Tasks

### - [ ] 59.7.1 Unit Testing Interval Logic
Filename: `59_07_01_unit_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test interval calculations
- [ ] Mock context
- [ ] Edge cases
- [ ] pytest patterns

### - [ ] 59.7.2 Integration Testing
Filename: `59_07_02_integration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test with data sources
- [ ] End-to-end verification
- [ ] Data consistency
- [ ] CI integration

### - [ ] 59.7.3 Testing Boundary Conditions
Filename: `59_07_03_boundaries.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Interval edges
- [ ] Off-by-one errors
- [ ] Inclusive/exclusive
- [ ] Test patterns

### - [ ] 59.7.4 Testing Backfill Scenarios
Filename: `59_07_04_backfill.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Historical data
- [ ] Sequential processing
- [ ] Data availability
- [ ] Performance

### - [ ] 59.7.5 Testing Cross-DAG Intervals
Filename: `59_07_05_cross_dag.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Aligned intervals
- [ ] Dependency verification
- [ ] Data consistency
- [ ] Mock patterns

---

# 59.8 Anti-Patterns

## Overview
Data interval anti-patterns to avoid.

## Tasks

### - [ ] 59.8.1 Ignoring Interval Boundaries
Filename: `59_08_01_ignoring_boundaries.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Processing wrong data
- [ ] Duplicate processing
- [ ] Missing data
- [ ] Correct patterns

### - [ ] 59.8.2 Hardcoded Date Ranges
Filename: `59_08_02_hardcoded_dates.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Static dates in code
- [ ] Maintenance burden
- [ ] Backfill issues
- [ ] Parameterized approach

### - [ ] 59.8.3 Timezone Mishandling
Filename: `59_08_03_timezone_mishandling.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Mixed timezones
- [ ] Conversion errors
- [ ] DST issues
- [ ] Best practices

### - [ ] 59.8.4 Assuming Interval Duration
Filename: `59_08_04_assuming_duration.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Variable intervals
- [ ] Month length issues
- [ ] Calendar assumptions
- [ ] Dynamic calculation

### - [ ] 59.8.5 Not Handling Gaps
Filename: `59_08_05_not_handling_gaps.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Missing intervals
- [ ] Recovery issues
- [ ] Data inconsistency
- [ ] Gap detection

---

# 59.9 Monitoring and Observability

## Overview
Monitoring data interval processing.

## Tasks

### - [ ] 59.9.1 Interval Processing Metrics
Filename: `59_09_01_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Processing duration
- [ ] Data volume per interval
- [ ] Success rates
- [ ] Latency tracking

### - [ ] 59.9.2 Interval Coverage Dashboard
Filename: `59_09_02_dashboard.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Processed intervals
- [ ] Gaps visualization
- [ ] Trend analysis
- [ ] Alerting integration

### - [ ] 59.9.3 Interval Anomaly Detection
Filename: `59_09_03_anomaly_detection.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Unusual intervals
- [ ] Data volume anomalies
- [ ] Processing time spikes
- [ ] Automated alerts

### - [ ] 59.9.4 Interval Audit Trail
Filename: `59_09_04_audit_trail.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Track processing history
- [ ] Compliance requirements
- [ ] Debugging support
- [ ] Data lineage

### - [ ] 59.9.5 SLA Monitoring
Filename: `59_09_05_sla_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Interval SLA tracking
- [ ] Deadline monitoring
- [ ] Early warning
- [ ] Escalation

---

# 59.10 Real-World Scenarios

## Overview
Production data interval patterns.

## Tasks

### - [ ] 59.10.1 Daily Data Pipeline
Filename: `59_10_01_daily_pipeline.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Standard daily processing
- [ ] Timezone handling
- [ ] Late data
- [ ] Reprocessing

### - [ ] 59.10.2 Hourly Streaming Integration
Filename: `59_10_02_hourly_streaming.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Micro-batch from stream
- [ ] Exactly-once semantics
- [ ] Ordering guarantees
- [ ] Performance

### - [ ] 59.10.3 Monthly Financial Reports
Filename: `59_10_03_monthly_financial.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Month-end processing
- [ ] Fiscal calendar
- [ ] Reconciliation
- [ ] Audit requirements

### - [ ] 59.10.4 Cross-Region Data Sync
Filename: `59_10_04_cross_region.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Multi-region intervals
- [ ] Timezone coordination
- [ ] Consistency
- [ ] Conflict resolution

### - [ ] 59.10.5 Machine Learning Feature Windows
Filename: `59_10_05_ml_features.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Feature calculation windows
- [ ] Historical features
- [ ] Point-in-time accuracy
- [ ] Backfill considerations
