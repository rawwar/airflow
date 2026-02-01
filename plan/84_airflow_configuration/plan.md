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

# 84 Airflow Configuration

## Overview

Airflow configuration controls all aspects of the platform's behavior. This section provides a deep dive into airflow.cfg sections, configuration options, performance tuning, and configuration management best practices for Airflow 3.x.

## Research & Background

### Key Concepts
- **airflow.cfg**: Main configuration file
- **Configuration Sections**: Grouped settings (core, scheduler, etc.)
- **Default Values**: Built-in defaults
- **Configuration Sources**: File, env vars, secrets
- **Dynamic Configuration**: Runtime config changes

### Airflow 3.x Features
- Streamlined configuration
- Better defaults
- Improved documentation
- Configuration validation
- Secret config values

### Prerequisites
- Airflow 3.x installed
- Admin access to Airflow
- Understanding of Airflow architecture

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Understand all configuration sections
2. Tune performance settings
3. Configure security options
4. Manage configuration across environments
5. Troubleshoot configuration issues

---

# 84.1 Configuration File Basics

## Overview
Understanding airflow.cfg structure and management.

## Tasks

### - [ ] 84.1.1 Configuration File Location
Filename: `84_01_01_config_location.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Find and understand config file

- [ ] Default location (AIRFLOW_HOME/airflow.cfg)
- [ ] AIRFLOW_CONFIG override
- [ ] Generated on first run
- [ ] Template comments

**Expected Behavior**: Config file located

---

### - [ ] 84.1.2 Configuration Sections Overview
Filename: `84_01_02_sections_overview.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand config sections

- [ ] [core] section
- [ ] [database] section
- [ ] [scheduler] section
- [ ] [webserver] section

**Expected Behavior**: Sections understood

---

### - [ ] 84.1.3 Viewing Effective Configuration
Filename: `84_01_03_viewing_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: See current configuration

- [ ] airflow config list command
- [ ] airflow config get-value
- [ ] Filter by section
- [ ] Show non-defaults

**Expected Behavior**: Config visible

---

### - [ ] 84.1.4 Configuration Validation
Filename: `84_01_04_config_validation.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Validate configuration

- [ ] Built-in validation
- [ ] Deprecated settings warnings
- [ ] Type checking
- [ ] Required settings

**Expected Behavior**: Invalid config detected

---

### - [ ] 84.1.5 Configuration Documentation
Filename: `84_01_05_config_docs.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Find config documentation

- [ ] Official docs reference
- [ ] In-file comments
- [ ] airflow config list --defaults
- [ ] Change log for versions

**Expected Behavior**: Documentation accessible

---

# 84.2 Core and Scheduler Settings

## Overview
Essential operational configuration.

## Tasks

### - [ ] 84.2.1 Core Section Deep Dive
Filename: `84_02_01_core_section.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure core settings

- [ ] executor selection
- [ ] parallelism
- [ ] dag_concurrency
- [ ] max_active_tasks_per_dag

**Expected Behavior**: Core settings tuned

---

### - [ ] 84.2.2 Scheduler Section Settings
Filename: `84_02_02_scheduler_section.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure scheduler behavior

- [ ] scheduler_heartbeat_sec
- [ ] min_file_process_interval
- [ ] dag_dir_list_interval
- [ ] parsing_processes

**Expected Behavior**: Scheduler optimized

---

### - [ ] 84.2.3 Database Section Settings
Filename: `84_02_03_database_section.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure database connection

- [ ] sql_alchemy_conn
- [ ] sql_alchemy_pool_size
- [ ] sql_alchemy_pool_recycle
- [ ] Connection pooling

**Expected Behavior**: Database configured

---

### - [ ] 84.2.4 Concurrency Settings
Filename: `84_02_04_concurrency_settings.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Tune concurrent execution

- [ ] parallelism (global)
- [ ] max_active_tasks_per_dag
- [ ] max_active_runs_per_dag
- [ ] Worker concurrency

**Expected Behavior**: Concurrency balanced

---

### - [ ] 84.2.5 DAG Discovery Settings
Filename: `84_02_05_dag_discovery.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure DAG loading

- [ ] dags_folder
- [ ] plugins_folder
- [ ] dag_discovery_safe_mode
- [ ] donot_pickle

