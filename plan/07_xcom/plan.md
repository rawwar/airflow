# 07 XCom

## Overview

This section covers all aspects of XCom (cross-communication) in Airflow 3.x for passing data between tasks.

## Airflow 3.x Notes
- Use `logical_date` instead of deprecated `execution_date` when referencing XCom
- Template: `{{ ti.xcom_pull() }}` works with `logical_date` context
- TaskFlow API provides implicit XCom handling

---

# 7.1 XCom Basics

### - [ ] 7.7.1.1 XCom push and pull
Filename: `07_01_01_xcom_push_and_pull.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with ti.xcom_push() and ti.xcom_pull()
- [ ] Show basic value passing
- [ ] Include key parameter usage

### - [ ] 7.7.1.2 XCom return value
Filename: `07_01_02_xcom_return_value.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with implicit XCom from task return
- [ ] Show return_value key
- [ ] Include multiple returns

### - [ ] 7.7.1.3 XCom with task_ids
Filename: `07_01_03_xcom_with_task_ids.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG pulling XCom from specific tasks
- [ ] Show task_ids parameter
- [ ] Include dag_id for cross-DAG XCom

### - [ ] 7.7.1.4 XCom with templates
Filename: `07_01_04_xcom_with_templates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using {{ ti.xcom_pull() }} in templates
- [ ] Show dynamic value substitution
- [ ] Include Jinja templating

### - [ ] 7.7.1.5 XCom metadata
Filename: `07_01_05_xcom_metadata.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG examining XCom table
- [ ] Show logical_date (replaces execution_date), task_id, key columns
- [ ] Include timestamp tracking
- [ ] Note: execution_date column name may still appear in DB schema

### - [ ] 7.7.1.6 XCom cleanup
Filename: `07_01_06_xcom_cleanup.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating XCom TTL
- [ ] Show automatic cleanup
- [ ] Include manual XCom deletion

---

# 7.2 XCom Data Types

### - [ ] 7.7.2.1 XCom with JSON
Filename: `07_02_01_xcom_with_json.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG passing JSON objects via XCom
- [ ] Show serialization behavior
- [ ] Include nested structures

### - [ ] 7.7.2.2 XCom with lists and dicts
Filename: `07_02_02_xcom_with_lists_and_dicts.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG passing lists and dictionaries
- [ ] Show iteration patterns
- [ ] Include size considerations

### - [ ] 7.7.2.3 XCom with pandas DataFrames
Filename: `07_02_03_xcom_with_pandas_dataframes.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG passing DataFrames via XCom
- [ ] Show pickling behavior
- [ ] Include size limitations

### - [ ] 7.7.2.4 XCom with binary data
Filename: `07_02_04_xcom_with_binary_data.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG passing binary data
- [ ] Show encoding/decoding
- [ ] Include use cases

### - [ ] 7.7.2.5 XCom serialization limits
Filename: `07_02_05_xcom_serialization_limits.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG exceeding XCom size limits
- [ ] Show failure scenarios
- [ ] Include workarounds

### - [ ] 7.7.2.6 XCom with custom types
Filename: `07_02_06_xcom_with_custom_types.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with custom serialization
- [ ] Show implementing __getstate__, __setstate__
- [ ] Include deserialization errors

---

# 7.3 XCom Backends

### - [ ] 7.7.3.1 Default XCom backend
Filename: `07_03_01_default_xcom_backend.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using metadata database for XCom
- [ ] Show default behavior
- [ ] Include limitations

### - [ ] 7.7.3.2 S3 XCom backend
Filename: `07_03_02_s3_xcom_backend.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with S3 XCom backend
- [ ] Show configuration
- [ ] Include large data handling

### - [ ] 7.7.3.3 GCS XCom backend
Filename: `07_03_03_gcs_xcom_backend.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with GCS XCom backend
- [ ] Show bucket configuration
- [ ] Include authentication

### - [ ] 7.7.3.4 Custom XCom backend
Filename: `07_03_04_custom_xcom_backend.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create custom XCom backend implementation
- [ ] Show serialize_value(), deserialize_value()
- [ ] Include backend registration

### - [ ] 7.7.3.5 XCom backend performance
Filename: `07_03_05_xcom_backend_performance.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG comparing backend performance
- [ ] Show latency differences
- [ ] Include throughput considerations

### - [ ] 7.7.3.6 XCom backend selection
Filename: `07_03_06_xcom_backend_selection.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with backend selection logic
- [ ] Show when to use each backend
- [ ] Include decision matrix

---

# 7.4 XCom Patterns

