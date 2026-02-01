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

# 119 - Multi-Executor Configuration

## Overview
Airflow 3.x supports running multiple executors simultaneously, enabling per-task executor selection for optimal resource utilization, isolation, and cost efficiency.

---

## Section 1: Multi-Executor Fundamentals

### - [ ] 119.1.1 Multi-Executor Architecture
Filename: `119_01_01_multi_executor_intro.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand multi-executor architecture
- [ ] Review supported executor combinations
- [ ] Identify use cases for multiple executors
- [ ] Compare single vs multi-executor deployments

### - [ ] 119.1.2 Executor Configuration Syntax
Filename: `119_01_02_executor_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Configure multiple executors in airflow.cfg
- [ ] Define executor names and types
- [ ] Set default executor for tasks
- [ ] Validate executor configuration

### - [ ] 119.1.3 Executor Types Overview
Filename: `119_01_03_executor_types.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Review LocalExecutor characteristics
- [ ] Understand CeleryExecutor for distributed
- [ ] Explore KubernetesExecutor isolation
- [ ] Compare executor capabilities

### - [ ] 119.1.4 Executor Lifecycle Management
Filename: `119_01_04_executor_lifecycle.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Understand executor startup sequence
- [ ] Handle executor health monitoring
- [ ] Manage executor shutdown gracefully
- [ ] Configure executor-specific resources

### - [ ] 119.1.5 Executor Compatibility Matrix
Filename: `119_01_05_executor_compat.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Identify compatible executor pairs
- [ ] Understand shared resource constraints
- [ ] Handle queue namespace conflicts
- [ ] Configure isolated executor resources

---

## Section 2: CeleryExecutor + KubernetesExecutor

### - [ ] 119.2.1 Combined Executor Setup
Filename: `119_02_01_celery_k8s_setup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Configure Celery and Kubernetes together
- [ ] Set up shared metadata database
- [ ] Configure executor-specific connections
- [ ] Validate combined deployment

### - [ ] 119.2.2 Celery for Standard Tasks
Filename: `119_02_02_celery_standard.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Route lightweight tasks to Celery
- [ ] Configure Celery worker pools
- [ ] Optimize for low-latency execution
- [ ] Handle Celery queue priorities

### - [ ] 119.2.3 Kubernetes for Isolated Tasks
Filename: `119_02_03_k8s_isolated.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Route resource-heavy tasks to K8s
- [ ] Configure pod templates per task
- [ ] Handle container resource limits
- [ ] Manage Kubernetes namespace isolation

### - [ ] 119.2.4 Resource Optimization Strategy
Filename: `119_02_04_resource_optimization.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Balance load across executors
- [ ] Optimize cost with executor selection
- [ ] Handle resource contention
- [ ] Monitor cross-executor metrics

### - [ ] 119.2.5 Migration to Multi-Executor
Filename: `119_02_05_migration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Plan migration from single executor
- [ ] Identify tasks for each executor
- [ ] Test executor assignment incrementally
- [ ] Handle rollback scenarios

---

## Section 3: Per-Task Executor Selection

### - [ ] 119.3.1 Task Executor Parameter
Filename: `119_03_01_task_executor_param.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Set executor parameter on tasks
- [ ] Use executor name from configuration
- [ ] Handle invalid executor references
- [ ] Test executor assignment

### - [ ] 119.3.2 Operator-Level Executor Default
Filename: `119_03_02_operator_executor.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Configure executor in custom operators
- [ ] Set executor default in base operators
- [ ] Override at task instantiation
- [ ] Handle inheritance patterns

### - [ ] 119.3.3 Dynamic Executor Selection
Filename: `119_03_03_dynamic_selection.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Select executor based on runtime data
- [ ] Use task parameters for routing
- [ ] Implement executor selection callbacks
- [ ] Handle dynamic queue mapping

### - [ ] 119.3.4 DAG-Level Executor Default
Filename: `119_03_04_dag_executor.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Set default executor for entire DAG
- [ ] Override at task level when needed
- [ ] Handle mixed executor DAGs
- [ ] Document executor assignments

### - [ ] 119.3.5 Executor Selection Best Practices
Filename: `119_03_05_selection_best_practices.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Match task requirements to executor
- [ ] Consider latency vs isolation trade-offs
- [ ] Document executor selection rationale
- [ ] Review and optimize periodically

---

## Section 4: Executor Routing Strategies

### - [ ] 119.4.1 Queue-Based Routing
Filename: `119_04_01_queue_routing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Map queues to executors
- [ ] Configure queue namespace separation
- [ ] Handle queue priority within executor
- [ ] Debug queue routing issues

