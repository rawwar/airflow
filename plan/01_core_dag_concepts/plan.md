# 01 Core Dag Concepts

## Overview

This section covers all aspects of 01 core dag concepts.

---

# DAG Declaration Patterns

## Overview
Explore different ways to declare and define DAGs in Apache Airflow.

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

#### - [ ] 1.1.2.6 schedule_interval vs schedule
Filename: `01_02_06_schedule_interval_vs_schedule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating parameter differences
- [ ] Show old vs new scheduling parameters
- [ ] File: `dag_schedule_parameter_comparison.py`

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

#### - [ ] 1.1.4.5 Data Interval
Filename: `01_04_05_data_interval.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating data_interval - understanding execution windows
- [ ] File: `dag_data_interval.py`

---
