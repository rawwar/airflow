# 77 Email Operators

## Overview

Email operators enable sending notifications, reports, and alerts from Airflow workflows. This section covers EmailOperator configuration, SMTP setup, HTML templates, attachments, and integration with notification callbacks for Airflow 3.x.

## Research & Background

### Key Concepts
- **EmailOperator**: Sends email from task execution
- **SMTP Configuration**: Server settings for email delivery
- **Email Callbacks**: Automatic emails on task state changes
- **HTML Templates**: Rich email content formatting
- **Attachments**: File attachments in emails

### Airflow 3.x Features
- Improved email templating
- Better attachment handling
- Enhanced SMTP configuration
- Integration with notification callbacks
- Jinja templating in email content

### Prerequisites
- Airflow 3.x with email configuration
- SMTP server access
- Understanding of Airflow callbacks (Section 12)

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Configure SMTP for email delivery
2. Send emails from tasks with attachments
3. Create HTML email templates
4. Set up automatic failure/success notifications
5. Build custom email notification systems

---

# 77.1 Email Configuration

## Overview
Setting up email infrastructure in Airflow.

## Tasks

### - [ ] 77.1.1 SMTP Configuration
Filename: `77_01_01_smtp_configuration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure SMTP settings

- [ ] airflow.cfg [smtp] section
- [ ] smtp_host and smtp_port
- [ ] smtp_user and smtp_password
- [ ] smtp_starttls and smtp_ssl

**Expected Behavior**: Email delivery works

---

### - [ ] 77.1.2 Email Connection Setup
Filename: `77_01_02_email_connection.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use Airflow connections for email

- [ ] Create smtp:// connection
- [ ] Connection parameters
- [ ] Test connection
- [ ] Multiple email configurations

**Expected Behavior**: Connection-based email works

---

### - [ ] 77.1.3 Default Email Settings
Filename: `77_01_03_default_email_settings.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Configure default email behavior

- [ ] smtp_mail_from setting
- [ ] email_backend configuration
- [ ] Default subject prefix
- [ ] Timeout settings

**Expected Behavior**: Defaults applied consistently

---

### - [ ] 77.1.4 Email Backend Selection
Filename: `77_01_04_email_backend.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Choose email sending backend

- [ ] Default SMTP backend
- [ ] SendGrid backend
- [ ] SES backend
- [ ] Custom backend implementation

**Expected Behavior**: Correct backend used

---

### - [ ] 77.1.5 Testing Email Configuration
Filename: `77_01_05_testing_email.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Verify email setup

- [ ] CLI email test command
- [ ] Debug email issues
- [ ] Check SMTP logs
- [ ] Common configuration errors

**Expected Behavior**: Email delivery verified

---

# 77.2 EmailOperator Usage

## Overview
Sending emails from DAG tasks.

## Tasks

### - [ ] 77.2.1 Basic EmailOperator
Filename: `77_02_01_basic_email_operator.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Send simple email from task

- [ ] Import EmailOperator
- [ ] Set to, subject, html_content
- [ ] Plain text content
- [ ] Multiple recipients

**Expected Behavior**: Email sent successfully

---

### - [ ] 77.2.2 HTML Email Content
Filename: `77_02_02_html_email_content.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create rich HTML emails

- [ ] html_content parameter
- [ ] Basic HTML formatting
- [ ] Inline styles
- [ ] Email client compatibility

**Expected Behavior**: HTML email renders correctly

---

### - [ ] 77.2.3 Email Attachments
Filename: `77_02_03_email_attachments.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Attach files to emails

- [ ] files parameter for attachments
- [ ] Multiple file attachments
- [ ] File path resolution
- [ ] MIME type handling

**Expected Behavior**: Attachments included

---

### - [ ] 77.2.4 Templated Email Content
Filename: `77_02_04_templated_email.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use Jinja in email content

- [ ] Template macros in subject
- [ ] Template in html_content
- [ ] Access context variables
- [ ] Dynamic email generation

**Expected Behavior**: Templates rendered correctly

---

### - [ ] 77.2.5 CC and BCC Recipients
Filename: `77_02_05_cc_bcc_recipients.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Add CC/BCC to emails

- [ ] cc parameter
- [ ] bcc parameter
- [ ] Multiple CC/BCC recipients
- [ ] Reply-to configuration

**Expected Behavior**: CC/BCC recipients receive email

---

# 77.3 Email Templates and Formatting

## Overview
Creating reusable email templates.

## Tasks

### - [ ] 77.3.1 External HTML Templates
Filename: `77_03_01_external_templates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Use external template files

- [ ] Template file location
- [ ] Load and render templates
- [ ] Template inheritance
- [ ] Pass variables to templates

**Expected Behavior**: External templates work

---

### - [ ] 77.3.2 Task Execution Report Template
Filename: `77_03_02_execution_report.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Standard execution report email

