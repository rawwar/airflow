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

# 53 DAG Dependencies

## Overview
Advanced cross-DAG dependency patterns beyond Assets, including ExternalTaskSensor, TriggerDagRunOperator, and programmatic dependencies.

---

# 53.1 ExternalTaskSensor Patterns

### - [ ] 53.1.1 Basic ExternalTaskSensor
Filename: `53_01_01_basic_external_task_sensor.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Wait for task in another DAG
- [ ] external_dag_id, external_task_id params
- [ ] execution_delta for time alignment
- [ ] Timeout configuration

### - [ ] 53.1.2 ExternalTaskSensor with execution_date_fn
Filename: `53_01_02_execution_date_fn.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Custom date matching function
- [ ] Cross-schedule dependencies
- [ ] Handle different schedules
- [ ] Complex date logic

### - [ ] 53.1.3 ExternalTaskSensor Deferrable Mode
Filename: `53_01_03_external_task_deferrable.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] deferrable=True for efficiency
- [ ] Long-running upstream waits
- [ ] Resource savings
- [ ] Triggerer requirement

### - [ ] 53.1.4 Waiting for DAG Completion
Filename: `53_01_04_wait_dag_completion.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] external_task_id=None for entire DAG
- [ ] Wait for all tasks to complete
- [ ] vs waiting for specific task
- [ ] Use cases

### - [ ] 53.1.5 ExternalTaskMarker
Filename: `53_01_05_external_task_marker.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Mark dependencies for clearing
- [ ] Recursive clear behavior
- [ ] Dependency documentation
- [ ] UI visualization

---

# 53.2 TriggerDagRunOperator

### - [ ] 53.2.1 Basic TriggerDagRunOperator
Filename: `53_02_01_basic_trigger_dag_run.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Trigger another DAG
- [ ] trigger_dag_id parameter
- [ ] Pass conf to triggered DAG
- [ ] Wait vs fire-and-forget

### - [ ] 53.2.2 Passing Configuration to Triggered DAG
Filename: `53_02_02_trigger_with_conf.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] conf parameter with dict
- [ ] Access conf in triggered DAG
- [ ] Dynamic configuration
- [ ] Templated conf values

### - [ ] 53.2.3 Wait for Triggered DAG
Filename: `53_02_03_wait_for_triggered.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] wait_for_completion=True
- [ ] poke_interval configuration
- [ ] Timeout handling
- [ ] Failed triggered DAG handling

### - [ ] 53.2.4 Trigger Multiple DAGs
Filename: `53_02_04_trigger_multiple_dags.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Fan-out to multiple DAGs
- [ ] Parallel triggering
- [ ] Collect results
- [ ] Error handling

### - [ ] 53.2.5 Conditional DAG Triggering
Filename: `53_02_05_conditional_trigger.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Trigger based on conditions
- [ ] Branching to trigger
- [ ] Skip trigger scenarios
- [ ] Dynamic trigger_dag_id

---

# 53.3 Dependency Patterns

### - [ ] 53.3.1 Sequential DAG Chain
Filename: `53_03_01_sequential_dag_chain.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] DAG A triggers DAG B triggers DAG C
- [ ] Passing context through chain
- [ ] Error propagation
- [ ] Monitoring chains

### - [ ] 53.3.2 Fan-Out Fan-In Pattern
Filename: `53_03_02_fan_out_fan_in.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] One DAG triggers many
- [ ] Aggregator waits for all
- [ ] Parallel processing
- [ ] Result collection

### - [ ] 53.3.3 Diamond Dependency
Filename: `53_03_03_diamond_dependency.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] DAG A -> B,C -> D
- [ ] Handle concurrent middle DAGs
- [ ] Aggregation DAG
- [ ] Timing considerations

### - [ ] 53.3.4 Conditional Branch Dependencies
Filename: `53_03_04_conditional_branches.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Different DAGs based on conditions
- [ ] Branch operator with triggers
- [ ] Downstream handling
- [ ] Skip propagation

### - [ ] 53.3.5 Self-Triggering DAG
Filename: `53_03_05_self_triggering.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] DAG triggers itself
- [ ] Recursive processing
- [ ] Termination condition
- [ ] Avoiding infinite loops

---

# 53.4 Asset vs Sensor Dependencies

### - [ ] 53.4.1 When to Use Assets
Filename: `53_04_01_when_use_assets.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Data-centric dependencies
- [ ] Loose coupling benefits
- [ ] Multiple producers/consumers
- [ ] Event-driven scheduling

