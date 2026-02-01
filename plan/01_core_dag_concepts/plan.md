# 01 Core DAG Concepts

## Overview

This section covers fundamental DAG concepts in Apache Airflow 3.x, including declaration patterns, scheduling, and configuration.

## Airflow 3.x Notes
- `schedule_interval` deprecated, use `schedule` parameter
- `execution_date` deprecated, use `logical_date`
- Data interval model (data_interval_start, data_interval_end) preferred
- Import DAG from `airflow.sdk` or `airflow` module

---

# DAG Declaration Patterns

## Overview
Explore different ways to declare and define DAGs in Apache Airflow 3.x.

## Tasks

#### - [ ] 1.1.1.1 Context Manager Pattern
Filename: `01_01_01_context_manager_pattern.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using `with` statement (context manager)
- [ ] Basic pattern with EmptyOperator
- [ ] Demonstrate implicit DAG assignment to operators
- [ ] File: `dag_with_context_manager.py`

#### - [ ] 1.1.1.2 Standard Constructor Pattern
Filename: `01_01_02_standard_constructor_pattern.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using standard constructor
- [ ] Pass dag explicitly to operators using `dag=` parameter
- [ ] Show when this pattern is useful
- [ ] File: `dag_with_constructor.py`

#### - [ ] 1.1.1.3 @dag Decorator Pattern
Filename: `01_01_03_dag_decorator_pattern.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using `@dag` decorator
- [ ] Function-based DAG generation
- [ ] Demonstrate return value and function call
- [ ] File: `dag_with_decorator.py`

#### - [ ] 1.1.1.4 Comprehensive DAG Parameters
Filename: `01_01_04_comprehensive_dag_parameters.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Create DAG with all common parameters
- [ ] Include: description, tags, default_args, catchup, max_active_runs, etc.
- [ ] Demonstrate each parameter's effect
- [ ] File: `dag_comprehensive_parameters.py`

#### - [ ] 1.1.1.5 Multiple DAGs in Single File
Filename: `01_01_05_multiple_dags_in_single_file.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create multiple DAGs in one file
- [ ] Demonstrate proper DAG isolation
- [ ] Show naming conventions and organization
- [ ] File: `multiple_dags_single_file.py`

#### - [ ] 1.1.1.6 Parse Failure Example
Filename: `01_01_06_parse_failure_example.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG that fails to parse (learning example)
- [ ] Common parsing errors: syntax, imports, variable issues
- [ ] Documented error messages for learning
- [ ] File: `dag_parse_failure_examples.py`

---

# DAG Scheduling

## Overview
Different scheduling patterns and configurations for DAGs.

## Tasks

#### - [ ] 1.1.2.1 Cron Expression Schedule
Filename: `01_02_01_cron_expression_schedule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with cron expression schedule
- [ ] Standard cron patterns (hourly, daily, weekly variations)
- [ ] File: `dag_cron_schedule.py`

#### - [ ] 1.1.2.2 Preset Schedules
Filename: `01_02_02_preset_schedules.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with preset schedules
- [ ] @daily, @hourly, @weekly, @monthly, @yearly
- [ ] File: `dag_preset_schedules.py`

#### - [ ] 1.1.2.3 Timedelta Schedule
Filename: `01_02_03_timedelta_schedule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with timedelta schedule
- [ ] Schedule using datetime.timedelta
- [ ] File: `dag_timedelta_schedule.py`

#### - [ ] 1.1.2.4 None Schedule (Manual Only)
Filename: `01_02_04_none_schedule_manual_only.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with None schedule
- [ ] Manual trigger only, no automatic scheduling
- [ ] File: `dag_manual_trigger_only.py`

#### - [ ] 1.1.2.5 Custom Timetable
Filename: `01_02_05_custom_timetable.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with custom timetable
- [ ] Implement custom scheduling logic
- [ ] File: `dag_custom_timetable.py`

#### - [ ] 1.1.2.6 schedule_interval vs schedule (Deprecated vs Current)
Filename: `01_02_06_schedule_interval_vs_schedule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using `schedule` parameter (Airflow 3.x preferred)
- [ ] Show `schedule_interval` is deprecated but still works
- [ ] Demonstrate both for migration reference
- [ ] File: `dag_schedule_parameter_comparison.py`

**Note**: In Airflow 3.x, always prefer `schedule` over `schedule_interval`

---

# DAG Configuration

