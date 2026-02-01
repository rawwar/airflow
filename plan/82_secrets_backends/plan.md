# 82 Secrets Backends

## Overview

Secrets backends enable storing Airflow connections and variables in external secret management systems. This section covers configuring and using HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, and custom backends for Airflow 3.x.

## Research & Background

### Key Concepts
- **Secrets Backend**: External storage for sensitive configuration
- **Connection Lookup**: Retrieve connections from backend
- **Variable Lookup**: Retrieve variables from backend
- **Backend Priority**: Order of secret resolution
- **Secret Path**: Location of secret in backend

### Airflow 3.x Features
- Multiple simultaneous backends
- Improved caching
- Backend chaining
- Better error handling
- Custom backend support

### Prerequisites
- Airflow 3.x installed
- Access to secret management system
- Understanding of connections (Section 81)

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Configure secrets backends
2. Store connections in external systems
3. Manage variables securely
4. Chain multiple backends
5. Implement custom backends

---

# 82.1 Secrets Backend Fundamentals

## Overview
Understanding secrets backend architecture.

## Tasks

### - [ ] 82.1.1 What is a Secrets Backend
Filename: `82_01_01_secrets_backend_intro.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand secrets backend concept

- [ ] Central secret storage
- [ ] Separation of secrets from code
- [ ] Benefits over database storage
- [ ] When to use secrets backends

**Expected Behavior**: Backend concept clear

---

### - [ ] 82.1.2 Backend Configuration
Filename: `82_01_02_backend_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure backend in airflow.cfg

- [ ] backend setting in [secrets]
- [ ] backend_kwargs for parameters
- [ ] Multiple backend support
- [ ] Configuration via env vars

**Expected Behavior**: Backend configured

---

### - [ ] 82.1.3 Secret Lookup Order
Filename: `82_01_03_lookup_order.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand resolution priority

- [ ] Environment variables first
- [ ] Secrets backend second
- [ ] Metastore database last
- [ ] Short-circuit on find

**Expected Behavior**: Lookup order clear

---

### - [ ] 82.1.4 Connection vs Variable Backends
Filename: `82_01_04_conn_vs_var_backends.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Separate backends for different secrets

- [ ] Connection lookup path
- [ ] Variable lookup path
- [ ] Different prefixes
- [ ] Mixed backend strategies

**Expected Behavior**: Separation understood

---

### - [ ] 82.1.5 Backend Caching
Filename: `82_01_05_backend_caching.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Optimize backend calls

- [ ] Cache timeout settings
- [ ] Reduce API calls
- [ ] Cache invalidation
- [ ] Performance tuning

**Expected Behavior**: Caching configured

---

# 82.2 HashiCorp Vault Backend

## Overview
Using Vault for secrets management.

## Tasks

### - [ ] 82.2.1 Vault Backend Setup
Filename: `82_02_01_vault_setup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure Vault backend

- [ ] VaultBackend class
- [ ] Vault URL and mount point
- [ ] Authentication method
- [ ] Backend kwargs

**Expected Behavior**: Vault backend works

---

### - [ ] 82.2.2 Vault Authentication Methods
Filename: `82_02_02_vault_auth.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Authenticate to Vault

- [ ] Token authentication
- [ ] AppRole authentication
- [ ] Kubernetes auth
- [ ] AWS IAM auth

**Expected Behavior**: Vault auth works

---

### - [ ] 82.2.3 Vault Secret Paths
Filename: `82_02_03_vault_paths.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Organize secrets in Vault

- [ ] connections_path setting
- [ ] variables_path setting
- [ ] Path templates
- [ ] Nested paths

**Expected Behavior**: Secrets at correct paths

---

### - [ ] 82.2.4 Storing Connections in Vault
Filename: `82_02_04_vault_connections.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Store Airflow connections

- [ ] Connection as Vault secret
- [ ] Field mapping
- [ ] URI format storage
- [ ] Extra field handling

**Expected Behavior**: Connections from Vault

---

### - [ ] 82.2.5 Vault Dynamic Secrets
Filename: `82_02_05_vault_dynamic.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Use Vault dynamic secrets

- [ ] Database dynamic credentials
- [ ] AWS STS credentials
- [ ] Short-lived secrets
- [ ] Lease renewal

**Expected Behavior**: Dynamic secrets work

---

# 82.3 AWS Secrets Manager Backend

## Overview
Using AWS Secrets Manager.

## Tasks

