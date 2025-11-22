# DAG Run Scheduling: How Scheduler Determines When to Create DAG Runs

## Overview

This document explains the complete flow of how Airflow determines when a DAG run should be created, from DAG parsing to scheduler execution.

## High-Level Flow

```mermaid
graph LR
    A[DAG File] --> B[Dag Processor]
    B --> C[DagModel Table]
    C --> D[Scheduler]
    D --> E[DAG Run Creation]
    
    B -.calculates.-> F[next_dagrun_create_after]
    F -.stored in.-> C
    D -.queries.-> G[WHERE next_dagrun_create_after <= NOW]
    G -.from.-> C
```

## Complete Scheduling Flow

```mermaid
sequenceDiagram
    participant DF as DAG File
    participant DP as Dag Processor
    participant TT as Timetable
    participant DB as Database (DagModel)
    participant SC as Scheduler
    participant DR as DagRun
    
    Note over DF,DR: Phase 1: DAG Parsing (runs periodically)
    DP->>DF: Parse DAG definition
    DP->>DB: Query latest automated run
    DB-->>DP: Return last DagRun (if exists)
    DP->>TT: Calculate next_dagrun_info(last_data_interval)
    TT->>TT: Apply schedule logic<br/>(cron, timedelta, etc.)
    TT-->>DP: Return DagRunInfo<br/>(logical_date, run_after)
    DP->>DB: Update next_dagrun_create_after
    
    Note over DF,DR: Phase 2: Scheduling Loop (runs every ~1 second)
    SC->>DB: Query WHERE next_dagrun_create_after <= NOW()
    DB-->>SC: Return DAGs needing runs
    SC->>SC: Check max_active_runs
    SC->>DR: Create DagRun (state=QUEUED)
    SC->>TT: Calculate next run
    TT-->>SC: Return next DagRunInfo
    SC->>DB: Update next_dagrun_create_after
```

## Component Responsibilities

### 1. DAG Processor (Parsing Phase)

**File**: `airflow-core/src/airflow/dag_processing/collection.py`

**Responsibility**: Parse DAG files and calculate when the next DAG run should be created.

#### Key Steps:

1. **Parse DAG** from Python file
2. **Query Latest Automated Run**:
   - Fetches the most recent `SCHEDULED` or `BACKFILL_JOB` run (excludes manual runs)
   - Query: `SELECT * FROM dag_run WHERE dag_id = ? AND run_type IN ('scheduled', 'backfill') ORDER BY logical_date DESC LIMIT 1`
   - See `_get_latest_runs_stmt()` in `collection.py:95`

3. **Extract Last Data Interval**:
   - From the latest run, gets the `data_interval_start` and `data_interval_end`
   - This represents the time period the last run operated on

4. **Calculate Next Run Info**:
   - Calls `DagModel.calculate_dagrun_date_fields(dag, last_automated_data_interval)`
   - This delegates to the DAG's timetable

5. **Update DagModel Table** with three critical fields:
   - `next_dagrun`: The logical date (start of data interval) for the next run
   - `next_dagrun_create_after`: The actual timestamp when the run should be created
   - `next_dagrun_data_interval`: The data interval for the next run (JSON)

**Code Location**: `collection.py:554-556`
```python
if run_info.num_active_runs.get(dag.dag_id, 0) >= dm.max_active_runs:
    dm.next_dagrun_create_after = None  # Prevent new runs
else:
    dm.calculate_dagrun_date_fields(dag, last_automated_data_interval)
```

### 2. Timetable Logic (Schedule Calculation)

**File**: `airflow-core/src/airflow/timetables/interval.py`, `base.py`

**Responsibility**: Calculate when the next DAG run should occur based on the schedule.

#### Timetable Decision Flow

```mermaid
flowchart TD
    A[Start: next_dagrun_info called] --> B{First run?}
    B -->|Yes| C{catchup=True?}
    B -->|No| D[Get last run's end time]
    
    C -->|Yes| E[Use start_date]
    C -->|No| F[Skip to latest time]
    
    D --> G[Align to previous schedule]
    
    E --> H{start > end_date?}
    F --> H
    G --> H
    
    H -->|Yes| I[Return None<br/>No more runs]
    H -->|No| J[Calculate next scheduled time]
    
    J --> K[Return DagRunInfo<br/>data_interval + run_after]
```

#### Timetable.next_dagrun_info() Flow:

**Input**:
- `last_automated_data_interval`: DataInterval from the previous run (start, end)
- `restriction`: TimeRestriction containing:
  - `earliest`: DAG's `start_date`
  - `latest`: DAG's `end_date`
  - `catchup`: Whether to backfill missed runs

