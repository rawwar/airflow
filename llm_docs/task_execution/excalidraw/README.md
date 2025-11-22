# Excalidraw Diagrams - Task Execution on CeleryExecutor

This folder contains editable Excalidraw diagrams that visualize task execution flow, XCom operations, variable caching, process architecture, and debugging workflows.

## Files

### 01_complete_flow.excalidraw
**Complete Task Execution Flow**

Visualizes the end-to-end journey of a task from scheduler to completion:
- Phase 1: Scheduler queues task
- Phase 2: Message broker receives task
- Phase 3: Celery worker polls and spawns process
- Phase 4: Task subprocess executes
- Database interactions (XCom, Variables, state updates)
- Timeline annotations (T=0ms to T=30s)

### 02_xcom_operations.excalidraw
**XCom Push & Pull Operations**

Detailed flow of XCom data sharing between tasks:
- Task 1 (producer) pushes data
- Serialization (JSON vs Pickle)
- Storage in xcom table
- Task 2 (consumer) pulls data
- Deserialization
- Size limits and best practices

### 03_variable_access.excalidraw
**Variable.get() with Caching**

Cache decision tree for Airflow variables:
- Cache HIT path (1μs response)
- Cache MISS path (10ms DB query)
- Decryption flow (if encrypted)
- Cache storage for subsequent calls
- 10,000x performance improvement

### 04_process_architecture.excalidraw
**Celery Worker Process Architecture**

Process hierarchy of a Celery worker:
- Main worker process (poll, dispatch, collect)
- Monitor thread (health, timeouts, signals)
- Process pool (16 workers by default)
- Task subprocess details (airflow tasks run command)
- Configuration options (concurrency, pool type)

### 05_debugging_flowchart.excalidraw
**Common Issues Debugging Flowchart**

Decision trees for troubleshooting:
- Issue 1: Task stuck in QUEUED (worker? broker?)
- Issue 2: DB connection errors (pool exhausted?)
- Issue 3: XCom not found (task ran? correct key?)
- Debugging commands reference
- Solutions for each scenario

## How to Use

### Viewing
1. Go to [excalidraw.com](https://excalidraw.com)
2. Click "Open" and upload any `.excalidraw` file
3. View and interact with the diagram

### Editing
1. Open file at excalidraw.com
2. Edit shapes, text, arrows, colors
3. Export as `.excalidraw` (JSON format)
4. Save back to this folder

### Exporting
- **PNG**: File → Export image → PNG
- **SVG**: File → Export image → SVG
- **PDF**: Print to PDF from browser

## Color Scheme

Consistent colors across all diagrams:

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Cyan** | `#4ecdc4` | Scheduler, main processes |
| **Yellow** | `#ffd93d` | Queues, databases, critical data |
| **Green** | `#95e1d3`, `#b2f2bb` | Workers, success states |
| **Red** | `#ffe3e3`, `#e03131` | Errors, failures, decisions |
| **Orange** | `#ffec99`, `#f08c00` | Intermediate states, warnings |
| **Blue** | `#d0ebff`, `#1971c2` | Monitoring, logs, info boxes |

## Tips

- **Zoom**: Mouse wheel or pinch gesture
- **Pan**: Hold space + drag
- **Multi-select**: Shift + click
- **Duplicate**: Ctrl/Cmd + D
- **Align**: Select multiple → right-click → Align

## Related Documentation

- Main doc: `../celery_task_lifecycle.md`
- Scheduler docs: `../../scheduler/`
- DAG run lifecycle: `../../dag_run_lifecycle/`

---

**Version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow CeleryExecutor