### - [ ] 53.4.2 When to Use ExternalTaskSensor
Filename: `53_04_02_when_use_sensor.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Task-centric dependencies
- [ ] Execution date alignment
- [ ] Specific task completion
- [ ] Legacy compatibility

### - [ ] 53.4.3 Hybrid Approach
Filename: `53_04_03_hybrid_approach.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Combine Assets and sensors
- [ ] Assets for data flow
- [ ] Sensors for orchestration
- [ ] Migration strategy

### - [ ] 53.4.4 Migration: Sensor to Asset
Filename: `53_04_04_sensor_to_asset_migration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Identify migration candidates
- [ ] Step-by-step migration
- [ ] Testing approach
- [ ] Rollback strategy

### - [ ] 53.4.5 Dependency Anti-Patterns
Filename: `53_04_05_dependency_anti_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Circular dependencies
- [ ] Over-coupled DAGs
- [ ] Hidden dependencies
- [ ] Brittle timing assumptions

---

# 53.5 Programmatic Dependencies

### - [ ] 53.5.1 API-Triggered Dependencies
Filename: `53_05_01_api_triggered.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] REST API to trigger DAGs
- [ ] External system integration
- [ ] Webhook patterns
- [ ] Authentication

### - [ ] 53.5.2 Database-Based Coordination
Filename: `53_05_02_database_coordination.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Shared state in database
- [ ] Coordination tables
- [ ] Lock patterns
- [ ] Cleanup strategies

### - [ ] 53.5.3 Message Queue Dependencies
Filename: `53_05_03_message_queue.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Kafka/SQS/Pub-Sub triggers
- [ ] Event-driven DAG runs
- [ ] Message processing
- [ ] At-least-once semantics

### - [ ] 53.5.4 File-Based Dependencies
Filename: `53_05_04_file_based.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Sentinel files for triggering
- [ ] File sensor combinations
- [ ] Atomic file operations
- [ ] Cleanup patterns

### - [ ] 53.5.5 Time-Window Dependencies
Filename: `53_05_05_time_window.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Wait for time window
- [ ] Business hours logic
- [ ] Timezone considerations
- [ ] Holiday handling

---

# 53.6 Dependency Testing

## Overview
Testing cross-DAG dependencies and orchestration.

## Tasks

### - [ ] 53.6.1 Unit Testing Dependencies
Filename: `53_06_01_unit_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Mock external sensors
- [ ] Test trigger logic
- [ ] Isolation patterns
- [ ] pytest fixtures

### - [ ] 53.6.2 Integration Testing
Filename: `53_06_02_integration_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Test DAG chains
- [ ] Real Airflow environment
- [ ] End-to-end verification
- [ ] CI/CD integration

### - [ ] 53.6.3 Testing with Mocked External DAGs
Filename: `53_06_03_mocked_external.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Create mock DAG runs
- [ ] Simulate task states
- [ ] Test sensor behavior
- [ ] Edge case coverage

### - [ ] 53.6.4 Dependency Graph Validation
Filename: `53_06_04_graph_validation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Validate dependency graph
- [ ] Detect circular dependencies
- [ ] Orphan DAG detection
- [ ] Documentation generation

### - [ ] 53.6.5 Performance Testing
Filename: `53_06_05_performance_testing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Dependency overhead
- [ ] Sensor polling impact
- [ ] Trigger latency
- [ ] Scalability testing

---

# 53.7 Debugging Dependencies

## Overview
Troubleshooting cross-DAG dependency issues.

## Tasks

### - [ ] 53.7.1 Sensor Not Finding Task
Filename: `53_07_01_sensor_not_finding.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Execution date mismatch
- [ ] DAG ID typos
- [ ] Task ID changes
- [ ] Debugging steps

### - [ ] 53.7.2 Trigger Not Firing
Filename: `53_07_02_trigger_not_firing.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Trigger conditions
- [ ] DAG paused state
- [ ] Permission issues
- [ ] Log analysis

