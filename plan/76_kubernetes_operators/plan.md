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

# 76 Kubernetes Operators

## Overview

KubernetesPodOperator enables running tasks in isolated Kubernetes pods, providing resource isolation, custom images, and cloud-native workload execution. This section covers KubernetesPodOperator configuration, pod templates, resource management, and debugging strategies for Airflow 3.x.

## Research & Background

### Key Concepts
- **KubernetesPodOperator**: Launches pods in K8s cluster for task execution
- **Pod Template**: YAML-based pod configuration
- **Resource Requests/Limits**: CPU and memory allocation
- **Namespaces**: K8s namespace isolation for pods
- **Secrets/ConfigMaps**: Kubernetes-native configuration injection

### Airflow 3.x Features
- Improved KubernetesPodOperator with better error handling
- Pod template file support
- Enhanced logging from pods
- Deferrable mode support
- Better resource cleanup

### Prerequisites
- Airflow 3.x with kubernetes provider
- Kubernetes cluster access
- Understanding of basic Kubernetes concepts
- kubectl configured

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Configure KubernetesPodOperator for custom workloads
2. Use pod templates for complex configurations
3. Manage resources and namespaces effectively
4. Handle secrets and configuration in pods
5. Debug and troubleshoot pod failures

---

# 76.1 KubernetesPodOperator Basics

## Overview
Getting started with KubernetesPodOperator fundamentals.

## Tasks

### - [ ] 76.1.1 Basic KubernetesPodOperator
Filename: `76_01_01_basic_k8s_pod_operator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Run first task in Kubernetes pod

- [ ] Import KubernetesPodOperator from providers
- [ ] Configure minimal pod: image, name, task_id
- [ ] Specify namespace
- [ ] Run simple command in container

**Expected Behavior**: Pod created, runs, completes successfully

---

### - [ ] 76.1.2 Image and Container Configuration
Filename: `76_01_02_image_container_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure container images and commands

- [ ] Specify custom Docker image
- [ ] Set image_pull_policy (Always, IfNotPresent, Never)
- [ ] Configure cmds and arguments
- [ ] Use entrypoint overrides

**Expected Behavior**: Custom container runs with specified configuration

---

### - [ ] 76.1.3 Namespace Management
Filename: `76_01_03_namespace_management.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Run pods in different namespaces

- [ ] Specify namespace parameter
- [ ] Use default namespace from connection
- [ ] Namespace isolation patterns
- [ ] Permission requirements per namespace

**Expected Behavior**: Pods run in correct namespaces

---

### - [ ] 76.1.4 Pod Naming and Labels
Filename: `76_01_04_pod_naming_labels.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure pod identification

- [ ] Set name and name prefix
- [ ] Apply labels for organization
- [ ] Use annotations for metadata
- [ ] Label selectors for monitoring

**Expected Behavior**: Pods properly named and labeled

---

### - [ ] 76.1.5 Basic Resource Configuration
Filename: `76_01_05_basic_resources.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Set CPU and memory for pods

- [ ] Define resource requests (minimum)
- [ ] Define resource limits (maximum)
- [ ] Understand request vs limit
- [ ] Resource units (Mi, Gi, m)

**Expected Behavior**: Pod runs with allocated resources

---

# 76.2 Pod Templates and Specifications

## Overview
Using pod templates for complex pod configurations.

## Tasks

### - [ ] 76.2.1 Pod Template File
Filename: `76_02_01_pod_template_file.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use YAML pod templates

- [ ] Create pod_template_file YAML
- [ ] Reference template in operator
- [ ] Override template values
- [ ] Template inheritance patterns

**Expected Behavior**: Pod created from template

---

### - [ ] 76.2.2 Full Pod Spec Configuration
Filename: `76_02_02_full_pod_spec.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Define complete pod specification

- [ ] Use full_pod_spec parameter
- [ ] V1Pod object construction
- [ ] Multi-container pods
- [ ] Init containers

**Expected Behavior**: Complex pod spec works

---

### - [ ] 76.2.3 Volume Mounts
Filename: `76_02_03_volume_mounts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Mount volumes in pods

