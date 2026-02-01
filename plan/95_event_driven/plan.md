# 95 Event-Driven Patterns

## Overview

Event-driven patterns enable reactive workflows triggered by external events rather than schedules. Airflow 3.x Assets (formerly Datasets) combined with sensors and external triggers support sophisticated event-driven architectures.

## Airflow 3.x Notes
- Assets (Datasets) for data-aware scheduling
- Enhanced sensor deferrable support
- External trigger capabilities
- Event-driven cross-DAG dependencies
- Webhook-based triggering

---

# 95.1 Asset-Based Event Triggers

## Overview
Using Assets for data-driven DAG execution.

## Tasks

### - [ ] 95.1.1 Asset Producer Pattern
Filename: `95_01_01_asset_producer.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create Asset-producing DAGs

- [ ] Define Asset URIs
- [ ] Outlet declaration
- [ ] Asset update emission
- [ ] Producer DAG pattern

**Expected Behavior**: Asset updates emitted

---

### - [ ] 95.1.2 Asset Consumer Pattern
Filename: `95_01_02_asset_consumer.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create Asset-consuming DAGs

- [ ] schedule=[Asset()] pattern
- [ ] Multiple Asset dependencies
- [ ] Consumer DAG structure
- [ ] Event correlation

**Expected Behavior**: Consumer triggers on Asset

---

### - [ ] 95.1.3 Multi-Asset Dependencies
Filename: `95_01_03_multi_asset_dependencies.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Wait for multiple Assets

- [ ] AND logic for Assets
- [ ] All Assets must update
- [ ] Partial trigger patterns
- [ ] Asset grouping

**Expected Behavior**: Multi-Asset trigger works

---

### - [ ] 95.1.4 Asset Event Metadata
Filename: `95_01_04_asset_event_metadata.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Pass data via Asset events

- [ ] Extra metadata in events
- [ ] Accessing event data
- [ ] Event payload patterns
- [ ] Metadata schema

**Expected Behavior**: Metadata flows with events

---

### - [ ] 95.1.5 Conditional Asset Triggers
Filename: `95_01_05_conditional_asset_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Conditional event processing

- [ ] Filter Asset events
- [ ] Conditional triggering logic
- [ ] Event validation
- [ ] Skip patterns

**Expected Behavior**: Conditional triggers work

---

# 95.2 External Event Integration

## Overview
Triggering DAGs from external systems.

## Tasks

### - [ ] 95.2.1 Webhook-Based Triggering
Filename: `95_02_01_webhook_triggering.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger DAGs via webhooks

- [ ] REST API trigger endpoint
- [ ] DAG trigger with conf
- [ ] Authentication handling
- [ ] Response patterns

**Expected Behavior**: Webhook triggers DAG

---

### - [ ] 95.2.2 Message Queue Triggers
Filename: `95_02_02_message_queue_triggers.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger from message queues

- [ ] Kafka message triggers
- [ ] RabbitMQ integration
- [ ] SQS event triggers
- [ ] Message processing

**Expected Behavior**: Queue messages trigger DAGs

---

### - [ ] 95.2.3 Cloud Event Triggers
Filename: `95_02_03_cloud_event_triggers.py` | Tags: `['reference', 'providers', 'intermediate', 'success']`

**Purpose**: Trigger from cloud events

- [ ] S3 event notifications
- [ ] GCS object changes
- [ ] Azure Blob events
- [ ] CloudEvents format

**Expected Behavior**: Cloud events trigger DAGs

---

### - [ ] 95.2.4 Database Change Events
Filename: `95_02_04_database_change_events.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Trigger on database changes

- [ ] Change data capture
- [ ] Debezium integration
- [ ] Row-level triggers
- [ ] Batch change handling

**Expected Behavior**: DB changes trigger DAGs

---

### - [ ] 95.2.5 Custom Event Gateway
Filename: `95_02_05_custom_event_gateway.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Build event ingestion layer

- [ ] Event router service
- [ ] DAG dispatch logic
- [ ] Event transformation
- [ ] Idempotency handling

**Expected Behavior**: Event gateway works

---

# 95.3 Sensor-Based Event Handling

## Overview
Using sensors for event detection.

## Tasks

### - [ ] 95.3.1 External Task Sensor Events
Filename: `95_03_01_external_task_sensor.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Wait for external DAG completion

- [ ] ExternalTaskSensor pattern
- [ ] Cross-DAG dependencies
- [ ] Execution date alignment
- [ ] Timeout handling

**Expected Behavior**: External event detected

---

