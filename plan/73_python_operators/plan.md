# 73 Python Operators

## Overview
Deep dive into PythonOperator and related Python-based operators including @task decorator, callables, and execution patterns.

---

# 73.1 PythonOperator Basics

### - [ ] 73.1.1 Basic PythonOperator
Filename: `73_01_01_basic.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] python_callable parameter
- [ ] Simple function execution
- [ ] Return values
- [ ] Task instantiation

### - [ ] 73.1.2 Passing Arguments
Filename: `73_01_02_arguments.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] op_args parameter
- [ ] op_kwargs parameter
- [ ] Mixed arguments
- [ ] Argument ordering

### - [ ] 73.1.3 Templates in PythonOperator
Filename: `73_01_03_templates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] templates_dict parameter
- [ ] Jinja templating
- [ ] Template fields
- [ ] Render behavior

### - [ ] 73.1.4 Accessing Context
Filename: `73_01_04_context.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] **kwargs context
- [ ] get_current_context()
- [ ] Context variables
- [ ] Task instance access

### - [ ] 73.1.5 Return Value Handling
Filename: `73_01_05_return_values.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Auto XCom push
- [ ] do_xcom_push parameter
- [ ] Return serialization
- [ ] Large return handling

---

# 73.2 TaskFlow API (@task)

### - [ ] 73.2.1 @task Decorator Basics
Filename: `73_02_01_task_decorator.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Basic decoration
- [ ] Function definition
- [ ] Automatic XCom
- [ ] Task parameters

### - [ ] 73.2.2 @task with Parameters
Filename: `73_02_02_task_params.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Decorator arguments
- [ ] retries, timeout
- [ ] pool, queue
- [ ] Multiple tasks

### - [ ] 73.2.3 @task Return Types
Filename: `73_02_03_return_types.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Simple types
- [ ] Dict returns
- [ ] Multiple outputs
- [ ] Custom serialization

### - [ ] 73.2.4 @task.branch
Filename: `73_02_04_task_branch.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Branch decoration
- [ ] Return task IDs
- [ ] Skip behavior
- [ ] Multiple branches

### - [ ] 73.2.5 @task.short_circuit
Filename: `73_02_05_short_circuit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Short circuit decoration
- [ ] Boolean return
- [ ] Downstream skip
- [ ] Use cases

---

# 73.3 Advanced Python Patterns

### - [ ] 73.3.1 PythonVirtualenvOperator
Filename: `73_03_01_virtualenv.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Isolated environment
- [ ] requirements parameter
- [ ] python_version
- [ ] system_site_packages

### - [ ] 73.3.2 ExternalPythonOperator
Filename: `73_03_02_external_python.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Pre-existing venv
- [ ] python parameter
- [ ] Environment isolation
- [ ] Performance benefits

### - [ ] 73.3.3 @task.virtualenv
Filename: `73_03_03_task_virtualenv.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] TaskFlow virtualenv
- [ ] Decorator parameters
- [ ] Dependencies
- [ ] Caching

### - [ ] 73.3.4 BranchPythonOperator
Filename: `73_03_04_branch_python.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Branch decision logic
- [ ] Return task IDs
- [ ] Multiple branches
- [ ] Default branch

### - [ ] 73.3.5 ShortCircuitOperator
Filename: `73_03_05_short_circuit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Pipeline control
- [ ] Condition checking
- [ ] Downstream behavior
- [ ] ignore_downstream_trigger_rules

---

# 73.4 Callable Patterns

### - [ ] 73.4.1 Class-Based Callables
Filename: `73_04_01_class_callable.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] __call__ method
- [ ] State management
- [ ] Configuration
- [ ] Reusability

### - [ ] 73.4.2 Factory Functions
Filename: `73_04_02_factory.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Function factories
- [ ] Parameterized tasks
- [ ] Closure patterns
- [ ] Configuration injection

### - [ ] 73.4.3 Lambda Functions
Filename: `73_04_03_lambda.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Inline lambdas
- [ ] Simple operations
- [ ] Limitations
- [ ] Best practices

### - [ ] 73.4.4 Partial Functions
Filename: `73_04_04_partial.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] functools.partial
- [ ] Pre-bound arguments
- [ ] Task variants
- [ ] Use cases

### - [ ] 73.4.5 Module Functions
Filename: `73_04_05_module.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Import from modules
- [ ] Package organization
- [ ] Testing benefits
- [ ] Code reuse

---

# 73.5 Execution and Error Handling

### - [ ] 73.5.1 Exception Handling
Filename: `73_05_01_exceptions.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Try/except patterns
- [ ] AirflowException
- [ ] AirflowSkipException
- [ ] AirflowFailException

### - [ ] 73.5.2 Logging in Python Tasks
Filename: `73_05_02_logging.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Task logging
- [ ] Log levels
- [ ] Structured logging
- [ ] Log aggregation

### - [ ] 73.5.3 Resource Management
Filename: `73_05_03_resources.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Context managers
- [ ] Connection handling
- [ ] Cleanup patterns
- [ ] Memory management

### - [ ] 73.5.4 Async Python Tasks
Filename: `73_05_04_async.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Async callables
- [ ] Event loop handling
- [ ] Concurrent operations
- [ ] Limitations

### - [ ] 73.5.5 Python Task Testing
Filename: `73_05_05_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Unit test callables
- [ ] Mock context
- [ ] Isolation testing
- [ ] Integration tests

---

# 73.6 Python Operator Anti-Patterns

### - [ ] 73.6.1 Heavy DAG File Processing
Filename: `73_06_01_heavy_dag_file.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Import-time execution
- [ ] Parsing performance
- [ ] Scheduler impact
- [ ] Lazy loading patterns

