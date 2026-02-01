# 120 - Human-in-the-Loop Workflows

## Overview
Implementing human approval workflows in Airflow 3.x, enabling manual intervention points, approval gates, and interactive decision-making within automated pipelines.

---

## Section 1: Manual Approval Tasks

### - [ ] 120.1.1 Manual Approval Basics
Filename: `120_01_01_approval_basics.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand human-in-the-loop concepts
- [ ] Identify use cases for manual approval
- [ ] Review approval task patterns
- [ ] Compare approval mechanisms

### - [ ] 120.1.2 Pause and Resume Pattern
Filename: `120_01_02_pause_resume.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Implement task that waits for approval
- [ ] Use reschedule mode for waiting
- [ ] Handle approval state persistence
- [ ] Configure timeout for approvals

### - [ ] 120.1.3 Approval State Management
Filename: `120_01_03_approval_state.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Store approval status externally
- [ ] Track approver identity
- [ ] Record approval timestamp
- [ ] Handle approval audit trail

### - [ ] 120.1.4 Multi-Level Approvals
Filename: `120_01_04_multi_level.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement sequential approval chain
- [ ] Configure parallel approvals
- [ ] Handle majority/unanimous voting
- [ ] Track approval progress

### - [ ] 120.1.5 Approval Timeout Handling
Filename: `120_01_05_approval_timeout.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Configure approval deadlines
- [ ] Implement timeout escalation
- [ ] Handle auto-rejection on timeout
- [ ] Send reminder notifications

---

## Section 2: External Task Sensors for Approval

### - [ ] 120.2.1 External Signal Sensor
Filename: `120_02_01_external_signal.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Use ExternalTaskSensor for approvals
- [ ] Configure external DAG/task to wait for
- [ ] Handle approval via manual trigger
- [ ] Implement timeout and poke interval

### - [ ] 120.2.2 File-Based Approval Gate
Filename: `120_02_02_file_approval.py` | Tags: `['reference', 'patterns', 'beginner', 'success']`
- [ ] Wait for approval file creation
- [ ] Use FileSensor for approval detection
- [ ] Parse approval metadata from file
- [ ] Handle cleanup after approval

### - [ ] 120.2.3 Database Approval Sensor
Filename: `120_02_03_db_approval.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Poll database for approval record
- [ ] Use SqlSensor for approval check
- [ ] Handle approval with conditions
- [ ] Track sensor polling metrics

### - [ ] 120.2.4 API-Based Approval Sensor
Filename: `120_02_04_api_approval.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Check external API for approval
- [ ] Use HttpSensor for polling
- [ ] Handle API authentication
- [ ] Parse approval response data

### - [ ] 120.2.5 Asset-Based Approval Pattern
Filename: `120_02_05_asset_approval.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Use Asset events for approvals
- [ ] Trigger approval via Asset update
- [ ] Handle approval metadata in event
- [ ] Chain approval-dependent DAGs

---

## Section 3: Callback-Based Approvals

### - [ ] 120.3.1 Webhook Approval Callback
Filename: `120_03_01_webhook_callback.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Expose webhook for approval submission
- [ ] Validate approval webhook payload
- [ ] Update task state on callback
- [ ] Secure webhook endpoint

### - [ ] 120.3.2 Slack Approval Integration
Filename: `120_03_02_slack_approval.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Send approval request to Slack
- [ ] Handle Slack interactive buttons
- [ ] Process approval/rejection response
- [ ] Update workflow on Slack action

### - [ ] 120.3.3 Email Approval Links
Filename: `120_03_03_email_approval.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Send approval email with action links
- [ ] Generate secure approval tokens
- [ ] Handle click-to-approve flow
- [ ] Expire approval links

### - [ ] 120.3.4 Teams/Chat Approval
Filename: `120_03_04_teams_approval.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Integrate with Microsoft Teams
- [ ] Send adaptive cards for approval
- [ ] Handle Teams action responses
- [ ] Track chat-based approvals

### - [ ] 120.3.5 Custom Approval Service
Filename: `120_03_05_custom_approval.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Build approval microservice
- [ ] Integrate with Airflow API
- [ ] Handle complex approval logic
- [ ] Support custom approval UIs

---

## Section 4: UI-Triggered Actions

