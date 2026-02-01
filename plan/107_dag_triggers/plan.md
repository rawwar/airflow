# 107 DAG Triggers

## Overview

Manual and programmatic DAG triggering in Apache Airflow 3.x, covering UI triggers, CLI triggers, REST API triggers, external event triggers, and trigger rules for complex workflow orchestration.

## Airflow 3.x Notes
- REST API v2 for programmatic triggers
- Asset-based triggering (replaces Dataset)
- TriggerDagRunOperator for DAG chaining
- `logical_date` replaces deprecated `execution_date`
- trigger_rule parameter for task-level control

---

# 107.1 Manual Triggers

## Overview
Triggering DAGs manually through various interfaces.

## Tasks

### - [ ] 107.1.1 UI-Based Trigger
Filename: `107_01_01_ui_trigger.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Trigger DAG from web UI

- [ ] Navigate to DAG detail
- [ ] Click trigger button
- [ ] Pass configuration JSON
- [ ] View triggered run
- [ ] Monitor execution

**Expected Behavior**: DAG triggered via UI

---

### - [ ] 107.1.2 CLI Trigger Command
Filename: `107_01_02_cli_trigger.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Trigger DAG from command line

- [ ] airflow dags trigger command
- [ ] Pass --conf parameter
- [ ] Specify logical_date
- [ ] Trigger specific run_id
- [ ] Verify trigger success

**Expected Behavior**: DAG triggered via CLI

---

### - [ ] 107.1.3 Trigger with Configuration
Filename: `107_01_03_trigger_with_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Pass runtime configuration

- [ ] Define conf schema
- [ ] Trigger with JSON config
- [ ] Access conf in tasks
- [ ] Validate conf values
- [ ] Default conf handling

**Expected Behavior**: Config-driven execution

---

### - [ ] 107.1.4 Trigger with Specific logical_date
Filename: `107_01_04_trigger_logical_date.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Run for specific date

- [ ] Specify logical_date on trigger
- [ ] Data interval implications
- [ ] Idempotent reruns
- [ ] Historical backfill
- [ ] Future date handling

**Expected Behavior**: Date-specific runs

---

### - [ ] 107.1.5 Bulk Trigger Patterns
Filename: `107_01_05_bulk_trigger.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger multiple runs

- [ ] Loop trigger for date range
- [ ] Parallel trigger considerations
- [ ] Rate limiting
- [ ] Progress tracking
- [ ] Error handling

**Expected Behavior**: Efficient bulk triggering

---

# 107.2 REST API Triggers

## Overview
Programmatic triggering via REST API.

## Tasks

### - [ ] 107.2.1 API Trigger Endpoint
Filename: `107_02_01_api_trigger.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger via REST API

- [ ] POST to /api/v2/dags/{dag_id}/dagRuns
- [ ] Authentication headers
- [ ] Request body format
- [ ] Response handling
- [ ] Error responses

**Expected Behavior**: API trigger working

---

### - [ ] 107.2.2 API Trigger with Configuration
Filename: `107_02_02_api_trigger_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Pass conf via API

- [ ] Include conf in request body
- [ ] JSON serialization
- [ ] Size limitations
- [ ] Validation errors
- [ ] Access in DAG

**Expected Behavior**: Config passed via API

---

### - [ ] 107.2.3 Webhook-Style Triggers
Filename: `107_02_03_webhook_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Webhook integration

- [ ] External webhook to Airflow
- [ ] Transform webhook payload
- [ ] Map to DAG conf
- [ ] Security considerations
- [ ] Replay handling

**Expected Behavior**: Webhook-triggered DAGs

---

### - [ ] 107.2.4 API Trigger from CI/CD
Filename: `107_02_04_cicd_trigger.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger from pipelines

- [ ] GitHub Actions integration
- [ ] GitLab CI integration
- [ ] Jenkins trigger
- [ ] Artifact passing
- [ ] Status callback

**Expected Behavior**: CI/CD integrated triggers

---

### - [ ] 107.2.5 Idempotent API Triggers
Filename: `107_02_05_idempotent_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Safe retrigger handling

