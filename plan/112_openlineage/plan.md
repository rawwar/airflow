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

# 112 - OpenLineage Data Lineage

## Overview
OpenLineage integration in Airflow 3.x: extractors, listeners, facets, Marquez backend, lineage visualization, and custom extractors.

---

## Section 1: OpenLineage Fundamentals

### - [ ] 112.1.1 OpenLineage Overview
Filename: `112_01_01_openlineage_overview.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Understand OpenLineage standard
- [ ] Core concepts: jobs, runs, datasets
- [ ] Lineage event types (START, COMPLETE, FAIL)
- [ ] Benefits for data governance

### - [ ] 112.1.2 Enable OpenLineage in Airflow
Filename: `112_01_02_enable_openlineage.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Install openlineage-airflow provider
- [ ] Configure AIRFLOW__OPENLINEAGE__* settings
- [ ] Set transport type (HTTP, Kafka, console)
- [ ] Verify lineage emission

### - [ ] 112.1.3 OpenLineage Configuration Options
Filename: `112_01_03_openlineage_configuration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Namespace configuration
- [ ] Transport configuration details
- [ ] Disabled operators list
- [ ] Custom config file usage

### - [ ] 112.1.4 OpenLineage Events Structure
Filename: `112_01_04_openlineage_events_structure.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] RunEvent JSON structure
- [ ] Job facets and dataset facets
- [ ] Input and output datasets
- [ ] Event metadata fields

### - [ ] 112.1.5 Debug OpenLineage Emissions
Filename: `112_01_05_debug_openlineage_emissions.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Enable console transport for debugging
- [ ] Log lineage events
- [ ] Troubleshoot missing events
- [ ] Validate event payloads

---

## Section 2: Built-in Extractors

### - [ ] 112.2.1 SQL Operator Extractors
Filename: `112_02_01_sql_operator_extractors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] PostgresOperator lineage extraction
- [ ] BigQueryOperator lineage
- [ ] SnowflakeOperator lineage
- [ ] SQL parsing for input/output detection

### - [ ] 112.2.2 Python Operator Extractors
Filename: `112_02_02_python_operator_extractors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] PythonOperator default extraction
- [ ] Inlets and outlets specification
- [ ] Manual dataset declaration
- [ ] TaskFlow API lineage

### - [ ] 112.2.3 Transfer Operator Extractors
Filename: `112_02_03_transfer_operator_extractors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] S3ToRedshiftOperator lineage
- [ ] GCSToGCSOperator lineage
- [ ] Cross-system transfer tracking
- [ ] File path extraction

### - [ ] 112.2.4 Spark Operator Extractors
Filename: `112_02_04_spark_operator_extractors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] SparkSubmitOperator lineage
- [ ] DataprocSubmitJobOperator
- [ ] EMR lineage extraction
- [ ] Spark job facets

### - [ ] 112.2.5 dbt Operator Extractors
Filename: `112_02_05_dbt_operator_extractors.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] dbt model lineage extraction
- [ ] Manifest parsing for lineage
- [ ] Source and model relationships
- [ ] Test result facets

---

## Section 3: OpenLineage Listeners

### - [ ] 112.3.1 Listener Architecture
Filename: `112_03_01_listener_architecture.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] OpenLineage listener plugin
- [ ] Hook into task lifecycle
- [ ] Event emission timing
- [ ] Async vs sync emission

### - [ ] 112.3.2 Task Instance Listeners
Filename: `112_03_02_task_instance_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] on_task_instance_running
- [ ] on_task_instance_success
- [ ] on_task_instance_failed
- [ ] Custom listener callbacks

### - [ ] 112.3.3 DAG Run Listeners
Filename: `112_03_03_dag_run_listeners.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] DAG-level lineage events
- [ ] on_dag_run_running
- [ ] on_dag_run_success/failed
- [ ] Aggregate job facets

### - [ ] 112.3.4 Dataset Listeners
Filename: `112_03_04_dataset_listeners.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] on_dataset_created
- [ ] on_dataset_changed
- [ ] Dataset event correlation
- [ ] Cross-DAG dataset tracking

### - [ ] 112.3.5 Custom Event Listeners
Filename: `112_03_05_custom_event_listeners.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement custom listener
- [ ] Filter events by operator type
- [ ] Enrich events with metadata
- [ ] Forward to additional backends

---

## Section 4: Facets and Metadata

### - [ ] 112.4.1 Standard Facets Overview
Filename: `112_04_01_standard_facets_overview.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] SQLJobFacet
- [ ] SourceCodeFacet
- [ ] DocumentationFacet
- [ ] OwnershipFacet

