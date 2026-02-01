# 08 Sensors

## Overview

This section covers all aspects of sensors in Airflow 3.x, including basic sensors, modes, cloud sensors, and deferrable sensors.

## Airflow 3.x Notes
- Dataset renamed to **Asset** - see section 8.6
- Many sensors support `deferrable=True` for efficient resource usage
- Deferrable sensors require triggerer component
- See Section 51 for deep dive into deferrable operators

---

# 8.1 Basic Sensors

### - [ ] 8.8.1.1 FileSensor
Filename: `08_01_01_filesensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with FileSensor waiting for file
- [ ] Show filepath, fs_conn_id usage
- [ ] Include timeout and poke_interval

### - [ ] 8.8.1.2 TimeSensor
Filename: `08_01_02_timesensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with TimeSensor waiting for time
- [ ] Show target_time usage
- [ ] Include timezone handling

### - [ ] 8.8.1.3 TimeDeltaSensor
Filename: `08_01_03_timedeltasensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with TimeDeltaSensor waiting for duration
- [ ] Show delta parameter
- [ ] Include use cases

### - [ ] 8.8.1.4 DateTimeSensor
Filename: `08_01_04_datetimesensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with DateTimeSensor for specific datetime
- [ ] Show target_datetime usage
- [ ] Include scheduling patterns

### - [ ] 8.8.1.5 ExternalTaskSensor
Filename: `08_01_05_externaltasksensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with ExternalTaskSensor
- [ ] Show external_dag_id, external_task_id
- [ ] Include execution_date_fn

### - [ ] 8.8.1.6 PythonSensor
Filename: `08_01_06_pythonsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with PythonSensor
- [ ] Show python_callable usage
- [ ] Include returning boolean

---

# 8.2 Sensor Modes

### - [ ] 8.8.2.1 Poke mode
Filename: `08_02_01_poke_mode.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor in poke mode
- [ ] Show blocking task slot
- [ ] Include resource usage

### - [ ] 8.8.2.2 Reschedule mode
Filename: `08_02_02_reschedule_mode.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with mode="reschedule"
- [ ] Show freeing task slot between pokes
- [ ] Include scheduler overhead

### - [ ] 8.8.2.3 Mode comparison
Filename: `08_02_03_mode_comparison.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAGs comparing poke vs reschedule
- [ ] Show performance characteristics
- [ ] Include best practice guidance

### - [ ] 8.8.2.4 Poke interval configuration
Filename: `08_02_04_poke_interval_configuration.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with various poke_interval values
- [ ] Show trade-offs
- [ ] Include resource considerations

### - [ ] 8.8.2.5 Sensor timeout
Filename: `08_02_05_sensor_timeout.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with timeout parameter
- [ ] Show failure after timeout
- [ ] Include soft_fail usage

### - [ ] 8.8.2.6 Exponential backoff
Filename: `08_02_06_exponential_backoff.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with exponential_backoff
- [ ] Show increasing poke intervals
- [ ] Include configuration

---

# 8.3 Database Sensors

### - [ ] 8.8.3.1 SqlSensor
Filename: `08_03_01_sqlsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with SqlSensor
- [ ] Show SQL query evaluation
- [ ] Include conn_id usage

### - [ ] 8.8.3.2 Success criteria
Filename: `08_03_02_success_criteria.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with success parameter
- [ ] Show callable vs lambda
- [ ] Include row count checks

### - [ ] 8.8.3.3 PostgreSQL-specific sensors
Filename: `08_03_03_postgresqlspecific_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with PostgresSensor (if exists)
- [ ] Show database-specific features
- [ ] Include connection pooling

### - [ ] 8.8.3.4 MySQL-specific sensors
Filename: `08_03_04_mysqlspecific_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with MySqlSensor (if exists)
- [ ] Show query patterns
- [ ] Include charset handling

### - [ ] 8.8.3.5 Database sensor performance
Filename: `08_03_05_database_sensor_performance.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with optimized SQL queries
- [ ] Show index usage
- [ ] Include query timeout

### - [ ] 8.8.3.6 Database sensor patterns
Filename: `08_03_06_database_sensor_patterns.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with common sensor patterns
- [ ] Show record existence check
- [ ] Include data quality validation

