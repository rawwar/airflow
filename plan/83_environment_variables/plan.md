# 83 Environment Variables

## Overview

Environment variables provide flexible configuration for Airflow components without code changes. This section covers Airflow-specific environment variables, configuration overrides, connection definitions, and best practices for environment management in Airflow 3.x.

## Research & Background

### Key Concepts
- **AIRFLOW__ Prefix**: Configuration override pattern
- **AIRFLOW_CONN_**: Connection definition format
- **AIRFLOW_VAR_**: Variable definition format
- **Environment Precedence**: Env vars override config file
- **Container Configuration**: Env-based deployment config

### Airflow 3.x Features
- Consistent env var naming
- Better documentation
- Improved secret handling
- Container-first design
- Dynamic configuration

### Prerequisites
- Airflow 3.x installed
- Basic shell/environment knowledge
- Understanding of Airflow configuration

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Override Airflow config via environment
2. Define connections and variables
3. Configure workers and executors
4. Manage secrets via environment
5. Deploy with environment-based config

---

# 83.1 Configuration Override

## Overview
Using environment variables to override airflow.cfg.

## Tasks

### - [ ] 83.1.1 AIRFLOW__ Naming Convention
Filename: `83_01_01_airflow_naming.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand env var naming

- [ ] AIRFLOW__{SECTION}__{KEY} format
- [ ] Double underscore as separator
- [ ] Case sensitivity
- [ ] Examples for common settings

**Expected Behavior**: Naming convention clear

---

### - [ ] 83.1.2 Core Configuration Overrides
Filename: `83_01_02_core_overrides.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Override [core] section settings

- [ ] AIRFLOW__CORE__EXECUTOR
- [ ] AIRFLOW__CORE__DAGS_FOLDER
- [ ] AIRFLOW__CORE__LOAD_EXAMPLES
- [ ] AIRFLOW__CORE__PARALLELISM

**Expected Behavior**: Core settings overridden

---

### - [ ] 83.1.3 Database Configuration
Filename: `83_01_03_database_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure database via env

- [ ] AIRFLOW__DATABASE__SQL_ALCHEMY_CONN
- [ ] Connection string formats
- [ ] Pool settings
- [ ] Encoding options

**Expected Behavior**: Database configured

---

### - [ ] 83.1.4 Webserver Configuration
Filename: `83_01_04_webserver_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure web UI via env

- [ ] AIRFLOW__WEBSERVER__BASE_URL
- [ ] AIRFLOW__WEBSERVER__WEB_SERVER_PORT
- [ ] AIRFLOW__WEBSERVER__SECRET_KEY
- [ ] Authentication settings

**Expected Behavior**: Webserver configured

---

### - [ ] 83.1.5 Logging Configuration
Filename: `83_01_05_logging_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure logging via env

- [ ] AIRFLOW__LOGGING__BASE_LOG_FOLDER
- [ ] AIRFLOW__LOGGING__REMOTE_LOGGING
- [ ] AIRFLOW__LOGGING__REMOTE_BASE_LOG_FOLDER
- [ ] Log level settings

**Expected Behavior**: Logging configured

---

# 83.2 Connections and Variables

## Overview
Defining connections and variables via environment.

## Tasks

### - [ ] 83.2.1 AIRFLOW_CONN_ Format
Filename: `83_02_01_conn_format.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Define connections via env

- [ ] AIRFLOW_CONN_{CONN_ID} naming
- [ ] URI format value
- [ ] JSON format alternative
- [ ] Special character handling

**Expected Behavior**: Connection created

---

### - [ ] 83.2.2 Connection URI Examples
Filename: `83_02_02_conn_uri_examples.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Common connection URIs

- [ ] PostgreSQL connection URI
- [ ] MySQL connection URI
- [ ] HTTP connection URI
- [ ] S3/AWS connection URI

**Expected Behavior**: Various connections defined

---

### - [ ] 83.2.3 JSON Connection Format
Filename: `83_02_03_conn_json_format.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Complex connections via JSON

- [ ] JSON object in env var
- [ ] Extra parameters
- [ ] Multiline handling
- [ ] When to use JSON vs URI

**Expected Behavior**: JSON connections work

---

### - [ ] 83.2.4 AIRFLOW_VAR_ Format
Filename: `83_02_04_var_format.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Define variables via env

- [ ] AIRFLOW_VAR_{KEY} naming
- [ ] String value
- [ ] JSON value for complex data
- [ ] Variable lookup order

**Expected Behavior**: Variables defined

---

### - [ ] 83.2.5 Sensitive Variable Handling
Filename: `83_02_05_sensitive_vars.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle secrets in env vars

