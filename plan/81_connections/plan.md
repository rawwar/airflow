# 81 Connections

## Overview

Connections store credentials and configuration for external systems in Airflow. This section covers connection creation, management, URI formats, extra configuration, and security best practices for Airflow 3.x.

## Research & Background

### Key Concepts
- **Connection**: Stored credentials and metadata for external systems
- **Connection ID**: Unique identifier for referencing connections
- **Connection Type**: Defines schema and required fields
- **Extra**: JSON field for additional parameters
- **URI Format**: Connection string encoding

### Airflow 3.x Features
- Improved connection UI
- Enhanced connection testing
- Better secret masking
- Connection import/export
- Custom connection types

### Prerequisites
- Airflow 3.x installed
- Understanding of operators and hooks
- Basic security awareness

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Create and manage connections via UI and CLI
2. Use connection URI format
3. Configure extra parameters
4. Test connections effectively
5. Secure connection credentials

---

# 81.1 Connection Basics

## Overview
Understanding connection fundamentals.

## Tasks

### - [ ] 81.1.1 What is a Connection
Filename: `81_01_01_connection_intro.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand connection purpose

- [ ] Connection as credential store
- [ ] Connection fields (host, port, etc.)
- [ ] Connection types
- [ ] How operators use connections

**Expected Behavior**: Connection concept clear

---

### - [ ] 81.1.2 Creating Connections via UI
Filename: `81_01_02_ui_connections.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Add connections in web UI

- [ ] Admin > Connections menu
- [ ] Fill connection form
- [ ] Connection type selection
- [ ] Test connection button

**Expected Behavior**: UI connection created

---

### - [ ] 81.1.3 Connection via CLI
Filename: `81_01_03_cli_connections.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Manage connections via airflow CLI

- [ ] airflow connections add
- [ ] airflow connections list
- [ ] airflow connections get
- [ ] airflow connections delete

**Expected Behavior**: CLI management works

---

### - [ ] 81.1.4 Connection URI Format
Filename: `81_01_04_uri_format.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Understand URI encoding

- [ ] URI structure: scheme://user:pass@host:port/schema
- [ ] URL encoding special chars
- [ ] Extra as query params
- [ ] URI to connection mapping

**Expected Behavior**: URI format understood

---

### - [ ] 81.1.5 Environment Variable Connections
Filename: `81_01_05_env_var_connections.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Define connections via env vars

- [ ] AIRFLOW_CONN_{CONN_ID} format
- [ ] URI value in env var
- [ ] JSON format alternative
- [ ] Priority over database

**Expected Behavior**: Env var connection works

---

# 81.2 Connection Types

## Overview
Working with different connection types.

## Tasks

### - [ ] 81.2.1 Database Connections
Filename: `81_02_01_database_connections.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure database connections

- [ ] Postgres connection type
- [ ] MySQL connection type
- [ ] SQLite connection
- [ ] Common database fields

**Expected Behavior**: Database connections work

---

### - [ ] 81.2.2 Cloud Provider Connections
Filename: `81_02_02_cloud_connections.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: AWS, GCP, Azure connections

- [ ] AWS connection (key/secret or role)
- [ ] Google Cloud connection (service account)
- [ ] Azure connection (various auth)
- [ ] Cloud-specific extras

**Expected Behavior**: Cloud connections work

---

### - [ ] 81.2.3 HTTP/API Connections
Filename: `81_02_03_http_connections.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: REST API connections

- [ ] HTTP connection type
- [ ] Base URL configuration
- [ ] Headers in extra
- [ ] Authentication methods

**Expected Behavior**: HTTP connections work

---

### - [ ] 81.2.4 SSH/SFTP Connections
Filename: `81_02_04_ssh_connections.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: SSH and SFTP connections

- [ ] SSH connection type
- [ ] Private key configuration
- [ ] Host key verification
- [ ] SSH tunnel setup

**Expected Behavior**: SSH connections work

---

### - [ ] 81.2.5 Custom Connection Types
Filename: `81_02_05_custom_connections.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Define custom connection types

- [ ] Custom connection form
- [ ] Register via provider
- [ ] Connection type schema
- [ ] Custom test method

**Expected Behavior**: Custom type registered

---

# 81.3 Extra Configuration

## Overview
Using the extra JSON field effectively.

## Tasks