## Overview
Various configuration options available for DAGs.

## Tasks

#### - [ ] 1.1.3.1 Default Args
Filename: `01_03_01_default_args.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with default_args - demonstrate task-level defaults inheritance
- [ ] File: `dag_default_args.py`

#### - [ ] 1.1.3.2 Catchup Enabled
Filename: `01_03_02_catchup_enabled.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with catchup=True - backfilling demonstration
- [ ] File: `dag_catchup_enabled.py`

#### - [ ] 1.1.3.3 Catchup Disabled
Filename: `01_03_03_catchup_disabled.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with catchup=False - skip historical runs
- [ ] File: `dag_catchup_disabled.py`

#### - [ ] 1.1.3.4 Max Active Runs
Filename: `01_03_04_max_active_runs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with max_active_runs - control concurrent DAG runs
- [ ] File: `dag_max_active_runs.py`

#### - [ ] 1.1.3.5 Max Active Tasks
Filename: `01_03_05_max_active_tasks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with max_active_tasks - control concurrent task instances
- [ ] File: `dag_max_active_tasks.py`

#### - [ ] 1.1.3.6 DAG Run Timeout
Filename: `01_03_06_dag_run_timeout.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dagrun_timeout - timeout for entire DAG run
- [ ] File: `dag_run_timeout.py`

#### - [ ] 1.1.3.7 Tags
Filename: `01_03_07_tags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with tags - organize and filter DAGs
- [ ] File: `dag_with_tags.py`

#### - [ ] 1.1.3.8 Documentation
Filename: `01_03_08_documentation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with doc_md and description - rich documentation in UI
- [ ] File: `dag_with_documentation.py`

#### - [ ] 1.1.3.9 Owner Links
Filename: `01_03_09_owner_links.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with owner_links - custom links for DAG owners
- [ ] File: `dag_owner_links.py`

#### - [ ] 1.1.3.10 Access Control
Filename: `01_03_10_access_control.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with access_control - role-based permissions
- [ ] File: `dag_access_control.py`

---

# DAG Start and End Dates

## Overview
Understanding start_date, end_date, and execution windows.

## Tasks

#### - [ ] 1.1.4.1 Start Date in Past
Filename: `01_04_01_start_date_in_past.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with start_date in past - immediate scheduling
- [ ] File: `dag_start_date_past.py`

#### - [ ] 1.1.4.2 Start Date in Future
Filename: `01_04_02_start_date_in_future.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with start_date in future - delayed scheduling
- [ ] File: `dag_start_date_future.py`

#### - [ ] 1.1.4.3 End Date
Filename: `01_04_03_end_date.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with end_date - demonstrate automatic pause after end date
- [ ] File: `dag_with_end_date.py`

#### - [ ] 1.1.4.4 Dynamic Start Date
Filename: `01_04_04_dynamic_start_date.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dynamic start_date - use pendulum for timezone-aware dates
- [ ] File: `dag_dynamic_start_date.py`

#### - [ ] 1.1.4.5 Data Interval (Airflow 3.x Model)
Filename: `01_04_05_data_interval.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating data_interval_start and data_interval_end
- [ ] Show relationship to logical_date (replaces execution_date)
- [ ] Explain why data interval model is clearer than execution_date
- [ ] File: `dag_data_interval.py`

**Note**: Airflow 3.x prefers `logical_date` over deprecated `execution_date`

#### - [ ] 1.1.4.6 logical_date vs execution_date
Filename: `01_04_06_logical_date_vs_execution_date.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Show `context['logical_date']` (Airflow 3.x)
- [ ] Show `context['execution_date']` is deprecated
- [ ] Template variables: `{{ logical_date }}` vs `{{ execution_date }}`
- [ ] Migration guidance

---

# DAG Lifecycle Management

## Overview
Managing DAG states, pausing, and lifecycle operations.

## Tasks

#### - [ ] 1.1.5.1 DAG Pausing and Unpausing
Filename: `01_05_01_dag_pausing_unpausing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Show is_paused_upon_creation parameter
- [ ] Demonstrate UI and CLI pausing
- [ ] Explain impact on scheduler behavior
- [ ] File: `dag_pause_control.py`

#### - [ ] 1.1.5.2 DAG Active Runs Management
Filename: `01_05_02_dag_active_runs_management.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Querying active DAG runs via API
- [ ] Managing running vs queued runs
- [ ] Clearing and rerunning DAG runs
- [ ] File: `dag_active_runs.py`