- [ ] Password masking
- [ ] Sensitive key patterns
- [ ] Avoid logging secrets
- [ ] Container secrets injection

**Expected Behavior**: Secrets handled safely

---

# 83.3 Executor and Worker Configuration

## Overview
Configuring execution environment.

## Tasks

### - [ ] 83.3.1 Executor Selection
Filename: `83_03_01_executor_selection.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Choose executor via env

- [ ] AIRFLOW__CORE__EXECUTOR values
- [ ] LocalExecutor
- [ ] CeleryExecutor
- [ ] KubernetesExecutor

**Expected Behavior**: Executor configured

---

### - [ ] 83.3.2 Celery Configuration
Filename: `83_03_02_celery_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure Celery via env

- [ ] AIRFLOW__CELERY__BROKER_URL
- [ ] AIRFLOW__CELERY__RESULT_BACKEND
- [ ] Worker concurrency
- [ ] Queue configuration

**Expected Behavior**: Celery configured

---

### - [ ] 83.3.3 Kubernetes Executor Config
Filename: `83_03_03_kubernetes_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure K8s executor via env

- [ ] AIRFLOW__KUBERNETES_EXECUTOR__* settings
- [ ] Namespace configuration
- [ ] Pod template path
- [ ] Worker config

**Expected Behavior**: K8s executor configured

---

### - [ ] 83.3.4 Scheduler Configuration
Filename: `83_03_04_scheduler_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure scheduler via env

- [ ] AIRFLOW__SCHEDULER__* settings
- [ ] Parsing interval
- [ ] DAG dir list interval
- [ ] Max active runs

**Expected Behavior**: Scheduler tuned

---

### - [ ] 83.3.5 Triggerer Configuration
Filename: `83_03_05_triggerer_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure triggerer via env

- [ ] AIRFLOW__TRIGGERER__* settings
- [ ] Default capacity
- [ ] Job heartbeat
- [ ] Cleanup interval

**Expected Behavior**: Triggerer configured

---

# 83.4 Deployment Patterns

## Overview
Environment configuration for different deployments.

## Tasks

### - [ ] 83.4.1 Docker Compose Environment
Filename: `83_04_01_docker_compose.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`

**Purpose**: Env vars in Docker Compose

- [ ] environment section
- [ ] .env file usage
- [ ] env_file directive
- [ ] Secret management

**Expected Behavior**: Docker env configured

---

### - [ ] 83.4.2 Kubernetes ConfigMaps
Filename: `83_04_02_k8s_configmaps.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Env from K8s ConfigMaps

- [ ] ConfigMap creation
- [ ] envFrom in pods
- [ ] Individual env vars
- [ ] ConfigMap updates

**Expected Behavior**: K8s ConfigMaps work

---

### - [ ] 83.4.3 Kubernetes Secrets
Filename: `83_04_03_k8s_secrets.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Sensitive env from K8s Secrets

- [ ] Secret creation
- [ ] secretKeyRef usage
- [ ] External secret operators
- [ ] Secret rotation

**Expected Behavior**: K8s Secrets work

---

### - [ ] 83.4.4 Helm Values Configuration
Filename: `83_04_04_helm_values.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Configure via Helm values

- [ ] env in values.yaml
- [ ] extraEnv and extraEnvFrom
- [ ] Secret references
- [ ] Environment-specific values

**Expected Behavior**: Helm env configured

---

### - [ ] 83.4.5 CI/CD Environment Injection
Filename: `83_04_05_cicd_injection.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Inject env in CI/CD

- [ ] GitHub Actions secrets
- [ ] GitLab CI variables
- [ ] Jenkins credentials
- [ ] Build-time vs runtime

**Expected Behavior**: CI/CD injects env

---

# 83.5 Best Practices and Troubleshooting

## Overview
Environment variable best practices.

## Tasks

### - [ ] 83.5.1 Environment Variable Precedence
Filename: `83_05_01_precedence.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand override order

- [ ] Env var highest priority
- [ ] Config file second
- [ ] Default values last
- [ ] Debug precedence issues

**Expected Behavior**: Precedence clear

---

### - [ ] 83.5.2 Debugging Environment Issues
Filename: `83_05_02_debugging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Troubleshoot env problems

- [ ] airflow config list
- [ ] Check effective values
- [ ] Log current config
- [ ] Common mistakes

**Expected Behavior**: Issues diagnosed

---

### - [ ] 83.5.3 Environment Validation
Filename: `83_05_03_validation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Validate environment setup