### - [ ] 82.3.1 AWS Secrets Manager Setup
Filename: `82_03_01_aws_secrets_setup.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure AWS backend

- [ ] SecretsManagerBackend class
- [ ] AWS region
- [ ] Prefix configuration
- [ ] IAM permissions

**Expected Behavior**: AWS backend works

---

### - [ ] 82.3.2 IAM Authentication
Filename: `82_03_02_aws_iam_auth.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: AWS authentication setup

- [ ] IAM role for Airflow
- [ ] Instance profile
- [ ] IRSA for EKS
- [ ] Cross-account access

**Expected Behavior**: IAM auth works

---

### - [ ] 82.3.3 Secret Naming Convention
Filename: `82_03_03_aws_naming.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Organize secrets in AWS

- [ ] connections_prefix
- [ ] variables_prefix
- [ ] Secret name format
- [ ] Environment separation

**Expected Behavior**: Secrets organized

---

### - [ ] 82.3.4 Connection Storage Format
Filename: `82_03_04_aws_connection_format.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Store connections in Secrets Manager

- [ ] JSON format for connection
- [ ] URI format option
- [ ] Full lookup mode
- [ ] Field extraction

**Expected Behavior**: Connections retrieved

---

### - [ ] 82.3.5 Secrets Rotation
Filename: `82_03_05_aws_rotation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle automatic rotation

- [ ] Secrets Manager rotation
- [ ] Airflow cache refresh
- [ ] Zero-downtime rotation
- [ ] Rotation monitoring

**Expected Behavior**: Rotation handled

---

# 82.4 Other Backend Providers

## Overview
GCP, Azure, and other backends.

## Tasks

### - [ ] 82.4.1 GCP Secret Manager
Filename: `82_04_01_gcp_secret_manager.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use GCP Secret Manager

- [ ] CloudSecretManagerBackend
- [ ] Project configuration
- [ ] Secret versioning
- [ ] IAM setup

**Expected Behavior**: GCP backend works

---

### - [ ] 82.4.2 Azure Key Vault
Filename: `82_04_02_azure_key_vault.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use Azure Key Vault

- [ ] AzureKeyVaultBackend
- [ ] Vault URL
- [ ] Managed identity auth
- [ ] Secret naming

**Expected Behavior**: Azure backend works

---

### - [ ] 82.4.3 Kubernetes Secrets Backend
Filename: `82_04_03_kubernetes_secrets.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use K8s secrets

- [ ] KubernetesSecretsBackend
- [ ] Namespace configuration
- [ ] Secret format
- [ ] RBAC requirements

**Expected Behavior**: K8s secrets backend works

---

### - [ ] 82.4.4 Local Filesystem Backend
Filename: `82_04_04_local_filesystem.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: File-based secrets

- [ ] LocalFilesystemBackend
- [ ] File per secret
- [ ] Directory structure
- [ ] Development usage

**Expected Behavior**: Local backend works

---

### - [ ] 82.4.5 Environment Variable Backend
Filename: `82_04_05_env_var_backend.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Built-in env var lookup

- [ ] AIRFLOW_CONN_{ID} format
- [ ] AIRFLOW_VAR_{KEY} format
- [ ] Container deployments
- [ ] CI/CD integration

**Expected Behavior**: Env vars work

---

# 82.5 Custom and Advanced Backends

## Overview
Building custom backends and advanced patterns.

## Tasks

### - [ ] 82.5.1 Custom Backend Implementation
Filename: `82_05_01_custom_backend.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Build custom secrets backend

- [ ] Inherit BaseSecretsBackend
- [ ] Implement get_conn_uri
- [ ] Implement get_variable
- [ ] Register backend

**Expected Behavior**: Custom backend works

---

### - [ ] 82.5.2 Backend Chaining
Filename: `82_05_02_backend_chaining.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Multiple backends in order

- [ ] Fallback patterns
- [ ] Override specific secrets
- [ ] Environment-based routing
- [ ] Performance considerations

**Expected Behavior**: Chaining works

---

### - [ ] 82.5.3 Backend for Config Override
Filename: `82_05_03_config_override.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Override Airflow config via backend

- [ ] Config secrets backend
- [ ] Dynamic configuration
- [ ] Sensitive config values
- [ ] Limitations

**Expected Behavior**: Config from backend

---

### - [ ] 82.5.4 Backend Testing and Debugging
Filename: `82_05_04_backend_testing.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Test backend configuration

- [ ] Verify backend connection
- [ ] Test secret retrieval
- [ ] Debug lookup issues
- [ ] Logging configuration

**Expected Behavior**: Backend issues diagnosed

