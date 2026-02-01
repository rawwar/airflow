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

# 51 Deferrable Operators

## Overview

Deferrable operators allow tasks to release their worker slot while waiting for external conditions, dramatically improving resource efficiency. Instead of blocking a worker process, deferrable tasks suspend and resume via the triggerer component.

## Research & Background

### Key Concepts
- **Deferrable**: Task that can suspend execution and free worker slot
- **Trigger**: Async component that monitors conditions in the triggerer
- **Triggerer**: Airflow component running async event loops
- **defer()**: Method to suspend task execution
- **TriggerEvent**: Signal from trigger that resumes task

### Airflow 3.x Features
- Built-in deferrable sensors (DateTimeSensorAsync, TimeSensorAsync)
- deferrable=True parameter on many sensors
- Custom trigger development
- Improved triggerer scalability

### Prerequisites
- Airflow 3.x with triggerer running
- Understanding of sensors (Section 08)
- Basic async Python knowledge for custom triggers

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Use built-in deferrable sensors for efficient waiting
2. Convert blocking sensors to deferrable mode
3. Create custom deferrable operators
4. Implement custom triggers for external systems
5. Debug deferrable task issues

---

# 51.1 Deferrable Operator Fundamentals

## Overview
Understanding how deferrable execution works and when to use it.

## Tasks

### - [ ] 51.1.1 What is Deferrable Execution
Filename: `51_01_01_deferrable_execution_intro.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand deferrable execution model

- [ ] Compare blocking vs deferrable sensor
- [ ] Show worker slot usage difference
- [ ] Explain trigger and triggerer roles
- [ ] When to use deferrable operators

**Expected Behavior**: Clear understanding of deferrable model

---

### - [ ] 51.1.2 Resource Savings Demonstration
Filename: `51_01_02_resource_savings.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Show resource efficiency of deferrable tasks

- [ ] DAG with multiple waiting tasks
- [ ] Blocking mode: N workers occupied
- [ ] Deferrable mode: 0 workers occupied while waiting
- [ ] Measure and log resource difference

**Expected Behavior**: Dramatic resource savings visible

---

### - [ ] 51.1.3 Triggerer Architecture
Filename: `51_01_03_triggerer_architecture.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand triggerer component

- [ ] Triggerer as separate Airflow process
- [ ] Async event loop processing triggers
- [ ] Multiple triggers per triggerer
- [ ] Triggerer scalability

**Expected Behavior**: Understanding of triggerer role

---

### - [ ] 51.1.4 Deferrable Task Lifecycle
Filename: `51_01_04_deferrable_lifecycle.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand deferrable task states

- [ ] Running → Deferred → Triggered → Running
- [ ] Task states in UI
- [ ] Trigger registration and cleanup
- [ ] Error handling in deferred state

**Expected Behavior**: Clear lifecycle understanding

---

# 51.2 Built-in Deferrable Sensors

## Overview
Using Airflow's built-in deferrable sensors.

## Tasks

### - [ ] 51.2.1 TimeSensorAsync
Filename: `51_02_01_time_sensor_async.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Wait for specific time without blocking

- [ ] TimeSensorAsync instead of TimeSensor
- [ ] target_time parameter
- [ ] Frees worker while waiting
- [ ] Compare to blocking TimeSensor

**Expected Behavior**: Non-blocking time wait

---

### - [ ] 51.2.2 DateTimeSensorAsync
Filename: `51_02_02_datetime_sensor_async.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Wait for specific datetime efficiently

- [ ] DateTimeSensorAsync usage
- [ ] target_datetime parameter
- [ ] Timezone handling
- [ ] Long duration waits

**Expected Behavior**: Efficient datetime waiting

---

### - [ ] 51.2.3 Sensor deferrable Parameter
Filename: `51_02_03_sensor_deferrable_param.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Enable deferrable mode on compatible sensors

- [ ] BaseSensorOperator with deferrable=True
- [ ] Sensors that support deferrable parameter
- [ ] Automatic trigger selection
- [ ] Fallback behavior

**Expected Behavior**: Sensors run in deferrable mode

---

### - [ ] 51.2.4 FileSensor in Deferrable Mode
Filename: `51_02_04_file_sensor_deferrable.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Deferrable file waiting

- [ ] FileSensor with deferrable=True
- [ ] Async file existence check
- [ ] Comparison to polling mode
- [ ] Use cases

**Expected Behavior**: Efficient file sensor

---

