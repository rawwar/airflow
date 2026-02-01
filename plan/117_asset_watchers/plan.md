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

# 117 - Asset Watchers (Event-Driven)

## Overview
Asset Watchers in Airflow 3.x enable event-driven DAG triggering based on external events, replacing polling-based approaches with push-based notifications.

---

## Section 1: AssetWatcher Fundamentals

### - [ ] 117.1.1 AssetWatcher Concept Introduction
Filename: `117_01_01_watcher_basics.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand AssetWatcher vs traditional sensors
- [ ] Define watcher attached to Asset definition
- [ ] Configure basic watcher with trigger source
- [ ] Demonstrate event-driven DAG scheduling

### - [ ] 117.1.2 Watcher Configuration Options
Filename: `117_01_02_watcher_config.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Configure watcher timeout and retry settings
- [ ] Set up event filtering parameters
- [ ] Handle watcher metadata extraction
- [ ] Define watcher-specific connection references

### - [ ] 117.1.3 Asset Definition with Watcher
Filename: `117_01_03_asset_with_watcher.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Create Asset with attached AssetWatcher
- [ ] Configure URI and watcher together
- [ ] Handle asset-watcher lifecycle
- [ ] Test watcher registration on DAG parse

### - [ ] 117.1.4 Event-Driven vs Polling Comparison
Filename: `117_01_04_event_vs_polling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Compare sensor polling vs watcher events
- [ ] Analyze resource usage differences
- [ ] Evaluate latency characteristics
- [ ] Choose appropriate approach per use case

### - [ ] 117.1.5 Watcher Lifecycle Management
Filename: `117_01_05_watcher_lifecycle.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Understand watcher startup and shutdown
- [ ] Handle watcher registration with scheduler
- [ ] Monitor watcher health status
- [ ] Debug watcher connection issues

---

## Section 2: AWS SQS Triggers

### - [ ] 117.2.1 SQS Watcher Setup
Filename: `117_02_01_sqs_watcher_setup.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Configure SqsQueueWatcher for Asset
- [ ] Set up AWS connection for SQS access
- [ ] Define queue URL and region
- [ ] Handle message visibility timeout

### - [ ] 117.2.2 SQS Message Filtering
Filename: `117_02_02_sqs_filtering.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Configure message attribute filters
- [ ] Filter by message body content patterns
- [ ] Handle multiple message types per queue
- [ ] Skip non-matching messages gracefully

### - [ ] 117.2.3 S3 Event Notifications via SQS
Filename: `117_02_03_s3_sqs_events.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Set up S3 bucket notifications to SQS
- [ ] Parse S3 event JSON from SQS messages
- [ ] Extract bucket, key, and event type
- [ ] Trigger DAG on file arrival events

### - [ ] 117.2.4 SQS Batch Processing Pattern
Filename: `117_02_04_sqs_batch_processing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Handle multiple messages per trigger
- [ ] Configure batch size and window
- [ ] Aggregate events for efficient processing
- [ ] Manage message acknowledgment

### - [ ] 117.2.5 SQS Dead Letter Queue Handling
Filename: `117_02_05_sqs_dlq.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure DLQ for failed event processing
- [ ] Monitor DLQ for watcher failures
- [ ] Implement DLQ reprocessing DAG
- [ ] Alert on DLQ message accumulation

---

## Section 3: External Event Monitoring

### - [ ] 117.3.1 Generic Event Watcher Pattern
Filename: `117_03_01_generic_watcher.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Create custom watcher for external systems
- [ ] Implement watcher interface methods
- [ ] Handle connection and event loop
- [ ] Register custom watcher with Airflow

### - [ ] 117.3.2 Kafka Event Watcher
Filename: `117_03_02_kafka_watcher.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure Kafka consumer as watcher
- [ ] Set up topic and consumer group
- [ ] Handle offset management
- [ ] Process Kafka messages as Asset events

### - [ ] 117.3.3 GCS Pub/Sub Watcher
Filename: `117_03_03_gcs_pubsub_watcher.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Set up GCS notifications to Pub/Sub
- [ ] Configure Pub/Sub subscription watcher
- [ ] Parse GCS object notifications
- [ ] Handle acknowledgment on success

### - [ ] 117.3.4 Webhook Event Watcher
Filename: `117_03_04_webhook_watcher.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Expose webhook endpoint for events
- [ ] Validate incoming webhook payloads
- [ ] Convert webhooks to Asset events
- [ ] Secure webhook with authentication

### - [ ] 117.3.5 Database Change Data Capture
Filename: `117_03_05_cdc_watcher.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Watch for database changes via CDC
- [ ] Configure Debezium/similar CDC source
- [ ] Filter relevant table changes
- [ ] Trigger pipelines on data modifications

---

## Section 4: TriggerEvent Handling

### - [ ] 117.4.1 TriggerEvent Structure
Filename: `117_04_01_trigger_event_basics.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand TriggerEvent data model
- [ ] Access event metadata in tasks
- [ ] Extract source URI and timestamp
- [ ] Handle event payload data