### - [ ] 81.3.1 Extra Field Basics
Filename: `81_03_01_extra_basics.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand extra field

- [ ] JSON format in extra
- [ ] Common extra parameters
- [ ] Access extra in hooks
- [ ] Extra vs other fields

**Expected Behavior**: Extra field usage clear

---

### - [ ] 81.3.2 AWS Extra Parameters
Filename: `81_03_02_aws_extra.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: AWS-specific extras

- [ ] region_name
- [ ] role_arn for assume role
- [ ] external_id
- [ ] endpoint_url for localstack

**Expected Behavior**: AWS extras configured

---

### - [ ] 81.3.3 GCP Extra Parameters
Filename: `81_03_03_gcp_extra.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: GCP-specific extras

- [ ] key_path or keyfile_dict
- [ ] project_id
- [ ] scopes
- [ ] num_retries

**Expected Behavior**: GCP extras configured

---

### - [ ] 81.3.4 Database Extra Parameters
Filename: `81_03_04_database_extra.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Database-specific extras

- [ ] SSL configuration
- [ ] Connection pool settings
- [ ] Timeout configuration
- [ ] Charset settings

**Expected Behavior**: Database extras work

---

### - [ ] 81.3.5 Dynamic Extra Values
Filename: `81_03_05_dynamic_extra.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Runtime extra configuration

- [ ] Override extras in hook
- [ ] Context-based extras
- [ ] Environment-specific
- [ ] Secret injection

**Expected Behavior**: Dynamic extras applied

---

# 81.4 Connection Testing and Validation

## Overview
Ensuring connections work correctly.

## Tasks

### - [ ] 81.4.1 UI Connection Test
Filename: `81_04_01_ui_test.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Test connections in UI

- [ ] Test Connection button
- [ ] Success/failure messages
- [ ] Connection test logging
- [ ] Troubleshoot failures

**Expected Behavior**: Connection test works

---

### - [ ] 81.4.2 CLI Connection Test
Filename: `81_04_02_cli_test.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Test via CLI

- [ ] airflow connections test
- [ ] Verbose output
- [ ] Hook-based testing
- [ ] Batch testing

**Expected Behavior**: CLI test works

---

### - [ ] 81.4.3 Programmatic Testing
Filename: `81_04_03_programmatic_test.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Test in DAG/task

- [ ] Hook.test_connection()
- [ ] Connection validation task
- [ ] Health check DAGs
- [ ] Alert on failure

**Expected Behavior**: Programmatic test works

---

### - [ ] 81.4.4 Connection Validation DAG
Filename: `81_04_04_validation_dag.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: DAG to validate all connections

- [ ] List critical connections
- [ ] Test each connection
- [ ] Report failures
- [ ] Schedule regular checks

**Expected Behavior**: Validation DAG runs

---

### - [ ] 81.4.5 Common Connection Errors
Filename: `81_04_05_common_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

**Purpose**: Debug connection issues

- [ ] Authentication failures
- [ ] Network/firewall issues
- [ ] SSL certificate errors
- [ ] Timeout problems

**Expected Behavior**: Errors diagnosed

---

# 81.5 Connection Security

## Overview
Securing connection credentials.

## Tasks

### - [ ] 81.5.1 Password Masking
Filename: `81_05_01_password_masking.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Hide passwords in logs

- [ ] Fernet encryption at rest
- [ ] Masking in UI
- [ ] Log scrubbing
- [ ] Extra field masking

**Expected Behavior**: Passwords masked

---

### - [ ] 81.5.2 Connection Export/Import
Filename: `81_05_02_export_import.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Migrate connections safely

- [ ] airflow connections export
- [ ] airflow connections import
- [ ] Exclude sensitive fields
- [ ] Environment promotion

**Expected Behavior**: Connections migrated

---

### - [ ] 81.5.3 Secrets Backend Integration
Filename: `81_05_03_secrets_backend.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: External secret storage

- [ ] Configure secrets backend
- [ ] Retrieve from backend
- [ ] Fallback behavior
- [ ] Backend priority

**Expected Behavior**: Secrets backend used

---

### - [ ] 81.5.4 Rotating Credentials
Filename: `81_05_04_credential_rotation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle credential changes

- [ ] Update connection safely
- [ ] Test after rotation
- [ ] Minimize downtime
- [ ] Automated rotation

**Expected Behavior**: Rotation handled

---