### - [ ] 51.2.5 HttpSensorAsync
Filename: `51_02_05_http_sensor_async.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Async HTTP endpoint monitoring

- [ ] HttpSensorAsync for API readiness
- [ ] response_check function
- [ ] Timeout and retry handling
- [ ] Long-running API operations

**Expected Behavior**: Non-blocking HTTP checks

---

### - [ ] 51.2.6 ExternalTaskSensor Deferrable
Filename: `51_02_06_external_task_deferrable.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Deferrable cross-DAG dependency

- [ ] ExternalTaskSensor with deferrable=True
- [ ] Wait for other DAG without blocking
- [ ] Long-running upstream DAGs
- [ ] Compare to Asset-based triggering

**Expected Behavior**: Efficient cross-DAG wait

---

# 51.3 Custom Deferrable Operators

## Overview
Building custom operators that support deferrable execution.

## Tasks

### - [ ] 51.3.1 Basic Deferrable Operator Structure
Filename: `51_03_01_basic_deferrable_operator.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Create simple deferrable operator

- [ ] Inherit from BaseOperator
- [ ] Implement execute() with self.defer()
- [ ] Create matching Trigger class
- [ ] Handle TriggerEvent in execute_complete()

**Expected Behavior**: Custom deferrable operator works

---

### - [ ] 51.3.2 Implementing execute() with defer()
Filename: `51_03_02_execute_with_defer.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Proper defer() usage

- [ ] self.defer(trigger=MyTrigger(), method_name="execute_complete")
- [ ] Pass trigger kwargs
- [ ] Timeout parameter
- [ ] Multiple defer points

**Expected Behavior**: Task defers correctly

---

### - [ ] 51.3.3 Creating Custom Trigger Class
Filename: `51_03_03_custom_trigger_class.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Build trigger for external system

- [ ] Inherit from BaseTrigger
- [ ] Implement serialize() for state
- [ ] Implement async run() method
- [ ] Yield TriggerEvent when ready

**Expected Behavior**: Trigger monitors external system

---

### - [ ] 51.3.4 Trigger Serialization
Filename: `51_03_04_trigger_serialization.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Properly serialize trigger state

- [ ] serialize() returns (classpath, kwargs)
- [ ] All state must be serializable
- [ ] Reconstruct trigger from serialized state
- [ ] Handle complex objects

**Expected Behavior**: Trigger state persists correctly

---

### - [ ] 51.3.5 Trigger run() Async Method
Filename: `51_03_05_trigger_run_async.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Implement async monitoring logic

- [ ] async def run(self) -> AsyncIterator[TriggerEvent]
- [ ] Use asyncio.sleep() not time.sleep()
- [ ] Yield TriggerEvent when condition met
- [ ] Handle cleanup on cancellation

**Expected Behavior**: Async monitoring works

---

### - [ ] 51.3.6 execute_complete() Handler
Filename: `51_03_06_execute_complete.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle trigger completion

- [ ] def execute_complete(self, context, event)
- [ ] Process event payload
- [ ] Return value or raise exception
- [ ] Multiple trigger scenarios

**Expected Behavior**: Trigger result handled

---

# 51.4 Deferrable Patterns

## Overview
Common patterns for deferrable operator usage.

## Tasks

### - [ ] 51.4.1 Long-Running External Job Monitoring
Filename: `51_04_01_long_running_job_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Monitor external job without blocking

- [ ] Submit job to external system
- [ ] Defer with job_id in trigger
- [ ] Trigger polls job status async
- [ ] Resume when job completes

**Expected Behavior**: Job monitored efficiently

---

### - [ ] 51.4.2 Polling External API Without Blocking
Filename: `51_04_02_polling_api_without_blocking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Async API polling

- [ ] External API that eventually returns result
- [ ] Deferrable polling trigger
- [ ] Exponential backoff in trigger
- [ ] Timeout handling

**Expected Behavior**: API polled without worker

---

### - [ ] 51.4.3 Batch Processing with Deferrable Waits
Filename: `51_04_03_batch_processing_deferrable.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Combine batch work with efficient waits

- [ ] Process batch
- [ ] Defer for external completion
- [ ] Resume and continue
- [ ] Multiple defer/resume cycles

**Expected Behavior**: Efficient batch processing

---

### - [ ] 51.4.4 Deferrable with Dynamic Task Mapping
Filename: `51_04_04_deferrable_with_mapping.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Combine deferrable with expand()

- [ ] Mapped tasks that defer
- [ ] Each mapped task has own trigger
- [ ] Efficient handling of N waiting tasks
- [ ] Resource savings at scale