- [ ] run_id for idempotency
- [ ] Check existing runs
- [ ] Prevent duplicates
- [ ] Retry safety
- [ ] State verification

**Expected Behavior**: Safe repeated triggers

---

# 107.3 DAG-to-DAG Triggers

## Overview
Triggering DAGs from within other DAGs.

## Tasks

### - [ ] 107.3.1 TriggerDagRunOperator
Filename: `107_03_01_trigger_dag_run_operator.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger another DAG from task

- [ ] Basic TriggerDagRunOperator usage
- [ ] Pass configuration
- [ ] Wait for completion
- [ ] Handle failures
- [ ] Execution date handling

**Expected Behavior**: DAG chains working

---

### - [ ] 107.3.2 Dynamic DAG Triggering
Filename: `107_03_02_dynamic_dag_trigger.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Dynamically choose DAG to trigger

- [ ] DAG ID from variable
- [ ] DAG ID from XCom
- [ ] Conditional triggering
- [ ] Multiple DAG triggers
- [ ] Fan-out patterns

**Expected Behavior**: Flexible DAG orchestration

---

### - [ ] 107.3.3 Pass Data Between DAGs
Filename: `107_03_03_cross_dag_data.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Share data across DAGs

- [ ] Configuration passing
- [ ] XCom cross-DAG access
- [ ] External storage pattern
- [ ] Asset-based data passing
- [ ] Large data handling

**Expected Behavior**: Data flows between DAGs

---

### - [ ] 107.3.4 Wait for Triggered DAG
Filename: `107_03_04_wait_for_completion.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Block until child completes

- [ ] wait_for_completion=True
- [ ] Timeout handling
- [ ] Poll interval
- [ ] Failure propagation
- [ ] Partial success handling

**Expected Behavior**: Parent waits for child

---

### - [ ] 107.3.5 Recursive/Self-Triggering DAGs
Filename: `107_03_05_self_trigger.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: DAG triggers itself

- [ ] Use case scenarios
- [ ] Termination conditions
- [ ] Recursion depth limits
- [ ] State management
- [ ] Avoiding infinite loops

**Expected Behavior**: Safe self-triggering

---

# 107.4 Event-Based Triggers

## Overview
Triggering DAGs based on external events.

## Tasks

### - [ ] 107.4.1 Asset-Based Triggering
Filename: `107_04_01_asset_triggering.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger on asset updates

- [ ] Define asset outlet
- [ ] Define asset inlet
- [ ] Automatic triggering
- [ ] Multiple asset dependencies
- [ ] Asset URI patterns

**Expected Behavior**: Asset-driven scheduling

---

### - [ ] 107.4.2 ExternalTaskSensor Triggers
Filename: `107_04_02_external_task_sensor.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Wait for external task

- [ ] Configure ExternalTaskSensor
- [ ] execution_date_fn
- [ ] Timeout handling
- [ ] Poke vs reschedule mode
- [ ] Failure modes

**Expected Behavior**: Cross-DAG coordination

---

### - [ ] 107.4.3 File-Based Triggers
Filename: `107_04_03_file_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger on file arrival

- [ ] FileSensor patterns
- [ ] Cloud storage sensors
- [ ] Trigger on file creation
- [ ] File pattern matching
- [ ] Cleanup after processing

**Expected Behavior**: File-driven workflows

---

### - [ ] 107.4.4 Message Queue Triggers
Filename: `107_04_04_message_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger from message queue

- [ ] Kafka trigger patterns
- [ ] SQS/Pub-Sub sensors
- [ ] Message to DAG config
- [ ] Acknowledgment handling
- [ ] Batch processing

**Expected Behavior**: Message-driven DAGs

---

### - [ ] 107.4.5 Database Change Triggers
Filename: `107_04_05_database_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger on data changes

- [ ] SQL sensor patterns
- [ ] Change data capture
- [ ] Polling strategies
- [ ] Trigger on threshold
- [ ] Idempotent processing

