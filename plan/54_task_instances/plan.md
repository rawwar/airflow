<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# 54 Task Instances

## Overview
Deep dive into task instance lifecycle, states, management, and manipulation in Airflow 3.x.

---

# 54.1 Task Instance Lifecycle

### - [ ] 54.1.1 Task Instance States
Filename: `54_01_01_task_instance_states.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] All possible states (queued, running, success, failed, etc.)
- [ ] State transitions
- [ ] State colors in UI
- [ ] Terminal vs non-terminal states

### - [ ] 54.1.2 Task Instance Creation
Filename: `54_01_02_task_instance_creation.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] When task instances are created
- [ ] Scheduler creates instances
- [ ] Instance per DAG run
- [ ] Dynamic task instance creation

### - [ ] 54.1.3 Task Instance Execution
Filename: `54_01_03_task_instance_execution.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Executor picks up instance
- [ ] Worker execution
- [ ] State updates during execution
- [ ] Heartbeat mechanism

### - [ ] 54.1.4 Task Instance Completion
Filename: `54_01_04_task_instance_completion.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Success state
- [ ] Failed state
- [ ] Skipped state
- [ ] Upstream failed state

### - [ ] 54.1.5 Task Instance Metadata
Filename: `54_01_05_task_instance_metadata.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Access task_instance attributes
- [ ] start_date, end_date, duration
- [ ] try_number, max_tries
- [ ] hostname, executor_config

---

# 54.2 Task Instance States Deep Dive

### - [ ] 54.2.1 Queued State
Filename: `54_02_01_queued_state.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] When tasks enter queued
- [ ] Pool slot waiting
- [ ] Executor queue
- [ ] Stuck in queued diagnosis

### - [ ] 54.2.2 Running State
Filename: `54_02_02_running_state.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Active execution
- [ ] Heartbeat updates
- [ ] Zombie detection
- [ ] Running but stuck

### - [ ] 54.2.3 Deferred State
Filename: `54_02_03_deferred_state.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Deferrable operator state
- [ ] Trigger waiting
- [ ] Worker slot freed
- [ ] Resume from deferred

### - [ ] 54.2.4 Up for Retry State
Filename: `54_02_04_up_for_retry.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Failed but will retry
- [ ] Retry delay
- [ ] Retry count tracking
- [ ] Exponential backoff

### - [ ] 54.2.5 Removed/Shutdown States
Filename: `54_02_05_removed_shutdown.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Removed state meaning
- [ ] Shutdown during execution
- [ ] Recovery scenarios
- [ ] Manual intervention

---

# 54.3 Task Instance Management

### - [ ] 54.3.1 Clearing Task Instances
Filename: `54_03_01_clearing_tasks.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Clear via UI
- [ ] Clear via CLI
- [ ] Downstream clearing
- [ ] Clear with dependencies

### - [ ] 54.3.2 Marking Task Success/Failed
Filename: `54_03_02_marking_tasks.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Mark as success in UI
- [ ] Mark as failed in UI
- [ ] Effect on downstream
- [ ] Use cases

### - [ ] 54.3.3 Task Instance History
Filename: `54_03_03_task_history.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] View past runs
- [ ] Compare attempts
- [ ] Duration trends
- [ ] Failure patterns

### - [ ] 54.3.4 Task Instance Logs
Filename: `54_03_04_task_logs.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Access logs per attempt
- [ ] Log file locations
- [ ] Remote logging
- [ ] Log retention

### - [ ] 54.3.5 Task Instance Notes
Filename: `54_03_05_task_notes.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Add notes to task instances
- [ ] Document manual actions
- [ ] Share context
- [ ] Audit trail

---

# 54.4 Programmatic Task Instance Access

### - [ ] 54.4.1 Access TaskInstance in Task
Filename: `54_04_01_access_in_task.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] context['ti'] or context['task_instance']
- [ ] Available attributes
- [ ] Methods on TaskInstance
- [ ] XCom via TaskInstance