- [ ] ConfigMap volumes
- [ ] Secret volumes
- [ ] PersistentVolumeClaim mounts
- [ ] EmptyDir for temp storage

**Expected Behavior**: Volumes accessible in container

---

### - [ ] 76.2.4 Environment Variables
Filename: `76_02_04_environment_variables.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Pass environment to containers

- [ ] env parameter with V1EnvVar
- [ ] env_from for bulk env vars
- [ ] ValueFrom for secrets/configmaps
- [ ] Airflow variable injection

**Expected Behavior**: Environment properly set

---

### - [ ] 76.2.5 Service Accounts and Security
Filename: `76_02_05_service_accounts.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure pod security

- [ ] Set service_account_name
- [ ] Security context configuration
- [ ] Run as non-root
- [ ] Capabilities and privileges

**Expected Behavior**: Pod runs with correct permissions

---

# 76.3 Data Exchange and Communication

## Overview
Passing data between Airflow and Kubernetes pods.

## Tasks

### - [ ] 76.3.1 XCom with KubernetesPodOperator
Filename: `76_03_01_xcom_kubernetes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Return data from pods via XCom

- [ ] do_xcom_push=True
- [ ] Write to /airflow/xcom/return.json
- [ ] XCom sidecar container
- [ ] Size limitations

**Expected Behavior**: Pod output available in XCom

---

### - [ ] 76.3.2 Passing Arguments to Pods
Filename: `76_03_02_passing_arguments.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Dynamic arguments to containers

- [ ] Use arguments parameter
- [ ] Template arguments with Jinja
- [ ] Pass XCom values
- [ ] Dynamic command construction

**Expected Behavior**: Arguments passed correctly

---

### - [ ] 76.3.3 ConfigMaps for Configuration
Filename: `76_03_03_configmaps_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use ConfigMaps for task config

- [ ] Create ConfigMap from Airflow
- [ ] Mount ConfigMap as volume
- [ ] ConfigMap as environment
- [ ] Dynamic ConfigMap creation

**Expected Behavior**: Configuration available in pod

---

### - [ ] 76.3.4 Secrets Management in Pods
Filename: `76_03_04_secrets_in_pods.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Securely pass secrets to pods

- [ ] Kubernetes Secret mounting
- [ ] Secret as environment variable
- [ ] Airflow connection secrets
- [ ] secrets parameter usage

**Expected Behavior**: Secrets securely available

---

### - [ ] 76.3.5 Shared Storage Between Tasks
Filename: `76_03_05_shared_storage.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Share data between pod tasks

- [ ] PersistentVolumeClaim sharing
- [ ] Write/read patterns
- [ ] Concurrent access considerations
- [ ] Cleanup strategies

**Expected Behavior**: Data shared between pods

---

# 76.4 Advanced Features

## Overview
Advanced KubernetesPodOperator capabilities.

## Tasks

### - [ ] 76.4.1 Deferrable KubernetesPodOperator
Filename: `76_04_01_deferrable_k8s.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Run pods without blocking workers

- [ ] deferrable=True parameter
- [ ] KubernetesPodTrigger
- [ ] Long-running pod efficiency
- [ ] Compare to blocking mode

**Expected Behavior**: Worker freed during pod execution

---

### - [ ] 76.4.2 Pod Affinity and Node Selection
Filename: `76_04_02_affinity_node_selection.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Control pod placement

- [ ] node_selector for simple selection
- [ ] Affinity rules (node, pod)
- [ ] Anti-affinity patterns
- [ ] Tolerations for tainted nodes

**Expected Behavior**: Pod scheduled on correct nodes

---

### - [ ] 76.4.3 Resource Quotas and Limits
Filename: `76_04_03_resource_quotas.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manage resource allocation

- [ ] GPU resources (nvidia.com/gpu)
- [ ] Extended resources
- [ ] LimitRange compliance
- [ ] ResourceQuota considerations

**Expected Behavior**: Resources properly allocated

---