**Expected Behavior**: Data-driven triggers

---

# 107.5 Trigger Rules

## Overview
Task-level trigger rules for complex workflows.

## Tasks

### - [ ] 107.5.1 Default trigger_rule Behavior
Filename: `107_05_01_default_trigger_rule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand all_success default

- [ ] all_success rule
- [ ] Upstream success requirement
- [ ] Failure propagation
- [ ] Skip propagation
- [ ] Visualization in UI

**Expected Behavior**: Default behavior understood

---

### - [ ] 107.5.2 all_failed and one_failed Rules
Filename: `107_05_02_failure_rules.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle failure scenarios

- [ ] all_failed trigger rule
- [ ] one_failed trigger rule
- [ ] Error handling tasks
- [ ] Cleanup on failure
- [ ] Notification patterns

**Expected Behavior**: Failure handling works

---

### - [ ] 107.5.3 all_done and none_skipped Rules
Filename: `107_05_03_completion_rules.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Run regardless of status

- [ ] all_done rule
- [ ] none_skipped rule
- [ ] Cleanup tasks
- [ ] Always-run patterns
- [ ] Status aggregation

**Expected Behavior**: Tasks run on completion

---

### - [ ] 107.5.4 one_success and none_failed Rules
Filename: `107_05_04_success_rules.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Partial success handling

- [ ] one_success rule
- [ ] none_failed rule
- [ ] First-win patterns
- [ ] Parallel alternatives
- [ ] Aggregation tasks

**Expected Behavior**: Flexible success criteria

---

### - [ ] 107.5.5 Complex Trigger Rule Patterns
Filename: `107_05_05_complex_rules.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Combine trigger rules

- [ ] Mixed rule workflows
- [ ] Branching with rules
- [ ] Conditional execution
- [ ] State machine patterns
- [ ] Testing trigger rules

**Expected Behavior**: Complex flows work correctly

---

# 107.6 Trigger Anti-Patterns

## Overview
Common mistakes in DAG triggering.

## Tasks

### - [ ] 107.6.1 Trigger Loops
Filename: `107_06_01_trigger_loops.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid infinite trigger cycles

- [ ] DAG A triggers B triggers A
- [ ] Detection methods
- [ ] Loop breaking strategies
- [ ] Safeguards implementation
- [ ] Proper dependency design

**Expected Behavior**: Loop risks understood

---

### - [ ] 107.6.2 Trigger Without Idempotency
Filename: `107_06_02_no_idempotency.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle duplicate triggers

- [ ] Duplicate run creation
- [ ] Data duplication issues
- [ ] run_id importance
- [ ] Idempotent task design
- [ ] Proper implementation

**Expected Behavior**: Idempotency ensured

---

### - [ ] 107.6.3 Over-Triggering
Filename: `107_06_03_over_triggering.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Prevent trigger floods

- [ ] Event storm scenarios
- [ ] Resource exhaustion
- [ ] Rate limiting importance
- [ ] Debouncing strategies
- [ ] Proper event handling

**Expected Behavior**: Trigger rate controlled

---

### - [ ] 107.6.4 Tight Coupling via Triggers
Filename: `107_06_04_tight_coupling.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid excessive DAG dependencies

- [ ] DAG spaghetti patterns
- [ ] Maintenance complexity
- [ ] Testing difficulties
- [ ] Decoupling strategies
- [ ] Asset-based alternatives

**Expected Behavior**: Loose coupling achieved

---

### - [ ] 107.6.5 Missing Trigger Monitoring
Filename: `107_06_05_no_monitoring.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Track trigger health

- [ ] Silent trigger failures
- [ ] Undetected delays
- [ ] Missing audit trail
- [ ] Proper monitoring setup
- [ ] Alert configuration

**Expected Behavior**: Triggers monitored

---

# 107.7 Testing DAG Triggers

## Overview
Validating trigger behavior.

## Tasks

