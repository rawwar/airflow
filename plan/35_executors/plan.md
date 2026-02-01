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

# 35 Executors

## Overview

Executors determine how Airflow runs tasks - locally, in parallel processes, distributed across Celery workers, or in Kubernetes pods. Understanding executor behavior helps you write portable DAGs and optimize for your deployment environment.

## Research & Background

### Key Concepts
- **Executor**: Component that runs task instances (SequentialExecutor, LocalExecutor, CeleryExecutor, KubernetesExecutor)
- **Task Slot**: A worker process/pod that can run one task
- **Queue**: Named destination for task routing (Celery/K8s)
- **executor_config**: Per-task executor customization

### Airflow 3.x Notes
- KubernetesExecutor fully supported
- executor_config for pod templates
- Queue-based task routing
- Hybrid executors available

### Prerequisites
- Airflow 3.x deployment
- Understanding of task fundamentals (Section 02)
- For K8s executor: Kubernetes basics

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Write DAGs that work across different executors
2. Configure executor-specific task settings
3. Route tasks to appropriate queues/workers
4. Customize Kubernetes pod specifications
5. Troubleshoot executor-related issues

---

# 35.1 Executor Concepts

## Overview
Understanding how executors work and writing executor-agnostic code.

## Tasks

### - [ ] 35.1.1 Executor Role in Airflow Architecture
Filename: `35_01_01_executor_architecture.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand where executor fits in Airflow

- [ ] DAG shows scheduler → executor → worker flow
- [ ] Log which executor is running the task
- [ ] Access executor info at runtime
- [ ] Visualize task execution path

**Expected Behavior**: Clear understanding of executor role

---

### - [ ] 35.1.2 Portable DAG (Executor-Agnostic)
Filename: `35_01_02_portable_dag.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Write DAG that works on any executor

- [ ] No executor-specific configurations
- [ ] Use standard operators and TaskFlow
- [ ] Avoid executor assumptions
- [ ] Works on Local, Celery, K8s

**Expected Behavior**: DAG runs identically on all executors

---

### - [ ] 35.1.3 Check Current Executor at Runtime
Filename: `35_01_03_check_current_executor.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Detect executor type within task

- [ ] Access airflow.configuration
- [ ] Get executor class name
- [ ] Conditional logic based on executor
- [ ] Log executor for debugging

**Expected Behavior**: Task knows which executor runs it

---

### - [ ] 35.1.4 Executor Impact on Parallelism
Filename: `35_01_04_executor_parallelism.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand parallelism differences

- [ ] SequentialExecutor: 1 task at a time
- [ ] LocalExecutor: parallelism config
- [ ] CeleryExecutor: worker concurrency
- [ ] KubernetesExecutor: pod limits
- [ ] DAG with parallel tasks to observe behavior

**Expected Behavior**: Clear parallelism understanding

---

### - [ ] 35.1.5 Executor Configuration Overview
Filename: `35_01_05_executor_config_overview.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Show executor configuration options

- [ ] airflow.cfg executor settings
- [ ] Environment variable overrides
- [ ] Per-executor config sections
- [ ] Validate current configuration

**Expected Behavior**: Understanding of executor config

---

# 35.2 LocalExecutor

## Overview
Running tasks in parallel local processes.

## Tasks

### - [ ] 35.2.1 Basic Parallel Task Execution
Filename: `35_02_01_local_parallel_execution.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Demonstrate LocalExecutor parallelism

- [ ] DAG with multiple independent tasks
- [ ] Tasks run concurrently on LocalExecutor
- [ ] Observe parallel execution in logs
- [ ] Compare to SequentialExecutor

**Expected Behavior**: Tasks run in parallel

---

### - [ ] 35.2.2 Parallelism Configuration Effect
Filename: `35_02_02_parallelism_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Show impact of parallelism setting

- [ ] DAG with many parallel tasks
- [ ] Observe task queueing when parallelism exceeded
- [ ] Document parallelism vs max_active_tasks
- [ ] System resource considerations

**Expected Behavior**: Understanding of concurrency limits

---

### - [ ] 35.2.3 max_active_tasks_per_dag with LocalExecutor
Filename: `35_02_03_max_active_tasks_per_dag.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: DAG-level task concurrency

- [ ] Set max_active_tasks_per_dag on DAG
- [ ] More tasks defined than allowed concurrent
- [ ] Observe queuing behavior
- [ ] Interaction with global parallelism

**Expected Behavior**: DAG-level concurrency control