#### - [ ] 1.1.5.3 DAG Cleanup and Deletion
Filename: `01_05_03_dag_cleanup_deletion.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Removing DAG files and metadata
- [ ] Cleaning up historical runs
- [ ] Database cleanup considerations
- [ ] File: `dag_cleanup.py`

#### - [ ] 1.1.5.4 DAG Import Errors
Filename: `01_05_04_dag_import_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Common import errors and causes
- [ ] Debugging parse failures
- [ ] Import error UI display
- [ ] File: `dag_import_errors.py`

#### - [ ] 1.1.5.5 DAG File Processing
Filename: `01_05_05_dag_file_processing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] DAG file discovery and parsing
- [ ] dag_dir_list_interval setting
- [ ] min_file_process_interval impact
- [ ] File: `dag_file_processing.py`

---

# DAG Testing Strategies

## Overview
Patterns for testing DAG definitions and structure.

## Tasks

#### - [ ] 1.1.6.1 DAG Validation Tests
Filename: `01_06_01_dag_validation_tests.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Test DAG loads without errors
- [ ] Validate task count and IDs
- [ ] Check dependencies are correct
- [ ] File: `test_dag_validation.py`

#### - [ ] 1.1.6.2 DAG Structure Tests
Filename: `01_06_02_dag_structure_tests.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test task dependencies with get_task()
- [ ] Verify upstream/downstream relationships
- [ ] Check cycle detection
- [ ] File: `test_dag_structure.py`

#### - [ ] 1.1.6.3 DAG Integrity Tests
Filename: `01_06_03_dag_integrity_tests.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test all DAGs in directory load
- [ ] Verify no import errors
- [ ] CI/CD integration patterns
- [ ] File: `test_dag_integrity.py`

#### - [ ] 1.1.6.4 DAG Config Tests
Filename: `01_06_04_dag_config_tests.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test default_args are applied
- [ ] Verify schedule is correct
- [ ] Check tags and owner
- [ ] File: `test_dag_config.py`

#### - [ ] 1.1.6.5 Mock DAG Run Tests
Filename: `01_06_05_mock_dag_run_tests.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create mock DAGRun for testing
- [ ] Test task execution order
- [ ] Verify XCom behavior
- [ ] File: `test_mock_dag_run.py`

---

# DAG Anti-Patterns

## Overview
Common mistakes to avoid when designing DAGs.

## Tasks

#### - [ ] 1.1.7.1 Top-Level Code Anti-Pattern
Filename: `01_07_01_top_level_code_antipattern.py` | Tags: `['reference', 'core', 'beginner', 'anti-pattern']`

- [ ] Show expensive operations at module level
- [ ] Impact on DAG parsing time
- [ ] Refactoring to task-level execution
- [ ] File: `dag_top_level_antipattern.py`

#### - [ ] 1.1.7.2 Dynamic DAG ID Anti-Pattern
Filename: `01_07_02_dynamic_dag_id_antipattern.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] DAG ID changing between parses
- [ ] Metadata database issues
- [ ] Deterministic ID generation
- [ ] File: `dag_dynamic_id_antipattern.py`

#### - [ ] 1.1.7.3 Excessive Parallelism Anti-Pattern
Filename: `01_07_03_excessive_parallelism_antipattern.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

- [ ] Too many concurrent tasks
- [ ] Resource exhaustion issues
- [ ] Proper concurrency limits
- [ ] File: `dag_excessive_parallelism.py`

#### - [ ] 1.1.7.4 Missing Dependencies Anti-Pattern
Filename: `01_07_04_missing_dependencies_antipattern.py` | Tags: `['reference', 'core', 'beginner', 'anti-pattern']`

- [ ] Tasks without proper ordering
- [ ] Race conditions in execution
- [ ] Explicit dependency patterns
- [ ] File: `dag_missing_dependencies.py`

#### - [ ] 1.1.7.5 Hardcoded Values Anti-Pattern
Filename: `01_07_05_hardcoded_values_antipattern.py` | Tags: `['reference', 'core', 'beginner', 'anti-pattern']`

- [ ] Environment-specific hardcoding
- [ ] Migration to Variables/params
- [ ] Configuration externalization
- [ ] File: `dag_hardcoded_values.py`

---

# DAG Performance Optimization