### - [ ] 107.7.1 Unit Testing Trigger Logic
Filename: `107_07_01_unit_test_triggers.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test trigger configurations

- [ ] Test trigger rule logic
- [ ] Mock upstream task states
- [ ] Verify expected behavior
- [ ] Edge case coverage
- [ ] pytest patterns

**Expected Behavior**: Trigger logic validated

---

### - [ ] 107.7.2 Integration Testing Triggers
Filename: `107_07_02_integration_test.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: End-to-end trigger testing

- [ ] Trigger via API in tests
- [ ] Verify DAG execution
- [ ] Configuration passing
- [ ] State verification
- [ ] Cleanup after tests

**Expected Behavior**: Full trigger flow tested

---

### - [ ] 107.7.3 Testing TriggerDagRunOperator
Filename: `107_07_03_test_trigger_operator.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate DAG chaining

- [ ] Mock triggered DAG
- [ ] Verify configuration passing
- [ ] Test wait_for_completion
- [ ] Failure handling tests
- [ ] Timeout behavior

**Expected Behavior**: Operator behavior verified

---

### - [ ] 107.7.4 Testing Event-Based Triggers
Filename: `107_07_04_test_event_triggers.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Validate event triggering

- [ ] Simulate Asset events
- [ ] Test sensor triggering
- [ ] File arrival simulation
- [ ] Message queue mocking
- [ ] Event payload validation

**Expected Behavior**: Event triggers validated

---

### - [ ] 107.7.5 Trigger Performance Testing
Filename: `107_07_05_performance_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Measure trigger latency

- [ ] Trigger-to-execution latency
- [ ] High-volume trigger tests
- [ ] Concurrent trigger handling
- [ ] Bottleneck identification
- [ ] Performance baselines

**Expected Behavior**: Trigger performance known

---

# 107.8 Trigger Debugging

## Overview
Troubleshooting trigger issues.

## Tasks

### - [ ] 107.8.1 Debugging Failed Triggers
Filename: `107_08_01_debug_failed.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Find trigger failures

- [ ] Check scheduler logs
- [ ] API response analysis
- [ ] DAG parse errors
- [ ] Configuration issues
- [ ] Permission problems

**Expected Behavior**: Failure cause found

---

### - [ ] 107.8.2 Debugging Trigger Rules
Filename: `107_08_02_debug_rules.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Understand rule behavior

- [ ] Upstream state analysis
- [ ] Rule evaluation logic
- [ ] Skip propagation
- [ ] UI visualization
- [ ] Common misconceptions

**Expected Behavior**: Rule behavior understood

---

### - [ ] 107.8.3 Debugging Cross-DAG Triggers
Filename: `107_08_03_debug_cross_dag.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Troubleshoot DAG chains

- [ ] Verify DAG exists and unpaused
- [ ] Check triggered run state
- [ ] Configuration validation
- [ ] Execution date alignment
- [ ] Log correlation

**Expected Behavior**: Cross-DAG issues resolved

---

### - [ ] 107.8.4 Debugging Asset Triggers
Filename: `107_08_04_debug_assets.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Fix Asset triggering

- [ ] Verify outlet emissions
- [ ] Check inlet configurations
- [ ] Asset event logs
- [ ] URI matching issues
- [ ] Scheduler Asset handling

**Expected Behavior**: Asset triggers working

---

### - [ ] 107.8.5 Trigger Audit Trail
Filename: `107_08_05_audit_trail.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Track trigger history

- [ ] Query DAG runs by trigger
- [ ] Identify trigger source
- [ ] Configuration history
- [ ] User action tracking
- [ ] API call logging

**Expected Behavior**: Trigger history accessible

---

# 107.9 Advanced Trigger Patterns

## Overview
Complex triggering scenarios.

## Tasks

### - [ ] 107.9.1 Conditional Trigger Pipeline
Filename: `107_09_01_conditional_pipeline.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Trigger based on conditions

- [ ] Evaluate runtime conditions
- [ ] Choose target DAG dynamically
- [ ] Pass conditional parameters
- [ ] Handle no-trigger scenarios
- [ ] Logging decisions

**Expected Behavior**: Smart triggering

---

### - [ ] 107.9.2 Trigger with Retries
Filename: `107_09_02_trigger_retries.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Robust trigger handling