---

### - [ ] 82.5.5 Migration to Secrets Backend
Filename: `82_05_05_migration.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Migrate from database to backend

- [ ] Export existing secrets
- [ ] Store in new backend
- [ ] Verify retrieval
- [ ] Cleanup migration

**Expected Behavior**: Migration complete

---

# 82.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding secrets backend pitfalls.

## Tasks

### - [ ] 82.6.1 Secrets in Environment Variables
Filename: `82_06_01_secrets_in_env.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Avoid plain-text env secrets

- [ ] Secrets exposed in logs
- [ ] Container inspection risks
- [ ] No rotation capability
- [ ] Use backends instead

**Expected Behavior**: Secrets properly stored

---

### - [ ] 82.6.2 Hardcoded Backend Credentials
Filename: `82_06_02_hardcoded_backend_creds.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Bootstrap secrets securely

- [ ] Backend auth in config
- [ ] Circular dependency
- [ ] IAM-based auth preferred
- [ ] Secure bootstrap patterns

**Expected Behavior**: Bootstrap secure

---

### - [ ] 82.6.3 Ignoring Cache Configuration
Filename: `82_06_03_ignoring_cache.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Configure caching properly

- [ ] No caching = slow
- [ ] Over-caching = stale
- [ ] Rate limit issues
- [ ] Optimal cache settings

**Expected Behavior**: Cache configured

---

### - [ ] 82.6.4 Single Backend Dependency
Filename: `82_06_04_single_backend_dependency.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Plan for backend failures

- [ ] No fallback strategy
- [ ] Backend unavailability
- [ ] Emergency access
- [ ] Redundancy patterns

**Expected Behavior**: Backend resilient

---

### - [ ] 82.6.5 Missing Secret Versioning
Filename: `82_06_05_missing_versioning.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Version secrets properly

- [ ] No rollback capability
- [ ] Rotation confusion
- [ ] Audit trail missing
- [ ] Version management

**Expected Behavior**: Secrets versioned

---

# 82.7 Testing Secrets Backends

## Overview
Testing secrets backend configurations.

## Tasks

### - [ ] 82.7.1 Local Backend Testing
Filename: `82_07_01_local_backend_testing.py` | Tags: `['reference', 'testing', 'beginner', 'success']`

**Purpose**: Test backends locally

- [ ] Local Vault instance
- [ ] LocalStack for AWS
- [ ] Filesystem backend
- [ ] Development setup

**Expected Behavior**: Local testing works

---

### - [ ] 82.7.2 Backend Connection Testing
Filename: `82_07_02_backend_connection_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify backend connectivity

- [ ] Authentication tests
- [ ] Permission tests
- [ ] Path access tests
- [ ] Error handling

**Expected Behavior**: Backend accessible

---

### - [ ] 82.7.3 Secret Retrieval Testing
Filename: `82_07_03_secret_retrieval_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test secret retrieval

- [ ] Connection retrieval
- [ ] Variable retrieval
- [ ] Cache behavior
- [ ] Fallback testing

**Expected Behavior**: Secrets retrieved correctly

---

### - [ ] 82.7.4 Rotation Testing
Filename: `82_07_04_rotation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test secret rotation

- [ ] Pre-rotation state
- [ ] Rotation execution
- [ ] Post-rotation verification
- [ ] Cache invalidation

**Expected Behavior**: Rotation works

---

### - [ ] 82.7.5 Failover Testing
Filename: `82_07_05_failover_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Test backend failures

- [ ] Backend unavailability
- [ ] Fallback behavior
- [ ] Cache expiration
- [ ] Recovery testing

**Expected Behavior**: Failover works

---

# 82.8 Performance Optimization

## Overview
Optimizing secrets backend performance.

## Tasks

### - [ ] 82.8.1 Cache Tuning Strategies
Filename: `82_08_01_cache_tuning.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize secret caching

- [ ] TTL configuration
- [ ] Cache size limits
- [ ] Pre-warming cache
- [ ] Selective caching

**Expected Behavior**: Cache optimized

---

### - [ ] 82.8.2 Connection Pooling for Backends
Filename: `82_08_02_backend_connection_pooling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Pool backend connections

- [ ] HTTP connection reuse
- [ ] Pool sizing
- [ ] Keep-alive settings
- [ ] Timeout configuration

**Expected Behavior**: Connections efficient

---