---

# 8.4 Cloud Storage Sensors

### - [ ] 8.8.4.1 S3KeySensor
Filename: `08_04_01_s3keysensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with S3KeySensor
- [ ] Show bucket_key, bucket_name
- [ ] Include wildcard usage

### - [ ] 8.8.4.2 GCSObjectExistenceSensor
Filename: `08_04_02_gcsobjectexistencesensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with GCS object sensor
- [ ] Show bucket and object parameters
- [ ] Include prefix matching

### - [ ] 8.8.4.3 Azure Blob sensors
Filename: `08_04_03_azure_blob_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with Azure blob sensors
- [ ] Show container and blob name
- [ ] Include authentication

### - [ ] 8.8.4.4 S3PrefixSensor
Filename: `08_04_04_s3prefixsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with S3PrefixSensor
- [ ] Show prefix matching
- [ ] Include min_objects parameter

### - [ ] 8.8.4.5 Multi-file sensors
Filename: `08_04_05_multifile_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG waiting for multiple files
- [ ] Show combining sensors
- [ ] Include trigger_rule usage

### - [ ] 8.8.4.6 Cloud sensor optimization
Filename: `08_04_06_cloud_sensor_optimization.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with optimized cloud sensors
- [ ] Show API call minimization
- [ ] Include cost considerations

---

# 8.5 Service and API Sensors

### - [ ] 8.8.5.1 HttpSensor
Filename: `08_05_01_httpsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with HttpSensor
- [ ] Show endpoint, response_check
- [ ] Include authentication

### - [ ] 8.8.5.2 Custom API sensor
Filename: `08_05_02_custom_api_sensor.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create custom sensor for API endpoint
- [ ] Show poke() implementation
- [ ] Include error handling

### - [ ] 8.8.5.3 WebHdfsSensor
Filename: `08_05_03_webhdfssensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with WebHdfsSensor
- [ ] Show HDFS file checking
- [ ] Include NameNode connectivity

### - [ ] 8.8.5.4 Service health sensors
Filename: `08_05_04_service_health_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG checking service health
- [ ] Show readiness probes
- [ ] Include retry logic

### - [ ] 8.8.5.5 Queue sensors
Filename: `08_05_05_queue_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with SqsSensor or similar
- [ ] Show message availability checking
- [ ] Include queue depth monitoring

### - [ ] 8.8.5.6 gRPC/custom protocol sensors
Filename: `08_05_06_grpc_custom_protocol_sensors.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create sensor for custom protocols
- [ ] Show protocol implementation
- [ ] Include connection management

---

# 8.6 Asset-Driven Scheduling (formerly Dataset)

**Note**: In Airflow 3.x, Dataset is renamed to **Asset**. See Section 11 for comprehensive Asset coverage.

### - [ ] 8.6.1 Asset Schedule Triggering
Filename: `08_06_01_asset_schedule_triggering.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG triggered by Asset updates
- [ ] Show `schedule=[Asset()]` usage (not Dataset)
- [ ] Import from `airflow.sdk.definitions.asset`
- [ ] Include asset URI patterns

### - [ ] 8.6.2 Multiple Asset Conditions
Filename: `08_06_02_multiple_asset_conditions.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with multiple Asset dependencies
- [ ] Show AND logic: `schedule=[Asset("a"), Asset("b")]`
- [ ] Show OR logic: `AssetAny(Asset("a"), Asset("b"))`
- [ ] Include complex conditions with AssetAll

### - [ ] 8.6.3 Asset Producing Tasks
Filename: `08_06_03_asset_producing_tasks.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with outlet assets
- [ ] Show `outlets=[Asset()]` on tasks
- [ ] Include lineage tracking in UI

### - [ ] 8.6.4 Cross-DAG Asset Dependencies
Filename: `08_06_04_crossdag_asset_dependencies.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create producer and consumer DAGs
- [ ] Show asset-driven workflow
- [ ] Include dependency graph visualization