### - [ ] 53.7.3 Deadlock Detection
Filename: `53_07_03_deadlock_detection.py` | Tags: `['reference', 'core', 'advanced', 'failure']`
- [ ] Cross-DAG deadlocks
- [ ] Circular waits
- [ ] Detection methods
- [ ] Resolution strategies

### - [ ] 53.7.4 Timing Issues
Filename: `53_07_04_timing_issues.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Schedule misalignment
- [ ] Timezone problems
- [ ] Data interval mismatch
- [ ] Debugging tools

### - [ ] 53.7.5 Logging and Monitoring
Filename: `53_07_05_logging_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Dependency logging
- [ ] Metrics collection
- [ ] Visualization
- [ ] Alerting

---

# 53.8 Real-World Patterns

## Overview
Production patterns for complex dependencies.

## Tasks

### - [ ] 53.8.1 ETL Pipeline Orchestration
Filename: `53_08_01_etl_orchestration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Extract -> Transform -> Load
- [ ] Cross-DAG dependencies
- [ ] Error handling
- [ ] Retry strategies

### - [ ] 53.8.2 Multi-Team DAG Coordination
Filename: `53_08_02_multi_team.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Team boundary dependencies
- [ ] Contract interfaces
- [ ] Version management
- [ ] Communication patterns

### - [ ] 53.8.3 Data Lake Orchestration
Filename: `53_08_03_data_lake.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Raw -> Curated -> Mart
- [ ] Asset-driven flow
- [ ] Quality gates
- [ ] Lineage tracking

### - [ ] 53.8.4 ML Pipeline Dependencies
Filename: `53_08_04_ml_pipeline.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Data prep -> Training -> Deployment
- [ ] Model versioning
- [ ] Conditional retraining
- [ ] Experiment tracking

### - [ ] 53.8.5 Microservice Event Chain
Filename: `53_08_05_microservice_chain.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Service-to-service flow
- [ ] Event-driven triggers
- [ ] Retry and compensation
- [ ] Saga pattern

---

# 53.9 Dependency Performance

## Overview
Optimizing dependency performance and resource usage.

## Tasks

### - [ ] 53.9.1 Sensor Optimization
Filename: `53_09_01_sensor_optimization.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Optimal poke interval
- [ ] Reschedule mode
- [ ] Deferrable mode
- [ ] Resource comparison

### - [ ] 53.9.2 Trigger Optimization
Filename: `53_09_02_trigger_optimization.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Batch triggers
- [ ] Efficient configuration
- [ ] Callback patterns
- [ ] Wait optimization

### - [ ] 53.9.3 Reducing Dependency Overhead
Filename: `53_09_03_reducing_overhead.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Asset vs sensor choice
- [ ] Direct vs indirect deps
- [ ] Consolidation patterns
- [ ] Cache strategies

### - [ ] 53.9.4 Monitoring Dependency Health
Filename: `53_09_04_monitoring_health.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Latency metrics
- [ ] Failure rates
- [ ] Dashboard creation
- [ ] Alerting rules

### - [ ] 53.9.5 Scaling Dependencies
Filename: `53_09_05_scaling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Many DAG dependencies
- [ ] High-frequency triggers
- [ ] Resource planning
- [ ] Architecture patterns

---

# 53.10 Best Practices and Anti-Patterns

## Overview
Recommended practices and patterns to avoid.

## Tasks

### - [ ] 53.10.1 Dependency Anti-Patterns
Filename: `53_10_01_anti_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Hidden dependencies
- [ ] Tight coupling
- [ ] Fragile timing
- [ ] God DAG patterns

### - [ ] 53.10.2 Loose Coupling Patterns
Filename: `53_10_02_loose_coupling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Asset-based decoupling
- [ ] Interface contracts
- [ ] Event-driven design
- [ ] Version tolerance

### - [ ] 53.10.3 Documentation Standards
Filename: `53_10_03_documentation.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Document dependencies
- [ ] Dependency diagrams
- [ ] Runbooks
- [ ] Change management

### - [ ] 53.10.4 Change Management
Filename: `53_10_04_change_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Safe dependency changes
- [ ] Communication protocols
- [ ] Testing requirements
- [ ] Rollback procedures

### - [ ] 53.10.5 Dependency Governance
Filename: `53_10_05_governance.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Approval processes
- [ ] Impact analysis
- [ ] SLA definitions
- [ ] Review requirements