### - [ ] 117.4.2 Event Data Extraction
Filename: `117_04_02_event_data_extraction.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Parse event extra field JSON
- [ ] Map event data to task parameters
- [ ] Use templating with event context
- [ ] Handle missing or malformed event data

### - [ ] 117.4.3 Multi-Event DAG Runs
Filename: `117_04_03_multi_event_runs.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Handle multiple events per DAG run
- [ ] Configure event aggregation window
- [ ] Access all triggering events in tasks
- [ ] Process events in parallel branches

### - [ ] 117.4.4 Event Filtering and Routing
Filename: `117_04_04_event_routing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Route events to different task branches
- [ ] Filter events by type or content
- [ ] Skip processing for irrelevant events
- [ ] Implement event-based branching logic

### - [ ] 117.4.5 Event Replay and Reprocessing
Filename: `117_04_05_event_replay.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Replay historical events for reprocessing
- [ ] Manually trigger Asset events via API
- [ ] Handle idempotent event processing
- [ ] Track processed vs pending events

---

## Section 5: Combining Watchers with Assets

### - [ ] 117.5.1 Multiple Watchers per Asset
Filename: `117_05_01_multiple_watchers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Attach multiple watchers to single Asset
- [ ] Handle events from different sources
- [ ] Configure watcher priority/ordering
- [ ] Deduplicate overlapping events

### - [ ] 117.5.2 Asset Dependencies with Watchers
Filename: `117_05_02_asset_watcher_deps.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Combine watcher-triggered and produced Assets
- [ ] Chain event-driven DAGs via Assets
- [ ] Handle mixed event and schedule triggers
- [ ] Design asset dependency graphs

### - [ ] 117.5.3 Conditional Asset Scheduling
Filename: `117_05_03_conditional_scheduling.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Trigger on event AND schedule combination
- [ ] Use AssetAlias for dynamic asset matching
- [ ] Configure complex trigger conditions
- [ ] Handle schedule with event override

### - [ ] 117.5.4 Cross-DAG Event Propagation
Filename: `117_05_04_cross_dag_events.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Produce Asset events in one DAG
- [ ] Consume via watcher in another DAG
- [ ] Track event lineage across DAGs
- [ ] Debug event propagation issues

### - [ ] 117.5.5 Event-Driven Data Pipeline
Filename: `117_05_05_event_driven_pipeline.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Build end-to-end event-driven workflow
- [ ] Handle file arrival to processing
- [ ] Implement error handling and retries
- [ ] Monitor pipeline latency metrics

---

## Section 6: Advanced Watcher Patterns

### - [ ] 117.6.1 Watcher Health Monitoring
Filename: `117_06_01_watcher_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Monitor watcher connection status
- [ ] Track event processing metrics
- [ ] Alert on watcher failures
- [ ] Implement watcher heartbeats

### - [ ] 117.6.2 High-Volume Event Handling
Filename: `117_06_02_high_volume_events.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Handle thousands of events per minute
- [ ] Configure event batching strategies
- [ ] Implement backpressure mechanisms
- [ ] Scale watcher infrastructure

### - [ ] 117.6.3 Event Deduplication
Filename: `117_06_03_event_deduplication.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Detect duplicate events from sources
- [ ] Implement idempotency keys
- [ ] Configure deduplication windows
- [ ] Handle at-least-once vs exactly-once

### - [ ] 117.6.4 Watcher Failover Patterns
Filename: `117_06_04_watcher_failover.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Configure watcher high availability
- [ ] Handle scheduler failover for watchers
- [ ] Implement event persistence
- [ ] Recover missed events after downtime

### - [ ] 117.6.5 Testing Event-Driven DAGs
Filename: `117_06_05_testing_event_dags.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Unit test watcher configurations
- [ ] Mock external event sources
- [ ] Simulate event sequences
- [ ] Validate event processing logic

---

## Section 7: Asset Watcher Anti-Patterns

### - [ ] 117.7.1 No Event Filtering
Filename: `117_07_01_no_filtering_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Processing irrelevant events
- [ ] Resource waste
- [ ] Filter configuration
- [ ] Event type selection

### - [ ] 117.7.2 Missing Error Handling
Filename: `117_07_02_missing_error_handling_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Silent event failures
- [ ] Lost events
- [ ] Error propagation
- [ ] Dead letter queue setup

### - [ ] 117.7.3 Ignoring Event Order
Filename: `117_07_03_ignoring_order_antipattern.py` | Tags: `['reference', 'anti-pattern', 'advanced', 'failure']`
- [ ] Out-of-order processing
- [ ] Data consistency issues
- [ ] Ordering guarantees
- [ ] Sequence handling

