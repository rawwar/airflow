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

# 04 Dynamic Dags

## Overview

This section covers all aspects of 04 dynamic dags.

---

# 4.1 Dynamic DAG Generation Basics

### - [ ] 4.4.1.1 Loop-based DAG generation
Filename: `04_01_01_loopbased_dag_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create multiple DAGs using for loop in single file
- [ ] Show globals() assignment pattern
- [ ] Include unique dag_id per iteration

### - [ ] 4.4.1.2 Configuration-driven DAG generation
Filename: `04_01_02_configurationdriven_dag_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAGs from YAML/JSON configuration file
- [ ] Show reading config and generating DAGs
- [ ] Include validation of configuration

### - [ ] 4.4.1.3 Dynamic task creation within DAG
Filename: `04_01_03_dynamic_task_creation_within_dag.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dynamically generated tasks
- [ ] Show loop-based task creation with >> operator
- [ ] Include task_id uniqueness handling

### - [ ] 4.4.1.4 Template-based DAG generation
Filename: `04_01_04_templatebased_dag_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Jinja2 templates for DAG structure
- [ ] Show template rendering with different parameters
- [ ] Include dag_file template pattern

### - [ ] 4.4.1.5 Factory pattern for DAG creation
Filename: `04_01_05_factory_pattern_for_dag_creation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG factory function returning DAG objects
- [ ] Show parameterized DAG creation
- [ ] Include multiple DAG variants from single factory

### - [ ] 4.4.1.6 Dynamic DAG from database
Filename: `04_01_06_dynamic_dag_from_database.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG reading configuration from database
- [ ] Show connection usage in DAG file parsing
- [ ] Include failure handling when DB unavailable

---

# 4.2 Dynamic Task Mapping

### - [ ] 4.4.2.1 Basic expand() usage
Filename: `04_02_01_basic_expand_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using .expand() for dynamic task instances
- [ ] Show mapping over list of parameters
- [ ] Include downstream task dependency

### - [ ] 4.4.2.2 expand() with multiple parameters
Filename: `04_02_02_expand_with_multiple_parameters.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using .expand() with multiple parameter lists
- [ ] Show zip vs product expansion
- [ ] Include map_index_template usage

### - [ ] 4.4.2.3 expand() with partial()
Filename: `04_02_03_expand_with_partial.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG combining .partial() and .expand()
- [ ] Show static vs dynamic parameters
- [ ] Include complex parameter combinations

### - [ ] 4.4.2.4 Nested expand()
Filename: `04_02_04_nested_expand.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with multiple levels of expand()
- [ ] Show fan-out patterns
- [ ] Include max_active_tis_per_dag consideration

### - [ ] 4.4.2.5 expand() with TaskFlow
Filename: `04_02_05_expand_with_taskflow.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using .expand() with @task decorated functions
- [ ] Show return value handling from mapped tasks
- [ ] Include collecting results from all mapped instances

### - [ ] 4.4.2.6 expand_kwargs()
Filename: `04_02_06_expand_kwargs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using .expand_kwargs() for dict expansion
- [ ] Show passing different kwargs to each instance
- [ ] Include use cases for expand_kwargs

---

# 4.3 Dynamic Task Mapping Advanced

### - [ ] 4.4.3.1 Dynamic task mapping with XCom
Filename: `04_03_01_dynamic_task_mapping_with_xcom.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG where expand() input comes from upstream XCom
- [ ] Show runtime task generation based on data
- [ ] Include empty list handling

### - [ ] 4.4.3.2 Map index access in tasks
Filename: `04_03_02_map_index_access_in_tasks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG accessing map_index in mapped tasks
- [ ] Show using map_index for data partitioning
- [ ] Include Jinja template {{ ti.map_index }}

### - [ ] 4.4.3.3 Reducing mapped task outputs
Filename: `04_03_03_reducing_mapped_task_outputs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with reduction task after expand()
- [ ] Show collecting and aggregating mapped results
- [ ] Include ti.xcom_pull with map_indexes parameter

### - [ ] 4.4.3.4 Conditional mapping
Filename: `04_03_04_conditional_mapping.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with conditional expand() based on upstream data
- [ ] Show using @task.branch before expand()
- [ ] Include empty expansion handling

### - [ ] 4.4.3.5 Dynamic mapping with sensors
Filename: `04_03_05_dynamic_mapping_with_sensors.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using expand() with sensor tasks
- [ ] Show mapping sensors over multiple resources
- [ ] Include mode='reschedule' with many mapped sensors

### - [ ] 4.4.3.6 Dynamic mapping limits
Filename: `04_03_06_dynamic_mapping_limits.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating max_map_length
- [ ] Show failure when exceeding limit
- [ ] Include configuration of max_map_length

---

# 4.4 Dynamic DAG Updates

### - [ ] 4.4.4.1 DAG versioning with dynamic generation
Filename: `04_04_01_dag_versioning_with_dynamic_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with version number in dag_id
- [ ] Show updating DAG generation logic
- [ ] Include handling multiple versions

### - [ ] 4.4.4.2 Hot-reloading dynamic DAGs
Filename: `04_04_02_hotreloading_dynamic_dags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG that changes based on external file
- [ ] Show DAG file refresh behavior
- [ ] Include dag_dir_list_interval consideration