**Processing** (for interval-based timetables like CronDataIntervalTimetable):

1. **Determine Start Time**:
   - **If catchup=False**: Skip to latest possible time (skip missed runs)
   - **If catchup=True**: Start from DAG's `start_date` or last run's end
   - **If first run**: Use DAG's `start_date`
   - **If subsequent run**: Start from end of previous data interval

2. **Align to Schedule**:
   - For fixed schedules (e.g., `0 0 * * *` - daily at midnight), align to the schedule
   - For relative schedules (e.g., `timedelta(hours=1)`), no alignment needed

3. **Calculate End Time**:
   - Call `_get_next(start)` to find the next scheduled time after start
   - For cron: use croniter to calculate next execution time
   - For timedelta: add the delta to start

4. **Check End Date**:
   - If `start > end_date`, return None (no more runs)

**Output**: `DagRunInfo`
- `data_interval`: DataInterval(start, end) - the time period this run will process
- `run_after`: DateTime - when the run should be created (typically equals `end`)

**Example for Daily Schedule (`0 0 * * *`)**:
```
Last run: DataInterval(2024-01-01 00:00, 2024-01-02 00:00)
          run_after: 2024-01-02 00:00

Next run: DataInterval(2024-01-02 00:00, 2024-01-03 00:00)
          run_after: 2024-01-03 00:00  <- This is when scheduler will create the run
```

**Code Location**: `interval.py:86-115`

### 3. DagModel.calculate_dagrun_date_fields()

**File**: `airflow-core/src/airflow/models/dag.py:675`

**Responsibility**: Bridge between timetable logic and database fields.

```mermaid
flowchart TD
    A[Start: calculate_dagrun_date_fields] --> B[Call dag.next_dagrun_info]
    B --> C{Result is None?}
    C -->|Yes| D[Set all fields to NULL<br/>next_dagrun=NULL<br/>next_dagrun_create_after=NULL<br/>next_dagrun_data_interval=NULL]
    C -->|No| E[Extract from DagRunInfo]
    E --> F[next_dagrun = info.logical_date]
    F --> G[next_dagrun_create_after = info.run_after]
    G --> H[next_dagrun_data_interval = info.data_interval]
    D --> I[Log result]
    H --> I
    I --> J[End: Fields updated in memory]
```

**Process**:
1. Call `dag.next_dagrun_info(last_automated_data_interval)`
2. If result is None:
   - Set `next_dagrun = None`
   - Set `next_dagrun_create_after = None`
   - Set `next_dagrun_data_interval = None`
3. If result is DagRunInfo:
   - Set `next_dagrun = info.logical_date` (start of data interval)
   - Set `next_dagrun_create_after = info.run_after` (when to create run)
   - Set `next_dagrun_data_interval = info.data_interval` (JSON)

**Code Location**: `dag.py:675-705`

### 4. Scheduler (Execution Phase)

**File**: `airflow-core/src/airflow/jobs/scheduler_job_runner.py`

**Responsibility**: Query DAGs that need runs and create them.

#### Scheduling Loop (_do_scheduling method)

The scheduler runs in a loop, typically every few seconds. In each iteration:

```mermaid
flowchart TD
    A[Scheduler Loop Start] --> B[Query: dags_needing_dagruns]
    B --> C{Any DAGs found?}
    C -->|No| D[Sleep until next loop]
    C -->|Yes| E[For each DAG model]
    
    E --> F{Run already exists?}
    F -->|Yes| G[Skip to next DAG]
    F -->|No| H{max_active_runs reached?}
    
    H -->|Yes| G
    H -->|No| I[Create DagRun state=QUEUED]
    
    I --> J[Calculate next run info]
    J --> K[Update next_dagrun_create_after]
    K --> G
    
    G --> L{More DAGs?}
    L -->|Yes| E
    L -->|No| M[Commit transaction]
    M --> N[Start queued DagRuns]
    N --> O[Schedule task instances]
    O --> D
    
    D --> A
```

**Step 1: Query DAGs Needing Runs** (`DagModel.dags_needing_dagruns()`)

**File**: `dag.py:587-671`

**SQL Query** (simplified):
```sql
SELECT * FROM dag_model
WHERE 
    is_paused = FALSE
    AND is_stale = FALSE
    AND has_import_errors = FALSE
    AND (
        next_dagrun_create_after <= NOW()  -- Time to create the run!
        OR dag_id IN (asset_triggered_dags)  -- Asset triggered
    )
ORDER BY next_dagrun_create_after ASC  -- Earliest due first
LIMIT 10  -- Configurable: scheduler.max_dagruns_to_create_per_loop
FOR UPDATE SKIP LOCKED;  -- Multi-scheduler coordination
```

