# Deferrable Task & Triggerer Documentation

## Quick Reference

Comprehensive guide to understanding and debugging deferrable tasks in Apache Airflow.

### Files in This Directory

- **`deferrable_task_lifecycle.md`** (2,271 lines) - Complete lifecycle documentation
  - Overview and concepts
  - Phase-by-phase execution flow  
  - Database schema and SQL queries
  - Triggerer architecture and async event loop
  - Trigger implementation patterns
  - State transitions and failure recovery
  - Debugging guide with SQL queries
  - Performance tuning and capacity planning
  - Comparison with normal tasks

- **`excalidraw/`** - Visual diagrams (editable .excalidraw format)
  - Complete execution flow
  - Trigger table lifecycle
  - Triggerer process architecture
  - State machine diagrams
  - Debugging flowcharts

### Quick Start

**What are deferrable tasks?**
- Tasks that can pause execution and free worker resources while waiting
- Monitored by the Triggerer component (async event loop)
- Resume automatically when condition is met

**When to use?**
- Waiting > 1 minute for external resources
- Long-running job polling (EMR, Databricks)
- Time-based delays (hours/days)
- Resource-constrained worker pools

**When NOT to use?**
- Tasks executing quickly (< 1 minute)
- Frequent checks (< 30 seconds between polls)
- Heavy computation tasks

### Key Concepts

#### Database Tables

```sql
-- Trigger table
CREATE TABLE trigger (
    id SERIAL PRIMARY KEY,
    classpath VARCHAR(1000),    -- e.g. 'airflow.triggers.temporal.TimeDeltaTrigger'
    kwargs TEXT,                 -- Encrypted JSON
    created_date TIMESTAMP,
    triggerer_id INTEGER         -- Which triggerer owns this
);

-- Task instance columns
ALTER TABLE task_instance ADD:
    trigger_id INTEGER,          -- FK to trigger.id
    next_method VARCHAR(1000),   -- Callback method name
    next_kwargs TEXT,            -- Event payload JSON
    trigger_timeout TIMESTAMP;   -- Timeout timestamp
```

#### Execution Flow

1. **Task starts** - Worker begins execution
2. **Task defers** - Calls `self.defer(trigger=..., method='callback')`
3. **Trigger created** - INSERT into trigger table, task state=DEFERRED
4. **Worker freed** - Process exits, slot available
5. **Triggerer claims** - Async thread picks up trigger
6. **Monitoring** - Trigger runs in event loop, checks condition
7. **Trigger fires** - Condition met, yields TriggerEvent
8. **Task resumes** - state=SCHEDULED, scheduler re-queues
9. **Callback executes** - Worker calls callback method with event payload
10. **Task completes** - state=SUCCESS

### Common Debugging Commands

#### Check if triggerer is running

```bash
ps aux | grep triggerer
airflow jobs list  # Look for TriggererJob
```

#### Check trigger status

```sql
-- Find active triggers
SELECT t.id, t.classpath, t.triggerer_id, ti.dag_id, ti.task_id
FROM trigger t
JOIN task_instance ti ON ti.trigger_id = t.id
WHERE ti.state = 'deferred';

-- Check triggerer health
SELECT id, state, latest_heartbeat, hostname
FROM job
WHERE job_type = 'TriggererJob'  
ORDER BY latest_heartbeat DESC;
```

#### Start triggerer

```bash
# Foreground
airflow triggerer

# Background
airflow triggerer --daemon

# Check logs
tail -f logs/triggerer/<date>/triggerer.log
```

### Configuration

```ini
[triggerer]
capacity = 1000              # Max concurrent triggers per instance
job_heartbeat_sec = 5        # Heartbeat frequency
```

### Example: Convert Polling to Deferrable

**Before** (blocks worker):
```python
class MyS3Sensor(BaseSensorOperator):
    def execute(self, context):
        while not self.check_s3_key_exists():
            time.sleep(60)  # Blocks worker!
        return True
```

**After** (frees worker):
```python
from airflow.providers.amazon.aws.triggers.s3 import S3KeyTrigger

class MyS3Sensor(BaseSensorOperator):
    def execute(self, context):
        if self.check_s3_key_exists():
            return True
        
        self.defer(
            trigger=S3KeyTrigger(
                bucket=self.bucket,
                key=self.key,
                poll_interval=60
            ),
            method_name='execute_complete',
            timeout=timedelta(hours=1)
        )
    
    def execute_complete(self, context, event):
        return True  # Key exists!
```

### Resource Savings

**Example**: 100 sensors waiting 30 minutes each

- **Traditional**: 100 workers × 30 min = 50 worker-hours
- **Deferrable**: 2 workers × 1 min = 0.03 worker-hours
- **Savings**: 99.9%!

### Troubleshooting Quick Checklist

- [ ] Triggerer process running?
- [ ] Triggerer heartbeat recent (< 30s)?
- [ ] Trigger exists in database?
- [ ] Trigger has triggerer_id assigned?
- [ ] Triggerer capacity not exhausted?
- [ ] No exceptions in triggerer logs?
- [ ] Trigger timeout not expired?

### Architecture Overview

```
┌────────────┐     ┌────────────┐     ┌────────────┐
│ Scheduler  │     │ Triggerer  │     │   Worker   │
│            │     │            │     │            │
│ Schedules  │─────│ Monitors   │─────│ Executes   │
│ tasks      │     │ triggers   │     │ tasks      │
└────────────┘     └────────────┘     └────────────┘
      │                  │                  │
      └──────────────────┴──────────────────┘
                     Database
                   (trigger table)
```

### Related Documentation

- CeleryExecutor task execution: `../task_execution/celery_task_lifecycle.md`
- KubernetesExecutor task execution: `../task_execution_k8s/kubernetes_task_lifecycle.md`
- Scheduler DAG run creation: `../scheduler/dag_run_scheduling.md`
- DAG run lifecycle: `../dag_run_lifecycle/lifecycle_overview.md`

### Support

For detailed debugging, performance tuning, and implementation patterns, see the main documentation file.
