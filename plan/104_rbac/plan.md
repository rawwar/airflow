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

# 104 Role-Based Access Control

## Overview

Role-based access control (RBAC) in Apache Airflow 3.x, covering role definitions, permission management, user authentication, DAG-level access control, and integration with external identity providers.

## Airflow 3.x Notes
- FAB (Flask-AppBuilder) RBAC enabled by default
- `access_control` parameter on DAGs
- Custom roles via webserver config
- Integration with OAuth/OIDC providers
- API authentication and authorization

---

# 104.1 RBAC Fundamentals

## Overview
Understanding Airflow's built-in RBAC system.

## Tasks

### - [ ] 104.1.1 Default Roles Overview
Filename: `104_01_01_default_roles.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand built-in roles

- [ ] Admin role capabilities
- [ ] User role permissions
- [ ] Viewer role limitations
- [ ] Op (Operator) role scope
- [ ] Public role restrictions

**Expected Behavior**: Clear understanding of default roles

---

### - [ ] 104.1.2 Permission Model Structure
Filename: `104_01_02_permission_model.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand permission architecture

- [ ] Resources in Airflow (DAGs, connections, variables)
- [ ] Actions (can_read, can_edit, can_delete)
- [ ] Permission = Action + Resource
- [ ] Role = Collection of permissions
- [ ] View permissions in UI

**Expected Behavior**: Understanding of permission structure

---

### - [ ] 104.1.3 User Management Basics
Filename: `104_01_03_user_management.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Manage users in Airflow

- [ ] Create users via UI
- [ ] Create users via CLI
- [ ] Assign roles to users
- [ ] Deactivate users
- [ ] Reset passwords

**Expected Behavior**: User CRUD operations working

---

### - [ ] 104.1.4 Role Assignment Patterns
Filename: `104_01_04_role_assignment.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Assign roles effectively

- [ ] Single role assignment
- [ ] Multiple roles per user
- [ ] Role inheritance patterns
- [ ] Temporary role elevation
- [ ] Audit role changes

**Expected Behavior**: Flexible role assignment

---

### - [ ] 104.1.5 RBAC Configuration Options
Filename: `104_01_05_rbac_config.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure RBAC behavior

- [ ] webserver_config.py settings
- [ ] AUTH_TYPE configurations
- [ ] Session management
- [ ] Login/logout customization
- [ ] Security settings

**Expected Behavior**: RBAC properly configured

---

# 104.2 Custom Roles

## Overview
Creating and managing custom roles for specific needs.

## Tasks

### - [ ] 104.2.1 Creating Custom Roles
Filename: `104_02_01_custom_roles.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Define custom roles

- [ ] Create role via UI
- [ ] Create role via CLI
- [ ] Create role via webserver_config.py
- [ ] Clone existing role
- [ ] Document role purpose

**Expected Behavior**: Custom roles created

---

### - [ ] 104.2.2 DAG-Specific Roles
Filename: `104_02_02_dag_specific_roles.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Roles for specific DAG access

- [ ] Team-based DAG access
- [ ] Project-specific roles
- [ ] Read-only analyst role
- [ ] DAG developer role
- [ ] Production operator role

**Expected Behavior**: Granular DAG access control

---

### - [ ] 104.2.3 Connection Manager Role
Filename: `104_02_03_connection_manager_role.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Role for connection management

- [ ] can_read connections
- [ ] can_edit connections
- [ ] can_create connections
- [ ] No DAG permissions
- [ ] Secrets access control

**Expected Behavior**: Isolated connection management

---

### - [ ] 104.2.4 Variable Admin Role
Filename: `104_02_04_variable_admin_role.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Role for variable management

- [ ] Variable read/write permissions
- [ ] No DAG trigger permissions
- [ ] Config management focus
- [ ] Environment-specific access
- [ ] Sensitive variable restrictions

**Expected Behavior**: Variable-focused role

---

### - [ ] 104.2.5 Read-Only Dashboard Role
Filename: `104_02_05_readonly_dashboard_role.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: View-only monitoring role

- [ ] Dashboard view access
- [ ] DAG run status read
- [ ] Task log reading
- [ ] No trigger permissions
- [ ] No edit permissions

**Expected Behavior**: Safe monitoring access

---

# 104.3 DAG-Level Access Control

## Overview
Controlling access at the individual DAG level.

## Tasks