**Key Points**:
- **Time Check**: `next_dagrun_create_after <= NOW()` is THE critical check
- **Ordering**: Processes DAGs in order of due time (earliest first)
- **Limiting**: Only processes 10 DAGs per loop (configurable)
- **Locking**: Uses row-level locks with SKIP LOCKED for multi-scheduler support

**Code Location**: `dag.py:654-671`

**Step 2: Create DAG Runs** (`_create_dag_runs()`)

**File**: `scheduler_job_runner.py:1697-1780`

For each DAG model returned:

1. **Check if run already exists**:
   - Query: `SELECT dag_id, logical_date FROM dag_run WHERE (dag_id, logical_date) IN (...)`
   - Prevents duplicate runs if `next_dagrun_create_after` wasn't updated

2. **Check max_active_runs**:
   - Query: `SELECT dag_id, COUNT(*) FROM dag_run WHERE state IN ('queued', 'running') GROUP BY dag_id`
   - Skip if DAG already has max concurrent runs

3. **Create the run**:
   ```python
   dag.create_dagrun(
       run_id=dag.timetable.generate_run_id(...),
       logical_date=dag_model.next_dagrun,          # From DagModel
       data_interval=data_interval,                  # From DagModel
       run_after=dag_model.next_dagrun_create_after, # From DagModel
       run_type=DagRunType.SCHEDULED,
       triggered_by=DagRunTriggeredByType.TIMETABLE,
       state=DagRunState.QUEUED,
       creating_job_id=self.job.id,
       session=session,
   )
   ```

4. **Update DagModel for next run**:
   - Calls `dag_model.calculate_dagrun_date_fields(dag, data_interval)` again
   - This calculates when the NEXT run after this one should be created
   - Updates `next_dagrun_create_after` to the future

## Complete Example: Daily DAG at Midnight

### DAG Definition:
```python
from airflow import DAG
from datetime import datetime

dag = DAG(
    dag_id="example_daily",
    schedule="0 0 * * *",  # Daily at midnight UTC
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
```

### Timeline Diagram

```mermaid
gantt
    title Daily DAG Scheduling Timeline
    dateFormat YYYY-MM-DD HH:mm
    axisFormat %Y-%m-%d %H:%M
    
    section Dag Processor
    Parse DAG & Calculate next_dagrun_create_after :milestone, 2024-01-01 12:00, 0m
    
    section DagModel
    next_dagrun_create_after = 2024-01-02 00:00 :2024-01-01 12:00, 12h
    
    section Scheduler
    Create Run 1 :milestone, 2024-01-02 00:00, 0m
    Update next_dagrun_create_after = 2024-01-03 00:00 :milestone, 2024-01-02 00:01, 0m
    Create Run 2 :milestone, 2024-01-03 00:00, 0m
    Update next_dagrun_create_after = 2024-01-04 00:00 :milestone, 2024-01-03 00:01, 0m
```

### Timeline:

**Time: 2024-01-01 12:00 UTC** (DAG first parsed)
- Dag Processor runs:
  - No previous runs exist
  - Timetable calculates: next run at 2024-01-02 00:00
  - DagModel updated:
    - `next_dagrun = 2024-01-01 00:00` (logical date)
    - `next_dagrun_create_after = 2024-01-02 00:00` (when to create)

**Time: 2024-01-02 00:00:05 UTC** (Scheduler loop runs)
- Scheduler checks: `next_dagrun_create_after (2024-01-02 00:00) <= NOW (2024-01-02 00:00:05)` ✓
- Scheduler creates DAG run:
  - `run_id = scheduled__2024-01-01T00:00:00+00:00`
  - `logical_date = 2024-01-01 00:00`
  - `data_interval_start = 2024-01-01 00:00`
  - `data_interval_end = 2024-01-02 00:00`
  - `state = QUEUED`
- Scheduler updates DagModel:
  - `next_dagrun = 2024-01-02 00:00`
  - `next_dagrun_create_after = 2024-01-03 00:00` (tomorrow)

**Time: 2024-01-03 00:00:05 UTC** (Next day)
- Scheduler checks: `next_dagrun_create_after (2024-01-03 00:00) <= NOW (2024-01-03 00:00:05)` ✓
- Creates next run...
- Updates: `next_dagrun_create_after = 2024-01-04 00:00`

## Key Configuration Options

### Scheduler Config (`airflow.cfg`):

```ini
[scheduler]
# How many DAGs to process per scheduling loop (default: 10)
max_dagruns_to_create_per_loop = 10

# How often the scheduler runs (seconds, default: 1)
scheduler_heartbeat_sec = 1
```