### - [ ] 81.5.5 Connection Access Control
Filename: `81_05_05_access_control.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Limit connection visibility

- [ ] RBAC for connections
- [ ] DAG-level connection access
- [ ] Audit connection usage
- [ ] Principle of least privilege

**Expected Behavior**: Access controlled

---

# 81.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding connection management pitfalls.

## Tasks

### - [ ] 81.6.1 Hardcoded Credentials Anti-Pattern
Filename: `81_06_01_hardcoded_credentials.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Never hardcode credentials

- [ ] Credentials in DAG code
- [ ] Credentials in version control
- [ ] Environment-specific leaks
- [ ] Use connections instead

**Expected Behavior**: Credentials externalized

---

### - [ ] 81.6.2 Shared Connection Abuse
Filename: `81_06_02_shared_connection_abuse.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid over-sharing connections

- [ ] One connection for all
- [ ] Permission creep
- [ ] Audit difficulty
- [ ] Purpose-specific connections

**Expected Behavior**: Connections scoped properly

---

### - [ ] 81.6.3 Missing Connection Documentation
Filename: `81_06_03_missing_documentation.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Document connections

- [ ] Unknown connection purpose
- [ ] Unclear ownership
- [ ] Missing dependencies
- [ ] Documentation patterns

**Expected Behavior**: Connections documented

---

### - [ ] 81.6.4 Stale Connection Management
Filename: `81_06_04_stale_connections.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Clean up unused connections

- [ ] Orphaned connections
- [ ] Expired credentials
- [ ] No usage tracking
- [ ] Cleanup procedures

**Expected Behavior**: Connections maintained

---

### - [ ] 81.6.5 Inconsistent Connection Naming
Filename: `81_06_05_inconsistent_naming.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Use consistent naming

- [ ] Random naming schemes
- [ ] Hard to find connections
- [ ] No conventions
- [ ] Naming standards

**Expected Behavior**: Names consistent

---

# 81.7 Testing Connections

## Overview
Testing connection configurations.

## Tasks

### - [ ] 81.7.1 Connection Unit Testing
Filename: `81_07_01_connection_unit_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test connection parsing

- [ ] URI parsing tests
- [ ] Extra field tests
- [ ] Type validation
- [ ] Mock connections

**Expected Behavior**: Connection logic tested

---

### - [ ] 81.7.2 Connection Integration Testing
Filename: `81_07_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test real connectivity

- [ ] Test connection validity
- [ ] Health check verification
- [ ] Permission testing
- [ ] Error handling

**Expected Behavior**: Connectivity verified

---

### - [ ] 81.7.3 Connection Validation Framework
Filename: `81_07_03_validation_framework.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Automated connection validation

- [ ] Scheduled validation DAG
- [ ] All connections tested
- [ ] Failure alerting
- [ ] Validation reporting

**Expected Behavior**: Connections validated regularly

---

### - [ ] 81.7.4 Mock Connection Testing
Filename: `81_07_04_mock_connection_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test without real systems

- [ ] Mock connection setup
- [ ] Simulated responses
- [ ] Error simulation
- [ ] CI/CD testing

**Expected Behavior**: Tests run without real connections

---

### - [ ] 81.7.5 Connection Migration Testing
Filename: `81_07_05_migration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test connection migrations

- [ ] Export/import testing
- [ ] Environment promotion
- [ ] Credential rotation
- [ ] Rollback testing

**Expected Behavior**: Migrations tested

---

# 81.8 Performance and Best Practices

## Overview
Connection management best practices.

## Tasks

### - [ ] 81.8.1 Connection Pooling Strategies
Filename: `81_08_01_connection_pooling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Optimize connection usage

- [ ] Pool configuration
- [ ] Hook connection reuse
- [ ] Pool sizing
- [ ] Connection lifecycle

**Expected Behavior**: Connections pooled efficiently

---

### - [ ] 81.8.2 Connection Naming Conventions
Filename: `81_08_02_naming_conventions.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`

**Purpose**: Establish naming standards

- [ ] Environment prefixes
- [ ] System identifiers
- [ ] Purpose suffixes
- [ ] Discoverability

**Expected Behavior**: Consistent naming

---

### - [ ] 81.8.3 Connection Organization
Filename: `81_08_03_connection_organization.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Organize connections effectively

- [ ] Group by system
- [ ] Environment separation
- [ ] Access control groups
- [ ] Documentation links

**Expected Behavior**: Connections organized

---

### - [ ] 81.8.4 Connection Lifecycle Management
Filename: `81_08_04_lifecycle_management.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Manage connection lifecycle