### - [ ] 104.3.1 access_control Parameter
Filename: `104_03_01_access_control_param.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use access_control on DAGs

- [ ] Basic access_control syntax
- [ ] Map roles to permissions
- [ ] Multiple roles configuration
- [ ] Read vs edit permissions
- [ ] UI visibility effects

**Expected Behavior**: DAG restricted to specific roles

---

### - [ ] 104.3.2 Team-Based DAG Access
Filename: `104_03_02_team_dag_access.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Restrict DAGs to teams

- [ ] Create team roles
- [ ] Assign team members
- [ ] DAGs use team access_control
- [ ] Cross-team visibility
- [ ] Shared DAG patterns

**Expected Behavior**: Team-scoped DAG access

---

### - [ ] 104.3.3 Environment-Based Access
Filename: `104_03_03_environment_access.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Different access per environment

- [ ] Development environment access
- [ ] Staging access patterns
- [ ] Production restrictions
- [ ] Promote DAGs with access changes
- [ ] Environment role mapping

**Expected Behavior**: Environment-appropriate access

---

### - [ ] 104.3.4 Dynamic access_control
Filename: `104_03_04_dynamic_access_control.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Generate access_control dynamically

- [ ] Read access from config
- [ ] Variable-based role mapping
- [ ] Factory pattern for access
- [ ] Consistent across DAGs
- [ ] Centralized management

**Expected Behavior**: Manageable access control

---

### - [ ] 104.3.5 access_control Troubleshooting
Filename: `104_03_05_access_troubleshooting.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Debug access control issues

- [ ] Permission denied scenarios
- [ ] Role not found errors
- [ ] Cache invalidation
- [ ] Logging access checks
- [ ] Common misconfigurations

**Expected Behavior**: Ability to debug access issues

---

# 104.4 Authentication Providers

## Overview
Integrating external authentication systems.

## Tasks

### - [ ] 104.4.1 OAuth2 Integration
Filename: `104_04_01_oauth2_integration.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Configure OAuth2 authentication

- [ ] AUTH_TYPE = AUTH_OAUTH
- [ ] OAuth provider configuration
- [ ] Token handling
- [ ] User info mapping
- [ ] Scope configuration

**Expected Behavior**: OAuth2 login working

---

### - [ ] 104.4.2 OIDC Provider Setup
Filename: `104_04_02_oidc_setup.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: OpenID Connect integration

- [ ] OIDC provider configuration
- [ ] Discovery document usage
- [ ] Claims mapping to roles
- [ ] Group-to-role mapping
- [ ] Token refresh handling

**Expected Behavior**: OIDC authentication functional

---

### - [ ] 104.4.3 LDAP Authentication
Filename: `104_04_03_ldap_auth.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: LDAP/Active Directory integration

- [ ] AUTH_TYPE = AUTH_LDAP
- [ ] LDAP server configuration
- [ ] User search patterns
- [ ] Group membership mapping
- [ ] Bind credentials

**Expected Behavior**: LDAP login functional

---

### - [ ] 104.4.4 SAML Integration
Filename: `104_04_04_saml_integration.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: SAML SSO configuration

- [ ] SAML provider setup
- [ ] Metadata configuration
- [ ] Attribute mapping
- [ ] Certificate management
- [ ] Logout handling

**Expected Behavior**: SAML SSO working

---

### - [ ] 104.4.5 Remote User Authentication
Filename: `104_04_05_remote_user.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Proxy-based authentication

- [ ] AUTH_TYPE = AUTH_REMOTE_USER
- [ ] Trust proxy headers
- [ ] User auto-creation
- [ ] Role assignment from headers
- [ ] Security considerations

**Expected Behavior**: Proxy auth functional

---

# 104.5 API Authentication

## Overview
Securing API access in Airflow.

## Tasks

### - [ ] 104.5.1 Basic Auth for API
Filename: `104_05_01_basic_auth_api.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Configure basic auth for REST API

- [ ] Enable basic auth
- [ ] User credentials
- [ ] API endpoint access
- [ ] Rate limiting
- [ ] Security recommendations

**Expected Behavior**: API accessible with basic auth

---

### - [ ] 104.5.2 Token-Based API Auth
Filename: `104_05_02_token_auth.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use tokens for API access

- [ ] Generate API tokens
- [ ] Token expiration
- [ ] Token revocation
- [ ] Scope limitations
- [ ] Token rotation

**Expected Behavior**: Token-based API access

---

### - [ ] 104.5.3 Service Account Patterns
Filename: `104_05_03_service_accounts.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: API access for services

- [ ] Create service accounts
- [ ] Minimal permissions
- [ ] Dedicated roles
- [ ] Credential management
- [ ] Audit service actions

**Expected Behavior**: Secure service integration

---

### - [ ] 104.5.4 API Rate Limiting
Filename: `104_05_04_rate_limiting.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Protect API from abuse

