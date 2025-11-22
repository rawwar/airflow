# Task Execution Lifecycle on CeleryExecutor - Complete Guide

Comprehensive documentation for debugging and understanding task execution on CeleryExecutor, from scheduler queuing to task completion.

## Table of Contents

1. [Overview](#overview)
2. [Architecture Components](#architecture-components)
3. [Complete Execution Flow](#complete-execution-flow)
4. [Task Command Execution](#task-command-execution)
5. [XCom Operations](#xcom-operations)
6. [Variable Access](#variable-access)
7. [Database Connections](#database-connections)
8. [Process Management](#process-management)
9. [Logging and Monitoring](#logging-and-monitoring)
10. [Debugging Guide](#debugging-guide)

---

## Overview

### What is CeleryExecutor?

CeleryExecutor is a distributed task execution backend that uses Celery (distributed task queue) to run Airflow tasks across multiple worker machines.

**Key Characteristics**:
- Tasks run on separate worker processes/machines
- Message broker (Redis/RabbitMQ) handles task distribution
- Result backend stores task outcomes
- Each task is a subprocess executing `airflow tasks run` command

### Execution Phases

```mermaid
flowchart TB
    subgraph Phase 1: Scheduler
        S1[Scheduler: queue_task_instance]
        S2[Build Celery message]
        S3[Send to broker]
    end
    
    subgraph Phase 2: Message Broker
        B1[Redis/RabbitMQ Queue]
        B2[Task persisted in broker]
    end
    
    subgraph Phase 3: Celery Worker
        W1[Worker polls broker]
        W2[Deserialize task]
        W3[Spawn subprocess]
    end
    
    subgraph Phase 4: Task Subprocess
        T1[airflow tasks run command]
        T2[Load DAG]
        T3[Create TaskInstance]
        T4[Execute operator]
    end
    
    subgraph Phase 5: Data Access
        D1[Fetch Variables]
        D2[Fetch XComs]
        D3[Read Connections]
        D4[Query metadata DB]
    end
    
    subgraph Phase 6: Completion
        C1[Write XCom outputs]
        C2[Update task state]
        C3[Return to worker]
        C4[Report to scheduler]
    end
    
    S1 --> S2 --> S3
    S3 --> B1 --> B2
    B2 --> W1 --> W2 --> W3
    W3 --> T1 --> T2 --> T3 --> T4
    T4 --> D1
    T4 --> D2
    T4 --> D3
    T4 --> D4
    D1 --> C1
    D2 --> C1
    D3 --> C1
    D4 --> C1
    C1 --> C2 --> C3 --> C4
    
    style S1 fill:#4ecdc4
    style B1 fill:#f08c00,color:#fff
    style W1 fill:#95e1d3
    style T1 fill:#ffec99
    style D1 fill:#ffd93d
    style C2 fill:#b2f2bb
```

---

## Architecture Components

### Component Diagram

```mermaid
flowchart TB
    subgraph Scheduler Machine
        Scheduler[Airflow Scheduler]
        CeleryExec[CeleryExecutor]
    end
    
    subgraph Broker Infrastructure
        Broker[(Message Broker<br/>Redis/RabbitMQ)]
        ResultBackend[(Result Backend<br/>Redis/Database)]
    end
    
    subgraph Worker Machine 1
        CW1[Celery Worker Process]
        subgraph Task Processes 1
            TP1[Task Subprocess 1]
            TP2[Task Subprocess 2]
        end
    end
    
    subgraph Worker Machine 2
        CW2[Celery Worker Process]
        subgraph Task Processes 2
            TP3[Task Subprocess 3]
            TP4[Task Subprocess 4]
        end
    end
    
    subgraph Shared Infrastructure
        MetaDB[(Metadata DB<br/>PostgreSQL/MySQL)]
        LogStorage[(Log Storage<br/>S3/GCS/Local)]
    end
    
    Scheduler -->|1. Queue task| CeleryExec
    CeleryExec -->|2. app.send_task()| Broker
    
    Broker -->|3. Dispatch| CW1
    Broker -->|3. Dispatch| CW2
    
    CW1 -->|4. Fork/spawn| TP1
    CW1 -->|4. Fork/spawn| TP2
    CW2 -->|4. Fork/spawn| TP3
    CW2 -->|4. Fork/spawn| TP4
    
    TP1 -.->|5. Read/Write| MetaDB
    TP2 -.->|5. Read/Write| MetaDB
    TP3 -.->|5. Read/Write| MetaDB
    TP4 -.->|5. Read/Write| MetaDB
    
    TP1 -.->|6. Write logs| LogStorage
    TP2 -.->|6. Write logs| LogStorage
    TP3 -.->|6. Write logs| LogStorage
    TP4 -.->|6. Write logs| LogStorage
    
    TP1 -->|7. Return result| CW1
    TP2 -->|7. Return result| CW1
    TP3 -->|7. Return result| CW2
    TP4 -->|7. Return result| CW2
    
    CW1 -->|8. Store result| ResultBackend
    CW2 -->|8. Store result| ResultBackend
    
    ResultBackend -.->|9. Poll results| CeleryExec
    CeleryExec -->|10. Sync states| Scheduler
    
    style Scheduler fill:#4ecdc4
    style CeleryExec fill:#ffd93d
    style Broker fill:#f08c00,color:#fff
    style ResultBackend fill:#f08c00,color:#fff
    style MetaDB fill:#ffd93d
    style LogStorage fill:#d0ebff
    style CW1 fill:#95e1d3
    style CW2 fill:#95e1d3
    style TP1 fill:#b2f2bb
    style TP2 fill:#b2f2bb
    style TP3 fill:#b2f2bb
    style TP4 fill:#b2f2bb
```

### Component Roles

**Scheduler**:
- Queries database for tasks ready to run
- Sends tasks to CeleryExecutor
- Polls result backend for completed tasks
- Updates metadata database with final states

**CeleryExecutor** (scheduler process):
- Wraps tasks as Celery tasks
- Sends to message broker via `app.send_task()`
- Monitors task states via result backend
- Returns completed tasks to scheduler

**Message Broker** (Redis/RabbitMQ):
- Stores task messages in queues
- Ensures reliable delivery
- Supports multiple queues (priority, default, etc.)
- Persists messages until acknowledged

**Celery Worker**:
- Long-running process on worker machine
- Polls broker for new tasks
- Spawns subprocess for each task
- Monitors subprocess execution
- Writes results to result backend

**Task Subprocess**:
- Runs `airflow tasks run <dag_id> <task_id> <logical_date>` command
- Isolated Python process
- Loads DAG definition
- Executes operator logic
- Accesses metadata DB, XCom, variables, connections
- Writes logs to log storage
- Updates task state in metadata DB

---

## Complete Execution Flow

### Detailed Sequence Diagram

```mermaid
sequenceDiagram
    participant Sch as Scheduler
    participant CE as CeleryExecutor
    participant Broker as Message Broker
    participant CW as Celery Worker
    participant Sub as Task Subprocess
    participant MetaDB as Metadata DB
    participant RB as Result Backend
    participant Logs as Log Storage
    
    Note over Sch,Logs: Phase 1: Task Queuing
    
    Sch->>CE: queue_task_instance(task_key, command, ...)
    CE->>CE: Build task payload:<br/>{command, queue, ...}
    CE->>Broker: app.send_task('execute_command', args=[command])
    Broker->>Broker: Store in queue (e.g., 'default')
    CE->>MetaDB: Update TaskInstance state=QUEUED
    
    Note over Sch,Logs: Phase 2: Task Dispatch
    
    CW->>Broker: BRPOP <queue> [blocking poll]
    Broker-->>CW: Return task message
    CW->>CW: Deserialize Celery task
    CW->>Sub: fork/spawn process
    
    Note over Sub: Command: airflow tasks run<br/>--dag_id example_dag<br/>--task_id my_task<br/>--logical_date 2024-01-01T00:00:00<br/>--local<br/>--subdir /path/to/dag.py
    
    Note over Sch,Logs: Phase 3: Task Initialization
    
    Sub->>Sub: Parse command-line args
    Sub->>Sub: Load Airflow config
    Sub->>Sub: Initialize logging
    Sub->>MetaDB: Query DagModel for DAG
    MetaDB-->>Sub: Return DAG metadata
    Sub->>Sub: Load DAG from file (import Python module)
    Sub->>Sub: Get task from DAG: dag.get_task(task_id)
    Sub->>MetaDB: Query TaskInstance record
    MetaDB-->>Sub: Return TI (state, try_number, etc.)
    Sub->>MetaDB: Update TaskInstance state=RUNNING
    Sub->>MetaDB: Set start_date=NOW(), hostname, pid
    Sub->>Logs: Open log file handler
    
    Note over Sch,Logs: Phase 4: Variable & Connection Loading
    
    Sub->>MetaDB: SELECT * FROM variable WHERE key IN (...)
    MetaDB-->>Sub: Return Variables
    Sub->>Sub: Cache variables in memory
    Sub->>MetaDB: SELECT * FROM connection WHERE conn_id IN (...)
    MetaDB-->>Sub: Return Connections (encrypted)
    Sub->>Sub: Decrypt connection passwords
    Sub->>Sub: Cache connections in memory
    
    Note over Sch,Logs: Phase 5: XCom Fetch
    
    Sub->>MetaDB: SELECT * FROM xcom<br/>WHERE dag_id=... AND task_ids IN (...)<br/>AND run_id=...
    MetaDB-->>Sub: Return XCom values
    Sub->>Sub: Deserialize XCom (JSON/pickle)
    Sub->>Sub: Make available via task_instance.xcom_pull()
    
    Note over Sch,Logs: Phase 6: Operator Execution
    
    Sub->>Sub: Call operator.execute(context)
    Sub->>Sub: context = {<br/>  task_instance: TI,<br/>  dag: DAG,<br/>  execution_date: datetime,<br/>  task: Task,<br/>  ti: TI,<br/>  var: {json: ..., value: ...},<br/>  conn: Connection,<br/>  ...<br/>}
    
    loop Operator Logic
        Sub->>Sub: Execute custom Python code
        Sub->>Logs: Log output via logger
        Sub->>MetaDB: Optional DB queries
        Sub->>Sub: Access context["var"]
        Sub->>Sub: Access context["ti"].xcom_pull()
    end
    
    alt Task Succeeds
        Sub->>Sub: Return value from execute()
        Sub->>Sub: Store return value as XCom
    else Task Fails
        Sub->>Sub: Raise exception
        Sub->>Sub: Log traceback
    end
    
    Note over Sch,Logs: Phase 7: XCom Push
    
    Sub->>MetaDB: INSERT INTO xcom<br/>(dag_id, task_id, run_id,<br/>key, value, timestamp)
    Sub->>MetaDB: Serialize value (JSON or pickle)
    
    Note over Sch,Logs: Phase 8: State Update
    
    alt Success
        Sub->>MetaDB: UPDATE task_instance<br/>SET state='SUCCESS',<br/>end_date=NOW(),<br/>duration=...
        Sub->>Sub: Exit code 0
    else Failure
        Sub->>MetaDB: UPDATE task_instance<br/>SET state='FAILED',<br/>end_date=NOW()
        Sub->>Sub: Exit code 1
    else Retry
        Sub->>MetaDB: UPDATE task_instance<br/>SET state='UP_FOR_RETRY',<br/>max_tries=...
        Sub->>Sub: Exit code 1
    end
    
    Sub->>Logs: Close log handlers
    Sub-->>CW: Exit with code
    
    Note over Sch,Logs: Phase 9: Result Propagation
    
    CW->>CW: Capture exit code
    CW->>RB: Store task result (success/failure)
    CW->>RB: Set TTL on result
    
    Note over Sch,Logs: Phase 10: Scheduler Sync
    
    Sch->>CE: heartbeat() [periodic]
    CE->>RB: Check result for queued tasks
    RB-->>CE: Return task states
    CE->>MetaDB: Verify TaskInstance states
    CE->>Sch: sync() - return completed tasks
    Sch->>Sch: Update internal state
```

### Execution Timeline

```mermaid
gantt
    title Task Execution Timeline on CeleryExecutor
    dateFormat ss
    axisFormat %Ss
    
    section Scheduler
    Queue task              :s1, 00, 1s
    Periodic heartbeat      :s2, 35, 2s
    Sync states             :s3, 37, 1s
    
    section Broker
    Store message           :b1, 01, 1s
    
    section Celery Worker
    Poll broker             :w1, 02, 1s
    Deserialize             :w2, 03, 1s
    Spawn subprocess        :w3, 04, 2s
    Wait for completion     :w4, 06, 29s
    Write result            :w5, 35, 1s
    
    section Task Subprocess
    Parse args              :t1, 06, 1s
    Load config             :t2, 07, 1s
    Load DAG                :t3, 08, 3s
    Query TI record         :t4, 11, 1s
    Update state=RUNNING    :t5, 12, 1s
    Load variables          :t6, 13, 1s
    Load connections        :t7, 14, 1s
    Fetch XComs             :t8, 15, 1s
    Execute operator        :active, t9, 16, 15s
    Push XComs              :t10, 31, 1s
    Update state=SUCCESS    :done, t11, 32, 1s
    Close logs              :t12, 33, 1s
    Exit                    :t13, 34, 1s
```

**Key Timing Points**:
- **0-2s**: Scheduler to broker (network latency)
- **2-6s**: Broker to worker, subprocess spawn
- **6-16s**: Task initialization (DAG load, DB queries)
- **16-31s**: Operator execution (business logic)
- **31-35s**: Cleanup and state update
- **35-38s**: Result propagation and scheduler sync

**Total**: ~38 seconds for a 15-second task

---

## Task Command Execution

### Command Structure

Every task runs as a subprocess with this command:

```bash
airflow tasks run \
  --dag_id <dag_id> \
  --task_id <task_id> \
  --run_id <run_id> \
  --map_index <map_index> \
  --local \
  --subdir <dag_file_path> \
  --pickle <pickle_id>
```

**File**: `airflow-core/src/airflow/cli/commands/task_command.py`

### Command Execution Flow

```mermaid
flowchart TD
    Start([airflow tasks run]) --> Parse[Parse CLI arguments]
    Parse --> LoadConf[Load Airflow configuration]
    LoadConf --> InitLog[Initialize logging]
    InitLog --> CheckLocal{--local flag?}
    
    CheckLocal -->|Yes| LoadDAG[Load DAG from file]
    CheckLocal -->|No| LoadPickle[Load DAG from pickle]
    
    LoadDAG --> GetTask[Get task from DAG]
    LoadPickle --> GetTask
    
    GetTask --> CreateTI[Create TaskInstance object]
    CreateTI --> QueryDB[Query TI record from DB]
    QueryDB --> SetState[Update state=RUNNING]
    SetState --> SetMeta[Set hostname, pid, start_date]
    SetMeta --> Run[Call TaskInstance._run_raw_task()]
    
    Run --> PreExec[Pre-execute hooks]
    PreExec --> Execute[operator.execute(context)]
    Execute --> PostExec[Post-execute hooks]
    PostExec --> HandleResult{Task result?}
    
    HandleResult -->|Success| Success[Set state=SUCCESS]
    HandleResult -->|Exception| CheckRetry{Retries left?}
    
    CheckRetry -->|Yes| Retry[Set state=UP_FOR_RETRY]
    CheckRetry -->|No| Failed[Set state=FAILED]
    
    Success --> CleanUp[Close logs, cleanup]
    Retry --> CleanUp
    Failed --> CleanUp
    
    CleanUp --> Exit([Exit with code])
    
    style Start fill:#4ecdc4
    style LoadDAG fill:#ffd93d
    style SetState fill:#ffec99
    style Execute fill:#95e1d3
    style Success fill:#b2f2bb
    style Failed fill:#ffe3e3
    style Retry fill:#ffec99
```

### Key Files

**Task execution entry point**:
- `airflow-core/src/airflow/cli/commands/task_command.py` - CLI command handler
- Method: `task_run()` at line ~200

**TaskInstance execution**:
- `airflow-core/src/airflow/models/taskinstance.py`
- Method: `_run_raw_task()` at line ~2000+
- Method: `_execute_task()` at line ~2200+

**Operator execution**:
- Each operator: `execute(context)` method
- Context building: `get_template_context()` at line ~1800


---

## XCom Operations

### XCom Architecture

```mermaid
flowchart TB
    subgraph Task 1 Execution
        T1[Task 1: Executes]
        T1_Return[Returns value]
        T1_Push[xcom_push()]
    end
    
    subgraph XCom Storage
        DB[(xcom table in Metadata DB)]
        Row[Row: dag_id, task_id, run_id, key, value, timestamp]
    end
    
    subgraph Task 2 Execution
        T2[Task 2: Executes]
        T2_Pull[xcom_pull(task_ids=['task1'])]
        T2_Use[Use pulled value]
    end
    
    T1 --> T1_Return
    T1_Return --> T1_Push
    T1_Push -->|INSERT| DB
    
    DB --> Row
    
    T2 --> T2_Pull
    T2_Pull -->|SELECT| DB
    DB -->|Deserialize| T2_Use
    
    style T1 fill:#95e1d3
    style DB fill:#ffd93d
    style T2 fill:#b2f2bb
```

### XCom Push Flow

**File**: `airflow-core/src/airflow/models/xcom.py`

```python
# Automatic XCom push (return value from execute())
def _execute_task(self, context):
    result = self.task.execute(context)
    
    # Push return value to XCom
    if result is not None:
        self.xcom_push(
            key=XCOM_RETURN_KEY,  # 'return_value'
            value=result
        )
```

**Sequence**:

```mermaid
sequenceDiagram
    participant Op as Operator.execute()
    participant TI as TaskInstance
    participant XCom as XCom.set()
    participant DB as Metadata DB
    
    Op->>Op: Execute business logic
    Op-->>TI: Return result value
    
    TI->>TI: Check if value is not None
    TI->>XCom: xcom_push(key='return_value', value=result)
    
    XCom->>XCom: Serialize value
    
    alt Value is JSON serializable
        XCom->>XCom: json.dumps(value)
        XCom->>DB: INSERT with value_type='json'
    else Value is Python object
        XCom->>XCom: pickle.dumps(value)
        XCom->>DB: INSERT with value_type='pickle'
    end
    
    XCom->>DB: INSERT INTO xcom (<br/>dag_id, task_id, run_id,<br/>key, value, timestamp)<br/>VALUES (...)
    
    DB-->>XCom: Confirm insert
    XCom-->>TI: XCom stored
```

### XCom Pull Flow

**Operator code**:
```python
def execute(self, context):
    # Pull XCom from upstream task
    value = context['ti'].xcom_pull(
        task_ids='upstream_task',
        key='return_value'  # Default
    )
    
    # Or pull from multiple tasks
    values = context['ti'].xcom_pull(
        task_ids=['task1', 'task2', 'task3']
    )
```

**Sequence**:

```mermaid
sequenceDiagram
    participant Op as Operator.execute()
    participant TI as TaskInstance
    participant XCom as XCom.get_many()
    participant DB as Metadata DB
    
    Op->>TI: xcom_pull(task_ids=['task1'])
    TI->>XCom: get_many(task_ids, key, run_id)
    
    XCom->>DB: SELECT * FROM xcom<br/>WHERE dag_id=...<br/>AND task_id IN ('task1')<br/>AND run_id=...<br/>AND key='return_value'
    
    DB-->>XCom: Return rows
    
    loop For each row
        XCom->>XCom: Check value_type
        
        alt value_type = 'json'
            XCom->>XCom: json.loads(value)
        else value_type = 'pickle'
            XCom->>XCom: pickle.loads(value)
        end
    end
    
    XCom-->>TI: Return deserialized values
    TI-->>Op: Return values (single or list)
    Op->>Op: Use values in business logic
```

### XCom Table Schema

```sql
CREATE TABLE xcom (
    dag_run_id INTEGER,
    task_id VARCHAR(250),
    map_index INTEGER DEFAULT -1,
    key VARCHAR(512),
    dag_id VARCHAR(250),
    run_id VARCHAR(250),
    value BYTEA,  -- or BLOB/TEXT depending on backend
    timestamp TIMESTAMP,
    
    PRIMARY KEY (dag_run_id, task_id, map_index, key),
    FOREIGN KEY (dag_run_id) REFERENCES dag_run(id)
);
```

### XCom Size Limits

**Important**: XComs are stored in the metadata database

| Backend | Max Size | Notes |
|---------|----------|-------|
| **PostgreSQL** | 1 GB | BYTEA column limit |
| **MySQL** | 4 GB | LONGBLOB limit |
| **SQLite** | 2 GB | BLOB limit |

**Best Practices**:
- Keep XCom values small (<1 MB recommended)
- For large data, store in external storage (S3, GCS) and pass references via XCom
- Use JSON serialization when possible (faster than pickle)

### XCom Cleanup

**Automatic cleanup** (configured in airflow.cfg):
```ini
[core]
max_xcom_days = 30  # Delete XComs older than 30 days
```

**Manual cleanup**:
```bash
airflow db clean --clean-before-timestamp '2024-01-01' --tables xcom
```

---

## Variable Access

### Variable Architecture

```mermaid
flowchart TB
    subgraph Task Subprocess
        Code[Operator code]
        Var[Variable.get('my_var')]
        Cache[In-memory cache]
    end
    
    subgraph Metadata DB
        VarTable[(variable table)]
        Row[Row: key, val, description, is_encrypted]
    end
    
    Code --> Var
    Var --> Check{In cache?}
    
    Check -->|Yes| ReturnCache[Return from cache]
    Check -->|No| Query[SELECT FROM variable<br/>WHERE key='my_var']
    
    Query --> VarTable
    VarTable --> Row
    Row --> Decrypt{is_encrypted?}
    
    Decrypt -->|Yes| DecryptVal[Decrypt using Fernet key]
    Decrypt -->|No| ReturnPlain[Return plain value]
    
    DecryptVal --> StoreCache[Store in cache]
    ReturnPlain --> StoreCache
    
    StoreCache --> Cache
    Cache --> ReturnCache
    ReturnCache --> Code
    
    style Code fill:#95e1d3
    style VarTable fill:#ffd93d
    style Cache fill:#d0ebff
```

### Variable.get() Flow

**File**: `airflow-core/src/airflow/models/variable.py`

**Code example**:
```python
from airflow.models import Variable

def execute(self, context):
    # Get single variable
    api_key = Variable.get('api_key')
    
    # Get with default
    timeout = Variable.get('timeout', default_var=30)
    
    # Get as JSON
    config = Variable.get('config', deserialize_json=True)
    # Returns: {'host': 'example.com', 'port': 8080}
```

**Sequence**:

```mermaid
sequenceDiagram
    participant Op as Operator
    participant Var as Variable.get()
    participant Cache as VariableAccessor
    participant DB as Metadata DB
    participant Fernet as Fernet Encryption
    
    Op->>Var: Variable.get('api_key')
    Var->>Cache: Check cache
    
    alt Cache hit
        Cache-->>Var: Return cached value
    else Cache miss
        Var->>DB: SELECT val, is_encrypted<br/>FROM variable<br/>WHERE key='api_key'
        
        alt Variable exists
            DB-->>Var: Return row
            
            Var->>Var: Check is_encrypted flag
            
            alt is_encrypted = True
                Var->>Fernet: decrypt(val)
                Fernet-->>Var: Decrypted value
            else is_encrypted = False
                Var->>Var: Use val as-is
            end
            
            Var->>Cache: Store in cache
            Cache-->>Var: Value stored
        else Variable not found
            alt default_var provided
                Var-->>Op: Return default_var
            else No default
                Var-->>Op: Raise KeyError
            end
        end
    end
    
    Var-->>Op: Return decrypted value
```

### Variable Encryption

**Fernet key** (from airflow.cfg):
```ini
[core]
fernet_key = <base64-encoded-32-byte-key>
```

**Encrypted variables**:
- Variables with keys matching patterns in `sensitive_var_conn_names`
- Variables marked as encrypted in UI/API
- Encrypted in database, decrypted on access

**Sensitive patterns** (default):
```python
# From airflow.cfg [core] sensitive_var_conn_names
default_patterns = [
    'password', 'secret', 'passwd', 'authorization',
    'api_key', 'apikey', 'access_token'
]
```

### Variable Caching

**Cache lifetime**: Per-task execution (not shared across tasks)

**Cache invalidation**: Cache cleared after task completes

**Why cache?**
- Reduces DB queries
- Improves performance for variables accessed multiple times
- Only within same task execution

### Variable via Context

**Accessing via context** (preferred in templates):
```python
def execute(self, context):
    # Access Variable object
    api_key = context['var']['value'].get('api_key')
    
    # Access as JSON
    config = context['var']['json'].get('config')
```

**Context structure**:
```python
context = {
    'var': {
        'value': Variable,  # Variable class for .get()
        'json': Variable,   # Variable class for .get(deserialize_json=True)
    },
    ...
}
```

---

## Database Connections

### Database Session Management

**File**: `airflow-core/src/airflow/settings.py`

**Session creation**:

```mermaid
flowchart TD
    Start[Task subprocess starts] --> InitSettings[Import airflow.settings]
    InitSettings --> CreateEngine[Create SQLAlchemy engine]
    CreateEngine --> Config{Read airflow.cfg<br/>[database] section}
    
    Config --> ConnStr[sql_alchemy_conn =<br/>postgresql://user:pass@host:5432/airflow]
    ConnStr --> PoolConfig[Configure connection pool]
    
    PoolConfig --> PoolSize[pool_size = 5<br/>max_overflow = 10<br/>pool_timeout = 30<br/>pool_recycle = 1800]
    
    PoolSize --> CreateSession[Create scoped_session]
    CreateSession --> SessionFactory[SessionFactory with engine]
    SessionFactory --> Ready[Session ready for use]
    
    Ready --> OpExec[Operator execution]
    OpExec --> UseSession[Use session for queries]
    UseSession --> Commit{Transaction?}
    
    Commit -->|Commit| CommitTx[session.commit()]
    Commit -->|Rollback| RollbackTx[session.rollback()]
    
    CommitTx --> Close[session.close()]
    RollbackTx --> Close
    Close --> Return[Return connection to pool]
    Return --> End([Task completes])
    
    style Start fill:#4ecdc4
    style CreateEngine fill:#ffd93d
    style UseSession fill:#95e1d3
    style CommitTx fill:#b2f2bb
    style RollbackTx fill:#ffe3e3
```

### Connection Pool Configuration

**File**: `airflow.cfg` section `[database]`

```ini
[database]
sql_alchemy_conn = postgresql+psycopg2://airflow:password@postgres:5432/airflow

# Connection pool settings
sql_alchemy_pool_size = 5          # Base number of connections
sql_alchemy_max_overflow = 10      # Additional connections allowed
sql_alchemy_pool_timeout = 30      # Wait time for connection (seconds)
sql_alchemy_pool_recycle = 1800    # Recycle connections after 30 min
sql_alchemy_pool_pre_ping = True   # Test connections before use
```

**Pool behavior**:

```mermaid
stateDiagram-v2
    [*] --> Idle: Connection created
    Idle --> Active: Task requests connection
    Active --> Idle: Task returns connection
    Idle --> Recycled: pool_recycle timeout
    Recycled --> [*]: Connection closed
    Active --> Failed: Query fails
    Failed --> [*]: Connection discarded
    
    note right of Idle
        pool_size = 5 connections
        always available
    end note
    
    note right of Active
        max_overflow = 10
        additional connections
        if pool exhausted
    end note
    
    note right of Recycled
        pool_recycle = 1800s
        prevents stale connections
    end note
```

### DB Query Examples in Tasks

**XCom query**:
```python
from airflow.models import XCom
from airflow.utils.session import create_session

def execute(self, context):
    with create_session() as session:
        xcoms = session.query(XCom).filter(
            XCom.dag_id == 'my_dag',
            XCom.task_id == 'upstream_task',
            XCom.run_id == context['run_id']
        ).all()
```

**TaskInstance query**:
```python
from airflow.models import TaskInstance
from airflow.utils.session import create_session

def execute(self, context):
    with create_session() as session:
        ti = session.query(TaskInstance).filter(
            TaskInstance.dag_id == 'my_dag',
            TaskInstance.task_id == 'my_task',
            TaskInstance.run_id == context['run_id']
        ).first()
        
        # Access TI fields
        print(f"State: {ti.state}")
        print(f"Try number: {ti.try_number}")
```

### Connection Strings

**PostgreSQL**:
```
postgresql+psycopg2://user:password@host:5432/dbname
```

**MySQL**:
```
mysql+pymysql://user:password@host:3306/dbname
```

**SQLite** (not recommended for production):
```
sqlite:////path/to/airflow.db
```

### Database Transactions

**File**: `airflow-core/src/airflow/models/taskinstance.py`

**State update with transaction**:

```python
def _run_raw_task(self, ...):
    with create_session() as session:
        # Start transaction
        self.state = State.RUNNING
        self.start_date = timezone.utcnow()
        self.hostname = get_hostname()
        self.pid = os.getpid()
        
        session.merge(self)
        session.commit()  # Commit transaction
        
    try:
        # Execute operator
        result = self.task.execute(context)
        
        with create_session() as session:
            self.state = State.SUCCESS
            self.end_date = timezone.utcnow()
            session.merge(self)
            session.commit()
    except Exception as e:
        with create_session() as session:
            self.state = State.FAILED
            session.merge(self)
            session.commit()
        raise
```

**Transaction isolation**:
- Default: READ COMMITTED (PostgreSQL)
- Each `create_session()` creates a new transaction
- Changes visible only after commit


---

## Process Management

### Celery Worker Process Architecture

```mermaid
flowchart TB
    subgraph Worker Machine
        Main[Celery Worker<br/>Main Process<br/>PID: 1000]
        
        subgraph Task Pool
            direction TB
            Pool[Process Pool<br/>concurrency=16]
            P1[Task Process 1<br/>PID: 1001]
            P2[Task Process 2<br/>PID: 1002]
            P3[Task Process 3<br/>PID: 1003]
            PN[Task Process N<br/>PID: 1016]
        end
        
        Monitor[Process Monitor<br/>Thread]
        
        Main --> Pool
        Pool --> P1
        Pool --> P2
        Pool --> P3
        Pool --> PN
        Main --> Monitor
        Monitor -.->|Watch| P1
        Monitor -.->|Watch| P2
        Monitor -.->|Watch| P3
        Monitor -.->|Watch| PN
    end
    
    Broker[(Message Broker)] -.->|Poll tasks| Main
    P1 -.->|Update state| DB[(Metadata DB)]
    P2 -.->|Update state| DB
    P3 -.->|Update state| DB
    PN -.->|Update state| DB
    
    style Main fill:#4ecdc4
    style Pool fill:#ffd93d
    style P1 fill:#95e1d3
    style P2 fill:#95e1d3
    style P3 fill:#95e1d3
    style PN fill:#95e1d3
    style Monitor fill:#ffec99
```

### Worker Startup

**Command**:
```bash
airflow celery worker \
  --concurrency 16 \
  --queue default,high_priority \
  --hostname worker1@%h \
  --autoscale 16,4  # max 16, min 4 processes
```

**Startup sequence**:

```mermaid
sequenceDiagram
    participant CLI as airflow celery worker
    participant Config as Load Configuration
    participant Celery as Celery App
    participant Pool as Process Pool
    participant Broker as Message Broker
    
    CLI->>Config: Read airflow.cfg [celery] section
    Config-->>CLI: broker_url, result_backend, etc.
    
    CLI->>Celery: Initialize Celery app
    Celery->>Celery: Register tasks<br/>('execute_command')
    
    CLI->>Pool: Create process pool<br/>(concurrency=16)
    Pool->>Pool: Spawn 16 worker processes
    
    CLI->>Broker: Connect to broker
    Broker-->>CLI: Connection established
    
    CLI->>Broker: Start consuming from queues<br/>['default', 'high_priority']
    
    loop Forever
        Broker->>CLI: Poll for new tasks
        CLI->>Pool: Dispatch task to available process
        Pool->>Pool: Execute task
        Pool-->>CLI: Task complete
        CLI->>Broker: Acknowledge task
    end
```

### Process Spawning

**File**: `providers/celery/src/airflow/providers/celery/executors/celery_executor.py`

**Methods**:
- **fork** (default on Linux): Fast, shares memory
- **spawn** (default on macOS/Windows): Slower, isolated memory
- **forkserver**: Hybrid approach

**Configuration**:
```ini
[celery]
worker_prefork_multiplier = 1  # pool_size = cpu_count * multiplier
```

**Process states**:

```mermaid
stateDiagram-v2
    [*] --> Idle: Process spawned
    Idle --> Executing: Task assigned
    Executing --> Idle: Task complete
    Idle --> Terminating: Worker shutdown
    Executing --> Terminating: SIGTERM received
    Terminating --> [*]: Process exits
    
    Executing --> Killed: Task timeout<br/>or SIGKILL
    Killed --> [*]
    
    note right of Idle
        Process waiting
        for task assignment
    end note
    
    note right of Executing
        Running subprocess:
        airflow tasks run
    end note
```

### Task Subprocess Monitoring

**Celery worker monitors**:
1. **Exit code**: 0 (success), non-zero (failure)
2. **Execution time**: Soft and hard time limits
3. **Memory usage**: OOM detection
4. **Signals**: SIGTERM, SIGKILL handling

**Timeout handling**:

```mermaid
sequenceDiagram
    participant Worker as Celery Worker
    participant Process as Task Process
    participant Timer as Timeout Timer
    
    Worker->>Process: spawn(airflow tasks run)
    Worker->>Timer: Start soft_time_limit timer (600s)
    Worker->>Timer: Start hard_time_limit timer (3600s)
    
    alt Task completes normally
        Process-->>Worker: Exit code 0
        Worker->>Timer: Cancel timers
        Worker->>Worker: Report SUCCESS
    else Soft timeout
        Timer->>Process: Send SIGTERM (SoftTimeLimitExceeded)
        Process->>Process: Catch exception<br/>Cleanup gracefully
        Process-->>Worker: Exit code 1
        Worker->>Worker: Report FAILED (soft timeout)
    else Hard timeout
        Timer->>Process: Send SIGKILL
        Process->>Process: Process killed immediately
        Worker->>Worker: Report FAILED (hard timeout)
    end
```

**Configuration**:
```ini
[celery]
task_soft_time_limit = 600    # 10 minutes (sends SIGTERM)
task_hard_time_limit = 3600   # 1 hour (sends SIGKILL)
```

### Worker Shutdown

**Graceful shutdown** (SIGTERM):

```mermaid
flowchart TD
    Signal[SIGTERM received] --> StopAccept[Stop accepting new tasks]
    StopAccept --> WaitCurrent{Running tasks?}
    
    WaitCurrent -->|Yes| Wait[Wait for completion<br/>up to shutdown_timeout]
    WaitCurrent -->|No| Cleanup
    
    Wait --> Check{All complete?}
    Check -->|Yes| Cleanup[Cleanup resources]
    Check -->|No| Force[Send SIGTERM to all<br/>task processes]
    
    Force --> Cleanup
    Cleanup --> Close[Close broker connection]
    Close --> Exit([Exit worker])
    
    style Signal fill:#ffe3e3
    style Wait fill:#ffec99
    style Cleanup fill:#95e1d3
    style Exit fill:#d0ebff
```

**Configuration**:
```ini
[celery]
worker_shutdown_timeout = 60  # Wait 60s for tasks to complete
```

**Force shutdown** (SIGKILL):
- Immediately terminates worker
- Tasks may be left in inconsistent state
- Use only as last resort

### Process Supervision

**Systemd service** (recommended):

```ini
# /etc/systemd/system/airflow-worker.service
[Unit]
Description=Airflow Celery Worker
After=network.target

[Service]
Type=notify
User=airflow
Group=airflow
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
WorkingDirectory=/opt/airflow
ExecStart=/usr/local/bin/airflow celery worker \
  --concurrency 16 \
  --queue default \
  --hostname worker1@%h
Restart=on-failure
RestartSec=10s
KillMode=mixed
KillSignal=SIGTERM
TimeoutStopSec=60

[Install]
WantedBy=multi-user.target
```

**Supervisor** (alternative):

```ini
# /etc/supervisor/conf.d/airflow-worker.conf
[program:airflow-worker]
command=/usr/local/bin/airflow celery worker --concurrency 16
directory=/opt/airflow
user=airflow
autostart=true
autorestart=true
stopwaitsecs=60
stopsignal=TERM
stdout_logfile=/var/log/airflow/worker.log
stderr_logfile=/var/log/airflow/worker-error.log
```

### Process Inspection

**Check worker status**:
```bash
# List active workers
airflow celery inspect active

# Check registered tasks
airflow celery inspect registered

# View stats
airflow celery inspect stats

# View queues
airflow celery inspect active_queues
```

**Process tree**:
```bash
pstree -p <worker_pid>

# Output:
celery(1000)
├─{celery}(1001)
├─{celery}(1002)
├─python(1010)───airflow(1011)  # Task subprocess
├─python(1020)───airflow(1021)  # Task subprocess
└─python(1030)───airflow(1031)  # Task subprocess
```

---

## Logging and Monitoring

### Log Architecture

```mermaid
flowchart TB
    subgraph Task Subprocess
        Logger[Python Logger]
        Handler1[StreamHandler<br/>stdout/stderr]
        Handler2[FileHandler<br/>/logs/dag_id/task_id/...]
        Handler3[RemoteHandler<br/>S3/GCS/Azure]
    end
    
    subgraph Local Storage
        LogFile[/logs/dag_id/task_id/<br/>logical_date/<br/>attempt.log]
    end
    
    subgraph Remote Storage
        S3[(S3 Bucket)]
        GCS[(GCS Bucket)]
    end
    
    Logger --> Handler1
    Logger --> Handler2
    Logger --> Handler3
    
    Handler1 --> Console[Worker console output]
    Handler2 --> LogFile
    Handler3 --> S3
    Handler3 --> GCS
    
    style Logger fill:#4ecdc4
    style LogFile fill:#ffd93d
    style S3 fill:#95e1d3
    style GCS fill:#95e1d3
```

### Log Configuration

**File**: `airflow.cfg` section `[logging]`

```ini
[logging]
base_log_folder = /opt/airflow/logs
remote_logging = True
remote_log_conn_id = aws_s3_logs
remote_base_log_folder = s3://my-bucket/airflow-logs

# Log format
log_format = [%%(asctime)s] {%%(filename)s:%%(lineno)d} %%(levelname)s - %%(message)s
log_format_with_prefix = [%%(asctime)s] {%%(filename)s:%%(lineno)d} %%(levelname)s - %%(message)s

# Log level
logging_level = INFO
fab_logging_level = WARNING

# Task log template
log_filename_template = {{ ti.dag_id }}/{{ ti.task_id }}/{{ ts }}/{{ try_number }}.log
```

### Log File Structure

**Local log path**:
```
/opt/airflow/logs/
└── dag_id/
    └── task_id/
        └── 2024-01-01T00:00:00+00:00/
            ├── 1.log  # Try 1
            ├── 2.log  # Try 2 (if retry)
            └── 3.log  # Try 3 (if retry)
```

**Log content**:
```
[2024-01-01 00:00:00,123] {taskinstance.py:1234} INFO - Starting attempt 1 of 1
[2024-01-01 00:00:00,125] {taskinstance.py:1250} INFO - Executing <Task(PythonOperator): my_task> on 2024-01-01 00:00:00+00:00
[2024-01-01 00:00:01,234] {python.py:177} INFO - Done. Returned value was: success
[2024-01-01 00:00:01,250] {taskinstance.py:1500} INFO - Marking task as SUCCESS
```

### Logging in Operators

**Use self.log**:
```python
from airflow.models import BaseOperator

class MyOperator(BaseOperator):
    def execute(self, context):
        self.log.info('Starting task execution')
        self.log.debug('Debug information')
        self.log.warning('Warning message')
        
        try:
            result = do_something()
            self.log.info(f'Result: {result}')
        except Exception as e:
            self.log.error(f'Error: {e}', exc_info=True)
            raise
```

**Available log levels**:
- **DEBUG**: Detailed debugging information
- **INFO**: General informational messages
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical errors

### Remote Logging

**S3 configuration**:
```ini
[logging]
remote_logging = True
remote_log_conn_id = aws_s3_logs
remote_base_log_folder = s3://my-bucket/airflow-logs
encrypt_s3_logs = False
```

**Connection** (`aws_s3_logs`):
```json
{
  "conn_type": "aws",
  "extra": {
    "aws_access_key_id": "AKIAIOSFODNN7EXAMPLE",
    "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "region_name": "us-east-1"
  }
}
```

**Log upload flow**:

```mermaid
sequenceDiagram
    participant Task as Task Subprocess
    participant Local as Local Log File
    participant Handler as Remote Log Handler
    participant S3 as S3 Bucket
    
    Task->>Local: Write log messages
    Local->>Local: Buffer in memory
    
    Note over Task,S3: Periodic flush or on task completion
    
    Local->>Handler: Flush logs
    Handler->>Handler: Read log file content
    Handler->>S3: PUT s3://bucket/logs/dag/task/date/try.log
    S3-->>Handler: Upload complete
    
    Note over Task,S3: On log retrieval (UI)
    
    Handler->>S3: GET s3://bucket/logs/dag/task/date/try.log
    S3-->>Handler: Log content
    Handler-->>Task: Display in UI
```

### Metrics and Monitoring

**StatsD metrics** (from tasks):

```python
from airflow.stats import Stats

def execute(self, context):
    # Increment counter
    Stats.incr('my_metric')
    
    # Timing
    with Stats.timer('my_operation'):
        result = do_something()
    
    # Gauge
    Stats.gauge('queue_size', 42)
```

**Celery metrics**:
```bash
# Worker stats
airflow celery inspect stats

# Output:
worker1@hostname:
    total: {'execute_command': 1234}
    pool:
        max-concurrency: 16
        processes: [1001, 1002, 1003, ...]
        timeouts: [600, 600, 600, ...]
```

**Task execution metrics**:
- `scheduler.tasks.executable`: Tasks ready to run
- `executor.queued_tasks`: Tasks in executor queue
- `executor.running_tasks`: Tasks currently running
- `celery.task.success`: Successful task count
- `celery.task.failure`: Failed task count
- `task_instance_duration.<dag_id>.<task_id>`: Task duration

### Health Checks

**Worker health**:
```bash
# Ping workers
airflow celery ping

# Output:
worker1@hostname: OK
worker2@hostname: OK
```

**Broker health** (Redis):
```bash
redis-cli ping
# Output: PONG

redis-cli info replication
redis-cli llen <queue_name>  # Queue length
```

**Database health**:
```bash
airflow db check
# Checks database connectivity and migrations
```


---

## Debugging Guide

### Common Issues and Solutions

#### Issue 1: Task Stuck in QUEUED State

**Symptoms**:
- Task remains QUEUED for extended period
- No logs generated
- Task never starts execution

**Investigation Steps**:

```mermaid
flowchart TD
    Start[Task stuck in QUEUED] --> Check1{Celery workers<br/>running?}
    
    Check1 -->|No| StartWorker[Start celery workers<br/>airflow celery worker]
    Check1 -->|Yes| Check2{Workers consuming<br/>correct queue?}
    
    Check2 -->|No| FixQueue[Update worker queue:<br/>--queue default,high_priority]
    Check2 -->|Yes| Check3{Message in broker?}
    
    Check3 -->|No| CheckExec[Check CeleryExecutor:<br/>Is it running?<br/>Check scheduler logs]
    Check3 -->|Yes| Check4{Worker concurrency<br/>maxed out?}
    
    Check4 -->|Yes| ScaleUp[Scale up workers or<br/>increase concurrency]
    Check4 -->|No| Check5{Broker connection<br/>issues?}
    
    Check5 -->|Yes| FixBroker[Fix broker connection<br/>Check Redis/RabbitMQ]
    Check5 -->|No| CheckLogs[Check worker logs<br/>for errors]
    
    style Start fill:#ffe3e3
    style CheckLogs fill:#ffd93d
```

**Commands**:
```bash
# Check if workers are running
airflow celery ping

# Check active queues
airflow celery inspect active_queues

# Check queue length in broker (Redis)
redis-cli llen celery  # or specific queue name

# Check worker concurrency
airflow celery inspect stats
```

#### Issue 2: Task Fails with Database Connection Error

**Symptoms**:
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) 
failed to connect to database
```

**Causes**:
1. Database connection pool exhausted
2. Database credentials incorrect
3. Network connectivity issues
4. Too many concurrent tasks

**Solutions**:

```ini
[database]
# Increase pool size
sql_alchemy_pool_size = 10      # From 5
sql_alchemy_max_overflow = 20   # From 10

# Reduce task concurrency per worker
[celery]
worker_concurrency = 8  # From 16
```

**Verify configuration**:
```bash
# Test database connection
airflow db check

# Check current connections
SELECT count(*) FROM pg_stat_activity WHERE datname = 'airflow';

# Check max connections
SHOW max_connections;
```

#### Issue 3: XCom Not Found

**Symptoms**:
```
KeyError: 'return_value' not found in XCom
```

**Investigation**:

```mermaid
flowchart TD
    Error[XCom not found] --> Check1{Upstream task<br/>completed?}
    
    Check1 -->|No| WaitUpstream[Wait for upstream<br/>to complete]
    Check1 -->|Yes| Check2{Upstream task<br/>returned value?}
    
    Check2 -->|No| FixReturn[Update upstream task<br/>to return value<br/>or use xcom_push()]
    Check2 -->|Yes| Check3{Using correct<br/>task_ids?}
    
    Check3 -->|No| FixTaskId[Fix task_ids in<br/>xcom_pull()]
    Check3 -->|Yes| Check4{Using correct<br/>run_id?}
    
    Check4 -->|No| FixRunId[Check run_id,<br/>don't hardcode dates]
    Check4 -->|Yes| Check5{Check database<br/>for XCom record}
    
    Check5 --> QueryDB[SELECT * FROM xcom<br/>WHERE dag_id=...<br/>AND task_id=...<br/>AND run_id=...]
    
    QueryDB --> Found{Record exists?}
    Found -->|No| CheckCleanup[Check max_xcom_days<br/>XCom may be deleted]
    Found -->|Yes| CheckKey[Verify key name<br/>default: 'return_value']
    
    style Error fill:#ffe3e3
    style QueryDB fill:#ffd93d
```

**Debug query**:
```sql
-- Check if XCom exists
SELECT 
    dag_id, task_id, run_id, key, 
    timestamp, 
    length(value) as value_size
FROM xcom
WHERE dag_id = 'my_dag'
  AND task_id = 'upstream_task'
ORDER BY timestamp DESC
LIMIT 10;
```

**Fix example**:
```python
# Upstream task - ensure return value
def execute(self, context):
    result = {'key': 'value'}
    return result  # This creates XCom automatically

# Or explicit push
def execute(self, context):
    result = {'key': 'value'}
    context['ti'].xcom_push(key='my_key', value=result)

# Downstream task - pull correctly
def execute(self, context):
    # Pull from specific task
    value = context['ti'].xcom_pull(
        task_ids='upstream_task',
        key='return_value'  # or 'my_key' if custom
    )
```

#### Issue 4: Variable Not Found

**Symptoms**:
```
KeyError: 'Variable api_key does not exist'
```

**Investigation**:

```bash
# List all variables
airflow variables list

# Get specific variable
airflow variables get api_key

# Check in database
SELECT key, is_encrypted FROM variable WHERE key = 'api_key';
```

**Solutions**:

```bash
# Set variable via CLI
airflow variables set api_key 'my-secret-key'

# Set from JSON file
airflow variables import variables.json

# Set in code with default
value = Variable.get('api_key', default_var='default-value')
```

#### Issue 5: Task Timeout

**Symptoms**:
```
celery.exceptions.SoftTimeLimitExceeded
```

**Timeout configuration**:

```mermaid
flowchart TD
    Start[Task starts] --> Exec[Task executes]
    Exec --> Check{Execution time?}
    
    Check -->|< soft_time_limit| Continue[Continue execution]
    Check -->|>= soft_time_limit<br/>< hard_time_limit| Soft[Raise SoftTimeLimitExceeded<br/>SIGTERM sent]
    Check -->|>= hard_time_limit| Hard[Kill process<br/>SIGKILL sent]
    
    Continue --> Success[Task completes]
    
    Soft --> Catch{Exception caught?}
    Catch -->|Yes| Cleanup[Cleanup gracefully]
    Catch -->|No| Failed[Task FAILED]
    
    Cleanup --> Failed
    Hard --> Killed[Task KILLED]
    
    Success --> End([Complete])
    Failed --> End
    Killed --> End
    
    style Soft fill:#ffec99
    style Hard fill:#ffe3e3
    style Success fill:#b2f2bb
```

**Fix**:

```ini
[celery]
# Increase timeout limits
task_soft_time_limit = 1800   # 30 minutes
task_hard_time_limit = 7200   # 2 hours
```

Or per-task:

```python
task = PythonOperator(
    task_id='long_task',
    execution_timeout=timedelta(hours=2),  # Task-specific timeout
    ...
)
```

### Debugging Tools

#### 1. Task Logs

**Access logs**:
```bash
# Via CLI
airflow tasks logs <dag_id> <task_id> <logical_date>

# Via file system
tail -f /opt/airflow/logs/<dag_id>/<task_id>/<date>/<try>.log

# Via API
curl http://airflow:8080/api/v1/dags/<dag_id>/dagRuns/<run_id>/taskInstances/<task_id>/logs/<try_number>
```

#### 2. Task State Inspection

**Query TaskInstance**:
```sql
SELECT 
    task_id,
    state,
    try_number,
    max_tries,
    start_date,
    end_date,
    duration,
    hostname,
    pid,
    queued_dttm,
    executor_config
FROM task_instance
WHERE dag_id = 'my_dag'
  AND run_id = 'manual__2024-01-01T00:00:00'
ORDER BY start_date;
```

#### 3. Celery Inspect Commands

```bash
# Active tasks
airflow celery inspect active

# Scheduled tasks
airflow celery inspect scheduled

# Reserved tasks
airflow celery inspect reserved

# Worker stats
airflow celery inspect stats

# Registered tasks
airflow celery inspect registered

# Query specific worker
airflow celery inspect active --destination worker1@hostname
```

#### 4. Broker Inspection (Redis)

```bash
# Connect to Redis
redis-cli

# List all keys
KEYS *

# Check queue length
LLEN celery       # Default queue
LLEN default      # Named queue

# View queue contents (first 10)
LRANGE celery 0 10

# Check result backend
KEYS celery-task-meta-*
GET celery-task-meta-<task_id>
```

#### 5. Database Queries for Debugging

**Find stuck tasks**:
```sql
-- Tasks in RUNNING state for > 1 hour
SELECT 
    dag_id,
    task_id,
    run_id,
    state,
    start_date,
    EXTRACT(EPOCH FROM (NOW() - start_date))/3600 AS hours_running,
    hostname,
    pid
FROM task_instance
WHERE state = 'running'
  AND start_date < NOW() - INTERVAL '1 hour'
ORDER BY start_date;
```

**Find tasks with retries**:
```sql
SELECT 
    dag_id,
    task_id,
    run_id,
    state,
    try_number,
    max_tries
FROM task_instance
WHERE try_number > 1
  AND dag_id = 'my_dag'
ORDER BY try_number DESC;
```

**Check XCom size**:
```sql
SELECT 
    dag_id,
    task_id,
    key,
    pg_size_pretty(length(value)) AS size,
    timestamp
FROM xcom
ORDER BY length(value) DESC
LIMIT 20;
```

### Performance Optimization

#### 1. Database Connection Pooling

**Optimize pool settings**:
```ini
[database]
sql_alchemy_pool_size = 10
sql_alchemy_max_overflow = 20
sql_alchemy_pool_recycle = 1800
sql_alchemy_pool_pre_ping = True
```

**Monitor connections**:
```sql
SELECT 
    application_name,
    state,
    count(*) 
FROM pg_stat_activity 
WHERE datname = 'airflow'
GROUP BY application_name, state;
```

#### 2. Worker Concurrency Tuning

**Formula**:
```
Total tasks = num_workers * worker_concurrency

DB connections per worker ≈ worker_concurrency * 1.5
Total DB connections = num_workers * worker_concurrency * 1.5

Ensure: Total DB connections < max_connections (PostgreSQL)
```

**Example**:
- 4 workers
- 16 concurrency each
- Total: 64 parallel tasks
- DB connections: ~96 (64 * 1.5)
- PostgreSQL max_connections should be >= 120

#### 3. XCom Best Practices

**DO**:
- Keep XCom values small (<1 MB)
- Use JSON serialization when possible
- Store large data in external storage (S3, GCS)
- Pass references via XCom

**DON'T**:
- Store large DataFrames in XCom
- Store binary files in XCom
- Use XCom for inter-task communication of large datasets

**Example** (good practice):
```python
# Upstream task
def execute(self, context):
    df = pd.read_csv('large_file.csv')
    
    # Save to S3
    s3_path = f's3://bucket/data/{context["run_id"]}.parquet'
    df.to_parquet(s3_path)
    
    # Return S3 path via XCom (small!)
    return {'s3_path': s3_path, 'row_count': len(df)}

# Downstream task
def execute(self, context):
    metadata = context['ti'].xcom_pull(task_ids='upstream')
    
    # Load from S3
    df = pd.read_parquet(metadata['s3_path'])
```

#### 4. Log Volume Management

**Reduce log verbosity**:
```ini
[logging]
logging_level = WARNING  # From INFO
fab_logging_level = ERROR
```

**Log rotation**:
```ini
[logging]
log_rotation_max_bytes = 104857600  # 100 MB
log_rotation_backup_count = 5
```

**Remote logging** (offload to S3):
```ini
[logging]
remote_logging = True
remote_base_log_folder = s3://my-bucket/logs
```

---

## Summary Checklist

### Task Execution Checklist

**Before task runs**:
- ☐ Scheduler is running
- ☐ CeleryExecutor is enabled
- ☐ Celery workers are running
- ☐ Workers consuming correct queues
- ☐ Broker (Redis/RabbitMQ) is accessible
- ☐ Metadata DB is accessible
- ☐ Variables are set
- ☐ Connections are configured

**During task execution**:
- ☐ Task state updates to RUNNING
- ☐ Logs are being written
- ☐ Variables are accessible
- ☐ XComs can be pulled
- ☐ Database queries work
- ☐ No timeout errors

**After task execution**:
- ☐ Task state is SUCCESS/FAILED
- ☐ XCom is pushed (if needed)
- ☐ Logs are uploaded (remote logging)
- ☐ Database connections closed
- ☐ Result reported to scheduler

### Key Files Reference

| Component | File | Key Methods |
|-----------|------|-------------|
| **CeleryExecutor** | `providers/celery/src/airflow/providers/celery/executors/celery_executor.py` | `queue_task_instance()`, `sync()`, `heartbeat()` |
| **TaskInstance** | `airflow-core/src/airflow/models/taskinstance.py` | `_run_raw_task()`, `_execute_task()`, `xcom_push()`, `xcom_pull()` |
| **XCom** | `airflow-core/src/airflow/models/xcom.py` | `set()`, `get_many()` |
| **Variable** | `airflow-core/src/airflow/models/variable.py` | `get()`, `set()` |
| **CLI Task Run** | `airflow-core/src/airflow/cli/commands/task_command.py` | `task_run()` |

### Monitoring Endpoints

**Health checks**:
- Celery workers: `airflow celery ping`
- Database: `airflow db check`
- Broker: `redis-cli ping` or RabbitMQ management UI

**Metrics**:
- Worker stats: `airflow celery inspect stats`
- Active tasks: `airflow celery inspect active`
- Queue length: `redis-cli llen <queue>`

**Logs**:
- Task logs: `/opt/airflow/logs/<dag_id>/<task_id>/<date>/<try>.log`
- Worker logs: `journalctl -u airflow-worker` (systemd)
- Scheduler logs: `/opt/airflow/logs/scheduler/`

---

**Document version**: 1.0  
**Last updated**: 2024  
**For**: Apache Airflow with CeleryExecutor

