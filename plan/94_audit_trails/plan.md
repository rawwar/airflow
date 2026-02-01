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

# 94 Audit Trails

## Overview

Audit logging captures who did what and when in Airflow, essential for compliance, security, and debugging. Airflow 3.x provides comprehensive audit capabilities through action logging, API audit trails, and integration with external audit systems.

## Airflow 3.x Notes
- Enhanced audit logging in webserver
- REST API action logging
- Improved user action tracking
- Integration with SIEM systems
- DAG-level access audit

---

# 94.1 Built-in Audit Logging

## Overview
Understanding Airflow's native audit capabilities.

## Tasks

### - [ ] 94.1.1 Webserver Action Logging
Filename: `94_01_01_webserver_action_logging.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand webserver audit logs

- [ ] Log table structure
- [ ] Action types tracked
- [ ] User attribution
- [ ] Timestamp recording

**Expected Behavior**: Actions logged in DB

---

### - [ ] 94.1.2 Log Table Schema
Filename: `94_01_02_log_table_schema.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand log data model

- [ ] log table columns
- [ ] Event types
- [ ] Extra field JSON
- [ ] Owner tracking

**Expected Behavior**: Schema understood

---

### - [ ] 94.1.3 Querying Audit Logs
Filename: `94_01_03_querying_audit_logs.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Extract audit information

- [ ] SQL queries for audit
- [ ] Filter by user/action
- [ ] Time range queries
- [ ] Aggregation reports

**Expected Behavior**: Audit queries work

---

### - [ ] 94.1.4 Audit Log Retention
Filename: `94_01_04_audit_log_retention.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manage audit log lifecycle

- [ ] Retention policies
- [ ] Log cleanup jobs
- [ ] Archive strategies
- [ ] Compliance requirements

**Expected Behavior**: Retention managed

---

### - [ ] 94.1.5 Viewing Logs in UI
Filename: `94_01_05_viewing_logs_ui.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Access audit logs via UI

- [ ] Browse > Audit Logs
- [ ] Filter and search
- [ ] Export capabilities
- [ ] User activity view

**Expected Behavior**: UI audit access

---

# 94.2 DAG and Task Audit

## Overview
Tracking changes and executions at DAG/task level.

## Tasks

### - [ ] 94.2.1 DAG Trigger Audit
Filename: `94_02_01_dag_trigger_audit.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Track DAG trigger events

- [ ] Manual trigger logging
- [ ] Triggering user
- [ ] Run configuration
- [ ] Trigger source

**Expected Behavior**: Triggers audited

---

### - [ ] 94.2.2 Task State Change Audit
Filename: `94_02_02_task_state_change_audit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track task state modifications

- [ ] Manual state changes
- [ ] Clear task audit
- [ ] Mark success/failed
- [ ] User attribution

**Expected Behavior**: State changes tracked

---

### - [ ] 94.2.3 DAG Pause/Unpause Audit
Filename: `94_02_03_dag_pause_audit.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Track DAG toggle events

- [ ] Pause action logging
- [ ] Unpause action logging
- [ ] Bulk operations
- [ ] Scheduled vs manual

**Expected Behavior**: Toggles audited

---

### - [ ] 94.2.4 Configuration Change Audit
Filename: `94_02_04_config_change_audit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track configuration changes

- [ ] Variable changes
- [ ] Connection modifications
- [ ] Pool updates
- [ ] Diff tracking

**Expected Behavior**: Config changes logged

---

### - [ ] 94.2.5 DAG Code Change Tracking
Filename: `94_02_05_dag_code_tracking.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Track DAG file changes

- [ ] Git commit correlation
- [ ] Serialized DAG versioning
- [ ] Change history
- [ ] Rollback tracking

**Expected Behavior**: Code changes tracked

---

# 94.3 API Audit Logging

## Overview
Auditing REST API access and modifications.

## Tasks

### - [ ] 94.3.1 REST API Access Logging
Filename: `94_03_01_rest_api_access_logging.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Log API endpoint access

- [ ] Request logging
- [ ] Authentication tracking
- [ ] Response codes
- [ ] Request payload

**Expected Behavior**: API access logged

---

### - [ ] 94.3.2 API Authentication Audit
Filename: `94_03_02_api_auth_audit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track API authentication

- [ ] Success/failure logging
- [ ] Token usage tracking
- [ ] OAuth flow audit
- [ ] Failed attempt alerts

