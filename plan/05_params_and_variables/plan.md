# 05 Params And Variables

## Overview

This section covers all aspects of 05 params and variables.

---

# 5.1 DAG Params

### - [ ] 5.5.1.1 Basic Param usage
Filename: `05_01_01_basic_param_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with Param() in dag.params
- [ ] Show accessing params in tasks via {{ params.key }}
- [ ] Include default values

### - [ ] 5.5.1.2 Typed Params
Filename: `05_01_02_typed_params.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with typed Param (string, number, boolean)
- [ ] Show type validation on trigger
- [ ] Include type coercion behavior

### - [ ] 5.5.1.3 Param with enum
Filename: `05_01_03_param_with_enum.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with Param using enum for allowed values
- [ ] Show dropdown in UI trigger form
- [ ] Include validation errors

### - [ ] 5.5.1.4 Param with JSON schema
Filename: `05_01_04_param_with_json_schema.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with Param using JSON schema validation
- [ ] Show complex validation rules
- [ ] Include nested object params

### - [ ] 5.5.1.5 Required vs optional Params
Filename: `05_01_05_required_vs_optional_params.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with required and optional Params
- [ ] Show trigger failure without required params
- [ ] Include default value behavior

### - [ ] 5.5.1.6 Param in task logic
Filename: `05_01_06_param_in_task_logic.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG accessing params in Python task
- [ ] Show context['params'] usage
- [ ] Include conditional logic based on params

---

# 5.2 Variables

### - [ ] 5.5.2.1 Basic Variable usage
Filename: `05_02_01_basic_variable_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Variable.get() in task
- [ ] Show setting Variable via UI or CLI
- [ ] Include default value handling

### - [ ] 5.5.2.2 Variable with JSON
Filename: `05_02_02_variable_with_json.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Variable.get(deserialize_json=True)
- [ ] Show storing complex objects as JSON
- [ ] Include parsing errors

### - [ ] 5.5.2.3 Variable in templates
Filename: `05_02_03_variable_in_templates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using {{ var.value.my_var }} in templates
- [ ] Show Jinja2 Variable access
- [ ] Include var.json for JSON variables

### - [ ] 5.5.2.4 Variable not found errors
Filename: `05_02_04_variable_not_found_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG with Variable.get() for non-existent variable
- [ ] Show default_var parameter
- [ ] Include error handling

### - [ ] 5.5.2.5 Encrypted Variables
Filename: `05_02_05_encrypted_variables.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using encrypted Variables
- [ ] Show sensitive data storage
- [ ] Include Variable.set() with encryption

### - [ ] 5.5.2.6 Variable caching
Filename: `05_02_06_variable_caching.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating Variable caching behavior
- [ ] Show when Variables are fetched
- [ ] Include DAG parsing vs task execution

---

# 5.3 Connections

### - [ ] 5.5.3.1 Basic Connection usage
Filename: `05_03_01_basic_connection_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using BaseHook.get_connection()
- [ ] Show accessing connection parameters
- [ ] Include conn_id reference

### - [ ] 5.5.3.2 Connection in operators
Filename: `05_03_02_connection_in_operators.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with operators using connection_id parameter
- [ ] Show PostgresOperator, S3Operator with connections
- [ ] Include connection configuration

### - [ ] 5.5.3.3 Connection URI parsing
Filename: `05_03_03_connection_uri_parsing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG parsing connection URI components
- [ ] Show host, port, schema, login, password access
- [ ] Include extra JSON field

### - [ ] 5.5.3.4 Connection testing
Filename: `05_03_04_connection_testing.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with connection test task
- [ ] Show using hooks to verify connectivity
- [ ] Include retry logic for connection failures

### - [ ] 5.5.3.5 Connection not found errors
Filename: `05_03_05_connection_not_found_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

- [ ] Create DAG referencing non-existent connection
- [ ] Show error handling
- [ ] Include fallback connection logic

### - [ ] 5.5.3.6 Custom Connection types
Filename: `05_03_06_custom_connection_types.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with custom connection type
- [ ] Show defining custom connection class
- [ ] Include extra fields usage

---

# 5.4 Advanced Variable Patterns

### - [ ] 5.5.4.1 Variable as configuration
Filename: `05_04_01_variable_as_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Variable for environment config
- [ ] Show dev/prod configuration switching
- [ ] Include Variable naming conventions

### - [ ] 5.5.4.2 Variable updates during DAG run
Filename: `05_04_02_variable_updates_during_dag_run.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG that updates Variables
- [ ] Show Variable.set() in tasks
- [ ] Include concurrency considerations

### - [ ] 5.5.4.3 Variable versioning
Filename: `05_04_03_variable_versioning.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with Variable version tracking
- [ ] Show timestamp or version in Variable name
- [ ] Include migration between Variable versions

### - [ ] 5.5.4.4 Variable with XCom
Filename: `05_04_04_variable_with_xcom.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG choosing between Variable and XCom
- [ ] Show when to use each
- [ ] Include scope and persistence differences