### - [ ] 117.7.4 No Idempotent Processing
Filename: `117_07_04_no_idempotency_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Duplicate event processing
- [ ] Data corruption
- [ ] Idempotency keys
- [ ] Deduplication logic

### - [ ] 117.7.5 Watcher Without Monitoring
Filename: `117_07_05_no_monitoring_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Silent watcher failures
- [ ] Undetected lag
- [ ] Health monitoring
- [ ] Alert configuration

---

## Section 8: Testing Asset Watchers

### - [ ] 117.8.1 Unit Testing Watcher Configuration
Filename: `117_08_01_unit_testing_config.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test watcher instantiation
- [ ] Validate filter configuration
- [ ] Test connection parameters
- [ ] Configuration edge cases

### - [ ] 117.8.2 Integration Testing with Event Sources
Filename: `117_08_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Test with real SQS queues
- [ ] Test Pub/Sub integration
- [ ] Validate event parsing
- [ ] End-to-end flow testing

### - [ ] 117.8.3 Testing Event Processing Logic
Filename: `117_08_03_testing_processing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Mock event payloads
- [ ] Test transformation logic
- [ ] Validate DAG triggering
- [ ] Error handling tests

### - [ ] 117.8.4 Load Testing Event Throughput
Filename: `117_08_04_load_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] High-volume event testing
- [ ] Latency measurement
- [ ] Throughput limits
- [ ] Backpressure testing

### - [ ] 117.8.5 Testing Failover Scenarios
Filename: `117_08_05_failover_testing.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Watcher failure simulation
- [ ] Recovery testing
- [ ] Event replay validation
- [ ] HA configuration testing

---

## Section 9: Asset Watcher Performance

### - [ ] 117.9.1 Optimizing Event Polling
Filename: `117_09_01_optimize_polling.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Polling interval tuning
- [ ] Batch message retrieval
- [ ] Long polling configuration
- [ ] Resource efficiency

### - [ ] 117.9.2 Event Batching Strategies
Filename: `117_09_02_event_batching.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Batch window configuration
- [ ] Batch size optimization
- [ ] Trade-off analysis
- [ ] Adaptive batching

### - [ ] 117.9.3 Minimizing Event Latency
Filename: `117_09_03_minimize_latency.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Event source to trigger latency
- [ ] Pipeline optimization
- [ ] Parallelization
- [ ] Bottleneck identification

### - [ ] 117.9.4 Scaling Watcher Infrastructure
Filename: `117_09_04_scaling_watchers.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Multiple watcher instances
- [ ] Load distribution
- [ ] Scheduler scaling
- [ ] Queue partitioning

### - [ ] 117.9.5 Cost Optimization for Event Sources
Filename: `117_09_05_cost_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] SQS/Pub-Sub pricing
- [ ] Message retention costs
- [ ] Polling vs push costs
- [ ] Right-sizing configuration

---

## Section 10: Real-World Asset Watchers

### - [ ] 117.10.1 S3 File Arrival Pipeline
Filename: `117_10_01_s3_file_arrival.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] S3 event notifications
- [ ] SQS integration
- [ ] File processing trigger
- [ ] Error handling

### - [ ] 117.10.2 Kafka-Driven Data Pipeline
Filename: `117_10_02_kafka_pipeline.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Kafka topic watching
- [ ] Message-driven processing
- [ ] Offset management
- [ ] Consumer group handling

### - [ ] 117.10.3 Database CDC Pipeline
Filename: `117_10_03_cdc_pipeline.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Debezium integration
- [ ] Change event processing
- [ ] Real-time sync
- [ ] Schema change handling

### - [ ] 117.10.4 Webhook-Driven Workflows
Filename: `117_10_04_webhook_workflows.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] External webhook handling
- [ ] Payload validation
- [ ] Security implementation
- [ ] Response handling

### - [ ] 117.10.5 Multi-Source Event Aggregation
Filename: `117_10_05_multi_source.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Multiple event sources
- [ ] Event correlation
- [ ] Unified processing
- [ ] Source prioritization

---

# Summary

## Topic Completion Checklist
- [ ] AssetWatcher fundamentals covered
- [ ] AWS SQS triggers explained
- [ ] External event monitoring documented
- [ ] TriggerEvent handling addressed
- [ ] Asset combination patterns included
- [ ] Advanced watcher patterns documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization addressed
- [ ] Real-world examples provided

## Related Topics
- Section 11: Assets
- Section 08: Sensors
- Section 107: DAG Triggers
- Section 95: Event-Driven

## Notes for Implementation
- Choose push over poll when possible
- Implement proper error handling
- Monitor watcher health continuously
- Plan for high-volume scenarios
- Test failover procedures
