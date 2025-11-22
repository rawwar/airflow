# Task Execution Documentation - CeleryExecutor

Comprehensive guide to understanding and debugging task execution on CeleryExecutor, from scheduler queuing to task completion.

## Quick Links

| Resource | Description |
|----------|-------------|
| **[celery_task_lifecycle.md](celery_task_lifecycle.md)** | Main documentation (2,000+ lines, 15+ diagrams) |
| **[excalidraw/](excalidraw/)** | Editable diagrams (5 files) |
| **[excalidraw/README.md](excalidraw/README.md)** | Diagram usage guide |

## What's Inside

### Main Documentation: celery_task_lifecycle.md

**1. Overview**
- CeleryExecutor fundamentals
- Execution phases (scheduler → broker → worker → subprocess → completion)
- Architecture diagram

**2. Architecture Components**
- Scheduler, broker (Redis/RabbitMQ), worker, metadata DB
- Component interactions

**3. Complete Execution Flow**
- 10-phase detailed sequence
- Timeline with typical durations
- State transitions

**4. Task Command Execution**
- `airflow tasks run` command structure
- Subprocess execution flow
- Key files reference

**5. XCom Operations**
- Push/pull workflows
- Serialization (JSON vs Pickle)
- Table schema, size limits, cleanup
- Best practices

**6. Variable Access**
- `Variable.get()` flow with caching
- Cache hit/miss performance (10,000x faster!)
- Encryption (Fernet)
- Context access patterns

**7. Database Connections**
- Session management (scoped_session)
- Connection pool configuration
- Query examples in tasks
- Transaction handling

**8. Process Management**
- Worker process architecture (main + pool + monitor)
- Process spawning and monitoring
- Timeouts, graceful shutdown, supervision
- Inspection commands

**9. Logging and Monitoring**
- Log architecture (local, remote)
- Configuration options
- Metrics (StatsD)
- Health checks

**10. Debugging Guide**
- 5 common issues with solutions:
  1. Task stuck in QUEUED
  2. DB connection errors
  3. XCom not found
  4. Variable not found
  5. Task timeout
- Debugging tools and queries
- Performance optimization

### Excalidraw Diagrams

**01_complete_flow.excalidraw**  
End-to-end task execution with timeline

**02_xcom_operations.excalidraw**  
XCom push/pull with serialization paths

**03_variable_access.excalidraw**  
Variable.get() cache decision tree

**04_process_architecture.excalidraw**  
Celery worker process hierarchy

**05_debugging_flowchart.excalidraw**  
Common issues troubleshooting

## Quick Reference

### Essential Commands

```bash
# Start worker
airflow celery worker --concurrency 16

# Inspect workers
airflow celery inspect active
airflow celery inspect stats

# Check broker (Redis)
redis-cli ping
redis-cli llen default

# Test task
airflow tasks test <dag_id> <task_id> <date>

# View logs
cat logs/<dag_id>/<task_id>/<date>/<try>.log
```

### Key Files

| Component | File | Key Methods |
|-----------|------|-------------|
| **CeleryExecutor** | `providers/celery/src/airflow/providers/celery/executors/celery_executor.py` | `queue_task_instance()`, `sync()`, `heartbeat()` |
| **TaskInstance** | `airflow-core/src/airflow/models/taskinstance.py` | `_run_raw_task()`, `xcom_push()`, `xcom_pull()` |
| **XCom** | `airflow-core/src/airflow/models/xcom.py` | `set()`, `get_many()` |
| **Variable** | `airflow-core/src/airflow/models/variable.py` | `get()`, `set()` |

### Debugging Checklist

**Task stuck in QUEUED?**
- ☑️ Worker running?
- ☑️ Broker accessible?
- ☑️ Queue name correct?
- ☑️ DB connection healthy?

**DB connection errors?**
- ☑️ Pool exhausted? (increase `pool_size`)
- ☑️ Stale connections? (enable `pool_pre_ping`)
- ☑️ Long-running queries?

**XCom not found?**
- ☑️ Upstream task ran?
- ☑️ Correct key and task_id?
- ☑️ Same DAG run?
- ☑️ Serialization issues?

## Related Documentation

- **Scheduler**: `../scheduler/` - How DAG runs are created
- **DAG Run Lifecycle**: `../dag_run_lifecycle/` - States and executors comparison
- **Airflow Docs**: https://airflow.apache.org/docs/apache-airflow-providers-celery/

## How to Use This Documentation

**For understanding flow**:
1. Start with main doc Overview section
2. Follow Complete Execution Flow
3. View excalidraw diagrams for visual understanding

**For debugging issues**:
1. Go directly to Debugging Guide section
2. Find your issue in the 5 common scenarios
3. Use debugging flowchart diagram
4. Run suggested commands

**For optimizing performance**:
1. Read Process Management section
2. Review Database Connections
3. Check Performance Optimization tips
4. Review XCom and Variable best practices

---

**Version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow with CeleryExecutor