- [ ] Task details in email
- [ ] Execution time and status
- [ ] Log links
- [ ] Error details if failed

**Expected Behavior**: Comprehensive report generated

---

### - [ ] 77.3.3 Data Quality Report Email
Filename: `77_03_03_data_quality_report.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Email data validation results

- [ ] Quality check summary
- [ ] Failed checks highlighted
- [ ] Statistics and metrics
- [ ] Actionable recommendations

**Expected Behavior**: Quality report delivered

---

### - [ ] 77.3.4 Pipeline Summary Email
Filename: `77_03_04_pipeline_summary.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: End-of-DAG summary email

- [ ] All task statuses
- [ ] Total execution time
- [ ] Key metrics extracted
- [ ] Links to dashboards

**Expected Behavior**: Summary email sent at DAG end

---

### - [ ] 77.3.5 Scheduled Report Distribution
Filename: `77_03_05_scheduled_reports.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Regular email report distribution

- [ ] Generate report data
- [ ] Format as table/chart
- [ ] Attach as PDF/Excel
- [ ] Distribution list management

**Expected Behavior**: Reports distributed on schedule

---

# 77.4 Callback-Based Notifications

## Overview
Automatic email notifications on task events.

## Tasks

### - [ ] 77.4.1 Email on Failure
Filename: `77_04_01_email_on_failure.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Automatic failure notification

- [ ] email_on_failure=True
- [ ] Default failure email format
- [ ] Customize failure recipients
- [ ] DAG-level vs task-level

**Expected Behavior**: Failure triggers email

---

### - [ ] 77.4.2 Email on Retry
Filename: `77_04_02_email_on_retry.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Notification on task retry

- [ ] email_on_retry=True
- [ ] Retry count in email
- [ ] Distinguish retry from failure
- [ ] When to use retry notifications

**Expected Behavior**: Retry triggers email

---

### - [ ] 77.4.3 Email on Success
Filename: `77_04_03_email_on_success.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Success notification email

- [ ] Custom success callback with email
- [ ] Selective success notifications
- [ ] Include execution metrics
- [ ] Avoid email fatigue

**Expected Behavior**: Success email sent

---

### - [ ] 77.4.4 Custom Email Callbacks
Filename: `77_04_04_custom_email_callbacks.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Build custom notification logic

- [ ] on_failure_callback with email
- [ ] on_success_callback with email
- [ ] Access context for details
- [ ] Conditional email sending

**Expected Behavior**: Custom callback emails work

---

### - [ ] 77.4.5 SLA Miss Emails
Filename: `77_04_05_sla_miss_emails.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Email on SLA violations

- [ ] sla_miss_callback configuration
- [ ] Default SLA email behavior
- [ ] Customize SLA notifications
- [ ] Include SLA details

**Expected Behavior**: SLA miss triggers email

---

# 77.5 Advanced Email Patterns

## Overview
Complex email notification scenarios.

## Tasks

### - [ ] 77.5.1 Aggregated Failure Notifications
Filename: `77_05_01_aggregated_failures.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Batch multiple failures into one email

- [ ] Collect failures in DAG run
- [ ] Send single summary email
- [ ] Reduce email volume
- [ ] Clear failure overview

**Expected Behavior**: One email for multiple failures

---

### - [ ] 77.5.2 Dynamic Recipient Selection
Filename: `77_05_02_dynamic_recipients.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Route emails based on context

- [ ] Determine recipients at runtime
- [ ] Based on task or error type
- [ ] Team routing rules
- [ ] Escalation patterns

**Expected Behavior**: Correct team receives email

---

### - [ ] 77.5.3 Email Throttling
Filename: `77_05_03_email_throttling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Prevent email flooding

- [ ] Rate limiting logic
- [ ] Deduplicate similar errors
- [ ] Cooldown periods
- [ ] Digest mode

**Expected Behavior**: Email volume controlled

---

### - [ ] 77.5.4 Email with External Services
Filename: `77_05_04_external_email_services.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Use external email APIs

- [ ] SendGrid operator
- [ ] AWS SES operator
- [ ] Mailgun integration
- [ ] Compare to SMTP

**Expected Behavior**: External service sends email

---

### - [ ] 77.5.5 Email Debugging and Logging
Filename: `77_05_05_email_debugging.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

**Purpose**: Troubleshoot email issues

- [ ] Email send failures
- [ ] SMTP authentication errors
- [ ] Connection timeouts
- [ ] Log email activity

**Expected Behavior**: Email issues diagnosed

---

# 77.6 Anti-Patterns and Common Mistakes

## Overview
Avoiding email notification pitfalls.

## Tasks

### - [ ] 77.6.1 Email Flooding Anti-Pattern
Filename: `77_06_01_email_flooding.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Prevent email overload