**Expected Behavior**: Auth events audited

---

### - [ ] 94.3.3 API Modification Tracking
Filename: `94_03_03_api_modification_tracking.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Audit API write operations

- [ ] POST/PUT/PATCH/DELETE logging
- [ ] Before/after state
- [ ] User attribution
- [ ] Change categorization

**Expected Behavior**: Modifications tracked

---

### - [ ] 94.3.4 Rate Limit Audit
Filename: `94_03_04_rate_limit_audit.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track rate limiting events

- [ ] Rate limit hits
- [ ] Client identification
- [ ] Threshold alerts
- [ ] Abuse detection

**Expected Behavior**: Rate limits audited

---

### - [ ] 94.3.5 Service Account Activity
Filename: `94_03_05_service_account_activity.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Track automation access

- [ ] Service account usage
- [ ] CI/CD pipeline access
- [ ] Scheduled API calls
- [ ] Permission usage

**Expected Behavior**: Service accounts tracked

---

# 94.4 External Audit Integration

## Overview
Integrating with external audit and SIEM systems.

## Tasks

### - [ ] 94.4.1 Splunk Audit Integration
Filename: `94_04_01_splunk_integration.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Send audit logs to Splunk

- [ ] Log forwarding setup
- [ ] HEC configuration
- [ ] Index mapping
- [ ] Search patterns

**Expected Behavior**: Audit in Splunk

---

### - [ ] 94.4.2 Elasticsearch Audit Logging
Filename: `94_04_02_elasticsearch_audit.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Store audit in Elasticsearch

- [ ] Logstash pipeline
- [ ] Index templates
- [ ] Kibana dashboards
- [ ] Retention policies

**Expected Behavior**: Audit in ELK

---

### - [ ] 94.4.3 CloudWatch Audit Trail
Filename: `94_04_03_cloudwatch_audit.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: AWS CloudWatch audit integration

- [ ] Log group setup
- [ ] CloudWatch insights
- [ ] Alarm integration
- [ ] Cross-account access

**Expected Behavior**: Audit in CloudWatch

---

### - [ ] 94.4.4 GCP Cloud Audit Logs
Filename: `94_04_04_gcp_audit_logs.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: GCP audit integration

- [ ] Cloud Logging setup
- [ ] Audit log types
- [ ] BigQuery export
- [ ] Log router

**Expected Behavior**: Audit in GCP

---

### - [ ] 94.4.5 Custom Audit Webhook
Filename: `94_04_05_custom_audit_webhook.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Custom audit destination

- [ ] Webhook listener
- [ ] Log transformation
- [ ] Batching logic
- [ ] Retry handling

**Expected Behavior**: Custom audit works

---

# 94.5 Compliance and Reporting

## Overview
Audit reporting for compliance requirements.

## Tasks

### - [ ] 94.5.1 User Activity Report
Filename: `94_05_01_user_activity_report.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Generate user activity reports

- [ ] Per-user action summary
- [ ] Time-based filtering
- [ ] Action categorization
- [ ] Export formats

**Expected Behavior**: Activity reports generated

---

### - [ ] 94.5.2 Access Control Report
Filename: `94_05_02_access_control_report.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Report on permissions

- [ ] Role assignments
- [ ] Permission changes
- [ ] Access patterns
- [ ] Privilege escalation

**Expected Behavior**: Access report ready

---

### - [ ] 94.5.3 Data Access Audit
Filename: `94_05_03_data_access_audit.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Track data access

- [ ] Connection usage
- [ ] Query logging
- [ ] Sensitive data access
- [ ] Data lineage

**Expected Behavior**: Data access tracked

---

### - [ ] 94.5.4 Change Management Report
Filename: `94_05_04_change_management_report.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Track all changes

- [ ] Configuration changes
- [ ] DAG modifications
- [ ] Infrastructure changes
- [ ] Approval tracking

**Expected Behavior**: Changes documented

---

### - [ ] 94.5.5 Compliance Dashboard
Filename: `94_05_05_compliance_dashboard.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Visual compliance overview

- [ ] Audit summary metrics
- [ ] Anomaly detection
- [ ] Policy violations
- [ ] Compliance score

**Expected Behavior**: Compliance visible

---

# 94.6 Audit Anti-Patterns

## Overview
Common audit logging mistakes to avoid.

## Tasks

### - [ ] 94.6.1 Insufficient Audit Coverage
Filename: `94_06_01_insufficient_coverage_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Avoid audit gaps

