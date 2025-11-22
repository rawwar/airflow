# Excalidraw Diagrams - DAG Run Lifecycle

Interactive diagrams for Apache Airflow DAG run lifecycle documentation. These diagrams can be edited at [excalidraw.com](https://excalidraw.com) by opening the `.excalidraw` JSON files.

## Files

### 1. `01_complete_lifecycle.excalidraw`

**Complete DAG run lifecycle with all 6 phases**

- Phase 1: DAG Parsing (Dag Processor)
- Phase 2: DAG Run Creation (Scheduler)
- Phase 3: DAG Run Start (QUEUED → RUNNING)
- Phase 4: Task Scheduling (NULL → SCHEDULED → QUEUED)
- Phase 5: Task Execution (QUEUED → RUNNING → SUCCESS/FAILED)
- Phase 6: State Evaluation (Calculate DAG run state)
- Database interactions (dashed lines)
- Process flow (solid arrows)

**Use for**: Understanding the end-to-end flow from DAG file to completion

### 2. `02_executor_comparison.excalidraw`

**Side-by-side comparison of three executors**

- **LocalExecutor**: Single machine, multiprocessing queue, ~32 parallel tasks
- **CeleryExecutor**: Distributed workers, message broker, 100s-1000s tasks
- **KubernetesExecutor**: Ephemeral pods, K8s API, 1000s-10000s tasks
- Characteristics comparison (pros/cons)
- Architecture diagrams for each

**Use for**: Choosing the right executor for your deployment

### 3. `03_state_machines.excalidraw`

**Combined state machines for DAG runs and task instances**

**DAG Run States (4)**:
- QUEUED → RUNNING → SUCCESS/FAILED
- Terminal states: SUCCESS, FAILED

**Task Instance States (14 - key states shown)**:
- NULL → SCHEDULED → QUEUED → RUNNING → SUCCESS/FAILED
- Retry flow: RUNNING → UP_FOR_RETRY → SCHEDULED (orange arrows)
- Terminal states: SUCCESS, FAILED, SKIPPED, UPSTREAM_FAILED, REMOVED

**Use for**: Understanding state transitions and debugging task issues

### 4. `04_kubernetes_pods.excalidraw`

**Detailed Kubernetes pod lifecycle for task execution**

**Pod States**:
- Pending: Pod created, waiting for scheduling, image pull
- Running: Container executing, task running
- Succeeded: Exit code 0, task SUCCESS
- Failed: Exit code != 0, task FAILED
- Deleted: Cleanup after completion

**Components**:
- Scheduler Pod (with KubernetesExecutor)
- Kubernetes API Server
- Worker Pods (ephemeral)
- Configuration examples

**Use for**: Understanding how KubernetesExecutor creates and manages pods

### 5. `05_retry_logic.excalidraw`

**Task retry logic with exponential backoff**

**Decision Flow**:
- Task fails → Check eligibility → UP_FOR_RETRY or FAILED
- Calculate retry delay (exponential backoff)
- Wait for delay
- Reschedule (SCHEDULED)
- Re-execute with incremented try_number

**Formula**: `delay = base_delay * (2 ** (try_number - 1))`

**Example delays** (base=5min):
- Try 1 fails → wait 5 minutes
- Try 2 fails → wait 10 minutes
- Try 3 fails → wait 20 minutes
- Try 4 fails → wait 40 minutes (capped at max_retry_delay)

**Use for**: Configuring retry behavior and understanding backoff strategy

## Usage

### View Diagrams

1. Go to [excalidraw.com](https://excalidraw.com)
2. Click "Open" or drag the `.excalidraw` file
3. Diagram will load with all elements

### Edit Diagrams

1. Open diagram in Excalidraw
2. Use tools to modify:
   - Select (V): Click and drag elements
   - Rectangle (R): Draw boxes
   - Diamond (D): Decision points
   - Ellipse (O): State circles
   - Arrow (A): Connections
   - Text (T): Labels
   - Line (L): Simple lines
3. Export as PNG/SVG or save JSON

### Color Scheme

Consistent colors across all diagrams (matching Mermaid docs):

- **Cyan (#4ecdc4)**: Scheduler/Dag Processor operations
- **Yellow (#ffd93d)**: Queues/Databases/Critical fields
- **Green (#95e1d3, #b2f2bb)**: Workers/Success states
- **Red (#ffe3e3, #e03131)**: Failed states/Critical decisions
- **Orange (#ffec99, #f08c00)**: Retry/Intermediate states
- **Blue (#d0ebff, #1971c2)**: Loops/Async operations

## Integration with Documentation

These diagrams complement the Mermaid diagrams in the main markdown files:

- **Mermaid diagrams**: Embedded in markdown, version-controlled, render in GitHub
- **Excalidraw diagrams**: Editable, presentation-ready, more visual flexibility

### Corresponding Markdown Files

| Excalidraw File | Markdown File | Section |
|----------------|---------------|----------|
| 01_complete_lifecycle.excalidraw | lifecycle_overview.md | Complete Lifecycle Flow |
| 02_executor_comparison.excalidraw | executors_comparison.md | All sections |
| 03_state_machines.excalidraw | state_machines.md, lifecycle_overview.md | State machines |
| 04_kubernetes_pods.excalidraw | executors_comparison.md | KubernetesExecutor |
| 05_retry_logic.excalidraw | state_machines.md | Retry Logic |

## Tips for Editing

1. **Maintain alignment**: Use Shift+drag to constrain movement
2. **Duplicate elements**: Cmd/Ctrl+D for consistency
3. **Group related items**: Cmd/Ctrl+G to move together
4. **Lock elements**: Right-click → Lock to prevent accidental moves
5. **Snap to grid**: Enable in settings for cleaner layouts
6. **Export options**: PNG (presentations), SVG (scalable), JSON (editable)

## Export for Presentations

1. Open diagram in Excalidraw
2. File → Export image
3. Choose format:
   - **PNG**: For slides (recommended: 2x scale)
   - **SVG**: For vector graphics
   - **Dark mode**: Toggle theme before export
4. Include in presentations or documentation

## Related Documentation

- **Main docs**: `files/docs/dag_run_lifecycle/README.md`
- **Lifecycle overview**: `files/docs/dag_run_lifecycle/lifecycle_overview.md`
- **Executors**: `files/docs/dag_run_lifecycle/executors_comparison.md`
- **State machines**: `files/docs/dag_run_lifecycle/state_machines.md`
- **Scheduler docs**: `files/docs/scheduler/` (includes more Excalidraw examples)

---

**All diagrams are created for the Apache Airflow project and follow Airflow's architectural patterns.**
