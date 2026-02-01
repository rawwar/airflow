# 60 Timezone Handling

## Overview
Managing timezones correctly in Airflow DAGs for global deployments and multi-region processing.

---

# 60.1 Timezone Fundamentals

### - [ ] 60.1.1 Airflow Default Timezone
Filename: `60_01_01_default_timezone.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] default_timezone configuration
- [ ] UTC as default
- [ ] Why UTC recommended
- [ ] Configuration options

### - [ ] 60.1.2 Timezone-Aware Datetimes
Filename: `60_01_02_timezone_aware.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Always use timezone-aware
- [ ] pendulum library
- [ ] Naive vs aware datetimes
- [ ] Common mistakes

### - [ ] 60.1.3 DAG Timezone Setting
Filename: `60_01_03_dag_timezone.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Per-DAG timezone
- [ ] Start date with timezone
- [ ] Schedule interpretation
- [ ] Mixing timezones

### - [ ] 60.1.4 Pendulum Usage
Filename: `60_01_04_pendulum_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Create timezone-aware dates
- [ ] Timezone conversions
- [ ] Common operations
- [ ] vs datetime module

### - [ ] 60.1.5 Timezone Configuration
Filename: `60_01_05_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] airflow.cfg settings
- [ ] Environment variables
- [ ] Web UI display timezone
- [ ] Per-user settings

---

# 60.2 Scheduling with Timezones

### - [ ] 60.2.1 Cron with Timezone
Filename: `60_02_01_cron_timezone.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Cron interpreted in DAG timezone
- [ ] Daily at midnight local
- [ ] DST handling
- [ ] Examples

### - [ ] 60.2.2 DST Transitions
Filename: `60_02_02_dst_transitions.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Spring forward issues
- [ ] Fall back issues
- [ ] Skipped/repeated runs
- [ ] Best practices

### - [ ] 60.2.3 Cross-Timezone Dependencies
Filename: `60_02_03_cross_timezone.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] DAGs in different zones
- [ ] Coordination challenges
- [ ] UTC as common ground
- [ ] ExternalTaskSensor timing

### - [ ] 60.2.4 Time-Based Sensors
Filename: `60_02_04_time_sensors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] TimeSensor timezone
- [ ] DateTimeSensor timezone
- [ ] Target time interpretation
- [ ] Timezone specification

### - [ ] 60.2.5 Schedule String Timezones
Filename: `60_02_05_schedule_strings.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] @daily, @hourly timezone
- [ ] Timedelta schedules
- [ ] Asset-driven timing
- [ ] Mixed approaches

---

# 60.3 Data Processing with Timezones

### - [ ] 60.3.1 Data Interval Timezones
Filename: `60_03_01_data_interval_tz.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Interval in DAG timezone
- [ ] Converting for queries
- [ ] Source data timezone
- [ ] Alignment strategies

### - [ ] 60.3.2 Database Queries with Timezone
Filename: `60_03_02_database_queries.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] SQL with timezone conversion
- [ ] Filter by local time
- [ ] Store in UTC, display local
- [ ] Common pitfalls

### - [ ] 60.3.3 API Calls with Timezone
Filename: `60_03_03_api_calls.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] API timezone requirements
- [ ] Convert before sending
- [ ] Parse responses
- [ ] Documentation

### - [ ] 60.3.4 File Path Date Patterns
Filename: `60_03_04_file_paths.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Date in file paths
- [ ] Timezone for paths
- [ ] Partition by local time
- [ ] Consistency

### - [ ] 60.3.5 Multi-Region Processing
Filename: `60_03_05_multi_region.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Process data per region
- [ ] Region-specific schedules
- [ ] Aggregation across zones
- [ ] Reporting timezone

---

# 60.4 UI and Display

### - [ ] 60.4.1 Web UI Timezone
Filename: `60_04_01_web_ui_timezone.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Display timezone setting
- [ ] Per-user preference
- [ ] UTC vs local display
- [ ] Confusion prevention

