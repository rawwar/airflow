# 91 Alerting

## Overview

Alerting in Airflow enables proactive notification when tasks fail, SLAs are missed, or anomalies occur. Airflow 3.x supports callbacks, listeners, and integration with external alerting systems like PagerDuty, Slack, and email.

## Airflow 3.x Notes
- Listeners provide event-driven alerting
- Callbacks remain primary alert mechanism
- SLA callbacks for deadline management
- Integration with observability platforms
- Asset-aware alerting patterns

---

# 91.1 Callback-Based Alerting

## Overview
Using task and DAG callbacks for notifications.

## Tasks

### - [ ] 91.1.1 on_failure_callback Basics
Filename: `91_01_01_on_failure_callback.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Alert on task failure

- [ ] Define on_failure_callback function
- [ ] Context object contents
- [ ] Extract failure information
- [ ] Send notification

**Expected Behavior**: Alert sent on failure

---

### - [ ] 91.1.2 on_success_callback
Filename: `91_01_02_on_success_callback.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Notify on task success

- [ ] Success callback implementation
- [ ] Completion notifications
- [ ] Selective success alerts
- [ ] Milestone tracking

**Expected Behavior**: Success notifications sent

---

### - [ ] 91.1.3 on_retry_callback
Filename: `91_01_03_on_retry_callback.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Alert when tasks retry

- [ ] Retry callback setup
- [ ] Retry count tracking
- [ ] Early warning on flaky tasks
- [ ] Retry pattern detection

**Expected Behavior**: Retry alerts sent

---

### - [ ] 91.1.4 DAG-Level Callbacks
Filename: `91_01_04_dag_level_callbacks.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Callbacks for entire DAG runs

- [ ] on_failure_callback at DAG level
- [ ] on_success_callback at DAG level
- [ ] DAG run context
- [ ] Aggregate failure handling

**Expected Behavior**: DAG-level alerts work

---

### - [ ] 91.1.5 Callback with default_args
Filename: `91_01_05_callback_default_args.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Apply callbacks to all tasks

- [ ] Callbacks in default_args
- [ ] Task-level override
- [ ] Inheritance patterns
- [ ] Centralized alert config

**Expected Behavior**: Callbacks applied globally

---

# 91.2 Email Alerting

## Overview
Configuring email notifications in Airflow.

## Tasks

### - [ ] 91.2.1 Email on Failure Configuration
Filename: `91_02_01_email_on_failure.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure task failure emails

- [ ] email_on_failure parameter
- [ ] email parameter for recipients
- [ ] SMTP configuration
- [ ] Email content customization

**Expected Behavior**: Failure emails sent

---

### - [ ] 91.2.2 Email on Retry
Filename: `91_02_02_email_on_retry.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Email when tasks retry

- [ ] email_on_retry parameter
- [ ] Retry notification templates
- [ ] Rate limiting retries
- [ ] Aggregate retry emails

**Expected Behavior**: Retry emails sent

---

### - [ ] 91.2.3 Custom Email Templates
Filename: `91_02_03_custom_email_templates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Customize email content

- [ ] Jinja2 email templates
- [ ] Including task logs
- [ ] Adding context links
- [ ] HTML vs plain text

**Expected Behavior**: Custom emails rendered

---

### - [ ] 91.2.4 SMTP Configuration
Filename: `91_02_04_smtp_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Set up SMTP for email

- [ ] smtp_host, smtp_port configuration
- [ ] Authentication setup
- [ ] TLS/SSL settings
- [ ] Connection testing

**Expected Behavior**: SMTP working

---

### - [ ] 91.2.5 Email Alerting Best Practices
Filename: `91_02_05_email_best_practices.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Effective email alerting

- [ ] Avoid alert fatigue
- [ ] Grouping related failures
- [ ] Escalation patterns
- [ ] On-call integration

**Expected Behavior**: Effective email strategy

---

# 91.3 Slack and Messaging Integration

## Overview
Integrating with Slack and other messaging platforms.

## Tasks

### - [ ] 91.3.1 SlackWebhookOperator for Alerts
Filename: `91_03_01_slack_webhook_alerts.py` | Tags: `['reference', 'providers', 'beginner', 'success']`

**Purpose**: Send alerts to Slack

- [ ] SlackWebhookOperator in callback
- [ ] Message formatting
- [ ] Channel routing
- [ ] Emoji and attachments

**Expected Behavior**: Slack alerts delivered

---

### - [ ] 91.3.2 Slack Callback Function
Filename: `91_03_02_slack_callback_function.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Reusable Slack callback

- [ ] Generic Slack callback factory
- [ ] Dynamic channel selection
- [ ] Rich message blocks
- [ ] Thread replies

**Expected Behavior**: Flexible Slack alerting

---

### - [ ] 91.3.3 Microsoft Teams Integration
Filename: `91_03_03_teams_integration.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Alert to Microsoft Teams