### - [ ] 112.4.2 Dataset Facets
Filename: `112_04_02_dataset_facets.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] SchemaDatasetFacet
- [ ] DataSourceDatasetFacet
- [ ] StorageDatasetFacet
- [ ] LifecycleStateChangeFacet

### - [ ] 112.4.3 Run Facets
Filename: `112_04_03_run_facets.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] ParentRunFacet
- [ ] ErrorMessageRunFacet
- [ ] NominalTimeRunFacet
- [ ] ExternalQueryRunFacet

### - [ ] 112.4.4 Custom Facets
Filename: `112_04_04_custom_facets.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Define custom facet schema
- [ ] Register custom facet
- [ ] Emit custom facets from tasks
- [ ] Validate facet compatibility

### - [ ] 112.4.5 Data Quality Facets
Filename: `112_04_05_data_quality_facets.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] DataQualityMetricsFacet
- [ ] DataQualityAssertionsFacet
- [ ] Integrate with Great Expectations
- [ ] Quality metric visualization

---

## Section 5: Marquez Backend Integration

### - [ ] 112.5.1 Marquez Setup and Configuration
Filename: `112_05_01_marquez_setup_configuration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Deploy Marquez server
- [ ] Configure Airflow HTTP transport
- [ ] API authentication setup
- [ ] Database backend options

### - [ ] 112.5.2 Marquez UI Navigation
Filename: `112_05_02_marquez_ui_navigation.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Explore jobs view
- [ ] Navigate dataset lineage
- [ ] Run history visualization
- [ ] Search and filter capabilities

### - [ ] 112.5.3 Marquez API Usage
Filename: `112_05_03_marquez_api_usage.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Query lineage via API
- [ ] Retrieve run history
- [ ] Get dataset versions
- [ ] Programmatic lineage access

### - [ ] 112.5.4 Marquez Column-Level Lineage
Filename: `112_05_04_marquez_column_lineage.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Enable column-level lineage
- [ ] SQL column parsing
- [ ] Column transformation tracking
- [ ] Visualize column flow

### - [ ] 112.5.5 Marquez High Availability
Filename: `112_05_05_marquez_high_availability.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Marquez clustering setup
- [ ] PostgreSQL replication
- [ ] Load balancing configuration
- [ ] Event buffering strategies

---

## Section 6: Custom Extractors

### - [ ] 112.6.1 Extractor Base Class
Filename: `112_06_01_extractor_base_class.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Understand BaseExtractor
- [ ] Required method implementations
- [ ] Operator to extractor mapping
- [ ] Registration mechanism

### - [ ] 112.6.2 Build Custom Extractor
Filename: `112_06_02_build_custom_extractor.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Implement extract() method
- [ ] Define input datasets
- [ ] Define output datasets
- [ ] Add job facets

### - [ ] 112.6.3 SQL Parsing in Extractors
Filename: `112_06_03_sql_parsing_extractors.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Use sqllineage library
- [ ] Parse SELECT/INSERT statements
- [ ] Handle CTEs and subqueries
- [ ] Extract table references

### - [ ] 112.6.4 Extractor Testing
Filename: `112_06_04_extractor_testing.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Unit test custom extractor
- [ ] Mock operator context
- [ ] Validate emitted events
- [ ] Integration test with Marquez

### - [ ] 112.6.5 Package and Distribute Extractors
Filename: `112_06_05_package_distribute_extractors.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Create extractor package
- [ ] Entry point configuration
- [ ] Version compatibility
- [ ] Contribute to openlineage-airflow

---

## Section 7: OpenLineage Anti-Patterns

### - [ ] 112.7.1 Missing Dataset Declarations
Filename: `112_07_01_missing_datasets_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Incomplete lineage graphs
- [ ] Silent lineage gaps
- [ ] Manual declaration patterns
- [ ] Validation approaches

### - [ ] 112.7.2 Ignoring Extractor Errors
Filename: `112_07_02_ignoring_errors_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Silent extraction failures
- [ ] Missing events undetected
- [ ] Error monitoring setup
- [ ] Fallback strategies

### - [ ] 112.7.3 Over-Granular Lineage
Filename: `112_07_03_over_granular_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Too many lineage events
- [ ] Performance impact
- [ ] Storage costs
- [ ] Right-sizing granularity

### - [ ] 112.7.4 Inconsistent Namespace Usage
Filename: `112_07_04_inconsistent_namespace_antipattern.py` | Tags: `['reference', 'anti-pattern', 'intermediate', 'failure']`
- [ ] Fragmented lineage
- [ ] Duplicate datasets
- [ ] Namespace governance
- [ ] Naming conventions

### - [ ] 112.7.5 Hardcoded Dataset URIs
Filename: `112_07_05_hardcoded_uri_antipattern.py` | Tags: `['reference', 'anti-pattern', 'beginner', 'failure']`
- [ ] Environment-specific issues
- [ ] URI construction patterns
- [ ] Dynamic URI generation
- [ ] Configuration-driven URIs

---

## Section 8: Testing OpenLineage

### - [ ] 112.8.1 Unit Testing Extractors
Filename: `112_08_01_unit_testing_extractors.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Mock operator contexts
- [ ] Validate extracted events
- [ ] Test edge cases
- [ ] Coverage verification