### - [ ] 60.4.2 Log Timestamps
Filename: `60_04_02_log_timestamps.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Log timezone
- [ ] Correlation with events
- [ ] Debugging across zones
- [ ] Standardization

### - [ ] 60.4.3 Rendered Templates
Filename: `60_04_03_rendered_templates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Timezone in templates
- [ ] Display conversions
- [ ] Format strings
- [ ] Localization

### - [ ] 60.4.4 Calendar Views
Filename: `60_04_04_calendar_views.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Calendar in UI
- [ ] Timezone interpretation
- [ ] Day boundaries
- [ ] User expectations

### - [ ] 60.4.5 Notifications
Filename: `60_04_05_notifications.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Alert timestamps
- [ ] Recipient timezone
- [ ] Clear communication
- [ ] Best practices

---

# 60.5 Timezone Best Practices

### - [ ] 60.5.1 Use UTC Internally
Filename: `60_05_01_use_utc.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Store in UTC
- [ ] Process in UTC
- [ ] Convert for display
- [ ] Benefits

### - [ ] 60.5.2 Consistent Timezone Strategy
Filename: `60_05_02_consistent_strategy.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Organization-wide policy
- [ ] Documentation
- [ ] Enforcement
- [ ] Training

### - [ ] 60.5.3 Testing Timezones
Filename: `60_05_03_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test with different zones
- [ ] DST edge cases
- [ ] Mock time
- [ ] CI considerations

### - [ ] 60.5.4 Timezone Debugging
Filename: `60_05_04_debugging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Common issues
- [ ] Diagnostic logging
- [ ] Verification steps
- [ ] Tools

### - [ ] 60.5.5 Timezone Anti-Patterns
Filename: `60_05_05_anti_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Naive datetimes
- [ ] Hardcoded offsets
- [ ] Ignoring DST
- [ ] Inconsistent handling

---

# 60.6 Advanced Timezone Patterns

## Overview
Complex timezone handling scenarios.

## Tasks

### - [ ] 60.6.1 Multi-Timezone DAG
Filename: `60_06_01_multi_timezone_dag.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Tasks in different zones
- [ ] Coordination logic
- [ ] Data alignment
- [ ] Implementation

### - [ ] 60.6.2 Timezone-Aware Sensors
Filename: `60_06_02_timezone_sensors.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Time-based sensor zones
- [ ] External system zones
- [ ] Conversion handling
- [ ] Best practices

### - [ ] 60.6.3 Global Data Processing
Filename: `60_06_03_global_processing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Follow-the-sun pattern
- [ ] Regional processing
- [ ] Aggregation across zones
- [ ] Reporting timezone

### - [ ] 60.6.4 Historical Timezone Changes
Filename: `60_06_04_historical_changes.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Timezone rule changes
- [ ] Historical accuracy
- [ ] Database updates
- [ ] Testing strategies

### - [ ] 60.6.5 Timezone Configuration Management
Filename: `60_06_05_config_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Centralized timezone config
- [ ] Environment-specific
- [ ] Override patterns
- [ ] Documentation

---

# 60.7 Testing Timezone Handling

## Overview
Comprehensive timezone testing strategies.

## Tasks

### - [ ] 60.7.1 Unit Testing Timezones
Filename: `60_07_01_unit_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Mock timezones
- [ ] Test conversions
- [ ] Edge cases
- [ ] pytest patterns

### - [ ] 60.7.2 DST Transition Testing
Filename: `60_07_02_dst_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Spring forward tests
- [ ] Fall back tests
- [ ] Boundary conditions
- [ ] All affected zones

### - [ ] 60.7.3 Cross-Zone Integration Testing
Filename: `60_07_03_integration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Multi-zone scenarios
- [ ] Data consistency
- [ ] End-to-end tests
- [ ] CI configuration

### - [ ] 60.7.4 Time Travel Testing
Filename: `60_07_04_time_travel.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] freezegun usage
- [ ] Future date testing
- [ ] Historical testing
- [ ] Isolation