**Expected Behavior**: DAG discovery configured

---

# 84.3 Webserver and Security

## Overview
UI and security configuration.

## Tasks

### - [ ] 84.3.1 Webserver Section Settings
Filename: `84_03_01_webserver_section.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure web UI

- [ ] base_url
- [ ] web_server_port
- [ ] web_server_host
- [ ] workers and threads

**Expected Behavior**: Webserver configured

---

### - [ ] 84.3.2 Authentication Configuration
Filename: `84_03_02_authentication.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure authentication

- [ ] auth_backend
- [ ] FAB authentication
- [ ] OAuth/OIDC settings
- [ ] Session management

**Expected Behavior**: Auth configured

---

### - [ ] 84.3.3 RBAC Configuration
Filename: `84_03_03_rbac_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Role-based access control

- [ ] rbac enabled
- [ ] Default roles
- [ ] Custom roles
- [ ] Permission sync

**Expected Behavior**: RBAC configured

---

### - [ ] 84.3.4 API Configuration
Filename: `84_03_04_api_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure REST API

- [ ] auth_backends for API
- [ ] enable_experimental_api
- [ ] maximum_page_limit
- [ ] CORS settings

**Expected Behavior**: API configured

---

### - [ ] 84.3.5 Security Best Practices
Filename: `84_03_05_security_practices.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Secure Airflow deployment

- [ ] secret_key configuration
- [ ] Fernet key for encryption
- [ ] HTTPS configuration
- [ ] Security headers

**Expected Behavior**: Security hardened

---

# 84.4 Logging and Monitoring

## Overview
Observability configuration.

## Tasks

### - [ ] 84.4.1 Logging Section Settings
Filename: `84_04_01_logging_section.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure logging

- [ ] base_log_folder
- [ ] logging_level
- [ ] fab_logging_level
- [ ] colored_console_log

**Expected Behavior**: Logging configured

---

### - [ ] 84.4.2 Remote Logging
Filename: `84_04_02_remote_logging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure cloud log storage

- [ ] remote_logging = True
- [ ] remote_base_log_folder
- [ ] S3/GCS/Azure paths
- [ ] Connection for logging

**Expected Behavior**: Remote logging works

---

### - [ ] 84.4.3 Metrics Configuration
Filename: `84_04_03_metrics_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure metrics export

- [ ] statsd settings
- [ ] metrics_enabled
- [ ] OpenTelemetry config
- [ ] Prometheus endpoint

**Expected Behavior**: Metrics exported

---

### - [ ] 84.4.4 Task Log Configuration
Filename: `84_04_04_task_logs.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure task logging

- [ ] log_format
- [ ] log_processor_filename_template
- [ ] task_log_reader
- [ ] Log retention

**Expected Behavior**: Task logs configured

---

### - [ ] 84.4.5 Audit Logging
Filename: `84_04_05_audit_logging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track user actions

- [ ] audit_log settings
- [ ] Event tracking
- [ ] Log destination
- [ ] Compliance requirements

**Expected Behavior**: Audit logs captured

---

# 84.5 Advanced Configuration

## Overview
Advanced configuration scenarios.

## Tasks

### - [ ] 84.5.1 Secrets Backend Configuration
Filename: `84_05_01_secrets_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure secrets backend

- [ ] [secrets] section
- [ ] backend class
- [ ] backend_kwargs
- [ ] Multiple backends

**Expected Behavior**: Secrets backend configured

---

### - [ ] 84.5.2 Email Configuration
Filename: `84_05_02_email_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure email settings

- [ ] [smtp] section
- [ ] smtp_host and port
- [ ] Authentication
- [ ] TLS/SSL settings

**Expected Behavior**: Email configured

---

### - [ ] 84.5.3 Celery Configuration
Filename: `84_05_03_celery_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure Celery executor

- [ ] [celery] section
- [ ] broker_url
- [ ] result_backend
- [ ] Worker settings

**Expected Behavior**: Celery configured

---

### - [ ] 84.5.4 Kubernetes Configuration
Filename: `84_05_04_kubernetes_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure K8s executor

- [ ] [kubernetes_executor] section
- [ ] namespace
- [ ] worker_container_repository
- [ ] Pod templates

**Expected Behavior**: K8s executor configured