## Overview
Techniques for improving DAG parsing and execution performance.

## Tasks

#### - [ ] 1.1.8.1 DAG Parsing Optimization
Filename: `01_08_01_dag_parsing_optimization.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Minimize module-level imports
- [ ] Lazy loading patterns
- [ ] Measure parsing time
- [ ] File: `dag_parsing_optimization.py`

#### - [ ] 1.1.8.2 DAG Serialization
Filename: `01_08_02_dag_serialization.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Understanding DAG serialization
- [ ] SerializedDAG model
- [ ] Serialization performance impact
- [ ] File: `dag_serialization.py`

#### - [ ] 1.1.8.3 DAG Bag Optimization
Filename: `01_08_03_dag_bag_optimization.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] DAG bag loading behavior
- [ ] include_examples=False
- [ ] Reducing DAG bag size
- [ ] File: `dag_bag_optimization.py`

#### - [ ] 1.1.8.4 Scheduler Performance
Filename: `01_08_04_scheduler_performance.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Scheduler configuration for large DAGs
- [ ] min_file_process_interval tuning
- [ ] dag_dir_list_interval impact
- [ ] File: `dag_scheduler_performance.py`

#### - [ ] 1.1.8.5 DAG Complexity Limits
Filename: `01_08_05_dag_complexity_limits.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Task count recommendations
- [ ] Dependency graph complexity
- [ ] Splitting large DAGs
- [ ] File: `dag_complexity_limits.py`

---

# DAG Versioning and Migration

## Overview
Strategies for versioning DAGs and handling migrations.

## Tasks

#### - [ ] 1.1.9.1 DAG Version Tracking
Filename: `01_09_01_dag_version_tracking.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Version in dag_id or tags
- [ ] Tracking DAG changes over time
- [ ] Rollback strategies
- [ ] File: `dag_version_tracking.py`

#### - [ ] 1.1.9.2 DAG Migration Patterns
Filename: `01_09_02_dag_migration_patterns.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Migrating from old to new DAG
- [ ] Preserving run history
- [ ] Blue-green DAG deployment
- [ ] File: `dag_migration_patterns.py`

#### - [ ] 1.1.9.3 Airflow 2.x to 3.x Migration
Filename: `01_09_03_airflow_2x_to_3x_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Schedule parameter changes
- [ ] execution_date to logical_date
- [ ] Import path updates
- [ ] File: `dag_airflow_migration.py`

#### - [ ] 1.1.9.4 DAG Deprecation Handling
Filename: `01_09_04_dag_deprecation_handling.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Marking DAGs as deprecated
- [ ] Warning notifications
- [ ] Gradual sunset process
- [ ] File: `dag_deprecation.py`

#### - [ ] 1.1.9.5 Multi-Version DAG Support
Filename: `01_09_05_multi_version_dag_support.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Running multiple DAG versions
- [ ] Version selection logic
- [ ] Testing across versions
- [ ] File: `dag_multi_version.py`

---

# Real-World DAG Examples

## Overview
Complete real-world DAG examples demonstrating best practices.

## Tasks

#### - [ ] 1.1.10.1 ETL Pipeline DAG
Filename: `01_10_01_etl_pipeline_dag.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Extract-Transform-Load pattern
- [ ] Proper task organization
- [ ] Error handling and retries
- [ ] File: `dag_etl_pipeline.py`

#### - [ ] 1.1.10.2 Data Validation DAG
Filename: `01_10_02_data_validation_dag.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Data quality checks
- [ ] Validation branching
- [ ] Alerting on failures
- [ ] File: `dag_data_validation.py`

#### - [ ] 1.1.10.3 Report Generation DAG
Filename: `01_10_03_report_generation_dag.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Scheduled report creation
- [ ] Multiple output formats
- [ ] Distribution via email/S3
- [ ] File: `dag_report_generation.py`

#### - [ ] 1.1.10.4 Microservice Orchestration DAG
Filename: `01_10_04_microservice_orchestration_dag.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Calling multiple services
- [ ] Handling service failures
- [ ] Aggregating responses
- [ ] File: `dag_microservice_orchestration.py`

#### - [ ] 1.1.10.5 Machine Learning Pipeline DAG
Filename: `01_10_05_ml_pipeline_dag.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] Training and evaluation flow
- [ ] Model versioning
- [ ] Deployment integration
- [ ] File: `dag_ml_pipeline.py`

---
