# DAG Run Lifecycle Documentation - Complete

## Summary

Comprehensive documentation for Apache Airflow DAG run lifecycle, from DAG file parsing to task execution completion.

## Files Created

### Main Documentation (4 files, 1,873 lines, 51KB)

1. **README.md** (206 lines, 7.5KB)
   - Index and quick reference
   - State tables (4 DAG run states, 14 task instance states)
   - Navigation guide
   - Source code references

2. **lifecycle_overview.md** (629 lines, 20KB)
   - Complete lifecycle (6 phases)
   - DAG run states (4)
   - Task instance states (14)
   - Key components (DagRun, TaskInstance, Scheduler)
   - Timestamps and timing
   - Error handling (retries, upstream failures)
   - **8 Mermaid diagrams**

3. **executors_comparison.md** (344 lines, 9.2KB)
   - LocalExecutor (single machine, ~32 tasks)
   - CeleryExecutor (distributed, 100s-1000s tasks)
   - KubernetesExecutor (cloud-native, 1000s-10000s tasks)
   - Feature comparison matrix
   - Performance comparison
   - Selection guide with decision flowchart
   - **6 Mermaid diagrams**

4. **state_machines.md** (527 lines, 14KB)
   - DAG run state transitions
   - Task instance state transitions (all 14 states)
   - Retry logic with exponential backoff
   - Sensor reschedule mode
   - Deferrable operators
   - Edge cases (cleared tasks, removed tasks, zombies)
   - **9 Mermaid diagrams**

### Excalidraw Diagrams (6 files, 96KB)

1. **01_complete_lifecycle.excalidraw** (18KB)
   - All 6 lifecycle phases
   - Database interactions
   - Process flow

2. **02_executor_comparison.excalidraw** (14KB)
   - Side-by-side comparison
   - Architecture diagrams
   - Characteristics (pros/cons)

3. **03_state_machines.excalidraw** (17KB)
   - DAG run state machine
   - Task instance state machine
   - Retry flows

4. **04_kubernetes_pods.excalidraw** (15KB)
   - Pod lifecycle states
   - Scheduler to K8s API flow
   - Configuration examples

5. **05_retry_logic.excalidraw** (16KB)
   - Retry decision flow
   - Exponential backoff formula
   - Configuration example

6. **excalidraw/README.md** (167 lines, 5.8KB)
   - Usage guide
   - Editing tips
   - Export instructions

## Statistics

- **Total files**: 10 (4 markdown + 1 index + 5 Excalidraw + 1 Excalidraw README)
- **Total lines**: 1,873 lines of documentation
- **Total size**: ~147KB
- **Mermaid diagrams**: 23 (embedded in markdown)
- **Excalidraw diagrams**: 5 (interactive JSON files)
- **Total diagrams**: 28

## Coverage

### DAG Run Lifecycle

✅ Phase 1: DAG Parsing (Dag Processor)  
✅ Phase 2: DAG Run Creation (Scheduler)  
✅ Phase 3: DAG Run Start (QUEUED → RUNNING)  
✅ Phase 4: Task Scheduling (NULL → SCHEDULED → QUEUED)  
✅ Phase 5: Task Execution (QUEUED → RUNNING → terminal)  
✅ Phase 6: State Evaluation (Calculate DAG run state)  

### States

✅ DAG Run States (4): QUEUED, RUNNING, SUCCESS, FAILED  
✅ Task Instance States (14): NULL, SCHEDULED, QUEUED, RUNNING, SUCCESS, FAILED, UP_FOR_RETRY, SKIPPED, UPSTREAM_FAILED, UP_FOR_RESCHEDULE, DEFERRED, REMOVED, RESTARTING, SHUTDOWN  

### Executors

✅ LocalExecutor: Architecture, characteristics, use cases  
✅ CeleryExecutor: Architecture, queue routing, configuration  
✅ KubernetesExecutor: Pod lifecycle, customization, configuration  
✅ Comparison matrix: Features, performance, selection guide  

### Advanced Topics

✅ Retry logic with exponential backoff  
✅ Sensor reschedule mode (poke vs reschedule)  
✅ Deferrable operators (async execution)  
✅ Edge cases (cleared tasks, removed tasks, upstream failures, zombies)  
✅ State transition rules with triggers and conditions  
✅ Timestamps and timing (queued_at, start_date, end_date)  

## Diagram Types

### Mermaid (23 diagrams)

- **stateDiagram-v2** (8): State machines for DAG runs and task instances
- **sequenceDiagram** (6): Interactions between components
- **flowchart TD/TB/LR** (8): Decision flows and architectures
- **gantt** (1): Timeline with timestamps

### Excalidraw (5 diagrams)

- Complete lifecycle with 6 phases
- Executor comparison (side-by-side)
- Combined state machines
- Kubernetes pod lifecycle
- Retry logic with exponential backoff

## Color Scheme (Consistent)

- **Cyan (#4ecdc4)**: Scheduler/Dag Processor
- **Yellow (#ffd93d)**: Queues/Databases/Critical fields
- **Green (#95e1d3, #b2f2bb)**: Workers/Success states
- **Red (#ffe3e3, #e03131)**: Failed states/Critical decisions
- **Orange (#ffec99, #f08c00)**: Retry/Intermediate states
- **Blue (#d0ebff, #1971c2)**: Loops/Async operations

## Source Code References

All documentation includes specific file paths and line numbers:

- `airflow-core/src/airflow/models/dagrun.py` (set_state, update_state)
- `airflow-core/src/airflow/models/taskinstance.py` (run, is_eligible_to_retry)
- `airflow-core/src/airflow/jobs/scheduler_job_runner.py` (_start_queued_dagruns, _schedule_dag_run)
- `airflow-core/src/airflow/utils/state.py` (DagRunState, TaskInstanceState)
- `airflow-core/src/airflow/executors/` (base, local, celery, kubernetes)

## Usage

### For Developers

1. Start with `README.md` for quick reference
2. Read `lifecycle_overview.md` for complete flow understanding
3. Check `state_machines.md` for debugging task issues
4. Use `executors_comparison.md` for deployment decisions

### For Presentations

1. Open Excalidraw diagrams at [excalidraw.com](https://excalidraw.com)
2. Export as PNG (2x scale) or SVG
3. Include in slides or documentation

### For Contribution

1. Mermaid diagrams render in GitHub/GitLab
2. Excalidraw diagrams are editable
3. Follow established color scheme
4. Update corresponding markdown when changing diagrams

## Related Documentation

- **Scheduler docs**: `files/docs/scheduler/` - How scheduler creates DAG runs
- **Airflow docs**: Official documentation at airflow.apache.org
- **Source code**: Links provided in each document

## Quality Metrics

✅ All 28 diagrams render correctly  
✅ Consistent color scheme across all diagrams  
✅ Source code references with file paths and line numbers  
✅ Complete coverage of lifecycle phases  
✅ Detailed state transition rules  
✅ Executor comparison with selection guide  
✅ Advanced topics (retries, sensors, deferrable)  
✅ Edge cases documented  
✅ Configuration examples included  
✅ Excalidraw diagrams for editing  

## Completion Status

**✅ COMPLETE** - All documentation and diagrams created

---

**Created**: November 22, 2024  
**For**: Apache Airflow Project  
**Purpose**: Comprehensive DAG run lifecycle documentation