### DAG Config:

```python
DAG(
    schedule="0 0 * * *",      # When runs should occur
    start_date=datetime(...),  # Earliest possible run
    end_date=datetime(...),    # Latest possible run (optional)
    catchup=False,             # Skip missed runs (default: True)
    max_active_runs=16,        # Max concurrent runs (default: 16)
)
```

## Common Scenarios

### Scenario 1: Scheduler Downtime

```mermaid
flowchart TD
    A[Scheduler Down<br/>2024-01-02 to 2024-01-05] --> B{catchup=True?}
    
    B -->|Yes| C[Scheduler Restarts<br/>2024-01-05]
    B -->|No| D[Scheduler Restarts<br/>2024-01-05]
    
    C --> E[Create ALL missed runs:<br/>2024-01-02, 01-03, 01-04, 01-05]
    D --> F[Timetable skips to latest]
    F --> G[Create ONLY 2024-01-05]
    
    E --> H[Limited by max_active_runs<br/>and processing capacity]
```

**Situation**: Scheduler is down from 2024-01-02 to 2024-01-05.

**With catchup=True**:
- When scheduler restarts, it will create runs for:
  - 2024-01-02 00:00
  - 2024-01-03 00:00
  - 2024-01-04 00:00
  - 2024-01-05 00:00
- Limited by `max_active_runs` and processing capacity

**With catchup=False**:
- When scheduler restarts, timetable skips to latest
- Only creates run for 2024-01-05 00:00
- Missed runs are skipped

### Scenario 2: DAG Paused Then Unpaused

**Situation**: DAG paused on 2024-01-02, unpaused on 2024-01-05.

- While paused:
  - `next_dagrun_create_after` is not updated
  - Scheduler skips the DAG (query filters `is_paused = FALSE`)
- When unpaused:
  - Dag Processor recalculates `next_dagrun_create_after`
  - Behavior depends on `catchup` setting (same as Scenario 1)

### Scenario 3: Multiple Schedulers

```mermaid
sequenceDiagram
    participant S1 as Scheduler 1
    participant S2 as Scheduler 2
    participant S3 as Scheduler 3
    participant DB as Database
    
    par Scheduler 1
        S1->>DB: SELECT ... FOR UPDATE SKIP LOCKED
        DB-->>S1: Lock DAGs 1-10
        S1->>S1: Process DAGs 1-10
    and Scheduler 2
        S2->>DB: SELECT ... FOR UPDATE SKIP LOCKED
        DB-->>S2: Lock DAGs 11-20 (skip 1-10)
        S2->>S2: Process DAGs 11-20
    and Scheduler 3
        S3->>DB: SELECT ... FOR UPDATE SKIP LOCKED
        DB-->>S3: Lock DAGs 21-30 (skip 1-20)
        S3->>S3: Process DAGs 21-30
    end
    
    Note over S1,DB: No duplicate DAG runs created
```

**Situation**: 3 schedulers running simultaneously.

- Each scheduler runs `dags_needing_dagruns()` query
- `SELECT ... FOR UPDATE SKIP LOCKED` ensures:
  - Only one scheduler locks each DAG row
  - Other schedulers skip locked rows
  - No duplicate DAG runs created
- Each scheduler processes up to 10 DAGs (30 total capacity)

## Potential Issues

### Issue 1: Asset-Triggered DAG Ordering

```mermaid
flowchart TD
    A[100 DAGs need runs] --> B{DAG Types}
    B -->|90 Scheduled DAGs| C[next_dagrun_create_after<br/>has timestamp]
    B -->|10 Asset-Triggered| D[next_dagrun_create_after<br/>= NULL]
    
    C --> E[ORDER BY next_dagrun_create_after]
    D --> E
    
    E --> F{NULL ordering?}
    F -->|PostgreSQL| G[NULLs FIRST<br/>Asset DAGs prioritized]
    F -->|MySQL| H[NULLs LAST<br/>Asset DAGs starved]
    
    E --> I[LIMIT 10]
    
    I --> J{Scheduled DAGs >= 10?}
    J -->|Yes + MySQL| K[Asset DAGs never processed!]
    J -->|No| L[Some Asset DAGs processed]
```

**Problem**: Asset-triggered DAGs may have `next_dagrun_create_after = NULL` if they don't have a timetable schedule. The `ORDER BY next_dagrun_create_after` can behave unpredictably:
- Some databases (PostgreSQL) sort NULL first
- Some databases (MySQL) sort NULL last
- Asset DAGs without schedules might be starved or prioritized incorrectly

