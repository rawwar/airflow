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

# 11 Assets (Data-Driven Scheduling)

## Overview

Assets (formerly Datasets in Airflow 2.x) enable data-driven DAG scheduling in Airflow 3.x. DAGs can produce and consume assets, creating event-driven workflows where downstream DAGs automatically trigger when upstream data becomes available.

## Research & Background

### Key Concepts
- **Asset**: A logical representation of data identified by a URI (e.g., `s3://bucket/path`, `file:///data/output.csv`)
- **Producer**: A task that creates or updates an asset (via `outlets` parameter)
- **Consumer**: A DAG that triggers when asset(s) are updated (via `schedule` parameter)
- **AssetEvent**: Metadata about an asset update including timestamp and extra info

### Airflow 3.x Breaking Changes
- `Dataset` renamed to `Asset`
- Import: `from airflow.sdk.definitions.asset import Asset, AssetAll, AssetAny`
- `schedule=[Dataset(...)]` becomes `schedule=[Asset(...)]`
- `outlets=[Dataset(...)]` becomes `outlets=[Asset(...)]`

### Prerequisites
- Airflow 3.x
- Understanding of DAG basics (Section 01)
- Understanding of TaskFlow API helpful (Section 03)

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Create and register assets with proper URI schemes
2. Build tasks that produce assets via outlets
3. Schedule DAGs to trigger on asset updates
4. Implement AND/OR asset conditions for complex workflows
5. Access asset event metadata within tasks
6. Design cross-DAG data pipelines using assets

---

# 11.1 Asset Fundamentals

## Overview
Learn the basics of defining and working with Assets in Airflow 3.x.

## Tasks

### - [ ] 11.1.1 Define Basic Asset
Filename: `11_01_01_basic_asset.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create and register a basic Asset with Airflow

- [ ] Import Asset from airflow.sdk.definitions.asset
- [ ] Create Asset with URI string (e.g., "s3://bucket/data/output.parquet")
- [ ] Register asset as outlet on a task
- [ ] Verify asset appears in Airflow UI Assets tab

**Expected Behavior**: Asset is registered and visible in UI after DAG parse

---

### - [ ] 11.1.2 Asset URI Schemes
Filename: `11_01_02_asset_uri_schemes.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Demonstrate various URI schemes supported for assets

- [ ] File URI: `file:///path/to/file`
- [ ] S3 URI: `s3://bucket/key`
- [ ] GCS URI: `gs://bucket/object`
- [ ] Database URI: `postgresql://host/db/table`
- [ ] Custom URI: `myapp://resource/id`
- [ ] Show that URI is logical identifier, not validated for existence

**Expected Behavior**: All URI formats accepted and tracked as distinct assets

---

### - [ ] 11.1.3 Asset with Extra Metadata
Filename: `11_01_03_asset_extra_metadata.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Attach metadata to assets for lineage and documentation

- [ ] Use `extra` parameter with dict for metadata
- [ ] Include owner, description, schema info
- [ ] Show how metadata appears in UI
- [ ] Demonstrate updating metadata on existing asset

**Expected Behavior**: Metadata stored and visible in asset details

---

### - [ ] 11.1.4 Asset Naming Best Practices
Filename: `11_01_04_asset_naming_best_practices.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Establish consistent asset naming conventions

- [ ] URI structure patterns (environment/domain/resource)
- [ ] Versioning in URIs when needed
- [ ] Environment separation (dev/staging/prod)
- [ ] Avoid overly specific URIs that change frequently

**Expected Behavior**: Well-organized asset namespace

---

# 11.2 Producing Assets

## Overview
Tasks can produce (update) assets by declaring them as outlets, signaling data availability.

## Tasks

### - [ ] 11.2.1 Task as Asset Producer
Filename: `11_02_01_task_asset_producer.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create a task that produces/updates an asset

- [ ] Use `outlets=[Asset("uri")]` on BashOperator or PythonOperator
- [ ] Show task completion triggers asset event
- [ ] Demonstrate multiple outlets from single task
- [ ] TaskFlow @task with outlets parameter

**Expected Behavior**: Asset event created on task success

---

### - [ ] 11.2.2 Conditional Asset Production with yield
Filename: `11_02_02_conditional_asset_production.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Produce asset only when conditions are met

