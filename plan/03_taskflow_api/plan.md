# 03 Taskflow Api

## Overview

This section covers all aspects of 03 taskflow api.

---

# 3.1 Basic TaskFlow Patterns

### - [ ] 3.3.1.1 Simple @task decorator
Filename: `03_01_01_simple_task_decorator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating basic @task decorator usage
- [ ] Show function-based task definition with return values
- [ ] Include XCom passing between @task functions

### - [ ] 3.3.1.2 @task with type hints
Filename: `03_01_02_task_with_type_hints.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task functions using Python type hints
- [ ] Show automatic XCom serialization with typed returns
- [ ] Include multiple data types (dict, list, dataclass)

### - [ ] 3.3.1.3 @task with multiple outputs
Filename: `03_01_03_task_with_multiple_outputs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing @task returning multiple values
- [ ] Use tuple unpacking for multiple outputs
- [ ] Show downstream tasks consuming specific outputs

### - [ ] 3.3.1.4 @task with kwargs
Filename: `03_01_04_task_with_kwargs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating @task with keyword arguments
- [ ] Show passing configuration via kwargs
- [ ] Include default parameter values

### - [ ] 3.3.1.5 @task.virtualenv
Filename: `03_01_05_taskvirtualenv.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task.virtualenv for isolated Python env
- [ ] Show requirements specification
- [ ] Include package installation and usage

### - [ ] 3.3.1.6 @task.external_python
Filename: `03_01_06_taskexternal_python.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task.external_python with specific Python path
- [ ] Show using different Python version/environment
- [ ] Include system_site_packages usage

---

# 3.2 TaskFlow Data Passing

### - [ ] 3.3.2.1 Implicit XCom passing
Filename: `03_02_01_implicit_xcom_passing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing implicit XCom between @task functions
- [ ] Show chaining multiple @task calls
- [ ] Include data transformation pipeline

### - [ ] 3.3.2.2 Explicit XCom with ti.xcom_pull
Filename: `03_02_02_explicit_xcom_with_tixcom_pull.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG mixing @task and traditional operators
- [ ] Show explicit XCom pulling in @task
- [ ] Include ti.xcom_push usage

### - [ ] 3.3.2.3 Multiple XCom values
Filename: `03_02_03_multiple_xcom_values.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG passing multiple XCom values between tasks
- [ ] Show dictionary-based data passing
- [ ] Include nested data structures

### - [ ] 3.3.2.4 Large data handling
Filename: `03_02_04_large_data_handling.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating XCom size limitations
- [ ] Show failure when exceeding XCom size
- [ ] Include workaround using external storage reference

### - [ ] 3.3.2.5 Custom XCom backend
Filename: `03_02_05_custom_xcom_backend.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG using custom XCom backend (S3/GCS)
- [ ] Show configuration for custom backend
- [ ] Include serialization/deserialization

### - [ ] 3.3.2.6 XCom with complex types
Filename: `03_02_06_xcom_with_complex_types.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Create DAG passing pandas DataFrames, numpy arrays
- [ ] Show custom serialization for complex objects
- [ ] Include error handling for non-serializable types

---

# 3.3 TaskFlow Decorators

### - [ ] 3.3.3.1 @task.docker
Filename: `03_03_01_taskdocker.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task.docker decorator
- [ ] Show Docker image specification
- [ ] Include volume mounting and environment variables

### - [ ] 3.3.3.2 @task.kubernetes
Filename: `03_03_02_taskkubernetes.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task.kubernetes decorator
- [ ] Show K8s pod specification
- [ ] Include resource requests/limits

### - [ ] 3.3.3.3 @task.bash
Filename: `03_03_03_taskbash.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task.bash decorator (if available)
- [ ] Show bash command execution in TaskFlow
- [ ] Include environment variable passing

### - [ ] 3.3.3.4 @task.python_virtualenv with system_site_packages
Filename: `03_03_04_taskpython_virtualenv_with_system_site_packages.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using system_site_packages=True
- [ ] Show access to globally installed packages
- [ ] Include mixed requirements

### - [ ] 3.3.3.5 @task with retry decorator
Filename: `03_03_05_task_with_retry_decorator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task.retry or custom retry logic
- [ ] Show exponential backoff
- [ ] Include retry-specific error handling

### - [ ] 3.3.3.6 @task with sensor pattern
Filename: `03_03_06_task_with_sensor_pattern.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task to implement sensor logic
- [ ] Show polling with sleep
- [ ] Include timeout handling

---

# 3.4 TaskFlow with Traditional Operators