### - [ ] 76.4.4 Sidecar Containers
Filename: `76_04_04_sidecar_containers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Multi-container pod patterns

- [ ] Add sidecar containers
- [ ] Logging sidecars
- [ ] Proxy sidecars
- [ ] Container lifecycle management

**Expected Behavior**: Sidecar pattern works

---

### - [ ] 76.4.5 Init Containers
Filename: `76_04_05_init_containers.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Pre-task initialization

- [ ] Define init_containers
- [ ] Download dependencies
- [ ] Setup shared volumes
- [ ] Wait for services

**Expected Behavior**: Init containers run before main

---

# 76.5 Troubleshooting and Operations

## Overview
Debugging and operating Kubernetes pod tasks.

## Tasks

### - [ ] 76.5.1 Pod Failure Debugging
Filename: `76_05_01_pod_failure_debugging.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Debug failing pods

- [ ] Get pod logs
- [ ] get_logs parameter
- [ ] Log retrieval on failure
- [ ] kubectl debugging commands

**Expected Behavior**: Understand failure diagnosis

---

### - [ ] 76.5.2 Image Pull Errors
Filename: `76_05_02_image_pull_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

**Purpose**: Handle image pull issues

- [ ] ImagePullBackOff diagnosis
- [ ] Private registry authentication
- [ ] image_pull_secrets parameter
- [ ] Registry troubleshooting

**Expected Behavior**: Image pull issues resolved

---

### - [ ] 76.5.3 Pod Cleanup and Deletion
Filename: `76_05_03_pod_cleanup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manage pod lifecycle

- [ ] is_delete_operator_pod parameter
- [ ] Cleanup on failure
- [ ] Pod retention for debugging
- [ ] Orphaned pod handling

**Expected Behavior**: Pods cleaned up properly

---

### - [ ] 76.5.4 Timeout and Retry Configuration
Filename: `76_05_04_timeout_retry.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle long-running pods

- [ ] startup_timeout_seconds
- [ ] Task timeout
- [ ] Pod restart policies
- [ ] Retry with backoff

**Expected Behavior**: Timeouts handled gracefully

---

### - [ ] 76.5.5 Resource Monitoring
Filename: `76_05_05_resource_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Monitor pod resource usage

- [ ] Metrics collection
- [ ] OOMKilled detection
- [ ] Resource adjustment strategies
- [ ] Kubernetes events monitoring

**Expected Behavior**: Resource issues identified

---

# 76.6 Advanced Patterns

## Overview
Production-ready patterns for KubernetesPodOperator.

## Tasks

### - [ ] 76.6.1 Dynamic Pod Generation
Filename: `76_06_01_dynamic_pod_generation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Generate pod specs dynamically

- [ ] Compute pod spec at runtime
- [ ] Conditional resource allocation
- [ ] Environment-based configurations
- [ ] Template-driven pod specs

**Expected Behavior**: Pods adapt to runtime context

---

### - [ ] 76.6.2 Multi-Cluster Pod Execution
Filename: `76_06_02_multi_cluster_execution.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Run pods across multiple clusters

- [ ] Multiple cluster connections
- [ ] Cluster selection logic
- [ ] Cross-cluster data patterns
- [ ] Failover between clusters

**Expected Behavior**: Pods run on appropriate cluster

---

### - [ ] 76.6.3 Spot/Preemptible Instance Handling
Filename: `76_06_03_spot_instance_handling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Handle node preemption gracefully

- [ ] Tolerate spot node eviction
- [ ] Checkpoint and resume patterns
- [ ] Graceful termination handling
- [ ] Cost optimization strategies

**Expected Behavior**: Tasks survive node preemption

---

### - [ ] 76.6.4 Job-Based Execution Pattern
Filename: `76_06_04_job_based_execution.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Use K8s Jobs instead of bare pods

- [ ] Kubernetes Job semantics
- [ ] Backoff and retry via Job
- [ ] Job completion tracking
- [ ] Job cleanup strategies

**Expected Behavior**: Jobs provide better guarantees

---

### - [ ] 76.6.5 Batch Processing with Pods
Filename: `76_06_05_batch_processing_pods.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Process batches using pod parallelism