---

### - [ ] 35.2.4 Resource Sharing Between Tasks
Filename: `35_02_04_resource_sharing_local.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand shared resources in LocalExecutor

- [ ] Tasks share filesystem
- [ ] Tasks share network
- [ ] Memory considerations
- [ ] CPU contention patterns

**Expected Behavior**: Understanding of shared resources

---

# 35.3 CeleryExecutor

## Overview
Distributing tasks across Celery workers.

## Tasks

### - [ ] 35.3.1 Queue Routing with queue Parameter
Filename: `35_03_01_queue_routing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Route tasks to specific queues

- [ ] Task with queue="default"
- [ ] Task with queue="heavy_compute"
- [ ] Task with queue="io_bound"
- [ ] Workers subscribe to specific queues

**Expected Behavior**: Tasks route to correct workers

---

### - [ ] 35.3.2 Multiple Celery Queues
Filename: `35_03_02_multiple_queues.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Design multi-queue workflow

- [ ] ETL DAG with different queue needs
- [ ] Extract: io_bound queue
- [ ] Transform: compute queue
- [ ] Load: io_bound queue
- [ ] Show worker specialization

**Expected Behavior**: Efficient queue utilization

---

### - [ ] 35.3.3 Worker Concurrency Control
Filename: `35_03_03_worker_concurrency.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand Celery worker concurrency

- [ ] Worker prefetch and concurrency settings
- [ ] Task distribution across workers
- [ ] Handling slow tasks
- [ ] Worker pool sizing

**Expected Behavior**: Understanding of worker behavior

---

### - [ ] 35.3.4 Celery Result Backend Usage
Filename: `35_03_04_result_backend.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand Celery result handling

- [ ] Task results flow
- [ ] XCom through Celery
- [ ] Result backend configuration
- [ ] Cleanup considerations

**Expected Behavior**: Understanding of result flow

---

### - [ ] 35.3.5 Task Priority with Celery
Filename: `35_03_05_task_priority_celery.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Prioritize tasks in Celery queues

- [ ] priority_weight on tasks
- [ ] Priority queue configuration
- [ ] High-priority task preemption
- [ ] Fair scheduling considerations

**Expected Behavior**: Task prioritization works

---

# 35.4 KubernetesExecutor

## Overview
Running each task in its own Kubernetes pod.

## Tasks

### - [ ] 35.4.1 Basic Pod Execution
Filename: `35_04_01_basic_pod_execution.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Simple task running in K8s pod

- [ ] Standard DAG on KubernetesExecutor
- [ ] Task runs in isolated pod
- [ ] Pod lifecycle: create, run, terminate
- [ ] Observe pod in kubectl

**Expected Behavior**: Task runs in K8s pod

---

### - [ ] 35.4.2 Pod Template Configuration
Filename: `35_04_02_pod_template.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Customize pod via template

- [ ] pod_template_file in airflow.cfg
- [ ] Default pod spec for all tasks
- [ ] Include labels, annotations
- [ ] Service account configuration

**Expected Behavior**: Pods use custom template

---

### - [ ] 35.4.3 executor_config for Pod Customization
Filename: `35_04_03_executor_config_pod.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Per-task pod customization

- [ ] executor_config dict on task
- [ ] Override image
- [ ] Override resources
- [ ] Override node selector
- [ ] Combine with pod template

**Expected Behavior**: Task-specific pod configuration

---

### - [ ] 35.4.4 Resource Requests and Limits
Filename: `35_04_04_resource_requests_limits.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure CPU/memory per task

- [ ] requests.cpu, requests.memory
- [ ] limits.cpu, limits.memory
- [ ] Different resources for different tasks
- [ ] Resource quota considerations

**Expected Behavior**: Tasks get appropriate resources

---

### - [ ] 35.4.5 Pod Affinity and Tolerations
Filename: `35_04_05_affinity_tolerations.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Control pod scheduling

- [ ] Node affinity for GPU nodes
- [ ] Pod anti-affinity for distribution
- [ ] Tolerations for tainted nodes
- [ ] Node selector shortcuts

**Expected Behavior**: Pods scheduled on correct nodes

---

### - [ ] 35.4.6 Sidecar Containers
Filename: `35_04_06_sidecar_containers.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Add sidecar containers to task pods

- [ ] Logging sidecar
- [ ] Proxy sidecar
- [ ] Init containers for setup
- [ ] Container lifecycle coordination