### - [ ] 60.7.5 Production Validation
Filename: `60_07_05_validation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Pre-DST checks
- [ ] Monitoring after transition
- [ ] Smoke tests
- [ ] Rollback criteria

---

# 60.8 Timezone Troubleshooting

## Overview
Debugging timezone-related issues.

## Tasks

### - [ ] 60.8.1 Common Timezone Bugs
Filename: `60_08_01_common_bugs.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Off-by-one hour
- [ ] Wrong day data
- [ ] Missing data
- [ ] Diagnosis steps

### - [ ] 60.8.2 DST Issue Diagnosis
Filename: `60_08_02_dst_diagnosis.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Identify DST issues
- [ ] Log analysis
- [ ] Reproduction steps
- [ ] Fix patterns

### - [ ] 60.8.3 Conversion Debugging
Filename: `60_08_03_conversion_debugging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Trace conversions
- [ ] Logging strategy
- [ ] Verification tools
- [ ] Common mistakes

### - [ ] 60.8.4 External System Timezone Issues
Filename: `60_08_04_external_systems.py` | Tags: `['reference', 'patterns', 'intermediate', 'failure']`
- [ ] API timezone mismatches
- [ ] Database timezone issues
- [ ] File timestamp issues
- [ ] Resolution strategies

### - [ ] 60.8.5 Recovery Procedures
Filename: `60_08_05_recovery.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Fix incorrect data
- [ ] Reprocessing strategy
- [ ] Data correction
- [ ] Prevention

---

# 60.9 Timezone Monitoring

## Overview
Monitoring timezone-related behavior.

## Tasks

### - [ ] 60.9.1 Timezone Health Metrics
Filename: `60_09_01_health_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Conversion accuracy
- [ ] Processing time consistency
- [ ] DST transition monitoring
- [ ] Anomaly detection

### - [ ] 60.9.2 DST Transition Alerts
Filename: `60_09_02_dst_alerts.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Pre-transition reminders
- [ ] Post-transition checks
- [ ] Issue detection
- [ ] Escalation

### - [ ] 60.9.3 Timezone Dashboard
Filename: `60_09_03_dashboard.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Processing by zone
- [ ] Schedule visualization
- [ ] DST calendar
- [ ] Health overview

### - [ ] 60.9.4 Audit Timezone Handling
Filename: `60_09_04_audit.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Track timezone usage
- [ ] Compliance requirements
- [ ] Change history
- [ ] Documentation

### - [ ] 60.9.5 Capacity by Timezone
Filename: `60_09_05_capacity.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Load distribution
- [ ] Peak times by zone
- [ ] Resource planning
- [ ] Optimization

---

# 60.10 Real-World Scenarios

## Overview
Production timezone handling patterns.

## Tasks

### - [ ] 60.10.1 Global E-Commerce Platform
Filename: `60_10_01_ecommerce.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Multi-region stores
- [ ] Local time reporting
- [ ] End-of-day processing
- [ ] Holiday handling

### - [ ] 60.10.2 Financial Markets Processing
Filename: `60_10_02_financial_markets.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Exchange timezones
- [ ] Market hours
- [ ] Settlement timing
- [ ] Regulatory requirements

### - [ ] 60.10.3 IoT Data Collection
Filename: `60_10_03_iot_data.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Device timezones
- [ ] Central processing
- [ ] Timestamp normalization
- [ ] Analysis timezone

### - [ ] 60.10.4 Multi-National Reporting
Filename: `60_10_04_multinational.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Regional reports
- [ ] Global consolidation
- [ ] Compliance by region
- [ ] Presentation timezone

### - [ ] 60.10.5 24/7 Operations
Filename: `60_10_05_24_7_ops.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Always-on processing
- [ ] Shift handoffs
- [ ] Maintenance windows
- [ ] Global support
