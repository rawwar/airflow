# 113 - Astronomer Cosmos dbt Integration

## Overview
Astronomer Cosmos integration: DbtDag, DbtTaskGroup, model-level tasks, test execution, manifests, profiles, selectors, and dbt Cloud.

---

## Section 1: Cosmos Fundamentals

### - [ ] 113.1.1 Cosmos Overview and Installation
Filename: `113_01_01_cosmos_overview_installation.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand Cosmos purpose
- [ ] Install astronomer-cosmos package
- [ ] Verify dbt CLI availability
- [ ] Basic configuration requirements

### - [ ] 113.1.2 Project Structure for Cosmos
Filename: `113_01_02_project_structure_cosmos.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] dbt project directory layout
- [ ] Airflow DAGs folder integration
- [ ] profiles.yml location options
- [ ] Environment variable configuration

### - [ ] 113.1.3 DbtDag Basic Usage
Filename: `113_01_03_dbtdag_basic_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Create DbtDag with minimal config
- [ ] Specify project and profiles paths
- [ ] Set execution mode (local, docker, k8s)
- [ ] View generated task structure

### - [ ] 113.1.4 DbtTaskGroup Integration
Filename: `113_01_04_dbttaskgroup_integration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Embed DbtTaskGroup in existing DAG
- [ ] Configure task group parameters
- [ ] Connect with upstream/downstream tasks
- [ ] Multiple task groups in one DAG

### - [ ] 113.1.5 Execution Modes
Filename: `113_01_05_execution_modes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] LocalExecutionMode configuration
- [ ] DockerExecutionMode setup
- [ ] KubernetesExecutionMode setup
- [ ] VirtualenvExecutionMode usage

---

## Section 2: Model-Level Task Generation

### - [ ] 113.2.1 Model to Task Mapping
Filename: `113_02_01_model_to_task_mapping.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] One task per dbt model
- [ ] Automatic dependency detection
- [ ] Seed and snapshot tasks
- [ ] Task naming conventions

### - [ ] 113.2.2 Manifest Parsing
Filename: `113_02_02_manifest_parsing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Use pre-built manifest.json
- [ ] Manifest generation at runtime
- [ ] Manifest caching strategies
- [ ] Handle manifest refresh

### - [ ] 113.2.3 Select Models with Selectors
Filename: `113_02_03_select_models_selectors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Use select parameter
- [ ] Exclude specific models
- [ ] Tag-based selection
- [ ] Path-based selection

### - [ ] 113.2.4 Node Conversion Configuration
Filename: `113_02_04_node_conversion_config.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] RenderConfig options
- [ ] Select nodes to render
- [ ] Test behavior configuration
- [ ] Emit datasets configuration

### - [ ] 113.2.5 Custom Task Configuration
Filename: `113_02_05_custom_task_configuration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Override task parameters
- [ ] Set retries per model
- [ ] Configure timeouts
- [ ] Add task callbacks

---

## Section 3: Test Execution Strategies

### - [ ] 113.3.1 Test Behavior Options
Filename: `113_03_01_test_behavior_options.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] TestBehavior.NONE
- [ ] TestBehavior.AFTER_EACH
- [ ] TestBehavior.AFTER_ALL
- [ ] TestBehavior.BUILD (combined)

### - [ ] 113.3.2 After Each Test Pattern
Filename: `113_03_02_after_each_test_pattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Run tests after each model
- [ ] Fail fast on test failure
- [ ] Test task dependencies
- [ ] View test results in Airflow

### - [ ] 113.3.3 After All Test Pattern
Filename: `113_03_03_after_all_test_pattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Run all tests at end
- [ ] Consolidate test results
- [ ] Parallel test execution
- [ ] Test task grouping

### - [ ] 113.3.4 Test Selection and Filtering
Filename: `113_03_04_test_selection_filtering.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Select specific tests
- [ ] Filter by test type
- [ ] Exclude tests
- [ ] Custom test commands

### - [ ] 113.3.5 Test Failure Handling
Filename: `113_03_05_test_failure_handling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure warn vs error severity
- [ ] Continue on test failure
- [ ] Alert on test failures
- [ ] Test result reporting

---

## Section 4: Profiles and Connections

### - [ ] 113.4.1 Profiles Configuration
Filename: `113_04_01_profiles_configuration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] profiles.yml structure
- [ ] Target selection
- [ ] Environment variable substitution
- [ ] Multiple target environments