- [ ] Show missing audit events
- [ ] Demonstrate compliance gaps
- [ ] Provide comprehensive coverage
- [ ] Include audit checklist

**Expected Behavior**: Complete audit coverage

---

### - [ ] 94.6.2 Sensitive Data in Audit Logs
Filename: `94_06_02_sensitive_data_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Protect sensitive info

- [ ] Show password logging
- [ ] Demonstrate PII exposure
- [ ] Provide masking patterns
- [ ] Include redaction strategies

**Expected Behavior**: Sensitive data protected

---

### - [ ] 94.6.3 Mutable Audit Logs
Filename: `94_06_03_mutable_logs_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Ensure log integrity

- [ ] Show editable logs
- [ ] Demonstrate tampering risk
- [ ] Provide immutable storage
- [ ] Include integrity verification

**Expected Behavior**: Tamper-proof logs

---

### - [ ] 94.6.4 Missing Timestamps
Filename: `94_06_04_missing_timestamps_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Proper time tracking

- [ ] Show missing/wrong timestamps
- [ ] Demonstrate forensics issues
- [ ] Provide UTC standardization
- [ ] Include timezone handling

**Expected Behavior**: Accurate timestamps

---

### - [ ] 94.6.5 Unstructured Audit Logs
Filename: `94_06_05_unstructured_logs_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Queryable audit logs

- [ ] Show free-text logs
- [ ] Demonstrate search difficulty
- [ ] Provide structured logging
- [ ] Include schema standards

**Expected Behavior**: Structured audit data

---

# 94.7 Audit Testing

## Overview
Testing audit log implementations.

## Tasks

### - [ ] 94.7.1 Unit Testing Audit Functions
Filename: `94_07_01_unit_testing_audit.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test audit logic

- [ ] Mock audit storage
- [ ] Test event capture
- [ ] Verify log content
- [ ] Test error handling

**Expected Behavior**: Audit logic tested

---

### - [ ] 94.7.2 Integration Testing Audit Trail
Filename: `94_07_02_integration_testing_audit.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: End-to-end audit testing

- [ ] Full action audit
- [ ] Query verification
- [ ] Retention testing
- [ ] Export validation

**Expected Behavior**: Audit trail verified

---

### - [ ] 94.7.3 Audit Completeness Testing
Filename: `94_07_03_completeness_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify all events logged

- [ ] Action coverage matrix
- [ ] Missing event detection
- [ ] Gap analysis
- [ ] Compliance verification

**Expected Behavior**: Complete audit coverage

---

### - [ ] 94.7.4 Audit Query Performance Testing
Filename: `94_07_04_query_performance_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test query speed

- [ ] Large volume queries
- [ ] Index effectiveness
- [ ] Time range queries
- [ ] Aggregation performance

**Expected Behavior**: Fast audit queries

---

### - [ ] 94.7.5 Audit Retention Testing
Filename: `94_07_05_retention_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify retention policies

- [ ] Archival verification
- [ ] Cleanup testing
- [ ] Recovery testing
- [ ] Compliance validation

**Expected Behavior**: Retention works correctly

---

# 94.8 Audit Performance

## Overview
Optimizing audit log performance.

## Tasks

### - [ ] 94.8.1 Async Audit Logging
Filename: `94_08_01_async_audit_logging.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Non-blocking audit

- [ ] Background logging
- [ ] Queue-based writes
- [ ] Batch processing
- [ ] Failure handling

**Expected Behavior**: No performance impact

---

### - [ ] 94.8.2 Audit Log Indexing
Filename: `94_08_02_audit_log_indexing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Fast audit queries

- [ ] Index strategy
- [ ] Partition by time
- [ ] Secondary indexes
- [ ] Index maintenance

**Expected Behavior**: Sub-second queries

---

### - [ ] 94.8.3 Audit Log Compression
Filename: `94_08_03_audit_log_compression.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Reduce storage

- [ ] Compression algorithms
- [ ] Cold storage tiering
- [ ] Decompression cost
- [ ] Query impact

**Expected Behavior**: Efficient storage

---