### - [ ] 54.4.2 TaskInstance in Callbacks
Filename: `54_04_02_in_callbacks.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Access in on_success_callback
- [ ] Access in on_failure_callback
- [ ] Modify behavior based on instance
- [ ] Custom logging

### - [ ] 54.4.3 Query TaskInstances via API
Filename: `54_04_03_query_via_api.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] REST API endpoints
- [ ] Filter by state, date, dag
- [ ] Pagination
- [ ] Bulk operations

### - [ ] 54.4.4 TaskInstance in Plugins
Filename: `54_04_04_in_plugins.py` | Tags: `['reference', 'core', 'advanced', 'success']`
- [ ] Access from listener hooks
- [ ] Custom views with instances
- [ ] Monitoring plugins
- [ ] Alerting based on state

### - [ ] 54.4.5 TaskInstance Database Model
Filename: `54_04_05_database_model.py` | Tags: `['reference', 'core', 'advanced', 'success']`
- [ ] TaskInstance table schema
- [ ] Key columns
- [ ] Indexes
- [ ] Direct queries (when appropriate)

---

# 54.5 Task Instance Troubleshooting

### - [ ] 54.5.1 Zombie Tasks
Filename: `54_05_01_zombie_tasks.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] What causes zombies
- [ ] Detection mechanism
- [ ] Automatic cleanup
- [ ] Prevention strategies

### - [ ] 54.5.2 Stuck Tasks
Filename: `54_05_02_stuck_tasks.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Task not progressing
- [ ] Diagnosis steps
- [ ] Manual intervention
- [ ] Root cause analysis

### - [ ] 54.5.3 Duplicate Task Runs
Filename: `54_05_03_duplicate_runs.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] When duplicates occur
- [ ] Detection methods
- [ ] Prevention
- [ ] Idempotency importance

### - [ ] 54.5.4 Task Instance Conflicts
Filename: `54_05_04_instance_conflicts.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Concurrent modification
- [ ] Lock mechanisms
- [ ] Resolution strategies
- [ ] High-availability considerations

### - [ ] 54.5.5 Performance Issues
Filename: `54_05_05_performance_issues.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Slow task instance queries
- [ ] Database optimization
- [ ] Archiving old instances
- [ ] Cleanup strategies

---

# 54.6 Task Instance Operations

## Overview
Advanced operations on task instances.

## Tasks

### - [ ] 54.6.1 Bulk Clear Operations
Filename: `54_06_01_bulk_clear.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Clear by date range
- [ ] Clear by state
- [ ] Clear with downstream
- [ ] Selective clearing

### - [ ] 54.6.2 Task Instance Rerun Patterns
Filename: `54_06_02_rerun_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Clear and rerun
- [ ] Force rerun
- [ ] Partial DAG rerun
- [ ] Idempotency considerations

### - [ ] 54.6.3 Task Instance Priority
Filename: `54_06_03_priority.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Priority weight calculation
- [ ] Upstream priority
- [ ] Manual priority override
- [ ] Pool interaction

### - [ ] 54.6.4 Task Instance Queuing
Filename: `54_06_04_queuing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Queue assignment
- [ ] Queue-specific workers
- [ ] Queue overflow handling
- [ ] Queue monitoring

### - [ ] 54.6.5 Task Instance Pools
Filename: `54_06_05_pools.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Pool slot allocation
- [ ] Priority in pools
- [ ] Waiting tasks
- [ ] Dynamic pool management

---

# 54.7 Task Instance Context

## Overview
Working with task instance context at runtime.

## Tasks

### - [ ] 54.7.1 Context Variables
Filename: `54_07_01_context_variables.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Available context keys
- [ ] Access patterns
- [ ] Common variables
- [ ] Template integration

### - [ ] 54.7.2 Dynamic Context
Filename: `54_07_02_dynamic_context.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Render template fields
- [ ] Runtime value access
- [ ] Params and conf
- [ ] Custom context