- [ ] Teams webhook connector
- [ ] Adaptive card format
- [ ] Action buttons
- [ ] Channel selection

**Expected Behavior**: Teams alerts work

---

### - [ ] 91.3.4 Discord Notifications
Filename: `91_03_04_discord_notifications.py` | Tags: `['reference', 'integration', 'intermediate', 'success']`

**Purpose**: Send alerts to Discord

- [ ] Discord webhook setup
- [ ] Embed formatting
- [ ] Mention roles/users
- [ ] Rate limiting

**Expected Behavior**: Discord alerts delivered

---

### - [ ] 91.3.5 Telegram Bot Alerts
Filename: `91_03_05_telegram_alerts.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Telegram bot notifications

- [ ] TelegramOperator for alerts
- [ ] Bot setup and chat_id
- [ ] Markdown formatting
- [ ] Group and channel alerts

**Expected Behavior**: Telegram alerts work

---

# 91.4 PagerDuty and Incident Management

## Overview
Integration with incident management platforms.

## Tasks

### - [ ] 91.4.1 PagerDuty Alert Integration
Filename: `91_04_01_pagerduty_integration.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Trigger PagerDuty incidents

- [ ] PagerDutyEventsHook
- [ ] Incident creation on failure
- [ ] Severity mapping
- [ ] Service integration key

**Expected Behavior**: PagerDuty incidents created

---

### - [ ] 91.4.2 PagerDuty Severity Levels
Filename: `91_04_02_pagerduty_severity.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Map task criticality to severity

- [ ] Critical/Warning/Info levels
- [ ] Task tag-based severity
- [ ] Time-based escalation
- [ ] Business hour routing

**Expected Behavior**: Appropriate severity set

---

### - [ ] 91.4.3 Opsgenie Integration
Filename: `91_04_03_opsgenie_integration.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Alert via Opsgenie

- [ ] OpsgenieAlertOperator
- [ ] Alert priority
- [ ] Team routing
- [ ] Tags and details

**Expected Behavior**: Opsgenie alerts work

---

### - [ ] 91.4.4 Auto-Resolution on Success
Filename: `91_04_04_auto_resolution.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Auto-resolve incidents

- [ ] Resolve incident on retry success
- [ ] Deduplication keys
- [ ] State management
- [ ] Flap detection

**Expected Behavior**: Incidents auto-resolve

---

### - [ ] 91.4.5 Incident Enrichment
Filename: `91_04_05_incident_enrichment.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Rich incident context

- [ ] Add logs URL to incident
- [ ] Include recent DAG history
- [ ] Runbook links
- [ ] Metadata attachment

**Expected Behavior**: Incidents have context

---

# 91.5 SLA and Threshold Alerting

## Overview
Alerting based on SLAs and custom thresholds.

## Tasks

### - [ ] 91.5.1 SLA Miss Callback
Filename: `91_05_01_sla_miss_callback.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Alert when SLA missed

- [ ] sla_miss_callback configuration
- [ ] SLA definition review
- [ ] Callback parameters
- [ ] SLA reporting

**Expected Behavior**: SLA miss alerts sent

---

### - [ ] 91.5.2 Duration Threshold Alerts
Filename: `91_05_02_duration_threshold_alerts.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Alert on slow tasks

- [ ] Measure task duration in callback
- [ ] Threshold comparison
- [ ] Historical baseline
- [ ] Trend alerts

**Expected Behavior**: Slow task alerts

---

### - [ ] 91.5.3 Failure Rate Alerts
Filename: `91_05_03_failure_rate_alerts.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Alert on high failure rates

- [ ] Track failure count
- [ ] Rolling window analysis
- [ ] Rate threshold alerts
- [ ] DAG health scoring

**Expected Behavior**: Failure rate monitored

---

### - [ ] 91.5.4 Data Quality Alerts
Filename: `91_05_04_data_quality_alerts.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Alert on data issues

- [ ] Row count thresholds
- [ ] Schema validation alerts
- [ ] Freshness monitoring
- [ ] Anomaly detection

**Expected Behavior**: Data quality alerts

---

### - [ ] 91.5.5 Multi-DAG Alert Aggregation
Filename: `91_05_05_multi_dag_aggregation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Aggregate alerts across DAGs

- [ ] Cross-DAG failure correlation
- [ ] System-wide health alerts
- [ ] Pipeline group monitoring
- [ ] Alert deduplication

**Expected Behavior**: Holistic alerting

---

# 91.6 Advanced Alerting Patterns

## Overview
Sophisticated alerting patterns for complex scenarios.

## Tasks

### - [ ] 91.6.1 Alert Correlation
Filename: `91_06_01_alert_correlation.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Correlate related alerts

