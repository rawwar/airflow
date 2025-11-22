# DAG Run Lifecycle Documentation

Comprehensive documentation on how DAG runs progress through their lifecycle in Apache Airflow, from creation to completion.

## Overview

This directory contains detailed documentation about:

- **DAG Run States**: QUEUED → RUNNING → SUCCESS/FAILED
- **Task Instance States**: NULL → SCHEDULED → QUEUED → RUNNING → terminal states
- **Executors**: LocalExecutor, CeleryExecutor, KubernetesExecutor
- **State Transitions**: Retry logic, sensors, deferrable operators, edge cases

## Quick Reference

### DAG Run States (4)

| State | Description | Terminal |
|-------|-------------|----------|
| **QUEUED** | Created, waiting to start | No |
| **RUNNING** | Tasks being scheduled/executed | No |
| **SUCCESS** | All required tasks completed | Yes |
| **FAILED** | One or more tasks failed | Yes |

### Task Instance States (14)

| State | Description | Terminal |
|-------|-------------|----------|
| **NULL** | Task created, not scheduled | No |
| **SCHEDULED** | Ready to run, dependencies met | No |
| **QUEUED** | In executor queue | No |
| **RUNNING** | Actively executing | No |
| **SUCCESS** | Completed successfully | Yes |
| **FAILED** | Failed (no retries) | Yes |
| **UP_FOR_RETRY** | Failed, will retry | No |
| **SKIPPED** | Skipped by branching | Yes |
| **UPSTREAM_FAILED** | Upstream dependency failed | Yes |
| **UP_FOR_RESCHEDULE** | Sensor waiting | No |
| **DEFERRED** | Deferrable operator | No |
| **REMOVED** | Task removed from DAG | Yes |
| **RESTARTING** | User cleared task | No |
| **SHUTDOWN** | Executor shutdown | No |

## Documentation Files

### 1. [lifecycle_overview.md](lifecycle_overview.md)

**Complete DAG run lifecycle from creation to completion.**

- DAG run state machine with Mermaid diagrams
- Task instance state machine with 14 states
- Complete lifecycle flow (6 phases)
- Key components: DagRun, TaskInstance, Scheduler, Executors
- Timestamps and timing (queued_at, start_date, end_date)
- Error handling (retries, upstream failures)

**Diagrams**: 7 Mermaid diagrams (stateDiagram-v2, sequenceDiagram, flowchart, gantt)

**Use this for**: Understanding the complete flow from DAG file to task execution

### 2. [executors_comparison.md](executors_comparison.md)

**Detailed comparison of LocalExecutor, CeleryExecutor, and KubernetesExecutor.**

#### LocalExecutor
- Architecture: Single machine, multiprocessing queue
- Scalability: ~32 parallel tasks
- Use case: Development, small production

#### CeleryExecutor
- Architecture: Distributed, message broker (Redis/RabbitMQ)
- Scalability: 100s-1000s parallel tasks
- Use case: Medium to large production

#### KubernetesExecutor
- Architecture: Container-based, ephemeral pods
- Scalability: 1000s-10000s parallel tasks
- Use case: Cloud-native, large-scale production

**Diagrams**: 12+ Mermaid diagrams (architecture, sequence flows, pod lifecycle)

**Comparison matrix**: Feature comparison, performance timeline, selection guide

**Use this for**: Choosing the right executor for your deployment

### 3. [state_machines.md](state_machines.md)

**Detailed state transition rules and edge cases.**

- DAG run state transitions with conditions
- Task instance state transitions (all 14 states)
- Retry logic with exponential backoff
- Sensor reschedule mode (poke vs reschedule)
- Deferrable operators (async execution)
- Edge cases:
  - Cleared tasks (user intervention)
  - Removed tasks (DAG definition changes)
  - Upstream failed propagation
  - Zombie tasks (worker crashes)

**Diagrams**: 10+ Mermaid diagrams (stateDiagram-v2, flowchart, sequenceDiagram)

**Use this for**: Understanding state transitions, debugging task failures, handling retries

## Quick Navigation

### By Task

