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

# 52 Listeners

## Overview

Listeners provide hooks into Airflow's execution lifecycle, allowing custom code to run on events like task start, success, failure, and DAG completion. Listeners enable observability, custom metrics, notifications, and audit logging without modifying DAG code.

## Research & Background

### Key Concepts
- **Listener**: Plugin that responds to Airflow events
- **Hookspec**: Interface definition for listener methods
- **Hookimpl**: Implementation of listener hooks
- **Event Types**: on_task_instance_running, on_task_instance_success, etc.

### Airflow 3.x Features
- Improved listener API
- More event types available
- Better error isolation
- Async listener support

### Prerequisites
- Airflow 3.x
- Understanding of Airflow plugins (Section 34)
- Basic plugin development knowledge

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Create listener plugins
2. Respond to task lifecycle events
3. Implement custom metrics and notifications
4. Build audit logging systems
5. Debug listener issues

---

# 52.1 Listener Basics

## Overview
Fundamentals of creating and registering listeners.

## Tasks

### - [ ] 52.1.1 Creating a Listener Plugin
Filename: `52_01_01_creating_listener_plugin.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Basic listener plugin structure

- [ ] Create plugin file in plugins directory
- [ ] Import listener hookspec
- [ ] Implement listener class
- [ ] Register listener with Airflow

**Expected Behavior**: Listener loads on Airflow start

---

### - [ ] 52.1.2 on_task_instance_running Hook
Filename: `52_01_02_on_task_instance_running.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: React when task starts running

- [ ] Implement on_task_instance_running
- [ ] Access task_instance, context
- [ ] Log task start information
- [ ] Example: notify start

**Expected Behavior**: Hook fires on task start

---

### - [ ] 52.1.3 on_task_instance_success Hook
Filename: `52_01_03_on_task_instance_success.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: React when task succeeds

- [ ] Implement on_task_instance_success
- [ ] Access return value if available
- [ ] Log success metrics
- [ ] Example: record completion time

**Expected Behavior**: Hook fires on task success

---

### - [ ] 52.1.4 on_task_instance_failed Hook
Filename: `52_01_04_on_task_instance_failed.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: React when task fails

- [ ] Implement on_task_instance_failed
- [ ] Access exception information
- [ ] Log failure details
- [ ] Example: alert on failure

**Expected Behavior**: Hook fires on task failure

---

### - [ ] 52.1.5 DAG-Level Listeners
Filename: `52_01_05_dag_level_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Respond to DAG run events

- [ ] on_dag_run_running
- [ ] on_dag_run_success
- [ ] on_dag_run_failed
- [ ] DAG-wide metrics

**Expected Behavior**: DAG events captured

---

### - [ ] 52.1.6 Multiple Listeners
Filename: `52_01_06_multiple_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Multiple listeners for same events

- [ ] Multiple listener classes
- [ ] Execution order
- [ ] Isolation between listeners
- [ ] One listener failure doesn't affect others

**Expected Behavior**: Multiple listeners coexist

---

# 52.2 Listener Use Cases

## Overview
Practical applications of listeners.

## Tasks

### - [ ] 52.2.1 Custom Metrics Emission
Filename: `52_02_01_custom_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Send metrics to monitoring system

- [ ] Listener emits StatsD/Prometheus metrics
- [ ] Task duration, success rate
- [ ] Custom business metrics
- [ ] DAG-level aggregations

**Expected Behavior**: Metrics visible in monitoring

---

### - [ ] 52.2.2 External Notification System
Filename: `52_02_02_external_notifications.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Send notifications on events

- [ ] Slack/Teams notifications
- [ ] Email on failure
- [ ] PagerDuty integration
- [ ] Conditional notifications

**Expected Behavior**: Notifications sent on events

---

### - [ ] 52.2.3 Audit Logging
Filename: `52_02_03_audit_logging.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Log all task executions for audit

- [ ] Log task start, end, duration
- [ ] Log user, dag_id, task_id
- [ ] External audit log sink
- [ ] Compliance requirements

**Expected Behavior**: Complete audit trail

---

### - [ ] 52.2.4 Custom Alerting Rules
Filename: `52_02_04_custom_alerting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Complex alerting logic

