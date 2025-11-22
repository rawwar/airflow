# State Machines - Detailed Transition Rules

This document provides detailed state transition rules for DAG runs and task instances in Apache Airflow.

## Table of Contents

1. [DAG Run State Machine](#dag-run-state-machine)
2. [Task Instance State Machine](#task-instance-state-machine)
3. [Retry Logic](#retry-logic)
4. [Sensor Reschedule](#sensor-reschedule)
5. [Deferrable Operators](#deferrable-operators)
6. [Edge Cases](#edge-cases)

---

## DAG Run State Machine

### State Definitions

**Source**: `airflow-core/src/airflow/utils/state.py:81`

```python
class DagRunState(str, Enum):
    QUEUED = "queued"      # Created, waiting to start
    RUNNING = "running"    # Actively executing tasks
    SUCCESS = "success"    # All required tasks succeeded
    FAILED = "failed"      # At least one required task failed
```

### State Transition Diagram

```mermaid
stateDiagram-v2
    [*] --> QUEUED: DagRun created
    QUEUED --> RUNNING: Scheduler starts execution
    RUNNING --> SUCCESS: All required tasks SUCCESS
    RUNNING --> FAILED: Any required task FAILED
    SUCCESS --> [*]
    FAILED --> [*]
    
    note right of QUEUED
        Trigger: create_dag_run()
        Set: queued_at timestamp
        Condition: Always starts here
    end note
    
    note right of RUNNING
        Trigger: _start_queued_dagruns()
        Set: start_date timestamp
        Condition: Scheduler picks up queued run
    end note
    
    note right of SUCCESS
        Trigger: update_state()
        Set: end_date timestamp
        Condition: All tasks in terminal success states
    end note
    
    note right of FAILED
        Trigger: update_state()
        Set: end_date timestamp
        Condition: Any task FAILED with no retries
    end note
```

### Transition Rules

#### QUEUED → RUNNING

**Trigger**: `SchedulerJobRunner._start_queued_dagruns()` (line ~1900)

**Conditions**:
- DAG run state is QUEUED
- DAG run run_type is not BACKFILL_JOB
- Scheduler has capacity (max_dagruns_to_create_per_loop)

**Actions**:
```python
dag_run.state = DagRunState.RUNNING
dag_run.start_date = timezone.utcnow()
session.flush()
```

#### RUNNING → SUCCESS

**Trigger**: `DagRun.update_state()` (line ~1200)

**Conditions**:
- All required task instances are in SUCCESS or SKIPPED state
- No task instances in RUNNING, QUEUED, SCHEDULED states
- No task instances in UP_FOR_RETRY or UP_FOR_RESCHEDULE

**Actions**:
```python
dag_run.state = DagRunState.SUCCESS
dag_run.end_date = timezone.utcnow()
session.flush()
```

**Logic**:
```python
# Required tasks = tasks not skipped by branching
required_tasks = [ti for ti in task_instances if ti.state != State.SKIPPED]

if all(ti.state == State.SUCCESS for ti in required_tasks):
    dag_run.set_state(DagRunState.SUCCESS)
```

#### RUNNING → FAILED

**Trigger**: `DagRun.update_state()`

**Conditions**:
- At least one required task instance is in FAILED state
- Task has no retries remaining
- Or task is marked as fail_stop

**Actions**:
```python
dag_run.state = DagRunState.FAILED
dag_run.end_date = timezone.utcnow()
session.flush()
```

---

## Task Instance State Machine

### State Definitions

**Source**: `airflow-core/src/airflow/utils/state.py:50`

```python
class TaskInstanceState(str, Enum):
    # Initial state
    NULL = None
    
    # Execution states
    SCHEDULED = "scheduled"          # Ready to run
    QUEUED = "queued"                # In executor queue
    RUNNING = "running"              # Actively executing
    
    # Terminal states
    SUCCESS = "success"              # Completed successfully
    FAILED = "failed"                # Failed (no retries)
    SKIPPED = "skipped"              # Skipped by branching
    UPSTREAM_FAILED = "upstream_failed"  # Upstream dependency failed
    REMOVED = "removed"              # Task removed from DAG
    
    # Intermediate states
    UP_FOR_RETRY = "up_for_retry"    # Failed, will retry
    UP_FOR_RESCHEDULE = "up_for_reschedule"  # Sensor waiting
    DEFERRED = "deferred"            # Deferrable operator
    RESTARTING = "restarting"        # User cleared task
    SHUTDOWN = "shutdown"            # Executor shutdown
```

### Complete State Diagram

```mermaid
stateDiagram-v2
    [*] --> NULL
    
    NULL --> SCHEDULED: Dependencies met
    NULL --> UPSTREAM_FAILED: Upstream failed
    NULL --> REMOVED: Task removed from DAG
    
    SCHEDULED --> QUEUED: Sent to executor
    SCHEDULED --> UPSTREAM_FAILED: Upstream fails
    
    QUEUED --> RUNNING: Worker starts
    
    RUNNING --> SUCCESS: Task succeeds
    RUNNING --> FAILED: Task fails (no retries)
    RUNNING --> UP_FOR_RETRY: Task fails (retries left)
    RUNNING --> SKIPPED: Skipped by branching
    RUNNING --> UP_FOR_RESCHEDULE: Sensor defers
    RUNNING --> DEFERRED: Deferrable operator
    
    UP_FOR_RETRY --> SCHEDULED: Retry delay expires
    UP_FOR_RESCHEDULE --> SCHEDULED: Reschedule delay expires
    DEFERRED --> SCHEDULED: Trigger fires
    
    SUCCESS --> RESTARTING: User clears
    FAILED --> RESTARTING: User clears
    SKIPPED --> RESTARTING: User clears
    UPSTREAM_FAILED --> RESTARTING: User clears
    
    RESTARTING --> SCHEDULED: Rescheduled
    
    SUCCESS --> [*]
    FAILED --> [*]
    SKIPPED --> [*]
    UPSTREAM_FAILED --> [*]
    REMOVED --> [*]
```

---

## Retry Logic

### Retry Decision Flow

```mermaid
flowchart TD
    Start[Task execution fails] --> Check{is_eligible_to_retry?}
    
    Check -->|No - retries=0| Failed[Set state=FAILED]
    Check -->|No - try_number > max_tries| Failed
    Check -->|Yes| Retry[Set state=UP_FOR_RETRY]
    
    Retry --> CalcDelay[Calculate retry_delay]
    
    CalcDelay --> ExpBackoff{exponential_backoff?}
    ExpBackoff -->|Yes| Exponential[delay = base_delay * 2^(try_number-1)]
    ExpBackoff -->|No| Linear[delay = base_delay]
    
    Exponential --> Clamp[delay = min(delay, max_retry_delay)]
    Linear --> Clamp
    
    Clamp --> SetNext[Set next_try_date = now + delay]
    SetNext --> Wait[Wait for delay]
    Wait --> Reschedule[Scheduler sets state=SCHEDULED]
    Reschedule --> Execute[Execute again with try_number+1]
    
    style Check fill:#f08c00,color:#fff
    style Failed fill:#ffe3e3
    style Retry fill:#ffec99
    style ExpBackoff fill:#f08c00,color:#fff
    style Reschedule fill:#95e1d3
```

### Retry Configuration

**Task definition**:
```python
task = PythonOperator(
    task_id='example',
    retries=3,                          # Number of retries
    retry_delay=timedelta(minutes=5),   # Base delay
    retry_exponential_backoff=True,     # Enable exponential backoff
    max_retry_delay=timedelta(hours=1), # Maximum delay
)
```

### Retry Calculation

**Source**: `airflow-core/src/airflow/models/taskinstance.py`

```python
def get_retry_delay(self) -> timedelta:
    retry_delay = self.task.retry_delay
    
    if self.task.retry_exponential_backoff:
        # Exponential backoff: delay * 2^(try_number - 1)
        min_backoff = int(retry_delay.total_seconds() * (2 ** (self.try_number - 2)))
        retry_delay = timedelta(seconds=min_backoff)
        
        if self.task.max_retry_delay:
            retry_delay = min(retry_delay, self.task.max_retry_delay)
    
    return retry_delay
```

**Example retry delays** (base_delay=5min, exponential=True):
- Try 1 fails → Wait 5 minutes (5 * 2^0)
- Try 2 fails → Wait 10 minutes (5 * 2^1)
- Try 3 fails → Wait 20 minutes (5 * 2^2)
- Try 4 fails → Wait 40 minutes (5 * 2^3)

---

## Sensor Reschedule

### Reschedule Mode

Sensors can operate in two modes:

1. **Poke mode** (default): Blocks worker, polls continuously
2. **Reschedule mode**: Releases worker, reschedules later

### Reschedule Flow

```mermaid
sequenceDiagram
    participant Sch as Scheduler
    participant TI as TaskInstance
    participant Sensor as Sensor
    participant DB as Database
    
    Sch->>TI: Schedule sensor task
    TI->>Sensor: execute()
    Sensor->>Sensor: poke()
    
    alt Condition met
        Sensor-->>TI: Return True
        TI->>DB: Set state=SUCCESS
    else Condition not met - Timeout not reached
        Sensor-->>TI: Raise AirflowRescheduleException
        TI->>DB: Set state=UP_FOR_RESCHEDULE
        TI->>DB: Set reschedule_date = now + poke_interval
        Note over TI: Worker released, task not running
    else Timeout reached
        Sensor-->>TI: Raise AirflowSensorTimeout
        TI->>DB: Set state=FAILED
    end
    
    Note over Sch,DB: Wait for reschedule_date
    
    Sch->>DB: Query tasks WHERE reschedule_date <= NOW()
    DB-->>Sch: Return sensor task
    Sch->>TI: Set state=SCHEDULED
    Sch->>TI: Re-execute sensor
```

**Configuration**:
```python
sensor = FileSensor(
    task_id='wait_for_file',
    filepath='/path/to/file',
    mode='reschedule',           # Enable reschedule mode
    poke_interval=60,            # Check every 60 seconds
    timeout=3600,                # Fail after 1 hour
)
```

---

## Deferrable Operators

### Deferrable Execution Flow

```mermaid
sequenceDiagram
    participant Sch as Scheduler
    participant TI as TaskInstance
    participant Op as Deferrable Operator
    participant Trig as Triggerer
    participant DB as Database
    
    Sch->>TI: Schedule task
    TI->>Op: execute()
    Op->>Op: Create Trigger object
    Op->>DB: Store trigger (serialized)
    Op->>TI: Raise TaskDeferred exception
    TI->>DB: Set state=DEFERRED
    TI->>DB: Set trigger_id
    Note over TI: Worker released immediately
    
    Note over Trig: Triggerer process polls triggers
    
    Trig->>DB: Query deferred tasks
    DB-->>Trig: Return triggers
    Trig->>Trig: Run trigger.run() async
    
    alt Trigger fires (condition met)
        Trig->>DB: Create TriggerEvent
        Trig->>DB: Mark trigger complete
        Note over Sch: Scheduler picks up event
        Sch->>DB: Set task state=SCHEDULED
        Sch->>TI: Re-execute task with event data
        TI->>Op: execute_complete(event)
        Op->>DB: Set state=SUCCESS
    else Trigger times out
        Trig->>DB: Create TriggerEvent (timeout)
        Sch->>DB: Set task state=SCHEDULED
        TI->>Op: execute_complete(timeout_event)
        Op->>DB: Set state=FAILED
    end
```

**Example**:
```python
from airflow.providers.http.sensors.http import HttpSensorAsync
from airflow.triggers.temporal import TimeDeltaTrigger

task = HttpSensorAsync(
    task_id='wait_for_api',
    endpoint='/api/status',
    # Deferrable - releases worker while waiting
)
```

---

## Edge Cases

### Cleared Tasks

```mermaid
flowchart TD
    Term[Task in terminal state] --> User[User clicks Clear]
    User --> Restart[State set to RESTARTING]
    Restart --> Check{Downstream<br/>cascade?}
    
    Check -->|Yes - recursive| ClearDown[Clear downstream tasks]
    Check -->|No| Schedule[Set state=SCHEDULED]
    
    ClearDown --> Schedule
    Schedule --> Execute[Task re-executed]
    
    style Term fill:#b2f2bb
    style Restart fill:#ffec99
    style Check fill:#f08c00,color:#fff
    style Schedule fill:#95e1d3
```

### Removed Tasks

**Scenario**: Task removed from DAG definition but TaskInstance exists in DB

```mermaid
flowchart TD
    Sch[Scheduler evaluates DAG run] --> Query[Query task instances]
    Query --> Compare[Compare with DAG definition]
    Compare --> Missing{Task in DB<br/>not in DAG?}
    
    Missing -->|Yes| Remove[Set state=REMOVED]
    Missing -->|No| Normal[Normal processing]
    
    Remove --> Update[Update DAG run state]
    Normal --> Update
    
    style Missing fill:#e03131,color:#fff
    style Remove fill:#ffe3e3
    style Normal fill:#95e1d3
```

### Upstream Failed Propagation

```mermaid
flowchart TB
    T1[Task 1<br/>FAILED] --> T2[Task 2<br/>depends_on_past=False]
    T1 --> T3[Task 3<br/>depends_on_past=False]
    T2 --> T4[Task 4]
    T3 --> T4
    
    T1 -.->|trigger_rule=all_success| UF2[Task 2<br/>UPSTREAM_FAILED]
    T1 -.->|trigger_rule=all_success| UF3[Task 3<br/>UPSTREAM_FAILED]
    UF2 -.->|propagate| UF4[Task 4<br/>UPSTREAM_FAILED]
    UF3 -.->|propagate| UF4
    
    style T1 fill:#ffe3e3
    style UF2 fill:#ffe3e3
    style UF3 fill:#ffe3e3
    style UF4 fill:#ffe3e3
```

**Trigger rule effects**:

```python
# Task runs only if all upstream succeeded (default)
task_a = PythonOperator(..., trigger_rule='all_success')

# Task runs even if upstream failed
task_b = PythonOperator(..., trigger_rule='all_done')

# Task runs only if all upstream failed
task_c = PythonOperator(..., trigger_rule='all_failed')
```

### Zombie Tasks

**Scenario**: Task marked RUNNING but worker crashed

```mermaid
sequenceDiagram
    participant Sch as Scheduler
    participant DB as Database
    participant W as Worker (crashed)
    
    Note over W: Worker crashes mid-execution
    W-xDB: Connection lost
    
    Note over Sch: Scheduler heartbeat
    Sch->>DB: Query running tasks
    DB-->>Sch: Return task (RUNNING, heartbeat old)
    
    Sch->>Sch: Check: heartbeat_timestamp + grace_period < NOW()?
    
    alt Zombie detected
        Sch->>DB: Set state=FAILED
        Sch->>DB: Add log: Detected as zombie
        Note over Sch: Or set state=UP_FOR_RETRY if retries remain
    else Still alive
        Sch->>Sch: Continue monitoring
    end
```

**Configuration**:
```yaml
[scheduler]
# Consider task zombie if no heartbeat for this duration
scheduler_zombie_task_threshold = 300
```

---

## Summary

### Key State Transition Methods

**DagRun**:
- `set_state()` - Manually set state with timestamps
- `update_state()` - Calculate state from task instances

**TaskInstance**:
- `run()` - Execute task, handle state transitions
- `is_eligible_to_retry()` - Check if retry possible
- `refresh_from_db()` - Sync with database state

### Terminal States

**DAG Run**: SUCCESS, FAILED

**Task Instance**: SUCCESS, FAILED, SKIPPED, UPSTREAM_FAILED, REMOVED

**No further transitions possible from terminal states unless user intervention (clear task).**

### State Change Triggers

1. **Scheduler**: NULL → SCHEDULED, QUEUED → RUNNING
2. **Executor**: SCHEDULED → QUEUED
3. **Worker**: RUNNING → terminal states
4. **User**: Terminal → RESTARTING → SCHEDULED

**Next Steps**: See `lifecycle_overview.md` for complete flow and `executors_comparison.md` for executor-specific behavior.