- [ ] Creation procedures
- [ ] Update processes
- [ ] Deprecation handling
- [ ] Deletion cleanup

**Expected Behavior**: Lifecycle managed

---

### - [ ] 81.8.5 Connection Auditing
Filename: `81_08_05_connection_auditing.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Audit connection usage

- [ ] Track connection access
- [ ] Usage reporting
- [ ] Compliance logging
- [ ] Change tracking

**Expected Behavior**: Connections audited

---

# 81.9 Debugging Connection Issues

## Overview
Troubleshooting connection problems.

## Tasks

### - [ ] 81.9.1 Connection Not Found Errors
Filename: `81_09_01_connection_not_found.py` | Tags: `['reference', 'debugging', 'beginner', 'failure']`

**Purpose**: Debug missing connections

- [ ] Verify connection exists
- [ ] Check connection ID
- [ ] Environment variables
- [ ] Secrets backend lookup

**Expected Behavior**: Missing connections found

---

### - [ ] 81.9.2 Authentication Failures
Filename: `81_09_02_auth_failures.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug auth problems

- [ ] Credential verification
- [ ] Password encoding
- [ ] Token expiration
- [ ] Permission issues

**Expected Behavior**: Auth issues resolved

---

### - [ ] 81.9.3 Network Connectivity Issues
Filename: `81_09_03_network_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug network problems

- [ ] Host resolution
- [ ] Port accessibility
- [ ] Firewall rules
- [ ] Proxy configuration

**Expected Behavior**: Network issues fixed

---

### - [ ] 81.9.4 SSL/TLS Connection Issues
Filename: `81_09_04_ssl_tls_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug SSL problems

- [ ] Certificate verification
- [ ] Self-signed certs
- [ ] TLS version issues
- [ ] Certificate chain

**Expected Behavior**: SSL issues resolved

---

### - [ ] 81.9.5 Extra Parameter Issues
Filename: `81_09_05_extra_parameter_issues.py` | Tags: `['reference', 'debugging', 'intermediate', 'failure']`

**Purpose**: Debug extra field problems

- [ ] JSON parsing errors
- [ ] Invalid parameters
- [ ] Provider-specific issues
- [ ] Parameter validation

**Expected Behavior**: Extra params fixed

---

# 81.10 Real-World Examples

## Overview
Production connection management patterns.

## Tasks

### - [ ] 81.10.1 Multi-Environment Connection Setup
Filename: `81_10_01_multi_environment_setup.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Setup for multiple environments

- [ ] Dev/staging/prod separation
- [ ] Environment-specific extras
- [ ] Promotion workflow
- [ ] Configuration management

**Expected Behavior**: Environments configured

---

### - [ ] 81.10.2 Cloud Provider Connection Management
Filename: `81_10_02_cloud_connections.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Manage cloud connections

- [ ] AWS/GCP/Azure setup
- [ ] Service account patterns
- [ ] Cross-account access
- [ ] IAM integration

**Expected Behavior**: Cloud connections work

---

### - [ ] 81.10.3 Database Connection Pool Configuration
Filename: `81_10_03_database_pool_config.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Configure database pools

- [ ] Pool size settings
- [ ] Timeout configuration
- [ ] SSL configuration
- [ ] Read replicas

**Expected Behavior**: DB connections optimized

---

### - [ ] 81.10.4 API Connection with OAuth
Filename: `81_10_04_api_oauth_connection.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: OAuth-based API connections

- [ ] OAuth configuration
- [ ] Token refresh
- [ ] Scope management
- [ ] Provider-specific setup

**Expected Behavior**: OAuth APIs accessible

---

### - [ ] 81.10.5 Connection Template Pattern
Filename: `81_10_05_connection_templates.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Templated connection management

- [ ] Base connection templates
- [ ] Environment overlays
- [ ] Automated provisioning
- [ ] Infrastructure as code

**Expected Behavior**: Connections templated

---

# Summary

## Topic Completion Checklist
- [ ] Connection basics covered
- [ ] Connection types documented
- [ ] Extra configuration included
- [ ] Testing patterns explained
- [ ] Security guidance provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Best practices documented
- [ ] Debugging guidance provided
- [ ] Real-world examples included

## Related Topics
- Section 82: Secrets Backends
- Section 84: Airflow Configuration
- Section 32: Security and Auth

## Notes for Implementation
- Show multiple creation methods
- Include error scenarios
- Demonstrate testing
- Cover security aspects
- Explain URI encoding