### - [ ] 4.4.4.3 Conditional DAG creation
Filename: `04_04_03_conditional_dag_creation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG only if certain conditions met
- [ ] Show if/else in DAG file for DAG creation
- [ ] Include environment-based DAG creation

### - [ ] 4.4.4.4 Dynamic DAG deletion
Filename: `04_04_04_dynamic_dag_deletion.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create pattern for removing dynamically created DAGs
- [ ] Show handling DAG removal from config
- [ ] Include cleanup of removed DAG runs

### - [ ] 4.4.4.5 Dynamic DAG with incremental tasks
Filename: `04_04_05_dynamic_dag_with_incremental_tasks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG that adds tasks over time
- [ ] Show task addition to existing DAG
- [ ] Include handling of active DAG runs during update

### - [ ] 4.4.4.6 Dynamic DAG generation errors
Filename: `04_04_06_dynamic_dag_generation_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG file with intentional dynamic generation error
- [ ] Show parsing failure in UI
- [ ] Include error debugging strategies

---

# 4.5 Dynamic DAG Patterns

### - [ ] 4.4.5.1 Multi-tenancy with dynamic DAGs
Filename: `04_05_01_multitenancy_with_dynamic_dags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG per tenant/customer from list
- [ ] Show isolated DAGs with shared logic
- [ ] Include tenant-specific parameters

### - [ ] 4.4.5.2 Dynamic DAG from API
Filename: `04_05_02_dynamic_dag_from_api.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG fetching configuration from REST API
- [ ] Show API call during DAG file parsing
- [ ] Include caching and error handling

### - [ ] 4.4.5.3 Dynamic DAG with inheritance
Filename: `04_05_03_dynamic_dag_with_inheritance.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create base DAG class with dynamic subclass DAGs
- [ ] Show OOP patterns for DAG generation
- [ ] Include shared task definitions

### - [ ] 4.4.5.4 Dynamic DAG from Git repository
Filename: `04_05_04_dynamic_dag_from_git_repository.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG reading DAG specs from Git repo
- [ ] Show cloning and parsing repository content
- [ ] Include version tracking

### - [ ] 4.4.5.5 Cross-DAG dynamic dependencies
Filename: `04_05_05_crossdag_dynamic_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create multiple dynamic DAGs with inter-DAG dependencies
- [ ] Show ExternalTaskSensor with dynamic DAG IDs
- [ ] Include dependency resolution

### - [ ] 4.4.5.6 Dynamic DAG monitoring
Filename: `04_05_06_dynamic_dag_monitoring.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG monitoring dynamically created DAGs
- [ ] Show listing all generated DAGs
- [ ] Include health check across dynamic DAGs

---

# 4.6 Dynamic DAG Best Practices

### - [ ] 4.4.6.1 Performance optimization for dynamic DAGs
Filename: `04_06_01_performance_optimization_for_dynamic_dags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with optimized dynamic generation
- [ ] Show caching expensive operations
- [ ] Include DAG parsing time consideration

### - [ ] 4.4.6.2 Testing dynamic DAG generation
Filename: `04_06_02_testing_dynamic_dag_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create tests for DAG generation logic
- [ ] Show validation of generated DAG structure
- [ ] Include pytest examples for dynamic DAGs

### - [ ] 4.4.6.3 Dynamic DAG documentation
Filename: `04_06_03_dynamic_dag_documentation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create well-documented dynamic DAG generation
- [ ] Show doc string generation for created DAGs
- [ ] Include metadata for generated DAGs

### - [ ] 4.4.6.4 Error handling in dynamic generation
Filename: `04_06_04_error_handling_in_dynamic_generation.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create robust error handling in DAG generation
- [ ] Show fallback when config unavailable
- [ ] Include default DAG creation on errors

### - [ ] 4.4.6.5 Security in dynamic DAGs
Filename: `04_06_05_security_in_dynamic_dags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with secure dynamic generation
- [ ] Show input validation for external configs
- [ ] Include SQL injection prevention in DB-driven DAGs

### - [ ] 4.4.6.6 Dynamic DAG migration strategies
Filename: `04_06_06_dynamic_dag_migration_strategies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create migration path from static to dynamic DAGs
- [ ] Show preserving DAG run history
- [ ] Include gradual rollout strategy

---

# 4.7 Dynamic DAG Anti-patterns

### - [ ] 4.4.7.1 Excessive dynamic DAG generation
Filename: `04_07_01_excessive_dynamic_dag_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create example of too many dynamic DAGs
- [ ] Show scheduler performance impact
- [ ] Include alternative approaches (single DAG with mapping)

### - [ ] 4.4.7.2 Complex logic in DAG files
Filename: `04_07_02_complex_logic_in_dag_files.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Create DAG with overly complex generation logic
- [ ] Show parsing delays and issues
- [ ] Include refactoring to external module