### - [ ] 73.6.2 Global State in Callables
Filename: `73_06_02_global_state.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Shared state issues
- [ ] Worker isolation
- [ ] Race conditions
- [ ] Stateless design

### - [ ] 73.6.3 Oversized Return Values
Filename: `73_06_03_oversized_returns.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] XCom size limits
- [ ] Database bloat
- [ ] Performance impact
- [ ] Alternative patterns

### - [ ] 73.6.4 Blocking Operations
Filename: `73_06_04_blocking.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Long-running code
- [ ] Worker starvation
- [ ] Timeout issues
- [ ] Async patterns

### - [ ] 73.6.5 Hard-Coded Configuration
Filename: `73_06_05_hardcoded_config.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Embedded secrets
- [ ] Environment inflexibility
- [ ] Testing difficulties
- [ ] Configuration patterns

---

# 73.7 Python Operator Performance

### - [ ] 73.7.1 Callable Optimization
Filename: `73_07_01_callable_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Code profiling
- [ ] Memory optimization
- [ ] CPU efficiency
- [ ] Best practices

### - [ ] 73.7.2 Import Optimization
Filename: `73_07_02_import_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Lazy imports
- [ ] Import caching
- [ ] Module organization
- [ ] Startup time

### - [ ] 73.7.3 Virtualenv Performance
Filename: `73_07_03_virtualenv_perf.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Environment creation
- [ ] Caching strategies
- [ ] Pre-built environments
- [ ] ExternalPython benefits

### - [ ] 73.7.4 Data Passing Performance
Filename: `73_07_04_data_passing.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] XCom efficiency
- [ ] Serialization costs
- [ ] Alternative storage
- [ ] Optimization

### - [ ] 73.7.5 Parallel Execution
Filename: `73_07_05_parallel.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Multi-threading
- [ ] Multi-processing
- [ ] Async execution
- [ ] Worker utilization

---

# 73.8 Python Operator Debugging

### - [ ] 73.8.1 Callable Debugging
Filename: `73_08_01_callable_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Print debugging
- [ ] Logging setup
- [ ] Remote debugging
- [ ] IDE integration

### - [ ] 73.8.2 Context Debugging
Filename: `73_08_02_context_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Context inspection
- [ ] Variable access
- [ ] Template debugging
- [ ] XCom debugging

### - [ ] 73.8.3 Exception Debugging
Filename: `73_08_03_exception_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Stack trace analysis
- [ ] Exception chaining
- [ ] Error reproduction
- [ ] Fix verification

### - [ ] 73.8.4 Virtualenv Debugging
Filename: `73_08_04_virtualenv_debug.py` | Tags: `['reference', 'debugging', 'intermediate', 'success']`
- [ ] Environment issues
- [ ] Dependency conflicts
- [ ] Path problems
- [ ] Isolation verification

### - [ ] 73.8.5 Performance Debugging
Filename: `73_08_05_perf_debug.py` | Tags: `['reference', 'debugging', 'advanced', 'success']`
- [ ] Profiling callables
- [ ] Memory leaks
- [ ] CPU bottlenecks
- [ ] Resource monitoring

---

# 73.9 Real-World Python Operator Examples

### - [ ] 73.9.1 Data Transformation Task
Filename: `73_09_01_data_transform.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] Pandas processing
- [ ] Error handling
- [ ] Result passing
- [ ] Performance tips

### - [ ] 73.9.2 API Integration Task
Filename: `73_09_02_api_integration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] HTTP requests
- [ ] Authentication
- [ ] Error handling
- [ ] Pagination

### - [ ] 73.9.3 ML Model Task
Filename: `73_09_03_ml_model.py` | Tags: `['reference', 'example', 'advanced', 'success']`
- [ ] Model loading
- [ ] Prediction execution
- [ ] Result handling
- [ ] Resource management

### - [ ] 73.9.4 File Processing Task
Filename: `73_09_04_file_processing.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] File reading/writing
- [ ] Stream processing
- [ ] Error handling
- [ ] Cleanup patterns

### - [ ] 73.9.5 Database Operation Task
Filename: `73_09_05_database_operation.py` | Tags: `['reference', 'example', 'intermediate', 'success']`
- [ ] Connection management
- [ ] Query execution
- [ ] Transaction handling
- [ ] Result processing

---

# 73.10 Python Operator Best Practices

### - [ ] 73.10.1 Callable Design
Filename: `73_10_01_callable_design.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`
- [ ] Single responsibility
- [ ] Testability
- [ ] Error handling
- [ ] Documentation

### - [ ] 73.10.2 Code Organization
Filename: `73_10_02_code_organization.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Module structure
- [ ] Shared utilities
- [ ] Import patterns
- [ ] Versioning

### - [ ] 73.10.3 Error Handling Standards
Filename: `73_10_03_error_handling.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Exception handling
- [ ] Error classification
- [ ] Retry decisions
- [ ] Logging patterns

### - [ ] 73.10.4 Testing Standards
Filename: `73_10_04_testing_standards.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`
- [ ] Unit testing
- [ ] Integration testing
- [ ] Mock strategies
- [ ] Coverage requirements

### - [ ] 73.10.5 Documentation Standards
Filename: `73_10_05_documentation.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`
- [ ] Docstrings
- [ ] Type hints
- [ ] Example usage
- [ ] Troubleshooting