- [ ] Required env vars check
- [ ] Startup validation DAG
- [ ] Configuration health check
- [ ] Missing config detection

**Expected Behavior**: Validation works

---

### - [ ] 83.5.4 Environment Documentation
Filename: `83_05_04_documentation.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`

**Purpose**: Document env requirements

- [ ] Required variables list
- [ ] Optional overrides
- [ ] Example .env files
- [ ] Environment README

**Expected Behavior**: Env documented

---

### - [ ] 83.5.5 Security Best Practices
Filename: `83_05_05_security.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Secure environment handling

- [ ] Never commit secrets
- [ ] Use secret management
- [ ] Audit env access
- [ ] Rotate secrets

**Expected Behavior**: Env secured

---

# 83.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding environment variable pitfalls.

## Tasks

### - [ ] 83.6.1 Secrets in Plain Text Env Vars
Filename: `83_06_01_secrets_plain_text.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Secure sensitive env vars

- [ ] Exposed in process list
- [ ] Logged accidentally
- [ ] Container inspection
- [ ] Use secrets instead

**Expected Behavior**: Secrets secured

---

### - [ ] 83.6.2 Inconsistent Naming Conventions
Filename: `83_06_02_inconsistent_naming.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Use consistent naming

- [ ] Mixed naming styles
- [ ] Missing prefixes
- [ ] Collision risks
- [ ] Naming standards

**Expected Behavior**: Names consistent

---

### - [ ] 83.6.3 Missing Environment Documentation
Filename: `83_06_03_missing_documentation.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Document required env vars

- [ ] Undocumented requirements
- [ ] Deployment failures
- [ ] Onboarding difficulties
- [ ] Documentation templates

**Expected Behavior**: Env vars documented

---

### - [ ] 83.6.4 Environment Drift
Filename: `83_06_04_environment_drift.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Prevent configuration drift

- [ ] Inconsistent environments
- [ ] Manual changes
- [ ] No version control
- [ ] IaC patterns

**Expected Behavior**: Environments consistent

---

### - [ ] 83.6.5 Overriding Critical Settings
Filename: `83_06_05_overriding_critical.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Protect critical settings

- [ ] Accidental overrides
- [ ] Security setting changes
- [ ] Production impact
- [ ] Protection patterns

**Expected Behavior**: Critical settings protected

---

# 83.7 Testing Environment Configuration

## Overview
Testing environment variable configurations.

## Tasks

### - [ ] 83.7.1 Environment Validation Testing
Filename: `83_07_01_validation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate env var configuration

- [ ] Required vars present
- [ ] Value format validation
- [ ] Type checking
- [ ] Range validation

**Expected Behavior**: Config validated

---

### - [ ] 83.7.2 Configuration Diff Testing
Filename: `83_07_02_config_diff_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Compare configurations

- [ ] Env to env comparison
- [ ] Detect missing vars
- [ ] Value differences
- [ ] Report generation

**Expected Behavior**: Diffs detected

---

### - [ ] 83.7.3 Environment Isolation Testing
Filename: `83_07_03_isolation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test environment isolation

- [ ] No cross-env leakage
- [ ] Isolated test runs
- [ ] Environment switching
- [ ] Cleanup verification

**Expected Behavior**: Environments isolated

---

### - [ ] 83.7.4 Default Value Testing
Filename: `83_07_04_default_value_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test default behaviors

- [ ] Verify defaults applied
- [ ] Override behavior
- [ ] Missing var handling
- [ ] Fallback testing

**Expected Behavior**: Defaults work correctly

---

### - [ ] 83.7.5 CI Environment Testing
Filename: `83_07_05_ci_environment_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test in CI pipelines

- [ ] CI secret injection
- [ ] Environment setup
- [ ] Automated validation
- [ ] Environment parity

**Expected Behavior**: CI testing works

---

# 83.8 Advanced Configuration Patterns

## Overview
Advanced environment configuration patterns.

## Tasks

### - [ ] 83.8.1 Dynamic Environment Configuration
Filename: `83_08_01_dynamic_configuration.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Runtime configuration changes

- [ ] Config from external sources
- [ ] Feature flags
- [ ] A/B testing config
- [ ] Gradual rollouts

**Expected Behavior**: Dynamic config works

---

### - [ ] 83.8.2 Environment Hierarchy Patterns
Filename: `83_08_02_environment_hierarchy.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Layer configurations

- [ ] Base configurations
- [ ] Environment overlays
- [ ] Instance-specific
- [ ] Merge strategies

**Expected Behavior**: Hierarchy applied

---

### - [ ] 83.8.3 Secret Injection Patterns
Filename: `83_08_03_secret_injection.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Secure secret injection

