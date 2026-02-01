# 02 Task Fundamentals

## Overview

This section covers all aspects of 02 task fundamentals.

---

# Task Types

## Overview
Different types of tasks/operators in Airflow.

## Tasks

#### - [ ] 2.2.1.1 BashOperator
Filename: `02_01_01_bashoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with BashOperator - shell command execution
- [ ] File: `task_bash_operator.py`

#### - [ ] 2.2.1.2 PythonOperator
Filename: `02_01_02_pythonoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with PythonOperator - Python function execution
- [ ] File: `task_python_operator.py`

#### - [ ] 2.2.1.3 EmptyOperator
Filename: `02_01_03_emptyoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with EmptyOperator - placeholder/dummy tasks
- [ ] File: `task_empty_operator.py`

#### - [ ] 2.2.1.4 BranchPythonOperator
Filename: `02_01_04_branchpythonoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with BranchPythonOperator - conditional branching
- [ ] File: `task_branch_python_operator.py`

#### - [ ] 2.2.1.5 ShortCircuitOperator
Filename: `02_01_05_shortcircuitoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with ShortCircuitOperator - early termination pattern
- [ ] File: `task_short_circuit_operator.py`

#### - [ ] 2.2.1.6 LatestOnlyOperator
Filename: `02_01_06_latestonlyoperator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with LatestOnlyOperator - skip non-latest runs
- [ ] File: `task_latest_only_operator.py`

---

# Task Dependencies

## Overview
Defining relationships between tasks.

## Tasks

#### - [ ] 2.2.2.1 Linear Dependencies
Filename: `02_02_01_linear_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with simple linear dependencies - task1 >> task2 >> task3
- [ ] File: `task_linear_dependencies.py`

#### - [ ] 2.2.2.2 Fan-Out Dependencies
Filename: `02_02_02_fanout_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with fan-out dependencies - one task to many tasks
- [ ] File: `task_fan_out.py`

#### - [ ] 2.2.2.3 Fan-In Dependencies
Filename: `02_02_03_fanin_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with fan-in dependencies - many tasks to one task
- [ ] File: `task_fan_in.py`

#### - [ ] 2.2.2.4 Complex Dependency Graph
Filename: `02_02_04_complex_dependency_graph.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Create DAG with complex dependency graph - mixed patterns
- [ ] File: `task_complex_dependencies.py`

#### - [ ] 2.2.2.5 set_upstream/set_downstream
Filename: `02_02_05_set_upstream_set_downstream.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using alternative syntax - set_upstream() and set_downstream() methods
- [ ] File: `task_set_upstream_downstream.py`

#### - [ ] 2.2.2.6 cross_downstream
Filename: `02_02_06_cross_downstream.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with cross_downstream - cross product dependencies
- [ ] File: `task_cross_downstream.py`

#### - [ ] 2.2.2.7 chain Helper
Filename: `02_02_07_chain_helper.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with chain - linear chain helper function
- [ ] File: `task_chain_helper.py`

#### - [ ] 2.2.2.8 Circular Dependency Error
Filename: `02_02_08_circular_dependency_error.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG with circular dependency (learning example) - demonstrate error
- [ ] File: `task_circular_dependency_error.py`

---

# Task Configuration

## Overview
Configuration options for individual tasks.

## Tasks

#### - [ ] 2.2.3.1 Task Retries
Filename: `02_03_01_task_retries.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task retries - retry and retry_delay parameters
- [ ] File: `task_retries.py`

#### - [ ] 2.2.3.2 Task Timeout
Filename: `02_03_02_task_timeout.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task timeout - execution_timeout parameter
- [ ] File: `task_timeout.py`

#### - [ ] 2.2.3.3 Trigger Rules
Filename: `02_03_03_trigger_rules.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task trigger rules - all_success, all_failed, all_done, etc.
- [ ] File: `task_trigger_rules.py`

#### - [ ] 2.2.3.4 Priority Weight
Filename: `02_03_04_priority_weight.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task priority_weight - execution ordering
- [ ] File: `task_priority_weight.py`

#### - [ ] 2.2.3.5 Queue Assignment
Filename: `02_03_05_queue_assignment.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task queue assignment - route tasks to specific queues
- [ ] File: `task_queue_assignment.py`

#### - [ ] 2.2.3.6 Pool Usage
Filename: `02_03_06_pool_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task pool usage - resource management
- [ ] File: `task_pool_usage.py`

#### - [ ] 2.2.3.7 Task SLA
Filename: `02_03_07_task_sla.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task SLA - service level agreement monitoring
- [ ] File: `task_sla.py`

#### - [ ] 2.2.3.8 Email Alerts
Filename: `02_03_08_email_alerts.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task email alerts - on_failure_callback, on_success_callback
- [ ] File: `task_email_alerts.py`

#### - [ ] 2.2.3.9 Run As User
Filename: `02_03_09_run_as_user.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task run_as_user - execute as different user
- [ ] File: `task_run_as_user.py`

#### - [ ] 2.2.3.10 Depends on Past
Filename: `02_03_10_depends_on_past.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task depends_on_past - sequential execution
- [ ] File: `task_depends_on_past.py`

#### - [ ] 2.2.3.11 Wait for Downstream
Filename: `02_03_11_wait_for_downstream.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task wait_for_downstream - dependency on previous run
- [ ] File: `task_wait_for_downstream.py`

#### - [ ] 2.2.3.12 Disable XCom Push
Filename: `02_03_12_disable_xcom_push.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with task do_xcom_push=False - skip XCom storage
- [ ] File: `task_disable_xcom_push.py`

---

# Task Groups

## Overview
Organizing tasks into logical groups.

## Tasks

#### - [ ] 2.2.4.1 Basic TaskGroup
Filename: `02_04_01_basic_taskgroup.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with basic TaskGroup - group related tasks
- [ ] File: `taskgroup_basic.py`

#### - [ ] 2.2.4.2 Nested TaskGroups
Filename: `02_04_02_nested_taskgroups.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with nested TaskGroups - hierarchical organization
- [ ] File: `taskgroup_nested.py`

#### - [ ] 2.2.4.3 TaskGroup Prefix Control
Filename: `02_04_03_taskgroup_prefix_control.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with TaskGroup prefix_group_id - ID naming control
- [ ] File: `taskgroup_prefix_control.py`

#### - [ ] 2.2.4.4 TaskGroup Tooltip
Filename: `02_04_04_taskgroup_tooltip.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with TaskGroup tooltip - UI documentation
- [ ] File: `taskgroup_tooltip.py`

#### - [ ] 2.2.4.5 TaskGroup UI Color
Filename: `02_04_05_taskgroup_ui_color.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with TaskGroup UI color - visual organization
- [ ] File: `taskgroup_ui_color.py`

#### - [ ] 2.2.4.6 TaskGroup Default Args
Filename: `02_04_06_taskgroup_default_args.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with TaskGroup default_args - group-level defaults
- [ ] File: `taskgroup_default_args.py`

---