### - [ ] 113.4.2 Airflow Connection Integration
Filename: `113_04_02_airflow_connection_integration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Map Airflow connections to dbt
- [ ] ProfileConfig with connection_id
- [ ] Automatic profile generation
- [ ] Connection type mapping

### - [ ] 113.4.3 Dynamic Profile Generation
Filename: `113_04_03_dynamic_profile_generation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Generate profiles at runtime
- [ ] Environment-specific profiles
- [ ] Secret injection
- [ ] Profile validation

### - [ ] 113.4.4 Multi-Database Profiles
Filename: `113_04_04_multi_database_profiles.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure multiple targets
- [ ] Cross-database dbt projects
- [ ] Target switching logic
- [ ] Connection pooling

### - [ ] 113.4.5 Secrets Management
Filename: `113_04_05_secrets_management.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Integrate with secrets backend
- [ ] Avoid plaintext credentials
- [ ] Environment-based secrets
- [ ] Rotation handling

---

## Section 5: Advanced Cosmos Patterns

### - [ ] 113.5.1 Custom Operator Mapping
Filename: `113_05_01_custom_operator_mapping.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Override default operators
- [ ] Custom run operator
- [ ] Custom test operator
- [ ] Operator configuration override

### - [ ] 113.5.2 Virtual Environment Execution
Filename: `113_05_02_virtual_environment_execution.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] VirtualenvExecutionMode setup
- [ ] dbt version isolation
- [ ] Package dependency management
- [ ] Cache virtual environments

### - [ ] 113.5.3 Docker Execution Mode
Filename: `113_05_03_docker_execution_mode.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure Docker operator
- [ ] Custom dbt Docker image
- [ ] Mount project files
- [ ] Resource limits

### - [ ] 113.5.4 Kubernetes Execution Mode
Filename: `113_05_04_kubernetes_execution_mode.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] KubernetesPodOperator integration
- [ ] Pod template configuration
- [ ] Resource requests/limits
- [ ] Node selector and affinity

### - [ ] 113.5.5 Incremental Model Handling
Filename: `113_05_05_incremental_model_handling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure full refresh
- [ ] Handle incremental failures
- [ ] Force full refresh option
- [ ] Backfill strategies

---

## Section 6: dbt Cloud Integration

### - [ ] 113.6.1 dbt Cloud Operator Basics
Filename: `113_06_01_dbt_cloud_operator_basics.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] DbtCloudRunJobOperator setup
- [ ] API token configuration
- [ ] Account and job IDs
- [ ] Trigger job execution

### - [ ] 113.6.2 dbt Cloud Job Monitoring
Filename: `113_06_02_dbt_cloud_job_monitoring.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Wait for job completion
- [ ] Poll job status
- [ ] Handle job failures
- [ ] Retrieve run artifacts

### - [ ] 113.6.3 dbt Cloud with Cosmos
Filename: `113_06_03_dbt_cloud_with_cosmos.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] DbtCloudExecutionMode
- [ ] Map models to Cloud jobs
- [ ] Hybrid local/cloud execution
- [ ] Cost optimization

### - [ ] 113.6.4 dbt Cloud Webhooks
Filename: `113_06_04_dbt_cloud_webhooks.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure webhook triggers
- [ ] Airflow webhook receiver
- [ ] Event-driven dbt execution
- [ ] Bi-directional integration

### - [ ] 113.6.5 dbt Cloud CI/CD Integration
Filename: `113_06_05_dbt_cloud_cicd_integration.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Slim CI job triggering
- [ ] PR environment handling
- [ ] Deployment job orchestration
- [ ] Environment promotion

---

## Section 7: Cosmos Anti-Patterns

### - [ ] 113.7.1 Running All Models in One Task
Filename: `113_07_01_all_models_one_task_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Lost granularity
- [ ] No parallel execution
- [ ] Single point of failure
- [ ] Model-per-task benefits

### - [ ] 113.7.2 Ignoring Test Failures
Filename: `113_07_02_ignoring_tests_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Data quality risks
- [ ] Silent corruption
- [ ] Proper test handling
- [ ] Alert configuration

### - [ ] 113.7.3 Manifest Staleness
Filename: `113_07_03_stale_manifest_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Model changes missed
- [ ] Out-of-sync DAG
- [ ] Manifest refresh strategies
- [ ] CI/CD manifest generation

### - [ ] 113.7.4 Over-Selecting Models
Filename: `113_07_04_over_selecting_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Running unnecessary models
- [ ] Resource waste
- [ ] Selector optimization
- [ ] Tag-based organization