- [ ] Emails on every task failure
- [ ] No deduplication logic
- [ ] Missing rate limiting
- [ ] Alert fatigue consequences

**Expected Behavior**: Understand flooding risks

---

### - [ ] 77.6.2 Hardcoded Recipients Anti-Pattern
Filename: `77_06_02_hardcoded_recipients.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`

**Purpose**: Avoid static recipient lists

- [ ] Hardcoded email addresses
- [ ] No environment separation
- [ ] Missing team routing
- [ ] Maintenance overhead

**Expected Behavior**: Dynamic recipients preferred

---

### - [ ] 77.6.3 Large Attachment Problems
Filename: `77_06_03_large_attachments.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle attachment size limits

- [ ] SMTP size limits
- [ ] Memory issues with large files
- [ ] Link instead of attach
- [ ] Compression strategies

**Expected Behavior**: Attachment sizes managed

---

### - [ ] 77.6.4 Missing Error Handling
Filename: `77_06_04_missing_error_handling.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Handle email failures gracefully

- [ ] SMTP connection failures
- [ ] Authentication errors
- [ ] Failing silently
- [ ] Fallback strategies

**Expected Behavior**: Email errors handled

---

### - [ ] 77.6.5 Sensitive Data in Emails
Filename: `77_06_05_sensitive_data_emails.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`

**Purpose**: Avoid exposing sensitive info

- [ ] Credentials in email body
- [ ] Full stack traces
- [ ] Customer data exposure
- [ ] Secure logging alternatives

**Expected Behavior**: Sensitive data protected

---

# 77.7 Testing Email Functionality

## Overview
Testing email operators and notifications.

## Tasks

### - [ ] 77.7.1 Local SMTP Testing with MailHog
Filename: `77_07_01_mailhog_testing.py` | Tags: `['reference', 'testing', 'beginner', 'success']`

**Purpose**: Test emails locally

- [ ] MailHog setup
- [ ] Docker Compose integration
- [ ] API for email verification
- [ ] Web UI inspection

**Expected Behavior**: Local email testing works

---

### - [ ] 77.7.2 Unit Testing Email Templates
Filename: `77_07_02_unit_testing_templates.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test template rendering

- [ ] Render templates in tests
- [ ] Validate HTML structure
- [ ] Check variable substitution
- [ ] Test edge cases

**Expected Behavior**: Templates tested

---

### - [ ] 77.7.3 Mocking EmailOperator
Filename: `77_07_03_mocking_email_operator.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test without sending emails

- [ ] Mock SMTP connection
- [ ] Verify email parameters
- [ ] Test callback triggers
- [ ] Assert email content

**Expected Behavior**: Email logic tested without sending

---

### - [ ] 77.7.4 Integration Testing Email Flow
Filename: `77_07_04_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: End-to-end email tests

- [ ] Trigger email via DAG
- [ ] Verify delivery
- [ ] Check content accuracy
- [ ] Test failure notifications

**Expected Behavior**: Full email flow tested

---

### - [ ] 77.7.5 Email Deliverability Testing
Filename: `77_07_05_deliverability_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`

**Purpose**: Ensure emails reach recipients

- [ ] SPF/DKIM configuration
- [ ] Spam score checking
- [ ] Domain reputation
- [ ] Test with real providers

**Expected Behavior**: Deliverability verified

---

# 77.8 Performance and Reliability

## Overview
Ensuring email notifications are reliable.

## Tasks

### - [ ] 77.8.1 Async Email Sending
Filename: `77_08_01_async_email_sending.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Send emails without blocking

- [ ] Decouple email from task
- [ ] Queue-based sending
- [ ] Background processing
- [ ] Task completion speed

**Expected Behavior**: Tasks not blocked by email

---