### - [ ] 8.6.5 Asset vs ExternalTaskSensor
Filename: `08_06_05_asset_vs_externaltasksensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create comparison DAGs
- [ ] Assets: data-centric, loose coupling
- [ ] ExternalTaskSensor: task-centric, execution alignment
- [ ] Include migration guide

### - [ ] 8.6.6 Asset Best Practices
Filename: `08_06_06_asset_best_practices.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG demonstrating asset patterns
- [ ] Show URI conventions
- [ ] Include versioning strategies
- [ ] Reference Section 11 for deep dive

---

# 8.7 Specialized Sensors

### - [ ] 8.8.7.1 BashSensor
Filename: `08_07_01_bashsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with BashSensor
- [ ] Show bash_command exit code checking
- [ ] Include environment setup

### - [ ] 8.8.7.2 EmailSensor (if exists)
Filename: `08_07_02_emailsensor_if_exists.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG waiting for email
- [ ] Show IMAP/POP3 configuration
- [ ] Include criteria matching

### - [ ] 8.8.7.3 HdfsRegexSensor
Filename: `08_07_03_hdfsregexsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with HDFS regex sensor
- [ ] Show pattern matching
- [ ] Include directory scanning

### - [ ] 8.8.7.4 PartitionSensor
Filename: `08_07_04_partitionsensor.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with Hive/Metastore partition sensor
- [ ] Show partition existence check
- [ ] Include metastore connection

### - [ ] 8.8.7.5 Smart sensors (deprecated)
Filename: `08_07_05_smart_sensors_deprecated.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG showing smart sensors (if supported)
- [ ] Show consolidation pattern
- [ ] Include deprecation notes

### - [ ] 8.8.7.6 Named sensors
Filename: `08_07_06_named_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with custom named sensors
- [ ] Show sensor registration
- [ ] Include sensor discovery

---

# 8.8 Sensor Patterns

### - [ ] 8.8.8.1 Chained sensors
Filename: `08_08_01_chained_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with multiple sensors in sequence
- [ ] Show sequential waiting
- [ ] Include timeout management

### - [ ] 8.8.8.2 Parallel sensors
Filename: `08_08_02_parallel_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with parallel sensors
- [ ] Show trigger_rule="all_done"
- [ ] Include resource management

### - [ ] 8.8.8.3 Sensor with downstream dependencies
Filename: `08_08_03_sensor_with_downstream_dependencies.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor + operator chain
- [ ] Show data availability pattern
- [ ] Include error handling

### - [ ] 8.8.8.4 Sensor in loops
Filename: `08_08_04_sensor_in_loops.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor in dynamic loop
- [ ] Show expand() with sensors
- [ ] Include scalability

### - [ ] 8.8.8.5 Sensor retry patterns
Filename: `08_08_05_sensor_retry_patterns.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor retry logic
- [ ] Show retries vs timeout
- [ ] Include exponential backoff

### - [ ] 8.8.8.6 Sensor soft fail
Filename: `08_08_06_sensor_soft_fail.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with soft_fail=True
- [ ] Show skipping downstream on timeout
- [ ] Include use cases

---

# 8.9 Sensor Errors and Debugging

### - [ ] 8.8.9.1 Sensor timeout handling
Filename: `08_09_01_sensor_timeout_handling.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor timeout
- [ ] Show failure behavior
- [ ] Include notification patterns

### - [ ] 8.8.9.2 Sensor connection errors
Filename: `08_09_02_sensor_connection_errors.py` | Tags: `['reference', 'control', 'beginner', 'failure']`

- [ ] Create DAG with connection failures
- [ ] Show retry logic
- [ ] Include error logging

### - [ ] 8.8.9.3 Sensor debugging
Filename: `08_09_03_sensor_debugging.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with sensor logging
- [ ] Show poke return value inspection
- [ ] Include troubleshooting guide

### - [ ] 8.8.9.4 Sensor performance issues
Filename: `08_09_04_sensor_performance_issues.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with poorly performing sensor
- [ ] Show optimization techniques
- [ ] Include monitoring

### - [ ] 8.8.9.5 Sensor anti-patterns
Filename: `08_09_05_sensor_antipatterns.py` | Tags: `['reference', 'control', 'beginner', 'anti-pattern']`

- [ ] Create DAG showing sensor misuse
- [ ] Show blocking patterns to avoid
- [ ] Include alternative approaches

### - [ ] 8.8.9.6 Sensor best practices
Filename: `08_09_06_sensor_best_practices.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Create DAG with optimal sensor usage
- [ ] Show reschedule mode usage
- [ ] Include resource considerations