- [ ] Group related task failures
- [ ] Identify root cause alerts
- [ ] Suppress downstream alerts
- [ ] Alert chain analysis

**Expected Behavior**: Related alerts grouped

---

### - [ ] 91.6.2 Alert Rate Limiting
Filename: `91_06_02_alert_rate_limiting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Prevent alert storms

- [ ] Throttle repeated alerts
- [ ] Time-window suppression
- [ ] Digest/summary alerts
- [ ] Cooldown periods

**Expected Behavior**: Alert storms prevented

---

### - [ ] 91.6.3 Context-Aware Alerting
Filename: `91_06_03_context_aware_alerting.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Alerts with rich context

- [ ] Include upstream task status
- [ ] Add data lineage info
- [ ] Recent run history
- [ ] Related DAG status

**Expected Behavior**: Alerts have full context

---

### - [ ] 91.6.4 Business Hours Alerting
Filename: `91_06_04_business_hours_alerting.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Time-based alert routing

- [ ] On-call schedule integration
- [ ] Weekend/holiday handling
- [ ] Timezone-aware routing
- [ ] Escalation after hours

**Expected Behavior**: Alerts routed by time

---

### - [ ] 91.6.5 Alert Deduplication
Filename: `91_06_05_alert_deduplication.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Prevent duplicate alerts

- [ ] Deduplication key generation
- [ ] Window-based dedup
- [ ] State tracking
- [ ] Dedup across retries

**Expected Behavior**: No duplicate alerts

---

# 91.7 Alerting Anti-Patterns

## Overview
Common alerting mistakes to avoid.

## Tasks

### - [ ] 91.7.1 Alert Fatigue Anti-Pattern
Filename: `91_07_01_alert_fatigue_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Avoid alert overload

- [ ] Show excessive alerting
- [ ] Demonstrate ignored alerts
- [ ] Provide filtering strategies
- [ ] Include priority-based alerting

**Expected Behavior**: Understand alert fatigue

---

### - [ ] 91.7.2 Missing Context Anti-Pattern
Filename: `91_07_02_missing_context_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Alerts without useful info

- [ ] Show bare-bones alerts
- [ ] Demonstrate debugging difficulty
- [ ] Provide context enrichment
- [ ] Include runbook links

**Expected Behavior**: Context-rich alerts

---

### - [ ] 91.7.3 Hardcoded Recipients Anti-Pattern
Filename: `91_07_03_hardcoded_recipients_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Inflexible alert routing

- [ ] Show hardcoded emails
- [ ] Demonstrate maintenance issues
- [ ] Provide dynamic routing
- [ ] Include configuration-based routing

**Expected Behavior**: Flexible recipients

---

### - [ ] 91.7.4 No Acknowledgment Anti-Pattern
Filename: `91_07_04_no_ack_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Alerts without tracking

- [ ] Show untracked alerts
- [ ] Demonstrate repeated alerts
- [ ] Provide ack mechanism
- [ ] Include incident tracking

**Expected Behavior**: Alerts tracked properly

---

### - [ ] 91.7.5 Alerting on Expected Failures
Filename: `91_07_05_expected_failures_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Avoid noise from known issues

- [ ] Show alerts for known failures
- [ ] Demonstrate alert noise
- [ ] Provide maintenance windows
- [ ] Include conditional alerting

**Expected Behavior**: Only unexpected alerts

---

# 91.8 Testing Alerting

## Overview
Testing alert configurations and delivery.

## Tasks

### - [ ] 91.8.1 Unit Testing Callbacks
Filename: `91_08_01_unit_testing_callbacks.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test callback functions

- [ ] Mock context object
- [ ] Test callback logic
- [ ] Verify alert content
- [ ] Assert side effects

**Expected Behavior**: Callbacks tested

---

### - [ ] 91.8.2 Integration Testing Alerts
Filename: `91_08_02_integration_testing_alerts.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test end-to-end alerting

- [ ] Test with mock services
- [ ] Verify delivery
- [ ] Test failure scenarios
- [ ] Check formatting

**Expected Behavior**: Alert delivery tested

---

### - [ ] 91.8.3 Alert Dry Run Mode
Filename: `91_08_03_alert_dry_run.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test without sending

- [ ] Dry run configuration
- [ ] Log alert content
- [ ] Validate without delivery
- [ ] Development mode

**Expected Behavior**: Safe alert testing

---