### - [ ] 119.4.2 Resource-Based Routing
Filename: `119_04_02_resource_routing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Route by CPU/memory requirements
- [ ] Handle GPU task routing
- [ ] Configure resource pools per executor
- [ ] Optimize resource utilization

### - [ ] 119.4.3 Task Type Routing
Filename: `119_04_03_task_type_routing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Route by operator type
- [ ] Configure defaults for common operators
- [ ] Handle custom operator routing
- [ ] Document routing conventions

### - [ ] 119.4.4 Environment-Based Routing
Filename: `119_04_04_env_routing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Route based on execution environment
- [ ] Handle dev/staging/prod differences
- [ ] Configure environment-specific executors
- [ ] Test routing in each environment

### - [ ] 119.4.5 Cost-Based Routing
Filename: `119_04_05_cost_routing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Route to minimize execution cost
- [ ] Use spot instances via K8s executor
- [ ] Fall back to Celery on capacity
- [ ] Track cost by executor

---

## Section 5: Trade-offs Analysis

### - [ ] 119.5.1 Latency Considerations
Filename: `119_05_01_latency_analysis.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Compare executor startup latency
- [ ] Measure Celery vs K8s task start
- [ ] Optimize for time-sensitive tasks
- [ ] Handle latency SLAs

### - [ ] 119.5.2 Isolation Trade-offs
Filename: `119_05_02_isolation_analysis.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Compare isolation levels by executor
- [ ] Handle dependency isolation needs
- [ ] Balance isolation vs overhead
- [ ] Choose isolation strategy per task

### - [ ] 119.5.3 Efficiency Optimization
Filename: `119_05_03_efficiency_analysis.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Measure resource utilization per executor
- [ ] Optimize worker pool sizing
- [ ] Handle idle resource costs
- [ ] Balance throughput vs cost

### - [ ] 119.5.4 Operational Complexity
Filename: `119_05_04_operational_complexity.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Assess multi-executor ops burden
- [ ] Plan monitoring strategy
- [ ] Handle debugging across executors
- [ ] Document operational procedures

### - [ ] 119.5.5 Failure Mode Analysis
Filename: `119_05_05_failure_modes.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Identify executor-specific failures
- [ ] Handle partial executor outages
- [ ] Implement failover strategies
- [ ] Test failure recovery scenarios

---

## Section 6: Advanced Multi-Executor Patterns

### - [ ] 119.6.1 Executor Pool Management
Filename: `119_06_01_pool_management.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure pools per executor
- [ ] Handle cross-executor pool limits
- [ ] Optimize pool allocation
- [ ] Monitor pool utilization

### - [ ] 119.6.2 Priority Queues Across Executors
Filename: `119_06_02_priority_queues.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement priority across executors
- [ ] Handle urgent task preemption
- [ ] Configure priority inheritance
- [ ] Balance fairness vs priority

### - [ ] 119.6.3 Executor-Specific Callbacks
Filename: `119_06_03_executor_callbacks.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement executor-aware callbacks
- [ ] Handle pre/post execution hooks
- [ ] Configure cleanup per executor
- [ ] Monitor callback execution

### - [ ] 119.6.4 Multi-Executor Monitoring
Filename: `119_06_04_multi_executor_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Monitor all executors unified
- [ ] Track per-executor metrics
- [ ] Alert on executor-specific issues
- [ ] Build multi-executor dashboards

### - [ ] 119.6.5 Testing Multi-Executor DAGs
Filename: `119_06_05_testing_multi_executor.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Test DAGs with multiple executors
- [ ] Mock executor behavior in tests
- [ ] Validate executor assignments
- [ ] Integration test across executors

---

## Section 7: Multi-Executor Anti-Patterns

### - [ ] 119.7.1 Random Executor Assignment
Filename: `119_07_01_random_assignment_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Inconsistent behavior
- [ ] Resource mismatch
- [ ] Explicit assignment strategy
- [ ] Documentation importance

### - [ ] 119.7.2 Ignoring Executor Capabilities
Filename: `119_07_02_ignoring_capabilities_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Wrong executor for task
- [ ] Resource waste
- [ ] Capability matching
- [ ] Task requirements analysis

### - [ ] 119.7.3 No Fallback Strategy
Filename: `119_07_03_no_fallback_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Single executor dependency
- [ ] No resilience
- [ ] Fallback configuration
- [ ] Graceful degradation

### - [ ] 119.7.4 Complex Routing Logic
Filename: `119_07_04_complex_routing_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Unmaintainable routing
- [ ] Debugging difficulty
- [ ] Simple routing patterns
- [ ] Convention over configuration