**Expected Behavior**: Mapped deferrable tasks work

---

### - [ ] 51.4.5 Converting Blocking Sensor to Deferrable
Filename: `51_04_05_converting_to_deferrable.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Migration pattern for custom sensors

- [ ] Existing blocking sensor code
- [ ] Add trigger class
- [ ] Update execute() to defer
- [ ] Maintain backward compatibility

**Expected Behavior**: Sensor converted to deferrable

---

# 51.5 Debugging and Troubleshooting

## Overview
Debugging issues with deferrable operators.

## Tasks

### - [ ] 51.5.1 Debugging Deferred Tasks
Filename: `51_05_01_debugging_deferred_tasks.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Troubleshoot deferrable issues

- [ ] Check triggerer logs
- [ ] Task state inspection
- [ ] Trigger registration verification
- [ ] Common failure modes

**Expected Behavior**: Ability to debug issues

---

### - [ ] 51.5.2 Triggerer Not Running Issues
Filename: `51_05_02_triggerer_not_running.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

**Purpose**: Handle missing triggerer

- [ ] Task stuck in deferred state
- [ ] Triggerer health check
- [ ] Fallback to blocking mode
- [ ] Monitoring triggerer

**Expected Behavior**: Recognize triggerer issues

---

### - [ ] 51.5.3 Trigger Serialization Errors
Filename: `51_05_03_trigger_serialization_errors.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Fix serialization problems

- [ ] Non-serializable trigger state
- [ ] Error messages and diagnosis
- [ ] Fixing serialization
- [ ] Testing serialization

**Expected Behavior**: Serialization issues fixed

---

### - [ ] 51.5.4 Deferrable Timeout Handling
Filename: `51_05_04_deferrable_timeout.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle timeout in deferrable tasks

- [ ] Trigger timeout parameter
- [ ] Task timeout vs trigger timeout
- [ ] Timeout exception handling
- [ ] Cleanup on timeout

**Expected Behavior**: Timeouts handled gracefully

---

# Summary

## Topic Completion Checklist
- [ ] Deferrable concept explained clearly
- [ ] Built-in deferrable sensors covered
- [ ] Custom trigger development documented
- [ ] Common patterns included
- [ ] Debugging guidance provided

## Related Topics
- Section 08: Sensors (sensor basics)
- Section 14: Error Handling (timeout, retry)
- Section 35: Executors (resource management)

## Notes for Implementation
- Requires triggerer to be running
- Test with and without triggerer
- Show logs from both worker and triggerer
- Include async code examples
- Demonstrate resource savings

---

# 51.6 Advanced Trigger Development

## Overview
Advanced patterns for building robust custom triggers.

## Tasks

### - [ ] 51.6.1 Multi-Condition Triggers
Filename: `51_06_01_multi_condition_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Monitor multiple conditions
- [ ] Any/all condition logic
- [ ] Dynamic condition updates
- [ ] Complex event handling

### - [ ] 51.6.2 Stateful Triggers
Filename: `51_06_02_stateful_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Maintain state across polls
- [ ] Progress tracking
- [ ] Checkpoint handling
- [ ] State recovery

### - [ ] 51.6.3 Webhook-Based Triggers
Filename: `51_06_03_webhook_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Listen for webhooks
- [ ] Callback URL handling
- [ ] External system notification
- [ ] Security considerations

### - [ ] 51.6.4 Database Event Triggers
Filename: `51_06_04_database_event_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Monitor database changes
- [ ] Async database polling
- [ ] Connection management
- [ ] Resource cleanup

### - [ ] 51.6.5 Message Queue Triggers
Filename: `51_06_05_message_queue_triggers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Kafka/SQS/Pub-Sub triggers
- [ ] Async consumer patterns
- [ ] Message acknowledgment
- [ ] Error handling

---

# 51.7 Performance and Scalability

## Overview
Optimizing deferrable operators for scale.

## Tasks

### - [ ] 51.7.1 Triggerer Scaling
Filename: `51_07_01_triggerer_scaling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Multiple triggerer instances
- [ ] Trigger distribution
- [ ] Load balancing
- [ ] Capacity planning

### - [ ] 51.7.2 Efficient Trigger Polling
Filename: `51_07_02_efficient_polling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Optimal poll intervals
- [ ] Backoff strategies
- [ ] Resource usage optimization
- [ ] Connection pooling