---

### - [ ] 84.5.5 Configuration Management Strategies
Filename: `84_05_05_config_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Manage config across environments

- [ ] Base config with overrides
- [ ] Environment-specific values
- [ ] Version control for config
- [ ] Config as code

**Expected Behavior**: Config managed properly

---

# 84.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding configuration pitfalls.

## Tasks

### - [ ] 84.6.1 Default Configuration in Production
Filename: `84_06_01_default_production.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Customize for production

- [ ] Security defaults insufficient
- [ ] Performance not tuned
- [ ] Missing critical settings
- [ ] Production checklist

**Expected Behavior**: Production customized

---

### - [ ] 84.6.2 Over-Configured Parallelism
Filename: `84_06_02_over_configured_parallelism.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Balance parallelism settings

- [ ] Too many parallel tasks
- [ ] Resource exhaustion
- [ ] Database overload
- [ ] Proper sizing

**Expected Behavior**: Parallelism balanced

---

### - [ ] 84.6.3 Missing Security Configuration
Filename: `84_06_03_missing_security.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Secure all deployments

- [ ] Default secret key
- [ ] No authentication
- [ ] Missing HTTPS
- [ ] Security hardening

**Expected Behavior**: Security configured

---

### - [ ] 84.6.4 Unvalidated Configuration Changes
Filename: `84_06_04_unvalidated_changes.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Validate before deployment

- [ ] Untested changes
- [ ] Production impact
- [ ] Rollback difficulty
- [ ] Change validation

**Expected Behavior**: Changes validated

---

### - [ ] 84.6.5 Configuration Sprawl
Filename: `84_06_05_config_sprawl.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Manage configuration complexity

- [ ] Too many overrides
- [ ] Conflicting settings
- [ ] Hard to maintain
- [ ] Simplification strategies

**Expected Behavior**: Config manageable

---

# 84.7 Testing Configuration

## Overview
Testing Airflow configuration changes.

## Tasks

### - [ ] 84.7.1 Configuration Validation Testing
Filename: `84_07_01_validation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate configurations

- [ ] Schema validation
- [ ] Type checking
- [ ] Required settings
- [ ] Deprecated detection

**Expected Behavior**: Config validated

---

### - [ ] 84.7.2 Performance Impact Testing
Filename: `84_07_02_performance_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test config performance

- [ ] Benchmark baselines
- [ ] Change comparison
- [ ] Load testing
- [ ] Regression detection

**Expected Behavior**: Performance tested

---

### - [ ] 84.7.3 Configuration Diff Analysis
Filename: `84_07_03_diff_analysis.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Compare configurations

- [ ] Env comparison
- [ ] Version comparison
- [ ] Change detection
- [ ] Impact analysis

**Expected Behavior**: Diffs analyzed

---

### - [ ] 84.7.4 Staging Environment Testing
Filename: `84_07_04_staging_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test in staging

- [ ] Production-like staging
- [ ] Config verification
- [ ] Integration tests
- [ ] Approval gates

**Expected Behavior**: Staging tested

---

### - [ ] 84.7.5 Rollback Testing
Filename: `84_07_05_rollback_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test config rollbacks

- [ ] Version rollback
- [ ] State consistency
- [ ] Data integrity
- [ ] Quick recovery

**Expected Behavior**: Rollbacks work

---

# 84.8 Performance Tuning

## Overview
Tuning Airflow for optimal performance.

## Tasks

### - [ ] 84.8.1 Scheduler Performance Tuning
Filename: `84_08_01_scheduler_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize scheduler

- [ ] Parsing interval tuning
- [ ] Scheduler heartbeat
- [ ] Max processes
- [ ] Database optimization

**Expected Behavior**: Scheduler optimized

---

### - [ ] 84.8.2 Database Connection Tuning
Filename: `84_08_02_database_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize database settings

- [ ] Pool size optimization
- [ ] Connection timeout
- [ ] Query optimization
- [ ] Connection recycling

**Expected Behavior**: Database efficient

---

### - [ ] 84.8.3 Worker Configuration Tuning
Filename: `84_08_03_worker_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize workers

- [ ] Concurrency settings
- [ ] Memory allocation
- [ ] Task timeouts
- [ ] Queue configuration

**Expected Behavior**: Workers optimized