### - [ ] 54.7.3 Task Instance Methods
Filename: `54_07_03_instance_methods.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] xcom_push/xcom_pull
- [ ] get_previous_ti
- [ ] get_template_context
- [ ] Utility methods

### - [ ] 54.7.4 Modifying Task Instance
Filename: `54_07_04_modifying_instance.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] State modification
- [ ] Duration updates
- [ ] Note addition
- [ ] External ID tracking

### - [ ] 54.7.5 Task Instance Serialization
Filename: `54_07_05_serialization.py` | Tags: `['reference', 'core', 'advanced', 'success']`
- [ ] JSON serialization
- [ ] API representation
- [ ] Log serialization
- [ ] External export

---

# 54.8 Testing Task Instances

## Overview
Testing task instance behavior and states.

## Tasks

### - [ ] 54.8.1 Unit Testing with Task Instance
Filename: `54_08_01_unit_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Mock task instance
- [ ] Test state transitions
- [ ] Verify XCom
- [ ] Context testing

### - [ ] 54.8.2 Integration Testing
Filename: `54_08_02_integration_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test with real database
- [ ] State verification
- [ ] End-to-end execution
- [ ] Cleanup procedures

### - [ ] 54.8.3 Testing State Transitions
Filename: `54_08_03_state_transitions.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Valid transitions
- [ ] Invalid transitions
- [ ] Edge cases
- [ ] Concurrent access

### - [ ] 54.8.4 Performance Testing
Filename: `54_08_04_performance_testing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Many task instances
- [ ] Query performance
- [ ] State update speed
- [ ] Benchmarking

### - [ ] 54.8.5 Chaos Testing
Filename: `54_08_05_chaos_testing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Kill during execution
- [ ] Database failures
- [ ] Network partitions
- [ ] Recovery verification

---

# 54.9 Monitoring and Alerting

## Overview
Monitoring task instance health and alerting.

## Tasks

### - [ ] 54.9.1 Task Instance Metrics
Filename: `54_09_01_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Duration metrics
- [ ] Success/failure rates
- [ ] Retry counts
- [ ] Queue times

### - [ ] 54.9.2 State-Based Alerting
Filename: `54_09_02_state_alerting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Alert on failure
- [ ] Alert on long running
- [ ] Alert on stuck
- [ ] Escalation rules

### - [ ] 54.9.3 Task Instance Dashboards
Filename: `54_09_03_dashboards.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] State distribution
- [ ] Execution trends
- [ ] Error analysis
- [ ] Performance graphs

### - [ ] 54.9.4 Historical Analysis
Filename: `54_09_04_historical_analysis.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Trend detection
- [ ] Anomaly identification
- [ ] Capacity planning
- [ ] SLA tracking

### - [ ] 54.9.5 Task Instance Audit
Filename: `54_09_05_audit.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] State change history
- [ ] User actions
- [ ] Compliance reporting
- [ ] Forensic analysis

---

# 54.10 Best Practices

## Overview
Best practices for task instance management.

## Tasks

### - [ ] 54.10.1 Task Instance Naming
Filename: `54_10_01_naming.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Meaningful task IDs
- [ ] Consistency patterns
- [ ] Search-friendly names
- [ ] Avoid conflicts

### - [ ] 54.10.2 State Management Patterns
Filename: `54_10_02_state_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Clean state transitions
- [ ] Avoid manual manipulation
- [ ] Atomic operations
- [ ] Consistency maintenance

### - [ ] 54.10.3 Cleanup and Archival
Filename: `54_10_03_cleanup_archival.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Retention policies
- [ ] Archive strategies
- [ ] Space management
- [ ] Compliance requirements

### - [ ] 54.10.4 Anti-Patterns to Avoid
Filename: `54_10_04_anti_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Direct database updates
- [ ] Ignoring zombie detection
- [ ] Manual state hacking
- [ ] Bypassing Airflow APIs

### - [ ] 54.10.5 Documentation Standards
Filename: `54_10_05_documentation.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Document task behavior
- [ ] Expected states
- [ ] Recovery procedures
- [ ] Runbook creation