- [ ] Alert on repeated failures
- [ ] Alert on SLA breaches
- [ ] Alert on specific task patterns
- [ ] Aggregation before alerting

**Expected Behavior**: Smart alerting works

---

### - [ ] 52.2.5 Resource Usage Tracking
Filename: `52_02_05_resource_usage_tracking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Track resource consumption

- [ ] Record task memory/CPU usage
- [ ] Execution time tracking
- [ ] Cost allocation
- [ ] Capacity planning data

**Expected Behavior**: Resource data collected

---

### - [ ] 52.2.6 Data Lineage Events
Filename: `52_02_06_data_lineage_events.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Emit lineage events to external system

- [ ] Capture inlet/outlet assets
- [ ] Send to lineage system (OpenLineage)
- [ ] Enrich with task metadata
- [ ] Cross-DAG lineage

**Expected Behavior**: Lineage events emitted

---

# 52.3 Listener Implementation Details

## Overview
Deep dive into listener implementation.

## Tasks

### - [ ] 52.3.1 Listener Method Signatures
Filename: `52_03_01_method_signatures.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Correct listener method signatures

- [ ] Available parameters for each hook
- [ ] task_instance, context, exception
- [ ] Accessing DAG and task info
- [ ] Return values (if any)

**Expected Behavior**: Correct method signatures

---

### - [ ] 52.3.2 Accessing Task Instance Data
Filename: `52_03_02_accessing_task_instance.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Extract useful data from task instance

- [ ] task_instance.dag_id, task_id
- [ ] task_instance.execution_date
- [ ] task_instance.state
- [ ] task_instance.duration

**Expected Behavior**: Task data accessible

---

### - [ ] 52.3.3 Accessing Context Data
Filename: `52_03_03_accessing_context.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use context in listeners

- [ ] context['dag_run']
- [ ] context['params']
- [ ] context['conf']
- [ ] Template variables

**Expected Behavior**: Context data accessible

---

### - [ ] 52.3.4 Error Handling in Listeners
Filename: `52_03_04_error_handling_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle errors without affecting tasks

- [ ] Listener exceptions are caught
- [ ] Tasks not affected by listener errors
- [ ] Logging listener errors
- [ ] Retry logic in listeners

**Expected Behavior**: Errors isolated

---

### - [ ] 52.3.5 Async Listeners
Filename: `52_03_05_async_listeners.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Non-blocking listener implementations

- [ ] Async listener methods
- [ ] Queue events for processing
- [ ] Background processing
- [ ] Performance considerations

**Expected Behavior**: Listeners don't slow tasks

---

### - [ ] 52.3.6 Listener Configuration
Filename: `52_03_06_listener_configuration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure listeners via settings

- [ ] Environment variables for listeners
- [ ] Airflow Variables for config
- [ ] Connection for external services
- [ ] Conditional listener loading

**Expected Behavior**: Configurable listeners

---

# 52.4 Testing and Debugging Listeners

## Overview
Testing listeners and troubleshooting issues.

## Tasks

### - [ ] 52.4.1 Unit Testing Listeners
Filename: `52_04_01_unit_testing_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Test listener logic

- [ ] Mock task_instance and context
- [ ] Test hook implementations
- [ ] Assert expected behavior
- [ ] pytest patterns

**Expected Behavior**: Listeners tested

---

### - [ ] 52.4.2 Integration Testing Listeners
Filename: `52_04_02_integration_testing_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Test listeners with real Airflow

- [ ] Run DAG and verify listener fired
- [ ] Check external system received events
- [ ] End-to-end listener testing
- [ ] CI/CD integration

**Expected Behavior**: Listeners work in Airflow

---

### - [ ] 52.4.3 Debugging Listener Issues
Filename: `52_04_03_debugging_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Troubleshoot listener problems

- [ ] Listener not loading
- [ ] Hook not firing
- [ ] Exception in listener
- [ ] Log inspection

**Expected Behavior**: Issues diagnosed

---

### - [ ] 52.4.4 Listener Performance Impact
Filename: `52_04_04_listener_performance.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Minimize listener overhead