### - [ ] 95.3.2 File Arrival Events
Filename: `95_03_02_file_arrival_events.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: React to file arrivals

- [ ] FileSensor patterns
- [ ] S3KeySensor usage
- [ ] GCSObjectExistenceSensor
- [ ] Deferrable mode

**Expected Behavior**: File events detected

---

### - [ ] 95.3.3 HTTP Endpoint Events
Filename: `95_03_03_http_endpoint_events.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Wait for HTTP conditions

- [ ] HttpSensor for API readiness
- [ ] Response validation
- [ ] Deferrable HTTP sensing
- [ ] Timeout strategies

**Expected Behavior**: HTTP events detected

---

### - [ ] 95.3.4 SQL-Based Events
Filename: `95_03_04_sql_based_events.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger on SQL conditions

- [ ] SqlSensor patterns
- [ ] Row count triggers
- [ ] Flag table monitoring
- [ ] Query result events

**Expected Behavior**: SQL conditions detected

---

### - [ ] 95.3.5 Custom Event Sensors
Filename: `95_03_05_custom_event_sensors.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Build custom event sensors

- [ ] Custom sensor class
- [ ] poke() implementation
- [ ] Deferrable custom sensor
- [ ] Event payload extraction

**Expected Behavior**: Custom sensor works

---

# 95.4 Event-Driven Architecture Patterns

## Overview
Architectural patterns for event-driven workflows.

## Tasks

### - [ ] 95.4.1 Event Sourcing Pattern
Filename: `95_04_01_event_sourcing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Implement event sourcing

- [ ] Event log as source of truth
- [ ] Event replay capabilities
- [ ] State reconstruction
- [ ] Audit trail integration

**Expected Behavior**: Event sourcing works

---

### - [ ] 95.4.2 Pub/Sub Pattern
Filename: `95_04_02_pubsub_pattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Publisher-subscriber workflows

- [ ] Publisher DAGs
- [ ] Subscriber DAGs
- [ ] Topic-based routing
- [ ] Fan-out patterns

**Expected Behavior**: Pub/Sub working

---

### - [ ] 95.4.3 Event Choreography
Filename: `95_04_03_event_choreography.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Decoupled workflow coordination

- [ ] No central orchestrator
- [ ] Event-based sequencing
- [ ] Self-contained DAGs
- [ ] Eventual consistency

**Expected Behavior**: Choreography pattern works

---

### - [ ] 95.4.4 Saga Pattern
Filename: `95_04_04_saga_pattern.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Distributed transactions

- [ ] Saga coordinator DAG
- [ ] Compensating actions
- [ ] Failure handling
- [ ] State management

**Expected Behavior**: Saga transactions work

---

### - [ ] 95.4.5 CQRS Integration
Filename: `95_04_05_cqrs_integration.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Command-Query separation

- [ ] Command DAGs (write)
- [ ] Query DAGs (read)
- [ ] Event synchronization
- [ ] View materialization

**Expected Behavior**: CQRS pattern works

---

# 95.5 Event Processing Patterns

## Overview
Processing and handling events effectively.

## Tasks

### - [ ] 95.5.1 Event Deduplication
Filename: `95_05_01_event_deduplication.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle duplicate events

- [ ] Idempotency keys
- [ ] Event ID tracking
- [ ] Deduplication window
- [ ] At-least-once handling

**Expected Behavior**: Duplicates handled

---

### - [ ] 95.5.2 Event Ordering
Filename: `95_05_02_event_ordering.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Maintain event order

- [ ] Sequence tracking
- [ ] Out-of-order handling
- [ ] Buffering strategies
- [ ] Partition ordering

**Expected Behavior**: Order preserved

---

### - [ ] 95.5.3 Event Batching
Filename: `95_05_03_event_batching.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Process events in batches

- [ ] Batch collection
- [ ] Window-based batching
- [ ] Batch size limits
- [ ] Flush triggers

**Expected Behavior**: Events batched

---

### - [ ] 95.5.4 Event Filtering and Routing
Filename: `95_05_04_event_filtering_routing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Route events to appropriate handlers

- [ ] Event type filtering
- [ ] Content-based routing
- [ ] Dynamic DAG selection
- [ ] Filter chaining

**Expected Behavior**: Events routed correctly

---

### - [ ] 95.5.5 Dead Letter Queue Pattern
Filename: `95_05_05_dead_letter_queue.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Handle failed events

- [ ] DLQ for failures
- [ ] Retry from DLQ
- [ ] Error categorization
- [ ] Manual intervention

**Expected Behavior**: Failed events handled

---