- [ ] Rate limit configuration
- [ ] Per-user limits
- [ ] Per-endpoint limits
- [ ] Burst handling
- [ ] Rate limit headers

**Expected Behavior**: API protected from overload

---

### - [ ] 104.5.5 API Audit Logging
Filename: `104_05_05_api_audit.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Log API access

- [ ] Log all API calls
- [ ] Include user identity
- [ ] Request/response logging
- [ ] Sensitive data masking
- [ ] Compliance reporting

**Expected Behavior**: Complete API audit trail

---

# 104.6 RBAC Anti-Patterns

## Overview
Common RBAC mistakes to avoid.

## Tasks

### - [ ] 104.6.1 Over-Permissive Roles
Filename: `104_06_01_over_permissive_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Least privilege principle

- [ ] Show admin for everyone
- [ ] Demonstrate security risks
- [ ] Provide role scoping
- [ ] Include audit patterns

**Expected Behavior**: Minimal permissions

---

### - [ ] 104.6.2 Role Explosion
Filename: `104_06_02_role_explosion_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Manageable role count

- [ ] Show too many roles
- [ ] Demonstrate management issues
- [ ] Provide role hierarchy
- [ ] Include consolidation

**Expected Behavior**: Manageable roles

---

### - [ ] 104.6.3 Hardcoded Access Control
Filename: `104_06_03_hardcoded_access_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Configurable access

- [ ] Show hardcoded permissions
- [ ] Demonstrate inflexibility
- [ ] Provide config patterns
- [ ] Include external management

**Expected Behavior**: Flexible access

---

### - [ ] 104.6.4 No Access Audit
Filename: `104_06_04_no_audit_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Audit all access

- [ ] Show missing audit
- [ ] Demonstrate compliance gaps
- [ ] Provide audit patterns
- [ ] Include monitoring

**Expected Behavior**: Access audited

---

### - [ ] 104.6.5 Shared Service Accounts
Filename: `104_06_05_shared_accounts_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Individual accountability

- [ ] Show shared credentials
- [ ] Demonstrate attribution issues
- [ ] Provide per-user accounts
- [ ] Include rotation patterns

**Expected Behavior**: Individual accounts

---

# 104.7 RBAC Testing

## Overview
Testing RBAC configurations.

## Tasks

### - [ ] 104.7.1 Permission Testing
Filename: `104_07_01_permission_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify permissions work

- [ ] Positive permission tests
- [ ] Negative permission tests
- [ ] Boundary testing
- [ ] Role coverage

**Expected Behavior**: Permissions verified

---

### - [ ] 104.7.2 Role Inheritance Testing
Filename: `104_07_02_inheritance_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test role hierarchy

- [ ] Inherited permissions
- [ ] Override testing
- [ ] Denial testing
- [ ] Chain verification

**Expected Behavior**: Inheritance works

---

### - [ ] 104.7.3 access_control Testing
Filename: `104_07_03_access_control_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test DAG access

- [ ] Role-DAG mapping
- [ ] UI visibility tests
- [ ] API access tests
- [ ] Permission levels

**Expected Behavior**: DAG access correct

---

### - [ ] 104.7.4 Auth Provider Testing
Filename: `104_07_04_auth_provider_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test authentication

- [ ] Login flow testing
- [ ] Token handling
- [ ] Session testing
- [ ] Logout testing

**Expected Behavior**: Auth works

---

### - [ ] 104.7.5 RBAC Security Testing
Filename: `104_07_05_security_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Security verification

- [ ] Privilege escalation tests
- [ ] Bypass attempts
- [ ] Injection testing
- [ ] Session security

**Expected Behavior**: Security verified

---

# 104.8 RBAC Performance

## Overview
Optimizing RBAC performance.

## Tasks

### - [ ] 104.8.1 Permission Caching
Filename: `104_08_01_permission_caching.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Fast permission checks

- [ ] Cache strategies
- [ ] Invalidation patterns
- [ ] Cache sizing
- [ ] Hit rate monitoring

**Expected Behavior**: Fast checks

---

### - [ ] 104.8.2 Role Resolution Optimization
Filename: `104_08_02_role_resolution.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Efficient role lookup

- [ ] Role hierarchy caching
- [ ] Lazy loading
- [ ] Pre-computation
- [ ] Refresh strategies

**Expected Behavior**: Fast role resolution

---

### - [ ] 104.8.3 Session Management
Filename: `104_08_03_session_management.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Efficient sessions