- [ ] Measure listener execution time
- [ ] Async vs sync listeners
- [ ] Batching events
- [ ] Avoiding slow operations

**Expected Behavior**: Minimal performance impact

---

# Summary

## Topic Completion Checklist
- [ ] Listener plugin creation documented
- [ ] All common hooks covered
- [ ] Practical use cases included
- [ ] Implementation details explained
- [ ] Testing approaches provided

## Related Topics
- Section 34: Plugins and Extensions (plugin basics)
- Section 12: Callbacks and Notifications (task callbacks)
- Section 19: Logging and Monitoring (observability)

## Notes for Implementation
- Create actual plugin files for testing
- Show logs demonstrating listener execution
- Include external service mocks
- Test error isolation
- Document all available hooks

---

# 52.5 Advanced Listener Patterns

## Overview
Advanced patterns for production-grade listeners.

## Tasks

### - [ ] 52.5.1 Event Aggregation Listener
Filename: `52_05_01_event_aggregation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Collect events before processing
- [ ] Batch notifications
- [ ] Window-based aggregation
- [ ] Memory management

### - [ ] 52.5.2 Correlation ID Tracking
Filename: `52_05_02_correlation_tracking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Track across tasks
- [ ] Inject correlation IDs
- [ ] Log aggregation support
- [ ] Distributed tracing

### - [ ] 52.5.3 Event Filtering Listener
Filename: `52_05_03_event_filtering.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Filter by DAG/task
- [ ] Conditional processing
- [ ] Tag-based filtering
- [ ] Dynamic filters

### - [ ] 52.5.4 Event Replay Capability
Filename: `52_05_04_event_replay.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Store events for replay
- [ ] Recovery scenarios
- [ ] Audit requirements
- [ ] Event sourcing patterns

### - [ ] 52.5.5 Multi-Tenant Listener
Filename: `52_05_05_multi_tenant.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Route by tenant
- [ ] Isolated processing
- [ ] Tenant-specific config
- [ ] Scalability considerations

---

# 52.6 External Integrations

## Overview
Integrating listeners with external systems.

## Tasks

### - [ ] 52.6.1 Slack Integration Listener
Filename: `52_06_01_slack_integration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Slack webhook integration
- [ ] Message formatting
- [ ] Channel routing
- [ ] Rate limiting

### - [ ] 52.6.2 PagerDuty Integration
Filename: `52_06_02_pagerduty_integration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Alert on failures
- [ ] Severity mapping
- [ ] Deduplication
- [ ] Acknowledgment handling

### - [ ] 52.6.3 Datadog Metrics Listener
Filename: `52_06_03_datadog_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Custom metrics emission
- [ ] Tag management
- [ ] APM integration
- [ ] Dashboard creation

### - [ ] 52.6.4 Elasticsearch Event Logging
Filename: `52_06_04_elasticsearch_logging.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Index task events
- [ ] Structured logging
- [ ] Search and analysis
- [ ] Retention management

### - [ ] 52.6.5 Apache Kafka Event Stream
Filename: `52_06_05_kafka_events.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Publish to Kafka topics
- [ ] Event serialization
- [ ] Schema registry
- [ ] Consumer patterns

---

# 52.7 Listener Lifecycle Management

## Overview
Managing listener lifecycle and deployment.

## Tasks

### - [ ] 52.7.1 Listener Loading Mechanism
Filename: `52_07_01_loading_mechanism.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Plugin discovery
- [ ] Load order
- [ ] Conditional loading
- [ ] Version compatibility

### - [ ] 52.7.2 Listener Versioning
Filename: `52_07_02_versioning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Version listener code
- [ ] Backward compatibility
- [ ] Migration strategies
- [ ] Rollback procedures