**Expected Behavior**: Multi-container pods work correctly

---

### - [ ] 35.4.7 Volume Mounts
Filename: `35_04_07_volume_mounts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Mount volumes in task pods

- [ ] PVC volumes for shared storage
- [ ] ConfigMap volumes
- [ ] Secret volumes
- [ ] EmptyDir for scratch space

**Expected Behavior**: Data available in pods

---

### - [ ] 35.4.8 Pod GC and Cleanup
Filename: `35_04_08_pod_gc_cleanup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manage completed pod lifecycle

- [ ] delete_worker_pods configuration
- [ ] Pod retention for debugging
- [ ] Failed pod preservation
- [ ] Namespace cleanup

**Expected Behavior**: Pods cleaned up appropriately

---

### - [ ] 35.4.9 Debugging Failed Pods
Filename: `35_04_09_debugging_failed_pods.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Troubleshoot K8s executor issues

- [ ] View pod logs
- [ ] Describe pod for events
- [ ] Common failure modes
- [ ] OOMKilled, ImagePullBackOff handling

**Expected Behavior**: Ability to debug pod failures

---

# 35.5 Executor-Agnostic Patterns

## Overview
Writing DAGs that work across executors.

## Tasks

### - [ ] 35.5.1 DAG Working on Any Executor
Filename: `35_05_01_any_executor_dag.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`

**Purpose**: Best practices for portable DAGs

- [ ] No executor_config (unless needed)
- [ ] Standard operators
- [ ] No filesystem assumptions
- [ ] XCom for data passing

**Expected Behavior**: DAG runs on any executor

---

### - [ ] 35.5.2 Conditional Executor-Specific Config
Filename: `35_05_02_conditional_executor_config.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Add executor config only when needed

- [ ] Detect executor type
- [ ] Apply executor_config conditionally
- [ ] Default behavior for unknown executors
- [ ] Graceful degradation

**Expected Behavior**: Config applied when appropriate

---

### - [ ] 35.5.3 Testing DAGs Across Executors
Filename: `35_05_03_testing_across_executors.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Validate DAG on multiple executors

- [ ] Unit tests independent of executor
- [ ] Integration test approaches
- [ ] CI/CD executor matrix
- [ ] Mock executor for testing

**Expected Behavior**: DAG tested thoroughly

---

### - [ ] 35.5.4 Queue Abstraction Pattern
Filename: `35_05_04_queue_abstraction.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Abstract queue routing for portability

- [ ] Define logical queue names
- [ ] Map to physical queues per executor
- [ ] Variable-based queue configuration
- [ ] Works on Celery and K8s

**Expected Behavior**: Queue routing abstracted

---

### - [ ] 35.5.5 Resource Specification Pattern
Filename: `35_05_05_resource_specification.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Specify resource needs portably

- [ ] Pools for LocalExecutor
- [ ] Resources for K8s executor
- [ ] Queues for Celery
- [ ] Single DAG adapts to executor

**Expected Behavior**: Resources requested appropriately

---

# 35.6 Edge Executor (Airflow 3.x)

## Overview
Running tasks on remote/edge infrastructure via the Task SDK.

## Tasks

### - [ ] 35.6.1 Edge Executor Concepts
Filename: `35_06_01_edge_executor_concepts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand Edge Executor architecture

- [ ] Task SDK and remote execution
- [ ] Edge workers vs traditional workers
- [ ] Task Execution API
- [ ] Use cases: IoT, ML, specialized hardware

**Expected Behavior**: Understanding of edge execution model

---

### - [ ] 35.6.2 Configuring Edge Executor
Filename: `35_06_02_edge_executor_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Set up Edge Executor

- [ ] Configure executor = EdgeExecutor
- [ ] Edge worker setup
- [ ] API server configuration
- [ ] Authentication and security

**Expected Behavior**: Edge Executor configured and working

---

### - [ ] 35.6.3 Tasks for Edge Execution
Filename: `35_06_03_edge_tasks.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Design tasks for edge environments

- [ ] Lightweight task design
- [ ] Minimal dependencies
- [ ] Handle network unreliability
- [ ] Local data processing

**Expected Behavior**: Tasks run reliably on edge workers

---

### - [ ] 35.6.4 Edge Worker Deployment
Filename: `35_06_04_edge_worker_deployment.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Deploy edge workers in various environments

- [ ] Container-based edge workers
- [ ] Bare metal deployment
- [ ] GPU/TPU edge workers
- [ ] Auto-scaling edge workers

**Expected Behavior**: Edge workers deployed and operational

---

### - [ ] 35.6.5 Task Isolation Benefits
Filename: `35_06_05_task_isolation.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand task isolation with Edge Executor