### - [ ] 7.7.4.1 XCom for configuration
Filename: `07_04_01_xcom_for_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using XCom for runtime config
- [ ] Show parameter passing
- [ ] Include dynamic task configuration

### - [ ] 7.7.4.2 XCom for status passing
Filename: `07_04_02_xcom_for_status_passing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using XCom for task status
- [ ] Show success/failure indicators
- [ ] Include conditional branching

### - [ ] 7.7.4.3 XCom aggregation
Filename: `07_04_03_xcom_aggregation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG collecting XCom from multiple tasks
- [ ] Show ti.xcom_pull(task_ids=[...])
- [ ] Include reduction patterns

### - [ ] 7.7.4.4 XCom with dynamic task mapping
Filename: `07_04_04_xcom_with_dynamic_task_mapping.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using XCom with expand()
- [ ] Show passing lists for mapping
- [ ] Include map_index usage

### - [ ] 7.7.4.5 XCom cascade
Filename: `07_04_05_xcom_cascade.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with chained XCom passing
- [ ] Show multi-level data flow
- [ ] Include error propagation

### - [ ] 7.7.4.6 XCom fan-out/fan-in
Filename: `07_04_06_xcom_fanout_fanin.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with fan-out to multiple tasks
- [ ] Show collecting results with fan-in
- [ ] Include parallel processing patterns

---

# 7.5 XCom and TaskFlow

### - [ ] 7.7.5.1 Implicit XCom in TaskFlow
Filename: `07_05_01_implicit_xcom_in_taskflow.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task return values
- [ ] Show automatic XCom handling
- [ ] Include type hints

### - [ ] 7.7.5.2 Multiple outputs in TaskFlow
Filename: `07_05_02_multiple_outputs_in_taskflow.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task returning tuples
- [ ] Show unpacking outputs
- [ ] Include named tuples

### - [ ] 7.7.5.3 TaskFlow chaining
Filename: `07_05_03_taskflow_chaining.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with chained @task calls
- [ ] Show data pipeline
- [ ] Include transformation steps

### - [ ] 7.7.5.4 TaskFlow with explicit XCom
Filename: `07_05_04_taskflow_with_explicit_xcom.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG mixing implicit and explicit XCom
- [ ] Show ti.xcom_pull() in @task
- [ ] Include cross-paradigm communication

### - [ ] 7.7.5.5 TaskFlow XCom caveats
Filename: `07_05_05_taskflow_xcom_caveats.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing TaskFlow XCom limitations
- [ ] Show serialization requirements
- [ ] Include debugging techniques

### - [ ] 7.7.5.6 TaskFlow vs traditional XCom
Filename: `07_05_06_taskflow_vs_traditional_xcom.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create comparison DAGs
- [ ] Show advantages of each approach
- [ ] Include migration strategies

---

# 7.6 XCom Errors and Debugging

### - [ ] 7.7.6.1 XCom not found errors
Filename: `07_06_01_xcom_not_found_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG with missing XCom pull
- [ ] Show default value handling
- [ ] Include error handling patterns

### - [ ] 7.7.6.2 XCom serialization errors
Filename: `07_06_02_xcom_serialization_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG with non-serializable objects
- [ ] Show pickling failures
- [ ] Include workarounds

### - [ ] 7.7.6.3 XCom size errors
Filename: `07_06_03_xcom_size_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG exceeding XCom size limits
- [ ] Show database errors
- [ ] Include external storage patterns

### - [ ] 7.7.6.4 XCom race conditions
Filename: `07_06_04_xcom_race_conditions.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with concurrent XCom access
- [ ] Show timing issues
- [ ] Include synchronization patterns

### - [ ] 7.7.6.5 XCom debugging
Filename: `07_06_05_xcom_debugging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with XCom inspection tasks
- [ ] Show viewing XCom in UI and database
- [ ] Include logging XCom values

### - [ ] 7.7.6.6 XCom best practices
Filename: `07_06_06_xcom_best_practices.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating XCom best practices
- [ ] Show when to use vs avoid XCom
- [ ] Include alternative patterns

---

# 7.7 Advanced XCom Usage

### - [ ] 7.7.7.1 XCom with external dependencies
Filename: `07_07_01_xcom_with_external_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using XCom with ExternalTaskSensor
- [ ] Show cross-DAG communication
- [ ] Include external_dag_id, external_task_id

### - [ ] 7.7.7.2 XCom in callbacks
Filename: `07_07_02_xcom_in_callbacks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG accessing XCom in callbacks
- [ ] Show on_success_callback with XCom
- [ ] Include failure notifications with data

### - [ ] 7.7.7.3 XCom with retry logic
Filename: `07_07_03_xcom_with_retry_logic.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG preserving XCom across retries
- [ ] Show XCom state between attempts
- [ ] Include idempotent XCom operations

### - [ ] 7.7.7.4 XCom encryption
Filename: `07_07_04_xcom_encryption.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with encrypted XCom values
- [ ] Show custom encryption/decryption
- [ ] Include security considerations

