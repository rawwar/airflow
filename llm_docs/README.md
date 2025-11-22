# LLM Documentation - Complete Summary

Comprehensive documentation for understanding Apache Airflow internals: scheduler, DAG run lifecycle, and task execution on CeleryExecutor.

## Directory Structure

```
llm_docs/
├── scheduler/                    (7 files, 104KB)
│   ├── README.md                 Quick reference
│   ├── DIAGRAMS_OVERVIEW.md      Diagram guide
│   ├── dag_run_scheduling.md     Main doc (11 Mermaid diagrams)
│   └── excalidraw/
│       ├── 01_high_level_flow.excalidraw
│       ├── 02_scheduler_loop_detailed.excalidraw
│       ├── 03_critical_decision_point.excalidraw
│       └── README.md
├── dag_run_lifecycle/          (9 files)
│   ├── README.md                 Main index
│   ├── lifecycle_overview.md     DAG run & task instance states
│   ├── executors_comparison.md   Local, Celery, Kubernetes
│   ├── state_machines.md         Detailed state transitions
│   ├── DOCUMENTATION_COMPLETE.md Implementation notes
│   └── excalidraw/
│       ├── 01_complete_lifecycle.excalidraw
│       ├── 02_executor_comparison.excalidraw
│       ├── 03_state_machines.excalidraw
│       ├── 04_kubernetes_pods.excalidraw
│       ├── 05_retry_logic.excalidraw
│       └── README.md
└── task_execution/             (8 files)
    ├── README.md                 Quick reference & checklist
    ├── celery_task_lifecycle.md  Main doc (2,000+ lines, 15+ diagrams)
    └── excalidraw/
        ├── 01_complete_flow.excalidraw
        ├── 02_xcom_operations.excalidraw
        ├── 03_variable_access.excalidraw
        ├── 04_process_architecture.excalidraw
        ├── 05_debugging_flowchart.excalidraw
        └── README.md
```

## Total Files

- **26 files** total
- **13 markdown** files (~150KB)
- **13 excalidraw** diagrams (~110KB)

## Documentation Coverage

### 1. Scheduler (`scheduler/`)

**What it covers**:
- How scheduler creates DAG runs
- Critical scheduling decision: `next_dagrun_create_after <= NOW()`
- Multi-scheduler coordination with row locking
- Dag Processor vs Scheduler responsibilities
- Bug identified: Asset-triggered DAG NULL ordering issue

**Key diagrams**:
- High-level flow (DAG file → DagModel → DAG run)
- Scheduler loop with timing
- Critical decision point breakdown

**Read when**: Understanding why/when DAG runs are created

### 2. DAG Run Lifecycle (`dag_run_lifecycle/`)

**What it covers**:
- DAG run states: QUEUED → RUNNING → SUCCESS/FAILED
- Task instance states: NULL → SCHEDULED → QUEUED → RUNNING → terminal (14 states)
- Executor comparison: LocalExecutor, CeleryExecutor, KubernetesExecutor
- State machines with retry/reschedule/deferrable logic
- Performance characteristics per executor

**Key diagrams**:
- Complete lifecycle (5 phases)
- Executor architectures side-by-side
- State transition rules
- Kubernetes pod lifecycle
- Retry logic flowchart

**Read when**: Understanding DAG run progression and executor differences

### 3. Task Execution (`task_execution/`)

**What it covers**:
- Complete task execution flow on CeleryExecutor
- XCom operations (push/pull, serialization)
- Variable.get() with caching (10,000x faster!)
- Database connections and session management
- Process architecture (worker + pool + monitor)
- Logging and monitoring
- Debugging guide for 5 common issues

**Key diagrams**:
- End-to-end flow with timeline
- XCom push/pull with serialization paths
- Variable cache decision tree
- Celery worker process hierarchy
- Debugging flowchart

**Read when**: Debugging task execution issues or optimizing performance

## Quick Start Guide

### For Learning Airflow Internals

**Recommended reading order**:
1. `scheduler/dag_run_scheduling.md` - Understand DAG run creation
2. `dag_run_lifecycle/lifecycle_overview.md` - Understand states
3. `task_execution/celery_task_lifecycle.md` - Understand task execution