### - [ ] 5.5.4.5 Variable bulk operations
Filename: `05_04_05_variable_bulk_operations.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG reading multiple Variables
- [ ] Show efficient bulk Variable retrieval
- [ ] Include caching strategies

### - [ ] 5.5.4.6 Variable inheritance patterns
Filename: `05_04_06_variable_inheritance_patterns.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with hierarchical Variables
- [ ] Show namespace conventions (team.project.var)
- [ ] Include default fallback chain

---

# 5.5 Secrets Backend

### - [ ] 5.5.5.1 Secrets backend configuration
Filename: `05_05_01_secrets_backend_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using secrets backend for Variables
- [ ] Show AWS Secrets Manager integration
- [ ] Include HashiCorp Vault example

### - [ ] 5.5.5.2 Connection from secrets backend
Filename: `05_05_02_connection_from_secrets_backend.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG loading Connections from secrets backend
- [ ] Show precedence order (backend vs metadata DB)
- [ ] Include connection_lookup_pattern

### - [ ] 5.5.5.3 Environment variables as secrets
Filename: `05_05_03_environment_variables_as_secrets.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using environment variables
- [ ] Show os.environ vs Variable.get()
- [ ] Include security considerations

### - [ ] 5.5.5.4 Custom secrets backend
Filename: `05_05_04_custom_secrets_backend.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with custom secrets backend implementation
- [ ] Show get_variable() and get_connection() methods
- [ ] Include priority configuration

### - [ ] 5.5.5.5 Secrets rotation
Filename: `05_05_05_secrets_rotation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG handling secret rotation
- [ ] Show retry logic for invalid credentials
- [ ] Include gradual rollout of new secrets

### - [ ] 5.5.5.6 Secrets caching and TTL
Filename: `05_05_06_secrets_caching_and_ttl.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating secrets caching
- [ ] Show cache invalidation
- [ ] Include TTL configuration

---

# 5.6 Runtime Configuration

### - [ ] 5.5.6.1 Accessing conf in templates
Filename: `05_06_01_accessing_conf_in_templates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using {{ conf }} in templates
- [ ] Show airflow.cfg values access
- [ ] Include core, logging sections

### - [ ] 5.5.6.2 dag.conf vs task.conf
Filename: `05_06_02_dagconf_vs_taskconf.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing DAG-level vs task-level config
- [ ] Show override patterns
- [ ] Include precedence rules

### - [ ] 5.5.6.3 Runtime parameters override
Filename: `05_06_03_runtime_parameters_override.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with runtime parameter override
- [ ] Show CLI trigger with --conf JSON
- [ ] Include params vs conf differences

### - [ ] 5.5.6.4 Configuration validation
Filename: `05_06_04_configuration_validation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG validating runtime configuration
- [ ] Show type checking and range validation
- [ ] Include failure on invalid config

### - [ ] 5.5.6.5 Feature flags with Variables
Filename: `05_06_05_feature_flags_with_variables.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Variables as feature flags
- [ ] Show conditional task execution
- [ ] Include gradual feature rollout

### - [ ] 5.5.6.6 Configuration best practices
Filename: `05_06_06_configuration_best_practices.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating config best practices
- [ ] Show separation of code and config
- [ ] Include security considerations

---

# 5.7 Context Variables

### - [ ] 5.5.7.1 Accessing execution context
Filename: `05_07_01_accessing_execution_context.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing all available context variables
- [ ] Show ds, ts, execution_date, dag_run
- [ ] Include context printing task

### - [ ] 5.5.7.2 Context in Jinja templates
Filename: `05_07_02_context_in_jinja_templates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using context in templates
- [ ] Show {{ ds }}, {{ ts }}, {{ macros }}
- [ ] Include custom context variables

### - [ ] 5.5.7.3 TaskInstance context
Filename: `05_07_03_taskinstance_context.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG accessing ti context
- [ ] Show ti.task_id, ti.dag_id, ti.xcom_pull/push
- [ ] Include ti.hostname, ti.state

### - [ ] 5.5.7.4 DagRun context
Filename: `05_07_04_dagrun_context.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG accessing dag_run context
- [ ] Show dag_run.conf, dag_run.run_id
- [ ] Include dag_run.external_trigger

### - [ ] 5.5.7.5 Custom context injection
Filename: `05_07_05_custom_context_injection.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG adding custom variables to context
- [ ] Show user_defined_macros, user_defined_filters
- [ ] Include complex custom functions

### - [ ] 5.5.7.6 Context in callbacks
Filename: `05_07_06_context_in_callbacks.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using context in callback functions
- [ ] Show on_success_callback with context
- [ ] Include logging from callbacks

---

# 5.8 Macros and Filters

### - [ ] 5.5.8.1 Built-in macros
Filename: `05_08_01_builtin_macros.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using macros.datetime, macros.timedelta
- [ ] Show macros.ds_add, macros.ds_format
- [ ] Include all available macros

### - [ ] 5.5.8.2 Custom macros
Filename: `05_08_02_custom_macros.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with user_defined_macros
- [ ] Show function definition and usage
- [ ] Include macros with parameters