---

# 8.10 Custom Sensor Development

### - [ ] 8.8.10.1 Basic custom sensor
Filename: `08_10_01_basic_custom_sensor.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create custom sensor class
- [ ] Show poke() method implementation
- [ ] Include BaseSensorOperator inheritance

### - [ ] 8.8.10.2 Custom sensor with parameters
Filename: `08_10_02_custom_sensor_with_parameters.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create parameterized custom sensor
- [ ] Show template_fields
- [ ] Include validation

### - [ ] 8.8.10.3 Custom sensor with connections
Filename: `08_10_03_custom_sensor_with_connections.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create sensor using Airflow connections
- [ ] Show hook usage
- [ ] Include connection testing

### - [ ] 8.10.4 Deferrable Custom Sensor (Async)
Filename: `08_10_04_deferrable_custom_sensor.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create deferrable sensor using defer()
- [ ] Implement custom Trigger class
- [ ] Show suspend/resume pattern
- [ ] Efficient resource usage vs poke mode
- [ ] See Section 51 for complete deferrable coverage

### - [ ] 8.8.10.5 Custom sensor testing
Filename: `08_10_05_custom_sensor_testing.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create tests for custom sensor
- [ ] Show mocking external dependencies
- [ ] Include pytest examples

### - [ ] 8.10.6 Custom sensor packaging
Filename: `08_10_06_custom_sensor_packaging.py` | Tags: `['reference', 'control', 'advanced', 'success']`

- [ ] Create packaged custom sensor
- [ ] Show plugin or provider integration
- [ ] Include distribution

---

# 8.11 Deferrable Sensors (Airflow 3.x)

## Overview
Deferrable sensors release their worker slot while waiting, dramatically improving resource efficiency. See Section 51 for complete coverage of deferrable operators.

### - [ ] 8.11.1 Deferrable vs Poke Mode Comparison
Filename: `08_11_01_deferrable_vs_poke.py` | Tags: `['reference', 'control', 'intermediate', 'success']`

- [ ] Same sensor in poke mode vs deferrable mode
- [ ] Show worker slot usage difference
- [ ] Resource efficiency comparison
- [ ] When to use each mode

### - [ ] 8.11.2 deferrable=True Parameter
Filename: `08_11_02_deferrable_parameter.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Enable deferrable on compatible sensors
- [ ] FileSensor(deferrable=True)
- [ ] ExternalTaskSensor(deferrable=True)
- [ ] HttpSensor(deferrable=True)

### - [ ] 8.11.3 Built-in Async Sensors
Filename: `08_11_03_builtin_async_sensors.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] TimeSensorAsync
- [ ] DateTimeSensorAsync
- [ ] Async variants of common sensors
- [ ] Requires triggerer component

### - [ ] 8.11.4 Deferrable Sensor Resource Savings
Filename: `08_11_04_deferrable_resource_savings.py` | Tags: `['reference', 'control', 'intermediate', 'success']`

- [ ] DAG with many sensors waiting
- [ ] Poke mode: N workers blocked
- [ ] Deferrable mode: 0 workers while waiting
- [ ] Scale benefits demonstration

### - [ ] 8.11.5 Deferrable Sensor Timeout Handling
Filename: `08_11_05_deferrable_timeout.py` | Tags: `['reference', 'control', 'intermediate', 'success']`

- [ ] Timeout behavior in deferrable mode
- [ ] Trigger timeout vs task timeout
- [ ] Graceful timeout handling
- [ ] Cleanup on timeout

### - [ ] 8.11.6 Triggerer Requirement
Filename: `08_11_06_triggerer_requirement.py` | Tags: `['reference', 'control', 'beginner', 'success']`

- [ ] Triggerer must be running for deferrable
- [ ] Detect triggerer availability
- [ ] Fallback behavior
- [ ] Monitoring triggerer health

---