### - [ ] 119.7.5 No Executor Monitoring Split
Filename: `119_07_05_no_monitoring_split_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Aggregated metrics hide issues
- [ ] Per-executor blind spots
- [ ] Separate monitoring
- [ ] Executor-specific alerts

---

## Section 8: Testing Multi-Executor Configurations

### - [ ] 119.8.1 Unit Testing Executor Selection
Filename: `119_08_01_unit_testing_selection.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test routing logic
- [ ] Validate executor assignment
- [ ] Test edge cases
- [ ] Mock executor responses

### - [ ] 119.8.2 Integration Testing Executors
Filename: `119_08_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test with real executors
- [ ] Validate task execution
- [ ] Test cross-executor workflows
- [ ] Verify result consistency

### - [ ] 119.8.3 Testing Executor Failover
Filename: `119_08_03_failover_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Simulate executor failure
- [ ] Test fallback behavior
- [ ] Validate recovery
- [ ] HA configuration testing

### - [ ] 119.8.4 Performance Comparison Testing
Filename: `119_08_04_performance_comparison.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Benchmark same task on executors
- [ ] Latency comparison
- [ ] Resource usage analysis
- [ ] Cost comparison

### - [ ] 119.8.5 Testing Executor Configuration
Filename: `119_08_05_config_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Validate configuration syntax
- [ ] Test executor startup
- [ ] Configuration validation
- [ ] Error handling for misconfig

---

## Section 9: Multi-Executor Performance

### - [ ] 119.9.1 Optimal Task-Executor Matching
Filename: `119_09_01_optimal_matching.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Analyze task characteristics
- [ ] Match to executor strengths
- [ ] Measure performance gains
- [ ] Continuous optimization

### - [ ] 119.9.2 Cross-Executor Load Balancing
Filename: `119_09_02_load_balancing.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Distribute load efficiently
- [ ] Avoid executor overload
- [ ] Dynamic balancing
- [ ] Queue monitoring

### - [ ] 119.9.3 Minimizing Executor Overhead
Filename: `119_09_03_minimize_overhead.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Reduce context switching
- [ ] Batch similar tasks
- [ ] Minimize routing complexity
- [ ] Optimize configuration

### - [ ] 119.9.4 Resource Utilization Optimization
Filename: `119_09_04_resource_utilization.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Pool sizing per executor
- [ ] Shared vs dedicated resources
- [ ] Cost optimization
- [ ] Utilization monitoring

### - [ ] 119.9.5 Latency Optimization Strategies
Filename: `119_09_05_latency_optimization.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Task startup latency
- [ ] Executor warm-up
- [ ] Pre-provisioned capacity
- [ ] Latency-based routing

---

## Section 10: Real-World Multi-Executor Usage

### - [ ] 119.10.1 Celery + Kubernetes Hybrid
Filename: `119_10_01_celery_k8s_hybrid.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Standard tasks on Celery
- [ ] Isolated tasks on K8s
- [ ] Resource optimization
- [ ] Cost management

### - [ ] 119.10.2 Multi-Tenant Executor Isolation
Filename: `119_10_02_multi_tenant.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Tenant-specific executors
- [ ] Resource isolation
- [ ] Security boundaries
- [ ] Cost allocation

### - [ ] 119.10.3 Dev/Prod Executor Separation
Filename: `119_10_03_dev_prod_separation.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Different executors per environment
- [ ] Local dev with LocalExecutor
- [ ] Prod with distributed executor
- [ ] Seamless promotion

### - [ ] 119.10.4 GPU and CPU Task Split
Filename: `119_10_04_gpu_cpu_split.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] GPU tasks to K8s
- [ ] CPU tasks to Celery
- [ ] Resource efficiency
- [ ] Cost optimization

### - [ ] 119.10.5 Spot Instance Routing
Filename: `119_10_05_spot_instance.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Non-critical on spot
- [ ] Critical on on-demand
- [ ] Preemption handling
- [ ] Cost savings

---

# Summary

## Topic Completion Checklist
- [ ] Multi-executor fundamentals covered
- [ ] Celery + K8s combination explained
- [ ] Per-task selection documented
- [ ] Routing strategies addressed
- [ ] Trade-offs analysis included
- [ ] Advanced patterns documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization addressed
- [ ] Real-world examples provided

## Related Topics
- Section 35: Executors
- Section 118: Remote Execution
- Section 111: Task SDK
- Section 87: Scaling

## Notes for Implementation
- Start with clear routing strategy
- Monitor each executor separately
- Test executor combinations
- Document task-executor mapping
- Plan for executor failures