### - [ ] 112.8.2 Integration Testing Lineage
Filename: `112_08_02_integration_testing.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] End-to-end lineage tests
- [ ] Verify Marquez ingestion
- [ ] Test DAG lineage graphs
- [ ] Validate relationships

### - [ ] 112.8.3 Lineage Validation Tools
Filename: `112_08_03_validation_tools.py` | Tags: `['reference', 'testing', 'intermediate', 'success']`
- [ ] Event schema validation
- [ ] Lineage completeness checks
- [ ] Automated validation
- [ ] Regression detection

### - [ ] 112.8.4 Testing Custom Extractors
Filename: `112_08_04_testing_custom_extractors.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Extractor test harness
- [ ] Fixture generation
- [ ] Edge case coverage
- [ ] Performance testing

### - [ ] 112.8.5 Lineage Event Simulation
Filename: `112_08_05_event_simulation.py` | Tags: `['reference', 'testing', 'advanced', 'success']`
- [ ] Generate test events
- [ ] Simulate failure scenarios
- [ ] Load testing lineage
- [ ] Event replay testing

---

## Section 9: Performance and Scaling

### - [ ] 112.9.1 High-Volume Lineage Capture
Filename: `112_09_01_high_volume_lineage.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Event batching
- [ ] Async emission
- [ ] Buffer configuration
- [ ] Backpressure handling

### - [ ] 112.9.2 Marquez Scaling Strategies
Filename: `112_09_02_marquez_scaling.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Database optimization
- [ ] Query performance
- [ ] Retention policies
- [ ] Index management

### - [ ] 112.9.3 Lineage Event Filtering
Filename: `112_09_03_event_filtering.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] Selective event capture
- [ ] Filter by DAG/task
- [ ] Sample high-frequency events
- [ ] Cost optimization

### - [ ] 112.9.4 Transport Optimization
Filename: `112_09_04_transport_optimization.py` | Tags: `['reference', 'performance', 'intermediate', 'success']`
- [ ] HTTP vs Kafka transport
- [ ] Batch event sending
- [ ] Compression settings
- [ ] Retry configuration

### - [ ] 112.9.5 Lineage Query Performance
Filename: `112_09_05_query_performance.py` | Tags: `['reference', 'performance', 'advanced', 'success']`
- [ ] Optimize lineage queries
- [ ] Caching strategies
- [ ] Graph traversal efficiency
- [ ] API pagination

---

## Section 10: Real-World OpenLineage

### - [ ] 112.10.1 Data Governance Integration
Filename: `112_10_01_data_governance.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Catalog integration
- [ ] Policy enforcement
- [ ] Compliance reporting
- [ ] Impact analysis

### - [ ] 112.10.2 Cross-Platform Lineage
Filename: `112_10_02_cross_platform.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Airflow + Spark lineage
- [ ] dbt integration
- [ ] Unified lineage view
- [ ] Platform correlation

### - [ ] 112.10.3 Debugging with Lineage
Filename: `112_10_03_debugging_lineage.py` | Tags: `['reference', 'real-world', 'intermediate', 'success']`
- [ ] Trace data issues
- [ ] Identify failure impact
- [ ] Root cause analysis
- [ ] Historical comparison

### - [ ] 112.10.4 Lineage-Driven Automation
Filename: `112_10_04_lineage_automation.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Auto-generate documentation
- [ ] Trigger downstream on lineage
- [ ] Anomaly detection
- [ ] SLA monitoring

### - [ ] 112.10.5 Enterprise Lineage Deployment
Filename: `112_10_05_enterprise_deployment.py` | Tags: `['reference', 'real-world', 'advanced', 'success']`
- [ ] Multi-team setup
- [ ] Access control
- [ ] Namespace governance
- [ ] Centralized lineage

---

# Summary

## Topic Completion Checklist
- [ ] OpenLineage fundamentals covered
- [ ] Built-in extractors explained
- [ ] Listeners documented
- [ ] Facets and metadata addressed
- [ ] Marquez integration included
- [ ] Custom extractors documented
- [ ] Anti-patterns identified
- [ ] Testing strategies covered
- [ ] Performance optimization addressed
- [ ] Real-world examples provided

## Related Topics
- Section 113: Cosmos dbt
- Section 11: Assets
- Section 68: Data Quality
- Section 94: Audit Trails

## Notes for Implementation
- Enable lineage early in projects
- Validate extractor coverage
- Monitor lineage completeness
- Plan for high-volume scenarios
- Integrate with data governance