### - [ ] 3.3.4.1 Mixed TaskFlow and traditional operators
Filename: `03_04_01_mixed_taskflow_and_traditional_operators.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG mixing @task and BashOperator/PythonOperator
- [ ] Show dependency setting between different task types
- [ ] Include XCom passing between both styles

### - [ ] 3.3.4.2 TaskFlow wrapping existing operators
Filename: `03_04_02_taskflow_wrapping_existing_operators.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task to wrap operator logic
- [ ] Show converting traditional operator to TaskFlow
- [ ] Include parameter passing

### - [ ] 3.3.4.3 Traditional operator consuming TaskFlow output
Filename: `03_04_03_traditional_operator_consuming_taskflow_output.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with operator using output from @task
- [ ] Show XCom template usage in operators
- [ ] Include Jinja templating with TaskFlow data

### - [ ] 3.3.4.4 TaskFlow consuming traditional operator output
Filename: `03_04_04_taskflow_consuming_traditional_operator_output.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task pulling XCom from operators
- [ ] Show ti.xcom_pull with task_ids
- [ ] Include error handling for missing XCom

### - [ ] 3.3.4.5 Migration from traditional to TaskFlow
Filename: `03_04_05_migration_from_traditional_to_taskflow.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create two DAGs: same logic in traditional vs TaskFlow
- [ ] Show before/after comparison
- [ ] Include benefits and limitations notes

### - [ ] 3.3.4.6 When NOT to use TaskFlow
Filename: `03_04_06_when_not_to_use_taskflow.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing cases where traditional operators better
- [ ] Show sensor usage, external system operators
- [ ] Include anti-patterns with TaskFlow

---

# 3.5 TaskFlow Advanced Patterns

### - [ ] 3.3.5.1 TaskFlow with dynamic task generation
Filename: `03_05_01_taskflow_with_dynamic_task_generation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task with dynamic task mapping
- [ ] Show expand() with @task functions
- [ ] Include partial() usage

### - [ ] 3.3.5.2 TaskFlow with task groups
Filename: `03_05_02_taskflow_with_task_groups.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG combining @task with TaskGroup
- [ ] Show organizing @task functions in groups
- [ ] Include nested task groups

### - [ ] 3.3.5.3 TaskFlow with branching
Filename: `03_05_03_taskflow_with_branching.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task for branch logic
- [ ] Show @task.branch decorator usage
- [ ] Include conditional execution

### - [ ] 3.3.5.4 TaskFlow with setup/teardown
Filename: `03_05_04_taskflow_with_setup_teardown.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using @task for setup/teardown
- [ ] Show resource allocation and cleanup
- [ ] Include error handling in teardown

### - [ ] 3.3.5.5 TaskFlow with callbacks
Filename: `03_05_05_taskflow_with_callbacks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with @task using on_success/on_failure callbacks
- [ ] Show callback function definition
- [ ] Include context access in callbacks

### - [ ] 3.3.5.6 TaskFlow context access
Filename: `03_05_06_taskflow_context_access.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing all context variables in @task
- [ ] Show **context usage vs specific parameters
- [ ] Include ti, dag, dag_run, execution_date access

---

# 3.6 TaskFlow Error Handling and Best Practices

### - [ ] 3.3.6.1 Exception handling in @task
Filename: `03_06_01_exception_handling_in_task.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with try/except in @task functions
- [ ] Show raising AirflowException vs generic exceptions
- [ ] Include logging best practices

### - [ ] 3.3.6.2 @task return value validation
Filename: `03_06_02_task_return_value_validation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG validating @task return values
- [ ] Show type checking and data validation
- [ ] Include failure on invalid data

### - [ ] 3.3.6.3 @task with timeout
Filename: `03_06_03_task_with_timeout.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using execution_timeout with @task
- [ ] Show timeout behavior
- [ ] Include cleanup on timeout

### - [ ] 3.3.6.4 TaskFlow testing patterns
Filename: `03_06_04_taskflow_testing_patterns.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with easily testable @task functions
- [ ] Show unit testing @task functions
- [ ] Include mocking context and XCom

### - [ ] 3.3.6.5 TaskFlow documentation
Filename: `03_06_05_taskflow_documentation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create well-documented DAG with @task docstrings
- [ ] Show function documentation best practices
- [ ] Include parameter and return type documentation

### - [ ] 3.3.6.6 TaskFlow performance considerations
Filename: `03_06_06_taskflow_performance_considerations.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing performance implications
- [ ] Show when to use vs avoid TaskFlow
- [ ] Include memory and serialization overhead notes

---