| I want to... | See |
|--------------|-----|
| Understand the complete lifecycle | [lifecycle_overview.md](lifecycle_overview.md) |
| Choose an executor | [executors_comparison.md](executors_comparison.md) - Selection Guide |
| Debug a stuck task | [state_machines.md](state_machines.md) - Task Instance States |
| Configure retries | [state_machines.md](state_machines.md) - Retry Logic |
| Understand sensor behavior | [state_machines.md](state_machines.md) - Sensor Reschedule |
| Deploy to Kubernetes | [executors_comparison.md](executors_comparison.md) - KubernetesExecutor |
| Scale with Celery | [executors_comparison.md](executors_comparison.md) - CeleryExecutor |

### By Component

| Component | Main File | Section |
|-----------|-----------|----------|
| **DagRun** | lifecycle_overview.md | DAG Run States, Key Components |
| **TaskInstance** | lifecycle_overview.md | Task Instance States |
| **Scheduler** | lifecycle_overview.md | Complete Lifecycle Flow |
| **LocalExecutor** | executors_comparison.md | LocalExecutor |
| **CeleryExecutor** | executors_comparison.md | CeleryExecutor |
| **KubernetesExecutor** | executors_comparison.md | KubernetesExecutor |
| **State Transitions** | state_machines.md | All sections |

## Source Code References

Key files in Airflow codebase:

### Models
- `airflow-core/src/airflow/models/dagrun.py` - DagRun class
  - `set_state()` at line ~462
  - `update_state()` at line ~1200
- `airflow-core/src/airflow/models/taskinstance.py` - TaskInstance class
  - `run()` method
  - `is_eligible_to_retry()`
- `airflow-core/src/airflow/utils/state.py` - State enums
  - `DagRunState` at line 81
  - `TaskInstanceState` at line 50

### Scheduler
- `airflow-core/src/airflow/jobs/scheduler_job_runner.py`
  - `_start_queued_dagruns()` at line ~1900
  - `_schedule_dag_run()` at line ~2000

### Executors
- `airflow-core/src/airflow/executors/base_executor.py` - Base interface
- `airflow-core/src/airflow/executors/local_executor.py` - LocalExecutor
- `providers/celery/src/airflow/providers/celery/executors/celery_executor.py` - CeleryExecutor
- `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py` - KubernetesExecutor

## Diagram Color Scheme

Consistent colors used across all diagrams:

- **Cyan (#4ecdc4)**: Scheduler/Dag Processor
- **Yellow (#ffd93d)**: Queues/Databases/Critical fields
- **Green (#95e1d3, #b2f2bb)**: Workers/Success states
- **Red (#ffe3e3, #e03131)**: Failed states/Critical decisions
- **Orange (#ffec99, #f08c00)**: Retry states/Intermediate
- **Blue (#d0ebff, #1971c2)**: Loops/Async operations

## Related Documentation

For related topics, see:

- **Scheduler**: `files/docs/scheduler/` - How the scheduler decides when to create DAG runs
- **Security**: Airflow docs on auth managers and permissions
- **Configuration**: `airflow-core/src/airflow/config_templates/config.yml`

## Summary

### DAG Run Lifecycle (6 Phases)

1. **Creation**: Scheduler creates DAG run (QUEUED)
2. **Start**: Scheduler sets DAG run to RUNNING
3. **Task Scheduling**: Tasks with met dependencies set to SCHEDULED
4. **Task Execution**: Executor runs tasks (QUEUED → RUNNING → terminal)
5. **State Evaluation**: Scheduler evaluates overall state (SUCCESS/FAILED)
6. **Completion**: DAG run reaches terminal state, end_date set

### Task Execution Flow

```
NULL → SCHEDULED → QUEUED → RUNNING → SUCCESS/FAILED
                                    ↓
                                UP_FOR_RETRY → SCHEDULED
```

### Executor Selection

```
Development → LocalExecutor
Small Production (<50 DAGs) → LocalExecutor
Medium Production (50-500 DAGs) → CeleryExecutor
Large Production (>500 DAGs) → KubernetesExecutor
```

---

**All documentation includes detailed Mermaid diagrams that render in GitHub, GitLab, and markdown viewers.**