### - [ ] 82.8.3 Batch Secret Retrieval
Filename: `82_08_03_batch_retrieval.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Retrieve multiple secrets efficiently

- [ ] Batch API usage
- [ ] Parallel retrieval
- [ ] Reduce round trips
- [ ] Bulk loading patterns

**Expected Behavior**: Batch retrieval efficient

---

### - [ ] 82.8.4 Backend Selection for Performance
Filename: `82_08_04_backend_selection.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Choose performant backend

- [ ] Backend latency comparison
- [ ] Regional considerations
- [ ] Caching capabilities
- [ ] Cost vs performance

**Expected Behavior**: Backend selected wisely

---

### - [ ] 82.8.5 Monitoring Backend Performance
Filename: `82_08_05_backend_monitoring.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Monitor backend metrics

- [ ] Retrieval latency
- [ ] Cache hit rates
- [ ] Error rates
- [ ] API call volume

**Expected Behavior**: Performance monitored

---

# 82.9 Debugging Backend Issues

## Overview
Troubleshooting secrets backend problems.

## Tasks

### - [ ] 82.9.1 Backend Authentication Failures
Filename: `82_09_01_auth_failures.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug auth problems

- [ ] Token expiration
- [ ] IAM permission issues
- [ ] Certificate problems
- [ ] Authentication logs

**Expected Behavior**: Auth issues resolved

---

### - [ ] 82.9.2 Secret Not Found Debugging
Filename: `82_09_02_secret_not_found.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug missing secrets

- [ ] Path verification
- [ ] Naming conventions
- [ ] Backend search order
- [ ] Fallback behavior

**Expected Behavior**: Secrets found

---

### - [ ] 82.9.3 Cache-Related Issues
Filename: `82_09_03_cache_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug cache problems

- [ ] Stale cache data
- [ ] Cache invalidation
- [ ] Cache miss debugging
- [ ] Force refresh

**Expected Behavior**: Cache issues fixed

---

### - [ ] 82.9.4 Backend Connectivity Issues
Filename: `82_09_04_connectivity_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug network problems

- [ ] Endpoint accessibility
- [ ] DNS resolution
- [ ] Proxy configuration
- [ ] Firewall rules

**Expected Behavior**: Connectivity restored

---

### - [ ] 82.9.5 Secret Format Issues
Filename: `82_09_05_format_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug format problems

- [ ] JSON parsing errors
- [ ] Connection URI format
- [ ] Encoding issues
- [ ] Schema validation

**Expected Behavior**: Format issues fixed

---

# 82.10 Real-World Examples

## Overview
Production secrets backend patterns.

## Tasks

### - [ ] 82.10.1 Enterprise Vault Integration
Filename: `82_10_01_enterprise_vault.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Enterprise Vault setup

- [ ] Namespace configuration
- [ ] Policy management
- [ ] AppRole setup
- [ ] Dynamic secrets

**Expected Behavior**: Enterprise Vault works

---

### - [ ] 82.10.2 AWS Multi-Account Secrets
Filename: `82_10_02_aws_multi_account.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Cross-account secret access

- [ ] Assume role patterns
- [ ] Resource policies
- [ ] Account organization
- [ ] Centralized secrets

**Expected Behavior**: Multi-account works

---

### - [ ] 82.10.3 Zero-Trust Secrets Architecture
Filename: `82_10_03_zero_trust_secrets.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Zero-trust secret access

- [ ] Identity-based access
- [ ] Just-in-time secrets
- [ ] Audit everything
- [ ] Least privilege

**Expected Behavior**: Zero-trust implemented

---

### - [ ] 82.10.4 Hybrid Backend Configuration
Filename: `82_10_04_hybrid_backend.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Multiple backends together

- [ ] Backend chaining
- [ ] Override patterns
- [ ] Environment-specific
- [ ] Fallback configuration

**Expected Behavior**: Hybrid setup works

---

### - [ ] 82.10.5 Secrets Rotation Automation
Filename: `82_10_05_rotation_automation.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Automate secret rotation

- [ ] Rotation scheduling
- [ ] Notification workflows
- [ ] Validation testing
- [ ] Rollback procedures

**Expected Behavior**: Rotation automated

---

# Summary

## Topic Completion Checklist
- [ ] Backend fundamentals covered
- [ ] Vault integration documented
- [ ] AWS Secrets Manager included
- [ ] Other providers explained
- [ ] Custom backends provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization included
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 81: Connections
- Section 84: Airflow Configuration
- Section 32: Security and Auth

## Notes for Implementation
- Use local Vault for examples
- Show multiple backends
- Include authentication
- Cover error scenarios
- Demonstrate migration