- [ ] Session storage
- [ ] Token management
- [ ] Session cleanup
- [ ] Concurrent sessions

**Expected Behavior**: Efficient sessions

---

### - [ ] 104.8.4 Auth Provider Performance
Filename: `104_08_04_auth_provider_performance.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Fast authentication

- [ ] Connection pooling
- [ ] Token caching
- [ ] Timeout handling
- [ ] Failover patterns

**Expected Behavior**: Fast auth

---

### - [ ] 104.8.5 Large-Scale RBAC
Filename: `104_08_05_large_scale_rbac.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Scale RBAC

- [ ] Many users handling
- [ ] Many DAGs handling
- [ ] Role scalability
- [ ] Database optimization

**Expected Behavior**: RBAC scales

---

# 104.9 Advanced RBAC Patterns

## Overview
Sophisticated RBAC patterns.

## Tasks

### - [ ] 104.9.1 Attribute-Based Access Control
Filename: `104_09_01_abac.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: ABAC patterns

- [ ] Attribute definitions
- [ ] Policy rules
- [ ] Dynamic evaluation
- [ ] RBAC integration

**Expected Behavior**: ABAC works

---

### - [ ] 104.9.2 Policy-Based Access Control
Filename: `104_09_02_pbac.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Policy engine

- [ ] Policy definitions
- [ ] Evaluation engine
- [ ] Policy management
- [ ] Audit integration

**Expected Behavior**: Policies enforced

---

### - [ ] 104.9.3 Just-In-Time Access
Filename: `104_09_03_jit_access.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Temporary access

- [ ] Access requests
- [ ] Approval workflows
- [ ] Time-limited access
- [ ] Auto-revocation

**Expected Behavior**: JIT access works

---

### - [ ] 104.9.4 Break-Glass Procedures
Filename: `104_09_04_break_glass.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Emergency access

- [ ] Emergency procedures
- [ ] Override patterns
- [ ] Audit requirements
- [ ] Post-incident review

**Expected Behavior**: Emergency access safe

---

### - [ ] 104.9.5 Cross-System RBAC
Filename: `104_09_05_cross_system_rbac.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Unified access

- [ ] Role synchronization
- [ ] Cross-system mapping
- [ ] Central management
- [ ] Audit consolidation

**Expected Behavior**: Unified RBAC

---

# 104.10 Real-World Examples

## Overview
Complete RBAC implementations.

## Tasks

### - [ ] 104.10.1 Enterprise RBAC Setup
Filename: `104_10_01_enterprise_rbac.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Enterprise deployment

- [ ] Role hierarchy
- [ ] LDAP/AD integration
- [ ] Team structure
- [ ] Audit setup

**Expected Behavior**: Enterprise RBAC works

---

### - [ ] 104.10.2 Multi-Team Access Control
Filename: `104_10_02_multi_team_access.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Team isolation

- [ ] Team roles
- [ ] DAG ownership
- [ ] Shared DAG access
- [ ] Cross-team collaboration

**Expected Behavior**: Team access works

---

### - [ ] 104.10.3 Compliance-Focused RBAC
Filename: `104_10_03_compliance_rbac.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Regulatory compliance

- [ ] SOX compliance
- [ ] HIPAA patterns
- [ ] Audit requirements
- [ ] Reporting

**Expected Behavior**: Compliance met

---

### - [ ] 104.10.4 Cloud Identity Integration
Filename: `104_10_04_cloud_identity.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Cloud SSO

- [ ] Azure AD integration
- [ ] Google Workspace
- [ ] AWS IAM integration
- [ ] Okta/Auth0

**Expected Behavior**: Cloud SSO works

---

### - [ ] 104.10.5 Self-Service Access Management
Filename: `104_10_05_self_service_access.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: User self-service

- [ ] Access requests
- [ ] Approval workflows
- [ ] Role catalog
- [ ] Access review

**Expected Behavior**: Self-service works

---

# Summary

## Topic Completion Checklist
- [ ] Default roles explained
- [ ] Custom role creation covered
- [ ] DAG-level access control documented
- [ ] Auth providers integrated
- [ ] API security addressed
- [ ] Anti-patterns identified
- [ ] Testing covered
- [ ] Performance optimized
- [ ] Advanced patterns included
- [ ] Real-world examples provided

## Related Topics
- Section 103: Multi-Tenancy
- Section 32: Security and Authentication
- Section 48: REST API
- Section 47: UI Features

## Notes for Implementation
- Test permissions thoroughly
- Document custom roles
- Audit access regularly
- Plan for identity provider outages
- Include emergency access procedures