- [ ] Dynamic task mapping with pods
- [ ] Fan-out pod patterns
- [ ] Result aggregation
- [ ] Resource limits for batches

**Expected Behavior**: Batch workloads scale efficiently

---

# 76.7 Anti-Patterns and Common Mistakes

## Overview
Avoiding common pitfalls with KubernetesPodOperator.

## Tasks

### - [ ] 76.7.1 Resource Request Mistakes
Filename: `76_07_01_resource_mistakes.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid resource misconfiguration

- [ ] Missing resource requests
- [ ] Limits without requests
- [ ] Oversized resource requests
- [ ] OOMKilled without proper limits

**Expected Behavior**: Understand resource pitfalls

---

### - [ ] 76.7.2 Image Pull Problems
Filename: `76_07_02_image_pull_problems.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid image-related issues

- [ ] Using :latest tag
- [ ] Missing imagePullPolicy
- [ ] Private registry auth failures
- [ ] Large image pull times

**Expected Behavior**: Image problems prevented

---

### - [ ] 76.7.3 Pod Lifecycle Misunderstandings
Filename: `76_07_03_lifecycle_misunderstandings.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Understand pod lifecycle correctly

- [ ] Confusing task and pod state
- [ ] Not waiting for pod completion
- [ ] Ignoring termination grace period
- [ ] Orphaned pods accumulation

**Expected Behavior**: Lifecycle properly managed

---

### - [ ] 76.7.4 Network and DNS Issues
Filename: `76_07_04_network_dns_issues.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid network misconfigurations

- [ ] DNS resolution failures
- [ ] Service discovery issues
- [ ] Network policy blocking
- [ ] Cross-namespace access

**Expected Behavior**: Network issues diagnosed

---

### - [ ] 76.7.5 Security Context Errors
Filename: `76_07_05_security_context_errors.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle security constraints

- [ ] PodSecurityPolicy violations
- [ ] Running as root issues
- [ ] Capability requirements
- [ ] SELinux/AppArmor conflicts

**Expected Behavior**: Security errors resolved

---

# 76.8 Testing KubernetesPodOperator

## Overview
Testing strategies for Kubernetes-based tasks.

## Tasks

### - [ ] 76.8.1 Local Testing with Kind/Minikube
Filename: `76_08_01_local_testing_kind.py` | Tags: `['reference', 'testing', 'beginner', 'success']`

**Purpose**: Test pods locally

- [ ] Kind cluster setup
- [ ] Minikube configuration
- [ ] Local registry usage
- [ ] Fast iteration cycle

**Expected Behavior**: Local K8s testing works

---

### - [ ] 76.8.2 Unit Testing Pod Specs
Filename: `76_08_02_unit_testing_specs.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test pod configurations

- [ ] Validate pod spec generation
- [ ] Test volume mounts
- [ ] Verify environment variables
- [ ] Assert resource configurations

**Expected Behavior**: Pod specs validated

---

### - [ ] 76.8.3 Mocking Kubernetes API
Filename: `76_08_03_mocking_k8s_api.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test without real cluster

- [ ] Mock K8s client
- [ ] Simulate pod states
- [ ] Test error handling
- [ ] Verify API interactions

**Expected Behavior**: Tests run without cluster

---

### - [ ] 76.8.4 Integration Testing Pods
Filename: `76_08_04_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: End-to-end pod execution tests

- [ ] Test pod completes successfully
- [ ] Verify XCom returned
- [ ] Check resource cleanup
- [ ] Validate log retrieval

**Expected Behavior**: Integration tests pass

---

### - [ ] 76.8.5 CI/CD Pipeline Testing
Filename: `76_08_05_cicd_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Test in CI/CD environments

- [ ] GitHub Actions with K8s
- [ ] Test cluster provisioning
- [ ] Parallel test execution
- [ ] Cleanup automation

**Expected Behavior**: CI tests K8s operators

---

# 76.9 Performance Optimization

## Overview
Optimizing KubernetesPodOperator performance.

## Tasks

### - [ ] 76.9.1 Pod Startup Optimization
Filename: `76_09_01_pod_startup_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Reduce pod startup latency