- [ ] No metadata DB access from tasks
- [ ] API-based interaction only
- [ ] Security benefits
- [ ] Multi-tenant isolation

**Expected Behavior**: Understanding of isolation model

---

# 35.7 Multi-Executor Configuration

## Overview
Running multiple executors simultaneously in Airflow (2.10+/3.x).

## Tasks

### - [ ] 35.7.1 Multi-Executor Concepts
Filename: `35_07_01_multi_executor_concepts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand multi-executor architecture

- [ ] Why multiple executors
- [ ] Trade-offs between executors
- [ ] Per-task executor selection
- [ ] Configuration overview

**Expected Behavior**: Understanding of multi-executor benefits

---

### - [ ] 35.7.2 Configure Multiple Executors
Filename: `35_07_02_configure_multi_executor.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Set up multi-executor configuration

- [ ] `[core] executor = CeleryExecutor,KubernetesExecutor`
- [ ] Executor aliases
- [ ] Default executor selection
- [ ] Connection configuration

**Expected Behavior**: Multiple executors configured

---

### - [ ] 35.7.3 Task-Level Executor Selection
Filename: `35_07_03_task_executor_selection.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Assign executor per task

- [ ] executor parameter on task
- [ ] Use Celery for quick tasks
- [ ] Use K8s for isolated/heavy tasks
- [ ] Mixed DAG example

**Expected Behavior**: Tasks run on specified executor

---

### - [ ] 35.7.4 DAG-Level Executor Default
Filename: `35_07_04_dag_executor_default.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Set default executor for DAG

- [ ] DAG-level executor parameter
- [ ] Override at task level
- [ ] Inheritance patterns
- [ ] Migration strategies

**Expected Behavior**: DAG defaults work correctly

---

### - [ ] 35.7.5 Multi-Executor Use Cases
Filename: `35_07_05_multi_executor_use_cases.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Real-world multi-executor patterns

- [ ] Celery for fast tasks, K8s for heavy
- [ ] Local for dev, Celery for prod
- [ ] Edge for IoT, K8s for processing
- [ ] Cost optimization strategies

**Expected Behavior**: Multi-executor patterns demonstrated

---

# Summary

## Topic Completion Checklist
- [ ] All executor types covered (Local, Celery, K8s, Edge)
- [ ] Multi-executor configuration included
- [ ] Portable patterns emphasized
- [ ] K8s pod customization detailed
- [ ] Queue routing explained
- [ ] Debugging approaches included

## Related Topics
- Section 02: Task Fundamentals (task parameters)
- Section 13: Pools and Priority (resource management)
- Section 37: Performance (optimization)

## Notes for Implementation
- Test on multiple executors when possible
- Use executor_config sparingly
- Document executor assumptions
- Include kubectl commands for K8s debugging
- Show logs demonstrating behavior

---

# 35.8 Executor Debugging

## Overview
Troubleshooting executor-related issues.

## Tasks

### - [ ] 35.8.1 Debug Task Not Starting
Filename: `35_08_01_debug_task_not_starting.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Diagnose why tasks remain queued

- [ ] Check executor capacity and slots
- [ ] Verify pool availability
- [ ] Review scheduler logs
- [ ] Identify resource constraints

**Expected Behavior**: Ability to diagnose queued task issues

---

### - [ ] 35.8.2 Debug K8s Pod Failures
Filename: `35_08_02_debug_k8s_pod_failures.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Troubleshoot Kubernetes pod issues

- [ ] Interpret pod events and status
- [ ] Debug OOMKilled scenarios
- [ ] Handle ImagePullBackOff errors
- [ ] Fix permission/RBAC issues

**Expected Behavior**: Systematic K8s debugging approach

---

### - [ ] 35.8.3 Debug Celery Worker Issues
Filename: `35_08_03_debug_celery_workers.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Troubleshoot Celery executor problems

- [ ] Monitor worker heartbeats
- [ ] Debug task routing issues
- [ ] Handle worker crashes
- [ ] Diagnose broker connectivity

**Expected Behavior**: Celery debugging proficiency

---

### - [ ] 35.8.4 Executor Log Analysis
Filename: `35_08_04_executor_log_analysis.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`

**Purpose**: Extract insights from executor logs