### - [ ] 77.8.2 Email Queue Management
Filename: `77_08_02_email_queue_management.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Manage email sending queue

- [ ] Queue for outbound emails
- [ ] Retry failed sends
- [ ] Priority handling
- [ ] Queue monitoring

**Expected Behavior**: Emails queued reliably

---

### - [ ] 77.8.3 SMTP Connection Pooling
Filename: `77_08_03_smtp_connection_pooling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`

**Purpose**: Reuse SMTP connections

- [ ] Connection pool setup
- [ ] Reduce connection overhead
- [ ] Handle connection drops
- [ ] Pool size tuning

**Expected Behavior**: SMTP connections efficient

---

### - [ ] 77.8.4 Failover Email Providers
Filename: `77_08_04_failover_providers.py` | Tags: `['reference', 'reliability', 'advanced', 'success']`

**Purpose**: Handle provider failures

- [ ] Multiple SMTP backends
- [ ] Automatic failover logic
- [ ] Provider health checks
- [ ] Graceful degradation

**Expected Behavior**: Emails sent despite failures

---

### - [ ] 77.8.5 Email Delivery Monitoring
Filename: `77_08_05_delivery_monitoring.py` | Tags: `['reference', 'reliability', 'intermediate', 'success']`

**Purpose**: Track email delivery success

- [ ] Track sent/failed counts
- [ ] Delivery confirmation
- [ ] Bounce handling
- [ ] Metrics and alerting

**Expected Behavior**: Delivery tracked

---

# 77.9 Best Practices

## Overview
Email notification best practices.

## Tasks

### - [ ] 77.9.1 Email Content Best Practices
Filename: `77_09_01_content_best_practices.py` | Tags: `['reference', 'best-practice', 'beginner', 'success']`

**Purpose**: Write effective notification emails

- [ ] Clear subject lines
- [ ] Actionable content
- [ ] Essential info only
- [ ] Mobile-friendly formatting

**Expected Behavior**: Emails effective and readable

---

### - [ ] 77.9.2 Notification Strategy Design
Filename: `77_09_02_notification_strategy.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Design notification approach

- [ ] Define notification levels
- [ ] Recipient mapping
- [ ] Escalation paths
- [ ] Notification policies

**Expected Behavior**: Strategy documented

---

### - [ ] 77.9.3 Template Organization
Filename: `77_09_03_template_organization.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Organize email templates

- [ ] Centralized template location
- [ ] Base template inheritance
- [ ] Version control for templates
- [ ] Template documentation

**Expected Behavior**: Templates well organized

---

### - [ ] 77.9.4 Recipient Management
Filename: `77_09_04_recipient_management.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Manage email recipients effectively

- [ ] Distribution list usage
- [ ] Role-based recipients
- [ ] On-call integration
- [ ] Unsubscribe handling

**Expected Behavior**: Recipients managed properly

---

### - [ ] 77.9.5 Alert Fatigue Prevention
Filename: `77_09_05_alert_fatigue_prevention.py` | Tags: `['reference', 'best-practice', 'intermediate', 'success']`

**Purpose**: Prevent notification overload

- [ ] Alert prioritization
- [ ] Digest mode
- [ ] Intelligent grouping
- [ ] Threshold-based alerting

**Expected Behavior**: Alert fatigue minimized

---

# 77.10 Real-World Examples

## Overview
Production email notification scenarios.

## Tasks

### - [ ] 77.10.1 Daily Pipeline Summary System
Filename: `77_10_01_daily_pipeline_summary.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Send daily DAG summaries

- [ ] Aggregate daily status
- [ ] Generate summary report
- [ ] Highlight failures
- [ ] Trend analysis

**Expected Behavior**: Daily summary email sent

---

### - [ ] 77.10.2 Data Quality Alert System
Filename: `77_10_02_data_quality_alerts.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Alert on data quality issues

- [ ] Quality check results
- [ ] Threshold violations
- [ ] Affected data details
- [ ] Remediation steps

**Expected Behavior**: Quality alerts delivered

---

### - [ ] 77.10.3 Multi-Team Notification Routing
Filename: `77_10_03_multi_team_routing.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Route alerts to appropriate teams

- [ ] Team-based routing logic
- [ ] DAG metadata for routing
- [ ] Escalation workflows
- [ ] On-call integration

**Expected Behavior**: Correct team notified

---

### - [ ] 77.10.4 Executive Reporting Dashboard
Filename: `77_10_04_executive_reporting.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Send executive reports

- [ ] High-level KPIs
- [ ] Chart attachments
- [ ] Weekly summaries
- [ ] Business metrics

**Expected Behavior**: Executive reports delivered

---

### - [ ] 77.10.5 Incident Notification System
Filename: `77_10_05_incident_notification.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: Critical incident notifications

- [ ] Immediate alerts
- [ ] Incident details
- [ ] Runbook links
- [ ] Status updates

**Expected Behavior**: Incidents communicated quickly

---

# Summary

## Topic Completion Checklist
- [ ] SMTP configuration covered
- [ ] EmailOperator usage documented
- [ ] Templates and formatting included
- [ ] Callback notifications explained
- [ ] Advanced patterns provided
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance/reliability included
- [ ] Best practices documented
- [ ] Real-world examples provided

## Related Topics
- Section 12: Callbacks and Notifications
- Section 61: SLA Management
- Section 29: Communication Providers

## Notes for Implementation
- Use test SMTP server (mailhog) for examples
- Show HTML rendering examples
- Include attachment examples
- Demonstrate callback integration
- Cover common errors