- [ ] Use `yield AssetEvent()` for conditional production
- [ ] Skip asset update based on business logic
- [ ] Include extra metadata in AssetEvent
- [ ] Show difference vs implicit outlet triggering

**Expected Behavior**: Asset event only emitted when explicitly yielded

---

### - [ ] 11.2.3 Multiple Assets from One DAG
Filename: `11_02_03_multiple_assets_one_dag.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Single DAG producing multiple distinct assets

- [ ] Different tasks produce different assets
- [ ] One task producing multiple assets
- [ ] Asset dependency chain within same DAG
- [ ] Show all assets in UI lineage view

**Expected Behavior**: Multiple assets updated by single DAG run

---

### - [ ] 11.2.4 Asset Production with Metadata
Filename: `11_02_04_asset_production_with_metadata.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Include runtime metadata when producing assets

- [ ] Add row count, schema version in AssetEvent extra
- [ ] Include timestamp, source info
- [ ] Consumer can access this metadata
- [ ] Useful for data quality tracking

**Expected Behavior**: Rich metadata attached to asset events

---

# 11.3 Consuming Assets (Asset-Driven Scheduling)

## Overview
DAGs can be scheduled to trigger when assets are updated, replacing time-based schedules with data-driven schedules.

## Tasks

### - [ ] 11.3.1 DAG Triggered by Single Asset
Filename: `11_03_01_dag_triggered_single_asset.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Schedule a DAG to run when an asset is updated

- [ ] `schedule=[Asset("uri")]` in DAG definition
- [ ] Show DAG triggers automatically on asset update
- [ ] Access triggering_asset_events in context
- [ ] No need for sensors or external task sensors

**Expected Behavior**: DAG runs after producer completes

---

### - [ ] 11.3.2 DAG Triggered by Multiple Assets (AND Logic)
Filename: `11_03_02_dag_triggered_multiple_and.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Trigger DAG only when ALL specified assets are updated

- [ ] `schedule=[Asset("a"), Asset("b")]` implies AND logic
- [ ] DAG waits until both assets have new events
- [ ] Show queuing behavior when only one updates
- [ ] Demonstrate with producer DAGs for each asset

**Expected Behavior**: DAG triggers only after both assets updated

---

### - [ ] 11.3.3 DAG Triggered by Any Asset (OR Logic)
Filename: `11_03_03_dag_triggered_any_or.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger DAG when ANY of the specified assets is updated

- [ ] Use `AssetAny(Asset("a"), Asset("b"))`
- [ ] DAG triggers when either asset updates
- [ ] Identify which asset triggered using inlet_events
- [ ] Handle different assets differently in task

**Expected Behavior**: DAG triggers on any asset update

---

### - [ ] 11.3.4 Complex Asset Conditions (AND/OR Combinations)
Filename: `11_03_04_complex_asset_conditions.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Combine AND and OR logic for complex triggering

- [ ] `AssetAll(Asset("a"), AssetAny(Asset("b"), Asset("c")))`
- [ ] Nested conditions
- [ ] Real-world scenario: need A always, but B or C for alternate source
- [ ] Show UI representation of conditions

**Expected Behavior**: DAG triggers according to complex boolean logic

---

### - [ ] 11.3.5 Accessing Asset Events in Tasks
Filename: `11_03_05_accessing_asset_events.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Read triggering asset information within tasks

- [ ] Use `inlet_events` parameter in task
- [ ] Access event metadata, timestamp, source_dag_id
- [ ] Filter events by specific asset
- [ ] Use event data to parameterize task behavior

**Expected Behavior**: Tasks can inspect what triggered them

---

# 11.4 Cross-DAG Asset Workflows

## Overview
Assets enable loose coupling between DAGs, replacing tight ExternalTaskSensor dependencies.

## Tasks

### - [ ] 11.4.1 Producer-Consumer Pattern
Filename: `11_04_01_producer_consumer_pattern.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Two DAGs connected via asset dependency