### - [ ] 94.8.4 Audit Log Partitioning
Filename: `94_08_04_audit_log_partitioning.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Scalable storage

- [ ] Time-based partitioning
- [ ] Partition pruning
- [ ] Archive partitions
- [ ] Partition management

**Expected Behavior**: Scalable audit storage

---

### - [ ] 94.8.5 Audit Log Sampling
Filename: `94_08_05_audit_log_sampling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Reduce high-volume logs

- [ ] Read sampling
- [ ] Debug log sampling
- [ ] Critical event preservation
- [ ] Sample rate tuning

**Expected Behavior**: Balanced coverage

---

# 94.9 Advanced Audit Patterns

## Overview
Sophisticated audit implementations.

## Tasks

### - [ ] 94.9.1 Audit Event Correlation
Filename: `94_09_01_event_correlation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Connect related events

- [ ] Session tracking
- [ ] Request tracing
- [ ] Workflow correlation
- [ ] Cross-system correlation

**Expected Behavior**: Related events linked

---

### - [ ] 94.9.2 Anomaly Detection in Audit
Filename: `94_09_02_anomaly_detection.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Detect suspicious activity

- [ ] Baseline behavior
- [ ] Unusual patterns
- [ ] Alert generation
- [ ] Investigation triggers

**Expected Behavior**: Anomalies detected

---

### - [ ] 94.9.3 Real-Time Audit Monitoring
Filename: `94_09_03_realtime_monitoring.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Live audit visibility

- [ ] Stream processing
- [ ] Real-time alerts
- [ ] Live dashboards
- [ ] Event streaming

**Expected Behavior**: Instant visibility

---

### - [ ] 94.9.4 Audit Chain of Custody
Filename: `94_09_04_chain_of_custody.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Forensic readiness

- [ ] Hash-based integrity
- [ ] Timestamp proof
- [ ] Custody transfer
- [ ] Legal requirements

**Expected Behavior**: Forensically sound

---

### - [ ] 94.9.5 Cross-System Audit Federation
Filename: `94_09_05_audit_federation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Unified audit view

- [ ] Multi-system correlation
- [ ] Centralized queries
- [ ] Schema mapping
- [ ] Timeline unification

**Expected Behavior**: Unified audit trail

---

# 94.10 Real-World Examples

## Overview
Complete audit implementations.

## Tasks

### - [ ] 94.10.1 SOX Compliance Audit Setup
Filename: `94_10_01_sox_compliance_setup.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: SOX-compliant auditing

- [ ] Required events
- [ ] Retention policies
- [ ] Access controls
- [ ] Reporting requirements

**Expected Behavior**: SOX compliance met

---

### - [ ] 94.10.2 GDPR Audit Trail
Filename: `94_10_02_gdpr_audit_trail.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: GDPR data access auditing

- [ ] Personal data access
- [ ] Right to access support
- [ ] Deletion tracking
- [ ] Consent auditing

**Expected Behavior**: GDPR compliance met

---

### - [ ] 94.10.3 Security Incident Audit
Filename: `94_10_03_security_incident_audit.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Security event tracking

- [ ] Authentication events
- [ ] Authorization failures
- [ ] Suspicious activity
- [ ] Incident response

**Expected Behavior**: Security events tracked

---

### - [ ] 94.10.4 Change Management Audit
Filename: `94_10_04_change_management_audit.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Track all changes

- [ ] Configuration changes
- [ ] DAG modifications
- [ ] Deployment tracking
- [ ] Rollback history

**Expected Behavior**: All changes tracked

---

### - [ ] 94.10.5 Multi-Tenant Audit Setup
Filename: `94_10_05_multi_tenant_audit.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Tenant-isolated auditing

- [ ] Per-tenant audit logs
- [ ] Tenant access control
- [ ] Cross-tenant visibility
- [ ] Tenant reporting

**Expected Behavior**: Tenant-aware auditing

---

# Summary

## Topic Completion Checklist
- [ ] Built-in audit explained
- [ ] DAG/Task audit covered
- [ ] API audit documented
- [ ] External integration included
- [ ] Compliance reporting provided
- [ ] Anti-patterns identified
- [ ] Testing covered
- [ ] Performance optimized
- [ ] Advanced patterns included
- [ ] Real-world examples provided

## Related Topics
- Section 32: Security Auth (access control)
- Section 19: Logging Monitoring (logging basics)
- Section 48: REST API (API auditing)

## Notes for Implementation
- Test with actual audit scenarios
- Show compliance query patterns
- Include retention considerations
- Demonstrate SIEM integration