### - [ ] 52.7.3 Listener Deployment
Filename: `52_07_03_deployment.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Package as plugin
- [ ] CI/CD integration
- [ ] Testing before deploy
- [ ] Rollback strategy

### - [ ] 52.7.4 Feature Flags for Listeners
Filename: `52_07_04_feature_flags.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Enable/disable listeners
- [ ] Gradual rollout
- [ ] A/B testing listeners
- [ ] Emergency disable

### - [ ] 52.7.5 Listener Documentation
Filename: `52_07_05_documentation.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Document hook behavior
- [ ] Configuration options
- [ ] Usage examples
- [ ] Troubleshooting guide

---

# 52.8 Anti-Patterns and Best Practices

## Overview
Common mistakes and recommended practices.

## Tasks

### - [ ] 52.8.1 Heavy Operations in Listeners
Filename: `52_08_01_heavy_operations.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Blocking calls
- [ ] Long-running operations
- [ ] Task impact
- [ ] Async alternatives

### - [ ] 52.8.2 Listener Exception Handling
Filename: `52_08_02_exception_handling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Catch all exceptions
- [ ] Log errors properly
- [ ] Avoid cascade failures
- [ ] Graceful degradation

### - [ ] 52.8.3 State in Listeners
Filename: `52_08_03_state_in_listeners.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Avoid global state
- [ ] Thread safety
- [ ] Process isolation
- [ ] Stateless patterns

### - [ ] 52.8.4 Testing Without Side Effects
Filename: `52_08_04_testing_side_effects.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Mock external calls
- [ ] Verify listener behavior
- [ ] Isolated testing
- [ ] CI integration

### - [ ] 52.8.5 Listener Security
Filename: `52_08_05_listener_security.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Credential handling
- [ ] Data masking
- [ ] Audit compliance
- [ ] Secure communication

---

# 52.9 Monitoring and Observability

## Overview
Monitoring listener health and behavior.

## Tasks

### - [ ] 52.9.1 Listener Health Metrics
Filename: `52_09_01_health_metrics.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Execution count
- [ ] Error rates
- [ ] Latency tracking
- [ ] Custom metrics

### - [ ] 52.9.2 Listener Logging Strategy
Filename: `52_09_02_logging_strategy.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Structured logging
- [ ] Log levels
- [ ] Context inclusion
- [ ] Log aggregation

### - [ ] 52.9.3 Alerting on Listener Failures
Filename: `52_09_03_alerting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Error threshold alerts
- [ ] Silent failure detection
- [ ] Escalation procedures
- [ ] Recovery notification

### - [ ] 52.9.4 Listener Dashboards
Filename: `52_09_04_dashboards.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Event volume graphs
- [ ] Error tracking
- [ ] Latency charts
- [ ] Business metrics

### - [ ] 52.9.5 Troubleshooting Guide
Filename: `52_09_05_troubleshooting.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Common issues
- [ ] Diagnostic steps
- [ ] Log analysis
- [ ] Resolution procedures

---

# 52.10 Real-World Examples

## Overview
Production listener implementations.

## Tasks

### - [ ] 52.10.1 SLA Monitoring Listener
Filename: `52_10_01_sla_monitoring.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Track SLA compliance
- [ ] Early warning alerts
- [ ] Historical analysis
- [ ] Reporting integration

### - [ ] 52.10.2 Cost Tracking Listener
Filename: `52_10_02_cost_tracking.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Track task resources
- [ ] Cloud cost attribution
- [ ] Budget alerts
- [ ] Optimization insights

### - [ ] 52.10.3 Data Quality Listener
Filename: `52_10_03_data_quality.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Track data metrics
- [ ] Quality alerts
- [ ] Trend analysis
- [ ] Integration with DQ tools

### - [ ] 52.10.4 Workflow Analytics Listener
Filename: `52_10_04_workflow_analytics.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Task execution patterns
- [ ] Bottleneck detection
- [ ] Optimization recommendations
- [ ] Historical trends

### - [ ] 52.10.5 Compliance Audit Listener
Filename: `52_10_05_compliance_audit.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Regulatory compliance
- [ ] Access logging
- [ ] Data handling audit
- [ ] Report generation