### For Debugging Issues

**Task stuck in QUEUED?**
→ `task_execution/celery_task_lifecycle.md` § Debugging Guide

**DAG not running on schedule?**
→ `scheduler/dag_run_scheduling.md` § Critical Decision Point

**Task states confusing?**
→ `dag_run_lifecycle/state_machines.md`

**Executor choice?**
→ `dag_run_lifecycle/executors_comparison.md`

**XCom not found?**
→ `task_execution/celery_task_lifecycle.md` § XCom Operations

### For Visual Learners

**All excalidraw diagrams can be**:
1. Opened at [excalidraw.com](https://excalidraw.com)
2. Edited interactively
3. Exported as PNG/SVG/PDF

**Best diagrams to start with**:
- `scheduler/excalidraw/01_high_level_flow.excalidraw`
- `dag_run_lifecycle/excalidraw/01_complete_lifecycle.excalidraw`
- `task_execution/excalidraw/01_complete_flow.excalidraw`

## Color Coding (Consistent Across All Docs)

| Color | Usage |
|-------|-------|
| **Cyan** (#4ecdc4) | Scheduler, main processes |
| **Yellow** (#ffd93d) | Queues, databases, critical data |
| **Green** (#95e1d3, #b2f2bb) | Workers, success states |
| **Red** (#ffe3e3, #e03131) | Errors, failures, decisions |
| **Orange** (#ffec99, #f08c00) | Intermediate states, warnings |
| **Blue** (#d0ebff, #1971c2) | Monitoring, logs, info boxes |

## Key Insights Documented

### Scheduler
- **Critical field**: `next_dagrun_create_after` determines when DAG run is created
- **Formula**: `data_interval_end + schedule_interval`
- **Multi-scheduler**: Uses `SELECT ... FOR UPDATE SKIP LOCKED`
- **Bug**: Asset-triggered DAGs have NULL ordering causing unpredictable execution

### DAG Run Lifecycle
- **LocalExecutor**: ~32 concurrent tasks, single machine
- **CeleryExecutor**: 100s of tasks, distributed
- **KubernetesExecutor**: 1000s of tasks, container isolation
- **State count**: 4 DAG run states, 14 task instance states
- **Retry**: UP_FOR_RETRY → wait → SCHEDULED

### Task Execution
- **XCom limit**: < 1 MB recommended
- **Variable caching**: 10,000x faster (1μs vs 10ms)
- **Worker pool**: 16 processes default (configurable)
- **Task timeout**: 30 minutes default
- **DB pool**: Default 5 connections, increase for high concurrency

## Source Files Referenced

All documentation maps to real Airflow source code:

**Scheduler**:
- `airflow-core/src/airflow/jobs/scheduler_job_runner.py` (lines 1900-2000+)
- `airflow-core/src/airflow/models/dag.py` (line 3370)

**Models**:
- `airflow-core/src/airflow/models/dagrun.py`
- `airflow-core/src/airflow/models/taskinstance.py`
- `airflow-core/src/airflow/models/xcom.py`
- `airflow-core/src/airflow/models/variable.py`

**Executors**:
- `airflow-core/src/airflow/executors/local_executor.py`
- `providers/celery/src/airflow/providers/celery/executors/celery_executor.py`
- `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py`

**States**:
- `airflow-core/src/airflow/utils/state.py` (lines 50, 81)

## Usage in Development

**For contributors**:
- Reference when making scheduler/executor changes
- Understand state transition implications
- Debug integration test failures

**For operators**:
- Troubleshoot production issues
- Optimize task execution performance
- Choose appropriate executor for workload

**For users**:
- Understand why DAGs behave certain ways
- Debug task stuck issues
- Optimize XCom/Variable usage

## Future Enhancements (TODOs)

- [ ] Add triggerer component documentation
- [ ] Document dynamic task mapping lifecycle
- [ ] Add sensor reschedule detailed flow
- [ ] Document deferred operator execution
- [ ] Add distributed lock mechanisms
- [ ] Document task group behavior
- [ ] Add dataset/asset trigger deep dive

---

**Total documentation effort**: ~5,000 lines of markdown, 26 diagrams  
**Version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow 2.x