### - [ ] 7.7.7.5 XCom versioning
Filename: `07_07_05_xcom_versioning.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with versioned XCom schema
- [ ] Show schema evolution
- [ ] Include backward compatibility

### - [ ] 7.7.7.6 XCom performance optimization
Filename: `07_07_06_xcom_performance_optimization.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG optimizing XCom usage
- [ ] Show batching, caching strategies
- [ ] Include profiling and benchmarking

---

# 7.8 XCom Anti-Patterns

### - [ ] 7.8.1 Large Data in XCom
Filename: `07_08_01_large_data_in_xcom.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] Anti-pattern: passing DataFrames via XCom
- [ ] Database size explosion
- [ ] Alternative: external storage references
- [ ] File path passing pattern

### - [ ] 7.8.2 Sensitive Data in XCom
Filename: `07_08_02_sensitive_data_in_xcom.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] Anti-pattern: passwords in XCom
- [ ] Security implications
- [ ] Secrets backend usage
- [ ] Encryption patterns

### - [ ] 7.8.3 Overusing XCom
Filename: `07_08_03_overusing_xcom.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] Anti-pattern: XCom for everything
- [ ] When to use Variables instead
- [ ] External state storage
- [ ] Right tool for the job

### - [ ] 7.8.4 XCom Without Error Handling
Filename: `07_08_04_xcom_without_error_handling.py` | Tags: `['reference', 'core', 'beginner', 'anti-pattern']`

- [ ] Anti-pattern: assuming XCom exists
- [ ] KeyError on missing XCom
- [ ] Proper default handling
- [ ] Graceful degradation

### - [ ] 7.8.5 Non-Deterministic XCom Keys
Filename: `07_08_05_non_deterministic_xcom_keys.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] Anti-pattern: dynamic keys without pattern
- [ ] Key collision issues
- [ ] Consistent naming conventions
- [ ] Key schema documentation

---

# 7.9 XCom Testing

### - [ ] 7.9.1 Unit Testing XCom Push
Filename: `07_09_01_unit_testing_xcom_push.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Mock ti.xcom_push
- [ ] Verify pushed values
- [ ] Test key and value
- [ ] Assertions patterns

### - [ ] 7.9.2 Unit Testing XCom Pull
Filename: `07_09_02_unit_testing_xcom_pull.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Mock ti.xcom_pull
- [ ] Set up return values
- [ ] Test missing XCom handling
- [ ] Multiple task_ids

### - [ ] 7.9.3 Integration Testing XCom Flow
Filename: `07_09_03_integration_testing_xcom_flow.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test full XCom chain
- [ ] Verify data transformation
- [ ] End-to-end validation
- [ ] Database state checks

### - [ ] 7.9.4 Testing Custom XCom Backend
Filename: `07_09_04_testing_custom_xcom_backend.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Mock backend operations
- [ ] Test serialization/deserialization
- [ ] Error handling tests
- [ ] Performance tests

### - [ ] 7.9.5 Testing XCom with Dynamic Tasks
Filename: `07_09_05_testing_xcom_with_dynamic_tasks.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Test XCom from expand()
- [ ] Verify map_indexes parameter
- [ ] Aggregation testing
- [ ] Edge cases

---

# 7.10 XCom Real-World Patterns

### - [ ] 7.10.1 File Processing Pipeline XCom
Filename: `07_10_01_file_processing_pipeline_xcom.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Pass file paths between tasks
- [ ] Process file list via XCom
- [ ] Aggregated results
- [ ] Cleanup coordination

### - [ ] 7.10.2 API Response Chaining
Filename: `07_10_02_api_response_chaining.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Pass API responses via XCom
- [ ] Extract IDs for next call
- [ ] Pagination handling
- [ ] Response aggregation

### - [ ] 7.10.3 Data Quality Results XCom
Filename: `07_10_03_data_quality_results_xcom.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Pass validation results
- [ ] Aggregate quality metrics
- [ ] Conditional branching
- [ ] Alert generation

### - [ ] 7.10.4 ML Model Parameters XCom
Filename: `07_10_04_ml_model_parameters_xcom.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Hyperparameter passing
- [ ] Model metrics communication
- [ ] Best model selection
- [ ] Experiment tracking

### - [ ] 7.10.5 Resource Handle Passing
Filename: `07_10_05_resource_handle_passing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Pass cluster IDs via XCom
- [ ] Connection handles
- [ ] Teardown coordination
- [ ] Resource lifecycle

---