### - [ ] 51.7.3 Trigger Memory Management
Filename: `51_07_03_trigger_memory.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Memory footprint per trigger
- [ ] Large number of triggers
- [ ] Cleanup strategies
- [ ] Monitoring memory

### - [ ] 51.7.4 Monitoring Trigger Performance
Filename: `51_07_04_monitoring_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Trigger metrics
- [ ] Event latency
- [ ] Success/failure rates
- [ ] Alerting

### - [ ] 51.7.5 Benchmarking Deferrable vs Blocking
Filename: `51_07_05_benchmarking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Resource comparison
- [ ] Throughput testing
- [ ] When deferrable wins
- [ ] Break-even analysis

---

# 51.8 Testing Deferrable Operators

## Overview
Comprehensive testing strategies for deferrable code.

## Tasks

### - [ ] 51.8.1 Unit Testing Triggers
Filename: `51_08_01_unit_testing_triggers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test trigger serialization
- [ ] Test run() method
- [ ] Mock async dependencies
- [ ] pytest-asyncio usage

### - [ ] 51.8.2 Unit Testing Deferrable Operators
Filename: `51_08_02_unit_testing_operators.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test execute() defer path
- [ ] Test execute_complete()
- [ ] Mock trigger events
- [ ] State verification

### - [ ] 51.8.3 Integration Testing
Filename: `51_08_03_integration_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test with real triggerer
- [ ] End-to-end deferrable flow
- [ ] External system mocking
- [ ] CI/CD integration

### - [ ] 51.8.4 Testing Timeout Behavior
Filename: `51_08_04_testing_timeouts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Verify timeout triggers
- [ ] Test cleanup on timeout
- [ ] Time manipulation
- [ ] Edge cases

### - [ ] 51.8.5 Testing Error Scenarios
Filename: `51_08_05_testing_errors.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Trigger exceptions
- [ ] Network failures
- [ ] Serialization errors
- [ ] Recovery testing

---

# 51.9 Anti-Patterns and Common Mistakes

## Overview
Avoiding common pitfalls with deferrable operators.

## Tasks

### - [ ] 51.9.1 Blocking Calls in Triggers
Filename: `51_09_01_blocking_in_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Using time.sleep() instead of asyncio.sleep()
- [ ] Synchronous HTTP calls
- [ ] Blocking database calls
- [ ] Correct async patterns

### - [ ] 51.9.2 Non-Serializable State
Filename: `51_09_02_non_serializable.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Connection objects in trigger
- [ ] Lambda functions
- [ ] Open file handles
- [ ] Serializable alternatives

### - [ ] 51.9.3 Memory Leaks in Triggers
Filename: `51_09_03_memory_leaks.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Unclosed connections
- [ ] Growing data structures
- [ ] Resource accumulation
- [ ] Cleanup patterns

### - [ ] 51.9.4 Excessive Trigger Creation
Filename: `51_09_04_excessive_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Too many triggers
- [ ] Triggerer overload
- [ ] Consolidation strategies
- [ ] Resource planning

### - [ ] 51.9.5 Ignoring Triggerer Health
Filename: `51_09_05_ignoring_triggerer_health.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] No triggerer monitoring
- [ ] Silent failures
- [ ] Tasks stuck deferred
- [ ] Health checks and alerting

---

# 51.10 Real-World Use Cases

## Overview
Production use cases for deferrable operators.

## Tasks

### - [ ] 51.10.1 EMR Job Monitoring
Filename: `51_10_01_emr_job_monitoring.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Submit EMR step
- [ ] Deferrable monitoring
- [ ] Handle completion
- [ ] Error handling

### - [ ] 51.10.2 BigQuery Job Deferral
Filename: `51_10_02_bigquery_deferral.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Long-running BQ queries
- [ ] Job status trigger
- [ ] Result retrieval
- [ ] Cost optimization

### - [ ] 51.10.3 Kubernetes Pod Monitoring
Filename: `51_10_03_kubernetes_pod.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Launch K8s pod
- [ ] Async pod status
- [ ] Log retrieval
- [ ] Cleanup handling

### - [ ] 51.10.4 Lambda/Cloud Function Deferral
Filename: `51_10_04_lambda_deferral.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Async Lambda invocation
- [ ] Status polling
- [ ] Result handling
- [ ] Timeout management

### - [ ] 51.10.5 Data Pipeline Orchestration
Filename: `51_10_05_pipeline_orchestration.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Multi-system pipeline
- [ ] Efficient resource usage
- [ ] Parallel deferrable waits
- [ ] End-to-end example