- [ ] Pre-pulled images
- [ ] Node affinity for warm nodes
- [ ] Lightweight init containers
- [ ] Resource pre-allocation

**Expected Behavior**: Pods start faster

---

### - [ ] 76.9.2 Image Optimization for Pods
Filename: `76_09_02_image_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize container images

- [ ] Multi-stage builds
- [ ] Layer caching strategies
- [ ] Minimize image size
- [ ] Base image selection

**Expected Behavior**: Images optimized for K8s

---

### - [ ] 76.9.3 Resource Right-Sizing
Filename: `76_09_03_resource_right_sizing.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Allocate correct resources

- [ ] Profile actual usage
- [ ] Vertical Pod Autoscaler
- [ ] Right-size recommendations
- [ ] Cost vs performance balance

**Expected Behavior**: Resources properly sized

---

### - [ ] 76.9.4 Parallel Pod Execution
Filename: `76_09_04_parallel_pod_execution.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Run multiple pods concurrently

- [ ] Pool configuration for K8s
- [ ] Namespace resource quotas
- [ ] Node pool scaling
- [ ] Concurrent execution limits

**Expected Behavior**: Parallel execution efficient

---

### - [ ] 76.9.5 Caching and Reuse Patterns
Filename: `76_09_05_caching_patterns.py` | Tags: `['reference', 'performance', 'advanced', 'success']`

**Purpose**: Cache data across pod runs

- [ ] PVC for shared cache
- [ ] Init container warm-up
- [ ] Dependency caching
- [ ] Build cache persistence

**Expected Behavior**: Caching reduces execution time

---

# 76.10 Real-World Examples

## Overview
Complete real-world use cases for KubernetesPodOperator.

## Tasks

### - [ ] 76.10.1 ML Model Training Pipeline
Filename: `76_10_01_ml_training_pipeline.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Train ML models in K8s pods

- [ ] GPU resource allocation
- [ ] Training data mounting
- [ ] Model artifact export
- [ ] Distributed training setup

**Expected Behavior**: ML training runs in K8s

---

### - [ ] 76.10.2 Data Processing with Spark
Filename: `76_10_02_spark_on_kubernetes.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Run Spark jobs in pods

- [ ] Spark operator integration
- [ ] Driver and executor pods
- [ ] Dynamic allocation
- [ ] Log aggregation

**Expected Behavior**: Spark jobs complete

---

### - [ ] 76.10.3 ETL with Custom Images
Filename: `76_10_03_etl_custom_images.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: ETL using specialized containers

- [ ] Custom ETL image
- [ ] Source/target connections
- [ ] Data volume handling
- [ ] Incremental processing

**Expected Behavior**: ETL pipeline runs

---

### - [ ] 76.10.4 Integration Testing Environment
Filename: `76_10_04_integration_test_env.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Spin up test environments

- [ ] Database containers
- [ ] Service dependencies
- [ ] Test execution
- [ ] Environment teardown

**Expected Behavior**: Test env provisioned and cleaned

---

### - [ ] 76.10.5 Multi-Language Workflow
Filename: `76_10_05_multi_language_workflow.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Run tasks in different languages

- [ ] Python, R, Java pods
- [ ] Language-specific images
- [ ] Data passing between languages
- [ ] Polyglot pipeline

**Expected Behavior**: Multiple languages work together

---

# Summary

## Topic Completion Checklist
- [ ] Basic KubernetesPodOperator usage covered
- [ ] Pod templates documented
- [ ] Data exchange patterns included
- [ ] Advanced features explained
- [ ] Troubleshooting guidance provided
- [ ] Advanced patterns documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Real-world examples provided

## Related Topics
- Section 35: Executors (KubernetesExecutor)
- Section 82: Secrets Backends
- Section 88: Containerization

## Notes for Implementation
- Requires Kubernetes cluster
- Test with minikube or kind locally
- Include real YAML examples
- Show kubectl commands
- Demonstrate failure scenarios
