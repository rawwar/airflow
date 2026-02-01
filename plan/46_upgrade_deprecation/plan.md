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

# 46 Upgrade and Deprecation (Airflow 2.x to 3.x Migration)

## Overview

This section focuses on migrating DAGs from Airflow 2.x to 3.x, covering breaking changes, deprecated features, and compatibility patterns. Essential reading for teams upgrading their Airflow deployments.

## Research & Background

### Key Breaking Changes in Airflow 3.x
| Airflow 2.x | Airflow 3.x | Notes |
|-------------|-------------|-------|
| `Dataset` | `Asset` | Complete rename |
| `from airflow.datasets import Dataset` | `from airflow.sdk.definitions.asset import Asset` | Import path changed |
| `execution_date` | `logical_date` | Deprecated, use logical_date |
| `SubDAG` | `TaskGroup` | SubDAGs completely removed |
| `schedule_interval` | `schedule` | Parameter renamed |

### Prerequisites
- Airflow 2.x DAGs to migrate
- Understanding of Airflow 2.x patterns
- Access to Airflow 3.x environment for testing

### Learning Objectives
After completing the DAGs in this section, users will be able to:
1. Identify breaking changes affecting their DAGs
2. Migrate Dataset code to Asset
3. Update deprecated parameter usage
4. Write code compatible with both 2.x and 3.x (when needed)
5. Test migration changes safely

---

# 46.1 Dataset to Asset Migration

## Overview
The most significant breaking change: Dataset is renamed to Asset.

## Tasks

### - [ ] 46.1.1 Dataset to Asset Rename Migration
Filename: `46_01_01_dataset_to_asset_rename.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Migrate Dataset usage to Asset

- [ ] Show Airflow 2.x Dataset code (commented)
- [ ] Show equivalent Airflow 3.x Asset code
- [ ] Update import from airflow.datasets to airflow.sdk.definitions.asset
- [ ] Replace Dataset() with Asset()
- [ ] Update schedule=[Dataset()] to schedule=[Asset()]

**Expected Behavior**: DAG works on Airflow 3.x with Asset

---

### - [ ] 46.1.2 outlets Migration
Filename: `46_01_02_outlets_migration.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Migrate outlets parameter from Dataset to Asset

- [ ] 2.x: outlets=[Dataset("uri")]
- [ ] 3.x: outlets=[Asset("uri")]
- [ ] TaskFlow @task outlets migration
- [ ] Multiple outlets migration

**Expected Behavior**: Asset outlets work correctly

---

### - [ ] 46.1.3 DatasetEvent to AssetEvent
Filename: `46_01_03_dataset_event_to_asset_event.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Migrate DatasetEvent usage

- [ ] 2.x: yield DatasetEvent(Dataset("uri"))
- [ ] 3.x: yield AssetEvent(Asset("uri"))
- [ ] Update imports
- [ ] Migrate extra metadata

**Expected Behavior**: Asset events emitted correctly

---

### - [ ] 46.1.4 DatasetAll/DatasetAny to AssetAll/AssetAny
Filename: `46_01_04_dataset_conditions_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Migrate dataset conditions

- [ ] 2.x: DatasetAll, DatasetAny
- [ ] 3.x: AssetAll, AssetAny
- [ ] Complex condition migration
- [ ] Nested condition migration

**Expected Behavior**: Asset conditions work correctly

---

### - [ ] 46.1.5 inlet_events Migration
Filename: `46_01_05_inlet_events_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Update inlet_events access for Assets

- [ ] 2.x dataset_events parameter
- [ ] 3.x inlet_events parameter
- [ ] Access event metadata
- [ ] Filter by asset URI

**Expected Behavior**: Inlet events accessible in 3.x

---

# 46.2 execution_date to logical_date

## Overview
The execution_date parameter is deprecated in favor of logical_date.

## Tasks

### - [ ] 46.2.1 Basic execution_date Replacement
Filename: `46_02_01_execution_date_replacement.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Replace execution_date with logical_date

- [ ] 2.x: context['execution_date']
- [ ] 3.x: context['logical_date']
- [ ] Template: {{ execution_date }} to {{ logical_date }}
- [ ] Show deprecation warning with old syntax

**Expected Behavior**: logical_date works correctly

---