- [ ] Producer DAG with outlet asset
- [ ] Consumer DAG with `schedule=[Asset]`
- [ ] Show automatic triggering
- [ ] Compare to ExternalTaskSensor approach

**Expected Behavior**: Consumer runs after producer without explicit sensor

---

### - [ ] 11.4.2 Asset Chain (A to B to C)
Filename: `11_04_02_asset_chain.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Multi-stage asset pipeline across DAGs

- [ ] DAG1 produces Asset A
- [ ] DAG2 consumes A, produces B
- [ ] DAG3 consumes B, produces C
- [ ] Show end-to-end lineage in UI

**Expected Behavior**: Chain executes sequentially as assets update

---

### - [ ] 11.4.3 Diamond Asset Pattern
Filename: `11_04_03_diamond_asset_pattern.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Complex multi-DAG asset dependencies (fan-out/fan-in)

- [ ] Source DAG produces Asset X
- [ ] DAG-A and DAG-B both consume X, produce A and B
- [ ] Aggregator DAG consumes both A and B
- [ ] Show concurrent execution of middle layer

**Expected Behavior**: Diamond pattern executes with proper parallelism

---

### - [ ] 11.4.4 Asset Lineage Visualization
Filename: `11_04_04_asset_lineage_visualization.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Demonstrate asset lineage tracking in UI

- [ ] Multiple interconnected DAGs and assets
- [ ] Show lineage graph in Airflow UI
- [ ] Trace data flow from source to destination
- [ ] Include metadata at each stage

**Expected Behavior**: Clear visual lineage in Airflow UI

---

# 11.5 Asset Events

## Overview
Asset events carry metadata about updates and can be accessed by consumers.

## Tasks

### - [ ] 11.5.1 Access AssetEvent in Task
Filename: `11_05_01_access_asset_event.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Read triggering asset event details

- [ ] Access `inlet_events` in TaskFlow function
- [ ] Get event timestamp, extra metadata
- [ ] Get source DAG/task that produced event
- [ ] Handle multiple events from same asset

**Expected Behavior**: Full event details accessible in consumer

---

### - [ ] 11.5.2 Emit Custom AssetEvent with Metadata
Filename: `11_05_02_emit_custom_asset_event.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Manually emit asset events with custom metadata

- [ ] `yield AssetEvent(Asset("uri"), extra={"row_count": 1000})`
- [ ] Include business-relevant metadata
- [ ] Conditional emission based on task results
- [ ] Multiple events from single task

**Expected Behavior**: Custom metadata flows to consumers

---

### - [ ] 11.5.3 AssetEvent Filtering
Filename: `11_05_03_asset_event_filtering.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Filter and process specific asset events

- [ ] Filter inlet_events by asset URI
- [ ] Process only events matching criteria
- [ ] Handle mixed asset sources
- [ ] Time-based event filtering

**Expected Behavior**: Selective processing of relevant events

---

# 11.6 Asset Aliases

## Overview
Asset aliases provide dynamic or pattern-based asset references.

## Tasks

### - [ ] 11.6.1 Define Asset Alias
Filename: `11_06_01_asset_alias.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Create aliases for dynamic asset references

- [ ] Import AssetAlias from airflow.sdk.definitions.asset
- [ ] Create alias that resolves to actual asset
- [ ] Use alias in schedule and outlets
- [ ] Dynamic asset resolution at runtime

**Expected Behavior**: Alias provides indirection layer for assets

---

### - [ ] 11.6.2 Parameterized Assets with Aliases
Filename: `11_06_02_parameterized_assets.py` | Tags: `['reference', 'core', 'advanced', 'success']`

**Purpose**: Use aliases for parameterized asset patterns

- [ ] Date-partitioned assets via alias
- [ ] Environment-specific asset resolution
- [ ] Template variables in asset URIs
- [ ] Maintain single consumer for multiple sources

**Expected Behavior**: Flexible asset addressing via aliases

---

# 11.7 @asset Decorator

## Overview
The @asset decorator provides a shorthand for creating single-task DAGs that produce assets, enabling asset-oriented DAG design.

## Tasks

### - [ ] 11.7.1 Basic @asset Decorator
Filename: `11_07_01_asset_decorator_basic.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Create asset-producing DAG with minimal code