### - [ ] 120.4.1 Manual Task Trigger
Filename: `120_04_01_manual_trigger.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Trigger DAGs manually from UI
- [ ] Pass approval parameters via conf
- [ ] Handle manual run identification
- [ ] Track manual vs scheduled runs

### - [ ] 120.4.2 Task Instance Manipulation
Filename: `120_04_02_task_manipulation.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Mark task as success from UI
- [ ] Clear task to force re-run
- [ ] Handle downstream effects
- [ ] Audit UI-based changes

### - [ ] 120.4.3 DAG Run State Management
Filename: `120_04_03_dagrun_state.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Pause DAG run for review
- [ ] Resume paused DAG runs
- [ ] Mark DAG run as failed
- [ ] Handle partial completion

### - [ ] 120.4.4 UI Confirmation Dialogs
Filename: `120_04_04_confirmation_dialogs.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Implement confirmation for destructive actions
- [ ] Require reason for manual changes
- [ ] Track confirmation audit trail
- [ ] Handle confirmation timeout

### - [ ] 120.4.5 Custom UI Extensions
Filename: `120_04_05_custom_ui.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Build custom approval views
- [ ] Integrate with Airflow plugins
- [ ] Display approval forms
- [ ] Handle custom action buttons

---

## Section 5: Approval Workflow Patterns

### - [ ] 120.5.1 Gate-Based Approval Pattern
Filename: `120_05_01_gate_pattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Design approval gate tasks
- [ ] Position gates between phases
- [ ] Handle gate bypass options
- [ ] Track gate passage metrics

### - [ ] 120.5.2 Review and Approve Pattern
Filename: `120_05_02_review_approve.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Generate review artifacts
- [ ] Wait for human review
- [ ] Capture review feedback
- [ ] Proceed based on approval

### - [ ] 120.5.3 Conditional Approval Branching
Filename: `120_05_03_conditional_branching.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Branch based on approval type
- [ ] Handle approve/reject/defer paths
- [ ] Implement conditional downstream
- [ ] Track branch outcomes

### - [ ] 120.5.4 Approval with Data Input
Filename: `120_05_04_approval_with_data.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Collect data during approval
- [ ] Handle form-based input
- [ ] Validate approval data
- [ ] Use input in downstream tasks

### - [ ] 120.5.5 Rollback on Rejection
Filename: `120_05_05_rollback_rejection.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement rollback tasks
- [ ] Trigger rollback on rejection
- [ ] Handle partial rollback
- [ ] Track rollback status

---

## Section 6: Pause/Resume & Escalation

### - [ ] 120.6.1 DAG Pause Mechanisms
Filename: `120_06_01_dag_pause.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Pause DAG via UI/API
- [ ] Handle in-flight tasks on pause
- [ ] Resume DAG execution
- [ ] Track pause history

### - [ ] 120.6.2 Task-Level Pause
Filename: `120_06_02_task_pause.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Implement task that pauses workflow
- [ ] Store pause state externally
- [ ] Resume via external signal
- [ ] Handle pause timeouts

### - [ ] 120.6.3 Escalation on No Response
Filename: `120_06_03_escalation.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Detect stalled approvals
- [ ] Escalate to secondary approvers
- [ ] Configure escalation thresholds
- [ ] Track escalation chain

### - [ ] 120.6.4 Manager Escalation Pattern
Filename: `120_06_04_manager_escalation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Define approval hierarchy
- [ ] Auto-escalate up chain
- [ ] Handle skip-level approvals
- [ ] Configure escalation policies

### - [ ] 120.6.5 SLA-Driven Escalation
Filename: `120_06_05_sla_escalation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure approval SLAs
- [ ] Trigger escalation on SLA breach
- [ ] Send SLA warning notifications
- [ ] Track SLA compliance metrics

---

## Section 7: Human-in-the-Loop Anti-Patterns

### - [ ] 120.7.1 No Approval Timeout
Filename: `120_07_01_no_timeout_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Indefinite workflow blocking
- [ ] Resource waste
- [ ] Timeout configuration
- [ ] Escalation setup

### - [ ] 120.7.2 Blocking Without Deferral
Filename: `120_07_02_blocking_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Worker slot consumption
- [ ] Resource exhaustion
- [ ] Deferrable patterns
- [ ] Reschedule mode

### - [ ] 120.7.3 No Audit Trail
Filename: `120_07_03_no_audit_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Missing accountability
- [ ] Compliance issues
- [ ] Audit logging
- [ ] Decision tracking