### - [ ] 91.8.4 Alert Simulation
Filename: `91_08_04_alert_simulation.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Trigger test alerts

- [ ] Manual alert triggers
- [ ] Simulate failures
- [ ] Test escalation
- [ ] Verify routing

**Expected Behavior**: Alerts simulatable

---

### - [ ] 91.8.5 Alert Content Validation
Filename: `91_08_05_alert_content_validation.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Validate alert format

- [ ] Schema validation
- [ ] Required fields check
- [ ] Format verification
- [ ] Link validation

**Expected Behavior**: Alert content correct

---

# 91.9 Performance and Reliability

## Overview
Ensuring alerts are delivered reliably.

## Tasks

### - [ ] 91.9.1 Async Alert Delivery
Filename: `91_09_01_async_alert_delivery.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Non-blocking alerts

- [ ] Async callback execution
- [ ] Queue-based delivery
- [ ] Background processing
- [ ] Task timeout handling

**Expected Behavior**: Alerts don't block tasks

---

### - [ ] 91.9.2 Alert Retry Logic
Filename: `91_09_02_alert_retry_logic.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle delivery failures

- [ ] Retry on failure
- [ ] Exponential backoff
- [ ] Max retry limits
- [ ] Fallback channels

**Expected Behavior**: Alerts eventually delivered

---

### - [ ] 91.9.3 Alert Queue Management
Filename: `91_09_03_alert_queue_management.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Manage alert queues

- [ ] Queue persistence
- [ ] Priority queuing
- [ ] Queue monitoring
- [ ] Dead letter handling

**Expected Behavior**: Reliable queue processing

---

### - [ ] 91.9.4 Failover Alert Channels
Filename: `91_09_04_failover_channels.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Backup alert delivery

- [ ] Primary/secondary channels
- [ ] Automatic failover
- [ ] Channel health checks
- [ ] Multi-channel delivery

**Expected Behavior**: Alerts always delivered

---

### - [ ] 91.9.5 Alert Delivery Monitoring
Filename: `91_09_05_alert_delivery_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Monitor alert system

- [ ] Delivery success metrics
- [ ] Latency tracking
- [ ] Failure alerting
- [ ] Dashboard for alerts

**Expected Behavior**: Alert system monitored

---

# 91.10 Real-World Examples

## Overview
Complete alerting implementations for common scenarios.

## Tasks

### - [ ] 91.10.1 Data Pipeline Alerting
Filename: `91_10_01_data_pipeline_alerting.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Complete ETL alerting setup

- [ ] Extract failure alerts
- [ ] Transform validation alerts
- [ ] Load completion alerts
- [ ] Pipeline SLA alerts

**Expected Behavior**: Full pipeline alerting

---

### - [ ] 91.10.2 ML Pipeline Alerting
Filename: `91_10_02_ml_pipeline_alerting.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: ML workflow alerts

- [ ] Training failure alerts
- [ ] Model drift alerts
- [ ] Deployment alerts
- [ ] Performance degradation

**Expected Behavior**: ML pipeline monitored

---

### - [ ] 91.10.3 Multi-Team Alerting Setup
Filename: `91_10_03_multi_team_alerting.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Enterprise alerting

- [ ] Team-based routing
- [ ] Centralized config
- [ ] Cross-team escalation
- [ ] On-call integration

**Expected Behavior**: Enterprise-ready alerting

---

### - [ ] 91.10.4 Cost-Based Alerting
Filename: `91_10_04_cost_based_alerting.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Alert on cost anomalies

- [ ] Budget threshold alerts
- [ ] Cost spike detection
- [ ] Resource waste alerts
- [ ] Forecast alerts

**Expected Behavior**: Cost monitoring active

---

### - [ ] 91.10.5 Compliance Alerting
Filename: `91_10_05_compliance_alerting.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Regulatory compliance

- [ ] SLA breach alerts
- [ ] Data quality alerts
- [ ] Audit requirement alerts
- [ ] Security incident alerts

**Expected Behavior**: Compliance monitored

---

# Summary

## Topic Completion Checklist
- [ ] Callback alerting explained
- [ ] Email configuration covered
- [ ] Slack/Teams integration documented
- [ ] Incident management included
- [ ] SLA alerting provided
- [ ] Advanced patterns documented
- [ ] Anti-patterns identified
- [ ] Testing covered
- [ ] Performance addressed
- [ ] Real-world examples included

## Related Topics
- Section 12: Callbacks Notifications (callback basics)
- Section 61: SLA Management (SLA configuration)
- Section 90: Metrics (metrics-based alerts)

## Notes for Implementation
- Test with mock notification services
- Show callback context usage
- Include rate limiting patterns
- Demonstrate alert deduplication