- [ ] Import @asset from airflow.sdk.definitions.asset
- [ ] Define function decorated with @asset
- [ ] Automatic DAG and task creation
- [ ] Asset URI derived from function name

**Expected Behavior**: Single-task DAG producing named asset

---

### - [ ] 11.7.2 @asset with Custom URI
Filename: `11_07_02_asset_custom_uri.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Specify custom URI for @asset decorator

- [ ] `@asset(uri="s3://bucket/path")`
- [ ] Override default naming
- [ ] Include schedule parameter
- [ ] Configure DAG parameters

**Expected Behavior**: Asset with custom URI created

---

### - [ ] 11.7.3 @asset.multi for Multiple Assets
Filename: `11_07_03_asset_multi.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Produce multiple assets from single decorated function

- [ ] `@asset.multi(outlets=[Asset("a"), Asset("b")])`
- [ ] Emit events for each asset
- [ ] Conditional multi-asset emission
- [ ] Metadata per asset

**Expected Behavior**: Multiple assets produced by one function

---

### - [ ] 11.7.4 @asset vs Traditional DAG
Filename: `11_07_04_asset_vs_traditional.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Compare @asset decorator to traditional DAG approach

- [ ] Side-by-side examples
- [ ] When to use @asset (simple producers)
- [ ] When to use traditional DAG (complex logic)
- [ ] Migration from traditional to @asset

**Expected Behavior**: Clear understanding of both approaches

---

### - [ ] 11.7.5 @asset with Dependencies
Filename: `11_07_05_asset_with_deps.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Asset decorator consuming other assets

- [ ] `@asset(schedule=[Asset("upstream")])`
- [ ] Access inlet_events
- [ ] Chain @asset decorated functions
- [ ] Build asset pipeline

**Expected Behavior**: Asset chain built with decorators

---

# 11.8 AssetOrTimeSchedule

## Overview
Combine time-based and asset-based scheduling for DAGs that need both triggers.

## Tasks

### - [ ] 11.8.1 Basic AssetOrTimeSchedule
Filename: `11_08_01_asset_or_time_basic.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Trigger DAG on asset update OR time schedule

- [ ] Import AssetOrTimeSchedule from airflow.timetables
- [ ] Combine asset and cron schedule
- [ ] DAG runs whichever triggers first
- [ ] Use cases for hybrid scheduling

**Expected Behavior**: DAG triggers on asset OR time

---

### - [ ] 11.8.2 Time Schedule with Asset Fallback
Filename: `11_08_02_time_with_asset.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Run on schedule but also react to early data

- [ ] Primary: @daily schedule
- [ ] Secondary: trigger on data arrival
- [ ] Handle both trigger types in task
- [ ] Avoid duplicate processing

**Expected Behavior**: Flexible scheduling with both triggers

---

### - [ ] 11.8.3 Asset with Time Guarantee
Filename: `11_08_03_asset_time_guarantee.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`

**Purpose**: Ensure DAG runs even if asset never updates

- [ ] Asset-driven primary
- [ ] Time-based backup/SLA
- [ ] Handle stale data scenarios
- [ ] Alerting on fallback

**Expected Behavior**: Guaranteed execution with data preference

---

### - [ ] 11.8.4 Multiple Assets with Time
Filename: `11_08_04_multi_asset_time.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Combine multiple assets with time schedule

- [ ] `AssetOrTimeSchedule([Asset("a"), Asset("b")], cron)`
- [ ] AND logic for assets, OR with time
- [ ] Complex scheduling scenarios
- [ ] Real-world patterns

**Expected Behavior**: Complex hybrid scheduling works correctly

---

### - [ ] 11.8.5 Identify Trigger Source
Filename: `11_08_05_identify_trigger.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Determine what triggered the DAG run

- [ ] Check triggering_asset_events
- [ ] Detect time-triggered vs asset-triggered
- [ ] Conditional logic based on trigger
- [ ] Different processing paths

**Expected Behavior**: Task knows its trigger source

---