- [ ] Init container injection
- [ ] Vault agent sidecar
- [ ] External secrets operator
- [ ] Runtime injection

**Expected Behavior**: Secrets injected securely

---

### - [ ] 83.8.4 Configuration Templating
Filename: `83_08_04_configuration_templating.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Template configurations

- [ ] Jinja templating
- [ ] Envsubst usage
- [ ] Helm values templating
- [ ] Variable interpolation

**Expected Behavior**: Templates rendered

---

### - [ ] 83.8.5 Multi-Tenant Configuration
Filename: `83_08_05_multi_tenant_config.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Tenant-specific configs

- [ ] Namespace isolation
- [ ] Tenant configuration
- [ ] Shared base config
- [ ] Override patterns

**Expected Behavior**: Multi-tenant works

---

# 83.9 Debugging Environment Issues

## Overview
Troubleshooting environment problems.

## Tasks

### - [ ] 83.9.1 Missing Variable Debugging
Filename: `83_09_01_missing_variable.py` | Tags: `['reference', 'debugging', 'beginner', 'failure']`

**Purpose**: Debug missing env vars

- [ ] Check environment
- [ ] Container inspection
- [ ] Startup logs
- [ ] Default fallbacks

**Expected Behavior**: Missing vars found

---

### - [ ] 83.9.2 Value Format Issues
Filename: `83_09_02_value_format_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug format problems

- [ ] Escaping issues
- [ ] Multiline values
- [ ] Special characters
- [ ] Encoding problems

**Expected Behavior**: Format issues fixed

---

### - [ ] 83.9.3 Precedence Confusion
Filename: `83_09_03_precedence_confusion.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Understand override order

- [ ] Unexpected values
- [ ] Multiple sources
- [ ] Precedence verification
- [ ] Source tracing

**Expected Behavior**: Precedence clear

---

### - [ ] 83.9.4 Container Environment Issues
Filename: `83_09_04_container_env_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug container env vars

- [ ] ConfigMap not mounted
- [ ] Secret not available
- [ ] Ordering issues
- [ ] Volume mount problems

**Expected Behavior**: Container env fixed

---

### - [ ] 83.9.5 Environment Leakage Detection
Filename: `83_09_05_env_leakage.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Detect environment leaks

- [ ] Cross-env contamination
- [ ] Stale values
- [ ] Log exposure
- [ ] Security audit

**Expected Behavior**: Leakage detected

---

# 83.10 Real-World Examples

## Overview
Production environment configuration patterns.

## Tasks

### - [ ] 83.10.1 Complete Production Environment Setup
Filename: `83_10_01_production_setup.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Full production config

- [ ] All required vars
- [ ] Security settings
- [ ] Performance tuning
- [ ] Logging config

**Expected Behavior**: Production configured

---

### - [ ] 83.10.2 Kubernetes Helm Values Pattern
Filename: `83_10_02_helm_values_pattern.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: K8s deployment config

- [ ] values.yaml structure
- [ ] Environment secrets
- [ ] ConfigMap usage
- [ ] Per-env overrides

**Expected Behavior**: Helm config works

---

### - [ ] 83.10.3 Docker Compose Multi-Environment
Filename: `83_10_03_docker_compose_multi_env.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Docker Compose environments

- [ ] Base compose file
- [ ] Override files
- [ ] .env files
- [ ] Environment switching

**Expected Behavior**: Multi-env compose works

---

### - [ ] 83.10.4 CI/CD Pipeline Environment Setup
Filename: `83_10_04_cicd_pipeline_setup.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: CI/CD environment config

- [ ] Secret variables
- [ ] Environment-specific jobs
- [ ] Deployment credentials
- [ ] Dynamic environments

**Expected Behavior**: CI/CD env configured

---

### - [ ] 83.10.5 Environment Migration Playbook
Filename: `83_10_05_environment_migration.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Migrate environment configs

- [ ] Export current config
- [ ] Transform for new env
- [ ] Validation steps
- [ ] Rollback procedures

**Expected Behavior**: Migration successful

---

# Summary

## Topic Completion Checklist
- [ ] Configuration override covered
- [ ] Connections/variables documented
- [ ] Executor configuration included
- [ ] Deployment patterns explained
- [ ] Best practices provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Advanced patterns documented
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 81: Connections
- Section 82: Secrets Backends
- Section 84: Airflow Configuration

## Notes for Implementation
- Show common overrides
- Include Docker examples
- Cover Kubernetes patterns
- Demonstrate debugging
- Explain precedence