### - [ ] 120.7.4 Hard-Coded Approvers
Filename: `120_07_04_hardcoded_approvers_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Inflexible routing
- [ ] Personnel changes break flow
- [ ] Dynamic approver resolution
- [ ] Role-based approval

### - [ ] 120.7.5 No Notification Delivery Tracking
Filename: `120_07_05_no_tracking_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Undelivered notifications
- [ ] Silent approval requests
- [ ] Delivery confirmation
- [ ] Retry notifications

---

## Section 8: Testing Human-in-the-Loop Workflows

### - [ ] 120.8.1 Unit Testing Approval Logic
Filename: `120_08_01_unit_testing_approval.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test approval state transitions
- [ ] Validate escalation logic
- [ ] Test timeout handling
- [ ] Mock approval responses

### - [ ] 120.8.2 Integration Testing Approval Flow
Filename: `120_08_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] End-to-end approval testing
- [ ] Test notification delivery
- [ ] Validate state persistence
- [ ] Test callback handling

### - [ ] 120.8.3 Testing Notification Integrations
Filename: `120_08_03_notification_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test Slack integration
- [ ] Test email delivery
- [ ] Validate payload format
- [ ] Test action handling

### - [ ] 120.8.4 Testing Escalation Paths
Filename: `120_08_04_escalation_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test timeout escalation
- [ ] Validate escalation chain
- [ ] Test manager notification
- [ ] Multi-level escalation

### - [ ] 120.8.5 Testing Concurrent Approvals
Filename: `120_08_05_concurrent_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Multiple pending approvals
- [ ] Race condition handling
- [ ] State consistency
- [ ] Load testing approvals

---

## Section 9: Approval Performance and Reliability

### - [ ] 120.9.1 Minimizing Approval Latency
Filename: `120_09_01_minimize_latency.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Fast notification delivery
- [ ] Responsive approval interface
- [ ] State update optimization
- [ ] Polling vs push notifications

### - [ ] 120.9.2 High-Availability Approval System
Filename: `120_09_02_high_availability.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Redundant notification paths
- [ ] Database reliability
- [ ] Failover handling
- [ ] State persistence

### - [ ] 120.9.3 Scaling Approval Workflows
Filename: `120_09_03_scaling_approvals.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] High-volume approval handling
- [ ] Parallel approval processing
- [ ] Queue management
- [ ] Resource allocation

### - [ ] 120.9.4 Approval State Management
Filename: `120_09_04_state_management.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Efficient state storage
- [ ] State cleanup
- [ ] Orphan approval handling
- [ ] State consistency

### - [ ] 120.9.5 Approval Metrics and Monitoring
Filename: `120_09_05_metrics_monitoring.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Approval latency tracking
- [ ] Pending approval alerts
- [ ] SLA monitoring
- [ ] Dashboard creation

---

## Section 10: Real-World Human-in-the-Loop Examples

### - [ ] 120.10.1 Data Pipeline Quality Gate
Filename: `120_10_01_quality_gate.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Data quality review
- [ ] Approval before production load
- [ ] Rollback on rejection
- [ ] Quality metrics display

### - [ ] 120.10.2 Deployment Approval Workflow
Filename: `120_10_02_deployment_approval.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Pre-deployment approval
- [ ] Change review
- [ ] Staged deployment
- [ ] Emergency bypass

### - [ ] 120.10.3 Financial Transaction Approval
Filename: `120_10_03_financial_approval.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Amount-based routing
- [ ] Multi-level approval
- [ ] Compliance requirements
- [ ] Audit trail

### - [ ] 120.10.4 Content Moderation Pipeline
Filename: `120_10_04_content_moderation.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Automated flagging
- [ ] Human review queue
- [ ] Action handling
- [ ] Feedback loop

### - [ ] 120.10.5 ML Model Approval Workflow
Filename: `120_10_05_ml_model_approval.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Model performance review
- [ ] A/B test approval
- [ ] Production deployment gate
- [ ] Rollback capability

---

# Summary

## Topic Completion Checklist
- [ ] Manual approval tasks covered
- [ ] External sensors explained
- [ ] Callback-based approvals documented
- [ ] UI-triggered actions addressed
- [ ] Approval workflow patterns included
- [ ] Pause/resume and escalation documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance and reliability addressed
- [ ] Real-world examples provided

## Related Topics
- Section 08: Sensors
- Section 107: DAG Triggers
- Section 77: Email Operators
- Section 91: Alerting

## Notes for Implementation
- Always set approval timeouts
- Use deferrable patterns for waiting
- Implement comprehensive audit trail
- Plan escalation paths
- Test notification delivery