- [ ] Retry failed triggers
- [ ] Exponential backoff
- [ ] Max retry limits
- [ ] Alert on exhaustion
- [ ] Idempotent retry

**Expected Behavior**: Reliable triggering

---

### - [ ] 107.9.3 Scheduled with Event Override
Filename: `107_09_03_schedule_event_override.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Combine schedules and events

- [ ] Regular scheduled runs
- [ ] Event-triggered overrides
- [ ] Avoid duplicate runs
- [ ] Priority handling
- [ ] Configuration merging

**Expected Behavior**: Flexible triggering

---

### - [ ] 107.9.4 Multi-Environment Triggers
Filename: `107_09_04_multi_env_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Cross-environment orchestration

- [ ] Trigger across environments
- [ ] API authentication per env
- [ ] Environment-specific config
- [ ] Security considerations
- [ ] Monitoring cross-env

**Expected Behavior**: Multi-env triggers working

---

### - [ ] 107.9.5 Trigger Aggregation
Filename: `107_09_05_trigger_aggregation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Batch multiple triggers

- [ ] Collect trigger requests
- [ ] Aggregate within window
- [ ] Single DAG run for batch
- [ ] Metadata aggregation
- [ ] Window configuration

**Expected Behavior**: Efficient trigger handling

---

# 107.10 Real-World Trigger Examples

## Overview
Production trigger scenarios.

## Tasks

### - [ ] 107.10.1 Data Pipeline Chain
Filename: `107_10_01_data_pipeline_chain.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

**Purpose**: ETL pipeline triggering

- [ ] Ingest triggers transform
- [ ] Transform triggers load
- [ ] Load triggers reporting
- [ ] Error handling chain
- [ ] Recovery procedures

**Expected Behavior**: Data pipeline flowing

---

### - [ ] 107.10.2 CI/CD Triggered Workflows
Filename: `107_10_02_cicd_workflows.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`

**Purpose**: DevOps integration

- [ ] GitHub webhook trigger
- [ ] Build artifact passing
- [ ] Test pipeline trigger
- [ ] Deploy on success
- [ ] Rollback on failure

**Expected Behavior**: CI/CD integrated

---

### - [ ] 107.10.3 Event-Driven Data Lake
Filename: `107_10_03_data_lake_events.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`

**Purpose**: File-driven processing

- [ ] S3 event notification
- [ ] File arrival trigger
- [ ] Dynamic file processing
- [ ] Partition management
- [ ] Catalog updates

**Expected Behavior**: Data lake automated

---

### - [ ] 107.10.4 Multi-Tenant Triggering
Filename: `107_10_04_multi_tenant.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`

**Purpose**: Per-tenant workflows

- [ ] Tenant-specific triggers
- [ ] Configuration per tenant
- [ ] Isolation guarantees
- [ ] Shared infrastructure
- [ ] Tenant monitoring

**Expected Behavior**: Multi-tenant isolated

---

### - [ ] 107.10.5 Microservice Orchestration
Filename: `107_10_05_microservice_orch.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`

**Purpose**: Service coordination

- [ ] Service completion triggers
- [ ] Saga pattern implementation
- [ ] Compensation handling
- [ ] Distributed transactions
- [ ] Service health checks

**Expected Behavior**: Services orchestrated

---

# Summary

## Topic Completion Checklist
- [ ] Manual triggers covered
- [ ] API triggers documented
- [ ] DAG-to-DAG triggers explained
- [ ] Event-based triggers addressed
- [ ] Trigger rules detailed
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Debugging techniques included
- [ ] Advanced patterns documented
- [ ] Real-world examples provided

## Related Topics
- Section 11: Assets
- Section 08: Sensors
- Section 48: REST API
- Section 53: DAG Dependencies

## Notes for Implementation
- Test trigger scenarios thoroughly
- Handle idempotency
- Monitor trigger latency
- Document trigger sources
- Plan for trigger failures