# 95.6 Event-Driven Anti-Patterns

## Overview
Common event-driven mistakes to avoid.

## Tasks

### - [ ] 95.6.1 Polling Instead of Events
Filename: `95_06_01_polling_antipattern.py` | Tags: `['reference', 'patterns', 'beginner', 'anti-pattern']`

**Purpose**: Avoid inefficient polling

- [ ] Show frequent polling
- [ ] Demonstrate resource waste
- [ ] Provide event-driven alternative
- [ ] Include push-based patterns

**Expected Behavior**: Event-driven design

---

### - [ ] 95.6.2 Missing Event Replay
Filename: `95_06_02_no_replay_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Support event replay

- [ ] Show lost events
- [ ] Demonstrate recovery issues
- [ ] Provide event log patterns
- [ ] Include replay mechanisms

**Expected Behavior**: Events replayable

---

### - [ ] 95.6.3 Tight Event Coupling
Filename: `95_06_03_tight_coupling_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Loosely couple events

- [ ] Show direct dependencies
- [ ] Demonstrate cascading failures
- [ ] Provide decoupling patterns
- [ ] Include event schemas

**Expected Behavior**: Loose event coupling

---

### - [ ] 95.6.4 Synchronous Event Processing
Filename: `95_06_04_sync_processing_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Async event handling

- [ ] Show blocking processing
- [ ] Demonstrate throughput issues
- [ ] Provide async patterns
- [ ] Include queue-based processing

**Expected Behavior**: Non-blocking events

---

### - [ ] 95.6.5 Ignoring Event Schemas
Filename: `95_06_05_no_schema_antipattern.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`

**Purpose**: Schema-driven events

- [ ] Show unstructured events
- [ ] Demonstrate compatibility issues
- [ ] Provide schema patterns
- [ ] Include versioning

**Expected Behavior**: Schema-based events

---

# 95.7 Event-Driven Testing

## Overview
Testing event-driven workflows.

## Tasks

### - [ ] 95.7.1 Unit Testing Event Handlers
Filename: `95_07_01_unit_testing_handlers.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Test event processing

- [ ] Mock event sources
- [ ] Test handler logic
- [ ] Verify side effects
- [ ] Test error handling

**Expected Behavior**: Handlers tested

---

### - [ ] 95.7.2 Integration Testing Event Flows
Filename: `95_07_02_integration_testing_flows.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: End-to-end event testing

- [ ] Full event propagation
- [ ] DAG trigger verification
- [ ] Cross-DAG testing
- [ ] Timing validation

**Expected Behavior**: Event flows verified

---

### - [ ] 95.7.3 Testing Event Ordering
Filename: `95_07_03_testing_event_ordering.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify event sequence

- [ ] Order preservation
- [ ] Out-of-order handling
- [ ] Sequence testing
- [ ] Race condition detection

**Expected Behavior**: Ordering verified

---

### - [ ] 95.7.4 Testing Event Idempotency
Filename: `95_07_04_testing_idempotency.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Verify idempotent processing

- [ ] Duplicate event testing
- [ ] State verification
- [ ] Side effect checks
- [ ] Replay testing

**Expected Behavior**: Idempotency verified

---

### - [ ] 95.7.5 Event Simulation Testing
Filename: `95_07_05_event_simulation.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`

**Purpose**: Simulate event scenarios

- [ ] Event generators
- [ ] Load testing
- [ ] Failure injection
- [ ] Scenario replay

**Expected Behavior**: Scenarios testable

---

# 95.8 Event-Driven Performance

## Overview
Optimizing event-driven systems.

## Tasks

### - [ ] 95.8.1 Event Processing Throughput
Filename: `95_08_01_processing_throughput.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Maximize throughput

- [ ] Parallel processing
- [ ] Batch event handling
- [ ] Concurrency tuning
- [ ] Bottleneck identification

**Expected Behavior**: High throughput

---

### - [ ] 95.8.2 Event Latency Optimization
Filename: `95_08_02_latency_optimization.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Minimize latency

- [ ] End-to-end latency
- [ ] Processing optimization
- [ ] Queue tuning
- [ ] Hot path optimization

**Expected Behavior**: Low latency

---

### - [ ] 95.8.3 Event Queue Scaling
Filename: `95_08_03_queue_scaling.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Scale event queues

- [ ] Horizontal scaling
- [ ] Partition strategies
- [ ] Consumer groups
- [ ] Auto-scaling

**Expected Behavior**: Scalable queues

---