---

### - [ ] 84.8.4 Webserver Performance Tuning
Filename: `84_08_04_webserver_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize web UI

- [ ] Workers and threads
- [ ] Timeout settings
- [ ] Caching configuration
- [ ] Static asset serving

**Expected Behavior**: Webserver responsive

---

### - [ ] 84.8.5 Memory and Resource Tuning
Filename: `84_08_05_memory_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize resource usage

- [ ] Memory limits
- [ ] Garbage collection
- [ ] Temp file cleanup
- [ ] Resource monitoring

**Expected Behavior**: Resources efficient

---

# 84.9 Debugging Configuration Issues

## Overview
Troubleshooting configuration problems.

## Tasks

### - [ ] 84.9.1 Configuration Not Applied
Filename: `84_09_01_config_not_applied.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug missing config

- [ ] Check precedence
- [ ] Verify file location
- [ ] Environment override
- [ ] Service restart

**Expected Behavior**: Config applied

---

### - [ ] 84.9.2 Invalid Configuration Values
Filename: `84_09_02_invalid_values.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug invalid settings

- [ ] Type mismatches
- [ ] Out of range
- [ ] Invalid options
- [ ] Validation errors

**Expected Behavior**: Values corrected

---

### - [ ] 84.9.3 Deprecated Settings
Filename: `84_09_03_deprecated_settings.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Handle deprecations

- [ ] Identify deprecated
- [ ] Find replacements
- [ ] Migration path
- [ ] Version compatibility

**Expected Behavior**: Deprecations resolved

---

### - [ ] 84.9.4 Configuration Conflicts
Filename: `84_09_04_config_conflicts.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Resolve conflicts

- [ ] Contradictory settings
- [ ] Override conflicts
- [ ] Source identification
- [ ] Resolution strategies

**Expected Behavior**: Conflicts resolved

---

### - [ ] 84.9.5 Performance Configuration Issues
Filename: `84_09_05_performance_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug slow performance

- [ ] Identify bottlenecks
- [ ] Config analysis
- [ ] Resource monitoring
- [ ] Tuning recommendations

**Expected Behavior**: Performance improved

---

# 84.10 Real-World Examples

## Overview
Production configuration patterns.

## Tasks

### - [ ] 84.10.1 Small Team Configuration
Filename: `84_10_01_small_team_config.py` | Tags: `['reference', 'example', 'beginner', 'success']`

**Purpose**: Config for small deployments

- [ ] Minimal resources
- [ ] Essential settings
- [ ] Cost optimization
- [ ] Growth path

**Expected Behavior**: Small deploy works

---

### - [ ] 84.10.2 Enterprise Configuration
Filename: `84_10_02_enterprise_config.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Enterprise-grade config

- [ ] High availability
- [ ] Security hardening
- [ ] Compliance settings
- [ ] Scale configuration

**Expected Behavior**: Enterprise ready

---

### - [ ] 84.10.3 High-Volume Pipeline Configuration
Filename: `84_10_03_high_volume_config.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Config for high throughput

- [ ] Maximum parallelism
- [ ] Database scaling
- [ ] Worker optimization
- [ ] Queue management

**Expected Behavior**: High volume handled

---

### - [ ] 84.10.4 Multi-Tenant Configuration
Filename: `84_10_04_multi_tenant_config.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Multi-tenant setup

- [ ] Resource isolation
- [ ] Tenant configuration
- [ ] Access control
- [ ] Monitoring per tenant

**Expected Behavior**: Multi-tenant works

---

### - [ ] 84.10.5 Configuration as Code Pattern
Filename: `84_10_05_config_as_code.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Manage config with code

- [ ] Version control
- [ ] Automated deployment
- [ ] Environment templating
- [ ] Change tracking

**Expected Behavior**: Config managed as code

---

# Summary

## Topic Completion Checklist
- [ ] Configuration basics covered
- [ ] Core/scheduler settings documented
- [ ] Security configuration included
- [ ] Logging/monitoring explained
- [ ] Advanced configuration provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance tuning included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 83: Environment Variables
- Section 82: Secrets Backends
- Section 85: Deployment Patterns

## Notes for Implementation
- Reference all config sections
- Show tuning examples
- Include security settings
- Demonstrate validation
- Cover common issues