### - [ ] 5.5.8.3 Jinja filters
Filename: `05_08_03_jinja_filters.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using Jinja filters in templates
- [ ] Show built-in filters (upper, lower, replace)
- [ ] Include chaining multiple filters

### - [ ] 5.5.8.4 Custom Jinja filters
Filename: `05_08_04_custom_jinja_filters.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] Create DAG with user_defined_filters
- [ ] Show filter function definition
- [ ] Include filter parameters

### - [ ] 5.5.8.5 Complex template expressions
Filename: `05_08_05_complex_template_expressions.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Create DAG with complex Jinja logic
- [ ] Show loops, conditionals in templates
- [ ] Include multi-line template strings

### - [ ] 5.5.8.6 Template debugging
Filename: `05_08_06_template_debugging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with template rendering issues
- [ ] Show debugging undefined variables
- [ ] Include template_undefined configuration

---

# 5.9 Data Interval and Logical Date

### - [ ] 5.5.9.1 data_interval_start and data_interval_end
Filename: `05_09_01_data_interval_start_and_data_interval_end.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using data_interval_start/end
- [ ] Show difference from execution_date
- [ ] Include schedule-based intervals

### - [ ] 5.5.9.2 logical_date usage
Filename: `05_09_02_logical_date_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using logical_date (Airflow 2.2+)
- [ ] Show replacement for execution_date
- [ ] Include backward compatibility

### - [ ] 5.5.9.3 Data interval in manual runs
Filename: `05_09_03_data_interval_in_manual_runs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG showing data interval in manual triggers
- [ ] Show --logical-date CLI parameter
- [ ] Include UI trigger with logical date

### - [ ] 5.5.9.4 Data interval with time zones
Filename: `05_09_04_data_interval_with_time_zones.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with timezone-aware data intervals
- [ ] Show UTC vs local time
- [ ] Include timezone conversion

### - [ ] 5.5.9.5 Data interval in templates
Filename: `05_09_05_data_interval_in_templates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG using {{ data_interval_start }} in templates
- [ ] Show formatting and manipulation
- [ ] Include macros for interval math

### - [ ] 5.5.9.6 Data interval best practices
Filename: `05_09_06_data_interval_best_practices.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG demonstrating interval best practices
- [ ] Show avoiding execution_date
- [ ] Include migration guide

---

# 5.10 Config Anti-patterns

### - [ ] 5.5.10.1 Hardcoded values in DAG
Filename: `05_10_01_hardcoded_values_in_dag.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with hardcoded config values
- [ ] Show maintenance issues
- [ ] Include refactoring to Variables

### - [ ] 5.5.10.2 Variable usage in DAG file top-level
Filename: `05_10_02_variable_usage_in_dag_file_toplevel.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with Variable.get() at module level
- [ ] Show parsing delays and issues
- [ ] Include proper task-level Variable access

### - [ ] 5.5.10.3 Excessive Variable usage
Filename: `05_10_03_excessive_variable_usage.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with too many Variable lookups
- [ ] Show performance impact
- [ ] Include batching and caching strategies

### - [ ] 5.5.10.4 Unencrypted sensitive data
Filename: `05_10_04_unencrypted_sensitive_data.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with sensitive data in plain Variables
- [ ] Show security risks
- [ ] Include encryption best practices

### - [ ] 5.5.10.5 Missing default values
Filename: `05_10_05_missing_default_values.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG without default values for Variables
- [ ] Show failure when Variable missing
- [ ] Include robust error handling

### - [ ] 5.5.10.6 Overusing params for config
Filename: `05_10_06_overusing_params_for_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG overusing Params vs Variables
- [ ] Show when to use each
- [ ] Include design patterns

---

# 5.11 Configuration Management

### - [ ] 5.5.11.1 Environment-specific configuration
Filename: `05_11_01_environmentspecific_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with dev/staging/prod configs
- [ ] Show environment detection
- [ ] Include Variable or Connection per environment

### - [ ] 5.5.11.2 Configuration as code
Filename: `05_11_02_configuration_as_code.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG with configuration in version control
- [ ] Show loading config from files
- [ ] Include config deployment strategies

### - [ ] 5.5.11.3 Configuration validation pipeline
Filename: `05_11_03_configuration_validation_pipeline.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG validating configuration
- [ ] Show schema validation
- [ ] Include automated testing of configs

### - [ ] 5.5.11.4 Configuration documentation
Filename: `05_11_04_configuration_documentation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create well-documented DAG configuration
- [ ] Show inline documentation
- [ ] Include README for Variables/Connections

### - [ ] 5.5.11.5 Configuration migration
Filename: `05_11_05_configuration_migration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG handling config changes
- [ ] Show backward compatibility
- [ ] Include deprecation warnings

### - [ ] 5.5.11.6 Configuration monitoring
Filename: `05_11_06_configuration_monitoring.py` | Tags: `['reference', 'core', 'beginner', 'success']`

- [ ] Create DAG monitoring configuration usage
- [ ] Show alerting on config issues
- [ ] Include config drift detection

---