### - [ ] 95.8.4 Event Storage Optimization
Filename: `95_08_04_storage_optimization.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Efficient event storage

- [ ] Compression
- [ ] Retention policies
- [ ] Tiered storage
- [ ] Archival patterns

**Expected Behavior**: Efficient storage

---

### - [ ] 95.8.5 Event Monitoring and Metrics
Filename: `95_08_05_event_monitoring.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Monitor event systems

- [ ] Event rate metrics
- [ ] Lag monitoring
- [ ] Error tracking
- [ ] Performance dashboards

**Expected Behavior**: Events monitored

---

# 95.9 Advanced Event Patterns

## Overview
Sophisticated event-driven patterns.

## Tasks

### - [ ] 95.9.1 Event Versioning and Evolution
Filename: `95_09_01_event_versioning.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Evolve event schemas

- [ ] Schema versioning
- [ ] Backward compatibility
- [ ] Event upcasting
- [ ] Migration strategies

**Expected Behavior**: Events evolvable

---

### - [ ] 95.9.2 Complex Event Processing
Filename: `95_09_02_complex_event_processing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Pattern detection

- [ ] Event patterns
- [ ] Windowed aggregation
- [ ] Correlation rules
- [ ] Alert generation

**Expected Behavior**: Complex patterns detected

---

### - [ ] 95.9.3 Event-Driven State Machines
Filename: `95_09_03_event_state_machines.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: State machine workflows

- [ ] State definitions
- [ ] Transition events
- [ ] Guard conditions
- [ ] State persistence

**Expected Behavior**: State machines work

---

### - [ ] 95.9.4 Multi-Region Event Distribution
Filename: `95_09_04_multi_region_events.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Global event distribution

- [ ] Cross-region replication
- [ ] Eventual consistency
- [ ] Conflict resolution
- [ ] Latency optimization

**Expected Behavior**: Global events work

---

### - [ ] 95.9.5 Event-Driven Microservices
Filename: `95_09_05_event_microservices.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Microservices coordination

- [ ] Service boundaries
- [ ] Event contracts
- [ ] Choreography patterns
- [ ] Service discovery

**Expected Behavior**: Services coordinated

---

# 95.10 Real-World Examples

## Overview
Complete event-driven implementations.

## Tasks

### - [ ] 95.10.1 Data Lake Event Pipeline
Filename: `95_10_01_data_lake_event_pipeline.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Event-driven data lake

- [ ] File arrival triggers
- [ ] Processing pipelines
- [ ] Quality gates
- [ ] Catalog updates

**Expected Behavior**: Data lake automated

---

### - [ ] 95.10.2 Real-Time Analytics Pipeline
Filename: `95_10_02_realtime_analytics.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Real-time event analytics

- [ ] Event ingestion
- [ ] Stream processing
- [ ] Dashboard updates
- [ ] Alert generation

**Expected Behavior**: Real-time analytics

---

### - [ ] 95.10.3 IoT Event Processing
Filename: `95_10_03_iot_event_processing.py` | Tags: `['reference', 'example', 'advanced', 'success']`

**Purpose**: IoT device events

- [ ] Device event handling
- [ ] Aggregation patterns
- [ ] Anomaly detection
- [ ] Response actions

**Expected Behavior**: IoT events processed

---

### - [ ] 95.10.4 E-Commerce Order Events
Filename: `95_10_04_ecommerce_orders.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: Order processing events

- [ ] Order creation triggers
- [ ] Fulfillment workflows
- [ ] Inventory updates
- [ ] Notification events

**Expected Behavior**: Orders processed

---

### - [ ] 95.10.5 CI/CD Event Integration
Filename: `95_10_05_cicd_event_integration.py` | Tags: `['reference', 'example', 'intermediate', 'success']`

**Purpose**: CI/CD triggered DAGs

- [ ] Deployment events
- [ ] Test result triggers
- [ ] Release automation
- [ ] Rollback events

**Expected Behavior**: CI/CD integrated

---

# Summary

## Topic Completion Checklist
- [ ] Asset triggers explained
- [ ] External events covered
- [ ] Sensor patterns documented
- [ ] Architecture patterns included
- [ ] Processing patterns provided
- [ ] Anti-patterns identified
- [ ] Testing covered
- [ ] Performance optimized
- [ ] Advanced patterns included
- [ ] Real-world examples provided

## Related Topics
- Section 11: Assets (Asset basics)
- Section 08: Sensors (sensor basics)
- Section 96: Streaming Integration (streaming events)

## Notes for Implementation
- Test Asset triggers end-to-end
- Show webhook integration
- Include deferrable patterns
- Demonstrate event ordering