### - [ ] 113.7.5 Hardcoded Profile Credentials
Filename: `113_07_05_hardcoded_creds_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Security risks
- [ ] Environment issues
- [ ] Airflow connection integration
- [ ] Secrets backend usage

---

## Section 8: Testing Cosmos DAGs

### - [ ] 113.8.1 Unit Testing Cosmos Configuration
Filename: `113_08_01_unit_testing_config.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test DbtDag instantiation
- [ ] Validate selector behavior
- [ ] Test profile configuration
- [ ] Mock manifest parsing

### - [ ] 113.8.2 Integration Testing dbt Execution
Filename: `113_08_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test against real database
- [ ] Validate model outputs
- [ ] Test failure scenarios
- [ ] End-to-end validation

### - [ ] 113.8.3 Testing Model Dependencies
Filename: `113_08_03_testing_dependencies.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Validate task dependencies
- [ ] Test execution order
- [ ] Circular dependency detection
- [ ] Dependency graph validation

### - [ ] 113.8.4 Testing Test Behavior
Filename: `113_08_04_testing_test_behavior.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Validate test execution
- [ ] Test failure handling
- [ ] Test result reporting
- [ ] Test-only DAG runs

### - [ ] 113.8.5 Performance Testing Cosmos
Filename: `113_08_05_performance_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Measure DAG parse time
- [ ] Model execution benchmarks
- [ ] Parallel execution testing
- [ ] Resource usage profiling

---

## Section 9: Cosmos Performance

### - [ ] 113.9.1 Optimizing DAG Parse Time
Filename: `113_09_01_optimize_parse_time.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Pre-built manifest usage
- [ ] Manifest caching
- [ ] Lazy model loading
- [ ] Parse time monitoring

### - [ ] 113.9.2 Parallel Model Execution
Filename: `113_09_02_parallel_execution.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Configure parallelism
- [ ] Pool-based concurrency
- [ ] Database connection limits
- [ ] Optimal parallelism tuning

### - [ ] 113.9.3 Incremental Model Optimization
Filename: `113_09_03_incremental_optimization.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Incremental materialization
- [ ] Partition strategies
- [ ] Change detection
- [ ] Full refresh scheduling

### - [ ] 113.9.4 Resource Management
Filename: `113_09_04_resource_management.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Container resource limits
- [ ] Kubernetes resources
- [ ] Worker allocation
- [ ] Memory optimization

### - [ ] 113.9.5 Large Project Handling
Filename: `113_09_05_large_projects.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Hundreds of models
- [ ] Split into multiple DAGs
- [ ] Selector-based partitioning
- [ ] Dependency management

---

## Section 10: Real-World Cosmos Usage

### - [ ] 113.10.1 Enterprise dbt Orchestration
Filename: `113_10_01_enterprise_orchestration.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Multi-project setup
- [ ] Team isolation
- [ ] Environment promotion
- [ ] Governance patterns

### - [ ] 113.10.2 dbt + Data Quality Pipeline
Filename: `113_10_02_dbt_quality_pipeline.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] dbt tests integration
- [ ] Great Expectations
- [ ] Quality gates
- [ ] Failure alerting

### - [ ] 113.10.3 dbt + Reverse ETL
Filename: `113_10_03_dbt_reverse_etl.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Transform then export
- [ ] Census/Hightouch integration
- [ ] Dependency coordination
- [ ] Sync monitoring

### - [ ] 113.10.4 dbt + ML Feature Engineering
Filename: `113_10_04_dbt_ml_features.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Feature tables with dbt
- [ ] Feature store sync
- [ ] Training data prep
- [ ] Feature freshness

### - [ ] 113.10.5 Multi-Warehouse dbt
Filename: `113_10_05_multi_warehouse.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Snowflake + BigQuery
- [ ] Cross-warehouse models
- [ ] Connection switching
- [ ] Unified orchestration

---

# Summary

## Topic Completion Checklist
- [ ] Cosmos fundamentals covered
- [ ] Model-level tasks explained
- [ ] Test execution documented
- [ ] Profiles and connections addressed
- [ ] Advanced patterns included
- [ ] dbt Cloud integration documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization addressed
- [ ] Real-world examples provided

## Related Topics
- Section 112: OpenLineage
- Section 68: Data Quality
- Section 79: SQL Operators
- Section 71: Incremental Processing

## Notes for Implementation
- Use pre-built manifests in production
- Configure proper test behavior
- Monitor model execution times
- Plan connection management
- Leverage Cosmos for dbt governance