### - [ ] 46.2.2 Template Migration for Dates
Filename: `46_02_02_template_migration_dates.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Update Jinja templates for date references

- [ ] {{ ds }} remains valid (shortcut)
- [ ] {{ execution_date }} → {{ logical_date }}
- [ ] {{ next_execution_date }} → deprecated
- [ ] {{ data_interval_start }}, {{ data_interval_end }}

**Expected Behavior**: Templates render correctly

---

### - [ ] 46.2.3 ExternalTaskSensor execution_date_fn
Filename: `46_02_03_external_task_sensor_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Migrate ExternalTaskSensor date functions

- [ ] 2.x execution_date_fn parameter
- [ ] 3.x equivalent approach
- [ ] Execution delta migration
- [ ] Cross-DAG date alignment

**Expected Behavior**: Sensor works with new date handling

---

### - [ ] 46.2.4 Data Interval vs Execution Date
Filename: `46_02_04_data_interval_vs_execution_date.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Understand new data interval model

- [ ] data_interval_start and data_interval_end
- [ ] Relationship to logical_date
- [ ] Why this model is clearer
- [ ] Migration examples

**Expected Behavior**: Understanding of data interval model

---

# 46.3 SubDAG Removal

## Overview
SubDAGs are completely removed in Airflow 3.x - use TaskGroups instead.

## Tasks

### - [ ] 46.3.1 SubDAG to TaskGroup Migration
Filename: `46_03_01_subdag_to_taskgroup.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Replace SubDAG with TaskGroup

- [ ] Show SubDAGOperator pattern (commented, 2.x only)
- [ ] Equivalent TaskGroup implementation
- [ ] Benefits of TaskGroup (no separate DAG)
- [ ] UI comparison

**Expected Behavior**: TaskGroup replaces SubDAG functionality

---

### - [ ] 46.3.2 SubDAG Factory to TaskGroup Factory
Filename: `46_03_02_subdag_factory_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Migrate factory patterns

- [ ] 2.x SubDAG factory function
- [ ] 3.x TaskGroup factory function
- [ ] Parameterized group creation
- [ ] Reusable patterns

**Expected Behavior**: Factory pattern works with TaskGroups

---

### - [ ] 46.3.3 SubDAG Concurrency to TaskGroup
Filename: `46_03_03_subdag_concurrency_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Handle concurrency differently

- [ ] SubDAG had separate concurrency
- [ ] TaskGroup shares DAG concurrency
- [ ] Use pools for limiting TaskGroup
- [ ] max_active_tasks considerations

**Expected Behavior**: Concurrency managed appropriately

---

# 46.4 Deprecated Operators and Features

## Overview
Operators and features deprecated or removed in Airflow 3.x.

## Tasks

### - [ ] 46.4.1 Deprecated Operator Replacements
Filename: `46_04_01_deprecated_operators.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Replace deprecated operators

- [ ] List commonly deprecated operators
- [ ] Show replacement for each
- [ ] Import path changes
- [ ] Provider-specific migrations

**Expected Behavior**: Up-to-date operators used

---

### - [ ] 46.4.2 schedule_interval to schedule
Filename: `46_04_02_schedule_interval_to_schedule.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Use schedule instead of schedule_interval

- [ ] 2.x: DAG(schedule_interval="@daily")
- [ ] 3.x: DAG(schedule="@daily")
- [ ] Both parameters shown for comparison
- [ ] schedule_interval still works (deprecated)

**Expected Behavior**: schedule parameter used

---

### - [ ] 46.4.3 Removed Parameters
Filename: `46_04_03_removed_parameters.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`

**Purpose**: Identify completely removed parameters

- [ ] List removed DAG parameters
- [ ] List removed task parameters
- [ ] Error messages when using removed params
- [ ] Alternatives for removed functionality

**Expected Behavior**: Understand what was removed

---

### - [ ] 46.4.4 Import Path Changes
Filename: `46_04_04_import_path_changes.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Update import paths for 3.x

- [ ] airflow.operators changes
- [ ] airflow.sensors changes
- [ ] Provider package imports
- [ ] Utility function imports

**Expected Behavior**: Correct import paths used

---

# 46.5 Compatibility Patterns

## Overview
Writing code that works on both 2.x and 3.x during migration.

## Tasks

### - [ ] 46.5.1 Version Detection in DAGs
Filename: `46_05_01_version_detection.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Detect Airflow version at runtime

- [ ] Check airflow.version
- [ ] AIRFLOW_V_3_0_PLUS constant
- [ ] Conditional imports based on version
- [ ] Feature detection patterns

**Expected Behavior**: DAG adapts to version

---