### - [ ] 4.4.7.3 Dynamic generation without idempotency
Filename: `04_07_03_dynamic_generation_without_idempotency.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with non-idempotent generation
- [ ] Show issues with repeated parsing
- [ ] Include fixing with deterministic generation

### - [ ] 4.4.7.4 Hardcoded values in dynamic DAGs
Filename: `04_07_04_hardcoded_values_in_dynamic_dags.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create anti-pattern of hardcoded tenant lists
- [ ] Show maintenance issues
- [ ] Include refactoring to external config

### - [ ] 4.4.7.5 Missing error handling
Filename: `04_07_05_missing_error_handling.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create dynamic DAG without error handling
- [ ] Show cascade failures in DAG parsing
- [ ] Include robust error handling patterns

### - [ ] 4.4.7.6 Dynamic DAG without versioning
Filename: `04_07_06_dynamic_dag_without_versioning.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create dynamic DAG without version control
- [ ] Show debugging challenges
- [ ] Include versioning best practices

---

# 4.8 Dynamic Task Dependencies

### - [ ] 4.4.8.1 Dynamically generated dependency chains
Filename: `04_08_01_dynamically_generated_dependency_chains.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with runtime-determined dependency order
- [ ] Show using list comprehension for >> chains
- [ ] Include complex dependency graphs

### - [ ] 4.4.8.2 Conditional dependencies
Filename: `04_08_02_conditional_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dependencies based on configuration
- [ ] Show if/else for dependency definition
- [ ] Include skip patterns

### - [ ] 4.4.8.3 Cross-product dependencies
Filename: `04_08_03_crossproduct_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with all-to-all task dependencies
- [ ] Show cartesian product of task sets
- [ ] Include performance considerations

### - [ ] 4.4.8.4 Dynamic trigger rules
Filename: `04_08_04_dynamic_trigger_rules.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with runtime-determined trigger rules
- [ ] Show setting trigger_rule based on config
- [ ] Include one_success, all_done patterns

### - [ ] 4.4.8.5 Dynamic setup/teardown dependencies
Filename: `04_08_05_dynamic_setup_teardown_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dynamic setup/teardown tasks
- [ ] Show resource-based setup task generation
- [ ] Include cleanup task dependency patterns

### - [ ] 4.4.8.6 Cycle detection in dynamic dependencies
Filename: `04_08_06_cycle_detection_in_dynamic_dependencies.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating dependency cycle error
- [ ] Show how Airflow detects cycles
- [ ] Include debugging cyclic dependencies

---

# 4.9 Dynamic DAG Testing

### - [ ] 4.9.1 Testing DAG Generation Logic
Filename: `04_09_01_testing_dag_generation_logic.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Unit test factory functions
- [ ] Verify DAG count and IDs
- [ ] Test with various inputs
- [ ] Parameterized test patterns

### - [ ] 4.9.2 Testing Dynamic Task Creation
Filename: `04_09_02_testing_dynamic_task_creation.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Verify task IDs generated
- [ ] Test dependency structure
- [ ] Validate task parameters
- [ ] Edge case testing

### - [ ] 4.9.3 Testing expand() Behavior
Filename: `04_09_03_testing_expand_behavior.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test mapped task generation
- [ ] Verify map index assignment
- [ ] Test with XCom inputs
- [ ] Empty list handling

### - [ ] 4.9.4 Integration Testing Dynamic DAGs
Filename: `04_09_04_integration_testing_dynamic_dags.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Full execution tests
- [ ] Database state verification
- [ ] Cross-DAG dependency tests
- [ ] Performance testing

### - [ ] 4.9.5 Mocking Configuration Sources
Filename: `04_09_05_mocking_configuration_sources.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Mock database queries
- [ ] Mock API responses
- [ ] Mock file system
- [ ] Reproducible test configs

---

# 4.10 Dynamic DAG Real-World Examples

### - [ ] 4.10.1 Multi-Environment DAGs
Filename: `04_10_01_multi_environment_dags.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] Generate DAGs per environment
- [ ] Dev/staging/prod variants
- [ ] Environment-specific configs
- [ ] Deployment patterns

### - [ ] 4.10.2 Customer-Specific DAGs
Filename: `04_10_02_customer_specific_dags.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] One DAG per customer
- [ ] Customer configuration loading
- [ ] Isolated scheduling
- [ ] Customer-specific resources

### - [ ] 4.10.3 Schema-Driven DAGs
Filename: `04_10_03_schema_driven_dags.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

- [ ] DAG from database schema
- [ ] Table-per-task pattern
- [ ] Schema change handling
- [ ] Automatic DAG updates

### - [ ] 4.10.4 Event-Driven Dynamic DAGs
Filename: `04_10_04_event_driven_dynamic_dags.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] DAG triggered by events
- [ ] Dynamic task based on event
- [ ] Event payload processing
- [ ] Scalability patterns

### - [ ] 4.10.5 ML Experiment DAGs
Filename: `04_10_05_ml_experiment_dags.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

- [ ] DAG per experiment config
- [ ] Hyperparameter variants
- [ ] Result aggregation
- [ ] Experiment tracking

---