**Code Location**: `dag.py:666`
```python
.order_by(cls.next_dagrun_create_after)  # NULLs have undefined order
.limit(cls.NUM_DAGS_PER_DAGRUN_QUERY)
```

**Impact**: If 10+ scheduled DAGs are always due, asset-triggered DAGs might never be processed.

### Issue 2: Large Number of Overdue DAGs

**Problem**: If 100+ DAGs are all overdue (e.g., after scheduler downtime), only 10 are processed per loop.

**Impact**:
- Takes 10+ scheduling loops to catch up
- With 1-second scheduler heartbeat, ~10 seconds to process all
- Can be increased with `max_dagruns_to_create_per_loop` config

### Issue 3: Dag Processor Lag

**Problem**: If dag processor is slow to parse DAGs, `next_dagrun_create_after` may become stale.

**Impact**:
- Scheduler creates runs based on old schedule
- After dag processor updates, next run uses new schedule
- Can cause one run to be missed or duplicated during transition

## Database Schema

### Entity Relationship

```mermaid
erDiagram
    DagModel ||--o{ DagRun : creates
    DagModel {
        string dag_id PK
        boolean is_paused
        boolean is_stale
        boolean has_import_errors
        timestamp next_dagrun
        timestamp next_dagrun_create_after
        json next_dagrun_data_interval
        int max_active_runs
    }
    DagRun {
        int id PK
        string dag_id FK
        string run_id
        timestamp logical_date
        timestamp data_interval_start
        timestamp data_interval_end
        string run_type
        string state
    }
```

### DagModel Table (Relevant Columns):

```sql
CREATE TABLE dag_model (
    dag_id VARCHAR(250) PRIMARY KEY,
    is_paused BOOLEAN,
    is_stale BOOLEAN,
    has_import_errors BOOLEAN,
    next_dagrun TIMESTAMP,              -- Logical date of next run
    next_dagrun_create_after TIMESTAMP, -- When to create next run (THE KEY FIELD)
    next_dagrun_data_interval JSON,     -- Data interval for next run
    max_active_runs INTEGER,
    -- ... other fields
);

CREATE INDEX idx_next_dagrun_create_after 
ON dag_model(next_dagrun_create_after);
```

### DagRun Table (Relevant Columns):

```sql
CREATE TABLE dag_run (
    id INTEGER PRIMARY KEY,
    dag_id VARCHAR(250),
    run_id VARCHAR(250),
    logical_date TIMESTAMP,           -- Start of data interval
    data_interval_start TIMESTAMP,    -- Explicit start
    data_interval_end TIMESTAMP,      -- Explicit end
    run_type VARCHAR(50),             -- SCHEDULED, MANUAL, BACKFILL_JOB, etc.
    state VARCHAR(50),                -- QUEUED, RUNNING, SUCCESS, FAILED
    -- ... other fields
);
```

## Summary

```mermaid
graph TB
    subgraph "The Critical Decision"
        A[next_dagrun_create_after <= NOW?]
        style A fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px,color:#fff
    end
    
    subgraph "Phase 1: Calculation by Dag Processor"
        B[Parse DAG]
        C[Query Last Run]
        D[Timetable Logic]
        E[Store in DagModel]
        B --> C --> D --> E
    end
    
    subgraph "Phase 2: Execution by Scheduler"
        F[Query WHERE condition]
        G[Create DagRun]
        H[Update for Next Run]
        F --> G --> H
    end
    
    E --> A
    A --> F
    
    style B fill:#4ecdc4
    style C fill:#4ecdc4
    style D fill:#4ecdc4
    style E fill:#4ecdc4
    style F fill:#95e1d3
    style G fill:#95e1d3
    style H fill:#95e1d3
```

**The critical decision point**: `next_dagrun_create_after <= NOW()`

1. **Dag Processor** calculates and stores `next_dagrun_create_after` in `dag_model` table
2. **Scheduler** queries DAGs where `next_dagrun_create_after <= NOW()`
3. **Scheduler** creates the run and updates `next_dagrun_create_after` for the next run
4. **Loop continues** every ~1 second

This decouples DAG parsing (slow) from DAG run creation (fast), allowing the scheduler to be responsive while supporting complex scheduling logic.

## Key Takeaways

1. **Dag Processor is responsible for calculating WHEN** a DAG run should be created
2. **Scheduler is responsible for CREATING** the DAG run at the right time
3. **The field `next_dagrun_create_after`** is the critical link between them
4. **Timetables** encapsulate all scheduling logic (cron, timedelta, custom)
5. **Database query with time comparison** (`<= NOW()`) determines which DAGs get runs
6. **Multi-scheduler support** is achieved via row-level locking with SKIP LOCKED