### - [ ] 46.5.2 Conditional Imports for 2.x/3.x
Filename: `46_05_02_conditional_imports.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Import correct modules per version

- [ ] Try/except import pattern
- [ ] Version-based import selection
- [ ] Alias pattern for compatibility
- [ ] Example: Dataset vs Asset

**Expected Behavior**: Imports work on both versions

---

### - [ ] 46.5.3 Feature Detection Patterns
Filename: `46_05_03_feature_detection.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Check for feature availability

- [ ] hasattr() for new methods
- [ ] Try creating new objects
- [ ] Graceful fallback
- [ ] Feature flag patterns

**Expected Behavior**: Features detected correctly

---

### - [ ] 46.5.4 Compatibility Shim Example
Filename: `46_05_04_compatibility_shim.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`

**Purpose**: Create compatibility layer

- [ ] Wrapper for Asset/Dataset
- [ ] Unified API for both versions
- [ ] Central compatibility module
- [ ] Gradual migration support

**Expected Behavior**: Shim enables gradual migration

---

# 46.6 Testing Migration

## Overview
Safely test DAG migrations before production.

## Tasks

### - [ ] 46.6.1 Migration Testing Strategy
Filename: `46_06_01_migration_testing_strategy.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Plan migration testing

- [ ] Test DAG parsing on 3.x
- [ ] Test task execution
- [ ] Test scheduling behavior
- [ ] Parallel testing on 2.x and 3.x

**Expected Behavior**: Clear testing approach

---

### - [ ] 46.6.2 DAG Parse Test for 3.x
Filename: `46_06_02_dag_parse_test.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Verify DAG parses on Airflow 3.x

- [ ] Load DAG in test environment
- [ ] Check for deprecation warnings
- [ ] Validate task instances
- [ ] Check dependencies

**Expected Behavior**: DAG parses without errors

---

### - [ ] 46.6.3 Dry Run Migration
Filename: `46_06_03_dry_run_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`

**Purpose**: Test migration without side effects

- [ ] Run tasks in dry-run mode
- [ ] Verify XCom handling
- [ ] Check Asset/Dataset behavior
- [ ] Compare outputs

**Expected Behavior**: Migration verified safely

---

### - [ ] 46.6.4 Common Migration Errors
Filename: `46_06_04_common_migration_errors.py` | Tags: `['reference', 'core', 'beginner', 'failure']`

**Purpose**: Recognize and fix common errors

- [ ] ImportError from old paths
- [ ] TypeError from removed params
- [ ] AttributeError from renamed attrs
- [ ] Fix patterns for each

**Expected Behavior**: Errors recognized and fixed

---

# 46.7 Migration Checklist

## Overview
Systematic approach to migrating a DAG codebase.

## Tasks

### - [ ] 46.7.1 Pre-Migration Checklist
Filename: `46_07_01_pre_migration_checklist.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Prepare for migration

- [ ] Inventory all DAGs
- [ ] Identify Dataset usage
- [ ] Find SubDAG usage
- [ ] Document execution_date usage
- [ ] List deprecated operators

**Expected Behavior**: Clear migration scope

---

### - [ ] 46.7.2 Migration Steps DAG
Filename: `46_07_02_migration_steps.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Step-by-step migration example

- [ ] Original 2.x DAG (commented)
- [ ] Step 1: Update imports
- [ ] Step 2: Rename Dataset to Asset
- [ ] Step 3: Update schedule_interval
- [ ] Step 4: Fix execution_date
- [ ] Final 3.x DAG

**Expected Behavior**: Clear migration path

---

### - [ ] 46.7.3 Post-Migration Validation
Filename: `46_07_03_post_migration_validation.py` | Tags: `['reference', 'core', 'beginner', 'success']`

**Purpose**: Verify migration success

- [ ] No deprecation warnings
- [ ] Tasks run correctly
- [ ] Assets registered properly
- [ ] Scheduling works as expected
- [ ] XCom functions correctly

**Expected Behavior**: Migration validated

---

# Summary

## Topic Completion Checklist
- [ ] Dataset to Asset migration fully documented
- [ ] execution_date to logical_date covered
- [ ] SubDAG removal and TaskGroup migration
- [ ] Compatibility patterns for gradual migration
- [ ] Testing strategies included

## Related Topics
- Section 11: Assets (detailed Asset usage)
- Section 04: Dynamic DAGs (TaskGroup patterns)
- Section 01: Core DAG Concepts (schedule parameter)

## Notes for Implementation
- Show both 2.x and 3.x code side-by-side where helpful
- Use comments to indicate deprecated patterns
- Test on actual Airflow 3.x to verify
- Include deprecation warning messages
- Provide copy-paste migration examples