- [ ] Identify common error patterns
- [ ] Track task execution times
- [ ] Monitor resource utilization
- [ ] Correlate scheduler and worker logs

**Expected Behavior**: Effective log-based debugging

---

### - [ ] 35.8.5 Common Executor Pitfalls
Filename: `35_08_05_common_pitfalls.py` | Tags: `['reference', 'anti-patterns', 'intermediate', 'failure']`

**Purpose**: Avoid common executor mistakes

- [ ] Task assuming shared filesystem
- [ ] Hardcoded executor dependencies
- [ ] Resource over/under-provisioning
- [ ] Ignoring executor-specific limits

**Expected Behavior**: Awareness of executor pitfalls

---

# 35.9 Executor Performance

## Overview
Optimizing executor performance and resource utilization.

## Tasks

### - [ ] 35.9.1 Executor Scaling Strategies
Filename: `35_09_01_executor_scaling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Scale executors for workload demands

- [ ] Horizontal scaling for Celery workers
- [ ] Kubernetes pod autoscaling
- [ ] Handle bursty workloads
- [ ] Right-size worker resources

**Expected Behavior**: Effective scaling configuration

---

### - [ ] 35.9.2 Task Slot Optimization
Filename: `35_09_02_task_slot_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize task slot utilization

- [ ] Balance parallelism vs resource usage
- [ ] Configure pool slots effectively
- [ ] Monitor slot utilization
- [ ] Avoid slot starvation

**Expected Behavior**: Efficient slot usage

---

### - [ ] 35.9.3 Executor Latency Reduction
Filename: `35_09_03_executor_latency.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Minimize task startup latency

- [ ] Reduce scheduler-to-executor delay
- [ ] Optimize K8s pod startup time
- [ ] Pre-warm Celery workers
- [ ] Cache container images

**Expected Behavior**: Faster task execution start

---

### - [ ] 35.9.4 Resource Utilization Monitoring
Filename: `35_09_04_resource_monitoring.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Monitor executor resource usage

- [ ] Track CPU/memory per executor type
- [ ] Identify underutilized workers
- [ ] Monitor queue depths
- [ ] Alert on resource pressure

**Expected Behavior**: Visibility into executor resources

---

### - [ ] 35.9.5 Cost Optimization
Filename: `35_09_05_cost_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize executor costs

- [ ] Use spot/preemptible instances
- [ ] Scale down during idle periods
- [ ] Right-size K8s pod resources
- [ ] Balance cost vs performance

**Expected Behavior**: Cost-effective executor configuration

---

# 35.10 Real-World Executor Patterns

## Overview
Production-ready executor configurations and patterns.

## Tasks

### - [ ] 35.10.1 High-Availability Executor Setup
Filename: `35_10_01_ha_executor_setup.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Configure executors for high availability

- [ ] Multi-zone Celery workers
- [ ] K8s pod disruption budgets
- [ ] Handle executor failures gracefully
- [ ] Implement health checks

**Expected Behavior**: Resilient executor configuration

---

### - [ ] 35.10.2 Mixed Workload Patterns
Filename: `35_10_02_mixed_workloads.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle diverse task requirements

- [ ] GPU tasks alongside CPU tasks
- [ ] Memory-intensive vs IO-intensive
- [ ] Long-running vs quick tasks
- [ ] Configure appropriate queues

**Expected Behavior**: Efficient mixed workload handling

---

### - [ ] 35.10.3 Multi-Environment Deployment
Filename: `35_10_03_multi_environment.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Deploy across dev/staging/prod

- [ ] Environment-specific executor config
- [ ] Share DAGs across environments
- [ ] Test executor changes safely
- [ ] Promote configurations

**Expected Behavior**: Consistent multi-environment setup

---

### - [ ] 35.10.4 Disaster Recovery
Filename: `35_10_04_disaster_recovery.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Recover from executor failures

- [ ] Handle complete executor loss
- [ ] Recover orphaned tasks
- [ ] Failover between executors
- [ ] Test recovery procedures

**Expected Behavior**: Robust disaster recovery

---

### - [ ] 35.10.5 Production Executor Checklist
Filename: `35_10_05_production_checklist.py` | Tags: `['reference', 'best-practices', 'intermediate', 'success']`

**Purpose**: Validate production readiness

- [ ] Security configuration verified
- [ ] Monitoring and alerting set up
- [ ] Scaling policies defined
- [ ] Documentation complete

**Expected Behavior**: Production-ready executor deployment