# 11.9 Asset Best Practices

## Overview
Guidelines for effective asset usage in production environments.

## Tasks

### - [ ] 11.7.1 Asset vs ExternalTaskSensor
Filename: `11_07_01_asset_vs_external_task.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: When to use assets vs ExternalTaskSensor

- [ ] Side-by-side comparison DAGs
- [ ] Assets: data-centric, loose coupling
- [ ] ExternalTaskSensor: task-centric, execution_date alignment
- [ ] Migration guidance from sensors to assets

**Expected Behavior**: Clear understanding of when to use each

---

### - [ ] 11.7.2 Asset Granularity Guidelines
Filename: `11_07_02_asset_granularity.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Right-sizing asset definitions

- [ ] Too granular: every file as asset (overhead)
- [ ] Too coarse: entire database as one asset (no precision)
- [ ] Right-size: meaningful data boundaries (tables, datasets)
- [ ] Examples of good vs bad granularity

**Expected Behavior**: Balanced asset granularity

---

### - [ ] 11.7.3 Asset Anti-Patterns
Filename: `11_07_03_asset_anti_patterns.py` | Tags: `['reference', 'core', 'intermediate', 'anti-pattern']`

**Purpose**: Common mistakes to avoid with assets

- [ ] Circular asset dependencies (A triggers B triggers A)
- [ ] Too many fine-grained assets causing overhead
- [ ] Using assets for non-data events
- [ ] Ignoring asset cleanup/retention

**Expected Behavior**: Recognize and avoid anti-patterns

---

### - [ ] 11.7.4 Asset Naming Conventions
Filename: `11_07_04_asset_naming_conventions.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Establish organization-wide asset naming

- [ ] URI structure: `scheme://environment/domain/resource`
- [ ] Consistent naming across teams
- [ ] Documentation in asset extra metadata
- [ ] Searchability and discoverability

**Expected Behavior**: Organized, discoverable asset namespace

---

# Summary

## Topic Completion Checklist
- [ ] All subtasks have clear purpose and Airflow 3.x syntax
- [ ] Asset (not Dataset) terminology used throughout
- [ ] Import paths updated for airflow.sdk.definitions.asset
- [ ] Examples cover beginner to advanced use cases
- [ ] Cross-references to related sections included

## Related Topics
- Section 01: Core DAG Concepts (scheduling basics)
- Section 03: TaskFlow API (outlets with @task)
- Section 08: Sensors (Asset-triggered vs sensor-based)
- Section 46: Upgrade/Deprecation (Dataset to Asset migration)

## Notes for Implementation
- All examples must use `Asset` not `Dataset`
- Import from `airflow.sdk.definitions.asset` not `airflow.datasets`
- Test both producer and consumer DAGs together
- Verify UI shows assets and lineage correctly

---

# 11.10 Asset Testing

### - [ ] 11.10.1 Testing Asset Producers
Filename: `11_10_01_testing_asset_producers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Verify outlet declaration
- [ ] Test AssetEvent emission
- [ ] Mock external storage
- [ ] Validate metadata

### - [ ] 11.10.2 Testing Asset Consumers
Filename: `11_10_02_testing_asset_consumers.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Mock triggering events
- [ ] Test inlet_events access
- [ ] Verify schedule conditions
- [ ] Integration patterns

### - [ ] 11.10.3 Testing Asset Pipelines
Filename: `11_10_03_testing_asset_pipelines.py` | Tags: `['reference', 'core', 'advanced', 'success']`

- [ ] End-to-end workflow tests
- [ ] Multi-DAG coordination
- [ ] Event propagation
- [ ] Data flow verification

### - [ ] 11.10.4 Testing AssetOrTimeSchedule
Filename: `11_10_04_testing_asset_or_time.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Test asset trigger path
- [ ] Test time trigger path
- [ ] Verify trigger identification
- [ ] Edge case handling

### - [ ] 11.10.5 Asset CI/CD Integration
Filename: `11_10_05_asset_cicd_integration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

- [ ] Validate asset definitions
- [ ] Check for circular deps
- [ ] Lineage verification
- [ ] Deployment patterns