---

# 46.8 Provider Package Migration

## Overview
Migrating provider packages and operator imports for Airflow 3.x.

## Tasks

### - [ ] 46.8.1 Provider Package Updates
Filename: `46_08_01_provider_package_updates.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] New provider package versions required
- [ ] Compatibility matrix
- [ ] Upgrade order considerations
- [ ] Dependency conflicts resolution

### - [ ] 46.8.2 Provider Import Path Changes
Filename: `46_08_02_provider_import_changes.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Old vs new import paths
- [ ] Common provider migrations (AWS, GCP, Azure)
- [ ] Operator relocation
- [ ] Hook path changes

### - [ ] 46.8.3 Deprecated Provider Features
Filename: `46_08_03_deprecated_provider_features.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Removed operators per provider
- [ ] Replacement recommendations
- [ ] Feature flag changes
- [ ] Configuration updates

### - [ ] 46.8.4 Custom Provider Migration
Filename: `46_08_04_custom_provider_migration.py` | Tags: `['reference', 'patterns', 'advanced', 'success']`
- [ ] Update custom providers for 3.x
- [ ] SDK changes
- [ ] Hook interface changes
- [ ] Registration updates

### - [ ] 46.8.5 Provider Testing Strategy
Filename: `46_08_05_provider_testing.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Test providers against 3.x
- [ ] Mock external services
- [ ] Integration test patterns
- [ ] CI/CD provider testing

---

# 46.9 Configuration Migration

## Overview
Migrating Airflow configuration from 2.x to 3.x.

## Tasks

### - [ ] 46.9.1 Config File Changes
Filename: `46_09_01_config_file_changes.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Renamed configuration sections
- [ ] Removed configuration options
- [ ] New required settings
- [ ] Default value changes

### - [ ] 46.9.2 Environment Variable Changes
Filename: `46_09_02_env_var_changes.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] AIRFLOW__ prefix changes
- [ ] Deprecated environment variables
- [ ] New environment variables
- [ ] Secret management changes

### - [ ] 46.9.3 Database Migration
Filename: `46_09_03_database_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Schema changes 2.x to 3.x
- [ ] Migration command usage
- [ ] Backup procedures
- [ ] Rollback considerations

### - [ ] 46.9.4 Connection and Variable Migration
Filename: `46_09_04_connection_variable_migration.py` | Tags: `['reference', 'core', 'beginner', 'success']`
- [ ] Export from 2.x
- [ ] Import to 3.x
- [ ] Connection type changes
- [ ] Variable format compatibility

### - [ ] 46.9.5 Executor Configuration Migration
Filename: `46_09_05_executor_config_migration.py` | Tags: `['reference', 'core', 'intermediate', 'success']`
- [ ] Executor setting changes
- [ ] Kubernetes executor updates
- [ ] Celery executor updates
- [ ] Custom executor migration

---

# 46.10 Migration Anti-Patterns and Debugging

## Overview
Common mistakes during migration and how to debug issues.

## Tasks

### - [ ] 46.10.1 Migration Anti-Patterns
Filename: `46_10_01_migration_anti_patterns.py` | Tags: `['reference', 'patterns', 'intermediate', 'anti-pattern']`
- [ ] Big-bang migration risks
- [ ] Skipping testing phases
- [ ] Ignoring deprecation warnings
- [ ] Partial migrations

### - [ ] 46.10.2 Debugging Import Errors
Filename: `46_10_02_debugging_import_errors.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Common import failures
- [ ] Dependency resolution
- [ ] Path troubleshooting
- [ ] Module not found fixes

### - [ ] 46.10.3 Debugging Runtime Errors
Filename: `46_10_03_debugging_runtime_errors.py` | Tags: `['reference', 'core', 'intermediate', 'failure']`
- [ ] Attribute errors from renamed fields
- [ ] Type errors from changed signatures
- [ ] Context access changes
- [ ] XCom behavior differences

### - [ ] 46.10.4 Performance Regression Detection
Filename: `46_10_04_performance_regression.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] Benchmark before migration
- [ ] Compare post-migration
- [ ] Identify regressions
- [ ] Optimization strategies

### - [ ] 46.10.5 Rollback Procedures
Filename: `46_10_05_rollback_procedures.py` | Tags: `['reference', 'patterns', 'intermediate', 'success']`
- [ ] When to rollback
- [ ] Safe rollback steps
- [ ] Data preservation
- [ ] Communication plan
